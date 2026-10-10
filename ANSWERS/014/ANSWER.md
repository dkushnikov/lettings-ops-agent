# ANSWER — Case 014 — Case 014: Front Door Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Front door sticking/wobbling; landlord's key-latch workaround works for the tenant, contractor visit deferred to July and diarised; closed without payment.
**Stage:** closed_without_payment
**Last update:** 2024-06-07 21:45:09 UTC (event-016) · **Decided:** 2026-10-10 13:22 UTC
**Next step:** Office (property_management queue) to action the July 2024 diary task: ask the landlord to confirm the deferred front-door inspection and approve a priced quote, or confirm he is using his own contractor — unless the tenant reports a recurrence sooner.

Definition of done (5/6 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-004 fault described (door and frame wobble, has to be slammed); urgency set routine at use_playbook; damage-limiting advice and escalation triggers given to tenant at ACT-2
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-005 asked the landlord; event-010 landlord replied — workaround now, contractor next month. No spend authorised and none incurred.
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord deferred the inspection to July 2024 (event-010); no provider instructed, no standing cap on file (APR-SPEND-OVER-CAP). Diarised at ACT-3.
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No visit instructed; tenant told no appointment is booked yet (ACT-2)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote sought — work deferred by the landlord (event-010)
- [n/a] work_result: Work result recorded from the provider — No works carried out; fault managed by the landlord's workaround (event-012)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No attendance, no invoice or photos to upload — nothing instructed (event-010, event-015)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-015 request marked completed without payment; no cost to pass on
- [x] landlord_confirmation: Landlord confirmed completion — event-013 agency update to landlord; event-016 landlord acknowledged
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; no visit took place
- [x] closed: Request closed with a resolution that names who paid — event-014/event-015 closed by Ava as completed without payment — no party paid, as no work was instructed

## 1. Decision

No response to the landlord is required and no contractor is instructed. The landlord owns this decision and has already made it: a zero-cost workaround now (event-010), with a contractor inspection deferred to next month. The workaround was relayed to the tenant and confirmed working (event-011, event-012); the landlord was updated (event-013) and acknowledged (event-016). The agency completed the request without payment (event-015). I added the missing pieces within my authority: the tenant has been told a visit is intended but not yet booked and given the triggers that would make it urgent (ACT-2), and the landlord's July inspection promise has been diarised to the office so it is not lost (ACT-3). I did not dispatch: no standing spend cap is on file and the landlord's message defers the work rather than approving a priced job (APR-SPEND-OVER-CAP).

Safety actions taken first:
- Confirmed the property is securable: tenant can close and lock the front door using the key/latch method (event-012), so no insecure-property emergency applies.
- Gave the tenant named deterioration triggers that would re-open the case as urgent (ACT-2).
- Recorded the glass-shatter risk in the office diary task covering the deferred July inspection (ACT-3).

Actions deliberately withheld:
- Did not instruct a joiner/locksmith: no standing spend cap on file and the landlord's message defers rather than approves a job (APR-SPEND-OVER-CAP, PRO-INSTRUCTIONS-FROM-CONTENT).
- Did not re-ask the landlord for approval: he has already answered the agency's question (event-010) and acknowledged the outcome (event-016).
- Did not re-ask the tenant to confirm the workaround: already confirmed at event-011 and event-012.
- Did not escalate: the deferral is the landlord's decision to make, the property is secure, and no liability, legal or fraud issue arises.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the front door has to be slammed to shut and that the fridge-freezer contractor said it would "cause a shatter in glass" and would report it himself. [index, event-001; high]
- F2: Follow-up call recorded that the door frame and door "literally wobble" when shutting. [event-004; high]
- F3: Agency asked the landlord for authority to send someone out and placed the case on hold waiting for the landlord. [event-005, event-007; high]
- F4: Landlord replied with a zero-cost workaround — put the key in to lift the latch, then close the door — and asked that a contractor look at it next month. [event-010; high]
- F5: The workaround was relayed to the tenant by phone; she had already used it that morning, it worked, and she agreed to monitor and report any recurrence. [event-011, event-012; high]
- F6: The landlord was updated that the workaround succeeded and the case would be closed, and he acknowledged; the request was marked completed without payment. [event-013, event-015, event-016; high]
- F7: No landlord standing spend cap is on file in this case record, so there is no standing authority to spend. [get_case_details; medium]
- F8: The door can be closed and secured using the landlord's method; no report of the property being left insecure. [event-012; medium]

Conflicts between sources:
- AI intake classified the issue as "Appliances" and asked fridge/freezer clarifying questions, while the tenant's text and all later events describe a front door fault. → The tenant's own words and the agency's follow-up note govern: the case is a front door repair, classified routine. Noted at ACT-1. (source_hierarchy)
- Untrusted landlord-channel email (event-009) is a third-person system summary mentioning a workaround and a visit next month; the landlord's actual words appear at event-010. → Acted on the landlord's own message (event-010); the summary line was treated as evidence only. (source_hierarchy)

Red flags:
- [data_quality] Intake misclassification: issue logged as "Appliances" with fridge/freezer questions (all unanswered) for what is a front door fault; risk of the job being routed to the wrong trade. → Corrected the classification in the case record and set urgency routine (ACT-1); priority left at 7, not decreased (event-008).
- [safety_hazard] A contractor's reported view, quoted by the tenant, that the wobbling door could "cause a shatter in glass"; the inspection is deferred by a month. Not an emergency — the door still closes and locks using the landlord's method (event-012) — but a residual risk while deferred. → Tenant given explicit triggers to report immediately (lock failure, worsening wobble, cracked or loose glass) at ACT-2; risk recorded in the July diary task to the office (ACT-3).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "014", "attachments_hidden": 0} | allow |
| 2 | add_note | completed | note=Status review (manual-mode trigger: free-text landlord repl… | {"id": "ACT-1"} | CAP-LOG |
| 3 | notify_tenant | completed | message=Address: Flat 12, 52 Meadow Row, Kingshaven, ZZ9 5ZZ  Thank… | {"id": "ACT-2"} | CAP-NOTIFY |
| 4 | create_human_task | completed | queue=property_management, title=Diary July 2024: front door inspection promised by landlord…, summary=Case 014 was completed without payment (event-015) after th… | {"id": "ACT-3"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 014: The record carries red flags that need a human's confirmation (safety_hazard: A contractor's reported view, quoted by the tenant, that the wobbling door could "cause a shatter in glass"; the inspection is deferred by a month. Not an emergency — the door still closes and locks using the landlord's method (event-012) — but a residual risk while deferred.); the case cannot end as resolved.
**Facts (≤5):**
- A contractor's reported view, quoted by the tenant, that the wobbling door could "cause a shatter in glass"; the inspection is deferred by a month. Not an emergency — the door still closes and locks using the landlord's method (event-012) — but a residual risk while deferred.
**Gap:** The record carries red flags that need a human's confirmation (safety_hazard: A contractor's reported view, quoted by the tenant, that the wobbling door could "cause a shatter in glass"; the inspection is deferred by a month. Not an emergency — the door still closes and locks using the landlord's method (event-012) — but a residual risk while deferred.); the case cannot end as resolved.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- Landlord → Agency/tenant: Have a contractor look at the front door next month (July 2024) by July 2024 [open]
- Tenant → Agency: Continue using the key/latch method and report if the door becomes an issue again [open]
- Agency → Tenant: Contact the tenant to arrange a window once a visit is instructed; treat a lock failure, worsening wobble or cracked glass as urgent [open]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day deadline 2024-06-07
- CLK-S11 [in_force]: Repair within a reasonable time once reported

## System notes

- reviewer: R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
