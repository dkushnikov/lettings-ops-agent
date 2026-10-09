"""Recorder: the trace and the two files a judge reads.

ANSWER.md is the decision (compiled truth, disposition first). REASONING.md is
the evidence-based rationale plus the timeline of what actually happened. Both
are rendered from DecisionState, never written as free prose by the model, so
their layout is identical across cases and untrusted content cannot leak in
verbatim.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .sanitize import jsonable, redact_secrets, truncate
from .schema import ActionRecord, ActionStatus, Case, DecisionState, Disposition, RunMeta


class TraceWriter:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.events: list[dict[str, Any]] = []
        self._fh = self.path.open("a", encoding="utf-8")

    def __call__(self, event: dict[str, Any]) -> None:
        rec = {"ts": datetime.now(timezone.utc).isoformat(timespec="milliseconds"), **jsonable(event)}
        self.events.append(rec)
        self._fh.write(redact_secrets(json.dumps(rec, ensure_ascii=False, default=str)) + "\n")
        self._fh.flush()

    def close(self) -> None:
        try:
            self._fh.close()
        except Exception:  # noqa: BLE001
            pass


def _md_escape(text: Any) -> str:
    s = str(text) if text is not None else ""
    return redact_secrets(s.replace("|", "\\|").replace("\n", " ").strip())


def _status_badge(status: ActionStatus) -> str:
    return {
        ActionStatus.completed: "completed",
        ActionStatus.unconfirmed: "UNCONFIRMED",
        ActionStatus.blocked: "blocked by gate",
        ActionStatus.needs_approval: "needs approval",
        ActionStatus.failed: "failed",
        ActionStatus.attempted: "attempted",
        ActionStatus.proposed: "proposed",
    }[status]


def _key_inputs(a: ActionRecord) -> str:
    keep = {k: v for k, v in a.input.items() if isinstance(v, (str, int, float, bool))}
    text = ", ".join(f"{k}={truncate(str(v), 60)}" for k, v in list(keep.items())[:5])
    return _md_escape(text)


def render_answer(case: Case, state: DecisionState) -> str:
    disp = state.disposition.value.upper() if state.disposition else "UNKNOWN"
    lines: list[str] = []
    lines.append(f"# ANSWER — Case {case.id}" + (f" — {case.title}" if case.title else ""))
    lines.append("")
    lines.append(f"**Disposition:** {disp} · **Urgency:** {state.urgency} · **Case type:** {state.case_type or '-'} · **Playbook:** {state.playbook or '-'}")
    if state.fallback:
        lines.append("")
        lines.append("> Harness fallback: the agent did not finish on its own; this record was escalated by the runtime. See System notes.")
    lines.append("")
    lines.append("## 1. Decision")
    lines.append("")
    lines.append(redact_secrets(state.decision or "(no decision text)"))
    if state.safety_actions:
        lines.append("")
        lines.append("Safety actions taken first:")
        lines += [f"- {redact_secrets(s)}" for s in state.safety_actions]
    if state.withheld_actions:
        lines.append("")
        lines.append("Actions deliberately withheld:")
        lines += [f"- {redact_secrets(s)}" for s in state.withheld_actions]
    lines.append("")
    lines.append("## 2. Authority and evidence")
    lines.append("")
    cites = ", ".join(state.authority_citations) or "(none cited)"
    lines.append(f"Authority cited: {cites}")
    gate_rules = sorted({r for a in state.actions if a.gate for r in a.gate.rule_ids})
    if gate_rules:
        lines.append(f"Rules applied by the policy gate: {', '.join(gate_rules)}")
    lines.append("")
    lines.append("Key facts (source ids in brackets):")
    if state.facts:
        for f in state.facts[:12]:
            src = ", ".join(f.source_ids) or "-"
            lines.append(f"- {f.id}: {redact_secrets(f.statement)} [{src}; {f.confidence}]")
    else:
        lines.append("- (no facts recorded)")
    if state.conflicts:
        lines.append("")
        lines.append("Conflicts between sources:")
        for c in state.conflicts:
            res = c.resolution or "unresolved"
            lines.append(f"- {redact_secrets(c.description)} → {res} ({c.resolved_by})")
    if state.red_flags:
        lines.append("")
        lines.append("Red flags:")
        for r in state.red_flags:
            lines.append(f"- [{r.kind}] {redact_secrets(r.description)} → {redact_secrets(r.action_taken) or 'noted'}")
    lines.append("")
    lines.append("## 3. Actions (proposed → attempted → completed)")
    lines.append("")
    if state.actions:
        lines.append("| # | Tool | Status | Key inputs | Result / receipt | Gate |")
        lines.append("|---|---|---|---|---|---|")
        for a in state.actions:
            gate = ", ".join(a.gate.rule_ids) if a.gate and a.gate.rule_ids else (a.gate.verdict.value if a.gate else "-")
            receipt = a.receipt or (a.error or "")
            lines.append(f"| {a.seq} | {a.tool} | {_status_badge(a.status)} | {_key_inputs(a)} | {_md_escape(truncate(receipt, 160))} | {_md_escape(gate)} |")
    else:
        lines.append("No tool actions were taken.")
    lines.append("")
    lines.append("## 4. Human handover / information requested")
    lines.append("")
    if state.disposition == Disposition.escalated and state.handover:
        h = state.handover
        lines.append(f"**To:** {h.to}")
        lines.append(f"**Question:** {redact_secrets(h.question)}")
        if h.summary:
            lines.append("**Facts (≤5):**")
            lines += [f"- {redact_secrets(s)}" for s in h.summary[:5]]
        if h.gap:
            lines.append(f"**Gap:** {redact_secrets(h.gap)}")
        if h.options:
            lines.append("**Options:**")
            lines += [f"- {redact_secrets(o)}" for o in h.options]
        if h.recommended:
            lines.append(f"**Recommended:** {redact_secrets(h.recommended)}")
        if h.default_if_timeout:
            lines.append(f"**Default if no answer:** {redact_secrets(h.default_if_timeout)}")
        if h.deadline:
            lines.append(f"**Deadline:** {h.deadline}")
        if h.undo:
            lines.append(f"**Undo:** {redact_secrets(h.undo)}")
        if h.context_refs:
            lines.append(f"**Context:** {', '.join(h.context_refs)}")
    elif state.disposition == Disposition.needs_info and state.info_requests:
        for r in state.info_requests:
            blocking = "blocking" if r.blocking else "non-blocking"
            lines.append(f"- Ask **{r.to}**: {redact_secrets(r.question)} ({blocking}; {redact_secrets(r.why)})")
    else:
        lines.append("No human action needed.")
    if state.promises:
        lines.append("")
        lines.append("Promises made or recorded:")
        for p in state.promises:
            due = f" by {p.due}" if p.due else ""
            lines.append(f"- {p.by} → {p.to}: {redact_secrets(p.what)}{due} [{p.status}]")
    if state.clocks:
        lines.append("")
        lines.append("Clocks:")
        for c in state.clocks:
            dl = f" deadline {c.deadline}" if c.deadline else ""
            lines.append(f"- {c.rule_id} [{c.status}]: {c.name}{dl}")
    if state.system_notes or state.reviewer_notes:
        lines.append("")
        lines.append("## System notes")
        lines.append("")
        lines += [f"- {redact_secrets(n)}" for n in state.system_notes]
        lines += [f"- reviewer: {redact_secrets(n)}" for n in state.reviewer_notes]
    lines.append("")
    return "\n".join(lines)


def render_reasoning(case: Case, state: DecisionState, events: list[dict[str, Any]] | None = None) -> str:
    lines: list[str] = []
    lines.append(f"# REASONING — Case {case.id}")
    lines.append("")
    lines.append("## Compiled truth")
    lines.append("")
    lines.append(f"- Case type: {state.case_type or '-'}; urgency: {state.urgency}; playbook: {state.playbook or '-'}")
    lines.append("- Received artefacts: " + ", ".join(f"{a.id} ({a.kind.value}, {a.trust})" for a in case.artefacts))
    lines.append("")
    lines.append("Facts and their sources:")
    for f in state.facts or []:
        lines.append(f"- {f.id} [{f.confidence}] {redact_secrets(f.statement)} ← {', '.join(f.source_ids) or 'unsourced'}")
    if not state.facts:
        lines.append("- (none recorded)")
    if state.conflicts:
        lines.append("")
        lines.append("Conflicts and how they were handled:")
        for c in state.conflicts:
            lines.append(f"- {redact_secrets(c.description)} → {c.resolution or 'unresolved'} ({c.resolved_by}; sources {', '.join(c.source_ids) or '-'})")
    if state.uncertainty:
        lines.append("")
        lines.append("Uncertainty acknowledged:")
        lines += [f"- {redact_secrets(u)}" for u in state.uncertainty]
    if state.assumptions:
        lines.append("")
        lines.append("Assumptions made:")
        lines += [f"- {redact_secrets(a)}" for a in state.assumptions]
    lines.append("")
    lines.append("## Why this disposition")
    lines.append("")
    lines.append(f"Disposition: **{state.disposition.value if state.disposition else 'unknown'}**. {redact_secrets(state.decision)}")
    if state.authority_citations:
        lines.append(f"Authority relied on: {', '.join(state.authority_citations)}.")
    if state.red_flags:
        lines.append("Red flags shaped the decision: " + "; ".join(f"{r.kind}: {redact_secrets(r.description)}" for r in state.red_flags))
    lines.append("")
    lines.append("## Timeline")
    lines.append("")
    if events:
        for e in events:
            ev = e.get("event")
            ts = e.get("ts", "")[11:23]
            if ev == "model_turn":
                lines.append(f"- {ts} model turn {e.get('step')} → {e.get('stop_reason')}")
            elif ev == "playbook":
                lines.append(f"- {ts} playbook {e.get('name')} · type {e.get('case_type')} · urgency {e.get('urgency')}")
            elif ev == "gate":
                lines.append(f"- {ts} gate {e.get('tool')} → {e.get('verdict')} ({', '.join(e.get('rules') or []) or 'read'})")
            elif ev == "tool_result":
                extra = f" · {truncate(str(e.get('error')), 120)}" if e.get("error") else ""
                lines.append(f"- {ts} {e.get('tool')} → {e.get('status')} (attempts {e.get('attempts')}){extra}")
            elif ev == "reconciled":
                lines.append(f"- {ts} reconciled {e.get('tool')} by read-back")
            elif ev == "terminal":
                lines.append(f"- {ts} terminal {e.get('tool')} → {'accepted' if e.get('ok') else 'rejected: ' + truncate(str(e.get('message')), 120)}")
            elif ev == "nudge":
                lines.append(f"- {ts} nudge: model stopped without a terminal call")
            elif ev == "fallback":
                lines.append(f"- {ts} fallback: {e.get('reason')}")
    else:
        for a in state.actions:
            lines.append(f"- {a.seq}. {a.tool} → {a.status.value}")
    lines.append("")
    lines.append(f"Steps used: {state.steps}; tokens in/out: {state.input_tokens}/{state.output_tokens} (cache reads {state.cache_read_tokens}); model: {state.model}.")
    if state.reviewer_notes:
        lines.append("")
        lines.append("## Reviewer notes")
        lines.append("")
        lines += [f"- {redact_secrets(n)}" for n in state.reviewer_notes]
    lines.append("")
    return "\n".join(lines)


def write_case_outputs(out_dir: Path, case: Case, state: DecisionState, events: list[dict[str, Any]] | None = None) -> Path:
    case_dir = out_dir / case.id
    case_dir.mkdir(parents=True, exist_ok=True)
    (case_dir / "ANSWER.md").write_text(render_answer(case, state), encoding="utf-8")
    (case_dir / "REASONING.md").write_text(render_reasoning(case, state, events), encoding="utf-8")
    (case_dir / "_state.json").write_text(redact_secrets(state.model_dump_json(indent=1)), encoding="utf-8")
    return case_dir


def read_state(case_dir: Path) -> DecisionState | None:
    p = case_dir / "_state.json"
    if not p.exists():
        return None
    try:
        return DecisionState.model_validate_json(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def write_run_meta(out_dir: Path, meta: RunMeta) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / "_run.json"
    p.write_text(meta.model_dump_json(indent=1), encoding="utf-8")
    return p
