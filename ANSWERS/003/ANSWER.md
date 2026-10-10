# ANSWER — Case 003 — Case 003: Checkout Cleaning Estimate and Invoice

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Checkout clean/clearance done and £125 invoice paid by the landlord; escalated because the agency's email names Cedar Solutions while the invoice is branded Keystone Maintenance, payee Bennett Ingram.
**Stage:** closed
**Last update:** 2025-09-05 12:34:00 UTC (event-023) · **Decided:** 2026-10-10 13:19 UTC
**Next step:** Property manager to verify which provider was instructed and paid for job NBL-003-2766 (Cedar Solutions vs Keystone Maintenance / payee Bennett Ingram) and whether the £125 went to the correct payee.

Definition of done (7/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 request scope; attachment-01 checkout report (bedroom Poor/Unacceptable, bathroom Unacceptable, dumped items, carpet staining); property vacant at checkout so no tenant damage-limiting advi…
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-010 'Estimate approved' is a system status line with no amount and no landlord message; no landlord standing cap on file and no landlord approval event in the visible history
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-002 provider assigned; event-003/event-004 briefed by SMS and email with job ref NBL-003-2766 and the checkout report
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Property vacant at checkout; no tenant access window required and none recorded in the history
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No priced quote with VAT in the record before works; only the post-works invoice total of £125, no VAT stated (attachment-02)
- [x] work_result: Work result recorded from the provider — event-017 contractor 'hi invoice sent to Theo'; event-018 task moved to Result; event-019 marked completed
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — attachment-01 checkout report and attachment-02 invoice on file; no contractor completion photos supplied
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-020 invoice emailed to landlord 24/07/2025
- [x] landlord_confirmation: Landlord confirmed completion — event-023 landlord replied 'Paid' 05/09/2025
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — attachment-01 records no key details or comments on either report row; no management key issued in the history
- [x] closed: Request closed with a resolution that names who paid — event-022 'All checks have been completed; the request is now closed'; landlord paid the £125 (event-023), though the provider named to the landlord (event-020) differs from the invoice branding and…

## 1. Decision

The cleaning job itself is complete and paid: invoice £125 forwarded to the landlord (event-020) and the landlord replied "Paid" (event-023); the agency closed the request (event-022). I took no further party-facing action because two agency records name different providers for the same job reference and money has already left the landlord — identity of the paid provider is a human decision (ESC-FRAUD, ESC-CONFLICT, RTE-STAFF). Recorded the conflict and the missing pre-works estimate figure as an internal note (ACT-1); did not name either provider to the landlord or contractor.

Safety actions taken first:
- Checked the safety-pass terms across the artefacts: detectors recorded tested 'Yes' on both report rows (attachment-01); no gas, electrical, damp/mould or occupant-vulnerability issue reported; property vacant at checkout.

Actions deliberately withheld:
- Did not tell the landlord or contractor which provider name is correct (would pick a side in an unresolved records conflict).
- Did not reopen or re-close the request, and did not state that the cleaning is tenant-payable (PRO-TENANT-LIABILITY).
- Did not action or query payment details (PRO-PAYMENTS, PRO-PAYMENT-DETAILS).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-HUMAN-TASK, ESC-FRAUD, ESC-CONFLICT, RTE-STAFF, PRO-PAYMENTS, PRO-PAYMENT-DETAILS, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-LOG

Key facts (source ids in brackets):
- F1: Request was for an estimate to clean Flat 30, 30 Harbour View at checkout, including removal of dumped items and a carpet clean. [event-001, index; high]
- F2: A maintenance provider was assigned and briefed with job ref NBL-003-2766 and the checkout report; no provider name is recorded in the assignment event. [event-002, event-003, event-004; high]
- F3: The agency told the provider to proceed and the system logged 'Estimate approved'; no estimate amount appears anywhere in the visible history. [event-009, event-010; high]
- F4: The invoice dated 23/07/2025 for job NBL-003-2766 totals £125 with no VAT stated, covers EOT cleaning (heavy limescale), carpet shampoo and removal of dumped small items, is branded 'Keystone Maintenance' and names Bennett Ingram as payee. [attachment-02-cleaning-invoice; high]
- F5: The agency forwarded that invoice to the landlord describing it as an 'invoice from Cedar Solutions'. [event-020; high]
- F6: The landlord replied 'Paid' on 05/09/2025; the request had been closed by the agency on 24/07/2025. [event-023, event-022; high]
- F7: The checkout report records the site-wide smoke/CO detector system as tested 'Yes' on both the previous (29/11/2024) and current report rows. [attachment-01-checkout-inspection-report; high]
- F8: The checkout report also records a failed bedroom door handle and a damaged bathroom toilet roll holder, outside the cleaning scope and not addressed by this job. [attachment-01-checkout-inspection-report; high]

Conflicts between sources:
- Provider identity: agency email to landlord names Cedar Solutions; the invoice for the same job reference is branded Keystone Maintenance with payee Bennett Ingram, and the contractor emails sign as 'Bennett'. → Recorded in note ACT-1 and handed to the property manager; no provider name used in any outgoing message. (unresolved)
- Date inconsistency in the checkout report: appointment date given as 16 March 2026 while the report is signed 22 July 2025, on a case that ran in July 2025. → Flagged as data quality; does not change the action taken. (unresolved)

Red flags:
- [fraud] Invoice paid by the landlord names a payee and branding (Keystone Maintenance / Bennett Ingram) different from the provider the agency named when forwarding it (Cedar Solutions); payment account details are omitted from the case copy. → Recorded in note ACT-1 and escalated to the property manager; no payment action taken (PRO-PAYMENTS, PRO-PAYMENT-DETAILS).
- [data_quality] No pre-works estimate amount or VAT line exists despite the system logging 'Estimate approved'; checkout report carries a 2026 appointment date on a 2025 case. → Recorded in note ACT-1 and in the handover card.
- [other] Checkout report guidance raises possible deposit deduction for cleaning; liability for the £125 is not decided here. → Left to a human (PRO-TENANT-LIABILITY); listed as an option in the handover.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "003", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Conflict in agency records on provider identity: event-020… | {"id": "ACT-1"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Job NBL-003-2766 is closed and the landlord has paid £125 — confirm which provider was instructed and paid, as our email to the landlord names Cedar Solutions but the invoice is branded Keystone Maintenance with payee Bennett Ingram.
**Facts (≤5):**
- Scope: checkout clean, carpet shampoo and removal of dumped items at Flat 30, 30 Harbour View (event-001; attachment-01 rates bedroom Poor/Unacceptable, bathroom Unacceptable).
- Provider assigned and told to proceed with no provider name and no estimate figure on file (event-002, event-009, event-010 'Estimate approved').
- Invoice: £125 total, no VAT stated, job ref NBL-003-2766, branding 'Keystone Maintenance', payee 'Bennett Ingram' (attachment-02).
- Agency email forwarding that invoice calls it an 'invoice from Cedar Solutions' (event-020); landlord replied 'Paid' (event-023).
- attachment-01 data quality: appointment date 16 March 2026 but signed 22 July 2025; it also flags a failed bedroom door handle and damaged toilet roll holder, not covered by this job.
**Gap:** Which provider the agency actually instructed (no name in event-002), the pre-works estimate amount said to be approved at event-010, and whether the bank details on the original invoice match the instructed provider (payment details omitted from the case copy of attachment-02).
**Options:**
- Verify the instructed provider against the work-order/accounts record; if it matches, correct the provider name in the landlord correspondence and leave the case closed.
- If the paid payee does not match the instructed provider, refer to accounts/fraud checks before any further payment to this payee and tell the landlord in writing.
- Open a separate ticket for the uncovered defects (bedroom door handle, toilet roll holder) and for any deposit-deduction decision on the cleaning cost.
**Recommended:** Verify the instructed provider against the work-order/accounts record; if the payee does not match, refer to accounts before any further payment to this payee.
**Default if no answer:** Case stays closed and paid with the provider-name discrepancy unresolved on file.
**Undo:** Nothing to reverse: no messages sent and no contractor instructed by me; only internal note ACT-1 added. The £125 was paid by the landlord and cannot be reversed by the agency.
**Context:** event-002, event-009, event-010, event-020, event-022, event-023, attachment-01-checkout-inspection-report, attachment-02-cleaning-invoice

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge report within one working day
- CLK-S11 [in_force]: Repairs within a reasonable time
