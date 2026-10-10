# ANSWER — Case 048 — Case 048: Bathroom Window Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window repair ticket closed on completion reports naming a different property; conflict logged, contractor and tenant chased, escalated to verify or reopen.
**Stage:** final_checks · **Hold:** Waiting for Provider — Riverside Solutions to confirm which address was attended and the result (2 working days); office to decide on reopening.
**Last update:** 2024-12-17 00:50:21 UTC (event-036) · **Decided:** 2026-10-10 14:14 UTC
**Next step:** Property manager to decide whether to reopen Case 048 and re-dispatch to Flat 20 and to check no invoice was raised against the wrong property; contractor reply due within 2 working days (ACT-2).

Definition of done (4/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 fault logged and categorised as a window repair; urgency routine (no emergency definition matched)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 — landlord's own message 'Yes please get that sorted' (no amount named)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-009, event-011 provider briefed; event-010 tenant told who is attending
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-018 slot 12/12/2024 15:57; event-019 and event-020 confirmed to contractor and tenant
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-024 quote contents unavailable; event-026 is a system status line, not a landlord message — no amount or VAT evidenced (RTE-LANDLORD)
- [ ] work_result: Work result recorded from the provider — event-016, event-017 report completion at a different property (Flat 7, 177 Beacon Close); no result for Flat 20 — contractor asked (ACT-2), tenant asked (ACT-3)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-032 skip reason 'all works completed' — unsupported given the address mismatch
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice on file; no forwarding event in the history
- [ ] landlord_confirmation: Landlord confirmed completion — event-033 'Need confirmation from landlord'; no landlord message confirming completion
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issue event; event-035 keys line failed validation (assumption: tenant-attended visit)
- [ ] closed: Request closed with a resolution that names who paid — event-036 closed, but resolution names neither the verified work nor who paid; referred to property manager (ACT-4)

## 1. Decision

Case 048 was closed (event-036) on the strength of two contractor completion reports that name a different property (event-016, event-017: "Flat 7, 177 Beacon Close, Kingshaven"). No verified work result, photos, tenant confirmation or landlord completion confirmation exists for Flat 20, 120 Lantern Quay. I logged the conflict (ACT-1), chased the contractor for the address and result (ACT-2), asked the tenant whether the window now opens (ACT-3), raised an office task (ACT-4), and escalate for a human to decide whether to reopen and re-dispatch and to check the invoice. I did not re-dispatch (no priced landlord approval: event-006 names no amount — APR-SPEND-OVER-CAP / RTE-LANDLORD) and did not tell any party the job was or was not done at their address.

Safety actions taken first:
- Safety keyword pass: no gas, electrical, damp/mould, detector or vulnerability content in the artefacts; a stuck bathroom window matches no emergency definition. No hazard reported or observed — nothing to make safe.

Actions deliberately withheld:
- Did not re-dispatch a contractor: no priced landlord approval on file (event-006 names no amount) and no standing cap — APR-SPEND-OVER-CAP / RTE-LANDLORD.
- Did not tell the tenant or landlord that the repair was or was not completed: the only evidence names another property.
- Did not reopen or re-close the request, and did not forward or validate any invoice (PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: ESC-CONFLICT, RTE-STAFF, RTE-CONTRACTOR, RTE-LANDLORD, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Amelia Ingram reported on 05/12/2024 that the bathroom window at Flat 20, 120 Lantern Quay, Northbridge, ZZ8 2ZZ is stuck and will not open. [index, event-001; high]
- F2: The landlord ('Felix') approved getting the fault fixed in their own message on 06/12/2024, without naming an amount. [event-006; high]
- F3: Riverside Solutions was assigned and briefed on 06/12/2024; the tenant was told they would attend. [event-009, event-010, event-011; high]
- F4: A visit slot of 12/12/2024 15:57 was recorded on 13/12 and confirmed to contractor and tenant. [event-018, event-019, event-020; high]
- F5: The only completion reports on this ticket name a different property, 'Flat 7, 177 Beacon Close, Kingshaven, ZZ7 3ZZ', with handle, gearbox and hinges replaced. [event-016, event-017; high]
- F6: A quote document was added but its contents are unavailable; approval of the quote appears only as a system status line, not a landlord message. [event-024, event-026; high]
- F7: Documents were skipped, landlord confirmation was still needed, the keys update failed validation, and the request was then closed. [event-032, event-033, event-035, event-036; high]
- F8: No message from the tenant confirms the window was repaired; the agency itself noted on 15/12 that there were no work results. [event-021, search_history; high]

Conflicts between sources:
- The agency record places this job at Flat 20, 120 Lantern Quay; the contractor's two completion reports place the completed window repair at Flat 7, 177 Beacon Close, Kingshaven. The difference decides whether the tenant's window was ever repaired. → Contractor asked which address was attended and the result (ACT-2); tenant asked whether the window now opens (ACT-3); office task raised (ACT-4). Unresolved pending replies. (asked)
- Closure (event-036) and the skip reason 'all works completed' (event-032) assert a finished job, while event-021 ('No work results') and the mismatched completion reports show no verified result at this property. → Referred to the property manager (ACT-4). (unresolved)

Red flags:
- [data_quality] Two contractor completion emails on this ticket name a property that is not the ticket's property; the ticket was then closed, documents skipped and landlord confirmation bypassed. Risk of an unrepaired window and an invoice booked to the wrong property. → Conflict logged (ACT-1), contractor and tenant asked for the missing facts (ACT-2, ACT-3), office task raised (ACT-4), escalated.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "048", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [{"event": "event-006", "timestamp": "2024-12-06 02:54:06 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2024-12-06 02:54:… | allow |
| 4 | search_history | completed | from_party=Contractor | [{"event": "event-016", "timestamp": "2024-12-13 08:43:08 UTC", "channel": "Email", "from": "Contractor", "to": "Northbridge Lettings", "excerpt": "[2024-12-13… | allow |
| 5 | search_history | completed | query=Beacon Close | [{"event": "event-016", "timestamp": "2024-12-13 08:43:08 UTC", "channel": "Email", "from": "Contractor", "to": "Northbridge Lettings", "excerpt": "[2024-12-13… | allow |
| 6 | add_note | completed | note=Conflict on closure evidence. Agency record: job is the bat… | {"id": "ACT-1"} | CAP-LOG |
| 7 | notify_contractor | completed | message=Dear Riverside Solutions, re: Window Repair Request at Flat… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | notify_tenant | completed | message=Dear Amelia Ingram, re: your report of the bathroom window… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | create_human_task | completed | queue=property_manager, title=Case 048 closed on completion reports naming a different pr…, summary=Ticket for the stuck bathroom window at Flat 20, 120 Lanter… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 10 | definition_of_done | failed | facts=[{"id": "F1", "statement": "Tenant Amelia Ingram reported o…, conflicts=[{"description": "The agency record places this job at Flat…, red_flags=[{"kind": "data_quality", "description": "Two contractor co…, authority_citations=["ESC-CONFLICT", "RTE-STAFF", "RTE-CONTRACTOR", "RTE-LANDLO…, assumptions=["Assumption: no management key was issued for this visit,… | unknown tool | - |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Case 048 was closed on a completion report for a different address — reopen and re-dispatch the Flat 20 bathroom window repair, or accept the closure?
**Facts (≤5):**
- Tenant Amelia Ingram reported the bathroom window at Flat 20, 120 Lantern Quay stuck on 05/12/2024 (event-001; index).
- Riverside Solutions instructed 06/12 (event-011); slot recorded 12/12/2024 15:57 and confirmed to both sides 13/12 (event-018, event-019, event-020).
- The only completion reports (event-016, event-017, untrusted) state the repair was completed at 'Flat 7, 177 Beacon Close, Kingshaven, ZZ7 3ZZ' — not this property.
- Documents skipped 'all works completed' (event-032), landlord confirmation flagged outstanding (event-033), keys line failed validation (event-035), request closed (event-036).
- Quote contents unavailable (event-024); 'Quote was approved by landlord' is a system line (event-026) — the only landlord message is event-006 with no amount.
**Gap:** Whether any engineer attended Flat 20, 120 Lantern Quay; what the approved quote amount was and against which property it was raised.
**Options:**
- Reopen and re-dispatch to Flat 20 once the contractor/tenant replies — tenant gets the repair; cost needs a priced landlord approval (RTE-LANDLORD).
- Hold the closure pending the contractor's reply (due 2 working days) and act on what they say — no duplicate work order, but CLK-S11 keeps running.
- Accept the closure as it stands — risk: an unrepaired window and an invoice booked to the wrong property/landlord.
**Recommended:** Hold the closure pending the contractor's reply, then reopen and re-dispatch if Flat 20 was never attended; check the quote/invoice against the correct property either way.
**Default if no answer:** If the contractor does not reply within 2 working days, treat Flat 20 as unattended, reopen and seek a priced landlord approval before re-instructing.
**Deadline:** Contractor reply 2 working days from ACT-2; CLK-S11 running from 05/12/2024.
**Undo:** No irreversible action by me: one note, two information requests (contractor, tenant) and this office task. Nothing dispatched, no spend committed, no closure altered.
**Context:** event-001, event-006, event-011, event-016, event-017, event-018, event-024, event-026, event-032, event-033, event-035, event-036, ACT-1, ACT-2, ACT-3, ACT-4

Promises made or recorded:
- agency → tenant: Come back to the tenant once the provider replies about whether the repair was carried out at Flat 20 by within 2 working days of ACT-2 [open]
- agency → contractor: Asked for written confirmation of the address attended, date and result; no further work or invoicing until instructions are confirmed by 2 working days from ACT-2 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
