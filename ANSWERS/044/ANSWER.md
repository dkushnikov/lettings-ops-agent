# ANSWER — Case 044 — Case 044: Window Handle Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window handle at Flat 21 was approved and instructed, but closed without an invoice or landlord confirmation; I chased provider, tenant and landlord and flagged the tenant-identity conflict to the office.
**Stage:** final_checks · **Hold:** Waiting for Provider — Cedar Homes to resend the invoice, attendance date and photo (asked ACT-3, 3 working days); tenant and landlord confirmations also outstanding.
**Last update:** 2025-02-14 09:39:55 UTC (event-027) · **Decided:** 2026-10-10 14:13 UTC
**Next step:** Cedar Homes to send the missing invoice (amount + VAT), attendance date and photo within 3 working days; office to decide on reopening the closed ticket and reconcile the tenant name on record.

Definition of done (3/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 report; event-005/event-007 clarified which window; routine urgency set, no damage-limiting steps applicable to a detached window handle
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-012 — landlord's own message "Please go ahead" (CAP-DISPATCH-APPROVED); no spend cap on file
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-013/event-015 provider instructed; event-014 tenant told Cedar Homes would attend
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever recorded; chasers event-017, event-018, alert event-020; attendance date requested from Cedar Homes (ACT-3)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever produced; landlord approved the job itself at event-012 and no amount has been put to them
- [ ] work_result: Work result recorded from the provider — Only the provider's untrusted claim at event-019 with the attachment unavailable; tenant confirmation requested (ACT-4)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-023 skipped as "not needed", but the invoice and photo referenced in event-019 never arrived; re-requested (ACT-3)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice on file to forward; landlord informed of the position (ACT-5)
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 flagged it as needed; no landlord confirmation exists in the history; requested (ACT-5)
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — event-026 records a keys return but no artefact shows a management key was issued; flagged to the office (ACT-2)
- [ ] closed: Request closed with a resolution that names who paid — event-027 closed the request, but the resolution names no payer and the checks above were outstanding; office asked to decide on reopening (ACT-2)

## 1. Decision

The repair itself was properly authorised (landlord's own approval, event-012) and a provider was instructed (event-013/015), but the ticket was closed at event-027 with final checks outstanding: the only evidence of completion is the provider's untrusted email (event-019) whose invoice attachment is unavailable, documents were skipped "not needed" (event-023), no invoice was forwarded to the landlord, and the landlord confirmation flagged at event-024 was never obtained. I did not re-dispatch or duplicate the work order. Within mandate I chased Cedar Homes for the invoice, attendance date and photo (ACT-3), asked the tenant to confirm the handle is working (ACT-4), and told the landlord the position with no cost stated (ACT-5). The conflict between the agency's own records about who the tenant is (Harriet in event-005/event-007 vs Nora Quinn with two different numbers in event-014/015/016) was recorded and sent to the office rather than put to any party (ACT-1, ACT-2). The case now waits on three named parties, so it finishes as request_info rather than an escalation.

Safety actions taken first:
- Checked the report against the emergency definitions: no gas, electrical, water, heating or security hazard — the window cannot be opened, and the property is not reported insecure, so no make-safe step was due.
- Safety-pass keywords screened: no smoke/CO alarm, damp, mould, electrical or occupant-vulnerability content appears in any artefact of this case; no occupant health, age or family details were shared with the contractor.

Actions deliberately withheld:
- Did not re-dispatch or raise a second work order for the same fault (one report, one work order).
- Did not state or imply any cost, attendance date or who pays — no artefact gives them.
- Did not tell any party which tenant name or number is correct.
- Did not re-close the request: final checks are incomplete and reopening is the office's decision.

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-APPROVED, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, ESC-CONFLICT, PRO-TENANT-LIABILITY, PRO-PII, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 2025-01-13 that the window handle fell off and the window cannot be opened at Flat 21, 129 Juniper Mews, Northbridge, ZZ9 4ZZ. [index, event-001; high]
- F2: The window concerned is the one at the top of the staircase, described by the tenant as having a broken latch. [event-007; medium]
- F3: No hazard is reported anywhere in the artefacts: no gas, electrical, water, heating or security failure; the window cannot be opened rather than cannot be secured — routine urgency. [event-001, event-007; high]
- F4: The landlord approved the job in their own message on 2025-02-09: "Please go ahead" — authority for dispatch under CAP-DISPATCH-APPROVED; no spend cap or standing instruction is on file. [event-012; high]
- F5: Cedar Homes was assigned and briefed on 2025-02-09, and the tenant was told who was attending. [event-013, event-014, event-015, event-016; high]
- F6: No appointment slot was ever confirmed on the record; two reminders were sent to the provider (10 and 11 February) and an automation alert on 12 February reported 3+ reminders with no booking confirmation. [event-017, event-018, event-020; high]
- F7: Cedar Homes emailed on 2025-02-11 "This is complete, invoice attached"; the invoice attachment is unavailable, so no priced invoice, photo or attendance date is on file. [event-019; high]
- F8: Document upload was skipped with the reason "not needed"; landlord confirmation was flagged as needed but no landlord confirmation appears in the history; the request was nonetheless closed on 2025-02-14. [event-023, event-024, event-027; high]
- F9: A keys return was recorded as confirmed, although no artefact shows a management key was issued for this visit. [event-026; medium]
- F10: No quote amount was ever produced or put to the landlord; the provider brief states the contractor should only proceed after agency approval if a quote is required. [event-015; high]

Conflicts between sources:
- Agency records disagree about the tenant of Flat 21: agency email addresses "Harriet" and the reply is signed "Harriet", while the provider and tenant briefs name "Nora Quinn"; two different contact numbers are also given to the provider (07700 900307 and 07700 900251). → Not decided by me. Recorded and sent to the office (ACT-1, ACT-2); messages to parties avoid using either name. Routine steps continued meanwhile. (asked)
- Provider says the job was complete on 11 February, but the agency's own automation reported on 12 February that 3+ reminders had been sent with no booking confirmation, and no appointment was ever recorded. → Asked Cedar Homes for the attendance date and photo (ACT-3) and asked the tenant to confirm the handle works (ACT-4). (asked)

Red flags:
- [data_quality] Ticket closed with final checks outstanding: no invoice on file despite "invoice attached", documents skipped as "not needed", no invoice to landlord, no landlord confirmation, and a keys return confirmed with no key issued. → Recorded in the case note and handed to the property manager queue (ACT-1, ACT-2); chased the provider for the invoice (ACT-3).
- [data_quality] Two tenant names and two phone numbers for the same property across the agency's own records. → Conflict recorded; office asked to reconcile; no name used when writing to parties.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "044", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Review of closed ticket 044 (window handle, Flat 21, 129 Ju… | {"id": "ACT-1"} | CAP-LOG |
| 4 | create_human_task | completed | queue=property_manager, title=Case 044 closed with final checks outstanding + tenant-iden…, summary=Flat 21, 129 Juniper Mews — window handle. Two issues for t… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 5 | notify_contractor | completed | message=Cedar Homes — ref Window Repair Request, Flat 21, 129 Junip… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Re: window handle, Flat 21, 129 Juniper Mews — our contract… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | notify_landlord | completed | message=Re: Flat 21, 129 Juniper Mews — window handle repair you ap… | {"id": "ACT-5"} | CAP-NOTIFY |

## 4. Human handover / information requested

- Ask **contractor**: Please send the invoice for the Flat 21, 129 Juniper Mews window handle job (amount and VAT separately), the date and time you attended, and a photo of the fitted handle — the attachment referred to in your 11 February email did not arrive. (blocking; No invoice or work evidence is on file; the file cannot be completed and the landlord cannot be billed without it (event-019, event-023).)
- Ask **tenant**: Has the handle on the window at the top of the stairs been refitted, and does the window now open and close properly? (blocking; Completion rests only on the provider's untrusted email; the tenant's confirmation is the independent check (event-019).)
- Ask **landlord**: Once the invoice arrives we will forward it — please confirm you are content the job is complete and the cost is approved. (blocking; Landlord confirmation was flagged as required at event-024 and never obtained before closure at event-027 (RTE-LANDLORD).)
- Ask **property_manager**: Which name on our record is the tenant of Flat 21 — Harriet (event-005/007) or Nora Quinn (event-014/015/016) — and should the closed ticket be reopened for final checks? (non-blocking; Two agency records disagree about the tenant and the contact number; I must not pick a side in a message to a party (ESC-CONFLICT).)

Promises made or recorded:
- agency → contractor: Invoice, attendance date and photo requested; reply within 3 working days by 3 working days from ACT-3 [open]
- agency → landlord: Forward the invoice for confirmation as soon as it arrives [open]
- agency → tenant: Arrange a return visit if the handle was not repaired [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
