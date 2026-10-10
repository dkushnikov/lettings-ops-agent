# ANSWER — Case 015 — Case 015: Front Door Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Front door sticking at Flat 16, 76 Alder Lane; records conflict on property and provider, so I chased the provider, updated the tenant and escalated instead of closing.
**Stage:** on_hold · **Hold:** Waiting for Provider — Alder Homes to confirm attendance at Flat 16 or offer a slot, and to say whether the £68.97 invoice belongs to this job; property_manager to resolve the address/provider conflict (ACT-2, ACT-4).
**Last update:** 2025-01-12 09:37:48 UTC (event-019) · **Decided:** 2026-10-10 13:24 UTC
**Next step:** Property manager to confirm whether the completed job and the £68.97 invoice relate to Flat 16, 76 Alder Lane or to Flat 10, 110 Meadow Row (event-016), and whether Alder Homes or the landlord's named contractor "Imogen" holds the job; provider reply chased with a 2-working-day clock.

Definition of done (3/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 issue logged and categorised as a door repair; event-004 agency gave the tenant escalation advice on security concerns; ACT-3 repeated damage-limiting advice and set urgency routine.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 — landlord's own reply instructs the agency to have the door looked at (names 'Imogen'); landlord-owned decision under RTE-LANDLORD.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008/event-010 Alder Homes instructed and briefed; event-009 tenant told who is attending. Note: provider named by the landlord (event-007) differs — conflict raised.
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot confirmed with the tenant anywhere in the history; event-013 'awaiting completion' only. Chased at ACT-2.
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was put to the landlord; the only figure is £68.97 described in event-015 as an invoice already raised, which the brief in event-010 ('only proceed after receiving our approval') did not aut…
- [ ] work_result: Work result recorded from the provider — The only completion statement (event-016) names a different property, Flat 10, 110 Meadow Row; no result recorded for Flat 16.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — attachment-60-document added (event-017, event-019) but contents unavailable and not retrievable via get_attachment; no photos.
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice forwarded to the landlord for this property; event-016 reported completion at a different address.
- [ ] landlord_confirmation: Landlord confirmed completion — No landlord reply after event-016.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; the contractor was asked to contact the tenant direct (event-010).
- [ ] closed: Request closed with a resolution that names who paid — Supervisor flag at event-018 is not evidence the work was done at this address; closure withheld pending the conflict resolution.

## 1. Decision

Did not close the ticket despite the supervisor completion flag (event-018). The agency's own records conflict on which property was repaired and which provider holds the job, and that difference changes the action, so the case goes to the property_manager under ESC-CONFLICT / RTE-STAFF. Meanwhile I kept the reversible steps running: chased Alder Homes (the provider on the agency's own record, event-010) for attendance/slot and for clarification of the £68.97 invoice, asked the tenant for the current door status with damage-limiting/escalation advice, and placed the ticket on hold (ACT-1 to ACT-4). No spend instructed, no landlord correction sent, nothing closed.

Safety actions taken first:
- Reminded the tenant to report immediately if the door fails to latch or the property cannot be secured, and that this would be handled as an emergency (ACT-3).

Actions deliberately withheld:
- Did not close the request despite event-018, because work result, documents, invoice routing and landlord confirmation are unverified for this property (CAP-CLOSE).
- Did not forward or approve the £68.97 invoice or state who pays (PRO-PAYMENTS, PRO-TENANT-LIABILITY, RTE-LANDLORD).
- Did not tell the landlord that event-016 named the wrong property — that is picking a side in a records conflict before the office resolves it.
- Did not instruct a new contractor or re-dispatch under event-007, to avoid duplicating a possibly completed work order.

## 2. Authority and evidence

Authority cited: ESC-CONFLICT, RTE-STAFF, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-CONTRACTOR, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CAP-CLOSE, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Case property is Flat 16, 76 Alder Lane, Kingshaven, ZZ8 8ZZ; tenant Freya Bennett reported on 03/01/2025 that the front door sticks at the base and is hard to open/close, with no obstruction. [index, event-001, get_case_details; high]
- F2: The agency asked the landlord on 05/01/2025 whether to instruct a contractor and told the tenant it was awaiting instructions. [event-003, event-004; high]
- F3: The landlord replied on 05/01/2025: 'Please get Imogen to have a look at it' — approval to instruct, naming a contractor. [event-007; high]
- F4: The system assigned provider 'Alder Homes' and briefed them and the tenant on 06/01/2025; the brief said to quote first and only proceed after agency approval. [event-008, event-009, event-010; high]
- F5: A contractor email on 08/01/2025 describes an invoice from 'Keystone Homes' for £68.97 due 06/02/2025; no agency approval of any amount appears in the history. [event-015; medium]
- F6: The completion email to the landlord on 12/01/2025 states the door was sorted at Flat 10, 110 Meadow Row, Cedarford ZZ3 6ZZ — not the case property — and reports the door is rotting/swelling with a replacement recommended. [event-016; high]
- F7: The ticket was marked 'completed by supervisor' on 12/01/2025 with attachment-60-document added; the PDF contents are unavailable and the attachment cannot be retrieved. [event-017, event-018, event-019, get_attachment; high]
- F8: No access window was ever offered to or confirmed with the tenant on this ticket. [event-001, event-019; high]
- F9: No landlord spend cap or standing instruction record is available in this environment, so no standing authority to spend exists beyond the landlord's own approval at event-007. [get_case_details; medium]

