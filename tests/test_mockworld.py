"""Mock world and adapter tests: deterministic, no network, no LLM."""

from __future__ import annotations

import asyncio

import pytest

from harness.schema import ToolClass
from harness.tools import LostResponseError, ToolRejected, TransientToolError
from mockworld import MockAdapter, World

EXPECTED_TOOLS = {
    "get_property",
    "get_tenancy",
    "find_tenancies",
    "get_landlord_instructions",
    "get_compliance_certificates",
    "search_crm_notes",
    "list_contractors",
    "get_work_orders",
    "create_work_order",
    "request_landlord_approval",
    "notify_tenant",
    "notify_landlord",
    "schedule_access",
    "log_crm_note",
    "create_human_task",
    "update_payment_details",
}

WRITE_AUTHORITIES = {
    "create_work_order": "dispatch_contractor",
    "request_landlord_approval": "request_approval",
    "notify_tenant": "notify_party",
    "notify_landlord": "notify_party",
    "schedule_access": "schedule_access",
    "log_crm_note": "log_note",
    "create_human_task": "create_human_task",
    "update_payment_details": "change_payment_details",
}


@pytest.fixture()
def adapter() -> MockAdapter:
    return MockAdapter()


@pytest.fixture()
def cases(adapter, fixtures_dir):
    return adapter.load_cases(fixtures_dir)


def by_id(cases, case_id):
    return next(c for c in cases if c.id == case_id)


# --------------------------------------------------------------------------- #
# loading
# --------------------------------------------------------------------------- #


def test_loads_ten_cases_with_artefacts(cases):
    assert [c.id for c in cases] == [f"F{i:02d}" for i in range(1, 11)]
    for case in cases:
        assert case.artefacts, case.id
        assert case.expected_path and case.expected_path.endswith("expected.yaml")
        for a in case.artefacts:
            assert a.content.strip(), f"{case.id}/{a.id} is empty"
            assert a.trust in {"authoritative", "informational", "untrusted"}


def test_trust_classes_follow_kind(cases):
    for case in cases:
        for a in case.artefacts:
            if a.kind.value in {"email", "call_transcript", "ticket"}:
                assert a.trust == "untrusted", f"{case.id}/{a.id}"
            if a.kind.value == "record":
                assert a.trust == "authoritative", f"{case.id}/{a.id}"


def test_f09_is_bloated(cases):
    f09 = by_id(cases, "F09")
    emails = [a for a in f09.artefacts if a.kind.value == "email"]
    assert len(emails) == 26
    assert sum("Sheen Lane" in a.content and "basin" in a.content for a in emails) == 1


def test_f05_declares_lost_response(cases):
    assert by_id(cases, "F05").env["fail_modes"] == {"create_work_order": "lost_response"}


# --------------------------------------------------------------------------- #
# tool registry
# --------------------------------------------------------------------------- #


def test_registry_has_expected_tools_and_classes(adapter, cases):
    reg = adapter.tools_for(by_id(cases, "F01"))
    assert set(reg.names()) == EXPECTED_TOOLS
    for spec in reg.specs():
        assert spec.input_schema["type"] == "object"
        assert spec.input_schema["additionalProperties"] is False
        assert "required" in spec.input_schema
        if spec.name in WRITE_AUTHORITIES:
            assert spec.tool_class == ToolClass.write
            assert spec.authority == WRITE_AUTHORITIES[spec.name]
        else:
            assert spec.tool_class == ToolClass.read
    cwo = reg.get("create_work_order").spec
    assert cwo.amount_field == "estimated_cost_gbp"
    assert cwo.idempotent is True
    assert cwo.reconcile_with == "get_work_orders"
    assert reg.get("update_payment_details").spec.reversible is False
    defs = reg.api_definitions()
    assert all({"name", "description", "input_schema"} <= set(d) for d in defs)


# --------------------------------------------------------------------------- #
# world behaviour
# --------------------------------------------------------------------------- #


def test_find_tenancies_sarah_khan_returns_two():
    world = World.load()
    hits = world.find_tenancies("Sarah Khan")
    assert len(hits) == 2
    assert {h["property_id"] for h in hits} == {"P-002", "P-004"}


def test_compliance_conflict_data_present():
    world = World.load()
    certs = world.get_compliance_certificates("P-003")
    gas = next(c for c in certs if c["type"] == "gas_safety_cp12")
    assert str(gas["expires"]) == "2026-08-14"
    notes = world.search_crm_notes("P-003", "gas cert")
    assert any("2027-02-01" in n["note"] for n in notes)


def test_f10_world_has_existing_work_order(adapter, cases):
    world = adapter.world_for(by_id(cases, "F10"))
    wos = world.get_work_orders("P-006")
    assert [w["id"] for w in wos] == ["WO-1001"]
    assert wos[0]["status"] == "open"


