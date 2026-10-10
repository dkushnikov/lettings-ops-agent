# ANSWER — Case 011 — Case 011: Dishwasher Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Dishwasher repair closed with invoice and landlord confirmation unevidenced; chased provider, landlord and tenant, referred premature closure to the office.
**Stage:** final_checks · **Hold:** Waiting for Provider — Oakfield Homes to supply completion confirmation and invoice (3 working days from ACT-2); in parallel Waiting for Landlord for confirmation of completion (3 days from ACT-4).
**Last update:** 2026-12-13 05:45:21 UTC (event-032) · **Decided:** 2026-10-10 13:21 UTC
**Next step:** Oakfield Homes to send written completion confirmation, invoice and photos within 3 working days (ACT-2); invoice then to be forwarded to the landlord for confirmation before closure can stand.

Definition of done (5/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 — categorised Appliances/dishwasher not completing cycle, severity ROUTINE, containment step (photograph the appliance) given to the tenant
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 — landlord's own email 'Yes please go ahead' authorising a contractor visit
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-011/event-013 — Oakfield Homes instructed and briefed; event-012 — tenant told who is attending
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-018 — tenant agreed appointment for the following morning; event-025 — follow-up visit arranged for 12–5
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-020 quote £95 incl. parts, labour and VAT put to landlord; event-022 landlord's own reply 'Please go ahead' before the repair visit
- [ ] work_result: Work result recorded from the provider — Only system lines event-026/event-027 assert completion; event-028/event-029 are blank and no provider completion report exists — chased at ACT-2
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-030 records documents skipped with reason 'Invoice uploaded. The invoice is unavailable.' — no invoice or photos on file; requested at ACT-2
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice held, so none forwarded; landlord told at ACT-4 it will be forwarded on receipt
- [ ] landlord_confirmation: Landlord confirmed completion — event-031 'Need confirmation from landlord'; no landlord message after event-022 — asked at ACT-4
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provided access in person (event-018, event-025)
- [ ] closed: Request closed with a resolution that names who paid — event-032 closed the request, but the resolution names no payer and three checks above are unevidenced; reopening referred to the office at ACT-5. I did not re-close.

## 1. Decision

The request was marked closed (event-032) while two of the playbook's final checks were unevidenced: no invoice on file or forwarded (event-030) and no landlord confirmation (event-031 is followed by closure 56 seconds later, with no landlord message after event-022). Landlord authority for the spend is sound (event-009 to instruct; event-022 approving the £95 incl. VAT quote), so no new approval is needed and no further dispatch is warranted. I did not re-close or re-dispatch. I chased the instructed provider (Oakfield Homes, per the agency's own record at event-011/event-013) for completion confirmation, invoice and photos; asked the landlord to confirm completion and told them the invoice will be forwarded; asked the tenant to confirm the fault is cured; logged the gap and the provider-name discrepancy; and referred the premature closure and the provider identity question to the office (ACT-5). The case now waits on named parties, so it ends with request_info rather than an escalation.

Safety actions taken first:
- Checked the report against the emergency definitions: appliance fault only, water confined to the dishwasher base and removed by the provider (event-019), no water near electrics, no loss of essential service, no vulnerability disclosed — emergency-hazard playbook not triggered.
- Tenant advised not to attempt any repair themselves (ACT-3).

