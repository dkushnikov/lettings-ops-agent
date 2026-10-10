# ANSWER — Case 049 — Case 049: Shed Door Repair Request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Shed door sagging at Flat 13, 103 Meadow Row: tenant fixed it themselves under the landlord's approval; landlord told of nil cost and request closed without payment.
**Stage:** closed
**Last update:** 2024-03-16 23:34:45 UTC (event-014) · **Decided:** 2026-10-10 14:13 UTC
**Next step:** None — case closed; if the door worsens the tenant reports again and the landlord is asked before any trade is instructed (owner: tenant/landlord on a new report).

Definition of done (6/7 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 AI intake: Structural, ROUTINE; tenant states door closes when lifted (event-001). No emergency definition met; no damage-limiting advice needed beyond the tenant's own workaround.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 landlord email approving tenant self-fix, contractor otherwise; relayed to tenant at event-008.
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider required — tenant carried out the fix under the landlord's approval (event-007, event-013).
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No contractor visit needed (event-013).
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No spend; no quote obtained (event-014 completed without payment).
- [x] work_result: Work result recorded from the provider — event-013 'Tenats have completed the job themselves'.
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No contractor attendance, so no photos or invoice exist; skip reason recorded in ACT-2.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-014 task completed without payment; nil-cost position confirmed to the landlord in ACT-1.
- [x] landlord_confirmation: Landlord confirmed completion — Landlord's approval of the self-fix route at event-007; completion and nil cost notified to the landlord at ACT-1 — no further decision is outstanding with them.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; no visit took place.
- [x] closed: Request closed with a resolution that names who paid — ACT-3 close_request — resolution states nobody was charged.

## 1. Decision

Closed the request as completed without payment. The repair was a routine, non-emergency outbuilding fault; the landlord's own email (event-007) authorised the tenant to fix it themselves with a contractor as the fallback, the agency relayed that to the tenant (event-008), and the tenant completed the work (event-013). No contractor, quote, invoice or keys were involved, so those checklist items are not applicable. I informed the landlord of completion and nil cost (ACT-1), recorded the review note (ACT-2) and closed (ACT-3).

Safety actions taken first:
- Safety pass run over all artefacts: no gas, electrical, detector/alarm, damp/mould, asbestos, injury or vulnerable-occupant keywords present; the fault is an outbuilding door, so dwelling security under the emergency definitions is unaffected (event-001, event-002). No hazard reported or observed, so no safety red flag raised.

Actions deliberately withheld:
- Did not instruct a contractor: unnecessary once the tenant completed the repair (event-013), and the landlord's approval was conditional on the tenant being unable to do it (event-007).
- Did not state or decide who is liable for any future repair cost (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-CLOSE, CAP-DISPATCH-APPROVED, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-CLOSE, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 13, 103 Meadow Row, Bellmere, ZZ3 7ZZ; reporter is the tenant. [index, get_case_details; high]
- F2: Fault reported 2024-03-05: shed door sagging, closes if lifted from the bottom; tenant content to lift it but reported it in case it worsens. [event-001; high]
- F3: AI intake categorised the issue as Structural, severity ROUTINE, medium confidence; tenant confirmed no ceiling sagging, no access constraints, no pets. [event-002; high]
- F4: Agency asked the landlord on 2024-03-06 whether the tenant should do it or a contractor should attend. [event-004; high]
- F5: Landlord replied the same day approving the tenant to fix the door if able, otherwise assign a contractor. [event-007; high]
- F6: Agency relayed the landlord's decision to the tenant and asked them to say if they could not do it. [event-008; high]
- F7: Agency chased the tenant on 2024-03-14 and the case was held for a tenant reply. [event-011, event-012; high]
- F8: On 2024-03-16 the agency recorded that the tenants completed the job themselves and the task was completed without payment. [event-013, event-014; high]
- F9: No spend was incurred and no contractor was instructed on this ticket. [event-014, get_action_ledger; high]

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "049", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_landlord | completed | message=Address: Flat 13, 103 Meadow Row, Bellmere, ZZ3 7ZZ  Update… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | add_note | completed | note=Case 049 review before closure. Routine, non-emergency: she… | {"id": "ACT-2"} | CAP-LOG |
| 5 | close_request | completed | resolution=Shed door (sagging, lifted to close) at Flat 13, 103 Meadow… | {"id": "ACT-3"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Northbridge Lettings → Tenant: If the tenant cannot fix the door themselves, the agency will instruct a contractor [superseded]
- Northbridge Lettings → Landlord: No trade will be instructed without coming back to the landlord if the door deteriorates again [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
