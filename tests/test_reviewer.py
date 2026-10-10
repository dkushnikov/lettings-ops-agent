from pathlib import Path

from harness.reviewer import Reviewer
from harness.rulebook import Rulebook
from harness.schema import ActionRecord, ActionStatus, DecisionState, Disposition, GateDecision, GateVerdict, RedFlag, ToolClass

ROOT = Path(__file__).resolve().parent.parent


def _reviewer() -> Reviewer:
    return Reviewer(Rulebook.load(ROOT / "agent" / "rulebook.yaml"))


def _state(disposition: Disposition) -> DecisionState:
    s = DecisionState(case_id="C1", disposition=disposition, decision="done")
    return s


def test_unconfirmed_write_forces_escalation():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="create_work_order", tool_class=ToolClass.write, status=ActionStatus.unconfirmed, idempotency_key="k1"))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated
    assert s.handover is not None and "k1" in s.handover.gap
    assert any(n.startswith("R1") for n in s.reviewer_notes)


def test_fraud_flag_on_resolved_case_escalates():
    s = _state(Disposition.resolved)
    s.red_flags.append(RedFlag(kind="fraud", description="bank details change requested by email"))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated
    assert s.handover is not None


def test_resolved_with_blocked_write_and_no_approval_becomes_needs_info():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="create_work_order", tool_class=ToolClass.write, status=ActionStatus.needs_approval, gate=GateDecision(verdict=GateVerdict.needs_approval, rule_ids=["APR-SPEND-OVER-CAP"], required_approval_from="landlord")))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.needs_info
    assert s.info_requests and s.info_requests[0].to == "landlord"


def test_resolved_with_pending_approval_becomes_needs_info():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="create_work_order", tool_class=ToolClass.write, status=ActionStatus.needs_approval, gate=GateDecision(verdict=GateVerdict.needs_approval, rule_ids=["APR-SPEND-OVER-CAP"], required_approval_from="landlord")))
    s.actions.append(ActionRecord(seq=2, tool="request_landlord_approval", tool_class=ToolClass.write, status=ActionStatus.completed))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.needs_info
    assert s.info_requests and s.info_requests[0].to == "landlord"
    assert any(n.startswith("R7") for n in s.reviewer_notes)


def test_vulnerability_watch_flag_does_not_force_escalation():
    s = _state(Disposition.resolved)
    s.red_flags.append(RedFlag(kind="vulnerability", description="children in occupation; no loss of service; watch item"))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.resolved


def test_escalated_without_handover_gets_a_card():
    s = _state(Disposition.escalated)
    _reviewer().apply_rules(s)
    assert s.handover is not None and s.handover.question


def test_needs_info_without_question_escalates():
    s = _state(Disposition.needs_info)
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated


def test_resolved_while_on_hold_becomes_needs_info():
    s = _state(Disposition.resolved)
    s.stage = "on_hold"
    s.hold_reason = "Waiting for Provider — Clarke to confirm attendance date and access"
    s.next_step = "Clarke to confirm the attendance date for job NBL-007-0235"
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.needs_info
    assert s.info_requests and s.info_requests[0].to == "contractor" and "attendance" in s.info_requests[0].question
    assert any(n.startswith("R8") for n in s.reviewer_notes)


def test_resolved_with_a_hold_action_and_no_reason_still_flips():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="put_on_hold", tool_class=ToolClass.write, status=ActionStatus.completed))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.needs_info and s.info_requests[0].to == "property_manager"


def test_hard_flag_wins_over_the_hold_rule():
    s = _state(Disposition.resolved)
    s.hold_reason = "Waiting for Landlord"
    s.red_flags.append(RedFlag(kind="fraud", description="new bank details by email"))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated
