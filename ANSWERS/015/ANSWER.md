# ANSWER — Case 015 — Case 015: Front Door Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Door-sticking repair at Flat 16 was flagged complete, but records conflict on provider and property; kept open, chased provider, asked tenant, raised office task.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation whether anyone attended Flat 16 and whether the door still sticks/locks (2 working days); Waiting for Provider in parallel on attendance and the invoice; office task open on the records conflict.
**Last update:** 2025-01-12 09:37:48 UTC (event-019) · **Decided:** 2026-10-10 14:03 UTC
**Next step:** Tenant (Freya Bennett) to confirm whether a contractor attended and whether the front door still sticks or fails to lock (asked ACT-4, 2 working days); in parallel the provider to confirm attendance/booking (ACT-3) and the office to resolve the provider/property conflict and the £68.97 invoice (ACT-2).

Definition of done (2/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (report), event-004 (acknowledged to tenant with escalate-if-worse advice); urgency set routine via use_playbook
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 — landlord's own email approving instruction of a contractor (no amount named)
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Provider assigned and tenant briefed (event-008, event-009, event-010), but provider identity is contradicted by event-014 and event-015; conflict raised at ACT-2
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No confirmed slot anywhere in the history; provider chased at ACT-3, tenant asked at ACT-4
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was put to the landlord; the £68.97 invoice (event-015) was never approved and no standing cap is on file (RTE-LANDLORD, APR-SPEND-OVER-CAP)
- [ ] work_result: Work result recorded from the provider — No work result for this property; the only completion statement names a different address (event-016)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — attachment-60-document recorded twice (event-017, event-019) but contents unavailable and not retrievable via get_attachment; no photos
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No record of the £68.97 invoice being forwarded to the landlord; held pending the office decision at ACT-2
- [ ] landlord_confirmation: Landlord confirmed completion — event-016 was sent to the landlord about a different address; no landlord confirmation for Flat 16
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued; access was to be arranged direct with the tenant (event-010)
- [ ] closed: Request closed with a resolution that names who paid — Closure withheld despite event-018; ticket placed on hold at ACT-5

## 1. Decision

Did not close the ticket despite the "completed by supervisor" flag (event-018): no work result exists for this property, the completion email to the landlord names a different address (event-016), four different provider names appear for one job (event-007, event-010, event-014, event-015), and a £68.97 invoice sits unapproved and not forwarded. Logged the conflict (ACT-1), raised an office task for the property/provider conflict and the invoice (ACT-2), chased the provider on the agency's own record for attendance/booking (ACT-3), updated the tenant and asked for the current state of the door including security (ACT-4), and placed the ticket on hold (ACT-5). Withheld any message telling a party which record is correct, any closure, and any step towards paying or approving the invoice.

Safety actions taken first:
- Checked the report against the emergency definitions: a door sticking at the base with no lock or security failure reported is not an insecure property (event-001); urgency set routine.
- Asked the tenant to confirm the door still closes and locks and to report any security concern immediately, which would raise urgency (ACT-4, consistent with event-004).
- Safety-pass keywords screened: no gas, electrical, damp/mould, detector, injury or occupant-vulnerability content appears in this case's artefacts; no hazard observed or reported, so no safety red flag raised.

Actions deliberately withheld:
- Did not close the request despite event-018 — definition of done unmet (CAP-CLOSE).
- Did not forward, approve or action the £68.97 invoice (PRO-PAYMENTS, RTE-LANDLORD).
- Did not tell the landlord or tenant which of the conflicting records is correct, or correct event-016 to the landlord — office decision (ESC-CONFLICT, rule 2).
- Did not raise a quote for the recommended door replacement mentioned in event-016, as it is not established that it refers to this property.
- Did not dispatch a second contractor, which would duplicate the existing work order.

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-HUMAN-TASK, RTE-TENANT, RTE-CONTRACTOR, RTE-LANDLORD, ESC-CONFLICT, APR-SPEND-OVER-CAP, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 03/01/2025 that the front door of Flat 16, 76 Alder Lane, Kingshaven ZZ8 8ZZ sticks at the base and is difficult to open and close, with no obstruction found. [index, event-001, get_case_details; high]
- F2: No loss of security, no hazard and no vulnerability is reported anywhere in the history; the agency told the tenant to report any security concern immediately (event-004). [event-001, event-004; high]
- F3: The agency asked the landlord on 05/01/2025 whether to instruct a contractor; the landlord replied the same day "get Imogen to have a look at it" — approval to instruct, with no amount named. [event-003, event-007; high]
- F4: The agency assigned maintenance provider Alder Homes on 06/01/2025 and briefed both tenant and provider; a later agency email to the contractor says "Job for Noah please". [event-008, event-009, event-010, event-014; high]
- F5: On 08/01/2025 a contractor email reports an invoice from Keystone Homes for £68.97 due 06/02/2025; the PDF contents are unavailable and no attachment named attachment-60-document can be retrieved. [event-015, event-017, get_attachment; high]
- F6: The 12/01/2025 completion email to the landlord is headed Flat 16, 76 Alder Lane but states the door "got sorted" for Flat 10, 110 Meadow Row, Cedarford ZZ3 6ZZ, and relays that the door is rotting/swelling with a replacement recommended. [event-016; high]
- F7: The ticket was marked "Task has been completed by supervisor" on 12/01/2025 with no work result, no tenant confirmation, no landlord approval of the £68.97 and no invoice forwarded to the landlord. [event-018, event-019; high]
- F8: No landlord standing spend cap is on file for this landlord; the mandate default is £0, so the £68.97 is not covered by the event-007 approval, which named no amount. [get_action_ledger, event-007; medium]
- F9: One contractor reply (06/01/2025) has no retrievable text — the expected content could not be extracted. [event-011; high]

Conflicts between sources:
- Four provider identities for one job: landlord named "Imogen" (event-007), agency assigned Alder Homes (event-010), agency asked for "Noah" (event-014), invoice from Keystone Homes (event-015). → Not decided by me. Office task raised (ACT-2); provider on the agency's own record (Alder Homes) chased for attendance (ACT-3). No party told which name is correct. (asked)
- Property mismatch: the completion email headed Flat 16, 76 Alder Lane reports the door sorted at Flat 10, 110 Meadow Row, Cedarford ZZ3 6ZZ. It is not established that work was done at Flat 16. → Office task raised (ACT-2); tenant asked whether anyone attended her flat (ACT-4). Ticket kept open. (asked)
- Ticket flagged complete by supervisor while the definition of done is unmet (no work result, no landlord confirmation, invoice unapproved and not forwarded). → Closure withheld; case placed on hold pending tenant and provider replies and the office decision. (asked)

Red flags:
- [data_quality] The 05/01/2025 landlord email opens "I hope you had a great Valentines weekend" — the date/context of the correspondence is unreliable and may be a template or mis-dated record. → Recorded in the case note (ACT-1); not relied on for any date.
- [data_quality] Invoice evidence is second-hand: the PDF contents are unavailable and attachment-60-document cannot be retrieved, yet the amount £68.97 and trading name Keystone Homes were recorded against the job. → No payment, approval or forwarding of the invoice; provider asked to confirm whether it relates to this job (ACT-3); office task raised (ACT-2).
- [data_quality] A contractor reply of 06/01/2025 has no extractable text, so the provider's own position on scope/attendance is unknown. → Provider asked directly to confirm attendance and booking (ACT-3).
- [other] Landlord email signed "Harper" but sent from "Meadow Homes" and addressed to "Mercer", while the misdirected completion email concerns a property on Meadow Row — names in message bodies are inconsistent across this case. → Addressed parties only by the names on the case record; no body-text names copied into other parties' letters. Flagged to the office (ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "015", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-60-document | {"error": "no attachment named attachment-60-document"} | allow |
| 4 | search_history | completed | query=Imogen | [{"event": "event-007", "timestamp": "2025-01-05 12:22:12 UTC", "channel": "Email", "from": "Landlord", "to": "Northbridge Lettings", "excerpt": "[2025-01-05 1… | allow |
| 5 | search_history | completed | from_party=Contractor | [{"event": "event-011", "timestamp": "2025-01-06 08:20:11 UTC", "channel": "Email", "from": "Contractor", "to": "Agency / system", "excerpt": "[2025-01-06 08:2… | allow |
| 6 | add_note | completed | note=Conflicts on this ticket (Flat 16, 76 Alder Lane, Kingshave… | {"id": "ACT-1"} | CAP-LOG |
| 7 | create_human_task | completed | queue=property_manager, title=Case 015 Flat 16, 76 Alder Lane — provider/property records…, summary=Tenant reported the front door sticking at the base on 03/0… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 8 | notify_contractor | completed | message=Re: Door Repair Request — Flat 16, 76 Alder Lane, Kingshave… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | notify_tenant | completed | message=Dear Freya,  Re: front door sticking — Flat 16, 76 Alder La… | {"id": "ACT-4"} | CAP-NOTIFY |
| 10 | put_on_hold | completed | reason=Waiting for Tenant — confirmation whether a contractor atte…, until=2 working days from 2025-01-12 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Has anyone attended Flat 16, 76 Alder Lane about the front door, and on roughly what date? Is the door still sticking at the base, and does it close and lock properly? (blocking; No work result exists for this property; the only completion message names a different address (event-016). Whether the repair is done, and whether the door is secure (which would raise urgency), is a tenant-owned fact (RTE-TENANT).)
- Ask **contractor**: Confirm whether an operative attended Flat 16, 76 Alder Lane, Kingshaven ZZ8 8ZZ, on what date and what was done; if not attended, confirm an access window with the tenant. Also confirm whether the £68.97 invoice from Keystone Homes relates to this job at this address. (blocking; Attendance, scope and invoice scope are contractor-owned (RTE-CONTRACTOR); four provider names appear for one job (event-010, event-014, event-015).)
- Ask **property_manager**: Which provider holds this job, was event-016 sent to the landlord in error about a different property, and should the £68.97 go to the landlord for approval? (non-blocking; Agency records disagree in a way that changes the action (ESC-CONFLICT); the invoice has no spend authority behind it (APR-SPEND-OVER-CAP, PRO-PAYMENTS). Task raised at ACT-2.)

Promises made or recorded:
- agency → tenant: Update as soon as the provider responds; provider asked to reply within 2 working days; job confirmed still open by 2 working days from the chase (ACT-3/ACT-4) [open]
- agency → contractor: No further work to be carried out without written agency approval [open]
- agency → tenant: Earlier agency promise to update the tenant once next steps were confirmed (event-004) — not kept before now; renewed at ACT-4 [broken]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
