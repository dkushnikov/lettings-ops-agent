# ANSWER — Case 017 — Case 017: Kitchen Extractor Fan Repair Request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Extractor fan "fault" was an unswitched isolator; tenant confirmed it works, landlord informed of nil cost, request closed without payment.
**Stage:** closed
**Last update:** 2026-09-21 03:42:31 UTC (event-014) · **Decided:** 2026-10-10 13:23 UTC
**Next step:** None — case closed; landlord to come back to us only if they want further checks (notified, ACT-1).

Definition of done (5/6 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (fault logged); event-003 acknowledged to tenant; routine — no emergency definition matched
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-008: landlord answered with a zero-cost workaround; no contractor instructed, so no spend authority needed
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider required — fault resolved by the landlord's switch advice (event-009, event-011)
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No visit required (event-011)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote — nil cost
- [x] work_result: Work result recorded from the provider — event-011: tenant confirms the extractor fan works after locating the switch
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No works carried out, so no photos or invoice exist; picture referenced at event-004 was unavailable
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-014 task completed without payment; landlord told of nil cost in ACT-1
- [x] landlord_confirmation: Landlord confirmed completion — ACT-1 outcome notice to landlord; landlord's own diagnosis at event-008 was the resolution
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued — no visit
- [x] closed: Request closed with a resolution that names who paid — ACT-3 close_request — resolution records no cost incurred

## 1. Decision

Closed the request as resolved at nil cost. The landlord's own reply supplied a zero-cost workaround (an isolator switch right of the hob), the agency relayed it to the tenant, and the tenant confirmed the extractor fan works. No contractor was needed, so no spend authority was engaged. I notified the landlord of the outcome and nil cost, logged the closure check, and closed the request as completed without payment.

Safety actions taken first:
- Checked all artefacts against the safety pass list: no mention of gas, burning smell, sparks, electrical fault, damp/mould, detectors or vulnerable occupants. Extractor fan was reported as a non-functioning appliance switch only, with no hazard indication (event-001, event-011) — emergency-hazard playbook not triggered.

Actions deliberately withheld:
- Did not instruct a contractor — no fault remains and no landlord spend authority is on file (APR-SPEND-OVER-CAP).
- Did not make any statement about who would have been liable for a call-out (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-CLOSE, RTE-LANDLORD, RTE-TENANT, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-CLOSE, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 11/09/2026 that the kitchen extractor fan does not turn on at Flat 1, 31 Juniper Mews, Cedarford, ZZ7 7ZZ. [index, event-001, get_case_details; high]
- F2: Agency acknowledged the report to the tenant on 13/09/2026 and asked the landlord on the same day whether to use their own contractor or an agency contractor. [event-003, event-004; high]
- F3: The landlord replied on 15/09/2026 that there is a switch to the right-hand side of the hob which needs to be switched on. [event-008; high]
- F4: The agency relayed the landlord's instruction to the tenant on 16/09/2026. [event-009, event-010; high]
- F5: The tenant confirmed on 16/09/2026 that the extractor fan works after locating the switch. [event-011; high]
- F6: No contractor was instructed and no cost was incurred; the agency recorded the task as completed without payment on 21/09/2026. [event-012, event-013, event-014, get_action_ledger; high]
- F7: No landlord spend cap or standing instruction is on file in the visible record; none was needed because the fix was at nil cost. [get_case_details, get_action_ledger; medium]

Conflicts between sources:
- Internal note event-013 names the tenant 'Clarke'; agency letters address the tenant as 'Clara' (event-003, event-009). Same ticket and address throughout. → Treated as a typo in an internal note; no name was copied into any party correspondence. Does not change the action. (source_hierarchy)

Red flags:
- [data_quality] Tenant reply at event-011 is written in the third person ('The customer confirms...'), which reads as a paraphrase rather than the tenant's own words; it arrived to the agency's own question on this ticket and names no other property, so it is taken as the tenant's answer. → Accepted as the tenant-owned answer per RTE-TENANT and recorded; no further confirmation sought.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "017", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_landlord | completed | message=Flat 1, 31 Juniper Mews, Cedarford, ZZ7 7ZZ — kitchen extra… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | add_note | completed | note=Closure check (maintenance-request DoD): fault = kitchen ex… | {"id": "ACT-2"} | CAP-LOG |
| 5 | close_request | completed | resolution=Kitchen extractor fan at Flat 1, 31 Juniper Mews, Cedarford… | {"id": "ACT-3"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Northbridge Lettings → Tenant: Contact the landlord about getting someone to attend the extractor fan [kept]
- Northbridge Lettings → Tenant: Close the job down [kept]
- Northbridge Lettings → Landlord: Outcome notice: fan working, no cost, request closed without payment [kept]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day deadline 2026-09-12
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
