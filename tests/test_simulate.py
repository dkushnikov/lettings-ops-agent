"""Scenario simulator: library, world seeding, episode loop and verdicts with a fake agent and a scripted director."""

from pathlib import Path

import pytest
import yaml

from evalkit.simulate import (
    MAX_IDLE_TICKS,
    SIM_PROPERTY_ID,
    Episode,
    deterministic_checks,
    load_library,
    opening_history,
    run_episode,
    seed_world,
    select,
    verdict,
)
from harness.schema import DecisionState, Disposition, DodEntry, Handover, RedFlag

ROOT = Path(__file__).resolve().parent.parent
WORLD = yaml.safe_load((ROOT / "mockworld" / "data" / "world.yaml").read_text(encoding="utf-8"))

SCENARIO = {
    "id": "SC-T1",
    "title": "test",
    "setting": {"issue": "Tap dripping", "tenancy": {"let": True, "occupants": 1}, "property": {"spend_cap_gbp": 100}, "start_stage": "intake"},
    "script": [
        {"actor": "tenant", "channel": "email", "behaviour": "TT-01", "message": "tap drips"},
        {"actor": "landlord", "channel": "email", "behaviour": "LL-01", "on": "agent requests approval", "message": "Please go ahead"},
        {"actor": "contractor", "channel": "call", "behaviour": "CT-01"},
    ],
    "checks": {"should": ["Ask the landlord"], "must_not": ["Dispatch over the cap"], "red_flags": ["data_quality"]},
    "end_state": {"stage": "closed", "disposition": "resolved", "dod_done": ["assessed"]},
}


def _fire(turn, body="", silence="", hours=2):
    return {"fire": [{"turn": turn, "hours_after_previous": hours, "from_name": "", "silence": silence, "body": body}], "idle_hours": 0, "reasoning": f"turn {turn}"}


NOTHING = {"fire": [], "idle_hours": 48, "reasoning": "trigger not met"}


def _director(outputs):
    outputs = list(outputs)

    async def director(ep, agent_has_acted):
        return outputs.pop(0) if outputs else NOTHING

    return director


def _agent(cases, write_on_tick=1):
    async def agent_fn(case, registry):
        cases.append(case)
        if len(cases) == write_on_tick:
            await registry.get("request_landlord_approval").call(property_id=SIM_PROPERTY_ID, subject="Tap washer", amount_gbp=180, rationale="over cap")
        st = DecisionState(case_id=case.id, disposition=Disposition.needs_info, stage="landlord_approval", hold_reason="Waiting for Landlord")
        return st

    return agent_fn


def test_library_behaviours_resolve():
    lib = load_library()
    assert lib.scenarios
    for sc in lib.scenarios:
        assert lib.missing_behaviours(sc) == [], sc["id"]


def test_select_normalises_ids():
    lib = load_library()
    assert [s["id"] for s in select(lib, ["1", "sc-2", "SC-03"])] == ["SC-01", "SC-02", "SC-03"]
    with pytest.raises(KeyError):
        select(lib, ["SC-99"])


def test_seed_world_property_cap_and_stage():
    data = seed_world(WORLD, SCENARIO)
    ll = next(x for x in data["landlords"] if x["id"] == "L-SIM")
    assert ll["spend_cap_gbp"] == 100 and ll["always_ask"] is False
    assert any(t["property_id"] == SIM_PROPERTY_ID for t in data["tenancies"])
    assert not any(w["property_id"] == SIM_PROPERTY_ID for w in data.get("work_orders", []))
    vacant = {**SCENARIO, "setting": {**SCENARIO["setting"], "tenancy": {"let": False}, "start_stage": "paused"}}
    data = seed_world(WORLD, vacant)
    assert not any(t["property_id"] == SIM_PROPERTY_ID for t in data["tenancies"])
    assert any(w["property_id"] == SIM_PROPERTY_ID for w in data["work_orders"])
    assert "NOT TENANTED" in opening_history(vacant)[-1]
    assert WORLD["landlords"][-1]["id"] != "L-SIM"  # base data untouched


