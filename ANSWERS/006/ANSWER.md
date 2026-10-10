# ANSWER — Case 006 — Case 006: Check-Out Works: Carpet Replacement and Repainting

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Check-out works auto-closed; landlord completion confirmation, provider/property record conflict and alarm test unevidenced — escalated to the office.
**Stage:** final_checks
**Last update:** 2024-10-29 15:55:08 UTC (event-027) · **Decided:** 2026-10-10 14:00 UTC
**Next step:** Property manager to resolve the Cedar Utilities / Sawyer and Flat 21 / Flat 12 record conflict and confirm the works were done at Flat 21; landlord to confirm completion and invoice (asked, ACT-2).

Definition of done (6/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (scope logged), categorised as routine check-out works at a vacant flat; no damage-limiting advice needed — property vacant.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-015 — landlord's own message "Pls go ahead" approving the event-013 quote.
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Cedar Utilities assigned and briefed (event-003, event-005) but completion recorded against Sawyer (event-020); link unevidenced.
- [-] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever confirmed in the history despite three chases (event-006, event-007, event-008); property vacant so tenant access consent not required.
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-013 quote, approved by the landlord at event-015; VAT not stated — queried (ACT-2).
- [ ] work_result: Work result recorded from the provider — event-020 "Sawyer completed" is a system note with no photos, no address and no provider confirmation.
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-023 — skip reason recorded: "Sawyer invoices landlord directly".
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-023 — contractor invoices the landlord direct; receipt queried with the landlord (ACT-2).
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 flagged it as needed; no landlord message after event-015; requested at ACT-2.
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-026 — keys return confirmed 29 Oct 2024.
- [ ] closed: Request closed with a resolution that names who paid — event-027 closed the request, but work_result, provider identity and landlord confirmation are unevidenced; office to decide whether the closure stands.

## 1. Decision

The ticket was closed by the agency's automation (event-027) while three checks are not evidenced: the landlord's completion confirmation (flagged needed at event-024, no landlord reply after event-015), a conflict in the agency's own records about which provider holds the job (Cedar Utilities, event-003/005, vs "Sawyer", event-013/016/020) and which property the attending contractor was at (event-018 names Flat 12, 122 Juniper Mews, Westmarsh), and no record that smoke/CO alarms were tested before the flat is remarketed. Deciding whether a closed job was performed at the right property, and whether to stand by that closure, is a human decision (ESC-CONFLICT, RTE-STAFF). Within my authority I recorded the conflicts (ACT-1) and asked the landlord to confirm completion, invoice receipt and VAT (ACT-2). I did not instruct any contractor: the works are already reported complete and a second instruction would duplicate the work order.

Safety actions taken first:
- Checked the whole history for smoke/CO alarm testing before remarketing: no record found; flagged for the office and the landlord.
- Confirmed no live hazard: the property is vacant (event-001) and 'burnt carpet' is damage, not an active fire or electrical fault, so the emergency-hazard playbook does not apply.

Actions deliberately withheld:
- Did not re-instruct or duplicate a work order: the works are already reported complete (event-020).
- Did not reopen or alter the system closure (event-027) — outside my authority.
- Did not apportion the burnt carpet to the tenant or mention deposit deductions (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Did not relay the Flat 12 / Cedar Utilities discrepancy to the landlord or contractor as a settled fact (rule 2).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, ESC-CONFLICT, RTE-STAFF, RTE-LANDLORD, CAP-DISPATCH-APPROVED, PRO-TENANT-LIABILITY, PRO-LEGAL, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property on the ticket is Flat 21, 11 Juniper Mews, Northbridge, ZZ7 0ZZ; request is check-out works after the tenant vacated: replace burnt carpet and repaint throughout. [index, event-001, get_case_details; high]
- F2: Maintenance provider assigned and briefed on 20 Sep was Cedar Utilities; three chases were sent for an appointment (20, 21, 24 Sep) and the system flagged 3+ reminders with no booking. [event-003, event-005, event-006, event-007, event-008; high]
- F3: The only contractor reply on file gives costs for work "at the studio" and no appointment details; it names no address. [event-012; high]
- F4: Quote relayed to the landlord on 9 Oct, attributed to "Sawyer": painting GBP 220, carpet approx 27 sqm GBP 240, bathroom vinyl GBP 100, chrome sink waste GBP 45 (GBP 605 total); VAT not stated. [event-013; high]
- F5: The landlord approved the quoted works in his own message: "Pls go ahead" (9 Oct 19:37). [event-015; high]
- F6: Two of the four approved line items (bathroom vinyl, chrome sink waste) were not in the original request. [event-001, event-013; high]
- F7: A hold note of 15 Oct records Sawyer attending Flat 12, 122 Juniper Mews, Westmarsh, ZZ8 7ZZ — a different property from this ticket. [event-018; high]
- F8: Work recorded complete on 26 Oct ("Sawyer completed"); documents skipped with reason "Sawyer invoices landlord directly"; landlord confirmation flagged as still needed; keys return confirmed 29 Oct; request then closed as all checks complete. [event-020, event-023, event-024, event-026, event-027; high]
- F9: No landlord message appears in the history after the approval at event-015, so no landlord confirmation of completion is on file. [search_history, event-024; high]
- F10: No record in the case of smoke or carbon monoxide alarms being tested before the flat is remarketed. [search_history; high]
- F11: Priority could not be decreased to 0 at key-return (current priority 1). [event-026; high]

Conflicts between sources:
- Agency records disagree on who holds the job: Cedar Utilities was assigned and chased, while the quote, approval relay and completion are recorded against "Sawyer". → Recorded in the case note (ACT-1) and put to the office; no side taken in any message to a party. (unresolved)
- Agency records disagree on the property: this ticket is Flat 21, 11 Juniper Mews, Northbridge, but the attendance hold names Flat 12, 122 Juniper Mews, Westmarsh, and the contractor reply calls the unit "the studio". → Escalated to the property manager; closure rests on an unverified attendance address. (unresolved)
- Landlord named as "Oscar" in the quote email but the hold asks whether "Ruben" approved the quote. → Not used; the landlord was addressed without a first name (ACT-2). (unresolved)
- Event-024 records landlord confirmation as outstanding; event-027 closes the request as all checks complete. → Landlord asked to confirm completion and invoice (ACT-2); closure flagged to the office. (unresolved)

Red flags:
- [data_quality] Completion and closure recorded against a provider and an address that the agency's own records do not tie to this ticket (Cedar Utilities vs Sawyer; Flat 21 Northbridge vs Flat 12 Westmarsh). → Logged in the case note (ACT-1) and escalated to the property manager.
- [other] Approved spend includes two items (bathroom vinyl GBP 100, chrome sink waste GBP 45) outside the original instruction, and the quote states no VAT; the landlord nonetheless approved it in his own words. → VAT position queried with the landlord (ACT-2); no spend instructed by me.
- [other] Pre-remarketing smoke and carbon monoxide alarm test is nowhere recorded in the case; this is a check to make, not a reported hazard. → Named in the landlord message (ACT-2) and in the handover for the office to book.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "006", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=alarm smoke carbon monoxide detector tested | [] | allow |
| 4 | search_history | completed | from_party=Contractor | [{"event": "event-012", "timestamp": "2024-10-09 12:52:13 UTC", "channel": "Email", "from": "Contractor", "to": "Agency / system", "excerpt": "[2024-10-09 12:5… | allow |
| 5 | search_history | completed | from_party=Landlord | [{"event": "event-015", "timestamp": "2024-10-09 19:37:08 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2024-10-09 19:37:… | allow |
| 6 | add_note | completed | note=Post-closure review (ticket closed by system at event-027).… | {"id": "ACT-1"} | CAP-LOG |
| 7 | notify_landlord | completed | message=Re: Flat 21, 11 Juniper Mews, Northbridge, ZZ7 0ZZ — check-… | {"id": "ACT-2"} | CAP-NOTIFY |

## 4. Human handover / information requested

**To:** property_manager
**Question:** The check-out works at Flat 21, 11 Juniper Mews were auto-closed on 29 Oct — do we stand by that closure, or reopen until we can evidence that "Sawyer" (not the assigned provider Cedar Utilities) did the work at this flat and the landlord confirms it?
**Facts (≤5):**
- Provider assigned and briefed was Cedar Utilities (event-003, event-005); the quote, approval relay and completion sit against "Sawyer" (event-013, event-016, event-020) with no record linking them.
- Hold note event-018 records Sawyer attending Flat 12, 122 Juniper Mews, Westmarsh ZZ8 7ZZ; the only contractor reply (event-012) refers only to work "at the studio" and names no address.
- Landlord approved the GBP 605 of works in his own reply "Pls go ahead" (event-015) against the quote in event-013; the quote states no VAT and includes bathroom vinyl GBP 100 and a sink waste GBP 45 beyond the original request (event-001).
- Landlord confirmation was flagged as outstanding (event-024) and no landlord message appears after event-015, yet event-027 closed the request as all checks complete.
- No record anywhere in the case that smoke or carbon monoxide alarms were tested before remarketing; documents/invoice skipped because "Sawyer invoices landlord directly" (event-023); keys returned (event-026).
**Gap:** No evidence of which firm attended, at which address; no landlord confirmation of completion; VAT position on the GBP 605 unknown; smoke/CO alarm test status unknown.
**Options:**
- Reopen to final_checks: obtain the landlord's written confirmation (already requested, ACT-2) and the contractor's confirmation of the address worked on, then re-close naming the landlord as payer.
- Stand by the closure, log the provider/property discrepancy as a data-quality correction, and book the smoke/CO alarm test separately before remarketing.
- Ask the landlord or accounts for Sawyer's invoice first, to evidence the address worked on and the VAT position.
**Recommended:** Reopen to final_checks: landlord confirmation is already requested; add a contractor confirmation of the address and an alarm test before the flat is remarketed.
**Default if no answer:** Ticket stays closed on the system record with the discrepancies logged (ACT-1) and the alarm test unverified.
**Deadline:** Before the flat is remarketed / before the landlord settles Sawyer's invoice
**Undo:** Nothing irreversible by me: one internal note (ACT-1) and one landlord message (ACT-2). No contractor instructed, no spend committed, no closure altered.
**Context:** event-001, event-003, event-005, event-012, event-013, event-015, event-016, event-018, event-020, event-023, event-024, event-026, event-027

Promises made or recorded:
- agency → landlord: Confirm that smoke and CO alarms have been tested before the flat is remarketed by before remarketing [open]
- agency → tenant: Provider will contact the tenant to arrange a time (event-004) [superseded]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge report within one working day
