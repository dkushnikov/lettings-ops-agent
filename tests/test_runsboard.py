"""Runs board: collect case runs and sim runs from a runs directory and render one self-contained page."""

import json
import re
from pathlib import Path

from evalkit.runsboard import build_page, collect_runs


def _fake_runs(root: Path) -> Path:
    runs = root / "runs"
    run = runs / "pm-fake"
    (run / "003").mkdir(parents=True)
    (run / "_run.json").write_text(json.dumps({
        "run_id": "abc12345", "started_at": "2026-10-10T11:35:11Z", "finished_at": "2026-10-10T11:51:03Z", "model": "claude-opus-5", "effort": "high",
        "concurrency": 6, "cases_total": 2, "completed": 2, "resolved": 0, "needs_info": 1, "escalated": 1, "fallback_count": 1,
        "failures": ["004: boom"], "input_tokens": 1500, "output_tokens": 300, "actual_wall_s": 952.1,
    }), encoding="utf-8")
    (run / "_eval.json").write_text(json.dumps([
        {"case": "003", "disposition": "needs_info", "outcome": 2, "judgement_safety": 1, "critical_failure": False, "prohibited_violated": [], "notes": "fine"},
    ]), encoding="utf-8")
    (run / "_cutoffs.yaml").write_text("'003': 7\n", encoding="utf-8")
    (run / "003" / "_state.json").write_text(json.dumps({
        "case_id": "003", "disposition": "needs_info", "stage": "on_hold", "hold_reason": "Waiting for Landlord", "next_step": "Landlord to reply",
        "definition_of_done": [{"item": "assessed", "status": "done"}, {"item": "closed", "status": "pending"}, {"item": "na", "status": "not_applicable"}],
        "steps": 3, "fallback": False, "model": "claude-opus-5", "input_tokens": 1000, "output_tokens": 200,
        "info_requests": [{"to": "landlord", "question": "Go ahead?"}], "red_flags": [{"kind": "data_quality"}],
    }), encoding="utf-8")
    (run / "003" / "ANSWER.md").write_text("# ANSWER — Case 003\n", encoding="utf-8")
    (run / "004").mkdir()
    (run / "004" / "_state.json").write_text(json.dumps({"case_id": "004", "disposition": "escalated", "fallback": True, "handover": {"question": "?"}}), encoding="utf-8")
    (run / "_expected").mkdir()  # underscore dirs are never cases
    (run / "report.html").write_text("<html></html>", encoding="utf-8")
    sim = runs / "sim" / "20261010-140000"
    sim.mkdir(parents=True)
    (sim / "summary.json").write_text(json.dumps({
        "kind": "sim", "timestamp": "2026-10-10T14:00:00+01:00", "commit": "abc1234", "dirty": True, "wall_s": 12.5, "max_ticks": 10, "judge": True,
        "agent": {"model": "claude-opus-5", "effort": "high"}, "director": {"model": "claude-opus-5", "effort": "medium"},
        "scenarios": [{"id": "SC-01", "title": "Dripping tap", "ticks": 3, "final_disposition": "needs_info", "final_stage": "landlord_approval",
                       "expected_disposition": "resolved", "expected_stage": "closed", "expected": "resolved/closed", "should_passed": 1, "should_total": 2,
                       "must_not_violated": 0, "must_not_total": 1, "end_state_match": "partial", "critical_failure": False, "verdict": "PARTIAL",
                       "end_reason": "script complete", "tokens_in": 100, "tokens_out": 20, "file": "SC-01.json"}],
        "verdicts": {"PARTIAL": 1}, "tokens_in": 100, "tokens_out": 20,
    }), encoding="utf-8")
    (sim / "SC-01.json").write_text("{}", encoding="utf-8")
    (runs / "cases").mkdir()
    (runs / "cases" / "index.html").write_text("<html></html>", encoding="utf-8")
    (runs / "replay-cases" / "050").mkdir(parents=True)  # a symlink farm of inputs, not a run
    (runs / "replay-cases" / "050" / "index.md").write_text("# Case 050\n", encoding="utf-8")
    (runs / "empty").mkdir()
    return runs


def test_collect_runs_reads_both_kinds_newest_first(tmp_path: Path):
    runs = _fake_runs(tmp_path)
    entries = collect_runs(runs)
    assert [e["name"] for e in entries] == ["sim/20261010-140000", "pm-fake"]
    pm = entries[1]
    assert pm["kind"] == "cases" and pm["cases_total"] == 2 and pm["present"] == 2 and pm["valid"] == 1 and pm["fallbacks"] == 1
    assert pm["dispositions"] == {"needs_info": 1, "escalated": 1, "resolved": 0}
    assert pm["judge"] == {"rows": 1, "outcome_sum": 2, "outcome_max": 2, "js_sum": 1, "js_max": 2, "critical": 0, "prohibited": 0}
    assert pm["wall_s"] == 952.1 and pm["report"].endswith("report.html") and [r[0] for r in pm["raw"]] == ["_run.json", "_eval.json", "_cutoffs.yaml"]
    c3 = next(c for c in pm["cases"] if c["id"] == "003")
    assert c3["number"] == "003" and c3["judge"]["outcome"] == 2 and c3["cutoff"] == 7 and (c3["dod_done"], c3["dod_total"]) == (1, 2)
    assert c3["valid"] and c3["red_flags"] == 1 and c3["answer"].endswith("ANSWER.md")
    c4 = next(c for c in pm["cases"] if c["id"] == "004")
    assert c4["fallback"] and not c4["valid"] and c4["judge"] is None and c4["answer"] is None
    sim = entries[0]
    assert sim["kind"] == "sim" and sim["commit"] == "abc1234" and sim["dirty"] and sim["verdicts"] == {"PARTIAL": 1}
    assert sim["scenarios"][0]["file"].endswith("SC-01.json") and sim["model"].startswith("claude-opus-5 (high)")


def test_build_page_is_self_contained_with_links(tmp_path: Path):
    runs = _fake_runs(tmp_path)
    out = runs / "board" / "index.html"
    build_page(collect_runs(runs), out)
    text = out.read_text(encoding="utf-8")
    assert "pm-fake" in text and "sim/20261010-140000" in text
    assert "judge outcome <b>2/2</b>" in text and "J&amp;S <b>1/2</b>" in text and "critical <b>0</b>" in text
    assert "cases <b>2</b> · present <b>2</b> · valid <b>1</b> · fallbacks <b>1</b>" in text
    assert "needs_info 1" in text and "escalated 1" in text
    assert "15.9 min" in text and "abc1234*" in text
    assert 'href="../cases/index.html#Property%20Management/003"' in text
    assert 'href="../pm-fake/report.html"' in text and 'href="../pm-fake/_eval.json"' in text and 'href="../pm-fake/003/ANSWER.md"' in text
    assert 'href="../sim/20261010-140000/SC-01.json"' in text and "Dripping tap" in text and ">PARTIAL<" in text
    assert "prefers-color-scheme:dark" in text and "<details" in text
    assert not re.search(r"<(script|link)[^>]+(src|href)=\"https?://", text)


def test_missing_runs_dir_and_no_case_browser(tmp_path: Path):
    assert collect_runs(tmp_path / "nowhere") == []
    out = tmp_path / "board" / "index.html"
    build_page([], out)
    text = out.read_text(encoding="utf-8")
    assert "No runs found" in text and "cases/index.html#" not in text
