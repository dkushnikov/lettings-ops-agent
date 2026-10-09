from pathlib import Path

from harness.gate import PolicyGate, explain
from harness.rulebook import Rulebook
from harness.schema import GateVerdict, ToolClass
from harness.tools import make_spec

ROOT = Path(__file__).resolve().parent.parent


def _gate() -> PolicyGate:
    return PolicyGate(Rulebook.load(ROOT / "agent" / "rulebook.yaml"))


WO = make_spec(
    "create_work_order",
    "book a contractor",
    {"type": "object", "properties": {"estimated_cost_gbp": {"type": "number"}}, "required": [], "additionalProperties": False},
    tool_class=ToolClass.write,
    authority="dispatch_contractor",
    amount_field="estimated_cost_gbp",
    idempotent=True,
)
PAY = make_spec("update_payment_details", "change bank details", {"type": "object", "properties": {}}, tool_class=ToolClass.write, authority="change_payment_details", reversible=False)
ACCESS = make_spec("schedule_access", "book access", {"type": "object", "properties": {}}, tool_class=ToolClass.write, authority="schedule_access")
READ = make_spec("get_property", "read", {"type": "object", "properties": {}})
NOAUTH = make_spec("mystery_write", "write without authority", {"type": "object", "properties": {}}, tool_class=ToolClass.write)


def test_reads_always_allowed():
    d = _gate().check(READ, {}, urgency="unknown")
    assert d.verdict == GateVerdict.allow


def test_routine_within_cap_allowed_and_cited():
    d = _gate().check(WO, {"estimated_cost_gbp": 120}, urgency="routine")
    assert d.verdict == GateVerdict.allow
    assert "CAP-DISPATCH-ROUTINE" in d.rule_ids


def test_routine_over_cap_needs_landlord_approval():
    d = _gate().check(WO, {"estimated_cost_gbp": 450}, urgency="routine")
    assert d.verdict == GateVerdict.needs_approval
    assert "APR-SPEND-OVER-CAP" in d.rule_ids
    assert d.required_approval_from == "landlord"
    assert "BLOCKED" in explain(d)


def test_emergency_overrides_cap():
    d = _gate().check(WO, {"estimated_cost_gbp": 900}, urgency="emergency")
    assert d.verdict == GateVerdict.allow
    assert "CAP-DISPATCH-EMERGENCY" in d.rule_ids


def test_unknown_amount_is_conservative():
    d = _gate().check(WO, {}, urgency="routine")
    assert d.verdict == GateVerdict.needs_approval


def test_unknown_urgency_blocks_cap_override():
    d = _gate().check(WO, {"estimated_cost_gbp": 900}, urgency="unknown")
    assert d.verdict == GateVerdict.needs_approval


def test_prohibited_payment_details_escalates():
    d = _gate().check(PAY, {}, urgency="emergency")
    assert d.verdict == GateVerdict.escalate
    assert "PRO-PAYMENT-DETAILS" in d.rule_ids
    assert "PROHIBITED" in explain(d)


def test_consent_required_for_access():
    g = _gate()
    assert g.check(ACCESS, {"tenant_consent": False}, urgency="routine").verdict == GateVerdict.needs_approval
    assert g.check(ACCESS, {"tenant_consent": True}, urgency="routine").verdict == GateVerdict.allow


def test_write_without_authority_needs_a_human():
    d = _gate().check(NOAUTH, {}, urgency="routine")
    assert d.verdict == GateVerdict.needs_approval
