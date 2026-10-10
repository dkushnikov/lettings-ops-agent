# ANSWER — Case 005 — Case 005: Check-Out Cleaning

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Check-out clean done and approved, but ticket was closed with no invoice, no landlord confirmation, and detectors recorded "Tested? No" before the 30/11 move-in.
**Stage:** final_checks · **Hold:** Waiting for Provider — itemised invoice for Job NBL-005-0163 chased with a 3-working-day reply-by (ACT-2); alarm-test question with the property manager.
**Last update:** 2024-12-12 17:27:29 UTC (event-037) · **Decided:** 2026-10-10 14:00 UTC
**Next step:** Property manager to arrange/confirm a smoke and CO alarm test at Flat 10 (now occupied) and decide the billing route; provider to send the itemised invoice within 3 working days (ACT-2).

Definition of done (7/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 request logged; check-out report sent to provider at event-007; routine, vacant property (event-002)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-016 — landlord Palmer: 'Yes please go ahead. Let them do the carpets too.' after the quote was sent at event-015
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003 provider assigned; briefed at event-004 and instructed at event-017
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-024 — 'Ava cleaning on Saturday AM'; property vacant, no tenant access needed
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-015 quote to landlord, event-016 landlord approval; £205 calculated from attachment-02/03, VAT status not stated by the provider
- [x] work_result: Work result recorded from the provider — event-025 — 'Check clean completed and keys returned ready for move in on 30/11/2024'
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No invoice on file; requested event-026, chased event-030, provider replies event-029/032/033 unresolved; chased again ACT-2
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Cannot forward — no invoice received (event-033 claims an attachment was sent; not on file)
- [ ] landlord_confirmation: Landlord confirmed completion — event-034 'Need confirmation from landlord'; no landlord reply after event-016
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-025 and event-036 'Keys return confirmed'
- [ ] closed: Request closed with a resolution that names who paid — event-037 closed the request, but documents, invoice_to_landlord and landlord_confirmation were open and the pre-move-in alarm test is unverified (attachment-01 'Tested? No')

## 1. Decision

Reopen for final checks. The clean was approved by the landlord (event-016), carried out and the keys returned for a 30/11/2024 move-in (event-024, event-025), but the system closed the job (event-037) with three checks still open: no invoice on file, nothing forwarded to the landlord, no landlord completion confirmation. Separately, the check-out report records the smoke/CO detectors as "Tested? No" (attachment-01) and there is no record of an alarm test before the property was released for move-in — a safety check at a now-occupied property that a person must own. I chased the provider for the itemised invoice with a 3-working-day reply-by (ACT-2) and recorded the findings (ACT-1); I did not re-close the request, decide the unquoted bedroom 1 carpet charge, or instruct any further spend (no standing cap on file for this landlord).

Safety actions taken first:
- Named the smoke/CO alarm check and its result ('Tested? No', attachment-01) in the case note and made it the lead question of the handover, because the flat was released for a move-in on 30/11/2024 with no alarm test on record.

Actions deliberately withheld:
- Did not re-close the request (CAP-CLOSE: documents, invoice_to_landlord and landlord_confirmation still pending).
- Did not instruct any further work or alarm test (no standing cap on file; APR-SPEND-OVER-CAP).
- Did not decide whether any cleaning cost is tenant-payable from the deposit (PRO-TENANT-LIABILITY).
- Did not state an invoice total or VAT position to the landlord, as no invoice is on file.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, PRO-TENANT-LIABILITY, ESC-SAFETY, RTE-STAFF, RTE-CONTRACTOR, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Job NBL-005-0163 is end-of-tenancy cleaning at Flat 10, 160 Alder Lane, Westmarsh, ZZ8 9ZZ, raised after the tenant vacated. [index, event-001, event-004; high]
- F2: The provider's quote lists £135 general EOT/deep clean, £45 bedroom 2 carpet shampoo and £25 freezer defrost; £205 is a calculated sum, no total and no VAT status stated. [attachment-02-cleaning-quote, attachment-03-cleaning-quote; high]
- F3: The landlord approved the quote and the carpets in his own message. [event-016; high]
- F4: The agency instructed the provider to clean both bedroom carpets, whereas the quote prices bedroom 2 only. [event-017, attachment-02-cleaning-quote; high]
- F5: The clean was completed and keys returned ready for a move-in on 30/11/2024. [event-024, event-025, event-036; high]
- F6: The check-out report's detector section records 'Tested? No' and the detector photo caption repeats that detectors were not tested, contradicting the report's boilerplate that alarms were checked and working. [attachment-01-check-out-inspection-report; high]
- F7: No invoice has been received despite a request and a chase; the provider's replies suggest an attachment was sent but none is on the case file. [event-026, event-030, event-033; medium]
- F8: The system closed the request as 'All checks have been completed' while invoice, invoice-to-landlord and landlord confirmation were outstanding. [event-034, event-037; high]

Conflicts between sources:
- Check-out report boilerplate says smoke and CO alarms were checked and working; the same report's detector section records 'Tested? No'. → The specific detector line beats the general statement: detectors treated as not tested; verification raised with the property manager. (source_hierarchy)
- event-011 refers to a quote for 'Flat 27, 117 Lantern Quay, Kingshaven' on this Flat 10 job, while both quote documents name Flat 10. → Treated as an agency typing error in an outbound email; both quotes and job id NBL-005-0163 are for Flat 10. Recorded, not acted on in any message to a party. (source_hierarchy)
- Landlord-addressed quote wording ('Hi Palmer... do you wish to proceed?') was sent to the provider at event-013 before the landlord received it at event-015. → Authority relied on is the landlord's own reply at event-016 to the correctly addressed email event-015. (tool_check)

Red flags:
- [safety_hazard] Smoke/CO detectors recorded as not tested at check-out and no test recorded before the property was released for a move-in on 30/11/2024 (now occupied). → Lead question of the handover to the property manager; recorded in case note ACT-1.
- [data_quality] Outbound agency email on this job cites a different property's quote ('Flat 27, 117 Lantern Quay'); several hold notes have no retrievable text; the job was auto-closed with checks open. → Recorded in ACT-1 and the handover; no party was told which address is 'right'.
- [other] Provider's unconfirmed claim that an invoice attachment was sent; nothing on file, outcome unknown. → Single chase with a 3-working-day reply-by (ACT-2); no assumption of receipt.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "005", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Case review (check-out clean, Job NBL-005-0163, Flat 10, 16… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_contractor | completed | message=Job Id: NBL-005-0163 — Flat 10, 160 Alder Lane, Westmarsh,… | {"id": "ACT-2"} | CAP-NOTIFY |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Flat 10, 160 Alder Lane: the check-out report records smoke/CO detectors as 'Tested? No' and the flat was released for a move-in on 30/11/2024 — do you want an alarm test arranged now, and how should the missing cleaning invoice be settled?
**Facts (≤5):**
- Check-out report attachment-01 detector section: 'Tested? No', no detector comments; the report's boilerplate claim that alarms were checked and working is contradicted by that specific line.
- Property was recorded as cleaned, keys returned and ready for move-in on 30/11/2024 (event-025); no alarm test is recorded anywhere on the ticket.
- Landlord Palmer approved the clean and the carpets in his own message (event-016); quote items £135 + £45 + £25 = £205 calculated, no total and no VAT status stated (attachment-02, attachment-03).
- event-017 instructed the provider to clean BOTH bedroom carpets; the quote prices bedroom 2 only (£45), so any bedroom 1 charge is unquoted.
- Invoice requested (event-026) and chased (event-030); provider replies (event-029, event-032, event-033) imply an attachment was sent but none is on file, yet the system closed the job as 'All checks completed' (event-037).
**Gap:** Whether smoke/CO alarms were in fact tested at or before the 30/11/2024 move-in (no move-in/inventory record visible to me); whether the provider's invoice exists and what it totals; whether a bedroom 1 carpet charge was added. Safety items not addressed in the record: carbon monoxide (attachment-01-check-out-inspection-report).
**Options:**
- Arrange a smoke/CO alarm test at the occupied flat now (landlord approval needed for the spend — no standing cap on file) and keep the invoice chase running.
- Confirm from the move-in/inventory record that alarms were tested on or before 30/11/2024 and record that evidence; chase the invoice only.
- Leave the job closed as the system did — leaves the alarm test unverified and the £205-plus invoice unreconciled.
**Recommended:** Verify or arrange the alarm test first (option 2 if the move-in record shows a test, otherwise option 1), then reconcile the invoice against the approved quote before it goes to the landlord.
**Default if no answer:** If the provider does not invoice within 3 working days of ACT-2, billing is referred to the property manager; the alarm question stays open until a person answers it.
**Deadline:** Alarm verification: immediate (property occupied since 30/11/2024). Invoice: 3 working days from ACT-2.
**Undo:** Nothing irreversible done: one provider chase (ACT-2) and an internal note (ACT-1). No spend instructed, no closure re-issued.
**Context:** attachment-01-check-out-inspection-report, attachment-02-cleaning-quote, event-016, event-017, event-025, event-030, event-033, event-037

Promises made or recorded:
- agent → contractor: If the itemised invoice is not received within 3 working days, billing is referred to the property manager. by 3 working days from ACT-2 [open]

Clocks:
- CLK-SOP-ACK [prior]: Act on a provider reply within one working day
- CLK-S11 [in_force]: Repairs within a reasonable time once reported

## System notes

- reviewer: R11: safety pass — unaddressed item(s) noted: carbon monoxide (attachment-01-check-out-inspection-report)
