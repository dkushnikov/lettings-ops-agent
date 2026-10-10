# ANSWER — Case 023 — Case 023: Balcony Door Lock Repair

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Balcony door lock repair closed on an unverified contractor completion claim with no approved quote, no invoice and no confirmed visit; chased all parties and escalated.
**Stage:** final_checks · **Hold:** Waiting for Provider — invoice, attendance date and photos requested from Juniper Surveying (ACT-1); tenant confirmation also outstanding (ACT-2).
**Last update:** 2025-07-28 05:33:45 UTC (event-027) · **Decided:** 2026-10-10 14:05 UTC
**Next step:** Property manager to decide whether to reopen the request pending the provider's invoice and evidence (chased, 2 working days) and the tenant's confirmation that the lock is repaired.

Definition of done (3/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 / event-007: fault categorised as a lock repair; urgency routine; tenant advised to report immediately if the door cannot be secured (ACT-2)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006: landlord agreed to someone attending (no amount named)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008, event-009, event-010: Juniper Surveying assigned and briefed; tenant told who is attending
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-012, event-016, event-019: voicemail and chases only; no slot ever confirmed with the tenant
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-010 required a quote before proceeding; no quote or approved amount exists on the request
- [ ] work_result: Work result recorded from the provider — event-020 is an untrusted one-line claim with no photos, date or detail; provider chased (ACT-1)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-023: skipped with reason 'No further documents to add' — recorded, but no photos or invoice exist
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice received by the agency (search_history, ACT-1); landlord told nothing is approved (ACT-3)
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 flagged confirmation as needed; no landlord reply after event-006
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — event-026 records a key return, but no management key issue is recorded for this visit
- [ ] closed: Request closed with a resolution that names who paid — event-027 closed the request, but the resolution names no payer and the checks above are outstanding

## 1. Decision

The ticket was closed (event-027) although the completion claim is unverified and several closing checks were never met: no quote was approved, no invoice has been received, no appointment was ever confirmed with the tenant, and the landlord confirmation flagged at event-024 was never obtained. I took the reversible steps inside my mandate — chased the provider for the invoice, attendance date and photos (ACT-1), asked the tenant whether anyone attended and whether the lock now works (ACT-2), told the landlord that no amount is approved and no invoice is on file (ACT-3), and logged the discrepancies (ACT-4). Reopening a closed request, accepting an invoice for work carried out without the required prior approval, and deciding who bears that cost are human decisions (RTE-STAFF, APR-SPEND-OVER-CAP), so the case goes to the property manager.

Safety actions taken first:
- Told the tenant that if the balcony door cannot be secured they should keep it shut and tell us immediately so it can be treated as urgent (ACT-2) — an insecure property is an emergency under the mandate's definitions.

Actions deliberately withheld:
- Did not confirm completion or close/approve payment on the provider's untrusted claim (PRO-PAYMENTS, CAP-CLOSE).
- Did not decide who bears the cost of work done without prior approval (PRO-TENANT-LIABILITY, APR-SPEND-OVER-CAP).
- Did not dispatch a replacement contractor: no priced landlord approval and no standing cap on file (APR-SPEND-OVER-CAP).
- Did not book an access window: no tenant consent or agreed slot on record (CAP-SCHEDULE-ACCESS).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, CAP-SCHEDULE-ACCESS, RTE-STAFF, RTE-CONTRACTOR, RTE-LANDLORD, ESC-CONFLICT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the balcony glass door locking mechanism not turning/locking at Flat 20, 110 Meadow Row, Northbridge, ZZ2 5ZZ on 25 Jul 2025. [index, event-001, get_case_details; high]
- F2: The landlord (Isaac) replied agreeing someone should attend — 'needs sorting fairly soon' — without naming an amount or approving a quote. [event-003, event-006; high]
- F3: No landlord spend cap or standing instruction is available to me in this case record; the only landlord authority is the attendance agreement at event-006. [event-006, get_case_details; medium]
- F4: Juniper Surveying were assigned and briefed, with instructions to quote and to proceed only after the agency's approval. [event-008, event-009, event-010; high]
- F5: No appointment was ever confirmed with the tenant: a voicemail was left, two SMS chases were sent and the request sat on hold asking whether the tenant had called back. [event-012, event-014, event-015, event-016, event-019; high]
- F6: The provider claims by email 'I've done the job and sent you the invoice yesterday'; no invoice, quote, photos or attendance date is on the request. [event-020, search_history; high]
- F7: The request was moved to Result, documents skipped as 'No further documents to add', landlord confirmation flagged as still needed, key return marked confirmed, and the request closed. [event-021, event-022, event-023, event-024, event-026, event-027; high]
- F8: No key issue to the provider is recorded anywhere on the request, yet a key return was confirmed. [event-025, event-026; medium]
- F9: The tenant of record is Theo Ingram; Freya is named as the Juniper Surveying operative, but a call note records a voicemail left for 'Freya Langley'. [event-009, event-010, event-012, event-014; medium]

Conflicts between sources:
- Provider says the job is done and invoiced (event-020), while the agency record shows no confirmed appointment, no quote approval and no invoice received. → Provider asked for attendance date, work done, photos and the invoice (ACT-1); tenant asked whether anyone attended and whether the lock works (ACT-2). (asked)
- Request closed as all checks completed (event-027) while landlord confirmation was still outstanding (event-024) and no invoice or work evidence exists. → Referred to the property manager to decide on reopening. (unresolved)
- Key return confirmed although no management key is recorded as issued for this visit. → unresolved (unresolved)
- Name inconsistency: voicemail recorded as left for 'Freya Langley' while Freya is the provider's operative and the tenant is Theo Ingram. → Addressed the tenant by the name on the case record (Theo Ingram); flagged as data quality. (unresolved)

Red flags:
- [data_quality] Completion and closure rest on a single untrusted one-line provider email; no invoice, quote, photos or attendance record exists, and the key-return check was marked confirmed with no key issued. → Chased the provider for evidence and the invoice (ACT-1), asked the tenant to confirm attendance and repair (ACT-2), logged the discrepancies (ACT-4) and escalated.
- [data_quality] Occupant name inconsistency between the call note ('Freya Langley') and the tenancy/brief (tenant Theo Ingram; Freya is the provider's operative). → Used the case-record name for the tenant; raised for office check.
- [other] Work appears to have been carried out without the prior approval the provider brief required, creating an unapproved-spend/invoice-dispute risk for the landlord. → Landlord told no amount is approved and no invoice processed (ACT-3); decision referred to the property manager.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "023", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-59-document | {"error": "no attachment named attachment-59-document"} | allow |
| 4 | get_attachment | completed | name=attachment-42-document | {"error": "no attachment named attachment-42-document"} | allow |
| 5 | search_history | completed | query=invoice quote | [] | allow |
| 6 | search_history | completed | from_party=Landlord | [{"event": "event-006", "timestamp": "2025-07-25 04:29:47 UTC", "channel": "Email", "from": "Landlord", "to": "Northbridge Lettings", "excerpt": "[2025-07-25 0… | allow |
| 7 | notify_contractor | completed | message=Re: Lock Repair Request, Flat 20, 110 Meadow Row, Northbrid… | {"id": "ACT-1"} | CAP-NOTIFY |
| 8 | notify_tenant | completed | message=Dear Theo Ingram, regarding the balcony door lock at Flat 2… | {"id": "ACT-2"} | CAP-NOTIFY |
| 9 | notify_landlord | completed | message=Re: balcony door lock, Flat 20, 110 Meadow Row, Northbridge… | {"id": "ACT-3"} | CAP-NOTIFY |
| 10 | add_note | completed | note=Case was closed at event-027 with checks outstanding: contr… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** The lock job was closed on the provider's word alone, with no approved quote and no invoice on file — do we reopen and withhold payment until Juniper Surveying evidences the work, or accept the closure?
**Facts (≤5):**
- Tenant reported the balcony door lock not turning/locking on 25 Jul (event-001); property Flat 20, 110 Meadow Row.
- Landlord Isaac agreed someone should attend — 'needs sorting fairly soon' (event-006) — but named no amount; the provider brief required a quote and said 'only proceed after receiving our approval' (event-010).
- No appointment was ever confirmed: the tenant never called Freya back (event-012, event-016, event-019); then the provider emailed 'I've done the job and sent you the invoice yesterday' (event-020, untrusted).
- No invoice, quote or photos exist on the request; documents were skipped as 'No further documents to add' (event-023) and landlord confirmation was still flagged as needed (event-024).
- Request was nonetheless closed (event-027), and 'keys return confirmed' (event-026) although no management key is recorded as issued.
**Gap:** Whether the work was actually carried out, on what date, at what cost, and under whose authority — the only evidence is the provider's one-line untrusted email.
**Options:**
- Reopen the request, hold payment, and act on the provider's reply and the tenant's confirmation (chased today).
- Accept the closure and pass any invoice the provider sends to the landlord for approval after the fact — risk of a disputed, unapproved charge.
- Instruct a different provider to inspect and quote if the tenant reports the lock is still faulty — needs the landlord's approval of the cost.
**Recommended:** Reopen the request, hold payment, and act on the provider's and tenant's replies.
**Default if no answer:** If the provider does not reply within 2 working days and the tenant confirms the lock is still faulty, re-instruct a locksmith with the landlord's priced approval under APR-SPEND-OVER-CAP.
**Deadline:** Provider reply due 2 working days from today's chase (ACT-1)
**Undo:** No spend has been authorised and no money moved; the messages sent (ACT-1 to ACT-3) state that no invoice is approved and can be followed up or corrected.
**Context:** event-006, event-010, event-012, event-020, event-023, event-024, event-026, event-027

Promises made or recorded:
- Agency → Contractor: Invoice, attendance date, description of work and photos requested; no invoice processed until received by 2 working days from 2025-07-28 chase [open]
- Agency → Tenant: If no one attended or the lock is still faulty, a visit will be arranged at a time that suits the tenant [open]
- Agency → Landlord: Come back with the provider's reply and any cost before any invoice is processed [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-RRA-2025 [in_force]: Renters' Rights Act 2025 provisions
