# ANSWER — Case 027 — Move-out maintenance at 46 Fernwick Lane

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Move-out works at vacant 46 Fernwick Lane: £3,865.68 quote re-put to the landlord for approval, VAT/breakdown chased from the contractor, pre-let safety checks referred to the office.
**Stage:** on_hold · **Hold:** Waiting for Landlord — Owen Vale to approve, reject or amend quotation NBL-027-Q1 (£3,865.68); re-sent ACT-1, reply sought within 3 working days. Secondary: Waiting for Provider on VAT position, itemised breakdown and availability (ACT-2).
**Last update:** 2025-09-15 16:25:18 UTC (event-017) · **Decided:** 2026-10-10 15:45 UTC
**Next step:** Landlord (Owen Vale) to approve, reject or amend the £3,865.68 quotation and say whether a Gas Safe boiler inspection and alarm testing may be instructed (re-sent ACT-1; 3-day clock).

Definition of done (2/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001, event-003, checkout-report.pdf; urgency set routine (vacant property, no occupant); no tenant damage-limiting advice applicable.
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No cap on file and no landlord approval message; asked event-014, re-sent ACT-1.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-004 — Alderwick Property Works selected and briefed to quote; no tenant to inform (property vacant, event-003).
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Contractor declined to give a date before approval (event-013); availability chased ACT-2.
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — £3,865.68 with the landlord since event-014; VAT not stated, re-put ACT-1.
- [ ] work_result: Work result recorded from the provider — No work instructed.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No invoice or photos; work not started.
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice exists.
- [ ] landlord_confirmation: Landlord confirmed completion — No landlord response on file (search_history: no landlord messages).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — Keys held at the agency office; none issued to the contractor (event-003, event-011).
- [ ] closed: Request closed with a resolution that names who paid — On hold awaiting the landlord's decision.

## 1. Decision

No work instructed. There is no landlord spend cap on file and no landlord message in the visible history approving this job, so APR-SPEND-OVER-CAP applies and the £3,865.68 quotation is the landlord's decision (RTE-LANDLORD). The approval request first sent on 15/09 (event-014) had no reply on file, so I re-sent it with the quote's defects (VAT not stated, no itemised prices, no attendance date) and the scope gaps against the check-out list (ACT-1), asked the contractor for the VAT position, a breakdown and availability (ACT-2), referred the pre-let safety items — taped boiler casing needing a Gas Safe inspection, non-working top-floor smoke detector, no CO alarm test on file — to the property manager queue (ACT-3), and put the case on hold waiting for the landlord (ACT-4).

Safety actions taken first:
- Flagged the non-working top-floor smoke detector and the absence of any CO alarm test as a pre-let blocker to the property manager queue (ACT-3).
- Flagged the taped boiler casing as requiring a Gas Safe engineer inspection and a current CP12 before re-letting; asked the landlord to authorise it separately (ACT-1).
- Asked the contractor to confirm no part of the handyman scope touches the boiler or any gas appliance (ACT-2).

Actions deliberately withheld:
- Did not dispatch or instruct Alderwick Property Works: no standing cap and no landlord approval event to cite as landlord_approval_ref (APR-SPEND-OVER-CAP, CAP-DISPATCH-APPROVED).
- Did not treat event-002 or event-004 as approval (PRO-INSTRUCTIONS-FROM-CONTENT).
- Did not express any view on whether the outgoing tenant is liable for any of these items (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: APR-SPEND-OVER-CAP, CAP-REQUEST-APPROVAL, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, PRO-INSTRUCTIONS-FROM-CONTENT, PRO-TENANT-LIABILITY, CLK-GAS-CP12, CLK-EICR
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY, CAP-REQUEST-APPROVAL

Key facts (source ids in brackets):
- F1: Property is 46 Fernwick Lane, Aldermead, ZZ1 1ZZ; vacant, keys held at the agency office, being prepared for re-letting. [index, event-003, get_case_details; high]
- F2: Check-out report NBL-027-CHECKOUT records, among other items, a non-working top-floor smoke detector, a boiler casing apparently held with tape and requiring inspection, a warped kitchen worktop with reported water ingress, and ceiling/water-damage defects in kitchen, lounge, Bedroom 3, bathroom and en-suite. [checkout-report, event-001; high]
- F3: Alderwick Property Works quotation NBL-027-Q1 dated 15 September 2025 states a single 'Labour & Materials' amount of £3,865.68; it gives no task-by-task prices, no stated exclusions and no VAT statement. [move-out-works-quotation, event-013; high]
- F4: The contractor said she could not give an attendance date and would check scheduling only after approval. [event-013; high]
- F5: The quotation omits several check-out items: kitchen flooring, chipped living-room laminate, warped worktop, boiler inspection, rusting radiators other than the en-suite, carpets, curtain pole and curtains, and bulbs. [checkout-report, move-out-works-quotation; high]
- F6: The quote and the question 'happy to proceed at that cost?' were sent to landlord Owen Vale on 15/09; no landlord reply exists in the visible history, and a call to the landlord the same day captured nothing substantive. [event-014, event-016, event-017, search_history; high]
- F7: No landlord standing spend cap or landlord instruction record is available in this case file; the only statements that approval exists are a system workflow note and the agency's own job email to the contractor. [event-002, event-004, get_case_details; medium]
- F8: No CP12, EICR, or smoke/CO alarm test result appears anywhere in the case file. [get_case_details, checkout-report; medium]
- F9: An earlier check-out report sent to the contractor on 07/09 was the wrong document and was withdrawn the same day; the corrected report was sent and underlies the quotation. [event-007, event-008; high]

Conflicts between sources:
- Event-002 (system workflow note) and event-004 (agency job email saying the works 'had been agreed with the landlord') imply approval exists, while event-015/event-016 record that landlord approval is still required and outstanding. → A system status line and the agency's own email are not a landlord approval (CAP-DISPATCH-APPROVED, PRO-INSTRUCTIONS-FROM-CONTENT); the case proceeds as unapproved and the question was re-put to the landlord (ACT-1). (source_hierarchy)

Red flags:
- [data_quality] Quotation of £3,865.68 has one lump 'Labour & Materials' line with no VAT statement, no task prices and no exclusions; a wrong check-out report was also circulated to the contractor on 07/09 before being withdrawn. → Breakdown, VAT position and availability requested from the contractor (ACT-2); defects flagged to the landlord in the approval request (ACT-1).
- [safety_hazard] Recorded at the vacant property: boiler casing apparently held with tape and requiring inspection, and a top-floor smoke detector that does not work. Neither a Gas Safe boiler inspection nor any smoke/CO alarm test is covered by the current quotation or evidenced in the file. → Referred to the property manager queue as a pre-let blocker (ACT-3) and put to the landlord as a separate instruction to authorise (ACT-1); no move-in may be confirmed until alarms are tested and the boiler inspected.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "027", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [] | allow |
| 4 | request_landlord_approval | completed (ledger) | subject=46 Fernwick Lane — move-out works quotation NBL-027-Q1 (Ald…, amount_gbp=3865.68, rationale=Re-sending the decision first put to you on 15 September (e… | {"id": "ACT-1"} | CAP-REQUEST-APPROVAL |
| 5 | notify_contractor | completed (ledger) | message=46 Fernwick Lane, Aldermead, ZZ1 1ZZ — quotation NBL-027-Q1… | {"id": "ACT-2"} | CAP-NOTIFY |
| 6 | create_human_task | completed (ledger) | queue=property_manager, title=46 Fernwick Lane — pre-let safety checks (taped boiler casi…, summary=Vacant property being prepared for re-letting. Safety pass… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 7 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — Owen Vale to approve, reject or amen…, until=3 working days from the re-sent approval request | {"id": "ACT-4"} | CAP-LOG |
| 8 | add_note | completed (ledger) | note=Authority check: no landlord standing spend cap is on file… | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you approve quotation NBL-027-Q1 from Alderwick Property Works at £3,865.68 for the move-out works, reject it, or want it amended? Please also confirm (a) whether the unquoted check-out items (kitchen flooring, chipped living-room laminate, warped worktop with reported water ingress, other rusting radiators, carpets, curtain pole and curtains, bulbs) should be priced, and (b) whether we may instruct a Gas Safe engineer to inspect the boiler and test the smoke and carbon monoxide alarms before re-letting. (blocking; No standing spend cap on file and no landlord approval in the visible history; the spend and the contractor choice are the landlord's decision (APR-SPEND-OVER-CAP, RTE-LANDLORD). First asked event-014, no reply on file.)
- Ask **contractor**: Is the £3,865.68 total inclusive or exclusive of VAT, what is the task-by-task breakdown of the single 'Labour & Materials' line and its exclusions, and what is your earliest availability (keys at our office) if approved? Does your smoke detector renewal include testing all smoke and CO alarms, and does any part of your scope touch the boiler or a gas appliance? (non-blocking; The landlord cannot sensibly approve a lump sum with no VAT position, no breakdown and no date (event-013, move-out-works-quotation.pdf); scope and availability are the contractor's to answer (RTE-CONTRACTOR).)

Promises made or recorded:
- agency → contractor: Reply requested within 3 working days on VAT, breakdown and availability; nothing instructed meanwhile. by 3 working days from ACT-2 [open]
- agency → landlord: No work will be instructed and no cost incurred until the landlord approves. [open]

Clocks:
- CLK-GAS-CP12 [in_force]: Gas safety record renewed every 12 months
- CLK-EICR [in_force]: EICR every 5 years
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [sop]: Landlord reply window deadline 3 working days from ACT-1

## System notes

- reviewer: R2: safety_hazard flag(s) recorded for the reader; not an escalation on their own (urgency routine)