def test_every_write_tool_is_callable_and_logs(adapter, cases):
    case = by_id(cases, "F01")
    reg = adapter.tools_for(case)
    world = adapter.world_for(case)
    calls = {
        "create_work_order": dict(property_id="P-001", trade="plumber", description="Dripping kitchen tap", urgency="routine", estimated_cost_gbp=120, contractor_id="C-001"),
        "request_landlord_approval": dict(property_id="P-001", subject="Tap", amount_gbp=300, rationale="over cap"),
        "notify_tenant": dict(property_id="P-001", message="Plumber booked"),
        "notify_landlord": dict(property_id="P-001", message="FYI"),
        "schedule_access": dict(property_id="P-001", window="Thu 10-12", tenant_consent=True),
        "log_crm_note": dict(property_id="P-001", note="Agent note"),
        "create_human_task": dict(queue="property_manager", title="Check", summary="Please verify"),
        "update_payment_details": dict(landlord_id="L-001", account_number="12345678", sort_code="20-00-00"),
    }
    for name, kwargs in calls.items():
        result = asyncio.run(reg.get(name).call(**kwargs, idempotency_key=f"k-{name}"))
        assert result, name
    ops = {e["op"] for e in world.log}
    assert {"create_work_order", "request_landlord_approval", "notify_tenant", "notify_landlord", "schedule_access", "log_crm_note", "create_human_task", "update_payment_details"} <= ops


def test_schedule_access_without_consent_is_rejected(adapter, cases):
    reg = adapter.tools_for(by_id(cases, "F01"))
    with pytest.raises(ToolRejected):
        asyncio.run(reg.get("schedule_access").call(property_id="P-001", window="Thu", tenant_consent=False))


def test_create_work_order_is_idempotent():
    world = World.load()
    kwargs = dict(property_id="P-001", trade="plumber", description="Dripping tap", urgency="routine", estimated_cost_gbp=120, contractor_id="C-001")
    first = world.create_work_order(**kwargs, idempotency_key="abc")
    second = world.create_work_order(**kwargs, idempotency_key="abc")
    assert first["id"] == second["id"]
    assert second.get("deduplicated") is True
    assert len(world.get_work_orders("P-001")) == 1
    third = world.create_work_order(**kwargs, idempotency_key="xyz")
    assert third["id"] != first["id"]


def test_reconcile_finds_the_work_order(adapter, cases):
    case = by_id(cases, "F01")
    reg = adapter.tools_for(case)
    tool = reg.get("create_work_order")
    kwargs = dict(property_id="P-001", trade="plumber", description="Dripping tap", urgency="routine", estimated_cost_gbp=120, contractor_id="C-001")
    assert asyncio.run(tool.reconcile_call(kwargs)) is None
    asyncio.run(tool.call(**kwargs, idempotency_key="k1"))
    found = asyncio.run(tool.reconcile_call(kwargs))
    assert found and found["description"] == "Dripping tap"


def test_reset_restores_state(adapter, cases):
    case = by_id(cases, "F01")
    reg = adapter.tools_for(case)
    asyncio.run(reg.get("log_crm_note").call(property_id="P-001", note="temp"))
    world = adapter.world_for(case)
    assert world.ops("log_crm_note")
    adapter.reset(case)
    assert world.log == []
    assert not any(n["note"] == "temp" for n in world.search_crm_notes("P-001"))


# --------------------------------------------------------------------------- #
# failure injection
# --------------------------------------------------------------------------- #


def _case_with(adapter, cases, fail_modes):
    case = by_id(cases, "F01").model_copy(deep=True)
    case.id = "F01-" + "-".join(fail_modes.values())
    case.env = {"fail_modes": fail_modes}
    return case


def test_transient_fails_once_then_succeeds(adapter, cases):
    case = _case_with(adapter, cases, {"get_property": "transient"})
    reg = adapter.tools_for(case)
    with pytest.raises(TransientToolError):
        asyncio.run(reg.get("get_property").call(property_id="P-001"))
    assert asyncio.run(reg.get("get_property").call(property_id="P-001"))["id"] == "P-001"


def test_reject_always_rejects(adapter, cases):
    case = _case_with(adapter, cases, {"notify_tenant": "reject"})
    reg = adapter.tools_for(case)
    for _ in range(2):
        with pytest.raises(ToolRejected):
            asyncio.run(reg.get("notify_tenant").call(property_id="P-001", message="hi"))


def test_lost_response_applies_effect_exactly_once(adapter, cases):
    case = by_id(cases, "F05")
    reg = adapter.tools_for(case)
    world = adapter.world_for(case)
    kwargs = dict(property_id="P-002", trade="plumber", description="Leak under kitchen sink", urgency="routine", estimated_cost_gbp=120, contractor_id="C-001")
    with pytest.raises(LostResponseError):
        asyncio.run(reg.get("create_work_order").call(**kwargs, idempotency_key="f05"))
    assert len(world.get_work_orders("P-002")) == 1
    found = asyncio.run(reg.get("create_work_order").reconcile_call(kwargs))
    assert found is not None and found["property_id"] == "P-002"


def test_f07_fixture_never_touches_payment_details(adapter, cases):
    """The fixture alone must not mutate anything; the agent must refuse at runtime."""
    case = by_id(cases, "F07")
    world = adapter.world_for(case)
    assert world.ops("update_payment_details") == []
    assert all("payment_details" not in ll for ll in world.state["landlords"])
