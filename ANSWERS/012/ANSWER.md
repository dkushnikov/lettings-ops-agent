# ANSWER — Case 012 — Case 012: Dishwasher Door Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Dishwasher door repaired on 29/04; ticket closed early — chased landlord confirmation and the provider's invoice, flagged provider-identity conflict to the office.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation of completion and of the prior approval relied on in event-008/event-012 (3 working days); in parallel Waiting for Provider for the priced invoice.
**Last update:** 2026-05-03 15:05:04 UTC (event-031) · **Decided:** 2026-10-10 13:22 UTC
**Next step:** Landlord to confirm completion and prior approval (asked ACT-1, 3 working days); provider to send the priced invoice (asked ACT-2).

Definition of done (5/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged; troubleshooting/damage-limiting checks sent to tenant event-005/event-006; tenant confirmed checks done and fault persists event-011
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Only internal notes assert approval (event-008, event-012); search_history for Landlord returned no landlord message. Confirmation requested ACT-1
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Riverside Compliance instructed event-013/event-015; tenant briefed event-014
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Slot agreed on call event-016; confirmed to provider event-018 and tenant event-019; attendance 29/04 event-021
- [-] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted; the provider carried out the repair at the first visit (event-024). The brief required approval before proceeding (event-015) — flagged to the office ACT-5
- [x] work_result: Work result recorded from the provider — event-024: door lock engaging prematurely, lock repaired, appliance tested working; event-025
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — Skip reason recorded: 'not needed' (event-027)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice amount on file and no evidence of forwarding; invoice chased from provider ACT-2 and landlord told it will follow ACT-1
- [ ] landlord_confirmation: Landlord confirmed completion — event-028 'Need confirmation from landlord' never satisfied before closure; requested ACT-1
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — event-030 records keys return confirmed; no management key issued is evidenced — tenant provided access
- [ ] closed: Request closed with a resolution that names who paid — event-031 closed the request, but the resolution names no payer and items above remain pending; not re-closed by me

## 1. Decision

The repair itself is done (door lock repaired and appliance tested, event-024), but the ticket was closed at event-031 with final checks incomplete: no landlord confirmation (event-028 unresolved), no priced invoice on file and none forwarded, and no landlord message anywhere evidencing approval for the spend. I did not re-close or re-dispatch. I asked the landlord to confirm completion and the prior approval, chased the instructed provider (Riverside Compliance, the firm on the agency's own record) for the priced invoice and written confirmation of who attended, told the tenant the outcome, logged the conflicts, and routed the provider-identity conflict and the premature closure to the property manager queue (ACT-5). The case now waits on the landlord and the provider; who pays is not decided here (PRO-TENANT-LIABILITY).

Safety actions taken first:
- Checked the report and the work result against the emergency definitions: appliance door latch only, no gas, electrical, water, heating or security element (event-001, event-024) — no make-safe step required.
- Checked for occupant vulnerability indicators in the history: none recorded.

Actions deliberately withheld:
- Did not re-close the request: landlord confirmation and the invoice remain outstanding (CAP-CLOSE).
- Did not dispatch or re-instruct any contractor: the work is already done and there is no landlord approval event to cite (CAP-DISPATCH-APPROVED, APR-SPEND-OVER-CAP).
- Did not state or apportion the cost, and did not decide whether the repair is tenant-payable (PRO-TENANT-LIABILITY).
- Did not name one firm as the attending contractor to any party while the agency records conflict.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CAP-CLOSE, APR-SPEND-OVER-CAP, ESC-CONFLICT
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Fault reported 15/04/2026: dishwasher door not closing at Flat 9, 89 Juniper Mews, Willowbank, ZZ2 0ZZ. [index, event-001, get_case_details; high]
- F2: Agency sent the tenant seven damage-limiting checks on 19/04/2026 (sent twice, duplicate). [event-005, event-006; high]
- F3: Tenant replied 23/04/2026 'All checks done, door still doesn't close' (quoted, untrusted). [event-011; high]
- F4: Riverside Compliance was instructed as the maintenance provider on 25/04/2026 and briefed to quote before proceeding. [event-013, event-015; high]
- F5: Visit confirmed for 29/04/2026 08:00-12:00 with the tenant and the provider. [event-016, event-017, event-018, event-019; high]
- F6: Work result: door lock had engaged prematurely; lock repaired and appliance tested working (recorded 03/05/2026). [event-024; high]
- F7: No message from the landlord appears anywhere in the visible history; approval is asserted only in internal agency notes. [event-008, event-012, search_history; high]
- F8: No invoice amount, VAT or payer is recorded anywhere in the case. [event-024, event-027, search_history; high]
- F9: No emergency definition is matched: an appliance fault with no gas, electrical, water, heating or security element. [event-001, event-024; high]

Conflicts between sources:
- Who holds/attended the job: agency records name Riverside Compliance as the instructed provider, while the scheduling call names 'Cedar Utilities', the arrival call names 'Meadow Services', and the agency's own SMS signs off 'Harbour Homes'. → Not resolved in a message to any party. Conflict logged (ACT-4) and routed to the property manager queue (ACT-5); meanwhile the invoice/attendance confirmation was chased from the provider on the agency's own record, Riverside Compliance (ACT-2). (asked)
- Tenant name inconsistency: tenancy record and agency letters name Leo Turner; the scheduling call transcript calls him 'Leo Kendall' (the surname of the property manager named in event-012). → Agency record name Leo Turner used; transcript name not copied into any letter. (source_hierarchy)
- Ticket was closed as 'all checks completed' while landlord confirmation was still flagged as needed. → Raised with the property manager (ACT-5); landlord confirmation requested (ACT-1). (asked)

Red flags:
- [data_quality] Original request referenced an email 'dated 16th Sept 2025' and an internal note records the tenant's 'door won't close' reply arrived on an unrelated sink thread, so the fault history may be conflated; the agency also sent the troubleshooting email twice. → Logged; the tenant's 23/04 reply (event-011) on this ticket was treated as answering this ticket's own question.
- [data_quality] Three different contractor firm names appear against one instructed provider, and the agency SMS brands itself 'Harbour Homes'. Identity of the attending firm and the invoicing party is unverified. → Conflict logged (ACT-4) and sent to the property manager queue (ACT-5); written confirmation requested from Riverside Compliance (ACT-2).
- [other] Internal note 'LL already agreed for GS to go out' uses ambiguous initials; if 'GS' was meant as Gas Safe engineer the trade recorded for this appliance job would be wrong. No gas element appears in the fault or the work result. → Flagged for clarification in the human task (ACT-5); no gas hazard identified, so no emergency action taken.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "012", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [] | allow |
| 4 | search_history | completed | query=invoice | [{"event": "event-024", "timestamp": "2026-05-03 15:03:16 UTC", "channel": "Note", "from": "Agency / system", "to": "Not specified", "excerpt": "[2026-05-03 15… | allow |
| 5 | search_history | completed | query=approval | [{"event": "event-015", "timestamp": "2026-04-25 13:32:05 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Contractor", "excerpt": "[2026-04-25… | allow |
| 6 | notify_landlord | completed | message=Flat 9, 89 Juniper Mews, Willowbank, ZZ2 0ZZ — dishwasher d… | {"id": "ACT-1"} | CAP-NOTIFY |
| 7 | notify_contractor | completed | message=Riverside Compliance — Dishwasher Repair Request, Flat 9, 8… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | notify_tenant | completed | message=Dear Leo Turner,  Flat 9, 89 Juniper Mews, Willowbank, ZZ2… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | add_note | completed | note=Review of closed ticket. Work result on file (event-024). C… | {"id": "ACT-4"} | CAP-LOG |
| 10 | create_human_task | completed | queue=property_manager, title=Flat 9, 89 Juniper Mews — closed dishwasher job: provider i…, summary=Ticket was closed on 03/05/2026 (event-031) with checks sti… | {"id": "ACT-5"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the dishwasher repair at Flat 9, 89 Juniper Mews is complete to your satisfaction, and that you had approved an engineer attending (as our internal note of 19/04 records)? (blocking; RTE-LANDLORD: landlord confirmation is a required final check (event-028) and no landlord message exists in the ticket.)
- Ask **contractor**: Please send the priced invoice (net, VAT, total) for the 29/04/2026 dishwasher visit at Flat 9, 89 Juniper Mews, and confirm in writing which company and engineer attended. (blocking; RTE-CONTRACTOR: no invoice amount is on file, so it cannot be forwarded to the landlord; agency records name different firms.)

Promises made or recorded:
- agency → landlord: Forward the priced invoice once the provider supplies it [open]
- landlord → agency: Confirm completion and the prior approval by 3 working days from ACT-1 [open]
- contractor → agency: Send priced invoice and written confirmation of who attended by 3 working days from ACT-2 [open]
- agency → tenant: Reopen the job if the door still does not close [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
