# ANSWER — Case 032 — Case 032: Toilet flush mechanism repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Toilet flush repair reported complete at £172.51 + VAT, but invoice unreadable and the visit record names another address — verification requested, request held open.
**Stage:** on_hold · **Hold:** Waiting for Provider — Riverside Maintenance to give attendance date/address, works done, photos and a legible invoice by 2 working days (ACT-4, ACT-6); tenants' confirmation also outstanding (ACT-2).
**Last update:** 2026-11-01 07:01:16 UTC (event-036) · **Decided:** 2026-10-10 13:29 UTC
**Next step:** Riverside Maintenance to confirm the attendance date and address and re-send a legible invoice for Flat 10, 130 Lantern Quay (requested ACT-4, due within 2 working days); tenants to confirm the flush works (ACT-2).

Definition of done (4/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/index: flusher fault categorised as routine plumbing; no hazard keywords in the file.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 landlord 'Yes please mend it'.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-009, event-010, event-011: Riverside Maintenance assigned; tenant and provider briefed.
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-013/event-014 slot 11/10/2026 16:15 predates the instruction; the later booking on file names a different address (event-032/event-033). Attendance details requested from the provider (ACT-4).
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-018/event-021 quote £172.51 + VAT; landlord '👍' event-024; instruction event-025.
- [ ] work_result: Work result recorded from the provider — event-034 provider claims completion but no verifiable detail; tenant confirmation requested (ACT-2).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-035 invoice added but attachment unavailable; no photos; legible invoice and photos requested (ACT-4).
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — ACT-3: landlord told the invoice is being verified first; not forwarded.
- [ ] landlord_confirmation: Landlord confirmed completion — ACT-3 — awaiting verified invoice.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued on the record; access was arranged direct with the tenant (event-011, event-015).
- [ ] closed: Request closed with a resolution that names who paid — Not closed; ACT-6 hold pending provider and tenant verification, ACT-5 office task.

## 1. Decision

Did not close the request despite the provider's completion report and the supervisor's "completed" flag: the work result is unverifiable (invoice attachment unavailable; the only visit-booking evidence names a different property). Kept the routine, reversible steps going — asked the tenants to confirm attendance and that the flush works, asked the provider for attendance details, photos and a legible invoice within 2 working days, told the landlord the invoice is being verified before it reaches them, logged the discrepancy and raised an office task to verify before any payment. No new work order, no duplicate instruction, no liability or payment decision.

Actions deliberately withheld:
- close_request — work result, documents, invoice to landlord and landlord confirmation are all unverified.
- No new work order or re-instruction to the provider (the 19/10 instruction stands; avoiding a duplicate).
- No statement to any party about who pays or about the other property's tenancy.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, CAP-CLOSE, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported a fault with the toilet flusher in the second bedroom at Flat 10, 130 Lantern Quay, Willowbank, ZZ5 1ZZ on 2026-10-11. [index, event-001; high]
- F2: Landlord replied 'Yes please mend it' on 2026-10-12, authorising the agency to instruct a contractor. [event-006; high]
- F3: Riverside Maintenance was assigned as the plumbing provider and both tenant and provider were briefed on 2026-10-12. [event-009, event-010, event-011; high]
- F4: Provider quoted £172.51 + VAT for a new toilet flusher. [event-012, event-018; high]
- F5: Landlord replied '👍' on 2026-10-18 to the agency's chase of the £172.51 + VAT quote; the agency instructed the provider to proceed on 2026-10-19. [event-021, event-024, event-025; high]
- F6: Provider emailed on 2026-11-01 that the job is complete and an invoice uploaded; the uploaded invoice attachment is unavailable and no photos are on file. [event-034, event-035, get_attachment; high]
- F7: The only appointment-booking evidence for the attended visit is a contractor/tenant call naming Flat 29, 129 Lantern Quay, Northbridge, ZZ7 0ZZ, 'May 1st' 8am-12pm; the agency logged it on this ticket as 'visit schedule may 1st'. [event-032, event-033; medium]
- F8: The slot recorded as confirmed to tenant and provider, 11/10/2026 16:15, predates the quote and the instruction to proceed. [event-013, event-014, event-015, event-025; high]
- F9: A returned call on 2026-10-21 names the caller as Theo Quinn at Flat 10, 130 Lantern Quay; the tenants of record on this ticket are Grace Bennett & Maya Jenkins. [event-030, event-010; medium]
- F10: A supervisor marked the task completed on 2026-11-01 while the invoice remained unavailable and no tenant confirmation was on file. [event-036; high]
- F11: No landlord standing spend cap is on file in this case record; the authority relied on is the landlord's own approval in the history. [get_case_details, event-006, event-024; medium]

Conflicts between sources:
- The job is recorded against Flat 10, 130 Lantern Quay, Willowbank, ZZ5 1ZZ, but the visit booked and logged for it was arranged for Flat 29, 129 Lantern Quay, Northbridge, ZZ7 0ZZ. → Not resolved in a message to any party. Provider asked for the attendance date and address, tenants asked whether the visit happened; office task raised to verify before the invoice is paid or the request closed (ACT-4, ACT-2, ACT-5). (asked)
- Caller named Theo Quinn on the tenant line versus tenants of record Grace Bennett & Maya Jenkins. → Flagged to the office; not put to any party as an accusation. (unresolved)

Red flags:
- [data_quality] Completion and invoice cannot be verified: invoice attachment unavailable (event-035) and the booking logged for this job names a different property (event-032/event-033); the ticket was nonetheless flagged completed (event-036). → Request kept open, invoice not forwarded for payment, provider and tenants asked to verify, office task raised (ACT-1, ACT-2, ACT-4, ACT-5, ACT-6).
- [other] Identity mismatch on the tenant line: caller named Theo Quinn (event-030) against tenants of record Grace Bennett & Maya Jenkins (event-010). → Recorded and referred to the office; no party told it is a different property or person.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "032", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=Flat 29 129 Lantern Quay Northbridge | [] | allow |
| 4 | search_history | completed | from_party=Contractor | [{"event": "event-012", "timestamp": "2026-10-12 09:05:44 UTC", "channel": "Email", "from": "Contractor", "to": "Agency / system", "excerpt": "[2026-10-12 09:0… | allow |
| 5 | get_attachment | completed | name=invoice | {"error": "no attachment named invoice"} | allow |
| 6 | add_note | completed | note=Final checks before closure. Provider reported job complete… | {"id": "ACT-1"} | CAP-LOG |
| 7 | notify_tenant | completed | message=Dear Grace Bennett & Maya Jenkins,  Riverside Maintenance h… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | notify_landlord | completed | message=Address: Flat 10, 130 Lantern Quay, Willowbank, ZZ5 1ZZ  De… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | notify_contractor | completed | message=Address: Flat 10, 130 Lantern Quay, Willowbank, ZZ5 1ZZ — P… | {"id": "ACT-4"} | CAP-NOTIFY |
| 10 | create_human_task | completed | queue=property_management, title=Verify completion/invoice before payment — Flat 10, 130 Lan…, summary=Riverside Maintenance report the toilet flush job complete… | {"id": "ACT-5"} | CAP-HUMAN-TASK |
| 11 | put_on_hold | completed | reason=Waiting for Provider — attendance date/address, works done,…, until=2026-11-05 | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: For the toilet flush job at Flat 10, 130 Lantern Quay, Willowbank, ZZ5 1ZZ: on what date and time did your engineer attend, at which address, what work was carried out, and please re-send a legible invoice (photos if available). (blocking; Completion report (event-034) cannot be verified: invoice attachment unavailable (event-035) and the only booking record names Flat 29, 129 Lantern Quay, Northbridge (event-032).)
- Ask **tenant**: Did the plumber attend your flat, on what date, and is the second bedroom WC flush mechanism now working? (blocking; Tenant-owned fact that settles whether the work was done at this property before closure.)
- Ask **landlord**: Please confirm completion once we send the verified invoice for £172.51 + VAT. (non-blocking; DoD landlord_confirmation; held until the invoice is verified (ACT-3).)

Promises made or recorded:
- agency → landlord: Send the verified invoice for confirmation once provider and tenant verification are in; no charge passed on before then. [open]
- agency → tenant: Arrange a return visit with the provider if the visit did not happen or the flush is still faulty. [open]
- contractor → agency: Attendance date/address, works done, photos and a legible invoice within 2 working days. by 2026-11-05 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
