# ANSWER — Case 025 — Kitchen tap maintenance request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Kitchen tap replaced and invoiced, but the invoice is unpriced, attendance and key return unconfirmed; contractor and landlord chased, ticket on hold.
**Stage:** on_hold · **Hold:** Waiting for Provider — contractor to supply invoice total with VAT, attendance date and key return (ACT-1, 2 working days); in parallel Waiting for Landlord for completion confirmation and drawer instruction (ACT-3, 3 days).
**Last update:** 2025-09-15 11:11:18 UTC (event-022) · **Decided:** 2026-10-10 15:45 UTC
**Next step:** Bracken & Vale Plumbing to send the priced corrected invoice (total + VAT), the attendance date and confirmation the office spare key is returned, by close of the second working day (ACT-1).

Definition of done (3/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-002: dripping tap categorised as routine plumbing, no emergency criteria met; cloudy water recorded as tenant suspicion, advice on aerated water given to tenant at ACT-2
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-003 — landlord approved the maintenance works (tap). Drawer repair has no authority yet: asked at ACT-3
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-004 — Bracken & Vale Plumbing instructed to quote/attend; tenant kept informed at event-006, event-009, ACT-2
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-016 confirmed 10 September with the tenant's key authorisation (event-015), but event-017 left timing open and no attendance confirmation exists; chased at ACT-1
- [-] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No priced quote was ever returned by the contractor (event-004, event-005); landlord gave a general approval at event-003 and work proceeded without a priced quote — flagged to the landlord at ACT-3
- [ ] work_result: Work result recorded from the provider — Only the invoice description evidences the work (event-022); no job report, photos or attendance date; asked contractor (ACT-1) and tenant (ACT-2)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Corrected invoice on file (corrected-plumbing-invoice.pdf) but unpriced; no photos; priced copy requested at ACT-1
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Cannot forward a priced invoice: no amount stated (F6). Landlord told it is coming (ACT-3)
- [ ] landlord_confirmation: Landlord confirmed completion — Requested at ACT-3; 3-day reply window
- [ ] keys_returned: Keys returned, where a management key was issued for the visit — Office spare key issued for the visit (event-018); return not recorded; requested at ACT-1
- [ ] closed: Request closed with a resolution that names who paid — Open items above; closure would name who paid, which is not yet established

## 1. Decision

Tap work appears done and was landlord-approved (event-003), but the corrected invoice (event-022) states no amount, no attendance date is confirmed, and the office spare key issued for access (event-018) is not recorded as returned — so the request cannot be closed. Chased the contractor for the priced invoice, attendance date and key (ACT-1); told the tenant what the invoice records and asked whether the drip and cloudy water are resolved (ACT-2); put the priced invoice, the completion confirmation and the newly reported kitchen drawer to the landlord for instruction (ACT-3); logged the open items (ACT-4) and placed the ticket on hold (ACT-5). No new spend instructed: no standing cap is on file and the drawer is a separate job.

Safety actions taken first:
- Safety-pass check — cloudy water: no hazard reported or observed; the tenant described appearance only and no sample or test exists (event-002, event-004). Tenant asked whether it persists after the tap change and told to report immediately any failure to clear or any change in taste or smell, with escalation to the plumber and water supplier (ACT-2).
- Safety-pass check — boiler/gas: a boiler matter is mentioned only in passing in a call (event-021) and forms no part of this job; no gas symptom is reported. Recorded, no gas action triggered on this ticket.
- No emergency criteria met: no loss of water, heating or hot water, no leak onto electrics, no insecurity (event-001).

Actions deliberately withheld:
- Did not close the request: work result, priced invoice, landlord confirmation and key return all outstanding (CAP-CLOSE).
- Did not instruct any contractor for the kitchen drawer repair: no standing cap on file and the landlord's 5 August approval (event-003) covered the tap works only (APR-SPEND-OVER-CAP).
- Did not state or approve any invoice amount, and did not suggest who pays for any element (PRO-PAYMENTS, PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-REQUEST-APPROVAL, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, APR-SPEND-OVER-CAP, CAP-CLOSE, PRO-TENANT-LIABILITY, PRO-PAYMENTS
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported a constantly dripping kitchen mixer tap and cloudy-looking water, asking whether a replacement tap could be considered, on 4 August 2025. [index, event-001; high]
- F2: The landlord, Orin Bell, approved proceeding with the maintenance works on 5 August 2025 and said email is the best contact. [event-003; high]
- F3: No landlord standing spend cap is on file in this case record; default authority is therefore £0 for non-emergency spend. [get_case_details, mandate CAP-DISPATCH-ROUTINE; medium]
- F4: A visit was arranged for 10 September 2025 with the contractor collecting the agency spare key; the contractor said the late confirmation was difficult but would try to accommodate. No attendance confirmation is recorded. [event-015, event-016, event-017, event-018; high]
- F5: The first invoice (15 September) carried a postcode differing from the property record and was returned for correction; the corrected invoice records 'Supply and install one new mono kitchen sink tap' at 18 Thistlewick Row, ZZ1 1ZZ. [event-019, event-020, event-021, event-022, corrected-plumbing-invoice; high]
- F6: The corrected invoice (ref NBL-025-INV-15) states no amount, no VAT and no labour/parts breakdown. [corrected-plumbing-invoice, get_attachment; high]
- F7: On 5 September the tenant reported a separate fault: the top kitchen drawer is loose with its metal front brackets apparently snapped, and asked if it could be repaired at the same visit. No response to that item is recorded before now. [event-012; high]
- F8: The cloudy-water element of the report was passed to the landlord and the contractor as a tenant suspicion of limescale, with no water sample or test result available; no investigation result is recorded. [event-002, event-004; high]
- F9: A boiler matter was mentioned in passing during a 15 September call; no boiler work is documented as part of this tap job. [event-021; medium]

Conflicts between sources:
- Invoice postcode differed from the property's recorded postcode on the first invoice; call transcript also records address confusion by the contractor. → Corrected invoice and the attachment text both show 18 Thistlewick Row, Fenmere, ZZ1 1ZZ, matching the case record (get_case_details); no residual conflict about the property. (tool_check)

Red flags:
- [data_quality] Corrected invoice NBL-025-INV-15 carries a work description but no amount, VAT or breakdown; it cannot be passed to the landlord or used to establish who paid. → Priced copy requested from the contractor (ACT-1); landlord told the invoice is pending (ACT-3)
- [data_quality] Work appears to have been carried out and invoiced with no attendance confirmation on file and no priced quote ever returned, after repeated contractor non-response (event-005, event-009, event-013). → Attendance date requested (ACT-1); pattern logged (ACT-4) for office review if the contractor does not reply
- [other] An office spare key was issued to the contractor for access and no return is recorded — a property security housekeeping item, not a reported hazard. → Key return requested from the contractor (ACT-1); listed as an open closure item (ACT-4)

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "025", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=corrected-plumbing-invoice.pdf | {"name": "corrected-plumbing-invoice.pdf", "text": "B I L L I N G  D O C U M E N T Bracken & Vale Plumbing — Corrected Invoice\nBracken & Vale Plumbing\nInvoic… | allow |
| 4 | search_history | completed | query=key collection office spare key return | [] | allow |
| 5 | search_history | completed | query=drawer brackets cloudy water | [] | allow |
| 6 | search_history | completed | from_party=Contractor, query=invoice amount total work completed | [] | allow |
| 7 | notify_contractor | completed (ledger) | message=Re: 18 Thistlewick Row, Fenmere, ZZ1 1ZZ — kitchen mixer ta… | {"id": "ACT-1"} | CAP-NOTIFY |
| 8 | notify_tenant | completed (ledger) | message=Dear Ms Calder,  An update on your kitchen tap report (18 T… | {"id": "ACT-2"} | CAP-NOTIFY |
| 9 | notify_landlord | completed (ledger) | message=Dear Mr Bell,  Update on 18 Thistlewick Row, Fenmere — kitc… | {"id": "ACT-3"} | CAP-NOTIFY |
| 10 | add_note | completed (ledger) | note=Tap job: landlord approval on file (event-003); work invoic… | {"id": "ACT-4"} | CAP-LOG |
| 11 | put_on_hold | completed (ledger) | reason=Waiting for Provider — Bracken & Vale Plumbing to supply th…, until=2 working days for the contractor; 3 days for the landlord | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Please send the corrected invoice NBL-025-INV-15 showing the total with labour, parts and VAT; confirm the date the engineer attended and installed the tap; and confirm the office spare key has been returned. (blocking; The invoice on file carries no amount, attendance was never confirmed after the 10 September slot, and a management key was issued for access (event-016, event-017, event-018, event-022).)
- Ask **landlord**: Do you confirm the tap work as complete once the priced invoice reaches you, and how would you like us to handle the separately reported loose kitchen drawer (obtain a quote, use your own contractor, or leave it)? (blocking; No standing spend cap is on file, so any new work needs the landlord's instruction; completion confirmation is a closure item (event-003, event-012).)
- Ask **tenant**: Has the dripping stopped since the new tap was fitted, and does the water still look cloudy when you fill a glass? (non-blocking; The cloudy-water element of the original report (event-001) was never investigated and the work result is otherwise unverified.)

Promises made or recorded:
- agency → tenant: Come back with next steps on the kitchen drawer once the landlord instructs by after landlord reply (3 days from ACT-3) [open]
- agency → landlord: Forward the priced invoice once the contractor supplies the total with VAT by on receipt from contractor [open]
- agency → contractor: Refer invoice and outstanding key to the office if no reply by close of the second working day by 2 working days from ACT-1 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
