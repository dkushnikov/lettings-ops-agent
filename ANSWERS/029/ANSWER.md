# ANSWER — Case 029 — Case 029: Cracked basin repair request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Basin job recorded done and closed, but landlord confirmation and a first-hand work result are missing and records disagree on who attended; asked landlord and tenant, referred conflict to office.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation of completion requested (ACT-3); tenant verification also requested (ACT-4); provider-identity conflict with the office (ACT-2).
**Last update:** 2025-04-09 21:56:29 UTC (event-022) · **Decided:** 2026-10-10 14:07 UTC
**Next step:** Landlord to confirm the basin repair is complete (asked ACT-3); in parallel tenant to confirm the basin is repaired (ACT-4) and the office to resolve who attended (ACT-2).

Definition of done (3/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (report), event-007 + event-010 (cause established as pre-existing at move-in); no hazard element, routine
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No landlord instruction, cap or approval anywhere in the history (search_history: no landlord events); event-015 records no quote required so no spend authority was exercised
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003 (provider assigned), event-005 (provider briefed), event-004 (tenant told Henry Quinn would attend)
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-011 held awaiting contractor to arrange appointment; no confirmed slot appears in the history
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-015: no quote required
- [ ] work_result: Work result recorded from the provider — event-014 is a second-hand note ('update received from Miles'); no provider message, photos or invoice in the history; tenant verification requested (ACT-4)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-018 records the skip with the reason 'Update received from Miles advising job done'
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-015: no quote required; no invoice raised in the history
- [ ] landlord_confirmation: Landlord confirmed completion — event-019 'Need confirmation from landlord'; no landlord reply in the history; requested ACT-3
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-021 keys return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-022 closed the request as 'all checks completed', but landlord confirmation and work result are unevidenced; office asked to confirm the closure stands (ACT-2)

## 1. Decision

The repair was recorded as done and the request closed by the agency (event-014, event-022), but two final-check items are not evidenced: landlord confirmation of completion (raised at event-019, no landlord message anywhere in the history) and any first-hand work result or document from the provider (event-018 skip reason is hearsay). Agency records also disagree about who held the job: Henry Quinn is the assigned provider (event-003, event-005) while the completion update is attributed to "Miles" (event-014), with "Leo" (event-013) and "shared Beacon Utilities" (event-012) named elsewhere. I did not pick a side with any party: I logged the conflict (ACT-1) and referred it to the office (ACT-2). Within authority I asked the landlord to confirm completion (ACT-3) and the tenant to confirm the basin is actually repaired (ACT-4). No spend was committed: no landlord cap or approval is on file (CAP-DISPATCH-ROUTINE default cap £0; APR-SPEND-OVER-CAP), and none was needed as event-015 records no quote required. No liability finding was made on the tenant's statement that the basin was cracked at move-in (event-010) — that is a human decision (PRO-TENANT-LIABILITY). Nothing in the artefacts matches an emergency definition; routine under CLK-S11.

Safety actions taken first:
- Safety pass: no hazard keyword condition reported or observed in any artefact — no gas, electrical, damp/mould, water escape or detector issue; the fault is a cracked basin only (event-001, event-010). Tenant asked to report immediately any leak or water escape (ACT-4). No emergency definition matched, so no make-safe step was due.

Actions deliberately withheld:
- Did not close or re-close the request: work result and landlord confirmation are unevidenced (CAP-CLOSE).
- Did not re-instruct or duplicate a work order for the same fault (playbook: one work order per fault).
- Did not decide whether the pre-existing crack is tenant-payable (PRO-TENANT-LIABILITY).
- Did not name a cost: no quote or invoice exists in the record (event-015).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, ESC-CONFLICT, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Freya Fletcher reported a cracked bathroom hand basin at Flat 6, 24 Lantern Quay, Westmarsh, ZZ3 9ZZ on 14 March 2025. [index, event-001, event-004, get_case_details; high]
- F2: A plumbing provider, Henry Quinn, was assigned and briefed on 16 March 2025; the tenant was told he would attend and quote. [event-003, event-004, event-005; high]
- F3: The tenant answered the agency's question on cause: the basin was already cracked when she moved in (quoted fragment: 'was like that at the time I was mooving in'). [event-007, event-010; medium]
- F4: Completion is recorded only as a second-hand note, 'Update received from Miles advising job done'; no quote was required. [event-014, event-015; high]
- F5: Document upload was skipped, landlord confirmation was flagged as needed, keys return was confirmed, and the request was then closed as all checks complete. [event-018, event-019, event-021, event-022; high]
- F6: No landlord or contractor message exists in the visible history; no landlord spend cap or standing instruction is on file. [search_history, get_case_details; high]

Conflicts between sources:
- Agency records disagree about who held and completed the job: assigned provider Henry Quinn (event-003, event-005) vs completion update from 'Miles' (event-014), with 'Leo' (event-013) and 'shared Beacon Utilities' / Quinn on annual leave (event-012) also named. → Not decided by me; logged (ACT-1) and referred to the office (ACT-2). No party was told which record is right. (asked)
- The file was closed as 'all checks have been completed' (event-022) although landlord confirmation was outstanding (event-019) and documents were skipped (event-018). → Landlord asked to confirm completion (ACT-3); office asked whether the closure stands (ACT-2). (asked)

Red flags:
- [data_quality] Work result and document-skip reason rest on a named person ('Miles') who is not the provider of record, and the request was closed with landlord confirmation unevidenced. → Logged (ACT-1), referred to the office (ACT-2), verification requested from landlord (ACT-3) and tenant (ACT-4).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "029", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-46-document | {"error": "no attachment named attachment-46-document"} | allow |
| 4 | search_history | completed | query=Miles Leo Beacon Quinn provider | [] | allow |
| 5 | search_history | completed | from_party=Landlord | [] | allow |
| 6 | add_note | completed | note=Post-closure review. Record conflicts and gaps: (1) Provide… | {"id": "ACT-1"} | CAP-LOG |
| 7 | create_human_task | completed | queue=property_manager, title=Case 029 closed with provider-identity conflict and landlor…, summary=Flat 6, 24 Lantern Quay, Westmarsh, ZZ3 9ZZ — cracked bathr… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 8 | notify_landlord | completed | message=Flat 6, 24 Lantern Quay, Westmarsh, ZZ3 9ZZ — cracked bathr… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | notify_tenant | completed | message=Dear Ms Fletcher, regarding the cracked bathroom basin at F… | {"id": "ACT-4"} | CAP-NOTIFY |

## 4. Human handover / information requested

- Ask **landlord**: Please confirm you are satisfied the cracked bathroom basin at Flat 6, 24 Lantern Quay is complete, so the file can be finalised (no quote was required and no invoice has been raised). (blocking; event-019 required landlord confirmation and no landlord message exists in the history; landlord owns confirmation of completion (RTE-LANDLORD).)
- Ask **tenant**: Has the bathroom basin actually been repaired or replaced, and are you satisfied with it? Tell us immediately if there is any leak or water escaping. (blocking; The only work result is second-hand (event-014) with no provider message or photos; the tenant can verify the result (RTE-TENANT).)
- Ask **property_manager (office)**: Which record is correct about who held and completed this job — Henry Quinn (event-003/005), Miles (event-014), Leo (event-013) or Beacon Utilities (event-012) — and does the closure at event-022 stand? (non-blocking; Agency records disagree and the difference changes who is chased or paid (ESC-CONFLICT); referred via ACT-2.)

Promises made or recorded:
- agency → tenant: Job will not be attended without agreeing a time first; job reopened if the basin is not in fact repaired or there is a leak (ACT-4) [open]
- agency → landlord: File will be finalised once completion is confirmed (ACT-3) [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
