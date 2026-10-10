# ANSWER — Case 017 — Case 017: Kitchen Extractor Fan Repair Request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Kitchen extractor fan was not faulty — isolator switch by the hob; tenant confirmed it works. Landlord informed, request closed without payment.
**Stage:** closed
**Last update:** 2026-09-21 03:42:31 UTC (event-014) · **Decided:** 2026-10-10 14:03 UTC
**Next step:** None — case closed; landlord may reply to the completion notice (no action required of any party).

Definition of done (5/6 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 fault logged; event-003 acknowledged to tenant; routine — no hazard, no essential service lost
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-008 landlord answered with a zero-cost workaround; no contractor instructed, so no spend authority needed
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider required — fault resolved by tenant operating the hob-side switch (event-011)
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No visit required (event-011)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote — no chargeable work
- [x] work_result: Work result recorded from the provider — event-011 tenant confirms extractor fan working; event-013 internal note records the same
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No works carried out, so no photos or invoice exist; picture referenced at event-004 was unavailable
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-014 completed without payment; reason recorded (no works, no cost) in ACT-1 and ACT-3
- [x] landlord_confirmation: Landlord confirmed completion — event-008 landlord's instruction resolved the fault; completion notice sent to landlord ACT-2
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued — no visit took place
- [x] closed: Request closed with a resolution that names who paid — ACT-3 close_request; resolution states no cost incurred (completed without payment)

## 1. Decision

Closed as resolved at no cost. The landlord's own reply (event-008) supplied a zero-cost workaround, which was relayed to the tenant (event-009) and confirmed working by the tenant (event-011). No contractor, spend, access or documents arise, so no approval route (APR-ALWAYS-ASK / APR-SPEND-OVER-CAP) was triggered. I notified the landlord of the outcome and closed the request as completed without payment.

Safety actions taken first:
- Safety pass applied: no hazard reported or observed — no gas smell, burning smell, sparks, water near electrics, damp/mould or alarm failure anywhere in the artefacts. Extractor fan is ventilation only and is confirmed operating (event-011); no emergency definition engaged, so maintenance-request was the correct playbook.

Actions deliberately withheld:
- Did not instruct a contractor — no fault remains and there is no spend authority on file (APR-SPEND-OVER-CAP would apply).
- Did not message the tenant again — event-012 already told them the job is being closed; re-asking a question the history answers is prohibited by rule 2.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-CLOSE, RTE-LANDLORD, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-CLOSE, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 2026-09-11 that the kitchen extractor fan does not turn on at Flat 1, 31 Juniper Mews, Cedarford, ZZ7 7ZZ. [index, event-001, get_case_details; high]
- F2: Agency acknowledged the report to the tenant on 2026-09-13 and asked the landlord on the same day whether to use their own or an agency contractor. [event-003, event-004; high]
- F3: The landlord replied that there is a switch to the right-hand side of the hob which needs to be switched on. [event-008; high]
- F4: The agency relayed the landlord's instruction to the tenant on 2026-09-16. [event-009, event-010; high]
- F5: The tenant confirmed the extractor fan works after locating the switch; no contractor was instructed and the task was recorded as completed without payment. [event-011, event-012, event-013, event-014; high]
- F6: No landlord standing spend cap is on file in this case record; none was needed because no spend arose. [get_case_details, get_action_ledger; medium]

Red flags:
- [data_quality] Tenant is addressed as 'Clara' in agency correspondence but an internal note names 'Clarke'; names in message bodies were not copied into any outgoing letter. → Recorded in case note ACT-1; correspondence used the case record only.
- [data_quality] Picture attachment referenced in the landlord email was unavailable, so the visual evidence of the fault could not be reviewed. → Noted; immaterial as the tenant confirmed the fan operates.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "017", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Review of visible history: fault = kitchen extractor fan no… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Flat 1, 31 Juniper Mews, Cedarford, ZZ7 7ZZ — kitchen extra… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | close_request | completed | resolution=Kitchen extractor fan at Flat 1, 31 Juniper Mews, Cedarford… | {"id": "ACT-3"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Northbridge Lettings → Tenant: Contact the landlord about getting someone to attend the extractor fan [kept]
- Northbridge Lettings → Tenant: Close the job down [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
