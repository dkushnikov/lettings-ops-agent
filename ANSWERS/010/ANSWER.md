# ANSWER — Case 010 — Case 010: Solar panel readings photo request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Solar PV reading photo was already sent to the landlord and acknowledged; I recorded the next due date (15 Sept), diarised the next cycle and closed the request at no cost.
**Stage:** closed
**Last update:** 2025-01-17 06:06:30 UTC (event-015) · **Decided:** 2026-10-10 14:01 UTC
**Next step:** Property management admin to request a fresh dated solar meter photo from the tenant ahead of 15 September (task ACT-3); no action owed by any party before then.

Definition of done (5/5 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — index / get_case_details: categorised as a recurring administrative readings request, routine; no fault reported so no damage-limiting advice applies
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No spend or works; landlord's own standing request for readings (index) and reply event-015
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No contractor required (F6)
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No property access required (F6)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote; no cost
- [x] work_result: Work result recorded from the provider — event-013: meter photo supplied and forwarded; attachment-01 records the reading
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — attachment-01-photograph-of-a-solar-photovoltaic-generation-me.pdf on file and attached to event-013
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No chargeable work; closed without payment (ACT-4)
- [x] landlord_confirmation: Landlord confirmed completion — event-015: landlord confirmed receipt and set next date
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued
- [x] closed: Request closed with a resolution that names who paid — ACT-4 close_request — administrative request, no cost to either party

## 1. Decision

Treated as a routine administrative (non-repair) request. The visible history shows the photo was supplied and forwarded to the landlord (event-013) and the landlord confirmed receipt and named the next due date, 15 September (event-015) — a free-text landlord reply, which is the manual-mode trigger for this case. Nothing was outstanding that needed spend, access or a contractor, so no dispatch or approval route applied. I acknowledged the landlord, logged the data-quality points (the "mid June" label on a January email reusing the intake attachment; the call note attributing the photo promise to "a caller from Oakfield Compliance"), created an admin task to diarise the next reading before 15 September, and closed the request with no payment. Safety pass: the attachment's references to a solar PV "point of emergency switching" and a red isolator "marked I ON" are normal labelling, not a reported or observed fault — recorded as a check, not a hazard.

Safety actions taken first:
- Safety-pass check: attachment-01 mentions a solar PV 'point of emergency switching' and a red isolator 'marked I ON' — normal labelling of an in-service isolator; no electrical fault, sparks, burning smell or alarm issue is reported anywhere in the history, so no make-safe or escalation was required (recorded in ACT-1).

Actions deliberately withheld:
- Did not re-chase the tenant: the landlord has already confirmed receipt of the reading (event-015), so a further request now would duplicate work.
- Did not escalate: the open points are data-quality notes, not a decision a human must take today; they are carried into the September task.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-CLOSE, CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 10, 180 Alder Lane, Cedarford, ZZ3 4ZZ; the landlord requires a solar panel meter photo every 3 months. [index, get_case_details; high]
- F2: A photographic record of the solar PV generation meter for this address shows a display reading that 'appears to show 16845'. [attachment-01-photograph-of-a-solar-photovoltaic-generation-me; medium]
- F3: The agency emailed the tenant twice for the photo (2025-01-11, 2025-01-17) and a call note records a promise to send one. [event-006, event-010, event-008; high]
- F4: The agency sent the meter photo to the landlord on 2025-01-17, describing it as the reading 'for mid June'. [event-013; high]
- F5: The landlord replied thanking the agency for the reading and stating the next one is needed on 15th September. [event-015; high]
- F6: No repair, hazard, spend, contractor or property access is involved in this request at any point in the history. [index, event-001, event-014; high]

Conflicts between sources:
- Call note event-008 is logged as a call with the Tenant but describes the caller as being 'from Oakfield Compliance'; the record does not say who sent the image. → Did not change the action — the landlord has the reading and confirmed it; flagged in ACT-1 and in the next-cycle task ACT-3. (unresolved)

Red flags:
- [data_quality] event-013 forwarded the intake attachment to the landlord on 2025-01-17 described as the reading 'for mid June'; the image may not be a fresh reading for the period billed. Landlord accepted it (event-015). → Logged in ACT-1 and flagged in the September diary task (ACT-3); landlord invited to say if the image was unclear (ACT-2).
- [data_quality] Call note logged to the Tenant records 'the caller from Oakfield Compliance' as agreeing to send the photo; the sender's identity is not established, and the tenant email event-012 is a signature only with no attachment. → Recorded in ACT-1; next cycle to confirm the photo comes from the tenant.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "010", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Cycle complete. Solar PV meter photo (reading appears as 16… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Flat 10, 180 Alder Lane, Cedarford, ZZ3 4ZZ — solar panel r… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | create_human_task | completed | queue=property_management_admin, title=Diarise solar PV reading photo — Flat 10, 180 Alder Lane —…, summary=Landlord (event-015) states the next solar panel reading ph… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 6 | close_request | completed | resolution=Quarterly solar PV meter reading photo obtained and forward… | {"id": "ACT-4"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Agency → Landlord: Request a fresh dated solar meter photo from the tenant ahead of the next due date by 15 September [open]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge a party's reply within one working day
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
