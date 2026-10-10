from pathlib import Path

from harness.adapters.dwelly import DwellyCasesAdapter, load_dwelly_case, parse_history, parse_index, write_expected
from harness.schema import ArtefactKind, ToolClass

ROOT = Path(__file__).resolve().parent.parent
CASE = ROOT / "fixtures-dwelly" / "Property Management" / "003"


def test_parse_index_hides_outcome_by_default():
    parsed = parse_index((CASE / "index.md").read_text(encoding="utf-8"))
    assert parsed.title.startswith("Case 003")
    assert parsed.details["property"].startswith("Flat 30")
    assert parsed.outcome and parsed.overview
    case = load_dwelly_case(CASE)
    index = next(a for a in case.artefacts if a.id == "index")
    assert "Outcome" not in index.content and "Paid" not in index.content
    assert "Initial request" in index.content and "Status" not in index.content


def test_history_events_become_artefacts_with_trust():
    events = parse_history((CASE / "history.md").read_text(encoding="utf-8"))
    assert len(events) == 23 and events[0].number == 1 and events[0].channel == "Note"
    case = load_dwelly_case(CASE)
    ev = {a.id: a for a in case.artefacts if a.id.startswith("event-")}
    assert ev["event-001"].trust == "informational"  # Agency / system
    assert ev["event-007"].trust == "untrusted"  # Contractor
    assert ev["event-003"].kind == ArtefactKind.email  # SMS
    assert case.metadata["events_visible"] == 23


def test_cutoff_limits_visible_history():
    case = load_dwelly_case(CASE, cutoff=6)
    ids = [a.id for a in case.artefacts if a.id.startswith("event-")]
    assert ids == [f"event-{i:03d}" for i in range(1, 7)]
    assert case.metadata["cutoff"] == 6


def test_attachments_are_documents_with_text():
    case = load_dwelly_case(CASE)
    docs = [a for a in case.artefacts if a.kind == ArtefactKind.document]
    assert len(docs) == 2
    assert all(len(d.content) > 50 for d in docs)


def test_registry_and_ledger():
    adapter = DwellyCasesAdapter(cutoff=6)
    cases = adapter.load_cases(ROOT / "fixtures-dwelly" / "Property Management")
    assert {c.id for c in cases} == {"property-001", "property-003", "property-007"}
    case = next(c for c in cases if c.id == "property-003")
    reg = adapter.tools_for(case)
    names = set(reg.names())
    assert {"get_case_details", "search_history", "get_attachment", "assign_contractor", "request_landlord_approval", "create_human_task", "close_request"} <= names
    spec = reg.get("assign_contractor").spec
    assert spec.tool_class == ToolClass.write and spec.authority == "dispatch_contractor" and spec.amount_field == "estimated_cost_gbp"
    hits = reg.get("search_history").fn(query="estimate")
    assert hits and hits[0]["event"] == "event-001"
    receipt = reg.get("add_note").fn(note="hello", idempotency_key="k")
    assert receipt["recorded"] and receipt["id"] == "ACT-1"
    assert adapter.ledger_for("property-003")[0]["note"] == "hello"
    adapter.reset(case)
    assert adapter.ledger_for("property-003") == []


def test_write_expected_keeps_hidden_parts(tmp_path: Path):
    n = write_expected(ROOT / "fixtures-dwelly" / "Property Management", tmp_path, cutoff=6)
    assert n == 3
    text = (tmp_path / "property-003.yaml").read_text(encoding="utf-8")
    assert "outcome:" in text and "later_events" in text and "Paid" in text


def test_attachments_follow_the_cutoff():
    from harness.adapters.dwelly import visible_attachments_at

    events = parse_history((CASE / "history.md").read_text(encoding="utf-8"))
    parsed = parse_index((CASE / "index.md").read_text(encoding="utf-8"))
    assert visible_attachments_at(parsed, events, None) == parsed.attachments
    assert visible_attachments_at(parsed, events, 0) == []
    seen: list[str] = []
    for cut in range(0, len(events) + 1):
        now = visible_attachments_at(parsed, events, cut)
        assert set(seen) <= set(now), "visibility only grows with the cutoff"
        seen = now
    assert seen == parsed.attachments
    early = load_dwelly_case(CASE, cutoff=0)
    assert not [a for a in early.artefacts if a.kind == ArtefactKind.document]
    assert "## Attachments" not in next(a for a in early.artefacts if a.id == "index").content
    assert early.metadata["attachments_hidden"] == len(parsed.attachments)
    late = load_dwelly_case(CASE)
    assert late.metadata["attachments_hidden"] == 0


