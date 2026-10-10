# ANSWER — Case 002 — Case 002: Blocked toilet at Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Blocked toilet replaced and invoiced; I chased the landlord's completion confirmation and invoice acknowledgement, flagged the status/provider-name conflicts, and held the case.
**Stage:** on_hold · **Hold:** Waiting for Landlord — completion confirmation and acknowledgement of the invoice requested 2026-08-21 (ACT-1); 3 working days, i.e. by 2026-08-26.
**Last update:** 2026-08-21 10:32:59 UTC (event-049) · **Decided:** 2026-10-10 13:59 UTC
**Next step:** Landlord (Quinn) to confirm the works are complete and acknowledge the invoice by 2026-08-26; if no reply, property manager picks up the file (ACT-4).

Definition of done (7/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (fault logged: toilet to be removed to clear blockage at pan connector); routine — no emergency indicator in any artefact
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-019 — landlord's own email approving the quoted works (event-003/event-002 system lines are not approvals)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-004, event-008 (Riverside Works briefed), event-007 (tenant told who is coming)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-027/event-028/event-029 — 15/08/2026 08:30 confirmed with tenant and provider
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-017 quote sent, event-019 landlord approved before works; amount and VAT not visible — quote attachment unavailable
- [x] work_result: Work result recorded from the provider — event-034 — provider reported completion with photo on 19/08/2026
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-038 skip reason 'Not required' recorded; invoice document added at event-048 (content unavailable in file)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No event shows the invoice forwarded; chased with the landlord at ACT-1
- [ ] landlord_confirmation: Landlord confirmed completion — event-039 'Need confirmation from landlord'; no landlord message after event-019 — requested at ACT-1
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant-arranged access throughout (event-011, event-028)
- [ ] closed: Request closed with a resolution that names who paid — event-040 and event-049 show system/supervisor closure, but final checks above are incomplete and the status is itself in conflict (event-043, event-045, event-044); I did not close

## 1. Decision

Work is reported complete and the invoice is on file, but two final checks are outstanding: the invoice was never evidenced as sent to the landlord and the landlord has never confirmed completion (event-039 raised it; no landlord message after event-019). I did not close the request. I chased the landlord for both (ACT-1, 3 working-day window), told the tenant the work is reported complete and asked them to report any defect (ACT-2), logged the record gaps (ACT-3), raised a human task answering the office's unanswered dashboard/status question at event-044 and asking a person to verify the invoice is from the instructed provider before any payment (ACT-4), and placed the request on hold Waiting for Landlord (ACT-5). No spend authorised and no payment made (PRO-PAYMENTS); no liability decided (PRO-TENANT-LIABILITY).

Safety actions taken first:
- Safety-pass check: no gas, electrical, damp/mould, alarm or occupant-vulnerability keyword appears in any artefact; no sewage backing up or overflow reported, so the blocked toilet stayed routine rather than emergency (event-001, event-016, event-034).
- Tenant advised to report any leak, smell or overflow immediately and told that overflow/backing up is an emergency (ACT-2).

Actions deliberately withheld:
- Did not close the request: invoice_to_landlord and landlord_confirmation are outstanding (CAP-CLOSE).
- Did not state or approve any payment or who pays (PRO-PAYMENTS, PRO-TENANT-LIABILITY).
- Did not re-dispatch or duplicate the work order; the provider has reported completion.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, CAP-CLOSE, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Fault: toilet to be removed to clear a blockage lodged by the pan connector at Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ, logged 2026-08-07. [index, event-001; high]
- F2: Riverside Works was the provider instructed and briefed by the agency. [event-004, event-008, event-024, event-028; high]
- F3: First visit found the toilet needed repiping with a risk of damage on removal; a quote for a new toilet and cistern was supplied (amount not visible — attachment unavailable). [event-016, event-017; medium]
- F4: The landlord approved the quote in their own email of 2026-08-12. [event-019; high]
- F5: Works were booked for 15/08/2026 08:30 and the provider reported completion on 2026-08-19 with a photo and invoice. [event-027, event-029, event-034; high]
- F6: An invoice document was added to the file on 2026-08-21; its content and amount are unavailable. [event-048; high]
- F7: No landlord message confirming completion exists after event-019, although event-039 recorded that confirmation was needed. [event-039, search_history; high]

Conflicts between sources:
- Untrusted call transcript names 'Willow Utilities' as the party attending, while the agency record throughout names Riverside Works. → Ticket/agency record outranks a call transcript: Riverside Works holds the job. Flagged for a human to check the invoice issuer before payment (ACT-4). (source_hierarchy)
- Request status is recorded as closed (event-040) and completed by supervisor (event-049), yet also auto-paused for a missed deadline (event-043) and held for 'system issues' (event-045), and staff report it keeps reappearing on the dashboard (event-044). → Referred to the property manager queue (ACT-4); I did not pick a status in any message to a party. (asked)
- Two different tenant contact numbers were issued to the provider (07700 900422 and 07700 900946). → Logged (ACT-3); did not affect access, as both visits were arranged. (unresolved)

Red flags:
- [data_quality] Untrusted transcript names a different firm ('Willow Utilities') from the instructed provider Riverside Works; invoice and quote attachments are unavailable; duplicate/contradictory closure states on the ticket. → Logged (ACT-3) and referred to the property manager for verification before payment (ACT-4).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "002", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice | [{"event": "event-024", "timestamp": "2026-08-13 04:52:16 UTC", "channel": "Email", "from": "Agency / system", "to": "Contractor", "excerpt": "[2026-08-13 04:5… | allow |
| 4 | search_history | completed | from_party=Landlord | [{"event": "event-019", "timestamp": "2026-08-12 09:22:12 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2026-08-12 09:22:… | allow |
| 5 | get_attachment | completed | name=invoice | {"error": "no attachment named invoice"} | allow |
| 6 | notify_landlord | completed | message=Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ — Blocked to… | {"id": "ACT-1"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Dear Noah Turner,  Flat 3, 15 Willowmere Road, Alderwick, Z… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | add_note | completed | note=Final-checks review. Work result recorded (event-034, 19/08… | {"id": "ACT-3"} | CAP-LOG |
| 9 | create_human_task | completed | queue=property_manager, title=Willowmere Rd Flat 3 blocked toilet: status conflict + prov…, summary=Answer to the office question at event-044 (job shows close… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 10 | put_on_hold | completed | reason=Waiting for Landlord, until=2026-08-26 (3 working days from the request sent 2026-08-21) | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Please confirm you are happy that the blocked-toilet works at Flat 3, 15 Willowmere Road are complete, and confirm receipt of Riverside Works' invoice now on the request file, so we can close the request. (blocking; landlord_confirmation and invoice_to_landlord are the only outstanding definition-of-done items; RTE-LANDLORD owns both.)
- Ask **tenant**: Is the new toilet flushing and draining properly with no leak or smell since the visit on 15 August 2026? (non-blocking; Confirms the provider's reported work result from the occupant's side before closure; non-blocking.)
- Ask **property_manager**: Which status is correct (closed at event-040 vs paused/held at event-043/045 vs completed by supervisor at event-049), and is the invoice at event-048 from Riverside Works and matching the approved quote? (non-blocking; Answers the unanswered office question at event-044 and protects payment; raised as a human task (ACT-4).)

Promises made or recorded:
- agency → landlord: If no reply on completion confirmation/invoice within 3 working days, the file goes to the property manager rather than being closed. by 2026-08-26 [open]
- agency → tenant: Arrange a return visit if the tenant reports the toilet is not working properly, and treat any overflow/backing up as an emergency. [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
