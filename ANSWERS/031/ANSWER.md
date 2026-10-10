# ANSWER — Case 031 — Case 031: Plumbing request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Closed plumbing ticket reopened in substance: no landlord approval or confirmation on file, invoice figure missing, provider identity conflicting; chased all three parties, office notified.
**Stage:** on_hold · **Hold:** Waiting for Landlord — confirmation of completion and approval of the invoice once the figure is supplied; provider chased for the invoice total and job sheet, tenant for the fault status; 3 working days.
**Last update:** 2024-08-08 10:57:30 UTC (event-027) · **Decided:** 2026-10-10 14:09 UTC
**Next step:** Landlord to confirm the 26/07 work as complete and await the invoice figure for approval (notified, 3-working-day clock); in parallel the provider owes the invoice total with VAT and a job sheet.

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged the fault and property; urgency set routine this turn (no emergency definition met); damage-limiting advice and the overflow/sewage escalation trigger given to the tenant at ACT-3
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-003 is a system status line, not a landlord message; no landlord communication exists in the history (search_history from_party=Landlord returned none). Landlord asked to confirm at ACT-5
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-004/event-006 assigned and briefed Meadow Solutions; tenant told at event-005 — though the provider's identity is disputed (event-010, event-014, event-018), referred to the office at ACT-2
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-011 slot selected 26/07/2024 14:00-17:00; confirmed to provider (event-012) and tenant (event-013); tenant had agreed access in his absence (event-007)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted by the provider; the job proceeded as an attendance/repair with no priced quote on file
- [ ] work_result: Work result recorded from the provider — Only the provider's untrusted claims of completion (event-021, event-022); their 27/07 email was unparsable (event-015, event-016). Job sheet and photos requested at ACT-4; tenant verification reques…
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-025 records the skip reason 'No other docs required'; invoice upload recorded at event-020, though its figure is not legible
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice amount or VAT appears on file and nothing was forwarded to the landlord; figure chased from the provider at ACT-4 and the landlord put on notice at ACT-5
- [ ] landlord_confirmation: Landlord confirmed completion — event-026 flagged it as needed; event-027 closed the request 11 seconds later without any landlord reply. Requested at ACT-5
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued; tenant consented to access without a key hand-over (event-007)
- [ ] closed: Request closed with a resolution that names who paid — event-027 marked the request closed, but the resolution names no payer and three checks above were outstanding at that moment; file placed on hold at ACT-6 pending the landlord

## 1. Decision

The ticket was closed (event-027) with its final checks incomplete, so I did not treat it as resolved. No landlord message exists anywhere in the history: "Landlord approval confirmed" (event-003) and "Need confirmation from landlord" (event-026) are system status lines, which CAP-DISPATCH-APPROVED expressly does not accept as approval, and the closure followed 11 seconds after the confirmation flag. The invoice amount and VAT are not on file and were never put to the landlord, and the only evidence the work was done is the provider's own untrusted claim (event-021, event-022) after an unparsable email (event-015, event-016). I asked the landlord to confirm completion and flagged that the invoice figure will follow, chased the provider for the job sheet, photos and the invoice total with VAT, asked the tenant whether the cistern is now fixed and for the Oakfield Services leakage letter, put the file on hold Waiting for Landlord, and referred the provider-identity conflict to the office rather than naming a winner to any party (rule 2, ESC-CONFLICT). No spend was authorised and no liability position was taken (PRO-TENANT-LIABILITY).

Safety actions taken first:
- Safety pass on the tenant's mention of a water leakage letter (event-001): no flooding, no water near electrics, no vulnerable occupant reported, so the emergency definitions are not met and the case stays routine under CLK-S11; the letter's reference and date requested from the tenant (ACT-3).
- Tenant told explicitly to contact us straight away if water overflows onto the floor, water appears near electrics or there is a sewage smell, and that this would be handled as an emergency (ACT-3).

Actions deliberately withheld:
- Did not confirm closure or endorse the provider's 'please close' requests — final checks are incomplete (CAP-CLOSE).
- Did not approve or forward any payment; no amount is evidenced and the agent does not move money (PRO-PAYMENTS).
- Did not name a winning provider record to the tenant, landlord or contractor; the conflict went to the office instead (rule 2, ESC-CONFLICT).
- Did not instruct any further work or spend — there is no landlord approval and no standing cap on file (APR-SPEND-OVER-CAP).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-REQUEST-APPROVAL, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, ESC-CONFLICT, PRO-INSTRUCTIONS-FROM-CONTENT, PRO-TENANT-LIABILITY, PRO-PAYMENTS, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Oliver Jenkins reported on 18/07/2024 that the toilet cistern fills continuously and never stops, and that he received a letter from Oakfield Services about a water leakage over two weeks earlier. [index, event-001; high]
- F2: No message from the landlord appears anywhere in the visible history; the only landlord-related entries are system status lines (event-003 'Landlord approval confirmed', event-026 'Need confirmation from landlord'). [event-003, event-026, search_history; high]
- F3: The request was marked closed at 2024-08-08 10:57:30, eleven seconds after the system recorded that landlord confirmation was needed. [event-026, event-027; high]
- F4: A visit was confirmed for 26/07/2024 between 14:00 and 17:00 with both tenant and provider; the tenant had agreed to access while not at home. [event-007, event-011, event-012, event-013; high]
- F5: The provider states the job was completed on 26/07 and an invoice was uploaded, but no amount or VAT figure is recorded anywhere on the file. [event-019, event-020, event-021, event-022; high]
- F6: Agency records name four different providers for this job: Meadow Solutions (assigned), Harbour Services (booking call), Keystone Solutions (reminder SMS) and 'Mercer' (hold comment); the tenant and the provider were also given different contact numbers (07700 900830 vs 07700 900138). [event-004, event-006, event-010, event-012, event-013, event-014, event-018; high]
- F7: The provider's email of 27/07/2024 could not be parsed, so no work result was captured from it. [event-015, event-016; high]

