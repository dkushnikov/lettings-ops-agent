"""Batch runner: every case gets a record, whatever happens.

Concurrency with a semaphore, a per-case timeout, a small retry budget for
transient failures, checkpoints so a crashed run resumes without redoing
finished cases, and a fallback record (escalated, with context) when the agent
cannot finish. Prints a capacity estimate before starting so the 30-minute
window is a plan, not a hope.
"""

from __future__ import annotations

import asyncio
import math
import random
import subprocess
import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.progress import BarColumn, Progress, TextColumn, TimeElapsedColumn
from rich.table import Table

from .llm import Settings, is_transient_error
from .loop import CaseAgent
from .recorder import TraceWriter, read_state, write_case_outputs, write_run_meta
from .sanitize import truncate
from .schema import ActionStatus, Case, DecisionState, Disposition, Handover, RunMeta, utcnow
from .tools import EnvironmentAdapter

console = Console()


def fallback_state(case: Case, reason: str, model: str) -> DecisionState:
    state = DecisionState(case_id=case.id, model=model, fallback=True)
    state.system_notes.append(f"harness fallback: {reason}")
    state.disposition = Disposition.escalated
    state.decision = f"Escalated by the harness: {reason}. No autonomous resolution was recorded."
    state.handover = Handover(
        to="property_manager",
        question=f"The agent could not process case {case.id} ({reason}). Review the artefacts and decide the next action.",
        summary=[case.title or "See artefacts."],
        gap=reason,
        options=["Handle manually", "Re-run the agent once the blocker is fixed"],
        default_if_timeout="Case stays open in the human queue; no automated action.",
        context_refs=[a.id for a in case.artefacts][:10],
    )
    state.finished_at = utcnow()
    return state


def estimate_wall_seconds(n_cases: int, concurrency: int, t_case_s: float, margin: float = 1.25) -> float:
    if n_cases <= 0:
        return 0.0
    return math.ceil(n_cases / max(1, concurrency)) * t_case_s * margin


def previous_t_case(out_dir: Path, default: float = 90.0) -> float:
    p = out_dir / "_run.json"
    if not p.exists():
        return default
    try:
        meta = RunMeta.model_validate_json(p.read_text(encoding="utf-8"))
        if meta.actual_wall_s and meta.completed:
            return max(10.0, meta.actual_wall_s * meta.concurrency / meta.completed)
    except Exception:  # noqa: BLE001
        pass
    return default


def _workflow_completed(state: DecisionState) -> bool:
    if state.fallback or state.disposition is None:
        return False
    if state.disposition == Disposition.resolved:
        return state.completed_writes >= 1 or not any(a.tool_class.value == "write" for a in state.actions)
    if state.disposition == Disposition.escalated:
        return state.handover is not None and bool(state.handover.question)
    return bool(state.info_requests)


