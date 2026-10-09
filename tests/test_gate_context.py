"""The mandate is per landlord once the executor has read their instructions."""

from pathlib import Path

from harness.executor import ActionExecutor
from harness.gate import PolicyGate
from harness.rulebook import Rulebook
from harness.schema import ActionStatus, GateVerdict, ToolClass
from harness.tools import BoundTool, ToolRegistry, make_spec

ROOT = Path(__file__).resolve().parent.parent

WO = make_spec("create_work_order", "book", {"type": "object", "properties": {"estimated_cost_gbp": {"type": "number"}}}, tool_class=ToolClass.write, authority="dispatch_contractor", amount_field="estimated_cost_gbp", idempotent=True)


def _gate() -> PolicyGate:
    return PolicyGate(Rulebook.load(ROOT / "agent" / "rulebook.yaml"))


def test_landlord_cap_from_context_lowers_the_limit():
    g = _gate()
    assert g.check(WO, {"estimated_cost_gbp": 200}, urgency="routine").verdict == GateVerdict.allow
    d = g.check(WO, {"estimated_cost_gbp": 200}, urgency="routine", context={"spend_cap_gbp": 150})
    assert d.verdict == GateVerdict.needs_approval and "APR-SPEND-OVER-CAP" in d.rule_ids


def test_landlord_cap_from_context_raises_the_limit():
    d = _gate().check(WO, {"estimated_cost_gbp": 400}, urgency="routine", context={"spend_cap_gbp": 500})
    assert d.verdict == GateVerdict.allow and "CAP-DISPATCH-ROUTINE" in d.rule_ids


def test_always_ask_landlord_needs_approval_unless_emergency():
    g = _gate()
    d = g.check(WO, {"estimated_cost_gbp": 50}, urgency="routine", context={"always_ask": True})
    assert d.verdict == GateVerdict.needs_approval and "APR-ALWAYS-ASK" in d.rule_ids
    e = g.check(WO, {"estimated_cost_gbp": 50}, urgency="emergency", context={"always_ask": True})
    assert e.verdict == GateVerdict.allow and "CAP-DISPATCH-EMERGENCY" in e.rule_ids


async def test_executor_harvests_context_from_reads():
    reg = ToolRegistry()

    async def get_landlord_instructions(property_id: str):
        return {"landlord_id": "L-002", "spend_cap_gbp": 150, "always_ask": False, "standing_instructions": "Call me for anything over £150"}

    reg.add(BoundTool(make_spec("get_landlord_instructions", "read", {"type": "object", "properties": {"property_id": {"type": "string"}}}), get_landlord_instructions))

    async def create_work_order(property_id: str, estimated_cost_gbp: float, idempotency_key: str | None = None):
        return {"work_order_id": "WO-1"}

    reg.add(BoundTool(WO, create_work_order))
    ex = ActionExecutor(reg, _gate(), case_id="X")
    first = await ex.execute("create_work_order", {"property_id": "P-002", "estimated_cost_gbp": 200}, urgency="routine", seq=1)
    assert first.status == ActionStatus.completed  # default cap 250 applies before the instructions are read
    await ex.execute("get_landlord_instructions", {"property_id": "P-002"}, urgency="routine", seq=2)
    assert ex.context["spend_cap_gbp"] == 150
    second = await ex.execute("create_work_order", {"property_id": "P-002", "estimated_cost_gbp": 200, "description": "again"}, urgency="routine", seq=3)
    assert second.status == ActionStatus.needs_approval
