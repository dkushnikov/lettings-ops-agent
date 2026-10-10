"""Loop tests with a scripted fake client: no network, deterministic."""

from pathlib import Path
from types import SimpleNamespace

from harness.llm import Settings
from harness.loop import CaseAgent, harness_tool_definitions
from harness.playbooks import PlaybookLibrary
from harness.rulebook import Rulebook
from harness.schema import ActionStatus, Artefact, ArtefactKind, Case, Disposition, ToolClass
from harness.tools import BoundTool, ToolRegistry, make_spec

ROOT = Path(__file__).resolve().parent.parent


def _tool_use(name: str, inp: dict, tid: str):
    return SimpleNamespace(type="tool_use", name=name, input=inp, id=tid)


def _text(t: str):
    return SimpleNamespace(type="text", text=t)


def _response(content, stop_reason="tool_use"):
    return SimpleNamespace(content=content, stop_reason=stop_reason, usage=SimpleNamespace(input_tokens=100, output_tokens=20, cache_read_input_tokens=0))


class FakeClient:
    def __init__(self, script):
        self.script = list(script)
        self.calls = []

        class _Messages:
            def __init__(inner, outer):
                inner.outer = outer

            async def create(inner, **params):
                inner.outer.calls.append(params)
                if not inner.outer.script:
                    return _response([_text("done")], "end_turn")
                return inner.outer.script.pop(0)

        self.messages = _Messages(self)


def _registry():
    reg = ToolRegistry()

    async def get_property(property_id: str):
        return {"property_id": property_id, "address": "1 Test Street"}

    reg.add(BoundTool(make_spec("get_property", "read a property", {"type": "object", "properties": {"property_id": {"type": "string"}}, "required": ["property_id"]}), get_property))

    async def create_work_order(property_id: str, estimated_cost_gbp: float, idempotency_key: str | None = None, **kw):
        return {"work_order_id": "WO-7"}

    reg.add(
        BoundTool(
            make_spec(
                "create_work_order",
                "book a contractor",
                {"type": "object", "properties": {"property_id": {"type": "string"}, "estimated_cost_gbp": {"type": "number"}}, "required": ["property_id", "estimated_cost_gbp"]},
                tool_class=ToolClass.write,
                authority="dispatch_contractor",
                amount_field="estimated_cost_gbp",
                idempotent=True,
            ),
            create_work_order,
        )
    )
    return reg


def _agent(script) -> CaseAgent:
    settings = Settings(model="claude-test", max_steps=4)
    rulebook = Rulebook.load(ROOT / "agent" / "rulebook.yaml")
    playbooks = PlaybookLibrary.load(ROOT / "agent" / "playbooks")
    return CaseAgent(settings, FakeClient(script), rulebook, playbooks)


def _case() -> Case:
    return Case(id="L1", title="Tap", artefacts=[Artefact(id="email-01", kind=ArtefactKind.email, content="The tap drips.", trust="untrusted")])


def test_terminal_definitions_have_no_refs():
    defs = harness_tool_definitions()
    names = {d["name"] for d in defs}
    assert {"use_playbook", "finalize", "request_info", "escalate"} <= names
    for d in defs:
        assert "$ref" not in str(d["input_schema"]) and "$defs" not in str(d["input_schema"])


async def test_happy_path_resolved_with_gate_and_terminal():
    script = [
        _response([_tool_use("use_playbook", {"name": "maintenance-request", "case_type": "maintenance_request", "urgency": "routine", "why": "drip"}, "t1")]),
        _response([_tool_use("get_property", {"property_id": "P-001"}, "t2"), _tool_use("create_work_order", {"property_id": "P-001", "estimated_cost_gbp": 120, "landlord_approval_ref": "email-01"}, "t3")]),
        _response([
            _tool_use(
                "finalize",
                {
                    "decision": "Plumber booked within cap; tenant to be notified.",
                    "facts": [{"id": "F1", "statement": "Tap drips", "source_ids": ["email-01"], "confidence": "high"}],
                    "authority_citations": ["CAP-DISPATCH-ROUTINE"],
                    "urgency": "routine",
                },
                "t4",
            )
        ]),
    ]
    agent = _agent(script)
    events = []
    state = await agent.run(_case(), _registry(), trace=events.append)
    assert state.disposition == Disposition.resolved
    assert state.playbook == "maintenance-request" and state.urgency == "routine"
    assert [a.status for a in state.actions] == [ActionStatus.completed, ActionStatus.completed]
    assert state.actions[1].gate.rule_ids == ["CAP-DISPATCH-APPROVED"]
    assert state.steps == 3 and state.input_tokens == 300
    assert any(e["event"] == "terminal" and e["ok"] for e in events)


async def test_blocked_write_then_escalate():
    script = [
        _response([_tool_use("use_playbook", {"name": "maintenance-request", "case_type": "maintenance_request", "urgency": "routine", "why": "x"}, "t1")]),
        _response([_tool_use("create_work_order", {"property_id": "P-001", "estimated_cost_gbp": 900}, "t2")]),
        _response([_tool_use("escalate", {"decision": "Over cap", "handover": {"question": "Approve £900?", "summary": ["over cap"], "gap": "landlord approval"}}, "t3")]),
    ]
    state = await _agent(script).run(_case(), _registry())
    assert state.actions[0].status == ActionStatus.needs_approval
    assert state.disposition == Disposition.escalated and state.handover.question == "Approve £900?"