async def run_batch(
    cases: list[Case],
    adapter: EnvironmentAdapter,
    agent: CaseAgent,
    settings: Settings,
    out_dir: Path,
    *,
    force: bool = False,
    deadline: datetime | None = None,
    progress: bool = True,
) -> RunMeta:
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = RunMeta(
        run_id=uuid.uuid4().hex[:8],
        model=settings.model,
        effort=settings.effort,
        concurrency=settings.concurrency,
        case_timeout_s=settings.case_timeout_s,
        max_steps=settings.max_steps,
        cases_total=len(cases),
        **_git_commit(),
    )
    t_case = previous_t_case(out_dir)
    est = estimate_wall_seconds(len(cases), settings.concurrency, t_case)
    meta.estimated_wall_s = est
    console.print(
        f"[bold]Batch[/bold] {meta.run_id}: {len(cases)} cases · concurrency {settings.concurrency} · "
        f"t_case≈{t_case:.0f}s → estimated wall {est/60:.1f} min · model {settings.model} · effort {settings.effort}"
    )
    if deadline:
        console.print(f"Deadline {deadline.isoformat(timespec='minutes')}: cases not started by then get a fallback record.")

    sem = asyncio.Semaphore(max(1, settings.concurrency))
    started = time.monotonic()
    results: dict[str, DecisionState] = {}
    skipped = 0

    prog = Progress(TextColumn("[progress.description]{task.description}"), BarColumn(), TextColumn("{task.completed}/{task.total}"), TimeElapsedColumn(), console=console, disable=not progress)
    task_id = prog.add_task("cases", total=len(cases))

    async def one(case: Case) -> None:
        nonlocal skipped
        async with sem:
            case_dir = out_dir / case.id
            if not force:
                prev = read_state(case_dir)
                if prev is not None and prev.terminal_valid() and not prev.fallback:
                    results[case.id] = prev
                    skipped += 1
                    prog.advance(task_id)
                    return
            if deadline and datetime.now(deadline.tzinfo) > deadline:
                state = fallback_state(case, "not started: run deadline passed", settings.model)
                write_case_outputs(out_dir, case, state)
                results[case.id] = state
                prog.advance(task_id)
                return
            trace = TraceWriter(case_dir / "trace.jsonl")
            attempts = 0
            state: DecisionState | None = None
            while state is None:
                attempts += 1
                registry = adapter.tools_for(case)
                adapter.reset(case)
                holder: dict[str, Any] = {}
                try:
                    state = await asyncio.wait_for(agent.run(case, registry, trace=trace, holder=holder), timeout=settings.case_timeout_s)
                except asyncio.TimeoutError:
                    reason = f"case timed out after {settings.case_timeout_s:.0f}s"
                    retryable = False
                    partial = holder.get("state")
                    if partial is not None and (partial.actions or partial.facts or partial.playbook):
                        # Keep what the agent established and did; the record says the runtime cut it short.
                        agent._fallback(partial, case, reason + "; an action may have been in flight when the case was cancelled")  # noqa: SLF001
                        await agent.reviewer.review(partial)
                        partial.finished_at = utcnow()
                        meta.failures.append(f"{case.id}: {reason}")
                        trace({"event": "case_error", "attempt": attempts, "reason": reason, "retryable": False, "partial_state": True})
                        state = partial
                        break
                except Exception as e:  # noqa: BLE001
                    reason = f"{type(e).__name__}: {truncate(str(e), 200)}"
                    retryable = is_transient_error(e)
                else:
                    break
                trace({"event": "case_error", "attempt": attempts, "reason": reason, "retryable": retryable})
                if retryable and attempts <= settings.retry_budget:
                    # Exponential backoff with jitter so concurrent cases do not retry in lockstep.
                    await asyncio.sleep(min(2.0 * attempts, 8.0) + random.uniform(0.0, 1.5))
                    continue
                meta.failures.append(f"{case.id}: {reason}")
                state = fallback_state(case, reason, settings.model)
            write_case_outputs(out_dir, case, state, trace.events)
            trace.close()
            results[case.id] = state
            prog.advance(task_id)

    with prog:
        await asyncio.gather(*(one(c) for c in cases))

    meta.actual_wall_s = time.monotonic() - started
    meta.finished_at = utcnow()
    for st in results.values():
        meta.completed += 1
        if st.fallback:
            meta.fallback_count += 1
        if st.disposition == Disposition.resolved:
            meta.resolved += 1
        elif st.disposition == Disposition.needs_info:
            meta.needs_info += 1
        elif st.disposition == Disposition.escalated:
            meta.escalated += 1
        meta.input_tokens += st.input_tokens
        meta.output_tokens += st.output_tokens
        meta.cache_read_tokens += st.cache_read_tokens
    if skipped:
        meta.notes.append(f"{skipped} case(s) reused from checkpoint")
    write_run_meta(out_dir, meta)
    print_summary(results, meta)
    return meta


def _git_commit() -> dict[str, Any]:
    """Short hash of HEAD and whether tracked files are modified, for the run record; empty outside a checkout."""
    root = Path(__file__).resolve().parent.parent
    try:
        sha = subprocess.run(["git", "-C", str(root), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, timeout=5)
        if sha.returncode != 0:
            return {}
        status = subprocess.run(["git", "-C", str(root), "status", "--porcelain", "--untracked-files=no"], capture_output=True, text=True, timeout=5)
        return {"commit": sha.stdout.strip(), "dirty": bool(status.stdout.strip())}
    except Exception:  # noqa: BLE001
        return {}


def print_summary(results: dict[str, DecisionState], meta: RunMeta) -> None:
    table = Table(title=f"Run {meta.run_id} — {meta.completed}/{meta.cases_total} cases · {meta.actual_wall_s or 0:.0f}s")
    table.add_column("Case")
    table.add_column("Disposition")
    table.add_column("Urgency")
    table.add_column("Steps", justify="right")
    table.add_column("Writes ok", justify="right")
    table.add_column("Unconf.", justify="right")
    table.add_column("Flags", justify="right")
    table.add_column("Fallback")
    artefact_ok = valid_terminal = workflow_ok = 0
    for cid, st in sorted(results.items()):
        unconf = sum(1 for a in st.actions if a.status == ActionStatus.unconfirmed)
        table.add_row(cid, st.disposition.value if st.disposition else "-", st.urgency, str(st.steps), str(st.completed_writes), str(unconf), str(len(st.red_flags)), "yes" if st.fallback else "")
        artefact_ok += 1
        valid_terminal += int(st.terminal_valid() and not st.fallback)
        workflow_ok += int(_workflow_completed(st))
    console.print(table)
    n = max(1, len(results))
    console.print(
        f"[bold]Three metrics[/bold] — records present: {artefact_ok}/{n} · valid terminal decision: {valid_terminal}/{n} · "
        f"workflow completed: {workflow_ok}/{n} · fallbacks: {meta.fallback_count} · tokens in/out: {meta.input_tokens}/{meta.output_tokens} (cache {meta.cache_read_tokens})"
    )
    if meta.failures:
        console.print("[yellow]Failures:[/yellow] " + "; ".join(meta.failures[:10]))
