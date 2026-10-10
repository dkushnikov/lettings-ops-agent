# ANSWER — Case 026 — Case 026: Oven Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Oven element repair done and confirmed by tenant, but ticket closed early: landlord confirmation and invoice still outstanding, and provider identity conflicts.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation of completion requested (ACT-2, 3 working days); in parallel Waiting for Provider for the invoice copy (ACT-3).
**Last update:** 2025-09-08 19:13:14 UTC (event-038) · **Decided:** 2026-10-10 14:07 UTC
**Next step:** Landlord to confirm the works are complete and await the invoice we will forward once the provider supplies it (asked ACT-2, 3-working-day chase).

Definition of done (7/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 — categorised Appliances, severity ROUTINE, with tenant Q&A on fuel type and access
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 — landlord's own reply 'Yes go ahead' (CAP-DISPATCH-APPROVED); no standing cap on file
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-012, event-013, event-014 — provider assigned, tenant and provider briefed
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-017/018/019 slot issued; tenant moved it to 08/09 (event-021, event-025) and the visit took place (event-029)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-030 — 'no quote needed'
- [x] work_result: Work result recorded from the provider — event-029 — main heating element replaced, hobs cleaned, tenant confirms oven working
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-034 — upload skipped with reason recorded; photos/job sheet now requested from the provider (ACT-3)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice copy or amount on file; event-029 refers to one only. Provider asked (ACT-3); landlord told it will follow (ACT-2)
- [ ] landlord_confirmation: Landlord confirmed completion — event-035 flagged it as still needed; confirmation requested at ACT-2
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-037 — keys return confirmed (validation warning about priority noted to the office in ACT-4)
- [ ] closed: Request closed with a resolution that names who paid — event-038 closed the request while invoice_to_landlord and landlord_confirmation were outstanding; not re-closed by me (CAP-CLOSE)

## 1. Decision

The repair itself is verifiably done (tenant confirmed the main oven heating element was replaced and the oven works, event-029), but the ticket was closed (event-038) with final checks outstanding: landlord confirmation was still flagged as needed (event-035) and no invoice has ever been put in front of the landlord (event-029 names an invoice but no amount, VAT or copy is on file). I did not re-close it. I notified the landlord that the work is reported complete and asked for their confirmation, asked the instructed provider for the invoice, job sheet, photos and written confirmation of the invoicing entity, and referred the provider-identity mismatch to the office (ACT-1..ACT-4). No payment moved, no liability decided, no re-attendance ordered.

Safety actions taken first:
- Safety pass run: electric oven/hob repair only; no gas appliance, burning smell, sparks, water near electrics, damp/mould or occupant vulnerability reported in any artefact. Heating element replaced and oven confirmed working (event-029). No smoke or CO alarm question raised on this ticket; recorded as a check with no adverse finding.

Actions deliberately withheld:
- Did not re-close the request: landlord confirmation and invoice forwarding are still pending (CAP-CLOSE).
- Did not state or forward any invoice amount, and did not action payment (PRO-PAYMENTS).
- Did not decide who bears the cost of the repair (PRO-TENANT-LIABILITY).
- Did not raise a second work order or re-dispatch: the work is reported complete (ESC-UNCONFIRMED / contractor-failure guidance on not duplicating).

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-APPROVED, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, RTE-CONTRACTOR, RTE-STAFF, ESC-CONFLICT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the fan oven's main heating element not heating; grill element works; electric hob; no access constraints, no pets. [event-001, event-002; high]
- F2: Intake classified the issue as Appliances, severity ROUTINE. [event-002; high]
- F3: No landlord standing spend cap is on file for this property; authority for the job comes from the landlord's own reply 'Yes go ahead'. [event-009, get_case_details; high]
- F4: A provider was assigned and both tenant and provider were briefed on 26 August 2025. [event-012, event-013, event-014; high]
- F5: A slot of 30/08/2025 10:00-12:00 was issued, then the tenant stated the agreed date was 8 September; the agency told the tenant to take the provider's confirmed date. [event-017, event-018, event-019, event-021, event-023, event-025, event-028; medium]
- F6: Work result: main oven heating element replaced, hobs cleaned, tenant confirmed the oven works. [event-029; high]
- F7: No quote was required for the job. [event-030; high]
- F8: Document upload was skipped with the reason 'approved by landlord in activity notes'. [event-034; high]
- F9: Landlord confirmation was flagged as still needed, yet the request was marked closed 34 seconds later. [event-035, event-038; high]
- F10: No invoice amount, VAT figure or document exists anywhere in the file; event-029 only refers to an invoice in conversation. [event-029, event-030; high]
- F11: The instructed provider on the agency's own record is Keystone Compliance; message bodies variously name Riverside Works, Harbour Works and Lantern Utilities. [event-012, event-014, event-018, event-016, event-020, event-025, event-029; high]
- F12: Keys return was recorded alongside a validation error about priority not being decreasable. [event-037; medium]

Conflicts between sources:
- Who holds and invoices this job: agency work order names Keystone Compliance; attendance call names Riverside Works; tenant confirmation and the invoice reference name Harbour Works; reminder SMS signs as Lantern Utilities. → Not decided by me. Referred to the office by human task ACT-4 and the provider asked to confirm its invoicing entity in writing (ACT-3). No side taken in any message to a party; no payment actioned. (asked)
- Occupant name differs across records: case record and tenant signature say Clara; agency letters address Ruben Oakley; transcripts name Grace Mercer, Harriet Fletcher and Leo. → Case-record address used; no name from a message body copied into another party's letter (rule 7). Flagged as data quality. (source_hierarchy)
- Visit date: system recorded 30/08/2025 while the tenant stated 8 September; the 8 September attendance is the one borne out by the work result. → Resolved by outcome: the visit took place and the repair completed around 8 September (event-029). (tool_check)

Red flags:
- [data_quality] Four different provider trading names and five different occupant names appear across the ticket; the invoicing entity does not match the instructed one. → Recorded in the case note (ACT-1) and referred to the property manager queue (ACT-4); provider asked to confirm its invoicing name (ACT-3).
- [other] Request closed as 'all checks completed' (event-038) while landlord confirmation was outstanding (event-035) and no invoice had been forwarded; closure is not supported by the file. → Ticket treated as at final_checks, not closed; landlord and provider chased; office informed.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "026", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Review of closed ticket. Facts from the record: routine app… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Re: Flat 3, 3 Willowmere Road, Alderwick, ZZ9 6ZZ — oven re… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_contractor | completed | message=Re: Oven Repair Request — Flat 3, 3 Willowmere Road, Alderw… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | create_human_task | completed | queue=property_manager, title=Case 026 — closed early: provider-identity mismatch and no…, summary=Ticket was closed (event-038) with two definition-of-done i… | {"id": "ACT-4"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **landlord**: Please confirm you are satisfied the oven repair at Flat 3, 3 Willowmere Road is complete. The invoice will follow for your approval once the provider supplies it. (blocking; RTE-LANDLORD: landlord confirmation is a required final check and was still flagged outstanding at event-035 when the ticket was closed at event-038.)
- Ask **contractor**: Please send the invoice (net, VAT, total), job sheet and any photos for the 8 September oven repair, and confirm in writing the trading name invoicing for this work order. (blocking; RTE-CONTRACTOR: no invoice amount or document exists on file (event-029 refers to one only), and the invoicing name does not match the instructed provider (event-014 vs event-025/event-029).)
- Ask **property_manager**: Which company actually holds and invoices this job — Keystone Compliance as instructed, or Harbour Works as invoicing? (non-blocking; ESC-CONFLICT / rule 2: agency records disagree on who holds the job; referred by human task ACT-4 rather than decided in a message to a party.)

Promises made or recorded:
- agency → landlord: Forward the provider's invoice once received; chase again if no confirmation within 3 working days by 3 working days from ACT-2 [open]
- agency → contractor: No payment released until invoice, job sheet and invoicing-entity confirmation are received and the landlord approves by 3 working days from ACT-3 [open]
- agency → tenant: Come back to the tenant after seeking landlord approval to send a contractor [kept]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day deadline 2025-08-27
- CLK-S11 [in_force]: Repair within a reasonable time once reported
