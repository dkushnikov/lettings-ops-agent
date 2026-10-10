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
    events = parse_history((CASE / "history.md").read_text(encoding="utf-8"))
    parsed = parse_index((CASE / "index.md").read_text(encoding="utf-8"))
    first = {name: next((e.number for e in events if name in e.body or Path(name).stem in e.body), None) for name in parsed.attachments}
    assert first and all(v is not None for v in first.values()), first
    early = load_dwelly_case(CASE, cutoff=min(first.values()) - 1)
    assert not [a for a in early.artefacts if a.kind == ArtefactKind.document]
    assert "## Attachments" not in next(a for a in early.artefacts if a.id == "index").content
    assert early.metadata["attachments_hidden"] == len(parsed.attachments)
    late = load_dwelly_case(CASE, cutoff=max(first.values()))
    assert len([a for a in late.artefacts if a.kind == ArtefactKind.document]) == len(parsed.attachments)
    assert late.metadata["attachments_hidden"] == 0
