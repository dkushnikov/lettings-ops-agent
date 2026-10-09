from pathlib import Path

import yaml

from evalkit.mutate import AXES, mutate_case
from harness.loader import load_cases

ROOT = Path(__file__).resolve().parent.parent
F01 = ROOT / "fixtures" / "F01-routine-tap"


def test_all_axes_produce_loadable_cases(tmp_path: Path):
    for axis in AXES:
        mutate_case(F01, axis, tmp_path)
    cases = {c.id: c for c in load_cases(tmp_path)}
    assert len(cases) == len(AXES)
    assert cases["F01-mut-fail_tool"].env["fail_modes"]["create_work_order"] == "lost_response"
    assert len(cases["F01-mut-bloat"].artefacts) >= 20
    assert any(a.id == "email-injected" for a in cases["F01-mut-inject"].artefacts)
    assert all(a.kind.value not in ("record", "document") for a in cases["F01-mut-strip"].artefacts)
    stakes = next(a for a in cases["F01-mut-stakes"].artefacts if a.kind.value == "email")
    assert "oxygen concentrator" in stakes.content


def test_expected_carries_mutation_and_requirements(tmp_path: Path):
    dst = mutate_case(F01, "inject", tmp_path)
    exp = yaml.safe_load((dst / "expected.yaml").read_text(encoding="utf-8"))
    assert exp["mutation"]["axis"] == "inject"
    assert any("evidence, not authority" in r for r in exp["required_outcomes"])
    assert "injection" in exp["red_flags_expected"]
