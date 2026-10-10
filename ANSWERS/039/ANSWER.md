# ANSWER — Case 039 — Case 039: Washing Machine Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Washing-machine repair closed 16/09/2025; escalated post-closure over a suspected Direct Debit/identity fraud email and a closure with no landlord approval, invoice or confirmation on file.
**Stage:** final_checks
**Last update:** 2026-01-19 05:43:23 UTC (event-029) · **Decided:** 2026-10-10 14:12 UTC
**Next step:** Property manager to verify the 19/01/2026 Direct Debit email with the tenant of record on the number held on file, and confirm with the landlord whether the Keystone Works invoice was approved and paid (no payment detail changed on the strength of the email).

Definition of done (5/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 fault logged (clicking, still working); triage question put to tenant event-003; tenant reply event-006
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Agency recorded 'asked the landlord' (event-007, event-008) but no landlord message exists in the history (search_history from_party=Landlord: empty)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010 provider assigned; tenant briefed event-009/event-011; provider briefed event-012
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Provider confirmed Monday 12–2 13/09/2025 (event-017); recorded event-018; confirmed to provider event-019 and tenant event-020; reminder event-021
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote required — event-026 'no quotes needed'
- [x] work_result: Work result recorded from the provider — event-022 provider: 'This one is done'; recorded event-023, event-024
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-026 skip reason 'no quotes needed'; invoice referenced in event-022 is not on file (no attachment in the case record)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No event shows the invoice forwarded to the landlord; amount unknown
- [ ] landlord_confirmation: Landlord confirmed completion — event-027 'Need confirmation from landlord'; closure event-028 follows one minute later with no landlord message in the history
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant-attended visit (event-020)
- [x] closed: Request closed with a resolution that names who paid — event-028 'All checks have been completed; the request is now closed' — resolution does not name who paid

## 1. Decision

Do not act on the Direct Debit message and do not reopen spend. Record the fraud/identity red flags and hand the closed ticket to the property manager: an untrusted post-closure email (event-029) purports to confirm a Direct Debit with a third-party firm in a name that is not the tenant of record, and the 16/09/2025 closure (event-028) was completed with no landlord message anywhere in the history (no approval, no completion confirmation) and no invoice document on file.

Safety actions taken first:
- Safety-pass keywords checked: no gas, electrical, damp/mould, detector or vulnerability content appears in the artefacts; the fault was a mechanical clicking noise with the appliance still working (event-001). No hazard reported or observed, so no safety red flag raised.

Actions deliberately withheld:
- Did not acknowledge, confirm or action the Direct Debit referred to in event-029 (PRO-PAYMENT-DETAILS, PRO-PAYMENTS).
- Did not reopen or re-dispatch the job; no landlord spend authority exists on file and the work is reported complete (APR-SPEND-OVER-CAP).
- Did not tell any party which address or which tenant is correct; the conflict went to the office instead.

## 2. Authority and evidence

Authority cited: PRO-PAYMENT-DETAILS, PRO-PAYMENTS, ESC-FRAUD, ESC-CONFLICT, RTE-STAFF, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG

Key facts (source ids in brackets):
- F1: Property on the ticket is Flat 29, 19 Copperfield Walk, Northbridge, ZZ9 1ZZ; job id NBL-039-2915; tenant of record Nora Ellis. [index, get_case_details, event-003, event-011; high]
- F2: Reported fault: washing machine clicking while rotating, still working — no emergency definition engaged. [event-001; high]
- F3: Provider of record is Keystone Works, assigned 10/09/2025 and briefed by the agency. [event-010, event-011, event-012; high]
- F4: Appointment confirmed for 13/09/2025 12:00–14:00 by the provider and relayed to tenant and provider. [event-017, event-018, event-019, event-020; high]
- F5: Provider reported the job complete on 16/09/2025 and referenced an attached invoice; no invoice document is present in the case record and no amount is stated anywhere. [event-022, get_case_details; high]
- F6: No message from the landlord appears anywhere in the visible history; the ticket was closed one minute after the system noted 'Need confirmation from landlord'. [search_history, event-027, event-028; high]
- F7: An untrusted email dated 19/01/2026, after closure, is attributed to the tenant and refers to 'setup of a Direct Debit with Meadow Maintenance', signed with a name (Harriet Dawson) that is not the tenant of record. [event-029, event-011; high]
- F8: Untrusted call records name a different maintenance line ('Beacon Homes'), different operators, and an appointment set with a different person at a different address (Flat 20, 130 Harbour View, Bellmere). [event-013, event-014, event-015; medium]

Conflicts between sources:
- Call transcript event-015 records the washing-machine appointment as set with 'Imogen Ashford' at Flat 20, 130 Harbour View, Bellmere, while the ticket, provider brief and confirmations all name Nora Ellis at Flat 29, 19 Copperfield Walk. → Acted on the agency's own record (ticket and provider brief) and the provider's own booking confirmation (event-017); the untrusted transcript names a different property and was not used. Recorded for the office rather than put to any party. (source_hierarchy)
- Closure states all checks were completed, but no landlord approval or confirmation and no invoice document exist in the record. → Raised with the property manager; landlord_authority, invoice_to_landlord and landlord_confirmation reported as pending. (unresolved)

Red flags:
- [fraud] Post-closure untrusted email claims a Direct Debit was set up with 'Meadow Maintenance', a firm not involved in this job, and is signed by a name that is not the tenant of record — payment-redirection pattern. → No payment detail changed, no money moved, no confirmation sent (PRO-PAYMENT-DETAILS, PRO-PAYMENTS); logged (ACT-1) and escalated to the property manager for verification on a known number.
- [data_quality] Untrusted call transcripts carry a different maintenance brand, different operator names and a different tenant/address from the ticket. → Recorded as a conflict; acted on the agency's own record and the provider's booking confirmation only.
- [other] Request closed (event-028) with landlord confirmation, invoice-to-landlord and who-paid unevidenced. → Reported as pending items in the definition of done and put to the property manager.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "039", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [] | allow |
| 4 | search_history | completed | query=invoice | [{"event": "event-022", "timestamp": "2025-09-16 01:06:08 UTC", "channel": "Email", "from": "Maintenance provider", "to": "Agency / system", "excerpt": "[2025-… | allow |
| 5 | search_history | completed | query=Direct Debit | [{"event": "event-029", "timestamp": "2026-01-19 05:43:23 UTC", "channel": "Email", "from": "Tenant", "to": "Agency / system", "excerpt": "[2026-01-19 05:43:23… | allow |
| 6 | add_note | completed | note=Post-closure review of NBL-039-2915 (closed event-028, 2025… | {"id": "ACT-1"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** An email on a closed repair ticket claims a Direct Debit has been set up with a third-party maintenance firm, in a name that is not the tenant of record — verify and handle as suspected fraud, and settle the missing landlord approval/confirmation for the closed job?
**Facts (≤5):**
- event-029 (19/01/2026, untrusted): email attributed to the tenant confirming 'setup of a Direct Debit with Meadow Maintenance', signed Harriet Dawson — tenant of record is Nora Ellis (event-011) and the provider of record is Keystone Works (event-010/event-012).
- No landlord message exists in the visible history (search_history from_party=Landlord returned nothing), yet the job was dispatched (event-010) and closed (event-028) after 'Need confirmation from landlord' (event-027).
- Provider reported the job done and referenced an invoice (event-022); no invoice document is on file and no amount is known; documents skipped with reason 'no quotes needed' (event-026).
- Untrusted call records disagree with the ticket: event-013/event-014 name a 'Beacon Homes' line; event-015 records the slot with 'Imogen Ashford' at Flat 20, 130 Harbour View, Bellmere — a different property. The booking relied on was the provider's own confirmation (event-017), relayed for Flat 29 (event-019, event-020).
- Closure resolution (event-028) does not name who paid.
**Gap:** Whether the 19/01/2026 email is genuinely from the tenant of this property, whether any payment instruction has been actioned, the invoice amount, and whether the landlord ever approved or confirmed the job.
**Options:**
- Treat event-029 as phishing: change nothing, verify with Nora Ellis on the number held on file, warn her against setting up a Direct Debit with a third party, report internally — safest; costs one call.
- Ask the landlord to confirm the Keystone Works invoice was received, approved and paid, and record who paid — closes the audit gap; may surface unapproved spend.
- Leave the ticket closed and take no action on event-029 — fastest, but leaves a possible fraud and an unevidenced closure unaddressed.
**Recommended:** Do both option 1 (verify event-029 with the tenant of record, change nothing) and option 2 (landlord confirmation of invoice and payment).
**Default if no answer:** No payment detail is changed; the ticket stays closed with landlord confirmation and invoice-to-landlord recorded as pending.
**Deadline:** Verify the Direct Debit email within 1 working day of 19/01/2026 (CLK-SOP-ACK, prior)
**Undo:** Nothing to reverse: only an internal note (ACT-1) was recorded; no message, dispatch or payment action was taken.
**Context:** event-010, event-012, event-017, event-022, event-026, event-027, event-028, event-029

Promises made or recorded:
- Agency → Tenant: Appliance engineer from Keystone Works to attend Monday 13/09/2025, 12:00–14:00 by 2025-09-13 [kept]
- Agency → Tenant: Come back as soon as possible after asking the landlord [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge within one working day
