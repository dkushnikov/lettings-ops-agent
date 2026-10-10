# ANSWER — Case 042 — Case 042: Washing Machine Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Washing machine not heating on 60°C+; repair done under landlord approval (event-008), but closed without landlord confirmation and with an unreconciled invoice figure — final checks reopened.
**Stage:** on_hold · **Hold:** Waiting for Landlord — confirmation of completion requested (ACT-2, 3-day reply window); invoice figure being verified by the office (ACT-4).
**Last update:** 2024-02-28 20:51:40 UTC (event-031) · **Decided:** 2026-10-10 13:32 UTC
**Next step:** Landlord (Mercer) to confirm the repair is complete and to receive the verified invoice; office to obtain the invoice document from Lantern Services (ACT-4).

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (routine, appliance-only fault); tenant acknowledged event-005
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-008 landlord's own email approving an engineer
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010, event-013 (provider briefed), event-012 (tenant told)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-017/018/019 slot confirmed to both sides, though the logged date conflicts with event-016/event-022 — conflict recorded ACT-1/ACT-4
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote produced — job completed on the call-out visit (event-029)
- [ ] work_result: Work result recorded from the provider — Only the agency's own update (event-025) and an invoice summary (event-024); no provider report; tenant asked to confirm (ACT-3)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-029 skip reason 'Job completed on call out, no photos or quote'; invoice document requested via ACT-4
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Cost mentioned in event-025 but the figure conflicts with event-024; invoice document not forwarded (ACT-2, ACT-4)
- [ ] landlord_confirmation: Landlord confirmed completion — event-030 flagged it as needed; no landlord reply on file; requested at ACT-2
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provided access (event-013)
- [ ] closed: Request closed with a resolution that names who paid — event-031 closed the ticket while event-030 items were outstanding; file placed back on hold at ACT-5 pending landlord confirmation and the invoice

## 1. Decision

The repair was authorised by the landlord's own email and carried out; I did not re-instruct or re-close anything. The file was closed before the landlord's confirmation was obtained and with an unreconciled invoice figure, so I re-opened the final checks: wrote to the landlord for completion confirmation and flagged the invoice discrepancy, asked the tenant to confirm the machine now heats, and passed the billing/record conflicts to the office queue. Case waits on the landlord.

Actions deliberately withheld:
- Did not re-close the request: landlord confirmation and a reconciled invoice are outstanding (CAP-CLOSE).
- Did not instruct any further contractor spend: no standing cap on file and no new landlord approval for additional work (APR-SPEND-OVER-CAP).
- Did not forward or action payment of the invoice (PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CAP-DISPATCH-APPROVED
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the washing machine does not heat water on cycles of 60°C or above; property hot water unaffected. [index, event-001, event-002; high]
- F2: Intake classified the issue ROUTINE; no emergency definition met (appliance only, no hazard). [event-002; high]
- F3: Landlord's own email approved instructing an engineer: 'Yes please arrange an engineer'. [event-008; high]
- F4: Lantern Services assigned and briefed; tenant told who would attend. [event-010, event-012, event-013; high]
- F5: Provider invoice recorded as GBP 75.11; landlord separately told the cost was £75 + VAT; no invoice or photos uploaded (skip reason: job completed on call out). [event-024, event-025, event-029; medium]
- F6: Agency reported the repair done by replacing the wiring to the heating element. [event-025; medium]
- F7: Ticket was closed (event-031) one minute after the note 'Need confirmation from landlord' (event-030); no landlord confirmation appears in the history. [event-030, event-031; high]

Conflicts between sources:
- Appointment record disagrees: confirmed slot logged as 23/02/2024 15:25-15:30, a time before the booking calls, while the calls agreed 'Tuesday 1pm'; the contractor was still chasing a booking on 27/02. → Recorded in the case note (ACT-1) and passed to the office queue (ACT-4); tenant asked to confirm the repair actually took place (ACT-3). (asked)
- Invoice amount: GBP 75.11 on the provider's invoice email vs '£75 + VAT' reported to the landlord. → Landlord told not to treat either figure as final (ACT-2); office asked to obtain the invoice document and reconcile before payment (ACT-4). (asked)
- Contractor brief stated 'Pets: multiple tenants in this property' although intake records no pets. → Intake Q&A is the tenant's own answer; noted as a briefing data error (ACT-1), no action needed with the visit complete. (tool_check)

Red flags:
- [data_quality] Intake recorded the appliance make as 'Harbour Surveying' and categorised the fault as 'Heating & Hot Water'; the confirmed visit slot was logged with a date/time earlier than the calls that arranged it; pets field contradicts intake. → Recorded in the case note and in the office task; not relied on as fact.
- [data_quality] Provider invoice email summary gives a due date of 22 July 2026 for a February 2024 job and an amount that does not reconcile with the figure given to the landlord. → Invoice document requested via the office task; landlord warned the figure is unconfirmed.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "042", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Final-checks review of NBL-042. Authority: landlord's own a… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Job reference NBL-042 — Flat 20, 120 Alder Lane, Cedarford,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_tenant | completed | message=Dear Noah,  Job reference NBL-042 — Flat 20, 120 Alder Lane… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | create_human_task | completed | queue=property_management, title=NBL-042 closed before landlord confirmation; invoice figure…, summary=Flat 20, 120 Alder Lane, Cedarford. Washing machine not hea… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 7 | put_on_hold | completed | reason=Waiting for Landlord — confirmation of completion requested…, until=3 days from 2024-02-28 (landlord reply window) | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the washing machine repair at Flat 20, 120 Alder Lane is complete to your satisfaction, so the file can be closed? (blocking; Final check 'landlord_confirmation' was marked needed (event-030) but the ticket was closed a minute later (event-031) with no landlord reply on file.)
- Ask **contractor**: Please send the invoice document for NBL-042 showing the net amount and VAT — our record shows GBP 75.11 while the landlord was told £75 + VAT. (non-blocking; No invoice or photos on file (event-029); the two figures on record do not reconcile and the landlord must be billed the correct amount.)
- Ask **tenant**: Is the machine now heating correctly on 60°C and higher cycles after the engineer's visit? (non-blocking; No work result from the provider other than an invoice; the contractor was still chasing a booking on 27/02 (event-022).)

Promises made or recorded:
- agency → landlord: Send the verified provider invoice once the correct net/VAT figures are confirmed [open]
- agency → tenant: Re-open the job with the provider if the machine is still not heating [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