async def test_invalid_terminal_payload_is_rejected_then_fixed():
    script = [
        _response([_tool_use("escalate", {"decision": "x"}, "t1")]),  # missing handover → validation error
        _response([_tool_use("escalate", {"decision": "x", "handover": {"question": "Q?"}}, "t2")]),
    ]
    state = await _agent(script).run(_case(), _registry())
    assert state.disposition == Disposition.escalated and state.steps == 2


async def test_no_terminal_call_falls_back_to_escalation():
    script = [
        _response([_text("I think it's fine.")], "end_turn"),
        _response([_text("Still nothing.")], "end_turn"),
    ]
    state = await _agent(script).run(_case(), _registry())
    assert state.fallback is True
    assert state.disposition == Disposition.escalated and state.handover is not None
    assert state.terminal_valid()


async def test_step_budget_exhausted_falls_back():
    script = [_response([_tool_use("get_property", {"property_id": "P-001"}, f"t{i}")]) for i in range(10)]
    state = await _agent(script).run(_case(), _registry())
    assert state.fallback is True and state.steps == 4


def test_terminal_schemas_require_the_status_fields():
    for d in harness_tool_definitions():
        if d["name"] in ("finalize", "request_info", "escalate"):
            req = d["input_schema"]["required"]
            assert {"recap", "stage", "next_step", "definition_of_done"} <= set(req), d["name"]
            assert "item" in d["input_schema"]["properties"]["definition_of_done"]["items"]["properties"]


async def test_playbook_seeds_the_checklist_and_finalize_merges_it():
    agent = _agent(
        [
            _response([_tool_use("use_playbook", {"name": "maintenance-request", "case_type": "maintenance_request", "urgency": "routine", "why": "dripping tap"}, "t1")]),
            _response(
                [
                    _tool_use(
                        "finalize",
                        {
                            "decision": "Plumber booked within cap. Tenant told the slot.",
                            "recap": "Dripping tap: plumber booked within the standing cap.",
                            "stage": "visit_scheduling",
                            "next_step": "Provider to attend Tuesday AM; tenant confirmed",
                            "definition_of_done": [
                                {"item": "landlord_authority", "status": "done", "evidence": "CAP-DISPATCH-ROUTINE, under cap"},
                                {"item": "provider_assigned", "status": "done", "evidence": "action 2"},
                                {"item": "keys_returned", "status": "not_applicable", "evidence": "tenant present"},
                            ],
                        },
                        "t2",
                    )
                ]
            ),
        ]
    )
    case = Case(id="c1", title="Tap", artefacts=[Artefact(id="a1", kind=ArtefactKind("email"), title="t", source="s", content="The kitchen tap drips.", trust="untrusted")])
    state = await agent.run(case, _registry())
    assert state.disposition == Disposition.resolved
    assert state.recap.startswith("Dripping tap") and state.stage == "visit_scheduling"
    by_id = {d.item: d for d in state.definition_of_done}
    assert len(by_id) == 11, "the whole playbook checklist is seeded, not only the items the model mentioned"
    assert by_id["landlord_authority"].status == "done" and by_id["landlord_authority"].text.startswith("Landlord approval")
    assert by_id["work_result"].status == "pending"
    assert by_id["keys_returned"].status == "not_applicable"
    assert "DEFINITION OF DONE" in str(agent.client.calls[1]["messages"])


async def test_next_step_defaults_from_the_handover():
    agent = _agent(
        [
            _response([_tool_use("escalate", {"decision": "Disputed liability", "handover": {"question": "Who pays for the basin?", "summary": ["cracked basin"], "gap": "check-in inventory", "recommended": "Pull the check-in inventory before replying"}}, "t1")]),
        ]
    )
    case = Case(id="c2", title="Basin", artefacts=[])
    state = await agent.run(case, _registry())
    assert state.disposition == Disposition.escalated
    assert state.recap == "Disputed liability"
    assert state.next_step == "Pull the check-in inventory before replying"


async def test_time_budget_nudge_and_live_state_holder():
    from harness.loop import TIME_NUDGE

    agent = _agent(
        [
            _response([_tool_use("get_property", {"property_id": "P1"}, "t1")]),
            _response([_tool_use("escalate", {"decision": "out of time", "handover": {"question": "Continue?"}}, "t2")]),
        ]
    )
    agent.settings.case_timeout_s = 0.0  # soft deadline hits after the first tool round
    holder: dict = {}
    case = Case(id="c3", title="Slow", artefacts=[])
    state = await agent.run(case, _registry(), holder=holder)
    assert holder["state"] is state
    second_call = agent.client.calls[1]["messages"]
    assert any(isinstance(b, dict) and b.get("type") == "text" and b["text"] == TIME_NUDGE for m in second_call if isinstance(m.get("content"), list) for b in m["content"])
    assert state.disposition == Disposition.escalated
