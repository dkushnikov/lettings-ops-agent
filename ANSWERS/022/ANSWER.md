# ANSWER — Case 022 — Case 022: Front Door Lock Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Lock repair reported done but closed with invoice, documents, provider result for this address and landlord confirmation all outstanding; chased all three parties and flagged the conflict.
**Stage:** on_hold · **Hold:** Waiting for Provider — job sheet and invoice for Flat 23, 155 Willowmere Road chased (ACT-1), reply-by 27/11/2024; also awaiting tenant confirmation of the repair and landlord confirmation of completion.
**Last update:** 2024-11-21 12:22:26 UTC (event-023) · **Decided:** 2026-10-10 14:05 UTC
**Next step:** Contractor to send the job sheet and invoice for Flat 23, 155 Willowmere Road by 27/11/2024 (ACT-1); property manager to resolve the Harbour View/Willowmere result conflict and the missing landlord authority (ACT-4).

Definition of done (3/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 categorised as lock repair; urgency routine (lock still opens, property secure); tenant contacted same day event-004/event-008
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No landlord message in the history (search_history, sender Landlord: no results); no standing cap on file; event-002 is a system status line, not an approval. Landlord informed and referred to proper…
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003 provider assigned; event-007 provider briefed; event-008 tenant told who is coming
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-004 tenant agreed; event-006 visit date confirmed 17/11/2024 14:30; event-011 attendance 18/11/2024
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote or amount exists on the ticket; work was carried out without a priced quote or landlord approval (RTE-LANDLORD) — flagged in ACT-3, ACT-4
- [ ] work_result: Work result recorded from the provider — event-012 no work results; event-013 result call relates to a different property; agency notes event-016/event-020 are second-hand. Provider chased ACT-1, tenant asked ACT-2.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-021 upload skipped with reason "job complete" — reason recorded but no job sheet or invoice for this address; requested in ACT-1
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-016 invoice still to be sent by provider; nothing received, so nothing forwarded (ACT-1, ACT-3)
- [ ] landlord_confirmation: Landlord confirmed completion — event-022 "Need confirmation from landlord"; no landlord reply exists; asked in ACT-3
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued for the visit; a new key was delivered into the agency key set on 21/11/2024 (event-020)
- [ ] closed: Request closed with a resolution that names who paid — event-023 closed the request while items above were open; closure not valid, reopening referred to property manager (ACT-4)

## 1. Decision

The ticket was closed (event-023) with final checks still open: no provider work result for this address, no invoice, document upload skipped, landlord confirmation outstanding (events 016, 021, 022), and no landlord approval or standing spend cap anywhere in the history. I did not re-close or re-dispatch. I kept the routine, reversible steps running — chased the provider for a job sheet and invoice for this address with a reply-by date (ACT-1), asked the tenant to confirm the lock now works and the new key was received (ACT-2), told the landlord the status, the missing authority and that the invoice will be forwarded for confirmation (ACT-3) — recorded the records conflict and referred it to the property manager (ACT-4, ACT-5), and put the case on hold to 27/11/2024 (ACT-6). The case now waits on named parties, so it ends as request_info.

Safety actions taken first:
- Checked the report against the emergency definitions: the lock is stiff but the door opens and locks and the property is not insecure (event-001), so not an insecure-property emergency; tenant told to report immediately if the door cannot be locked or secured (ACT-2).
- Safety-pass keyword check: no gas, electrical, damp/mould, detector, injury or vulnerability content appears in the artefacts of this case; no hazard reported or observed.

Actions deliberately withheld:
- Did not re-close the request: final checks (work result, documents, invoice, landlord confirmation) are still open (CAP-CLOSE).
- Did not instruct any further contractor work: no landlord approval and no standing cap on file (APR-SPEND-OVER-CAP).
- Did not state or approve any cost, and did not decide who pays (PRO-PAYMENTS, PRO-TENANT-LIABILITY).
- Did not tell any party which of the conflicting agency records is correct (rule 2).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, ESC-CONFLICT, PRO-TENANT-LIABILITY, PRO-PAYMENTS, CAP-CLOSE, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 17/11/2024 that the front door lock at Flat 23, 155 Willowmere Road is very hard to turn to unlock, taking a couple of minutes to open; the door still opens and the property is not insecure. [index, event-001; high]
- F2: A maintenance provider was assigned the same day and an appointment was confirmed with the tenant for 17/11/2024; confirmation emails went to provider (named Oliver Sawyer) and tenant Amelia Oakley. [event-003, event-004, event-006, event-007, event-008; high]
- F3: The provider called the tenant on 18/11/2024 saying they were en route with two locks in the van; the tenant confirmed they would be in. [event-011; medium]
- F4: On 19/11/2024 the agency recorded that no work results had been received. [event-012; high]
- F5: The 20/11/2024 status call with the provider discusses completed work including a lock change at Flat 22, 42 Harbour View, Alderwick, ZZ3 3ZZ, and keys for Flat 18, 68 Harbour View, Eastmere — not this property; the ticket was moved to Result and marked completed immediately after that call. [event-013, event-014, event-015; high]
- F6: Agency notes record the repair as done by "Maya", with a new key brought to the office on 21/11/2024 and copied; the invoice was still to come. [event-016, event-020; medium]
- F7: Document upload was skipped with the reason "job complete"; the system then recorded "Need confirmation from landlord" and one minute later closed the request as all checks completed. [event-021, event-022, event-023; high]
- F8: No message from the landlord appears anywhere in the visible history (history search by sender Landlord returned no results), so there is no landlord approval and no standing spend cap on file; the job's cost is unknown. [search_history, event-002; high]
- F9: No key issued to the agency for access is recorded; instead a new key was delivered into the agency's key set on 21/11/2024. [event-020; medium]

Conflicts between sources:
- The work result for this ticket was recorded from a provider call about a different property (Flat 22, 42 Harbour View, ZZ3 3ZZ), while the ticket is for Flat 23, 155 Willowmere Road; no provider result exists for this address. → Not resolved by me: conflict recorded and referred to the property manager (ACT-4); provider asked for a job sheet for this address (ACT-1); tenant asked to confirm the repair (ACT-2). No party was told which version is correct. (asked)
- Provider identity inconsistent across agency records: instructed provider is named Oliver Sawyer in the appointment emails, but internal notes refer to "Maya". → Referred to the property manager (ACT-4); no name copied into another party's letter. (asked)
- The system closed the request as "all checks completed" one minute after recording that landlord confirmation was still needed, with no invoice received and documents skipped. → Premature closure flagged to the property manager to decide on reopening (ACT-4); final checks restarted with the three parties. (asked)

Red flags:
- [data_quality] Work result and closure for this ticket rest on a provider call about a different property (Flat 22, 42 Harbour View) and on notes naming a provider ("Maya") different from the instructed provider (Oliver Sawyer). → Conflict recorded and referred to property_manager (ACT-4); provider asked for a job sheet for this address (ACT-1); no party told which version is correct.
- [data_quality] Spend incurred with no landlord approval and no standing cap on file; closure recorded as "all checks completed" with invoice, documents and landlord confirmation outstanding. → Landlord informed (ACT-3); referred to property_manager (ACT-4); no payment actioned (PRO-PAYMENTS).
- [other] Two events show the agency's automation stopping: a provider reply needing a human response (event-017/event-018) and an untranscribable message (event-019). → Handled in manual mode: provider chased with a specific request and reply-by date (ACT-1).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "022", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [] | allow |
| 4 | search_history | completed | query=invoice | [{"event": "event-016", "timestamp": "2024-11-20 16:33:31 UTC", "channel": "Hold", "from": "Northbridge Lettings", "to": "Not specified", "excerpt": "[2024-11-… | allow |
| 5 | notify_contractor | completed | message=Re: Lock Repair Request – Flat 23, 155 Willowmere Road, Ald… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Dear Amelia Oakley,  About your front door lock at Flat 23,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_landlord | completed | message=Flat 23, 155 Willowmere Road, Alderwick, ZZ5 2ZZ – front do… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | create_human_task | completed | queue=property_manager, title=Case 022 closed with final checks outstanding + work result…, summary=Flat 23, 155 Willowmere Road, Alderwick, ZZ5 2ZZ – front do… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 9 | add_note | completed | note=Case 022 reviewed after closure (event-023). Final checks w… | {"id": "ACT-5"} | CAP-LOG |
| 10 | put_on_hold | completed | reason=Waiting for Provider — job sheet/work result and invoice fo…, until=2024-11-27 | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Please send the job sheet/work result and your invoice for the front door lock job at Flat 23, 155 Willowmere Road, Alderwick, ZZ5 2ZZ, stating what was carried out and on what date. Reply by 27/11/2024. (blocking; No provider work result or invoice exists for this address; the only status call on file (event-013) concerns a different property.)
- Ask **tenant**: Is the front door lock now opening and locking normally, and did you receive the new key(s)? (blocking; Tenant-owned fact; the repair result for this address is not evidenced by the provider.)
- Ask **landlord**: Please confirm completion of the lock repair once we forward the contractor's invoice, and tell us whether you want the job reviewed before the invoice is approved. (blocking; Landlord confirmation was still outstanding at closure (event-022) and no approval or spend cap is on file (RTE-LANDLORD).)

Promises made or recorded:
- agency → contractor: Chase again and refer to the property manager if no job sheet/invoice by 27/11/2024 by 2024-11-27 [open]
- agency → landlord: Forward the contractor's invoice as soon as it arrives, for confirmation before anything is settled [open]
- agency → tenant: Treat it as urgent if the lock is still stiff or the door cannot be secured [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
