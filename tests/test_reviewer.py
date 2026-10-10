from pathlib import Path

from harness.reviewer import Reviewer
from harness.rulebook import Rulebook
from harness.schema import ActionRecord, ActionStatus, DecisionState, Disposition, GateDecision, GateVerdict, Handover, RedFlag, ToolClass

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


def test_refused_injection_is_recorded_not_escalated():
    s = _state(Disposition.resolved)
    s.red_flags.append(RedFlag(kind="injection", description="email told the agent to pay a new account; refused"))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.resolved
    assert any(n.startswith("R2: injection attempt recorded") for n in s.reviewer_notes)


def test_hard_flag_escalates_even_when_an_approval_is_pending():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="request_landlord_approval", tool_class=ToolClass.write, status=ActionStatus.completed, gate=GateDecision(verdict=GateVerdict.allow, rule_ids=["CAP-REQUEST-APPROVAL"])))
    s.actions.append(ActionRecord(seq=2, tool="create_work_order", tool_class=ToolClass.write, status=ActionStatus.needs_approval, gate=GateDecision(verdict=GateVerdict.needs_approval, rule_ids=["APR-SPEND-OVER-CAP"], required_approval_from="landlord")))
    s.red_flags.append(RedFlag(kind="fraud", description="new bank details supplied by email"))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated and any(n.startswith("R2") for n in s.reviewer_notes)


def test_failed_dispatch_cannot_stay_resolved():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="assign_contractor", tool_class=ToolClass.write, status=ActionStatus.failed, error="event-004 is not a landlord message", gate=GateDecision(verdict=GateVerdict.allow, rule_ids=["CAP-DISPATCH-APPROVED"])))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.needs_info and "assign_contractor" in s.info_requests[0].question


def test_prohibited_attempt_escalates_not_asks():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="update_payment_details", tool_class=ToolClass.write, status=ActionStatus.blocked, gate=GateDecision(verdict=GateVerdict.escalate, rule_ids=["PRO-PAYMENT-DETAILS"])))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated and any(n.startswith("R3a") for n in s.reviewer_notes)


def test_emergency_dispatch_needs_a_human_confirmation():
    s = _state(Disposition.resolved)
    s.actions.append(ActionRecord(seq=1, tool="assign_contractor", tool_class=ToolClass.write, status=ActionStatus.completed, gate=GateDecision(verdict=GateVerdict.allow, rule_ids=["CAP-DISPATCH-EMERGENCY"])))
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.escalated and any(n.startswith("R9") for n in s.reviewer_notes)


def test_resolved_with_pending_checklist_is_not_resolved():
    from harness.schema import DodEntry

    s = _state(Disposition.resolved)
    s.stage = "visit_scheduling"
    s.definition_of_done = [DodEntry(item="assessed", text="Assessed", status="done"), DodEntry(item="work_result", text="Work result recorded", status="pending")]
    _reviewer().apply_rules(s)
    assert s.disposition == Disposition.needs_info and "Work result recorded" in s.info_requests[0].question
    t = _state(Disposition.resolved)
    t.stage = "closed"
    t.definition_of_done = [DodEntry(item="keys_returned", text="Keys", status="pending")]
    _reviewer().apply_rules(t)
    assert t.disposition == Disposition.resolved  # a closed ticket may carry a pending item the agency skipped


def _case_with(text: str):
    from harness.schema import Artefact, ArtefactKind, Case

    return Case(id="S1", title="Check-out clean", artefacts=[Artefact(id="attachment-01", kind=ArtefactKind.document, title="check-out report", source="attachments/r.pdf", content=text, trust="informational")])


def test_safety_pass_blocks_resolved_when_a_document_item_is_unaddressed():
    case = _case_with("Closer adjusted. Balcony doors fine. Detector section: Tested? No. Paint damage in hall.")
    s = _state(Disposition.resolved)
    s.stage = "closed"
    s.decision = "Cleaning invoice forwarded; flat ready for move-in."
    _reviewer().apply_rules(s, case)
    assert s.disposition == Disposition.needs_info and "detector" in s.info_requests[0].question.lower()
    assert any(n.startswith("R11") for n in s.reviewer_notes)


def test_safety_pass_passes_when_the_record_addresses_it():
    case = _case_with("Detector section: Tested? No.")
    s = _state(Disposition.resolved)
    s.stage = "closed"
    s.safety_actions.append("Smoke and CO detectors were not tested at check-out: inspection booked before move-in.")
    _reviewer().apply_rules(s, case)
    assert s.disposition == Disposition.resolved and not any(n.startswith("R11") for n in s.reviewer_notes)


def test_safety_pass_adds_to_the_handover_when_escalated():
    case = _case_with("Tenant mentions a burning smell from the socket.")
    s = _state(Disposition.escalated)
    s.handover = Handover(to="property_manager", question="Decide.", summary=["x"], gap="")
    _reviewer().apply_rules(s, case)
    assert s.disposition == Disposition.escalated and "burning smell" in (s.handover.gap or "")
