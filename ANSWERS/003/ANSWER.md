# ANSWER — Case 003 — Case 003: Checkout Cleaning Estimate and Invoice

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Checkout clean done and paid, but the agency email names Cedar Solutions while the paid invoice is Keystone Maintenance / payee Bennett Ingram — referred to the office.
**Stage:** final_checks
**Last update:** 2025-09-05 12:34:00 UTC (event-023) · **Decided:** 2026-10-10 13:59 UTC
**Next step:** Property manager to confirm with accounts/the provider record which firm holds job NBL-003-2766 and whether the landlord's £125 payment reached the correct payee.

Definition of done (7/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 request logged and categorised; condition/cleanliness evidence in attachment-01-checkout-inspection-report
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No landlord message authorising the spend before work; event-010 is a system status line and event-009 is agency-to-contractor. Landlord paid afterwards (event-023), which ratifies but does not repla…
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-002 provider assigned; briefed by email/SMS event-003, event-004
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Vacant property at checkout; no tenant access window required and none recorded in history
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No priced quote with VAT on file before the work; invoice £125 with no VAT breakdown (attachment-02-cleaning-invoice)
- [x] work_result: Work result recorded from the provider — event-017 contractor reports invoice sent; event-018 task moved to Result; event-019
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — Checkout report attachment-01 and invoice attachment-02 on file
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-020 invoice emailed to landlord
- [x] landlord_confirmation: Landlord confirmed completion — event-023 landlord: 'Paid'
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued recorded; key rows blank in attachment-01
- [x] closed: Request closed with a resolution that names who paid — event-022 closed, but the resolution did not name who paid and closure preceded the landlord's confirmation (event-023); payee identity now disputed

## 1. Decision

Case was closed by the agency (event-022) and the landlord has since paid the invoice (event-023), so the repair workflow itself is finished. But the agency's own record of the provider conflicts with the paid invoice: the covering email to the landlord names "Cedar Solutions" (event-020) while the invoice is branded Keystone Maintenance and names Bennett Ingram as payee (attachment-02). Money has already left the landlord against that document, so a person must verify which provider holds the job and whether the payment went to the right payee (ESC-FRAUD, ESC-CONFLICT, RTE-STAFF). I took no side in any message to a party; the conflict, the missing pre-work landlord approval, the detector check and the two outstanding checkout defects are recorded in the case note (ACT-1).

Safety actions taken first:
- Safety pass check: smoke and CO detectors (site-wide system) recorded as tested and working on both previous and current checkout reports — no hazard; 'evidence of smoking' in the bedroom treated as a cleanliness observation, not a reported hazard.

Actions deliberately withheld:
- Did not message the landlord or contractor naming either provider, to avoid picking a side in a conflict between agency records.
- Did not instruct any repair of the failed door handle or damaged toilet roll holder: no landlord approval and no standing spend cap on file (APR-SPEND-OVER-CAP).
- Did not decide tenant liability or deposit deduction (PRO-TENANT-LIABILITY).
- Did not reopen or re-close the request or alter payment records (PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-HUMAN-TASK, ESC-FRAUD, ESC-CONFLICT, RTE-STAFF, APR-SPEND-OVER-CAP, PRO-PAYMENTS, PRO-PAYMENT-DETAILS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-LOG

Key facts (source ids in brackets):
- F1: Job NBL-003-2766 is a checkout clean at Flat 30, 30 Harbour View, Northbridge, including removal of dumped items and a carpet clean. [index, event-001, event-004; high]
- F2: A maintenance provider was assigned and briefed on 2025-07-22. [event-002, event-003, event-004; high]
- F3: The contractor reported the work done and the invoice sent on 2025-07-23. [event-017; medium]
- F4: The invoice totals £125 for EOT cleaning (heavy limescale), carpet shampoo and removal of dumped small items; no VAT or itemisation is stated. [attachment-02-cleaning-invoice; high]
- F5: The invoice carries Keystone Maintenance branding and names Bennett Ingram as payee, while the agency's covering email to the landlord describes it as an invoice from Cedar Solutions. [attachment-02-cleaning-invoice, event-020; high]
- F6: The landlord confirmed payment with a one-word email 'Paid' on 2025-09-05, after the request had been closed on 2025-07-24. [event-023, event-022; high]
- F7: No landlord message in the visible history approves the spend before the work; the approval entries are agency/system lines. [event-009, event-010; high]
- F8: The checkout report records smoke/CO detectors (site-wide system, tested by staff) marked Yes on both the previous and current reports; no alarm failure is recorded. [attachment-01-checkout-inspection-report; high]
- F9: The checkout report records two maintenance defects outside the cleaning scope: a failed bedroom door handle and a damaged bathroom toilet roll holder. [attachment-01-checkout-inspection-report; high]
- F10: The checkout report's internal dates are inconsistent: appointment date 16 March 2026, signed 22 July 2025, previous report 29 November 2024. [attachment-01-checkout-inspection-report; high]

Conflicts between sources:
- Provider identity: agency email names Cedar Solutions; the paid invoice is branded Keystone Maintenance with payee Bennett Ingram. → Referred to the office via this handover; no side taken in any message to a party. (unresolved)
- Authority for the £125 spend: ticket shows 'Estimate approved' as a system line only; landlord confirmation arrives only after payment. → Recorded; landlord's payment ratifies the spend retrospectively but no pre-work landlord approval exists. (unresolved)

Red flags:
- [fraud] Payee/provider name mismatch on an invoice the landlord has already paid: 'Cedar Solutions' in the agency email vs Keystone Maintenance / Bennett Ingram on the invoice. → Recorded in case note ACT-1 and escalated to the property manager; no payment action taken (PRO-PAYMENTS, PRO-PAYMENT-DETAILS).
- [data_quality] Checkout report dates inconsistent (appointment 16 March 2026, signed 22 July 2025); invoice has no VAT breakdown or itemisation. → Recorded in case note ACT-1.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "003", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [{"event": "event-023", "timestamp": "2025-09-05 12:34:00 UTC", "channel": "Email", "from": "Landlord", "to": "Northbridge Lettings", "excerpt": "[2025-09-05 1… | allow |
| 4 | add_note | completed | note=Post-closure review of NBL-003-2766 (checkout clean, Flat 3… | {"id": "ACT-1"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Which provider holds job NBL-003-2766, and did the landlord's £125 payment go to the correct payee — the agency email says Cedar Solutions, the paid invoice says Keystone Maintenance / Bennett Ingram?
**Facts (≤5):**
- Job NBL-003-2766: checkout clean, carpet shampoo and removal of dumped items at Flat 30, 30 Harbour View; work reported complete and invoiced at £125, no VAT stated, not itemised (event-017, attachment-02-cleaning-invoice).
- Agency's covering email to the landlord says 'invoice from Cedar Solutions' (event-020); the invoice itself is branded Keystone Maintenance with payee Bennett Ingram; contractor emails on file are signed 'Bennett' (event-007).
- Landlord replied 'Paid' on 2025-09-05 (event-023) — payment already made; the ticket had been closed on 2025-07-24 (event-022) before that confirmation.
- No landlord message approving the £125 before the work: 'Estimate approved' is a system status line (event-010) and 'Received :) Please proceed' was agency-to-contractor (event-009).
- Checkout report also records a failed bedroom door handle and a damaged toilet roll holder, outside the cleaning scope; detectors (site-wide system) were tested and marked Yes on both reports (attachment-01-checkout-inspection-report).
**Gap:** No authoritative provider record is available to me to confirm whether Cedar Solutions and Keystone Maintenance are the same business, and no payment-destination evidence (account details were omitted from the invoice copy).
**Options:**
- Verify against the provider/accounts record: if the two names are one business, note it and leave the case closed.
- If they are different businesses, treat as a possible misdirected payment — contact the landlord and the provider, and refer to accounts before any further payment.
- Separately ask the landlord whether to instruct repair of the bedroom door handle and toilet roll holder, and whether any cleaning cost is to be put to the deposit (human decision, PRO-TENANT-LIABILITY).
**Recommended:** Verify against the provider/accounts record first; if the names are different businesses, treat as a possible misdirected payment.
**Default if no answer:** Case stays closed with the conflict recorded in the note (ACT-1); no further money or instruction issued by me.
**Undo:** Nothing to undo — my only action was an internal case note (ACT-1); no contractor was instructed, no message sent to a party, no money moved.
**Context:** event-009, event-010, event-017, event-020, event-022, event-023, attachment-01-checkout-inspection-report, attachment-02-cleaning-invoice

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a report within one working day
