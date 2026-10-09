"""In-memory lettings world with resettable state and a mutation log.

Reads return plain dicts/lists; writes mutate state and append to ``log``.
``create_work_order`` is idempotent on ``idempotency_key`` so the executor can
retry a lost response without booking a second contractor.
"""

from __future__ import annotations

import copy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from harness.tools import ToolRejected

DEFAULT_WORLD_PATH = Path(__file__).parent / "data" / "world.yaml"


def _now_iso(clock: str | None = None) -> str:
    """World time: the case's own clock when set (so records date from the case), else now."""
    if clock:
        return clock
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class World:
    """One case's view of the lettings environment.

    ``reset()`` restores the state loaded from YAML, so every case starts from
    the same world and the executor's side effects never leak across cases.
    """

    def __init__(self, data: dict[str, Any]):
        self._base = copy.deepcopy(data)
        self.clock: str | None = None
        self.state: dict[str, Any] = {}
        self.log: list[dict[str, Any]] = []
        self._idempotency: dict[str, str] = {}
        self._counters: dict[str, int] = {}
        self.reset()

    @classmethod
    def load(cls, path: Path | str = DEFAULT_WORLD_PATH) -> "World":
        with open(path, encoding="utf-8") as fh:
            return cls(yaml.safe_load(fh))

    def reset(self) -> None:
        self.state = copy.deepcopy(self._base)
        self.state.setdefault("work_orders", [])
        self.state.setdefault("approvals", [])
        self.state.setdefault("messages", [])
        self.state.setdefault("access_bookings", [])
        self.state.setdefault("human_tasks", [])
        self.log = []
        self._idempotency = {}
        existing = [
            int(wo["id"].split("-")[1])
            for wo in self.state["work_orders"]
            if str(wo.get("id", "")).startswith("WO-")
        ]
        self._counters = {
            "WO": (max(existing) + 1) if existing else 1001,
            "APR": 1,
            "MSG": 1,
            "ACC": 1,
            "HT": 1,
        }

    # ------------------------------------------------------------------ #
    # helpers
    # ------------------------------------------------------------------ #

    def _next_id(self, prefix: str) -> str:
        n = self._counters[prefix]
        self._counters[prefix] = n + 1
        return f"{prefix}-{n}"

    def _record(self, op: str, inputs: dict[str, Any], result: Any) -> None:
        self.log.append({"op": op, "input": inputs, "result": result, "at": _now_iso(self.clock)})

    def _property(self, property_id: str) -> dict[str, Any]:
        for p in self.state["properties"]:
            if p["id"] == property_id:
                return p
        raise ToolRejected(f"Unknown property_id '{property_id}'")

    # ------------------------------------------------------------------ #
    # reads
    # ------------------------------------------------------------------ #

    def get_property(self, property_id: str) -> dict[str, Any]:
        return copy.deepcopy(self._property(property_id))

    def get_tenancy(self, property_id: str) -> dict[str, Any]:
        self._property(property_id)
        for t in self.state["tenancies"]:
            if t["property_id"] == property_id:
                return copy.deepcopy(t)
        raise ToolRejected(f"No active tenancy for '{property_id}'")

    def find_tenancies(self, tenant_name: str) -> list[dict[str, Any]]:
        needle = tenant_name.strip().lower()
        hits = [
            copy.deepcopy(t)
            for t in self.state["tenancies"]
            if needle and needle in t["tenant_name"].lower()
        ]
        for t in hits:
            t["property"] = self.get_property(t["property_id"])
        return hits

    def get_landlord_instructions(self, property_id: str) -> dict[str, Any]:
        prop = self._property(property_id)
        for ll in self.state["landlords"]:
            if ll["id"] == prop["landlord_id"]:
                return {
                    "landlord_id": ll["id"],
                    "name": ll["name"],
                    "standing_instructions": ll["standing_instructions"].strip(),
                    "spend_cap_gbp": ll["spend_cap_gbp"],
                    "always_ask": ll["always_ask"],
                }
        raise ToolRejected(f"No landlord on file for '{property_id}'")

    def get_compliance_certificates(self, property_id: str) -> list[dict[str, Any]]:
        self._property(property_id)
        return [
            copy.deepcopy(c)
            for c in self.state["compliance_certificates"]
            if c["property_id"] == property_id
        ]

    def search_crm_notes(self, property_id: str, query: str = "") -> list[dict[str, Any]]:
        self._property(property_id)
        q = (query or "").strip().lower()
        return [
            copy.deepcopy(n)
            for n in self.state["crm_notes"]
            if n["property_id"] == property_id and (not q or q in n["note"].lower())
        ]

    def list_contractors(self, trade: str, postcode_area: str = "") -> list[dict[str, Any]]:
        trade_l = trade.strip().lower()
        area = (postcode_area or "").strip().upper()
        return [
            copy.deepcopy(c)
            for c in self.state["contractors"]
            if c["trade"] == trade_l and (not area or area in c["postcode_areas"])
        ]

    def get_work_orders(self, property_id: str) -> list[dict[str, Any]]:
        self._property(property_id)
        return [copy.deepcopy(w) for w in self.state["work_orders"] if w["property_id"] == property_id]

    # ------------------------------------------------------------------ #
    # writes
    # ------------------------------------------------------------------ #

    def create_work_order(
        self,
        property_id: str,
        trade: str,
        description: str,
        urgency: str,
        estimated_cost_gbp: float,
        contractor_id: str,
        idempotency_key: str | None = None,
        **_: Any,
    ) -> dict[str, Any]:
        if idempotency_key and idempotency_key in self._idempotency:
            wo_id = self._idempotency[idempotency_key]
            existing = next(w for w in self.state["work_orders"] if w["id"] == wo_id)
            self._record("create_work_order", {"idempotency_key": idempotency_key}, {"id": wo_id, "deduplicated": True})
            return {**copy.deepcopy(existing), "deduplicated": True}
        self._property(property_id)
        if not any(c["id"] == contractor_id for c in self.state["contractors"]):
            raise ToolRejected(f"Unknown contractor_id '{contractor_id}'")
        wo = {
            "id": self._next_id("WO"),
            "property_id": property_id,
            "trade": trade,
            "description": description,
            "urgency": urgency,
            "estimated_cost_gbp": estimated_cost_gbp,
            "contractor_id": contractor_id,
            "status": "open",
            "created_at": _now_iso(self.clock),
        }
        self.state["work_orders"].append(wo)
        if idempotency_key:
            self._idempotency[idempotency_key] = wo["id"]
        self._record("create_work_order", {k: v for k, v in wo.items() if k != "created_at"}, {"id": wo["id"]})
        return copy.deepcopy(wo)

    def find_work_order(self, property_id: str, description: str) -> dict[str, Any] | None:
        """Reconcile helper: an open work order for this property and description."""
        for w in self.state["work_orders"]:
            if w["property_id"] == property_id and w["description"] == description:
                return copy.deepcopy(w)
        return None

    def request_landlord_approval(
        self, property_id: str, subject: str, amount_gbp: float, rationale: str, **_: Any
    ) -> dict[str, Any]:
        prop = self._property(property_id)
        apr = {
            "id": self._next_id("APR"),
            "property_id": property_id,
            "landlord_id": prop["landlord_id"],
            "subject": subject,
            "amount_gbp": amount_gbp,
            "rationale": rationale,
            "status": "pending",
            "requested_at": _now_iso(self.clock),
        }
        self.state["approvals"].append(apr)
        self._record("request_landlord_approval", apr, {"id": apr["id"]})
        return copy.deepcopy(apr)

    def _send(self, to_role: str, property_id: str, message: str) -> dict[str, Any]:
        self._property(property_id)
        msg = {
            "id": self._next_id("MSG"),
            "to": to_role,
            "property_id": property_id,
            "message": message,
            "sent_at": _now_iso(self.clock),
        }
        self.state["messages"].append(msg)
        self._record(f"notify_{to_role}", {"property_id": property_id, "message": message}, {"id": msg["id"]})
        return copy.deepcopy(msg)

    def notify_tenant(self, property_id: str, message: str, **_: Any) -> dict[str, Any]:
        return self._send("tenant", property_id, message)

    def notify_landlord(self, property_id: str, message: str, **_: Any) -> dict[str, Any]:
        return self._send("landlord", property_id, message)

    def schedule_access(
        self, property_id: str, window: str, tenant_consent: bool, **_: Any
    ) -> dict[str, Any]:
        self._property(property_id)
        if not tenant_consent:
            raise ToolRejected("Access cannot be scheduled without the tenant's consent")
        booking = {
            "id": self._next_id("ACC"),
            "property_id": property_id,
            "window": window,
            "tenant_consent": True,
            "booked_at": _now_iso(self.clock),
        }
        self.state["access_bookings"].append(booking)
        self._record("schedule_access", booking, {"id": booking["id"]})
        return copy.deepcopy(booking)

    def log_crm_note(self, property_id: str, note: str, **_: Any) -> dict[str, Any]:
        self._property(property_id)
        entry = {"property_id": property_id, "date": _now_iso(self.clock)[:10], "author": "agent", "note": note}
        self.state["crm_notes"].append(entry)
        self._record("log_crm_note", entry, {"ok": True})
        return {"ok": True, "note": copy.deepcopy(entry)}

    def create_human_task(self, queue: str, title: str, summary: str, **_: Any) -> dict[str, Any]:
        task = {
            "id": self._next_id("HT"),
            "queue": queue,
            "title": title,
            "summary": summary,
            "status": "open",
            "created_at": _now_iso(self.clock),
        }
        self.state["human_tasks"].append(task)
        self._record("create_human_task", task, {"id": task["id"]})
        return copy.deepcopy(task)

    def update_payment_details(
        self, landlord_id: str, account_number: str, sort_code: str, **_: Any
    ) -> dict[str, Any]:
        for ll in self.state["landlords"]:
            if ll["id"] == landlord_id:
                ll["payment_details"] = {"account_number": account_number, "sort_code": sort_code}
                self._record(
                    "update_payment_details",
                    {"landlord_id": landlord_id, "account_number": account_number, "sort_code": sort_code},
                    {"status": "updated"},
                )
                return {"status": "updated", "landlord_id": landlord_id}
        raise ToolRejected(f"Unknown landlord_id '{landlord_id}'")

    # ------------------------------------------------------------------ #
    # inspection helpers for tests and traces
    # ------------------------------------------------------------------ #

    def work_orders(self) -> list[dict[str, Any]]:
        return copy.deepcopy(self.state["work_orders"])

    def ops(self, name: str) -> list[dict[str, Any]]:
        return [e for e in self.log if e["op"] == name]
