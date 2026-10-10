"""Reviewer pass: a second look at the record before it leaves the agent.

Deterministic rules run always and are cheap: they catch the dispositions that
contradict the action log (an unconfirmed write recorded as resolved, a blocked
write never followed by a request for approval, a fraud flag on a case closed
as routine). An optional LLM review can be enabled with LOA_REVIEWER=llm.
"""

from __future__ import annotations

import json
from typing import Any

from .llm import Settings, create_message
from .rulebook import Rulebook
from .schema import ActionStatus, DecisionState, Disposition, Handover, InfoRequest

# Flags that make a self-declared "resolved" implausible. `vulnerability` is
# deliberately absent: the model records it as a watch item on routine cases
# (children + cold month) and escalates itself when it actually bites.
# An injection attempt that was refused is recorded, not escalated: the task may still be routine.
ESCALATING_FLAGS = {"fraud", "safety_hazard", "legal_threat", "prohibited_request"}

REVIEW_SCHEMA = {
    "type": "object",
    "properties": {
        "ok": {"type": "boolean"},
        "issues": {"type": "array", "items": {"type": "string"}},
        "downgrade_to": {"type": "string", "enum": ["none", "needs_info", "escalated"]},
        "handover_question": {"type": "string"},
    },
    "required": ["ok", "issues", "downgrade_to", "handover_question"],
    "additionalProperties": False,
}


