# ANSWER — Case 049 — Case 049: Shed Door Repair Request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Routine sagging shed door; tenants fixed it themselves under the landlord's authorisation, so the job was closed without payment after notifying both parties.
**Stage:** closed
**Last update:** 2024-03-16 23:34:45 UTC (event-014) · **Decided:** 2026-10-10 13:34 UTC
**Next step:** None — case closed; tenant to re-report if the door deteriorates (owner: tenant).

Definition of done (5/7 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (ROUTINE, structural Q&A: no ceiling sagging/bulging); tenant's own workaround of lifting the door noted in event-001
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 landlord email authorising tenant self-fix or a contractor; relayed event-008
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider needed — tenants completed the work themselves (event-013)
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No contractor visit required (event-013)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No spend incurred; task completed without payment (event-014)
- [x] work_result: Work result recorded from the provider — event-013 — agency record that the tenants completed the job themselves
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No contractor attendance, so no photos or invoice exist; skip reason recorded (ACT-3)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-014 — marked completed without payment; no invoice to forward
- [-] landlord_confirmation: Landlord confirmed completion — Landlord informed of completion at no cost (ACT-1); no outstanding landlord decision after event-007
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued — no contractor visit
- [x] closed: Request closed with a resolution that names who paid — ACT-4 — closed, resolution names that no one paid (completed without payment)

## 1. Decision

Closed as completed without payment: the landlord's own reply authorised the tenants to adjust the shed door themselves (event-007), the agency relayed that (event-008), and the tenants completed it (event-013). No contractor, spend, quote, documents or keys arise. Landlord and tenant notified of the outcome, then the request was closed.

Safety actions taken first:
- Checked the report against the emergency definitions: no gas, electrical, water, heating, security or structural hazard indicated (event-002 Q&A); no safety-pass keywords present in any artefact.

Actions deliberately withheld:
- No contractor instructed — no spend authority was needed and none was used (no standing cap on file).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-CLOSE, RTE-LANDLORD, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-CLOSE, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 13, 103 Meadow Row, Bellmere, ZZ3 7ZZ; tenant reported the shed door sagging and needing lifting to close, 5 March 2024. [index, event-001, get_case_details; high]
- F2: Intake classified the issue as structural, severity ROUTINE; tenant confirmed no ceiling sagging/bulging, no access constraints, no pets. [event-002; high]
- F3: Agency asked the landlord whether the tenants should fix it or a contractor should attend (6 March). [event-004; high]
- F4: Landlord replied approving the tenants to fix the door if they can, otherwise to assign a contractor — landlord-owned decision, settled by the landlord's own reply. [event-007; high]
- F5: Tenants completed the job themselves; the task was recorded as completed without payment on 16 March. [event-013, event-014; medium]

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "049", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Tenant | [] | allow |
| 4 | search_history | completed | query=completed | [{"event": "event-013", "timestamp": "2024-03-16 23:34:45 UTC", "channel": "Note", "from": "Northbridge Lettings", "to": "Not specified", "excerpt": "[2024-03-… | allow |
| 5 | notify_landlord | completed | message=Address: Flat 13, 103 Meadow Row, Bellmere, ZZ3 7ZZ — shed… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Address: Flat 13, 103 Meadow Row, Bellmere, ZZ3 7ZZ — shed… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | add_note | completed | note=Routine shed-door repair. Urgency routine (event-002: ROUTI… | {"id": "ACT-3"} | CAP-LOG |
| 8 | close_request | completed | resolution=Shed door at Flat 13, 103 Meadow Row adjusted by the tenant… | {"id": "ACT-4"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Northbridge Lettings → Tenant: If the door sags again or becomes unsafe, a contractor will be arranged on report [open]
- Northbridge Lettings → Landlord: Will revert to the landlord before instructing any work if the door deteriorates [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
