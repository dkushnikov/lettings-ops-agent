import re
from pathlib import Path

from evalkit.casebrowser import build_page, collect_cases, load_runs, party_of

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "fixtures-dwelly" / "Property Management"


def test_party_classification():
    assert party_of("Agency / system") == "agency"
    assert party_of("Northbridge Lettings") == "agency"
    assert party_of("Contractor") == "contractor"
    assert party_of("Landlord") == "landlord"
    assert party_of("Tenant") == "tenant"


def test_build_page_is_self_contained(tmp_path: Path):
    out = tmp_path / "index.html"
    cases = collect_cases(CASES, out.parent)
    assert len(cases) == 3
    build_page(cases, load_runs([]), out)
    assert out.exists()
    text = out.read_text(encoding="utf-8")
    for c in cases:
        assert c["title"] in text
    assert '"number": "003"' in text
    assert "first_external" in text
    assert not re.search(r"<(script|link)[^>]+(src|href)=\"https?://", text)
    c3 = next(c for c in cases if c["number"] == "003")
    assert c3["n_events"] == 23 and c3["has_attachments"] and c3["attachments"][0]["href"].endswith(".pdf")
    assert c3["first_external"] == 7


def test_run_overlay_tolerates_partial_dirs(tmp_path: Path):
    run = tmp_path / "pm"
    (run / "property-003").mkdir(parents=True)
    (run / "property-003" / "ANSWER.md").write_text("# ANSWER — Case 003\n", encoding="utf-8")
    (run / "property-003" / "_state.json").write_text('{"disposition": "escalated", "steps": 4, "urgency": "routine", "red_flags": [{"kind": "fraud"}]}', encoding="utf-8")
    (run / "property-999").mkdir()  # no ANSWER.md → ignored
    (run / "_cutoffs.yaml").write_text('"003": 6\n', encoding="utf-8")
    (run / "_eval.json").write_text('[{"case": "property-003", "outcome": 1, "judgement_safety": 2, "critical_failure": false, "notes": "ok"}]', encoding="utf-8")
    overlay = load_runs([run, tmp_path / "missing"])
    assert set(overlay) == {"pm"}
    assert overlay["pm"]["cases"]["003"]["disposition"] == "escalated"
    assert overlay["pm"]["cutoffs"]["003"] == 6 and overlay["pm"]["evals"]["003"]["outcome"] == 1
    out = tmp_path / "index.html"
    build_page(collect_cases(CASES, out.parent), overlay, out)
    assert '"disposition": "escalated"' in out.read_text(encoding="utf-8")
