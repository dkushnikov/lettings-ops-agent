# ANSWER — Case 021 — Case 021: Key Replacement Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Lock replaced and reported complete, but the ticket was closed with no invoice, no landlord confirmation and an unevidenced key return; all three chased.
**Stage:** final_checks · **Hold:** Waiting for Provider — Alder Compliance to supply the invoice (net + VAT) and confirm the office/landlord key handover, reply due 2 working days; landlord confirmation of completion also outstanding (3-day wait).
**Last update:** 2024-11-23 04:22:42 UTC (event-029) · **Decided:** 2026-10-10 13:25 UTC
**Next step:** Alder Compliance to send the invoice (net + VAT) and confirm the date the office and landlord key sets were handed in (2 working days); office to check the key log.

Definition of done (5/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-003: snapped conservatory back door key, no spare; categorised routine, no hazard present
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 — landlord's own email approving the works and key sets
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010/event-012 provider briefed; event-011 tenant told Alder Compliance would attend
- [-] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot was ever confirmed (event-018 chase); superseded by the provider reporting attendance and completion at event-020
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-025 — 'No quote required, repaired on site'
- [x] work_result: Work result recorded from the provider — event-020 — provider reports cylinder and handles replaced; tenant verification requested (ACT-3)
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-025 — skip reason recorded: no quote required, repaired on site
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice or cost anywhere on file (search_history); provider chased (ACT-2), landlord told it will follow (ACT-4)
- [ ] landlord_confirmation: Landlord confirmed completion — event-026 flagged the need; no landlord reply before closure (event-029); confirmation requested (ACT-4)
- [ ] keys_returned: Keys returned, where a management key was issued for the visit — event-028 flag unsupported; only the provider's promise at event-020; handover date requested (ACT-2) and office key log check raised (ACT-5)
- [ ] closed: Request closed with a resolution that names who paid — event-029 closed the request, but the resolution names no payer and three items above are outstanding; treated as final_checks

## 1. Decision

The job itself is done and authorised, but the automation closed the ticket (event-029) with three definition-of-done items unevidenced: no invoice or cost on file, no landlord confirmation of completion, and a "Keys return confirmed" flag (event-028) backed only by the provider's promise to deliver the keys the next day (event-020). I did not re-close or re-dispatch. I logged the gap, chased the provider for the invoice and a key-handover confirmation, asked the landlord to confirm completion, asked the tenant to confirm the door locks and how many keys were left, and sent the premature-closure/key-log conflict to the office queue. The case now waits on named parties, so it finishes as request_info rather than an escalation.

Safety actions taken first:
- Safety-pass sweep of all artefacts: no smoke/CO alarm, gas, electrical, damp/mould, asbestos, injury or vulnerable-occupant content appears in this case; no safety item left unaddressed.
- Confirmed the report does not meet the 'property not secure' emergency definition — the snapped key affects an internal conservatory back door and no party reports the property insecure (event-001, event-003).

Actions deliberately withheld:
- Did not re-close the request: invoice, landlord confirmation and key-return evidence are all outstanding (CAP-CLOSE).
- Did not re-dispatch or duplicate the work order — the job is reported complete (event-020).
- Did not state or allocate any cost, and did not decide whether the snapped key is tenant-chargeable (PRO-TENANT-LIABILITY).
- Did not escalate: no safety, legal or liability decision arises; the case waits on named parties.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, ESC-CONFLICT, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 22, 148 Lantern Quay, Westmarsh, ZZ4 1ZZ; tenant on the brief is Clara Jenkins. [index, get_case_details, event-011; high]
- F2: Fault reported 21/11/2024: key snapped in the conservatory back door; no spare held by the tenant or the agency. Scope: replace the lock and supply 4 keys (2 tenant, 1 office, 1 landlord). [event-001, event-003, index; high]
- F3: Landlord's own email approves the works and the new key sets. [event-006; high]
- F4: Provider Alder Compliance was assigned and briefed; tenant was told who would attend. [event-010, event-011, event-012; high]
- F5: No visit slot was ever confirmed in the history; the provider went from acknowledging the chase to reporting the job complete. [event-018, event-020; high]
- F6: Provider reported the job complete — cylinder and handles replaced — and said remaining keys would be dropped to the office the next day. [event-020; medium]
- F7: No quote, cost figure or invoice appears anywhere in the case; documents were skipped with reason 'No quote required, repaired on site'. [event-025, search_history; high]
- F8: System flagged 'Need confirmation from landlord' (event-026); no landlord reply follows before the request was closed at event-029. [event-026, event-029; high]
- F9: 'Keys return confirmed' was recorded at event-028 with no delivery receipt, 16 minutes of system time after the skip note and the day after the provider's promise. [event-028, event-020; high]
- F10: Nothing in the case matches an emergency definition: the fault is a snapped key to a conservatory back door, the property is not reported insecure, and no hazard, vulnerability or essential-service loss is mentioned. [event-001, event-003; medium]

Conflicts between sources:
- Agency records disagree on whether the office and landlord key sets have been returned: event-028 states 'Keys return confirmed' while the only underlying evidence is the provider's promise at event-020 to deliver them 'tomorrow'. → Provider asked for the handover date; office asked to check the key log (ACT-2, ACT-5). Not asserted either way to any party. (asked)
- Tenant contact number differs between agency messages: 07700 900625 in the brief and reminder, 07700 900336 in the number sent to the provider. → Recorded and sent to the office queue (ACT-5); no number repeated to any party. (unresolved)

Red flags:
- [data_quality] Request closed as 'All checks have been completed' while invoice, landlord confirmation and key-return evidence were all missing; closure note names no payer. → Logged internally (ACT-1) and sent to the property_manager queue (ACT-5); ticket treated as still at final_checks.
- [data_quality] Agency emails to the provider are addressed 'Hi Clara' / 'Good morning Clara' — Clara Jenkins is the tenant, not the provider; names in message bodies are unreliable. → Parties addressed only by the names on the case record; discrepancy flagged to the office (ACT-5).
- [other] Landlord approval at event-006 is a third-person summary ('Quinn approves the maintenance action'), not a first-person reply, and carries no price. → Accepted as the landlord's own message for the job in principle (RTE-LANDLORD); the invoice amount will still be put to the landlord when it arrives.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "021", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice cost quote payment | [] | allow |
| 4 | get_attachment | completed | name=attachment-85-document | {"error": "no attachment named attachment-85-document"} | allow |
| 5 | add_note | completed | note=Final-checks audit. Provider Alder Compliance reported job… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_contractor | completed | message=Re: Key Replacement Request — Flat 22, 148 Lantern Quay, We… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Dear Ms Jenkins,  Our provider Alder Compliance has reporte… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_landlord | completed | message=Address: Flat 22, 148 Lantern Quay, Westmarsh, ZZ4 1ZZ  Dea… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | create_human_task | completed | queue=property_manager, title=Case 021 closed with final checks outstanding — verify key…, summary=The system closed this request at event-029 ("All checks ha… | {"id": "ACT-5"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **contractor**: Please send your invoice for the Flat 22, 148 Lantern Quay lock replacement with net amount and VAT shown separately, and confirm the date the remaining keys (1 office, 1 landlord) were delivered to our office plus how many keys were left with the tenant. (blocking; No cost figure or invoice exists anywhere on file and the key return flag (event-028) has no delivery evidence beyond the provider's promise in event-020.)
- Ask **landlord**: Quinn: please confirm you are content that the conservatory back door lock replacement is complete; the invoice will follow as soon as the provider sends it. (blocking; Event-026 flagged 'Need confirmation from landlord' and no landlord reply followed before closure at event-029.)
- Ask **tenant**: Ms Jenkins: does the new lock operate correctly, and how many keys were left with you on the visit? (non-blocking; Independent verification of the provider's completion claim (event-020) and of the 2-key allocation in the brief (event-012).)

Promises made or recorded:
- agency → landlord: Forward the provider's invoice as soon as it arrives [open]
- agency → contractor: Chase again and report the job as unverified if no invoice/key confirmation within 2 working days [open]
- agency → tenant: Send the provider back if the new lock is not working correctly [open]
- contractor → agency: Drop remaining keys to the office the day after completion by 2024-11-23 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-SOP-ACK [sop]: Landlord confirmation wait (3 days)