def test_case_metadata_names_the_agency():
    case = load_dwelly_case(CASE)
    assert case.metadata["agency"] == "Northbridge Lettings"


async def test_ledger_checks_that_the_approval_event_is_the_landlords():
    from harness.executor import ActionExecutor
    from harness.gate import PolicyGate
    from harness.rulebook import Rulebook
    from harness.schema import ActionStatus

    adapter = DwellyCasesAdapter()
    case = next(c for c in adapter.load_cases(ROOT / "fixtures-dwelly" / "Property Management") if c.id.endswith("001"))
    landlord = next(a.id for a in case.artefacts if "landlord" in str(a.metadata.get("from", "")).lower())
    other = next(a.id for a in case.artefacts if a.id.startswith("event-") and "landlord" not in str(a.metadata.get("from", "")).lower())
    ex = ActionExecutor(adapter.tools_for(case), PolicyGate(Rulebook.load(ROOT / "agent" / "rulebook.yaml")), case_id=case.id)
    base = {"trade": "gardener", "description": "clear the communal garden", "urgency": "routine", "estimated_cost_gbp": 180}
    blocked = await ex.execute("assign_contractor", base, urgency="routine", seq=1)
    assert blocked.status == ActionStatus.needs_approval and "APR-SPEND-OVER-CAP" in blocked.gate.rule_ids
    fake = await ex.execute("assign_contractor", {**base, "landlord_approval_ref": other}, urgency="routine", seq=2)
    assert fake.status == ActionStatus.failed and "not a landlord message" in (fake.error or "")
    real = await ex.execute("assign_contractor", {**base, "landlord_approval_ref": landlord}, urgency="routine", seq=3)
    assert real.status == ActionStatus.completed and real.gate.rule_ids == ["CAP-DISPATCH-APPROVED"]


async def test_ledger_rejects_lookalike_senders_and_records_once():
    from harness.executor import ActionExecutor
    from harness.gate import PolicyGate
    from harness.rulebook import Rulebook
    from harness.schema import ActionStatus, Artefact, Case

    def ev(i: int, sender: str) -> Artefact:
        return Artefact(id=f"event-{i:03d}", kind=ArtefactKind.email, title=sender, source="history.md", content="ok go ahead", trust="untrusted", metadata={"from": sender, "to": "Agency / system", "timestamp": f"2026-01-0{i} 10:00:00 UTC"})

    case = Case(id="x", title="t", artefacts=[ev(1, "Landlord's partner"), ev(2, "Contractor"), ev(3, "Landlord (Grace Nolan)"), ev(4, "Landlord")])
    adapter = DwellyCasesAdapter()
    ex = ActionExecutor(adapter.tools_for(case), PolicyGate(Rulebook.load(ROOT / "agent" / "rulebook.yaml")), case_id=case.id)
    base = {"trade": "plumber", "description": "fix the tap", "urgency": "routine", "estimated_cost_gbp": 95}
    for bad in ("event-001", "event-002", "event-9", " "):
        rec = await ex.execute("assign_contractor", {**base, "landlord_approval_ref": bad}, urgency="routine", seq=1)
        assert rec.status in (ActionStatus.failed, ActionStatus.needs_approval), bad
    ok = await ex.execute("assign_contractor", {**base, "landlord_approval_ref": "event-003"}, urgency="routine", seq=5)
    assert ok.status == ActionStatus.completed
    again = await ex.execute("assign_contractor", {**base, "landlord_approval_ref": "event-003"}, urgency="routine", seq=6)
    assert again.status == ActionStatus.completed and (again.result or {}).get("duplicate") is True
    ledger = await ex.execute("get_action_ledger", {}, urgency="routine", seq=7)
    assert len([e for e in (ledger.result or []) if e.get("action") == "assign_contractor"]) == 1


def test_event_ids_are_normalised_for_the_approval_ref():
    from harness.adapters.dwelly import normalise_event_id

    assert normalise_event_id("event-9") == "event-009"
    assert normalise_event_id("Event 012") == "event-012"
    assert normalise_event_id("#7") == "event-007"
    assert normalise_event_id("12") == "event-012"
    assert normalise_event_id("event-012") == "event-012"
    assert normalise_event_id("attachment-01") == "attachment-01"


def test_close_request_has_its_own_authority():
    adapter = DwellyCasesAdapter()
    case = next(iter(adapter.load_cases(ROOT / "fixtures-dwelly" / "Property Management")))
    spec = adapter.tools_for(case).get("close_request").spec
    assert spec.authority == "close_request"
