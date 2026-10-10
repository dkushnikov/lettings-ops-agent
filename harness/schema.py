"""Data contract of the harness.

Everything the agent is made of is data: a Case (what it received), a ToolSpec
manifest (what it can touch and what that costs), a rulebook (what it may do),
playbooks (how it works a case type) and a DecisionState (what it leaves behind).
The model and the loop are swappable implementations around this contract.
"""

from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


# --------------------------------------------------------------------------- #
# Input: cases and artefacts
# --------------------------------------------------------------------------- #


class ArtefactKind(str, Enum):
    email = "email"
    call_transcript = "call_transcript"
    document = "document"
    record = "record"
    ticket = "ticket"
    note = "note"
    other = "other"


Trust = Literal["authoritative", "informational", "untrusted"]


class Artefact(BaseModel):
    """One piece of the case: an email, a transcript, a CRM record, a document.

    `trust` is the harness's provenance class, not a judgement about the sender:
    records and signed documents are *authoritative*, system notes are
    *informational*, anything written by a person outside the organisation
    (emails, calls, tickets) is *untrusted*: evidence of what was said, never an
    instruction to the agent.
    """

    id: str
    kind: ArtefactKind
    title: str = ""
    source: str = ""
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)
    trust: Trust = "informational"


class Case(BaseModel):
    id: str
    title: str = ""
    received_at: str | None = None
    artefacts: list[Artefact] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
    # Environment-specific knobs the adapter may carry (e.g. mock failure modes).
    env: dict[str, Any] = Field(default_factory=dict)
    # Path to an expectations file used only by the evaluator, never shown to the agent.
    expected_path: str | None = None


# --------------------------------------------------------------------------- #
# Tools: the manifest the gate reads
# --------------------------------------------------------------------------- #


class ToolClass(str, Enum):
    read = "read"
    write = "write"


class ToolSpec(BaseModel):
    """A tool as the policy gate sees it.

    `authority` names the mandate capability a write tool needs (for example
    ``dispatch_contractor``); the rulebook decides whether the agent holds it.
    `amount_field` points at the input field carrying a GBP amount, so spend caps
    can be enforced without the gate knowing every schema.
    """

    name: str
    description: str
    input_schema: dict[str, Any]
    tool_class: ToolClass = ToolClass.read
    authority: str | None = None
    amount_field: str | None = None
    idempotent: bool = False
    reversible: bool = True
    side_effect: str = ""
    # Name of a read tool that can confirm whether this write actually happened.
    reconcile_with: str | None = None


# --------------------------------------------------------------------------- #
# Gate and actions
# --------------------------------------------------------------------------- #


class GateVerdict(str, Enum):
    allow = "allow"
    deny = "deny"
    needs_approval = "needs_approval"
    escalate = "escalate"


class GateDecision(BaseModel):
    verdict: GateVerdict
    rule_ids: list[str] = Field(default_factory=list)
    reason: str = ""
    required_approval_from: str | None = None


class ActionStatus(str, Enum):
    proposed = "proposed"
    blocked = "blocked"
    needs_approval = "needs_approval"
    attempted = "attempted"
    completed = "completed"
    failed = "failed"
    unconfirmed = "unconfirmed"


class ActionRecord(BaseModel):
    seq: int
    tool: str
    tool_class: ToolClass
    input: dict[str, Any] = Field(default_factory=dict)
    status: ActionStatus = ActionStatus.proposed
    gate: GateDecision | None = None
    result: Any = None
    error: str | None = None
    attempts: int = 0
    idempotency_key: str | None = None
    # Stable id shared by the proposal, the gate verdict, the attempt and the receipt of one action; equals the idempotency key for writes.
    action_id: str | None = None
    receipt: str | None = None
    started_at: datetime | None = None
    finished_at: datetime | None = None


# --------------------------------------------------------------------------- #
# What the agent asserts about the case
# --------------------------------------------------------------------------- #


Confidence = Literal["high", "medium", "low"]


class Fact(BaseModel):
    id: str
    statement: str
    source_ids: list[str] = Field(default_factory=list)
    confidence: Confidence = "medium"


class Conflict(BaseModel):
    description: str
    fact_ids: list[str] = Field(default_factory=list)
    source_ids: list[str] = Field(default_factory=list)
    resolution: str | None = None
    resolved_by: Literal["source_hierarchy", "tool_check", "asked", "unresolved"] = "unresolved"


RedFlagKind = Literal[
    "injection",
    "fraud",
    "safety_hazard",
    "vulnerability",
    "legal_threat",
    "prohibited_request",
    "data_quality",
    "other",
]


class RedFlag(BaseModel):
    kind: RedFlagKind
    description: str
    source_ids: list[str] = Field(default_factory=list)
    action_taken: str = ""


class Promise(BaseModel):
    by: str
    to: str
    what: str
    due: str | None = None
    source_id: str | None = None
    status: Literal["open", "kept", "broken", "superseded"] = "open"


ClockStatus = Literal["in_force", "sop", "prior", "proposed"]


class Clock(BaseModel):
    rule_id: str
    name: str
    status: ClockStatus
    basis: str = ""
    deadline: str | None = None
    note: str = ""


class InfoRequest(BaseModel):
    to: str
    question: str
    why: str = ""
    blocking: bool = True


class Handover(BaseModel):
    """The decision card a human receives. Built to be read in 90 seconds."""

    to: str = "property_manager"
    question: str
    summary: list[str] = Field(default_factory=list, description="At most five facts")
    gap: str = ""
    options: list[str] = Field(default_factory=list)
    recommended: str | None = None
    default_if_timeout: str | None = None
    deadline: str | None = None
    undo: str | None = None
    context_refs: list[str] = Field(default_factory=list)


