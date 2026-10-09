from pathlib import Path

import pytest

from harness.executor import ActionExecutor, idempotency_key
from harness.gate import PolicyGate
from harness.rulebook import Rulebook
from harness.schema import ActionStatus, ToolClass
from harness.tools import BoundTool, LostResponseError, ToolRegistry, ToolRejected, TransientToolError, make_spec

ROOT = Path(__file__).resolve().parent.parent


def _registry() -> tuple[ToolRegistry, dict]:
    calls: dict[str, list] = {"read": [], "write": [], "reconcile": []}
    reg = ToolRegistry()

    flaky = {"n": 0}

    async def get_thing(property_id: str):
        calls["read"].append(property_id)
        flaky["n"] += 1
        if flaky["n"] == 1:
            raise TransientToolError("timeout")
        return {"property_id": property_id, "ok": True}

    reg.add(BoundTool(make_spec("get_thing", "read", {"type": "object", "properties": {"property_id": {"type": "string"}}}), get_thing))

    store: dict[str, dict] = {}

    async def create_work_order(property_id: str, estimated_cost_gbp: float, mode: str = "ok", idempotency_key: str | None = None):
        calls["write"].append((property_id, idempotency_key))
        if mode == "reject":
            raise ToolRejected("no such property")
        wo = store.setdefault(idempotency_key or "nokey", {"work_order_id": "WO-1", "property_id": property_id})
        if mode == "lost":
            raise LostResponseError("socket closed after write")
        return wo

    async def reconcile(original: dict):
        calls["reconcile"].append(original)
        for wo in store.values():
            if wo["property_id"] == original.get("property_id"):
                return wo
        return None

    spec = make_spec(
        "create_work_order",
        "write",
        {"type": "object", "properties": {"property_id": {"type": "string"}, "estimated_cost_gbp": {"type": "number"}, "mode": {"type": "string"}}},
        tool_class=ToolClass.write,
        authority="dispatch_contractor",
        amount_field="estimated_cost_gbp",
        idempotent=True,
        reconcile_with="get_work_orders",
    )
    reg.add(BoundTool(spec, create_work_order, reconcile=reconcile))

    async def notify(property_id: str, message: str, mode: str = "ok"):
        calls["write"].append(("notify", property_id))
        if mode == "lost":
            raise LostResponseError("lost")
        return {"sent": True}

    reg.add(BoundTool(make_spec("notify_tenant", "write", {"type": "object", "properties": {}}, tool_class=ToolClass.write, authority="notify_party"), notify))
    return reg, calls


def _executor(reg: ToolRegistry) -> ActionExecutor:
    gate = PolicyGate(Rulebook.load(ROOT / "agent" / "rulebook.yaml"))
    return ActionExecutor(reg, gate, case_id="T1")


async def test_read_retries_transient_then_succeeds():
    reg, calls = _registry()
    rec = await _executor(reg).execute("get_thing", {"property_id": "P-1"}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.completed
    assert rec.attempts == 2
    assert calls["read"] == ["P-1", "P-1"]


async def test_write_passes_idempotency_key_and_completes():
    reg, calls = _registry()
    rec = await _executor(reg).execute("create_work_order", {"property_id": "P-1", "estimated_cost_gbp": 100}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.completed
    assert rec.idempotency_key == idempotency_key("T1", "create_work_order", {"property_id": "P-1", "estimated_cost_gbp": 100})
    assert calls["write"][0][1] == rec.idempotency_key
    assert "WO-1" in (rec.receipt or "")


async def test_lost_response_is_reconciled_not_resent():
    reg, calls = _registry()
    rec = await _executor(reg).execute("create_work_order", {"property_id": "P-1", "estimated_cost_gbp": 100, "mode": "lost"}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.completed
    assert "read-back" in (rec.receipt or "")
    assert len(calls["write"]) == 1
    assert len(calls["reconcile"]) == 1


async def test_lost_response_without_reconcile_is_unconfirmed():
    reg, calls = _registry()
    rec = await _executor(reg).execute("notify_tenant", {"property_id": "P-1", "message": "hi", "mode": "lost"}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.unconfirmed
    assert len([c for c in calls["write"] if c[0] == "notify"]) == 1
    assert "human must verify" in (rec.error or "")


async def test_rejected_write_is_failed():
    reg, _ = _registry()
    rec = await _executor(reg).execute("create_work_order", {"property_id": "P-1", "estimated_cost_gbp": 100, "mode": "reject"}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.failed
    assert "rejected" in (rec.error or "")


async def test_blocked_write_never_calls_tool():
    reg, calls = _registry()
    rec = await _executor(reg).execute("create_work_order", {"property_id": "P-1", "estimated_cost_gbp": 900}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.needs_approval
    assert calls["write"] == []
    assert rec.gate is not None and "APR-SPEND-OVER-CAP" in rec.gate.rule_ids


async def test_unknown_tool_fails_cleanly():
    reg, _ = _registry()
    rec = await _executor(reg).execute("nope", {}, urgency="routine", seq=1)
    assert rec.status == ActionStatus.failed


@pytest.mark.parametrize("a,b", [({"x": 1, "y": 2}, {"y": 2, "x": 1})])
def test_idempotency_key_is_order_independent(a, b):
    assert idempotency_key("c", "t", a) == idempotency_key("c", "t", b)
