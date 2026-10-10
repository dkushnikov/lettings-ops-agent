# ANSWER — Case 005 — Case 005: Check-Out Cleaning

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Void clean at Flat 10 done and keys returned, but invoice, landlord confirmation and an alarm test are outstanding; chased provider and escalated.
**Stage:** final_checks · **Hold:** Waiting for Provider — invoice chased with a 3-working-day reply-by; file also with the office for the alarm-test safety check.
**Last update:** 2024-12-12 17:27:29 UTC (event-037) · **Decided:** 2026-10-10 13:20 UTC
**Next step:** Property manager to confirm a smoke/CO alarm test was carried out at Flat 10 before the 30/11/2024 move-in and to reopen final checks; provider (Ava, Stonebridge Works) to send the invoice within 3 working days.

Definition of done (6/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-004: clean scoped from the check-out report; routine, void property (event-002)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-016 — landlord's own approval message
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003, event-004 — Stonebridge Works instructed; no tenant in occupation to brief (event-002)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-024 — 'Ava cleaning on Saturday AM'
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-016 approved the quote (£135+£45+£25, no VAT stated), but event-017 added a second bedroom carpet the quote does not price; excess unapproved
- [x] work_result: Work result recorded from the provider — event-025 — check clean completed, ready for move-in 30/11/2024
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No invoice or photos on file; invoice chased at ACT-1 with a 3-working-day reply-by
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Invoice not received (event-026, event-030); landlord told it will be forwarded on arrival (ACT-2)
- [ ] landlord_confirmation: Landlord confirmed completion — event-034 'Need confirmation from landlord'; no landlord reply after event-016
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-025, event-036 — keys returned and return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-037 marked closed, but invoice, landlord confirmation and the detector 'Tested? No' safety check (attachment-01) are outstanding; office asked to reopen

## 1. Decision

Chased the provider for the outstanding invoice with a 3-working-day reply-by, told the landlord the position on the invoice and the unapproved extra carpet, logged the file review, and escalated to the property manager: the check-out report records the smoke/CO detectors as "Tested? No" and the flat was re-let for move-in on 30/11/2024 with no alarm test on file, the request was closed (event-037) while the invoice and landlord confirmation were still outstanding, and a second address (Flat 27, 117 Lantern Quay) appears inside this Flat 10 job thread.

Safety actions taken first:
- Flagged the check-out report's detector line 'Tested? No' against a property re-let on 30/11/2024 and escalated for an alarm test to be confirmed or arranged.
- Informed the landlord that the alarm test is being confirmed by the office.
- Did not treat the report's general 'alarms checked and working' boilerplate as evidence of a test.

Actions deliberately withheld:
- Did not close the request: invoice, landlord confirmation and the alarm-test check are outstanding (CAP-CLOSE).
- Did not approve or pay any invoice (PRO-PAYMENTS).
- Did not tell any party which property event-011 refers to, and did not decide any tenant deposit deduction for cleaning (PRO-TENANT-LIABILITY, PRO-LEGAL).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, RTE-STAFF, ESC-SAFETY, ESC-CONFLICT, APR-SPEND-OVER-CAP, PRO-PAYMENTS, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 10, 160 Alder Lane, Westmarsh, ZZ8 9ZZ; job NBL-005-0163; request is an end-of-tenancy clean after the tenant vacated (all appliances, freezer defrost, bedroom 2 carpet). [index, event-001, event-004, get_case_details; high]
- F2: Property is not tenanted at the time of the request; the system paused the ticket for manual handling. [event-002; high]
- F3: Quote from Stonebridge Works (Ava Nolan): general EOT clean with deep clean of bathroom and kitchen £135, shampoo bedroom 2 carpet £45, defrost freezer £25; £205 is a calculated sum, with no total and no VAT stated. [attachment-02-cleaning-quote, attachment-03-cleaning-quote; high]
- F4: Landlord (Palmer) approved the work in his own message: 'Yes please go ahead. Let them do the carpets too.' [event-016; high]
- F5: The agency then instructed the provider to clean both bedroom carpets, beyond the single bedroom 2 carpet priced in the quote; no price for the second carpet is on file. [event-017, attachment-02-cleaning-quote; high]
- F6: The clean was carried out (provider booked Saturday AM) and the agency recorded the check clean completed and keys returned ready for move-in on 30/11/2024; keys return later confirmed. [event-024, event-025, event-036; high]
- F7: No invoice has been received: requested 04/12/2024, chased 12/12/2024; provider replies in between are garbled or mis-threaded. [event-026, event-027, event-030, event-028, event-029, event-032, event-033; high]
- F8: The system recorded 'Need confirmation from landlord' and then closed the request as all checks completed, although no landlord confirmation and no invoice are on file. [event-034, event-037; high]
- F9: The check-out inspection report's detector section records 'Tested? No' with no detector comments; the report's general guidance text separately states alarms were checked and working. [attachment-01-check-out-inspection-report; high]
- F10: No landlord standing spend cap or standing instruction is available in this case record; the only spend authority is the landlord's own approval message. [get_case_details, event-016; medium]

Conflicts between sources:
- A Flat 10 job thread contains an agency email about a quote for a different property, 'Flat 27, 117 Lantern Quay, Kingshaven, ZZ4 6ZZ'. → Not stated to any party; referred to the office in the handover and internal note. All agency action kept to the address on the agency's own job record (Flat 10). (unresolved)
- The check-out report's specific detector line ('Tested? No') contradicts the same report's boilerplate that smoke and CO alarms were checked and working. → The specific line beats the general statement in the same document: detectors treated as not tested; office asked to confirm a test around the 30/11/2024 move-in. (source_hierarchy)
- System closed the request as 'all checks completed' while the invoice and landlord confirmation were outstanding. → Final checks treated as incomplete; provider chased, landlord updated, office asked to reopen. (tool_check)

Red flags:
- [safety_hazard] Check-out report records smoke/CO detectors as 'Tested? No' and the flat was re-let for move-in on 30/11/2024 with no alarm test recorded. → Escalated to the property manager; landlord informed the office is confirming an alarm test; internal note logged.
- [data_quality] Several contractor emails are third-person summaries or garbled, and one agency email in this thread refers to a quote for a different property (Flat 27, 117 Lantern Quay). → Recorded as a conflict; no party told which address is correct; office asked to resolve.
- [other] Agency instructed cleaning of both bedroom carpets when only bedroom 2 was quoted, so the invoice may exceed the approved £205. → Provider asked to itemise any extra separately; landlord told any excess returns to him for approval.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "005", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_contractor | completed | message=Job NBL-005-0163 — Flat 10, 160 Alder Lane, Westmarsh, ZZ8… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed | message=Flat 10, 160 Alder Lane, Westmarsh, ZZ8 9ZZ — job NBL-005-0… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | add_note | completed | note=Case review, job NBL-005-0163, Flat 10, 160 Alder Lane. (1)… | {"id": "ACT-3"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Flat 10, 160 Alder Lane was re-let on 30/11/2024 after the check-out report recorded the smoke/CO detectors as 'Tested? No' — can you confirm an alarm test was done before move-in, and reopen final checks, which were closed with the invoice still missing?
**Facts (≤5):**
- Check-out report detector section records 'Tested? No' (and the detector photo caption repeats it); the same report's general boilerplate that alarms 'were checked and working' is beaten by that specific line (attachment-01-check-out-inspection-report).
- Agency note of 27/11/2024 records the check clean completed and keys returned ready for move-in on 30/11/2024 (event-025); keys return confirmed (event-036). No alarm test appears anywhere in the history.
- Landlord Palmer approved the clean and carpets in his own message of 16/11/2024 (event-016); quote items £135 general EOT clean + £45 bedroom 2 carpet + £25 freezer defrost = £205 calculated, no VAT stated (attachment-02/03-cleaning-quote).
- Scope was extended at event-017 to BOTH bedroom carpets, which the approved quote does not price; any excess over £205 needs the landlord's approval before payment (RTE-LANDLORD).
- Invoice never arrived: requested event-026, chased event-030, provider replies garbled or mis-threaded (event-028/029/032/033); the request was nevertheless marked closed at event-037 with invoice and landlord confirmation pending.
**Gap:** Whether smoke and CO alarms were tested before the new tenancy began; whether the second bedroom carpet was cleaned and at what price; why a quote for 'Flat 27, 117 Lantern Quay, Kingshaven' is discussed in this Flat 10 job thread (event-011).
**Options:**
- Confirm or arrange an alarm test at Flat 10 now and reopen final checks until the invoice arrives — safest; small cost for a test visit if none was done.
- Treat the report's boilerplate as sufficient and leave the file closed — leaves a possible Smoke and Carbon Monoxide Alarm (England) Regulations 2015 breach in an occupied flat.
- Close without payment if the provider never invoices — ends the chase but risks a late invoice landing against a closed job plus an unapproved carpet charge.
**Recommended:** Confirm or arrange an alarm test at Flat 10 now and reopen final checks until the invoice and the landlord's confirmation are in.
**Default if no answer:** If the provider does not invoice within the 3-working-day reply-by, the file returns to the office for manual follow-up; no payment is made and nothing is approved meanwhile.
**Deadline:** Alarm-test confirmation: immediate (occupied property). Invoice: 3 working days from the chase of today.
**Undo:** Nothing irreversible: only a chase to the provider (ACT-1), an update to the landlord (ACT-2) and an internal note (ACT-3). No spend authorised, no new instruction issued.
**Context:** event-011, event-016, event-017, event-025, event-026, event-030, event-037, attachment-01-check-out-inspection-report, attachment-02-cleaning-quote

Promises made or recorded:
- agency → contractor: If no invoice within 3 working days the file goes to the office for manual follow-up by 3 working days from the chase [open]
- agency → landlord: Forward the provider's invoice for confirmation on arrival and seek approval for any amount above the £205 quote [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge within one working day
