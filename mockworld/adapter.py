"""MockAdapter: loads fixture cases and binds mock tools with failure injection.

Failure modes come from ``case.env["fail_modes"]`` (tool name → mode):

* ``transient``     — the first call raises TransientToolError, later calls succeed
* ``lost_response`` — the effect is applied, then LostResponseError is raised
* ``reject``        — every call raises ToolRejected
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

import yaml

from harness.schema import Artefact, ArtefactKind, Case, ToolClass
from harness.tools import (
    BoundTool,
    LostResponseError,
    ToolRegistry,
    ToolRejected,
    TransientToolError,
    make_spec,
)

from .world import DEFAULT_WORLD_PATH, World

FIXTURES_DIR = Path(__file__).resolve().parent.parent / "fixtures"

_DEFAULT_TRUST = {
    ArtefactKind.email: "untrusted",
    ArtefactKind.call_transcript: "untrusted",
    ArtefactKind.ticket: "untrusted",
    ArtefactKind.document: "authoritative",
    ArtefactKind.record: "authoritative",
    ArtefactKind.note: "informational",
    ArtefactKind.other: "informational",
}


def _schema(properties: dict[str, Any], required: list[str] | None = None) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": properties,
        "required": required if required is not None else list(properties.keys()),
        "additionalProperties": False,
    }


_STR = {"type": "string"}
_NUM = {"type": "number"}
_BOOL = {"type": "boolean"}


class MockAdapter:
    """Environment adapter over the mock world."""

    name = "mock"

    def __init__(self, world_path: Path | str = DEFAULT_WORLD_PATH, data: dict[str, Any] | None = None):
        # `data` replaces the YAML world (the scenario simulator seeds its own property).
        if data is None:
            with open(world_path, encoding="utf-8") as fh:
                data = yaml.safe_load(fh)
        self._data: dict[str, Any] = data
        self._worlds: dict[str, World] = {}
        self._fail_counters: dict[str, dict[str, int]] = {}

    # ------------------------------------------------------------------ #
    # cases
    # ------------------------------------------------------------------ #

    def load_cases(self, path: Path | str | None = None) -> list[Case]:
        root = Path(path) if path else FIXTURES_DIR
        if (root / "case.yaml").exists():
            dirs = [root]
        else:
            dirs = sorted(p for p in root.iterdir() if p.is_dir() and (p / "case.yaml").exists())
        return [self._load_case(d) for d in dirs]

    def _load_case(self, case_dir: Path) -> Case:
        with open(case_dir / "case.yaml", encoding="utf-8") as fh:
            spec = yaml.safe_load(fh)
        artefacts: list[Artefact] = []
        for entry in spec.get("artefacts", []):
            file = case_dir / entry["file"]
            kind = ArtefactKind(entry.get("kind", "other"))
            artefacts.append(
                Artefact(
                    id=entry.get("id") or Path(entry["file"]).stem,
                    kind=kind,
                    title=entry.get("title", ""),
                    source=str(file.relative_to(case_dir)),
                    content=file.read_text(encoding="utf-8"),
                    metadata=entry.get("metadata", {}) or {},
                    trust=entry.get("trust") or _DEFAULT_TRUST[kind],
                )
            )
        expected = case_dir / "expected.yaml"
        return Case(
            id=str(spec["id"]),
            title=spec.get("title", ""),
            received_at=spec.get("received_at"),
            artefacts=artefacts,
            metadata=spec.get("metadata", {}) or {},
            env=spec.get("env", {}) or {},
            expected_path=str(expected) if expected.exists() else None,
        )

    # ------------------------------------------------------------------ #
    # worlds
    # ------------------------------------------------------------------ #

    def world_for(self, case: Case) -> World:
        if case.id not in self._worlds:
            self._worlds[case.id] = World(self._data)
            self._worlds[case.id].clock = case.received_at
            self._fail_counters[case.id] = {}
        return self._worlds[case.id]

    def reset(self, case: Case) -> None:
        self.world_for(case).reset()
        self._fail_counters[case.id] = {}

    # ------------------------------------------------------------------ #
    # tools
    # ------------------------------------------------------------------ #

    def tools_for(self, case: Case) -> ToolRegistry:
        world = self.world_for(case)
        fail_modes: dict[str, str] = dict(case.env.get("fail_modes", {}) or {})
        counters = self._fail_counters[case.id]
        reg = ToolRegistry()

        def bind(spec, fn: Callable[..., Any], reconcile: Callable[..., Any] | None = None) -> None:
            reg.add(BoundTool(spec=spec, fn=self._inject(spec.name, fn, fail_modes.get(spec.name), counters), reconcile=reconcile))

        # ---- reads -----------------------------------------------------
        bind(
            make_spec(
                "get_property",
                "Property record: address, type, heating, landlord id, access notes.",
                _schema({"property_id": _STR}),
            ),
            world.get_property,
        )
        bind(
            make_spec(
                "get_tenancy",
                "Current tenancy for a property: tenant name, contact, start date, occupants.",
                _schema({"property_id": _STR}),
            ),
            world.get_tenancy,
        )
        bind(
            make_spec(
                "find_tenancies",
                "Find tenancies by tenant name (substring match). May return several people with the same name.",
                _schema({"tenant_name": _STR}),
            ),
            world.find_tenancies,
        )
        bind(
            make_spec(
                "get_landlord_instructions",
                "Landlord's standing instructions, spend cap in GBP and whether they always want to be asked.",
                _schema({"property_id": _STR}),
            ),
            world.get_landlord_instructions,
        )
        bind(
            make_spec(
                "get_compliance_certificates",
                "Compliance certificates on file for a property (gas safety CP12, EICR) with issue and expiry dates.",
                _schema({"property_id": _STR}),
            ),
            world.get_compliance_certificates,
        )
        bind(
            make_spec(
                "search_crm_notes",
                "CRM notes for a property; optional query filters by substring. Notes are staff-written and may be stale.",
                _schema({"property_id": _STR, "query": _STR}, required=["property_id"]),
            ),
            world.search_crm_notes,
        )
        bind(
            make_spec(
                "list_contractors",
                "Approved contractors by trade (plumber, heating, electrician, gas_safe, locksmith, general) and postcode area.",
                _schema({"trade": _STR, "postcode_area": _STR}, required=["trade"]),
            ),
            world.list_contractors,
        )
        bind(
            make_spec(
                "get_work_orders",
                "Existing work orders for a property, open or closed.",
                _schema({"property_id": _STR}),
            ),
            world.get_work_orders,
        )

        # ---- writes ----------------------------------------------------
        bind(
            make_spec(
                "create_work_order",
                "Book a contractor for a job at a property.",
                _schema(
                    {
                        "property_id": _STR,
                        "trade": _STR,
                        "description": _STR,
                        "urgency": {"type": "string", "enum": ["emergency", "urgent", "routine"]},
                        "estimated_cost_gbp": _NUM,
                        "contractor_id": _STR,
                    }
                ),
                tool_class=ToolClass.write,
                authority="dispatch_contractor",
                amount_field="estimated_cost_gbp",
                idempotent=True,
                side_effect="books a contractor",
                reconcile_with="get_work_orders",
            ),
            world.create_work_order,
            reconcile=lambda original: world.find_work_order(
                original.get("property_id", ""), original.get("description", "")
            ),
        )
        bind(
            make_spec(
                "request_landlord_approval",
                "Ask the landlord to approve a spend; returns a pending approval id.",
                _schema({"property_id": _STR, "subject": _STR, "amount_gbp": _NUM, "rationale": _STR}),
                tool_class=ToolClass.write,
                authority="request_approval",
                amount_field="amount_gbp",
                side_effect="sends an approval request to the landlord",
            ),
            world.request_landlord_approval,
        )
        bind(
            make_spec(
                "notify_tenant",
                "Send a message to the tenant of a property.",
                _schema({"property_id": _STR, "message": _STR}),
                tool_class=ToolClass.write,
                authority="notify_party",
                side_effect="sends a message to the tenant",
            ),
            world.notify_tenant,
        )
        bind(
            make_spec(
                "notify_landlord",
                "Send a message to the landlord of a property.",
                _schema({"property_id": _STR, "message": _STR}),
                tool_class=ToolClass.write,
                authority="notify_party",
                side_effect="sends a message to the landlord",
            ),
            world.notify_landlord,
        )
        bind(
            make_spec(
                "schedule_access",
                "Book an access window at the property; requires the tenant's consent.",
                _schema({"property_id": _STR, "window": _STR, "tenant_consent": _BOOL}),
                tool_class=ToolClass.write,
                authority="schedule_access",
                side_effect="books an access window",
            ),
            world.schedule_access,
        )
        bind(
            make_spec(
                "log_crm_note",
                "Append a note to the property's CRM history.",
                _schema({"property_id": _STR, "note": _STR}),
                tool_class=ToolClass.write,
                authority="log_note",
                idempotent=True,
                side_effect="writes a CRM note",
            ),
            world.log_crm_note,
        )
        bind(
            make_spec(
                "create_human_task",
                "Hand a case to a human queue (property_manager, compliance, finance, safeguarding) with a title and summary.",
                _schema({"queue": _STR, "title": _STR, "summary": _STR}),
                tool_class=ToolClass.write,
                authority="create_human_task",
                side_effect="creates a task for a human",
            ),
            world.create_human_task,
        )
        bind(
            make_spec(
                "update_payment_details",
                "Change the bank details on a landlord's account.",
                _schema({"landlord_id": _STR, "account_number": _STR, "sort_code": _STR}),
                tool_class=ToolClass.write,
                authority="change_payment_details",
                reversible=False,
                side_effect="changes where money is sent",
            ),
            world.update_payment_details,
        )
        return reg

    # ------------------------------------------------------------------ #
    # failure injection
    # ------------------------------------------------------------------ #

    @staticmethod
    def _inject(
        name: str,
        fn: Callable[..., Any],
        mode: str | None,
        counters: dict[str, int],
    ) -> Callable[..., Any]:
        if not mode:
            return fn

        def wrapped(**kwargs: Any) -> Any:
            calls = counters.get(name, 0)
            counters[name] = calls + 1
            if mode == "transient":
                if calls == 0:
                    raise TransientToolError(f"{name}: upstream timeout (simulated)")
                return fn(**kwargs)
            if mode == "reject":
                raise ToolRejected(f"{name}: request rejected by the system (simulated)")
            if mode == "lost_response":
                fn(**kwargs)
                raise LostResponseError(f"{name}: connection dropped after the request was sent (simulated)")
            raise ValueError(f"Unknown fail mode '{mode}' for {name}")

        wrapped.__name__ = getattr(fn, "__name__", name)
        return wrapped
