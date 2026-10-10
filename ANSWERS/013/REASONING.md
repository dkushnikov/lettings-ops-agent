# REASONING — Case 013

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (email, untrusted), event-002 (email, informational), event-003 (email, informational), event-004 (email, informational), event-005 (note, informational), event-006 (email, informational), event-007 (email, informational), event-008 (email, informational), event-009 (email, informational), event-010 (email, untrusted), event-011 (email, informational), event-012 (note, informational), event-013 (email, informational), event-014 (email, untrusted), event-015 (email, informational), event-016 (call_transcript, informational), event-017 (email, informational), event-018 (email, untrusted), event-019 (email, informational), event-020 (email, informational), event-021 (call_transcript, informational), event-022 (note, informational), event-023 (note, informational), event-024 (note, informational), glazing-invoice (document, informational)

Facts and their sources:
- F1 [high] Tenant reported misting between the kitchen glazing panes, water gathering around the frame, a cold kitchen and concern about damp; the sash opens, closes and locks; pets at the property. ← index, event-001
- F2 [high] No emergency definition is met: the window is secure and operable, no heating loss, no water near electrics, no gas or electrical fault; report made 31/07 (outside cold months). ← index, event-001
- F3 [high] Quote stated to the landlord as £150 plus VAT, £180 total. ← event-009, event-011
- F4 [high] Landlord Orren Vale replied in his own message that he was happy to use the contractor if £180 was the total value of the quote — approval on file for £180 incl. VAT, matching the quoted figure. ← event-010
- F5 [high] Tenant offered any time on 24, 25 or 26 August and asked to be present; the contractor never selected a slot and no appointment was ever confirmed. ← event-014, event-015, event-017
- F6 [high] On 24/08 the contractor said the glass had been ordered with no delivery estimate; on 02/09 she said it had still not arrived and she could not estimate delivery. ← event-018, event-021
- F7 [high] On 09/09 the case was moved to 'awaiting post-visit documents' with no messages sent, no appointment confirmation and no visit report on file. ← event-022
- F8 [high] An invoice dated 10/09/2025, ref NBL-013-INV-09, for 'Supply and fit 1 pane of glass to the kitchen glazing' was uploaded; the copy held states 'Amount: —', i.e. no figure. ← event-023, event-024, glazing-invoice
- F9 [high] No site assessment or diagnosis of the wider damp or cold concern is recorded; the 04/08 authorisation covered obtaining a glazing price only. ← event-005
- F10 [high] Tenant report acknowledged the same working day (31/07 08:30), satisfying the acknowledgement SOP. ← event-002

Conflicts and how they were handled:
- The case status and the uploaded invoice assert the work was supplied and fitted, while the messaging record shows no confirmed appointment and the glass still undelivered on 02/09 — eight days before the invoice date. → Not resolved from the file. Asked the contractor for the attendance date and a priced invoice, and the tenant whether anyone attended (ACT-2, ACT-3). Invoice withheld from the landlord for payment pending the answer (ACT-4). (asked; sources event-021, event-022, event-023, glazing-invoice)

Uncertainty acknowledged:
- Whether the glazing has in fact been fitted is unknown: the invoice says supplied and fitted, the messaging record shows no attendance and undelivered glass on 02/09.
- The invoice amount is unknown — the copy on file shows 'Amount: —', so it cannot be reconciled with the approved £180.
- Whether damp or mould has actually developed at the frame is unknown; no site assessment has ever been carried out (event-005).

Assumptions made:
- Assumption: the landlord's conditional approval at event-010 ('happy if £180 is the total') is satisfied by the quote of £150 plus VAT = £180 total (event-009, event-011), so no fresh approval is needed for the original scope. Any invoice above £180 incl. VAT, or any additional work arising from the damp/frame check, would need a new landlord approval under RTE-LANDLORD / APR-SPEND-OVER-CAP.
- Assumption: no management key was issued, as the tenant asked to be present for access (event-014).

## Why this disposition

Disposition: **needs_info**. Did not close the request. Despite an invoice being uploaded (event-023), the record contains no confirmed appointment and no work result: the contractor never selected a slot from the tenant's offered dates (event-014, event-015, event-017) and on 02/09 reported the glass had still not arrived (event-021). The invoice copy (glazing-invoice.pdf, event-023) states no amount, so it cannot be checked against the landlord-approved £180 incl. VAT (event-010) or forwarded for payment. Landlord authority is sound and already on file, so no new approval was sought. I chased the instructed contractor with a 2-working-day reply-by for attendance confirmation, a fitting slot and a priced invoice; asked the tenant to confirm whether anyone attended, whether the unit is still misted and whether damp or mould has appeared (the damp/cold concern was never assessed on site — event-005); updated the landlord that the invoice is not being processed; and placed the case on hold. Not an escalation: the open questions are owned by the contractor and the tenant, and the routine next steps are all reversible.
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-DISPATCH-APPROVED, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, CAP-SCHEDULE-ACCESS, CAP-CLOSE, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-PII, CLK-S11, CLK-SOP-ACK.
Red flags shaped the decision: data_quality: Invoice NBL-013-INV-09 bills for 'supply and fit' with no amount stated, dated eight days after the contractor said the glass had not arrived, and with no confirmed attendance anywhere in the record. Recorded as unverified work and an unprocessable invoice, not as an allegation against the contractor.; other: Tenant's damp and cold concern, reported 31/07, has never been assessed on site; safety-pass keyword 'damp' present in the report. No damp or mould has been observed or reported as present, so this is recorded as an outstanding check rather than a hazard.

## Timeline

- 15:38:16.545 model turn 1 → tool_use
- 15:38:16.545 playbook maintenance-request · type maintenance_request · urgency routine
- 15:38:16.545 gate get_case_details → allow (read)
- 15:38:16.545 get_case_details → completed (attempts 1)
- 15:38:16.546 gate get_action_ledger → allow (read)
- 15:38:16.546 get_action_ledger → completed (attempts 1)
- 15:38:59.234 model turn 2 → tool_use
- 15:38:59.234 gate add_note → allow (CAP-LOG)
- 15:38:59.234 add_note → completed (attempts 1)
- 15:38:59.234 gate notify_contractor → allow (CAP-NOTIFY)
- 15:38:59.235 notify_contractor → completed (attempts 1)
- 15:38:59.235 gate notify_tenant → allow (CAP-NOTIFY)
- 15:38:59.235 notify_tenant → completed (attempts 1)
- 15:38:59.235 gate notify_landlord → allow (CAP-NOTIFY)
- 15:38:59.235 notify_landlord → completed (attempts 1)
- 15:38:59.235 gate put_on_hold → allow (CAP-LOG)
- 15:38:59.235 put_on_hold → completed (attempts 1)
- 15:39:58.553 model turn 3 → tool_use
- 15:39:58.553 terminal request_info → accepted

Steps used: 3; tokens in/out: 29055/8758 (cache reads 42561); model: claude-opus-5.
