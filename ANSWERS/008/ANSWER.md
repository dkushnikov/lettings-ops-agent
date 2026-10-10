# ANSWER — Case 008 — Case 008: Check-Out Works

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Check-out works at Flat 5, 55 Lantern Quay complete; landlord authorised the £1,190 invoice, so I closed the job and referred payment, ceiling water ingress and deposit to staff.
**Stage:** closed
**Last update:** 2025-06-17 02:24:25 UTC (event-049) · **Decided:** 2026-10-10 14:02 UTC
**Next step:** Accounts/property manager to release the £1,190.00 payment to the approved provider after verifying the payee name (human task ACT-3); landlord to say whether they want the bedroom carpet and ceiling water ingress quoted as a new request.

Definition of done (9/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (scope listed), attachment-01/attachment-03 (check-out defects); property void so no tenant damage-limiting advice applicable (event-012)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-038 landlord: 'Please go ahead with Eliza' in reply to event-036 quoting Flat 5
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-011 new provider assigned; event-039/event-041 provider asked and confirmed willing to proceed
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Property not tenanted (event-012); no tenant access window required, works carried out and reported complete (event-042)
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-036 both quotes with VAT position stated (£1,370.00 no VAT; £1,700.00 + VAT); landlord approved event-038 before works began (event-041)
- [x] work_result: Work result recorded from the provider — event-042 moved to Result; event-043 marked completed; event-045 provider reported tap not needed
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — Invoice attachment-04 on file; photo upload skipped with reason recorded — 'No photos attached' (event-046)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-045 invoice emailed to landlord for payment
- [x] landlord_confirmation: Landlord confirmed completion — event-049 landlord: 'Ok to pay.'
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issue recorded anywhere in the history; property void (event-012)
- [x] closed: Request closed with a resolution that names who paid — ACT-4 close_request — resolution names the landlord as payer; system had already closed at event-048 before the landlord's confirmation arrived

## 1. Decision

Closed the check-out works job. The workflow was complete within my mandate: landlord approved the cheaper quote (event-038), works were done (event-042/043), the invoice was forwarded (event-045) and the landlord confirmed payment (event-049). I recorded the scope and price variance, addressed the safety keywords (detectors tested Yes; bedroom ceiling water ingress unrepaired and outside scope), informed the landlord of the final position and the two outstanding items, referred payment release, payee verification, the water ingress and any deposit/liability question to the property manager, and closed with a resolution naming the landlord as payer. I did not move money, decide tenant liability, or act on the address mismatches in the agency's own outbound emails beyond recording them for the office.

Safety actions taken first:
- Safety pass: smoke and carbon monoxide detectors recorded tested — Yes with no adverse comments in both check-out reports (attachment-01, attachment-03); no detector action required before re-let, result recorded in ACT-1 and ACT-4.
- Damp/water keywords checked: bathroom water damage to boxing and flooring was within the completed works (damp paint, new lino — attachment-04); bedroom ceiling water ingress was not, and has been flagged to the landlord and the property manager for investigation before re-let.
- No gas, electrical, fire or security hazard reported or observed; property void (event-012), so no occupant at risk and no emergency capability engaged.

Actions deliberately withheld:
- Did not release or process payment of the £1,190.00 invoice (PRO-PAYMENTS) — referred to accounts/property manager.
- Did not decide that any item (burnt carpet, stained mattress, missing furniture, cleaning) is tenant-payable or deductible from the deposit (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Did not instruct any further works for the bedroom carpet or the ceiling water ingress: no landlord approval exists for that spend (APR-SPEND-OVER-CAP); offered to quote on the landlord's instruction.
- Did not tell any party which provider name or which property is 'correct' where agency records disagree; recorded the conflict and asked the office instead.

## 2. Authority and evidence

Authority cited: CAP-LOG — case note recording the scope variance, provider-name and address conflicts and the safety-pass result (ACT-1), CAP-NOTIFY — final position and outstanding items to the landlord (ACT-2), CAP-HUMAN-TASK — payment release, payee verification, ceiling water ingress and deposit question referred to the property manager (ACT-3), CAP-CLOSE — closed after work result, documents/skip reason, invoice to landlord and landlord confirmation were all in evidence; resolution names the payer (ACT-4), RTE-LANDLORD — the landlord owned the quote choice and the payment authorisation; both settled in their own messages (event-038, event-049), PRO-PAYMENTS — payment not moved by me, PRO-TENANT-LIABILITY — no deposit or tenant-cost decision taken, PRO-PAYMENT-DETAILS — payee to be verified against the supplier record, not from a message, APR-SPEND-OVER-CAP — no further works instructed without landlord approval
Rules applied by the policy gate: CAP-CLOSE, CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Job NBL-008-3466 is check-out works at Flat 5, 55 Lantern Quay, Cedarford, ZZ2 4ZZ: repaint, replace burnt bedroom carpet, replace bathroom flooring, repair broken plug, dripping bath tap and damaged bathroom shelf. [index, event-001, event-003, get_case_details; high]
- F2: The property is not tenanted; the system paused the request for that reason on 6 April 2025. [event-012; high]
- F3: First estimate £1,370.00 with no VAT itemised; its scope excludes the bedroom carpet ('carpet in the main room can stay as it's not that bad') and includes replacing the bathroom tap. [attachment-02; high]
- F4: The landlord asked for a second quote for comparison (6 April 2025); the second quote was £1,700.00 + VAT. [event-009, event-036; high]
- F5: Both quotes with their VAT position were put to the landlord on 25 May 2025 naming 'Flat 5', and the landlord approved the cheaper provider the same day. [event-036, event-038; high]
- F6: The provider confirmed willingness to proceed on 26 May 2025; works were reported complete on 2 June 2025. [event-041, event-042, event-043; high]
- F7: Final invoice is £1,190.00 with no VAT stated, for painting the bathroom in damp paint, painting all walls and ceiling in the main room, replacing bathroom lino, repairing the plug socket and repairing the shelf; no photos included. [attachment-04; high]
- F8: The bath tap was not replaced because the provider found it did not need replacing, which is why the invoice is below the approved estimate. [event-045; high]
- F9: The burnt bedroom carpet was not replaced: it was excluded from the estimate the landlord approved, and it does not appear on the invoice. [attachment-02, attachment-04, event-038; high]
- F10: The invoice was forwarded to the landlord on 2 June 2025 and the landlord authorised payment on 17 June 2025 ('Ok to pay'), after the system had already closed the request on 2 June 2025. [event-045, event-048, event-049; high]
- F11: Photo upload was skipped with the recorded reason 'No photos attached'. [event-046; high]
- F12: Smoke and carbon monoxide detectors are recorded as tested — Yes, with no adverse comments, in both check-out reports. [attachment-01, attachment-03; high]

Conflicts between sources:
- Provider identity: approved provider named 'Eliza Bennett' in the agency history, but the estimate and invoice documents are headed 'Alder Compliance' (and event-016 mentions 'Meadow Compliance'). → Not resolved by me and not asserted to any party. Quote value matches exactly, so the approved quote and invoice relate to the same instruction; payee verification before payment referred to the office (ACT-3). (unresolved)
- Property identity in agency outbound emails: event-021, event-027, event-028 and event-045 name Juniper Mews, Meadow Row or Flat 13 Harbour View in the body of a job headed Flat 5, 55 Lantern Quay. → The case record, both check-out reports and both financial documents are all Flat 5, 55 Lantern Quay, and the approval at event-038 answered event-036 which correctly stated 'Flat 5'. Worked the job at the record address; template fault reported to the office (ACT-3), not argued with any party. (source_hierarchy)
- Scope: the original instruction (event-001) asked for the burnt bedroom carpet to be replaced; the approved estimate says it can stay. → The landlord's own approval of that estimate (event-038) governs the instructed scope. Carpet recorded as outstanding and put back to the landlord (ACT-2). (source_hierarchy)
- Document dates (inspection 5 January 2026, invoice 09/03/2026) sit outside the April–June 2025 case timeline. → Recorded as a data-quality anomaly (ACT-1, ACT-3); does not change the action. (unresolved)

Red flags:
- [data_quality] Agency outbound emails on this job repeatedly quote unrelated addresses (Juniper Mews, Meadow Row, Flat 13 Harbour View) and event-027 is addressed 'Hi Langley' but sent to the contractor; document dates are a year out from the case timeline. → Recorded in the case note (ACT-1) and referred to the property manager (ACT-3); worked the job at the address on the case record.
- [data_quality] Payee name on the financial documents ('Alder Compliance') differs from the provider name the landlord approved ('Eliza'); event-016 mentions a third name. → Flagged for payee verification before payment release (ACT-3); no payment moved (PRO-PAYMENTS).
- [other] Unrepaired bedroom ceiling water ingress recorded in both check-out reports and never scoped or quoted; source of the leak unknown. Property is void, so no occupant is exposed. → Raised with the landlord with a recommendation to investigate before re-let (ACT-2) and referred to the property manager (ACT-3).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "008", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Case review at manual-mode trigger (free-text landlord repl… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Re: check-out works, Flat 5, 55 Lantern Quay, Cedarford, ZZ… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | create_human_task | completed | queue=property_manager, title=Flat 5, 55 Lantern Quay — post-closure items: payment relea…, summary=Check-out works job NBL-008-3466 is complete and closed; fo… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 6 | close_request | completed | resolution=Check-out works at Flat 5, 55 Lantern Quay, Cedarford, ZZ2… | {"id": "ACT-4"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- agency → landlord: Landlord's payment authorisation passed to accounts for processing; agency does not release payment itself [open]
- agency → landlord: Bedroom carpet replacement and bedroom ceiling water ingress to be raised as a new request if the landlord asks for quotes [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge within one working day
- CLK-GAS-CP12 [in_force]: Gas safety record renewed every 12 months