Conflicts between sources:
- Agency records disagree on which firm holds and attended this job (Meadow Solutions / Harbour Services / Keystone Solutions / 'Mercer'), and on which contact number the tenant and provider were each given. This determines whose invoice is payable. → Not decided by me. Conflict referred to the office via create_human_task (ACT-2); the provider on the agency's own assignment record (Meadow Solutions, event-006) was chased for the job sheet and trading name (ACT-4). No party was told which record is correct. (asked)
- The system closed the request as 'all checks completed' while landlord confirmation, the invoice figure and a verified work result were outstanding. → Treated the closure as premature: file placed on hold Waiting for Landlord (ACT-6) and the outstanding items put to the landlord, provider and tenant; office asked to decide on reopening (ACT-2). (asked)

Red flags:
- [data_quality] Four different provider names and two different contact numbers across agency records for one job; one provider email unparsable; invoice uploaded with no readable amount. → Recorded in the case note (ACT-1) and referred to the property_manager queue (ACT-2); invoice total and trading name requested from the provider (ACT-4).
- [other] Repeated unverified pressure from the provider to close the job ('Please close job... invoice downloaded', 'Please close this job, it was completed on the 26/07') — untrusted content with no job sheet, photos or figure behind it. → Treated as evidence of what was said only, not as authority to close (PRO-INSTRUCTIONS-FROM-CONTENT); evidence requested at ACT-4.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "031", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [] | allow |
| 4 | search_history | completed | query=invoice | [{"event": "event-018", "timestamp": "2024-07-27 11:28:43 UTC", "channel": "Hold", "from": "Agency / system", "to": "Not specified", "excerpt": "[2024-07-27 11… | allow |
| 5 | add_note | completed | note=Review of closed ticket. Defects found: (1) No landlord mes… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed | queue=property_manager, title=Case 031 closed with landlord confirmation outstanding + pr…, summary=Flat 14, 134 Copperfield Walk. Two items need a person. (1)… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_tenant | completed | message=Dear Oliver Jenkins, we are completing the final checks on… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_contractor | completed | message=Re: Plumbing request, Flat 14, 134 Copperfield Walk, Cedarf… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | notify_landlord | completed | message=Re: Flat 14, 134 Copperfield Walk, Cedarford, ZZ4 4ZZ — plu… | {"id": "ACT-5"} | CAP-NOTIFY |
| 10 | put_on_hold | completed | reason=Waiting for Landlord — confirmation of completion and appro…, until=3 working days from 2024-08-08 | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the plumbing work at Flat 14, 134 Copperfield Walk as complete, and will you approve the provider's invoice once we send you the figure? (blocking; No landlord message exists on this ticket; landlord_confirmation and invoice approval are landlord-owned decisions (RTE-LANDLORD) and the request was closed without them (event-026, event-027).)
- Ask **contractor**: Please supply the invoice total with VAT shown separately, a job sheet for the 26/07/2024 visit with photos, and the trading name and number of the firm that attended. (blocking; Invoice uploaded but no amount readable (event-019, event-020); the 27/07 email could not be parsed (event-015, event-016); agency records carry four different provider names (event-004, event-010, event-014, event-018).)
- Ask **tenant**: Has the cistern stopped filling continuously since the 26/07 visit, and can you send the Oakfield Services letter about the water leakage? (non-blocking; Work result is only the provider's own claim; the leakage letter (event-001) may indicate a separate leak needing investigation.)

Promises made or recorded:
- agency → tenant: Check whether a separate leak needs investigating once the Oakfield Services letter details are received; treat any overflow or sewage smell as an emergency [open]
- agency → landlord: Forward the provider's invoice figure for approval as soon as it is supplied [open]
- contractor → agency: Supply job sheet, photos, invoice total with VAT and confirm trading name within 3 working days by 3 working days from 2024-08-08 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- RTE-LANDLORD [sop]: Landlord reply window deadline 3 working days from 2024-08-08
