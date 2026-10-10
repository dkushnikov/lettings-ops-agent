# ANSWER — Case 013 — Kitchen glazing maintenance request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Misted kitchen glazing: invoice arrived with no amount and no evidence of fitting, so I chased the contractor and tenant for proof of attendance and held the case.
**Stage:** on_hold · **Hold:** Waiting for Provider — Clearfirth Glazing to confirm whether the glazing was fitted and when, offer a slot if not, and reissue invoice NBL-013-INV-09 with the amount; reply due within 2 working days, then to the property manager (ACT-5).
**Last update:** 2025-09-10 10:10:00 UTC (event-024) · **Decided:** 2026-10-10 15:39 UTC
**Next step:** Clearfirth Glazing (Sella Vane) to confirm attendance date or offer a fitting slot and reissue the invoice showing the amount, within 2 working days (ACT-2).

Definition of done (4/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Categorised as routine glazing repair and acknowledged same working day (event-002); moisture-limiting steps and a mould-reporting instruction given to the tenant (ACT-3). Site assessment of the damp…
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-010 — landlord's own message approving the contractor at £180 total, matching the £150 + VAT quoted (event-009, event-011).
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Clearfirth Glazing instructed and briefed (event-006, event-015, event-017); tenant told who is attending and what happens next (event-013, event-019, ACT-3).
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Tenant offered 24/25/26 Aug (event-014); contractor never selected a slot and none was agreed (event-015, event-017, event-021). Chased at ACT-2; no schedule_access booked because no provider-confirm…
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-010 (landlord approval of £180 total) against the quote at event-009/event-011; VAT stated.
- [ ] work_result: Work result recorded from the provider — No visit report or provider confirmation of completion anywhere in the record (event-022); glass undelivered as at 02/09 (event-021). Requested at ACT-2 and cross-checked with the tenant at ACT-3.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Only document is invoice NBL-013-INV-09 with no amount (event-023, glazing-invoice); no photos. Reissue requested at ACT-2.
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Deliberately withheld — an invoice with no amount cannot be checked against the approved £180; landlord told it is on hold (ACT-4).
- [ ] landlord_confirmation: Landlord confirmed completion — Cannot be sought until the work result and priced invoice exist (ACT-4).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; the tenant asked to be present for access (event-014).
- [ ] closed: Request closed with a resolution that names who paid — Case placed on hold pending the contractor (ACT-5); closure would be unsupported while work_result, visit_confirmed, documents and invoice_to_landlord are open.

## 1. Decision

Did not close the request. Despite an invoice being uploaded (event-023), the record contains no confirmed appointment and no work result: the contractor never selected a slot from the tenant's offered dates (event-014, event-015, event-017) and on 02/09 reported the glass had still not arrived (event-021). The invoice copy (glazing-invoice.pdf, event-023) states no amount, so it cannot be checked against the landlord-approved £180 incl. VAT (event-010) or forwarded for payment. Landlord authority is sound and already on file, so no new approval was sought. I chased the instructed contractor with a 2-working-day reply-by for attendance confirmation, a fitting slot and a priced invoice; asked the tenant to confirm whether anyone attended, whether the unit is still misted and whether damp or mould has appeared (the damp/cold concern was never assessed on site — event-005); updated the landlord that the invoice is not being processed; and placed the case on hold. Not an escalation: the open questions are owned by the contractor and the tenant, and the routine next steps are all reversible.

Actions deliberately withheld:
- Did not close the request: work result, confirmed visit, priced invoice and landlord confirmation are all outstanding (CAP-CLOSE).
- Did not forward invoice NBL-013-INV-09 to the landlord for payment or approve any payment — no amount stated and the work is unverified (PRO-PAYMENTS).
- Did not re-dispatch or raise a second work order: Clearfirth Glazing remains instructed and has ordered the glass; duplicating the order would duplicate the cost (playbook, duplicate rule).
- Did not book an access window: no provider-confirmed date exists, and promising the tenant a date no booking backs is prohibited (CAP-NOTIFY).
- Did not state or imply who pays for anything, including the unverified invoice (PRO-TENANT-LIABILITY).
- Did not pass the tenant's pet or absence details to the contractor beyond the access need (PRO-PII).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-DISPATCH-APPROVED, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, CAP-SCHEDULE-ACCESS, CAP-CLOSE, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-PII, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported misting between the kitchen glazing panes, water gathering around the frame, a cold kitchen and concern about damp; the sash opens, closes and locks; pets at the property. [index, event-001; high]
- F2: No emergency definition is met: the window is secure and operable, no heating loss, no water near electrics, no gas or electrical fault; report made 31/07 (outside cold months). [index, event-001; high]
- F3: Quote stated to the landlord as £150 plus VAT, £180 total. [event-009, event-011; high]
- F4: Landlord Orren Vale replied in his own message that he was happy to use the contractor if £180 was the total value of the quote — approval on file for £180 incl. VAT, matching the quoted figure. [event-010; high]
- F5: Tenant offered any time on 24, 25 or 26 August and asked to be present; the contractor never selected a slot and no appointment was ever confirmed. [event-014, event-015, event-017; high]
- F6: On 24/08 the contractor said the glass had been ordered with no delivery estimate; on 02/09 she said it had still not arrived and she could not estimate delivery. [event-018, event-021; high]
- F7: On 09/09 the case was moved to 'awaiting post-visit documents' with no messages sent, no appointment confirmation and no visit report on file. [event-022; high]
- F8: An invoice dated 10/09/2025, ref NBL-013-INV-09, for 'Supply and fit 1 pane of glass to the kitchen glazing' was uploaded; the copy held states 'Amount: —', i.e. no figure. [event-023, event-024, glazing-invoice; high]
- F9: No site assessment or diagnosis of the wider damp or cold concern is recorded; the 04/08 authorisation covered obtaining a glazing price only. [event-005; high]
- F10: Tenant report acknowledged the same working day (31/07 08:30), satisfying the acknowledgement SOP. [event-002; high]

Conflicts between sources:
- The case status and the uploaded invoice assert the work was supplied and fitted, while the messaging record shows no confirmed appointment and the glass still undelivered on 02/09 — eight days before the invoice date. → Not resolved from the file. Asked the contractor for the attendance date and a priced invoice, and the tenant whether anyone attended (ACT-2, ACT-3). Invoice withheld from the landlord for payment pending the answer (ACT-4). (asked)

Red flags:
- [data_quality] Invoice NBL-013-INV-09 bills for 'supply and fit' with no amount stated, dated eight days after the contractor said the glass had not arrived, and with no confirmed attendance anywhere in the record. Recorded as unverified work and an unprocessable invoice, not as an allegation against the contractor. → Invoice not forwarded for payment; contractor asked to confirm the attendance date and reissue with the amount; tenant asked to confirm whether anyone attended; landlord informed the invoice is on hold (ACT-1, ACT-2, ACT-3, ACT-4).
- [other] Tenant's damp and cold concern, reported 31/07, has never been assessed on site; safety-pass keyword 'damp' present in the report. No damp or mould has been observed or reported as present, so this is recorded as an outstanding check rather than a hazard. → Asked the tenant whether damp, mould or staining has appeared and requested a photo; gave moisture-limiting steps; asked the contractor to note the frame condition on attendance; told the landlord a recommendation will follow if anything is reported (ACT-2, ACT-3, ACT-4).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "013", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed (ledger) | note=Case review before any closure. Established from the visibl… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_contractor | completed (ledger) | message=Re: 8 Brackenmere Walk, Vellumbrook, ZZ1 1ZZ — kitchen glaz… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_tenant | completed (ledger) | message=Dear Ms Marr,  An update on the kitchen glazing at 8 Bracke… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_landlord | completed (ledger) | message=Dear Mr Vale,  Kitchen glazing, 8 Brackenmere Walk — status… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | put_on_hold | completed (ledger) | reason=Waiting for Provider — Clearfirth Glazing to confirm whethe…, until=2 working days from today, then to the property manager | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Has the kitchen pane at 8 Brackenmere Walk been fitted? If so, on what date and time did you attend and who gave access? If not, what is the delivery position and your first available date? Please also reissue invoice NBL-013-INV-09 showing the amount. (blocking; Invoice NBL-013-INV-09 (event-023) shows no amount and the file holds no confirmed appointment or work result; on 02/09 the glass had not arrived (event-021). Scope, attendance and the priced invoice are the contractor's to answer (RTE-CONTRACTOR).)
- Ask **tenant**: Has anyone attended to fit new glass in the kitchen? Is the glazing still misted between the panes, and has any damp, mould or staining appeared around the frame or nearby wall since July (photo if possible)? (blocking; The tenant can independently confirm whether the billed work happened, and the damp/cold concern reported on 31/07 (index, event-001) was never assessed on site (event-005). Facts about the fault and access are tenant-owned (RTE-TENANT).)

Promises made or recorded:
- agency → contractor: If no reply within 2 working days, the case goes to the property manager to review the instruction and the invoice. by 2 working days from today [open]
- agency → tenant: Come back with a fitting slot as soon as the contractor replies, agreeing it with her before booking; contractor has a 2-working-day reply-by. by 2 working days from today [open]
- agency → landlord: Update once the contractor replies; no spend beyond the approved £180 incl. VAT and the unpriced invoice not passed for payment. [open]
- agency → tenant: Earlier promise (event-019) to be in touch when the glass arrived to arrange a date — unkept since 24/08; superseded by today's chase and update. [superseded]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
