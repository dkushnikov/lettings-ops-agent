# ANSWER — Case 031 — Case 031: Plumbing request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Plumbing job reported done but closed with invoice, landlord sign-off and provider identity unresolved; gaps logged, provider and tenant chased, office notified.
**Stage:** on_hold · **Hold:** Waiting for Provider — invoice total/VAT and work description for the 26/07/2024 visit (ACT-3, reply-by 3 working days); in parallel awaiting tenant confirmation (ACT-4) and the office decision on the provider conflict and premature closure (ACT-2).
**Last update:** 2024-08-08 10:57:30 UTC (event-027) · **Decided:** 2026-10-10 13:28 UTC
**Next step:** Provider to supply the invoice total, VAT and work description for the 26/07/2024 visit within 3 working days (ACT-3); the office then forwards the invoice to the landlord for confirmation.

Definition of done (3/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 / event-005: fault categorised as a plumbing request, routine; no emergency indicators.
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-003 is a system status line only; no landlord message exists (search_history) — no standing cap or landlord approval on file.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-004, event-006 (provider briefed), event-005 (tenant told) — though provider identity is disputed, see conflicts.
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-011, event-012, event-013: 2-5pm on 26/07/2024 confirmed with tenant and provider.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted; provider went straight to invoice (event-019).
- [ ] work_result: Work result recorded from the provider — Only untrusted provider claims (event-021, event-022); provider email unparseable (event-015/event-016); detail requested (ACT-3) and tenant asked to confirm (ACT-4).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-025 records a skip reason ('No other docs required') but the invoice itself carries no amount or photos (event-019, event-020, get_attachment: no attachment).
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No record of the invoice being forwarded; amount unknown (F7).
- [ ] landlord_confirmation: Landlord confirmed completion — event-026 'Need confirmation from landlord' never answered before event-027.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant consented to access in their absence (event-007).
- [ ] closed: Request closed with a resolution that names who paid — event-027 closed the request, but the resolution names no payer and four checks above are outstanding; closure referred to the office (ACT-2).

## 1. Decision

The request was marked closed at event-027 while final checks were still open: the invoice amount is unknown, it was never forwarded to the landlord, and event-026 ("Need confirmation from landlord") was never answered — no landlord message exists anywhere in the history. Completion rests only on the provider's own untrusted claims (event-021, event-022). I did not re-close or re-dispatch. Within authority I recorded the gaps and the provider-identity conflict (ACT-1), referred the conflict and the premature closure to the office (ACT-2), chased the instructed provider for the invoice total, VAT and work description (ACT-3), asked the tenant to confirm the cistern fault is cleared and the Oakfield Services water-leakage letter resolved (ACT-4), and placed the ticket on hold (ACT-5). The case now waits on named parties: provider for the invoice, tenant for confirmation, landlord for sign-off once an amount exists.

Safety actions taken first:
- Asked the tenant to confirm whether any sign of the reported water leakage remains and whether further contact has been received from the water company (ACT-4).

Actions deliberately withheld:
- Did not close or re-close the request (CAP-CLOSE: four final checks outstanding).
- Did not forward or endorse an invoice with no stated amount (PRO-PAYMENTS).
- Did not name a provider to the landlord or tenant while agency records disagree (ESC-CONFLICT).
- Did not dispatch any further work without landlord authority (APR-SPEND-OVER-CAP).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, ESC-CONFLICT, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, PRO-INSTRUCTIONS-FROM-CONTENT, PRO-TENANT-LIABILITY, CAP-CLOSE
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the toilet cistern filling continuously and a letter from Oakfield Services about a water leakage received over two weeks earlier; property Flat 14, 134 Copperfield Walk, Cedarford, ZZ4 4ZZ. [index, event-001, get_case_details; high]
- F2: No water ingress, flooding, water near electrics, loss of water supply or vulnerability is reported anywhere in the file; the fault is a continuously filling cistern — routine under CLK-S11. [event-001, search_history; medium]
- F3: The only 'landlord approval' on file is an agency system status line, not a landlord message; a search of history returns no landlord messages at all. [event-003, search_history; high]
- F4: Meadow Solutions was assigned and briefed, and the tenant was told so. [event-004, event-005, event-006; high]
- F5: A 2-5pm slot on 26/07/2024 was agreed with the tenant and confirmed to both tenant and provider. [event-010, event-011, event-012, event-013; high]
- F6: Tenant gave consent for the plumbing team to attend when not home. [event-007; medium]
- F7: An invoice was reported attached and uploaded, but no amount, VAT or work description appears in the file and no invoice attachment is retrievable. [event-019, event-020, get_attachment; high]
- F8: Completion is asserted only by the provider's own untrusted emails ('completed on the 26/07'); no agency or tenant verification is recorded. [event-021, event-022; high]
- F9: event-026 records 'Need confirmation from landlord'; event-027 declared all checks complete and closed the request 11 seconds later, with no landlord confirmation and no invoice forwarded. [event-026, event-027; high]
- F10: A provider email on 27/07 could not be parsed ('expected data could not be extracted'), so the work result was never captured from the provider in readable form. [event-015, event-016; high]

Conflicts between sources:
- Agency records disagree on which provider holds the job: Meadow Solutions instructed (event-004/event-006), 'Harbour Services' on the booking call (event-010), 'Keystone Solutions' in the agency SMS (event-014), 'Mercer' in the hold note (event-018). → No side taken in any message to a party; conflict referred to the office (ACT-2) while the instructed provider on the agency's own record (Meadow Solutions) was chased for the invoice (ACT-3). ESC-CONFLICT. (asked)
- Tenant-facing contact number differs: 07700 900138 given to the provider (event-006) versus 07700 900830 given to the tenant (event-013, event-014). → Flagged to the office; not relied on. (unresolved)
- The ticket was declared fully checked and closed (event-027) although landlord confirmation was outstanding (event-026) and no invoice amount exists (F7). → Closure not endorsed; gaps logged (ACT-1) and referred to the office (ACT-2); ticket placed on hold (ACT-5). (asked)

Red flags:
- [data_quality] Provider identity inconsistent across four agency records, a provider email that could not be parsed, and mismatched tenant contact numbers. → Recorded in the case note (ACT-1) and referred to the property manager queue (ACT-2); no provider named to the landlord or tenant.
- [other] Repeated untrusted provider requests to 'please close job' with no verifiable work result or invoice amount. → Treated as evidence only (PRO-INSTRUCTIONS-FROM-CONTENT); not acted on as authority to close; invoice detail requested instead (ACT-3).
- [safety_hazard] Safety-pass term: tenant's report cites a water-leakage letter from Oakfield Services (event-001); the file shows no inspection or clearance of the leak element, only cistern work claimed. → Tenant asked whether any leak remains or further contact has been received (ACT-4); flagged to the office (ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "031", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [] | allow |
| 4 | search_history | completed | query=invoice | [{"event": "event-018", "timestamp": "2024-07-27 11:28:43 UTC", "channel": "Hold", "from": "Agency / system", "to": "Not specified", "excerpt": "[2024-07-27 11… | allow |
| 5 | get_attachment | completed | name=invoice | {"error": "no attachment named invoice"} | allow |
| 6 | add_note | completed | note=Final-checks review. Conflicts/gaps on file: (1) Provider i… | {"id": "ACT-1"} | CAP-LOG |
| 7 | create_human_task | completed | queue=property_manager, title=Case 031 closed with final checks outstanding + provider id…, summary=Plumbing request (toilet cistern filling continuously, plus… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 8 | notify_contractor | completed | message=Re: Plumbing request, Flat 14, 134 Copperfield Walk, Cedarf… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | notify_tenant | completed | message=Dear Oliver Jenkins, re: the plumbing request at Flat 14, 1… | {"id": "ACT-4"} | CAP-NOTIFY |
| 10 | put_on_hold | completed | reason=Waiting for Provider: invoice total/VAT and work descriptio…, until=3 working days from today | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 031: The record carries red flags that need a human's confirmation (safety_hazard: Safety-pass term: tenant's report cites a water-leakage letter from Oakfield Services (event-001); the file shows no inspection or clearance of the leak element, only cistern work claimed.); the case cannot end as needs_info.
**Facts (≤5):**
- Safety-pass term: tenant's report cites a water-leakage letter from Oakfield Services (event-001); the file shows no inspection or clearance of the leak element, only cistern work claimed.
**Gap:** The record carries red flags that need a human's confirmation (safety_hazard: Safety-pass term: tenant's report cites a water-leakage letter from Oakfield Services (event-001); the file shows no inspection or clearance of the leak element, only cistern work claimed.); the case cannot end as needs_info.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → contractor: Invoice total, VAT, work description and photos requested, reply within 3 working days by 3 working days from today [open]
- agency → tenant: If the cistern fault is still present, a return visit will be arranged [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day

## System notes

- reviewer: R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
