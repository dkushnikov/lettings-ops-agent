"""Policy gate: deny-by-default wrapper on the tool boundary.

The model proposes; the gate decides. Reads pass. Writes are checked against
the rulebook with the current urgency and the amount carried by the tool input.
The verdict and the cited rule ids go into the action record, so the judge can
see why an action happened or did not.
"""

from __future__ import annotations

from typing import Any

from .rulebook import Rulebook
from .schema import GateDecision, GateVerdict, ToolClass, ToolSpec


class PolicyGate:
    def __init__(self, rulebook: Rulebook):
        self.rulebook = rulebook

    def check(self, spec: ToolSpec, tool_input: dict[str, Any], *, urgency: str, context: dict[str, Any] | None = None) -> GateDecision:
        if spec.tool_class == ToolClass.read:
            return GateDecision(verdict=GateVerdict.allow, reason="read")
        amount = self._amount(spec, tool_input)
        return self.rulebook.evaluate(spec.authority, tool_input, amount_gbp=amount, urgency=urgency, context=context)

    @staticmethod
    def _amount(spec: ToolSpec, tool_input: dict[str, Any]) -> float | None:
        if not spec.amount_field:
            return None
        value = tool_input.get(spec.amount_field)
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None


def explain(decision: GateDecision) -> str:
    """One line for the tool_result the model receives when a write is stopped."""
    ids = ", ".join(decision.rule_ids) if decision.rule_ids else "no rule"
    if decision.verdict == GateVerdict.needs_approval:
        who = decision.required_approval_from or "a human"
        return (
            f"BLOCKED by policy gate ({ids}): {decision.reason} "
            f"This action needs approval from {who}. Use request_approval-type tools "
            f"or finish with request_info / escalate; do not retry the same call."
        )
    if decision.verdict == GateVerdict.escalate:
        return (
            f"PROHIBITED ({ids}): {decision.reason} This must go to a human. "
            f"Record a red flag and finish with escalate."
        )
    if decision.verdict == GateVerdict.deny:
        return f"PROHIBITED ({ids}): {decision.reason} Do not attempt this action."
    return f"ALLOWED ({ids})"
