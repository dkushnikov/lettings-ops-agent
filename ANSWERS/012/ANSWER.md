# ANSWER — Case 012 — Case 012: Dishwasher Door Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Dishwasher door repaired and tested (event-024), but ticket closed with landlord confirmation and invoice sign-off outstanding; landlord asked, office task raised.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation of the completed repair and sign-off of the provider's invoice; 3 working days from ACT-2, then the property-manager task (ACT-4) takes it on.
**Last update:** 2026-05-03 15:05:04 UTC (event-031) · **Decided:** 2026-10-10 14:02 UTC
**Next step:** Landlord to confirm the completed repair and authorise the provider's invoice (emailed ACT-2; 3-working-day reply window), with the property manager holding ACT-4 if no reply.

Definition of done (6/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (fault logged), event-005 (damage-limiting/troubleshooting steps to tenant), urgency routine — no emergency definition met
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No landlord message in history (search_history); authority rests on internal notes event-008 and event-012 only; landlord asked to confirm at ACT-2
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-013, event-015 (provider briefed), event-014 (tenant told who is coming)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-017, event-018, event-019 (slot 29/04/2026 08:00-12:00 confirmed with tenant and provider)
- [-] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote amount or VAT recorded and none put to the landlord despite the brief at event-015; engineer proceeded to repair on the visit (event-024). Flagged for the property manager at ACT-4
- [x] work_result: Work result recorded from the provider — event-024 — door lock repaired, appliance tested working; event-025/026
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-027 — upload skipped, reason recorded as 'not needed'
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Invoice referenced at event-024 but no record of it being forwarded and no amount on file; raised with the landlord at ACT-2 and the property manager at ACT-4
- [ ] landlord_confirmation: Landlord confirmed completion — event-028 flagged confirmation as needed and no landlord reply exists; requested at ACT-2
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-030 — keys return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-031 closed the request, but the resolution names no payer and landlord confirmation/invoice remain outstanding; reopened for final checks

## 1. Decision

The repair is done and reported (event-024), but the ticket was closed (event-031) with final checks outstanding: the system itself still flagged "Need confirmation from landlord" (event-028), no landlord message exists anywhere in the history, no quote/VAT was ever put to or approved by the landlord despite the provider brief requiring approval before proceeding (event-015), and the invoice is not evidenced as forwarded. Within my authority I recorded the review note, asked the landlord to confirm the completed repair and the invoice (no amount stated — none is on file), told the tenant the reported outcome and invited them to flag a recurrence, and raised a property-manager task covering the missing approval trail and the provider-name discrepancy. I did not decide liability, state a cost, or move money (PRO-PAYMENTS, PRO-TENANT-LIABILITY). The case now waits on the landlord's reply.

Safety actions taken first:
- Safety pass check: the only keyword-adjacent content is the instruction to switch the appliance off at the socket in the troubleshooting email (event-005); no gas, burning smell, sparks, water near electrics, damp/mould, detector or occupant-vulnerability issue is reported anywhere in the record. Appliance fault only — no emergency definition met, no hazard red flag raised.

Actions deliberately withheld:
- Did not re-close the request: landlord confirmation and invoice forwarding are outstanding (CAP-CLOSE).
- Did not instruct or re-instruct any contractor: work is complete and no further visit is needed.
- Did not state or approve any cost, or decide who pays (PRO-PAYMENTS, PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, APR-SPEND-OVER-CAP, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Fault reported 15/04/2026: dishwasher door not closing at Flat 9, 89 Juniper Mews, Willowbank, ZZ2 0ZZ; no hazard element. [index, event-001; high]
- F2: Agency sent the tenant troubleshooting steps on 19/04/2026 (sent twice, duplicate). [event-005, event-006; high]
- F3: Tenant replied 23/04/2026 that all checks were done and the door still does not close. [event-011; high]
- F4: Provider Riverside Compliance was assigned and briefed on 25/04/2026; tenant told who was coming and that a quote would need landlord approval before work. [event-013, event-014, event-015; high]
- F5: Visit slot 29/04/2026 08:00-12:00 agreed with the tenant and confirmed to tenant and provider. [event-016, event-017, event-018, event-019; high]
- F6: Work result recorded 03/05/2026: door lock had engaged prematurely, lock repaired, appliance run on test and working. [event-024; high]
- F7: No message from the landlord exists in the visible history; the only authority cited for instructing the engineer is internal agency notes. [search_history, event-008, event-012; high]
- F8: No quote amount or VAT figure appears anywhere in the record, and no quote was put to the landlord, although the provider brief said to proceed only after approval. [event-015, event-024; high]
- F9: Document upload skipped with reason 'not needed'; keys return confirmed; landlord confirmation flagged as still needed; request then closed. [event-027, event-028, event-030, event-031; high]

Conflicts between sources:
- Provider identity: agency record names Riverside Compliance; untrusted call transcripts name Cedar Utilities and Meadow Services, and the appointment SMS is signed Harbour Homes. Tenant surname also differs (Leo Kendall vs Leo Turner). → Acted on the agency's own record (Riverside Compliance) for all messages; referred the discrepancy to the property manager (ACT-4) before the invoice is matched and paid. (asked)
- The ticket was closed as 'all checks completed' while the same session recorded that landlord confirmation was still needed and no invoice forwarding is evidenced. → Landlord asked to confirm completion and the invoice (ACT-2); property manager task raised (ACT-4). (asked)

Red flags:
- [data_quality] Three different provider names and two tenant surnames across the call/SMS records for one job; also a duplicated troubleshooting email (event-005/006) and duplicated status updates (event-022/023). → Relied only on the agency record for provider identity and the case record for the tenant's name; referred to the property manager (ACT-4) and logged (ACT-1).
- [other] Spend was incurred with no landlord approval message and no standing cap on file — authority rests on internal notes only ('LL already agreed for GS to go out'). → Landlord asked to confirm/authorise the invoice before payment (ACT-2); flagged to the property manager (ACT-4). No payment made (PRO-PAYMENTS).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "012", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=landlord approval invoice cost quote | [] | allow |
| 4 | search_history | completed | from_party=Landlord | [] | allow |
| 5 | add_note | completed | note=Review of closed ticket. Facts from the record: fault repor… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_landlord | completed | message=Flat 9, 89 Juniper Mews, Willowbank, ZZ2 0ZZ — dishwasher d… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Dear Leo Turner,  Flat 9, 89 Juniper Mews, Willowbank, ZZ2… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | create_human_task | completed | queue=property_manager, title=Flat 9, 89 Juniper Mews — dishwasher closed with final chec…, summary=Ticket was closed 03/05/2026 (event-031) although the syste… | {"id": "ACT-4"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the completed dishwasher repair at Flat 9, 89 Juniper Mews (door lock repaired and appliance tested working, 29 April 2026) and authorise settlement of the provider's invoice? If you did not agree this work, tell us now and we will hold the invoice. (blocking; RTE-LANDLORD: landlord confirmation was still flagged as needed (event-028) and no landlord approval or standing spend cap is on file (search_history from_party=Landlord: nil; authority rests only on internal notes event-008, event-012).)
- Ask **property_manager**: Which firm actually attended and should the invoice be matched to — Riverside Compliance per the agency record, or one of the firms named in the call/SMS records? (non-blocking; Agency record (event-013, event-015, event-018) names Riverside Compliance; untrusted transcripts name Cedar Utilities (event-016) and Meadow Services (event-021) and the SMS is signed Harbour Homes (event-020). Raised as ACT-4; not blocking the landlord question.)

Promises made or recorded:
- agency → landlord: Pass the file to the property manager if no reply to the confirmation/invoice request by 3 working days from ACT-2 [open]
- agency → tenant: Reopen the job if the door fault returns [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- RTE-LANDLORD [sop]: Landlord reply window deadline 3 working days from ACT-2
