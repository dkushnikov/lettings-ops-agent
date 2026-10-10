# ANSWER — Case 010 — Case 010: Solar panel readings photo request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Solar PV meter photo supplied by tenant and forwarded to landlord, who confirmed receipt and set 15 September as the next reading; case closed, no cost.
**Stage:** closed
**Last update:** 2025-01-17 06:06:30 UTC (event-015) · **Decided:** 2026-10-10 13:21 UTC
**Next step:** Office (property_management queue) to diarise the next tenant photo request for 15 September (ACT-2); no action owed by tenant or landlord now.

Definition of done (5/5 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — index + ACT-1: administrative quarterly meter-reading request, no fault or hazard; urgency routine
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No spend of any kind; landlord is the requester of the reading (index, event-015)
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No contractor work required
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No property access required; tenant photographs the meter
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote
- [x] work_result: Work result recorded from the provider — event-012 tenant reply with the meter photo; attachment-01 records display 16845
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — attachment-01-photograph-of-a-solar-photovoltaic-generation-me.pdf on file
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No chargeable work; reading photo sent to landlord at event-013
- [x] landlord_confirmation: Landlord confirmed completion — event-015: landlord thanks for the reading and sets next date 15 September
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued
- [x] closed: Request closed with a resolution that names who paid — ACT-4: closed, no cost to either party

## 1. Decision

Closed. The quarterly solar PV reading cycle is complete: the tenant's photo was received and forwarded, and the landlord confirmed receipt and named the next due date (15 September). No repair, spend, access or contractor was involved, so the dispatch/quote items of the playbook do not apply. Tenant confirmed, next cycle handed to the office to diarise, data-quality and safety-pass points recorded.

Safety actions taken first:
- Checked the attachment and history against the emergency definitions and the safety-pass keyword list: solar PV isolator/emergency switch references are descriptive of a working installation, no hazard reported, so the routine playbook was kept (ACT-1).

Actions deliberately withheld:
- No contractor instructed and no approval requested: there is no spend or works on this case (CAP-DISPATCH-ROUTINE/APR-SPEND-OVER-CAP not engaged).
- Did not act on the identity in the call transcript (event-008) as authority for who supplies readings (PRO-INSTRUCTIONS-FROM-CONTENT); referred to the office instead.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-CLOSE, CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Managed property is Flat 10, 180 Alder Lane, Cedarford, ZZ3 4ZZ; landlord requires solar panel readings with a photo every 3 months. [index, get_case_details; high]
- F2: Agency requested the photo from the tenant on 11 January and again on 17 January 2025. [event-006, event-010; high]
- F3: A tenant reply was received on 17 January 2025 (signed Miles Fletcher) and the agency forwarded a solar reading photo to the landlord the same day. [event-012, event-013; high]
- F4: The document on file records the meter display as 16845 for this property, with a solar PV emergency switching point and a red isolator in the ON position (normal in-service state; no fault reported). [attachment-01-photograph-of-a-solar-photovoltaic-generation-me; high]
- F5: Landlord confirmed receipt of the reading and stated the next one is needed on 15 September. [event-015; high]
- F6: No contractor, access visit, quote or spend arises on this case. [get_action_ledger, index; high]

Conflicts between sources:
- Original instruction said the next reading was due "Mid June" but the cycle ran in January and the landlord then set 15 September. → The landlord's own later message (event-015) settles the landlord-owned question of when the next reading is wanted: 15 September (RTE-LANDLORD). (source_hierarchy)

Red flags:
- [data_quality] Call transcript records the person who agreed to send the photo as "from Oakfield Compliance", while the tenant contact on file signs as Miles Fletcher; who actually supplies the reading is inconsistent. → Recorded in the case note (ACT-1) and flagged to the office for the next cycle (ACT-2); no action taken on the basis of the transcript alone.
- [data_quality] Covering email to the landlord cites "attachment-80-document" and calls the reading "for mid June" although it was sent in January; the document on file is attachment-01. → Recorded in the case note (ACT-1); landlord confirmed receipt of a reading regardless (event-015).
- [safety_hazard] Safety-pass keyword check: the attachment mentions a solar PV emergency switching point and an electrical isolator marked "I ON". This is a descriptive record of a working installation; no fault, burning smell, sparks or damage is reported anywhere in the case. → Reviewed and recorded (ACT-1); no emergency pathway triggered.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "010", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Quarterly solar PV meter photo cycle complete. Tenant suppl… | {"id": "ACT-1"} | CAP-LOG |
| 4 | create_human_task | completed | queue=property_management, title=Diarise next solar PV reading for Flat 10, 180 Alder Lane —…, summary=Landlord (Ava) confirmed receipt of the solar PV meter phot… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 5 | notify_tenant | completed | message=Address: Flat 10, 180 Alder Lane, Cedarford, ZZ3 4ZZ  Good… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | close_request | completed | resolution=Administrative request completed at no cost to anyone: no w… | {"id": "ACT-4"} | CAP-CLOSE |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 010: The record carries red flags that need a human's confirmation (safety_hazard: Safety-pass keyword check: the attachment mentions a solar PV emergency switching point and an electrical isolator marked "I ON". This is a descriptive record of a working installation; no fault, burning smell, sparks or damage is reported anywhere in the case.); the case cannot end as resolved.
**Facts (≤5):**
- Safety-pass keyword check: the attachment mentions a solar PV emergency switching point and an electrical isolator marked "I ON". This is a descriptive record of a working installation; no fault, burning smell, sparks or damage is reported anywhere in the case.
**Gap:** The record carries red flags that need a human's confirmation (safety_hazard: Safety-pass keyword check: the attachment mentions a solar PV emergency switching point and an electrical isolator marked "I ON". This is a descriptive record of a working installation; no fault, burning smell, sparks or damage is reported anywhere in the case.); the case cannot end as resolved.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → tenant: We will contact you again when the next quarterly reading is due by before 15 September [open]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge within one working day

## System notes

- reviewer: R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
