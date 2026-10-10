# ANSWER — Case 026 — Case 026: Oven Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Oven element replaced and confirmed working; file reopened at final checks — invoice chased from provider, landlord asked to confirm, provider-identity conflict sent to the office.
**Stage:** final_checks · **Hold:** Waiting for Provider — invoice, job sheet and photos requested (3 working days, ACT-3); also Waiting for Landlord — completion confirmation requested (ACT-2).
**Last update:** 2025-09-08 19:13:14 UTC (event-038) · **Decided:** 2026-10-10 13:26 UTC
**Next step:** Provider to send the invoice (net/VAT/total) and job sheet within 3 working days (ACT-3); then forward to the landlord for confirmation (ACT-2) and the office to settle which provider invoices (ACT-4).

Definition of done (6/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (Appliances, ROUTINE); tenant acknowledged event-006
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 landlord's own email 'Yes go ahead'
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-012/event-014 provider instructed; event-013 tenant briefed
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-019 slot confirmed; date corrected to 8 Sept (event-023, event-025, event-028)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-030 'no quote needed'
- [x] work_result: Work result recorded from the provider — event-029 element replaced, oven working; event-031 moved to Result
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-034 skip reason recorded but does not cover job paperwork; invoice/job sheet/photos requested ACT-3
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — no forwarding event in history (search_history 'invoice' returns only event-029); landlord told invoice will follow ACT-2
- [ ] landlord_confirmation: Landlord confirmed completion — event-035 'Need confirmation from landlord'; requested ACT-2
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-037 keys return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-038 marked closed, but documents, invoice and landlord confirmation outstanding — not re-closed (CAP-CLOSE)

## 1. Decision

Repair is verifiably done (tenant confirmed the replaced oven element works, event-029), but the ticket was closed at event-038 with final checks outstanding: no invoice forwarded to the landlord and no landlord confirmation (event-035 still open). I did not re-close or re-dispatch. I chased the instructed provider for the invoice and job paperwork, asked the landlord to confirm completion, and raised an office task for the conflict between agency records about which provider holds the job (Keystone Compliance per event-014/018 vs "Riverside Works" event-016 / "Harbour Works" event-029 / "Lantern Utilities" event-020) — no provider was named to any party as the one who invoiced, and no payment was actioned.

Safety actions taken first:
- Safety pass: oven/hob are electric (event-002), fault limited to the main oven element, no gas appliance and no burning smell, sparks or alarm issue reported; element replaced and appliance confirmed working (event-029). No smoke/CO alarm question arises on this ticket.

Actions deliberately withheld:
- Did not re-close the request: invoice_to_landlord and landlord_confirmation are still pending (CAP-CLOSE).
- Did not dispatch or re-instruct any contractor: the work is done; a second work order would duplicate it.
- Did not state or approve any invoice amount (PRO-PAYMENTS; no figure in any artefact).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, ESC-CONFLICT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the main oven element not heating; grill element works; appliance is electric. [index, event-001, event-002; high]
- F2: Intake classified the issue as Appliances, severity ROUTINE. [event-002; high]
- F3: Landlord approved instructing a contractor: 'Yes go ahead' (26 Aug 2025). [event-009; high]
- F4: Agency instructed Keystone Compliance and briefed the tenant that they would attend. [event-012, event-013, event-014; high]
- F5: Appointment first set for 30/08/2025 10:00-12:00, then the tenant stated the provider had arranged 8 September; the agency told the tenant to take the provider's confirmed date. [event-017, event-018, event-019, event-021, event-023, event-025, event-028; high]
- F6: Work completed: heating element replaced, oven confirmed working by the occupant on 8 Sept 2025; hobs cleaned. [event-029; high]
- F7: No quote was required for the job. [event-030; high]
- F8: Document upload was skipped with the reason 'approved by landlord in activity notes'. [event-034; high]
- F9: 'Need confirmation from landlord' was flagged and no invoice forwarding to the landlord appears in the history; the request was nonetheless marked closed. [event-035, event-038, search_history; high]
- F10: No invoice amount appears anywhere in the record; the only reference is a call mentioning 'the invoice from Harbour Works'. [event-029, search_history; high]
- F11: Keys return confirmed at final checks. [event-037; medium]

Conflicts between sources:
- Provider identity: agency instruction and appointment confirmation name Keystone Compliance; a booking call names 'Riverside Works'; the closing call cites an invoice from 'Harbour Works'; the reminder SMS is signed 'Lantern Utilities'. → No side taken in any message to a party; invoice chased from the provider on the agency's own record (Keystone Compliance) and the conflict sent to the office (ACT-4) before any payment. (asked)
- Occupant/contact names are inconsistent across the history (Clara, Ruben Oakley, Grace Mercer, Harriet Fletcher, Leo). → Names from message bodies not copied into outgoing letters; flagged to the office for a tenancy-record check. (unresolved)
- Visit date: system recorded 30/08/2025 while the tenant stated 8 September with the provider. → Settled by events: attendance and completion occurred on 8 September (event-028, event-029). (source_hierarchy)

Red flags:
- [data_quality] Four different provider trading names and five different occupant names appear across the same ticket; the job was also closed with landlord confirmation and invoice forwarding outstanding. → Conflict recorded (ACT-1) and sent to the property_manager queue (ACT-4); no provider named to any party as the invoicing party; no payment actioned.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "026", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice | [{"event": "event-029", "timestamp": "2025-09-08 19:02:48 UTC", "channel": "Call", "from": "Agency / system", "to": "Tenant", "excerpt": "[2025-09-08 19:02:48… | allow |
| 4 | search_history | completed | from_party=Landlord | [{"event": "event-009", "timestamp": "2025-08-26 17:28:53 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2025-08-26 17:28:… | allow |
| 5 | add_note | completed | note=Final-checks review. Work result: tenant confirmed oven wor… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_landlord | completed | message=Re: Flat 3, 3 Willowmere Road, Alderwick, ZZ9 6ZZ — oven re… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_contractor | completed | message=Re: Oven Repair Request — Flat 3, 3 Willowmere Road, Alderw… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | create_human_task | completed | queue=property_manager, title=Case 026 oven repair: provider identity conflict + ticket c…, summary=Flat 3, 3 Willowmere Road. Repair done (element replaced; t… | {"id": "ACT-4"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **contractor**: Please send the invoice (net, VAT, total), job sheet/engineer's notes and any photos for the oven element replacement at Flat 3, 3 Willowmere Road on 8 September 2025, and confirm the trading name that will appear on the invoice. (blocking; Documents and invoice are required before the file can be closed; agency records disagree on the provider's trading name.)
- Ask **landlord**: Please confirm you are happy the oven works are complete; the invoice will follow as soon as the provider supplies it. (blocking; event-035 'Need confirmation from landlord' is still outstanding and no invoice has been forwarded.)

Promises made or recorded:
- agency → landlord: Forward the provider's invoice once received and chase if no reply within 3 working days by 3 working days from ACT-2 [open]
- contractor → agency: Send invoice, job sheet and photos, and confirm invoicing trading name by 3 working days from ACT-3 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report (26 Aug 2025)
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