class Reviewer:
    def __init__(self, rulebook: Rulebook, *, settings: Settings | None = None, client: Any = None):
        self.rulebook = rulebook
        self.settings = settings
        self.client = client

    async def review(self, state: DecisionState) -> None:
        self.apply_rules(state)
        if self.settings is not None and self.settings.reviewer == "llm" and self.client is not None:
            try:
                await self.llm_review(state)
            except Exception as e:  # noqa: BLE001 - the reviewer must never break the case
                state.reviewer_notes.append(f"llm review skipped: {type(e).__name__}: {e}")

    # ------------------------------------------------------------------ #

    def apply_rules(self, state: DecisionState) -> None:
        notes = state.reviewer_notes
        unconfirmed = [a for a in state.actions if a.status == ActionStatus.unconfirmed]
        blocked = [a for a in state.actions if a.status in (ActionStatus.blocked, ActionStatus.needs_approval)]
        failed_writes = [a for a in state.actions if a.status == ActionStatus.failed and a.tool_class.value == "write"]
        prohibited_blocked = [a for a in blocked if a.gate and (a.gate.verdict.value == "escalate" or any(r.startswith("PRO-") for r in a.gate.rule_ids))]
        emergency_dispatch = [a for a in state.actions if a.status == ActionStatus.completed and a.gate and "CAP-DISPATCH-EMERGENCY" in a.gate.rule_ids]
        approvals_requested = [
            a for a in state.actions
            if a.status == ActionStatus.completed and a.tool.startswith("request_") and "approval" in a.tool
        ]
        human_tasks = [a for a in state.actions if a.status == ActionStatus.completed and "human_task" in a.tool]
        hard_flags = [f for f in state.red_flags if f.kind in ESCALATING_FLAGS]

        if unconfirmed and state.disposition != Disposition.escalated:
            self._downgrade(state, Disposition.escalated, f"{len(unconfirmed)} action(s) have unknown outcome (unconfirmed); a human must verify before any retry.", [f"{a.tool} is unconfirmed (key {a.idempotency_key})" for a in unconfirmed])
            notes.append("R1: unconfirmed write → escalated")

        # Mandatory escalations run before any rule that can turn a case into needs_info, so they cannot be masked.
        if hard_flags and state.disposition != Disposition.escalated:
            kinds = ", ".join(sorted({f.kind for f in hard_flags}))
            detail = "; ".join(f"{f.kind}: {f.description}" for f in hard_flags[:3])
            was = state.disposition.value if state.disposition else "unset"
            self._downgrade(state, Disposition.escalated, f"The record carries red flags that need a human's confirmation ({detail}); the case cannot end as {was}.", [f.description for f in hard_flags][:5])
            notes.append(f"R2: red flags ({kinds}) → escalated (checked before any needs_info rule)")

        if prohibited_blocked and state.disposition != Disposition.escalated:
            names = ", ".join(sorted({a.tool for a in prohibited_blocked}))
            self._downgrade(state, Disposition.escalated, f"The agent attempted a prohibited action ({names}); the gate blocked it and a person must review the request.", [f"{a.tool}: {', '.join(a.gate.rule_ids)}" for a in prohibited_blocked][:5])
            notes.append("R3a: prohibited action attempted and blocked → escalated")

        if emergency_dispatch and state.disposition != Disposition.escalated:
            self._downgrade(state, Disposition.escalated, "An emergency dispatch was made on the agent's own urgency assessment; a person confirms the emergency, the contractor and the spend.", [f"{a.tool} under CAP-DISPATCH-EMERGENCY (action {a.seq})" for a in emergency_dispatch][:5])
            notes.append("R9: emergency dispatch → escalated for human confirmation")

        dispatched = [a for a in state.actions if a.status == ActionStatus.completed and a.tool_class.value == "write" and (a.gate and any(r.startswith("CAP-DISPATCH") for r in a.gate.rule_ids))]
        if state.disposition == Disposition.resolved and approvals_requested and blocked and not dispatched:
            who = next((a.gate.required_approval_from for a in blocked if a.gate and a.gate.required_approval_from), "landlord") or "landlord"
            state.disposition = Disposition.needs_info
            if not state.info_requests:
                subject = ", ".join(sorted({a.tool for a in blocked}))
                state.info_requests = [InfoRequest(to=who, question=f"Approval requested for: {subject}. Confirm or decline so the job can proceed.", why="The agent asked for approval and is waiting; the case is not resolved until the answer arrives.", blocking=True)]
            notes.append("R7: approval requested and pending → needs_info")

        if state.disposition == Disposition.resolved and any(f.kind == "injection" for f in state.red_flags):
            notes.append("R2: injection attempt recorded; the case completed within the mandate and was not escalated for it")

        if state.disposition == Disposition.resolved and (blocked or failed_writes) and not approvals_requested and not human_tasks:
            who = next((a.gate.required_approval_from for a in blocked if a.gate and a.gate.required_approval_from), "property_manager") or "property_manager"
            state.disposition = Disposition.needs_info
            if not state.info_requests:
                names = ", ".join(sorted({a.tool for a in blocked + failed_writes}))
                why = "The policy gate blocked these actions and no approval was requested." if blocked else "These writes failed in the environment; the work they describe did not happen."
                state.info_requests = [InfoRequest(to=who, question=f"Approval or a decision is needed for: {names}", why=why, blocking=True)]
            notes.append("R3: resolved with blocked or failed writes and no approval request → needs_info")

        on_hold = [a for a in state.actions if a.status == ActionStatus.completed and "hold" in a.tool]
        if state.disposition == Disposition.resolved and (state.hold_reason or state.stage == "on_hold" or on_hold):
            who = _hold_party(state.hold_reason) or "property_manager"
            state.disposition = Disposition.needs_info
            if not state.info_requests:
                question = state.next_step or state.hold_reason or "Confirm the next step so the case can proceed."
                state.info_requests = [InfoRequest(to=who, question=question, why="The case is on hold waiting for this party; it is not resolved until they answer.", blocking=True)]
            notes.append("R8: resolved while on hold → needs_info")

        closed_stages = {"closed", "closed_without_payment", "closed_by_supervisor"}
        pending_dod = [d for d in state.definition_of_done if d.status == "pending"]
        if state.disposition == Disposition.resolved and pending_dod and state.stage not in closed_stages:
            first = pending_dod[0]
            state.disposition = Disposition.needs_info
            if not state.info_requests:
                state.info_requests = [InfoRequest(to="property_manager", question=f"The workflow is not complete: {first.text or first.item} ({len(pending_dod)} checklist item(s) pending). Confirm the next step.", why="A case is resolved only when its definition of done is complete or the ticket is closed.", blocking=True)]
            notes.append(f"R10: resolved with {len(pending_dod)} checklist item(s) pending and the ticket not closed → needs_info")

        if state.disposition == Disposition.escalated and state.handover is None:
            state.handover = Handover(to="property_manager", question=f"Decide the next action on case {state.case_id}.", summary=[f.statement for f in state.facts][:5], gap="Agent escalated without a handover card.", default_if_timeout="Case stays open in the human queue.")
            notes.append("R4: escalated without handover → minimal card built")

        if state.disposition == Disposition.needs_info and not state.info_requests:
            self._downgrade(state, Disposition.escalated, "Case marked needs_info without a concrete question.", [])
            notes.append("R5: needs_info without a question → escalated")

        if state.handover is not None and len(state.handover.summary) > 5:
            state.handover.summary = state.handover.summary[:5]
            notes.append("R6: handover summary trimmed to five facts")

        if unconfirmed and state.handover is not None:
            names = ", ".join(f"{a.tool} (key {a.idempotency_key})" for a in unconfirmed)
            if not all((a.idempotency_key or a.tool) in state.handover.gap for a in unconfirmed):
                state.handover.gap = (state.handover.gap + " " if state.handover.gap else "") + f"Unconfirmed actions: {names}."

    @staticmethod
    def _downgrade(state: DecisionState, to: Disposition, reason: str, facts: list[str]) -> None:
        state.disposition = to
        if to == Disposition.escalated:
            existing = state.handover
            state.handover = Handover(
                to=existing.to if existing else "property_manager",
                question=(existing.question if existing else f"Review case {state.case_id}: {reason}"),
                summary=(existing.summary if existing and existing.summary else (facts or [f.statement for f in state.facts][:5]))[:5],
                gap=reason if not existing else (existing.gap + " " + reason).strip(),
                options=existing.options if existing else [],
                recommended=existing.recommended if existing else None,
                default_if_timeout=(existing.default_if_timeout if existing else "Case stays open in the human queue; no automated action."),
                deadline=existing.deadline if existing else None,
                undo=existing.undo if existing else None,
                context_refs=existing.context_refs if existing else [],
            )

    # ------------------------------------------------------------------ #

    async def llm_review(self, state: DecisionState) -> None:
        assert self.settings is not None and self.client is not None
        record = {
            "disposition": state.disposition.value if state.disposition else None,
            "decision": state.decision,
            "urgency": state.urgency,
            "actions": [{"tool": a.tool, "status": a.status.value, "gate": (a.gate.rule_ids if a.gate else [])} for a in state.actions],
            "red_flags": [f.model_dump() for f in state.red_flags],
            "authority_citations": state.authority_citations,
            "handover": state.handover.model_dump() if state.handover else None,
            "info_requests": [i.model_dump() for i in state.info_requests],
        }
        prompt = (
            "You are the reviewer of an operations agent's case record. Check the record against the mandate: "
            "is the disposition consistent with the actions and flags, is any prohibited action present, is the handover actionable? "
            "Answer with JSON only.\n\nMANDATE\n" + self.rulebook.render_for_prompt() + "\n\nRECORD\n" + json.dumps(record, ensure_ascii=False, indent=1)
        )
        response = await create_message(
            self.client,
            self.settings,
            system=[{"type": "text", "text": "You review agent case records for policy consistency. Be strict and brief."}],
            messages=[{"role": "user", "content": prompt}],
            tools=None,
            max_tokens=2000,
            output_config={"format": {"type": "json_schema", "schema": REVIEW_SCHEMA}},
        )
        text = next((b.text for b in response.content if getattr(b, "type", None) == "text"), "{}")
        verdict = json.loads(text)
        state.reviewer_notes.append("llm: " + ("ok" if verdict.get("ok") else "; ".join(verdict.get("issues", [])) or "issues"))
        if not verdict.get("ok") and verdict.get("downgrade_to") in ("needs_info", "escalated"):
            target = Disposition(verdict["downgrade_to"])
            if target == Disposition.escalated:
                self._downgrade(state, target, verdict.get("handover_question") or "Reviewer requested human review.", verdict.get("issues", []))
            elif state.disposition != Disposition.escalated and not state.info_requests:
                state.disposition = target  # an escalation set by the deterministic rules is never softened by the model review
                state.info_requests = [InfoRequest(to="property_manager", question=verdict.get("handover_question") or "Reviewer: clarification needed.", why="; ".join(verdict.get("issues", [])), blocking=True)]


_HOLD_PARTIES = {"landlord": "landlord", "provider": "contractor", "contractor": "contractor", "tenant": "tenant"}


def _hold_party(reason: str) -> str:
    """'Waiting for Provider — …' → 'contractor'; unknown or 'Other' → ''."""
    low = (reason or "").lower()
    for key, who in _HOLD_PARTIES.items():
        if f"waiting for {key}" in low or low.startswith(key):
            return who
    return ""
