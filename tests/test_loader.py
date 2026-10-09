import json
from pathlib import Path

from harness.loader import guess_kind, load_cases
from harness.schema import ArtefactKind


def test_case_dir_with_manifest(tmp_path: Path):
    d = tmp_path / "C1"
    d.mkdir()
    (d / "email-01.md").write_text("Hello, the boiler is broken.", encoding="utf-8")
    (d / "record-tenancy.json").write_text(json.dumps({"property_id": "P-1"}), encoding="utf-8")
    (d / "case.yaml").write_text(
        "id: C1\ntitle: Boiler\nreceived_at: 2026-10-01T09:00:00\nenv:\n  fail_modes: {create_work_order: lost_response}\nartefacts:\n  - {file: email-01.md, kind: email}\n  - {file: record-tenancy.json, kind: record, title: Tenancy}\n",
        encoding="utf-8",
    )
    (d / "expected.yaml").write_text("expected_disposition: resolved\n", encoding="utf-8")
    cases = load_cases(tmp_path)
    assert len(cases) == 1
    c = cases[0]
    assert c.id == "C1" and c.env["fail_modes"]["create_work_order"] == "lost_response"
    assert c.artefacts[0].trust == "untrusted" and c.artefacts[1].trust == "authoritative"
    assert '"property_id": "P-1"' in c.artefacts[1].content
    assert c.expected_path and c.expected_path.endswith("expected.yaml")


def test_loose_dir_guesses_kinds(tmp_path: Path):
    d = tmp_path / "C2"
    d.mkdir()
    (d / "call_transcript.txt").write_text("Agent: hello", encoding="utf-8")
    (d / "crm_export.json").write_text("{}", encoding="utf-8")
    cases = load_cases(tmp_path)
    kinds = {a.id: a.kind for a in cases[0].artefacts}
    assert kinds["call_transcript"] == ArtefactKind.call_transcript
    assert kinds["crm_export"] == ArtefactKind.record


def test_guess_kind():
    assert guess_kind("tenant-email.md") == ArtefactKind.email
    assert guess_kind("gas-certificate.pdf") == ArtefactKind.document
    assert guess_kind("misc.txt") == ArtefactKind.other