async def test_episode_runs_script_to_completion():
    cases = []
    director = _director([_fire(0, body="director text ignored"), _fire(1, body="also ignored"), _fire(2, body="Call summary: contractor booked Friday.")])
    ep = await run_episode(SCENARIO, agent_fn=_agent(cases), director=director, world_data=WORLD)
    assert ep.end_reason == "script complete"
    assert len(ep.ticks) == 3
    msgs = [e for e in ep.events if e.kind == "message"]
    assert [m.body for m in msgs] == ["tap drips", "Please go ahead", "Call summary: contractor booked Friday."]
    # tick 1 saw only the tenant; its approval request reached the agency log the director and tick 2 read
    assert [a.id for a in cases[0].artefacts] == ["ticket", "ev01"]
    assert cases[0].artefacts[1].trust == "untrusted"
    agency = [e for e in ep.events if e.kind == "agency"]
    assert "Approval requested from the landlord" in agency[0].body
    assert any(a.kind.value == "call_transcript" for a in cases[2].artefacts)
    # the world persists across ticks: one approval only, written in tick 1
    assert len(ep.ticks[0].effects) == 1 and ep.ticks[1].effects == []
    assert ep.clock > ep.events[0].time


async def test_episode_stalls_when_trigger_never_met():
    ep = await run_episode(SCENARIO, agent_fn=_agent([], write_on_tick=0), director=_director([_fire(0)]), world_data=WORLD)
    assert ep.end_reason.startswith("stalled: turn 1")
    assert len(ep.ticks) == MAX_IDLE_TICKS + 1
    assert sum(1 for e in ep.events if e.kind == "system") == MAX_IDLE_TICKS


async def test_out_of_order_turn_is_ignored_and_silence_recorded():
    director = _director([_fire(0), _fire(2, body="skipped ahead"), _fire(1, silence="Landlord silent for 3 days", hours=72)])
    ep = await run_episode(SCENARIO, agent_fn=_agent([]), director=director, world_data=WORLD, max_ticks=3)
    assert 2 not in ep.fired or ep.fired[2] > ep.fired[1]
    assert any("out-of-order" in n for n in ep.director_notes)
    kinds = [(e.kind, e.turn) for e in ep.events if e.turn == 1]
    assert kinds == [("silence", 1), ("message", 1)]  # silence first, then the literal message


def _graded(state, grade):
    ep = Episode(scenario=SCENARIO, end_reason="script complete")
    from evalkit.simulate import TickResult

    ep.ticks.append(TickResult(tick=1, time=ep.clock, state=state, effects=[]))
    ep.grade = {**grade, "deterministic": deterministic_checks(ep)}
    return ep


def test_verdicts():
    good = DecisionState(case_id="x", disposition=Disposition.resolved, stage="closed", decision="done",
                         red_flags=[RedFlag(kind="data_quality", description="address mismatch")],
                         definition_of_done=[DodEntry(item="assessed", status="done")])
    ok = {"should": [{"check": "a", "verdict": "pass", "evidence": ""}], "must_not": [{"check": "b", "violated": False, "evidence": ""}],
          "end_state_match": "yes", "critical_failure": False, "summary": ""}
    assert verdict(_graded(good, ok)) == "PASS"
    assert verdict(_graded(good, {**ok, "must_not": [{"check": "b", "violated": True, "evidence": ""}]})) == "FAIL"
    esc = DecisionState(case_id="x", disposition=Disposition.escalated, stage="closed", handover=Handover(question="q"))
    ep = _graded(esc, ok)
    assert ep.grade["deterministic"]["disposition"] == ("resolved", "escalated")
    assert ep.grade["deterministic"]["red_flags_missing"] == ["data_quality"]
    assert verdict(ep) == "PARTIAL"


def test_crashed_episode_is_an_error():
    ep = Episode(scenario=SCENARIO, end_reason="simulator error: AuthenticationError: 401")
    assert verdict(ep) == "ERROR"
    assert verdict(Episode(scenario=SCENARIO, end_reason="script complete")) == "UNGRADED"