Actions deliberately withheld:
- Did not re-dispatch or raise a second work order — the job is already instructed (event-023) and a duplicate order is barred by the playbook.
- Did not re-close the request: three final checks are unevidenced (CAP-CLOSE).
- Did not approve, settle or acknowledge any invoice amount (PRO-PAYMENTS).
- Did not pass the occupant's pet or household details beyond what the existing provider brief already contains (PRO-PII).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-DISPATCH-APPROVED, RTE-CONTRACTOR, RTE-LANDLORD, RTE-TENANT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-PII, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Amelia Nolan reported on 29 Nov 2026 that the dishwasher at Flat 12, 78 Copperfield Walk fills and washes but never ends its cycle; started recently. [index, event-001, event-002; high]
- F2: Agency intake classified the issue as ROUTINE — no loss of essential service, no hazard. [event-002; high]
- F3: Landlord authorised instructing a contractor on 3 Dec 2026 ('Yes please go ahead'). [event-009; high]
- F4: Oakfield Homes was assigned and briefed on 6 Dec 2026; the tenant was told they would attend. [event-011, event-012, event-013; high]
- F5: Provider reported on 7 Dec 2026: water in the base removed, loose connection from the flow-through heater tightened and retested, appliance running as it should; a missing dial needs replacing, quoted £95 including parts, labour and VAT, parts to be ordered. [event-019; high]
- F6: Landlord approved the £95 incl. VAT quote on 7 Dec 2026 and the provider was instructed to proceed the same day. [event-022, event-023; high]
- F7: No invoice is on file: the document step was skipped with the reason 'Invoice uploaded. The invoice is unavailable.' [event-030; high]
- F8: The system flagged 'Need confirmation from landlord' at 05:44:25 and closed the request at 05:45:21 on 13 Dec 2026; no landlord message appears after event-022. [event-031, event-032; high]
- F9: Completion is asserted only by system status lines; the two provider notes of 13 Dec carry no text. [event-026, event-027, event-028, event-029; high]
- F10: Access was arranged directly between provider and tenant; tenant agreed a morning slot on 6 Dec and a 12–5 slot for the parts visit on 9 Dec. [event-018, event-025; medium]
- F11: No landlord standing spend cap is on file in this case record; authority for the £95 rests on the landlord's own messages. [get_case_details, event-009, event-022; medium]

Conflicts between sources:
- Provider identity: the agency record instructs Oakfield Homes and the quote is signed 'Ashford, Oakfield Homes', while untrusted call summaries name 'Ashford at Cedar Maintenance' and an 'Alder Maintenance' line for a 'Ruben Kendall', and the intake summary calls it 'the Riverside Services dishwasher'. This changes who is chased and who is paid. → Acted on the agency's own record (Oakfield Homes, event-013) for the chase; discrepancy referred to the office at ACT-5 and no party was told which firm is 'wrong'. (asked)
- Record of completeness: system line event-032 states all checks are complete, while event-030 (no invoice) and event-031 (landlord confirmation needed) show otherwise. → The specific lines about the missing invoice and the outstanding landlord confirmation beat the general closure statement; those items are reported as pending. (source_hierarchy)

Red flags:
- [data_quality] Three different contractor names appear across untrusted transcripts and the intake summary alongside the instructed provider Oakfield Homes; one transcript also reports a call that could not be connected. → Logged at ACT-1 and referred to the office at ACT-5; chased only the provider named on the agency record.
- [data_quality] Closure recorded with the invoice unavailable, two blank provider notes and no landlord confirmation — the ticket's own checks contradict its closure. → Pending items reported; reopening decision referred to the office (ACT-5); no re-closure by me.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "011", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Post-closure review. Closed at event-032 with two final che… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_contractor | completed | message=Re: Flat 12, 78 Copperfield Walk, Kingshaven, ZZ3 1ZZ — dis… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_tenant | completed | message=Dear Amelia Nolan,  Re: Flat 12, 78 Copperfield Walk, Kings… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Address: Flat 12, 78 Copperfield Walk, Kingshaven, ZZ3 1ZZ… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | create_human_task | completed | queue=property_management, title=Case 011 closed with final checks unevidenced — invoice mis…, summary=Flat 12, 78 Copperfield Walk — dishwasher repair. Closed at… | {"id": "ACT-5"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **contractor**: Please confirm in writing that the dishwasher repair at Flat 12, 78 Copperfield Walk (replacement dial fitted, appliance retested) is complete, give the date of the completing visit, and send your invoice, any site photos, and the final amount if it differs from the £95 incl. VAT quoted. (blocking; Work result and invoice are required final checks; the provider's last substantive message is the quote at event-019 and event-030 records the invoice as unavailable.)
- Ask **landlord**: Do you consider the dishwasher repair complete and to your satisfaction, or have you been invoiced directly by the contractor? (blocking; event-031 flagged that landlord confirmation was needed; the ticket was closed at event-032 without any landlord reply after event-022.)
- Ask **tenant**: Is the dishwasher now completing its cycle normally, and has the replacement dial been fitted? (non-blocking; Independent confirmation that the reported fault is cured; the only record of the second visit is an untrusted call summary (event-025).)

Promises made or recorded:
- agency → landlord: Forward the contractor's invoice as soon as it is received by on receipt of the invoice [open]
- agency → contractor: Chase again and refer to the property manager if no reply within 3 working days by 3 working days from ACT-2 [open]
- agency → tenant: Arrange a further visit if the dishwasher is still not completing its cycle [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- CLK-SOP-ACK [sop]: Provider reply window on the invoice chase deadline 3 working days from ACT-2