Conflicts between sources:
- Which property the completed repair and invoice relate to: the ticket and all tenant/contractor correspondence say Flat 16, 76 Alder Lane, but the completion email to the landlord says Flat 10, 110 Meadow Row, Cedarford. → Not decided by me; referred to property_manager. Ticket kept open and provider chased for attendance at Flat 16 (ACT-2). (unresolved)
- Who holds the job: the landlord named 'Imogen' (event-007), the system assigned 'Alder Homes' (event-008/010), a later agency email asked for 'Noah' (event-014) and the invoice is from 'Keystone Homes' (event-015). → Chased the provider on the agency's own record (Alder Homes) for attendance and invoice ownership; naming question left to the office. (unresolved)
- Two tenant contact numbers on file for the same tenant: 07700 900170 and 07700 900452. → Flagged as data quality; no number quoted to any third party by me. (unresolved)

Red flags:
- [data_quality] Completion reported to the landlord against a different property (Flat 10, 110 Meadow Row) while this ticket for Flat 16 was closed by a supervisor; invoice of £68.97 from a company name that matches neither the assigned provider nor the landlord's named contractor; attachment contents unavailable; duplicate document-added notes; two tenant phone numbers; an email dated 05/01/2025 referring to a 'Valentines weekend'. → Recorded in the case note (ACT-1), ticket not closed, conflict escalated to property_manager.
- [other] An invoice appears (event-015) although the provider brief required a quote and agency approval before proceeding (event-010); no approval of any amount is in the history. → Provider asked to confirm which job the £68.97 relates to and to do no further chargeable work without written instruction (ACT-2); payment question left to the property_manager and landlord. No money moved (PRO-PAYMENTS).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "015", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-60-document | {"error": "no attachment named attachment-60-document"} | allow |
| 4 | add_note | completed | note=Conflict in agency records — door repair, Flat 16, 76 Alder… | {"id": "ACT-1"} | CAP-LOG |
| 5 | notify_contractor | completed | message=Northbridge Lettings — Door Repair Request, Flat 16, 76 Ald… | {"id": "ACT-2"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Dear Ms Bennett,  Regarding the front door sticking at Flat… | {"id": "ACT-3"} | CAP-NOTIFY |
| 7 | put_on_hold | completed | reason=Waiting for Provider — Alder Homes to confirm whether Flat…, until=2 working days from 2025-01-12 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Does the completed door repair and the £68.97 invoice belong to Flat 16, 76 Alder Lane (this ticket) or to Flat 10, 110 Meadow Row — and may this ticket be closed, or must a visit still be booked?
**Facts (≤5):**
- Tenant reported the front door sticking at the base at Flat 16, 76 Alder Lane on 03/01/2025 (event-001); case property confirmed by the case record (get_case_details).
- Landlord's own reply approved instruction and named 'Imogen' (event-007); the system instead assigned 'Alder Homes' (event-008, event-010), a later agency email asked for 'Job for Noah' (event-014), and the invoice email names 'Keystone Homes' £68.97 due 06/02/2025 (event-015).
- The completion email to the landlord says the door 'got sorted' at Flat 10, 110 Meadow Row, Cedarford — a different property (event-016) — yet this ticket was marked 'completed by supervisor' (event-018).
- No visit slot was ever confirmed with the tenant on this ticket, and no work result for Flat 16 is recorded; attachment-60-document is not retrievable (event-017, event-019, get_attachment error).
- Two different tenant phone numbers are on file: 07700 900170 (event-010) and 07700 900452 (event-014).
**Gap:** Whether any operative actually attended Flat 16, whether the £68.97 invoice is for this address, and whether the landlord has been told about the wrong property in event-016.
**Options:**
- Confirm the work was done at Flat 16: verify with Alder Homes/the invoice, forward the invoice to the landlord, obtain landlord confirmation, then close naming who paid.
- Confirm the work belongs to Flat 10, 110 Meadow Row: reassign the invoice to that ticket, correct the landlord update (event-016), and book a fresh visit for Flat 16 under the landlord's existing approval (event-007).
- Re-instruct the landlord's named contractor ('Imogen') for Flat 16 and withhold payment of the £68.97 until the address is matched.
**Recommended:** Option 2 pathway first: treat Flat 16 as unrepaired until the provider confirms attendance at that address, and correct the landlord update; close only on evidence.
**Default if no answer:** If Alder Homes does not reply within 2 working days of ACT-2, the ticket stays on hold as Waiting for Provider and a second chase plus re-instruction decision is needed; it must not be auto-closed.
**Deadline:** 2 working days from 12/01/2025 for the provider reply; CLK-S11 reasonable-time clock runs from 03/01/2025.
**Undo:** Nothing irreversible done by me: no contractor instructed, no spend committed, no closure. ACT-2/ACT-3 are informational messages; the hold (ACT-4) can be lifted.
**Context:** event-001, event-007, event-010, event-014, event-015, event-016, event-018, ACT-1, ACT-2, ACT-3, ACT-4

Promises made or recorded:
- agency → tenant: Confirm an appointment time once the contractor replies; treat any loss of security as an emergency if reported [open]
- agency → contractor: Reply requested within 2 working days on attendance, slot and invoice ownership by 2 working days from 2025-01-12 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
