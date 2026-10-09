"""ActionExecutor: the only path from the model's intent to a side effect.

Reads may be retried. Writes are different: a retry can duplicate a booking or
a message, so a write is sent once with an idempotency key; if the response is
lost the executor reconciles through a read-back tool when one exists and
otherwise records the action as *unconfirmed* and leaves it to a human.
"""

from __future__ import annotations

import hashlib
import inspect
import json
from typing import Any, Callable

from .gate import PolicyGate, explain
from .sanitize import jsonable, truncate
from .schema import ActionRecord, ActionStatus, GateVerdict, ToolClass, utcnow
from .tools import LostResponseError, ToolRegistry, ToolRejected, TransientToolError

TraceFn = Callable[[dict[str, Any]], None]


def idempotency_key(case_id: str, tool: str, tool_input: dict[str, Any]) -> str:
    canonical = json.dumps(jsonable(tool_input), sort_keys=True, ensure_ascii=False)
    digest = hashlib.sha256(f"{case_id}|{tool}|{canonical}".encode("utf-8")).hexdigest()
    return f"{case_id}-{tool}-{digest[:12]}"


def _accepts_kwarg(fn: Callable[..., Any], name: str) -> bool:
    try:
        sig = inspect.signature(fn)
    except (TypeError, ValueError):
        return False
    for p in sig.parameters.values():
        if p.kind == inspect.Parameter.VAR_KEYWORD or p.name == name:
            return True
    return False


def receipt_of(result: Any) -> str:
    data = jsonable(result)
    if isinstance(data, dict):
        ids = {k: v for k, v in data.items() if isinstance(v, (str, int)) and ("id" in k.lower() or k.lower() in {"status", "state"})}
        if ids:
            return truncate(json.dumps(ids, ensure_ascii=False), 200)
    return truncate(json.dumps(data, ensure_ascii=False, default=str), 200)


class ActionExecutor:
    def __init__(
        self,
        registry: ToolRegistry,
        gate: PolicyGate,
        *,
        case_id: str,
        read_retries: int = 2,
        trace: TraceFn | None = None,
    ):
        self.registry = registry
        self.gate = gate
        self.case_id = case_id
        self.read_retries = read_retries
        self.trace = trace or (lambda e: None)
        # Facts harvested from authoritative reads that the mandate refers to
        # (the landlord's own spend cap, an always-ask instruction).
        self.context: dict[str, Any] = {}
        self._context_keys = list(getattr(gate.rulebook, "context_keys", []) or [])

    def _harvest(self, result: Any) -> None:
        data = jsonable(result)
        candidates = []
        if isinstance(data, dict):
            candidates.append(data)
            candidates += [v for v in data.values() if isinstance(v, dict)]
        elif isinstance(data, list):
            candidates += [v for v in data if isinstance(v, dict)]
        for d in candidates:
            for k in self._context_keys:
                if k in d and d[k] is not None:
                    if self.context.get(k) != d[k]:
                        self.trace({"event": "context", "key": k, "value": d[k]})
                    self.context[k] = d[k]

    async def execute(self, name: str, tool_input: dict[str, Any], *, urgency: str, seq: int) -> ActionRecord:
        tool = self.registry.get(name)
        if tool is None:
            rec = ActionRecord(seq=seq, tool=name, tool_class=ToolClass.read, input=tool_input, status=ActionStatus.failed, error="unknown tool")
            self.trace({"event": "tool_unknown", "tool": name})
            return rec

        spec = tool.spec
        decision = self.gate.check(spec, tool_input, urgency=urgency, context=self.context)
        rec = ActionRecord(seq=seq, tool=name, tool_class=spec.tool_class, input=jsonable(tool_input), gate=decision, started_at=utcnow())
        self.trace({"event": "gate", "tool": name, "verdict": decision.verdict.value, "rules": decision.rule_ids, "reason": decision.reason})

        if decision.verdict != GateVerdict.allow:
            rec.status = ActionStatus.needs_approval if decision.verdict == GateVerdict.needs_approval else ActionStatus.blocked
            rec.error = explain(decision)
            rec.finished_at = utcnow()
            return rec

        if spec.tool_class == ToolClass.read:
            await self._run_read(tool, tool_input, rec)
        else:
            await self._run_write(tool, tool_input, rec)
        rec.finished_at = utcnow()
        self.trace({"event": "tool_result", "tool": name, "status": rec.status.value, "attempts": rec.attempts, "error": rec.error, "receipt": rec.receipt})
        return rec

    async def _run_read(self, tool, tool_input: dict[str, Any], rec: ActionRecord) -> None:
        last_error: str | None = None
        for attempt in range(1 + self.read_retries):
            rec.attempts = attempt + 1
            try:
                result = await tool.call(**tool_input)
            except (TransientToolError, LostResponseError) as e:
                last_error = f"{type(e).__name__}: {e}"
                continue
            except ToolRejected as e:
                rec.status = ActionStatus.failed
                rec.error = f"rejected: {e}"
                return
            except Exception as e:  # noqa: BLE001 - a tool must never crash the case
                rec.status = ActionStatus.failed
                rec.error = f"{type(e).__name__}: {e}"
                return
            rec.status = ActionStatus.completed
            rec.result = jsonable(result)
            rec.receipt = receipt_of(result)
            self._harvest(result)
            return
        rec.status = ActionStatus.failed
        rec.error = f"transient failure after {rec.attempts} attempts: {last_error}"

    async def _run_write(self, tool, tool_input: dict[str, Any], rec: ActionRecord) -> None:
        key = idempotency_key(self.case_id, tool.spec.name, tool_input)
        rec.idempotency_key = key
        kwargs = dict(tool_input)
        if _accepts_kwarg(tool.fn, "idempotency_key"):
            kwargs["idempotency_key"] = key

        max_attempts = 2 if tool.spec.idempotent else 1
        for attempt in range(max_attempts):
            rec.attempts = attempt + 1
            rec.status = ActionStatus.attempted
            try:
                result = await tool.call(**kwargs)
            except TransientToolError as e:
                rec.error = f"transient: {e}"
                if tool.spec.idempotent and attempt + 1 < max_attempts:
                    continue
                # Not safe to resend: find out what happened, or leave it to a human.
                await self._reconcile_or_unconfirm(tool, tool_input, rec)
                return
            except LostResponseError as e:
                rec.error = f"lost response: {e}"
                await self._reconcile_or_unconfirm(tool, tool_input, rec)
                return
            except ToolRejected as e:
                rec.status = ActionStatus.failed
                rec.error = f"rejected: {e}"
                return
            except Exception as e:  # noqa: BLE001
                rec.status = ActionStatus.failed
                rec.error = f"{type(e).__name__}: {e}"
                return
            rec.status = ActionStatus.completed
            rec.result = jsonable(result)
            rec.receipt = receipt_of(result)
            rec.error = None
            return

    async def _reconcile_or_unconfirm(self, tool, tool_input: dict[str, Any], rec: ActionRecord) -> None:
        if tool.reconcile is not None:
            try:
                existing = await tool.reconcile_call(tool_input)
            except Exception as e:  # noqa: BLE001
                existing = None
                rec.error = (rec.error or "") + f"; reconcile failed: {e}"
            if existing:
                rec.status = ActionStatus.completed
                rec.result = jsonable(existing)
                rec.receipt = receipt_of(existing) + " (confirmed by read-back)"
                self.trace({"event": "reconciled", "tool": tool.spec.name})
                return
        rec.status = ActionStatus.unconfirmed
        rec.error = (rec.error or "") + "; outcome unknown — not retried, human must verify before anyone resends"
