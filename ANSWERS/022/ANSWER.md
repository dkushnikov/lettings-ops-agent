# ANSWER — Case 022 — Case 022: Front Door Lock Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Lock repair marked closed without a verified work result, invoice or landlord confirmation; provider and tenant chased, conflict over the property referred to the office.
**Stage:** on_hold · **Hold:** Waiting for Provider — written job result and itemised invoice for Flat 23, 155 Willowmere Road, due close of business on the second working day after ACT-3; tenant confirmation also outstanding.
**Last update:** 2024-11-21 12:22:26 UTC (event-023) · **Decided:** 2026-10-10 13:25 UTC
**Next step:** Contractor (Oliver Sawyer, per event-007) to send the job result and itemised invoice for Flat 23, 155 Willowmere Road quoting the job ID, by close of business on the second working day (ACT-3); property manager to resolve the property/provider-identity conflict (ACT-2).

Definition of done (3/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged and categorised as a lock repair; urgency routine — door still locks/unlocks (index); tenant advised not to force the key (ACT-4)
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No landlord message in the visible history: no cap and no approval on file (F8); referred to the office (ACT-2) — APR-SPEND-OVER-CAP
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003; provider and tenant briefed at event-007 and event-008
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-004 tenant agreed; event-006 slot confirmed 17/11/2024 14:30; provider en route 18/11 (event-011)
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote or amount exists anywhere in the history; a lock change (event-013/event-016) was never priced or approved by the landlord
- [ ] work_result: Work result recorded from the provider — Only completion record (event-013) names a different property; provider chased for a written result for this address (ACT-3)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-021 skipped with reason 'job complete' — no photos or invoice; re-requested at ACT-3
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Invoice never received (event-016 promised it); nothing forwarded to the landlord
- [ ] landlord_confirmation: Landlord confirmed completion — event-022 'Need confirmation from landlord' — never obtained before closure at event-023
- [ ] keys_returned: Keys returned, where a management key was issued for the visit — New key taken into agency key management (event-020); not confirmed whether the tenant holds a working set — asked at ACT-4
- [ ] closed: Request closed with a resolution that names who paid — event-023 marked closed, but the resolution names no work result, no amount and no payer; ticket placed back on hold (ACT-5)

## 1. Decision

Reopened the final-checks stage: the ticket was marked closed (event-023) with documents skipped (event-021) and landlord confirmation still outstanding (event-022), and the only completion evidence on file (event-013) describes work at a different property. I did not confirm completion to anyone, did not re-dispatch, and did not approach the landlord for retrospective approval of an unquoted lock change. I chased the provider in writing for the job result and invoice for this address (ACT-3), asked the tenant to confirm the lock now operates and that she holds working keys (ACT-4), recorded the records conflict (ACT-1), raised an office task for the conflict and the premature closure (ACT-2) and placed the ticket on hold pending the provider (ACT-5).

Actions deliberately withheld:
- Did not close the request or confirm completion — work result, documents, invoice and landlord confirmation are all unverified (CAP-CLOSE).
- Did not re-dispatch a contractor: no landlord cap or approval on file and completion status unknown (APR-SPEND-OVER-CAP, no duplicate work order per playbook step 3).
- Did not tell the tenant or landlord which property record is correct (rule 2: conflict referred to the office instead).
- Did not seek or approve payment of an invoice that does not exist (PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, ESC-CONFLICT, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the front door lock key being very hard to turn to unlock, taking minutes to open; door still operates, so no loss of security. [index, event-001; high]
- F2: Case property is Flat 23, 155 Willowmere Road, Alderwick, ZZ5 2ZZ; tenant on record is Amelia Oakley. [index, get_case_details, event-008; high]
- F3: A provider was assigned and an appointment confirmed for 17/11/2024; booking emails name the provider as Oliver Sawyer. [event-003, event-006, event-007, event-008; high]
- F4: Provider called the tenant on 18/11 saying he was en route with two locks in the van. [event-011; medium]
- F5: The only 'work completed' call record (20/11) concerns Flat 22, 42 Harbour View, Alderwick ZZ3 3ZZ (two tasks incl. a lock change) and mentions keys for Flat 18, 68 Harbour View, Eastmere ZZ7 9ZZ — neither is the case property. [event-013; high]
- F6: Internal notes attribute the repair and a new key to this ticket and name the operative 'Maya'. [event-005, event-016, event-020; medium]
- F7: Document upload was skipped with the reason 'job complete'; landlord confirmation was flagged as still needed; the request was nevertheless marked closed minutes later. [event-021, event-022, event-023; high]
- F8: No landlord message appears anywhere in the visible history: no spend cap on file and no approval for the job or for a lock replacement. [search_history, event-001, event-023; high]
- F9: No invoice has been received or forwarded to the landlord for this job. [event-016, event-021; medium]

Conflicts between sources:
- Agency records disagree about which property the completed work belongs to: event-013 reports completion (incl. a lock change) at Flat 22, 42 Harbour View, Alderwick ZZ3 3ZZ, while event-014/015/016/020 treat the work as done on this ticket for Flat 23, 155 Willowmere Road. → Not decided by me; office task raised (ACT-2) and the provider asked to confirm in writing which address was worked on (ACT-3). No party was told which version is correct. (asked)
- Provider identity differs: booking emails name Oliver Sawyer; internal notes name 'Maya'. → Referred to the office (ACT-2); contractor chased at the address on the agency's own booking record. (asked)

Red flags:
- [data_quality] Completion evidence for this ticket points to a different address (Flat 22, 42 Harbour View) and a different operative name than the booking emails; ticket closed with final checks outstanding. → Conflict noted (ACT-1), office task raised (ACT-2), provider asked to confirm in writing (ACT-3); no completion claimed to any party.
- [other] A lock change appears to have been carried out with no quote, no spend cap on file and no landlord approval in the history. → Flagged to the property manager (ACT-2); no retrospective approval sought or payment actioned (PRO-PAYMENTS).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "022", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=landlord approval invoice cost | [] | allow |
| 4 | search_history | completed | query=Harbour View lock change completed | [] | allow |
| 5 | add_note | completed | note=Record conflict + premature closure. Case property is Flat… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed | queue=property_manager, title=Case 022 closed without final checks; job-result evidence n…, summary=Flat 23, 155 Willowmere Road, Alderwick ZZ5 2ZZ — front doo… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_contractor | completed | message=Re: Lock Repair Request — Flat 23, 155 Willowmere Road, Ald… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_tenant | completed | message=Dear Amelia Oakley,  Regarding your report of the front doo… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | put_on_hold | completed | reason=Waiting for Provider — written job result and itemised invo…, until=Close of business on the second working day after ACT-3 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Did you repair or replace the front door lock at Flat 23, 155 Willowmere Road, Alderwick ZZ5 2ZZ, on what date, what was fitted, and please send your itemised invoice (with VAT) for this address only, quoting the job ID. (blocking; No work result, photos or invoice exist for this address; the only completion record (event-013) describes Flat 22, 42 Harbour View, Alderwick ZZ3 3ZZ.)
- Ask **tenant**: Does the front door lock now lock and unlock normally, and were you given a new key / do you hold a working set? (blocking; Tenant-owned fact; confirms whether the reported fault (event-001) is actually resolved before the ticket is treated as complete.)
- Ask **property_manager**: Which job does event-013 belong to, who attended (Oliver Sawyer per event-007 vs 'Maya' per event-016/020), and is retrospective landlord approval needed for a lock change with no cap or approval on file? (non-blocking; Authoritative records disagree and no landlord authority exists in the history; raised as ACT-2.)

Promises made or recorded:
- agency → tenant: Come back to the tenant once the contractor's report is received; no further visit booked unless needed by On receipt of the provider's reply [open]
- agency → contractor: If no job result and invoice by close of business on the second working day, the job is treated as unverified and referred to the property manager before payment by Close of business, second working day after ACT-3 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