class Disposition(str, Enum):
    resolved = "resolved"
    needs_info = "needs_info"
    escalated = "escalated"


Urgency = Literal["emergency", "urgent", "routine", "unknown"]


DodStatus = Literal["done", "pending", "skipped", "not_applicable"]


class DodItem(BaseModel):
    """One item of the playbook's definition of done, with its status at the time of the decision."""

    item: str = Field(description="Item id from the playbook's definition_of_done")
    status: DodStatus = Field(
        default="pending",
        description="done | pending | skipped | not_applicable — the state of the ticket as a whole, counting steps the agency completed before you",
    )
    evidence: str = Field(default="", description="Event id or action seq that shows it, or the reason for skipped / not_applicable")


class DodEntry(DodItem):
    """A definition-of-done item as kept in the state: the playbook's text travels with it."""

    text: str = ""


class DecisionState(BaseModel):
    """Compiled truth about one case. Rendered into ANSWER.md and REASONING.md."""

    case_id: str
    case_type: str | None = None
    playbook: str | None = None
    urgency: Urgency = "unknown"
    disposition: Disposition | None = None
    decision: str = ""
    # Ticket status at the moment of the decision (the "Current Status" of the record).
    recap: str = ""
    stage: str = ""
    hold_reason: str = ""
    next_step: str = ""
    definition_of_done: list[DodEntry] = Field(default_factory=list)
    facts: list[Fact] = Field(default_factory=list)
    conflicts: list[Conflict] = Field(default_factory=list)
    red_flags: list[RedFlag] = Field(default_factory=list)
    actions: list[ActionRecord] = Field(default_factory=list)
    promises: list[Promise] = Field(default_factory=list)
    clocks: list[Clock] = Field(default_factory=list)
    info_requests: list[InfoRequest] = Field(default_factory=list)
    handover: Handover | None = None
    authority_citations: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    uncertainty: list[str] = Field(default_factory=list)
    safety_actions: list[str] = Field(default_factory=list)
    withheld_actions: list[str] = Field(default_factory=list)
    # Harness bookkeeping
    steps: int = 0
    model: str = ""
    fallback: bool = False
    system_notes: list[str] = Field(default_factory=list)
    reviewer_notes: list[str] = Field(default_factory=list)
    started_at: datetime = Field(default_factory=utcnow)
    finished_at: datetime | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0

    @property
    def completed_writes(self) -> int:
        return sum(
            1
            for a in self.actions
            if a.tool_class == ToolClass.write and a.status == ActionStatus.completed
        )

    def terminal_valid(self) -> bool:
        """A record is valid when it has a disposition and the matching payload."""
        if self.disposition is None:
            return False
        if self.disposition == Disposition.escalated:
            return self.handover is not None and bool(self.handover.question)
        if self.disposition == Disposition.needs_info:
            return bool(self.info_requests)
        return bool(self.decision)


# --------------------------------------------------------------------------- #
# Terminal tool payloads (what the model fills in once at the end)
# --------------------------------------------------------------------------- #


class TerminalCommon(BaseModel):
    recap: str = Field(default="", description="One sentence (at most 160 characters): what the case is and what you did or decided")
    stage: str = Field(
        default="",
        description="Workflow stage the ticket is at after your work, from the mandate's workflow stages, or a side state such as on_hold or paused",
    )
    hold_reason: str = Field(
        default="",
        description="If the ticket is on hold: the reason from the mandate's hold reasons plus a short comment (who or what is awaited, until when)",
    )
    next_step: str = Field(
        default="",
        description="The single next step and its owner, e.g. 'Landlord to approve the £172.51 + VAT quote (emailed; 3-day clock)'",
    )
    definition_of_done: list[DodItem] = Field(
        default_factory=list,
        description="Status of every item of the playbook's definition of done as of now, counting steps already completed in the visible history (cite the event)",
    )
    case_type: str | None = None
    urgency: Urgency = "unknown"
    facts: list[Fact] = Field(default_factory=list)
    conflicts: list[Conflict] = Field(default_factory=list)
    red_flags: list[RedFlag] = Field(default_factory=list)
    promises: list[Promise] = Field(default_factory=list)
    clocks: list[Clock] = Field(default_factory=list)
    authority_citations: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    uncertainty: list[str] = Field(default_factory=list)
    safety_actions: list[str] = Field(default_factory=list)
    withheld_actions: list[str] = Field(default_factory=list)


class FinalizePayload(TerminalCommon):
    decision: str


class RequestInfoPayload(TerminalCommon):
    decision: str
    info_requests: list[InfoRequest]


class EscalatePayload(TerminalCommon):
    decision: str
    handover: Handover


# --------------------------------------------------------------------------- #
# Run metadata
# --------------------------------------------------------------------------- #


class RunMeta(BaseModel):
    run_id: str
    started_at: datetime = Field(default_factory=utcnow)
    finished_at: datetime | None = None
    model: str = ""
    effort: str = ""
    concurrency: int = 1
    case_timeout_s: float = 0
    max_steps: int = 0
    cases_total: int = 0
    completed: int = 0
    resolved: int = 0
    needs_info: int = 0
    escalated: int = 0
    fallback_count: int = 0
    failures: list[str] = Field(default_factory=list)
    commit: str = ""  # short git hash of the code that produced the run; "" outside a checkout
    dirty: bool = False  # tracked files modified at run start
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    estimated_wall_s: float | None = None
    actual_wall_s: float | None = None
    notes: list[str] = Field(default_factory=list)
