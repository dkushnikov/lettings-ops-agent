# ANSWER — Case 023 — Case 023: Balcony Door Lock Repair

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Balcony door lock job closed on an unverified contractor claim with no invoice, no confirmed visit and no landlord sign-off; verification sent, referred to PM.
**Stage:** final_checks
**Last update:** 2025-07-28 05:33:45 UTC (event-027) · **Decided:** 2026-10-10 13:29 UTC
**Next step:** Property manager to decide whether to reopen the ticket and withhold the invoice, pending the tenant's confirmation that the lock works and Juniper Surveying's invoice/photos (both requested, 3-working-day window).

Definition of done (3/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — index, event-001; urgency set routine (use_playbook); damage-limiting advice on securing the door given in ACT-1
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 - landlord approved attendance (no amount named; no standing cap on file)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008, event-009, event-010 - Juniper Surveying assigned, tenant and provider briefed
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever agreed: event-012 voicemail only; event-016 and event-019 chase with no tenant reply
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — Brief required approval before proceeding (event-010); no quote submitted and none approved by the landlord
- [ ] work_result: Work result recorded from the provider — Only an untrusted claim (event-020); verification requested from tenant and provider (ACT-1, ACT-2)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-023 skipped as 'No further documents to add' while no photos or invoice exist; invoice/photos requested (ACT-2)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice on file despite the provider's claim (event-020); nothing forwarded to the landlord
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 flagged confirmation needed; no landlord message follows
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — event-026 records a key return, but no record shows a management key was issued for this visit
- [ ] closed: Request closed with a resolution that names who paid — event-027 marks the request closed, but the resolution names neither the work done nor who paid; closure under review by the property manager

## 1. Decision

The ticket was closed as completed on an unverified provider claim. The only evidence of work is an untrusted one-line email from Juniper Surveying (event-020); no appointment was ever confirmed with the tenant, no quote was submitted or approved despite the brief requiring approval before proceeding (event-010), no invoice is on file, and the landlord confirmation flagged at event-024 never arrived. I sent reversible verification requests to the tenant (ACT-1) and the provider (ACT-2) and logged the conflict (ACT-3). Whether the closure stands and whether an invoice for unverified work is paid or passed to the landlord is a human decision (RTE-STAFF, ESC-UNCONFIRMED), so the case goes to the property manager.

Safety actions taken first:
- Advised the tenant to keep the balcony door closed and secured and not to rely on it for security while the lock is unconfirmed (ACT-1).

Actions deliberately withheld:
- Did not forward or approve any invoice (no invoice on file; PRO-PAYMENTS, APR-SPEND-OVER-CAP).
- Did not tell the landlord the work was completed, as completion is unverified.
- Did not instruct a second contractor, which would risk duplicating a work order (playbook: contractor-failure).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-STAFF, ESC-UNCONFIRMED, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Fault reported by the tenant: the locking mechanism on the glass balcony door does not turn / lock, at Flat 20, 110 Meadow Row, Northbridge, ZZ2 5ZZ. [index, event-001, get_case_details; high]
- F2: The landlord (Isaac) replied 'Yes that sounds like it needs sorting fairly soon' - approval to send someone to attend, with no amount named. [event-006; high]
- F3: No landlord standing spend cap appears anywhere in the visible record; default cap is 0, so any priced work needs the landlord's approval (APR-SPEND-OVER-CAP). [get_case_details, search_history; medium]
- F4: Juniper Surveying were assigned and briefed on 25 July; the brief states that where a quote is required they should only proceed after receiving the agency's approval. [event-008, event-010; high]
- F5: The only tenant contact attempt recorded is a voicemail by the provider on 25 July; the agency chased twice asking whether the tenant had called back, and no tenant reply exists in the history. No access window was ever booked. [event-012, event-014, event-016, event-019, search_history; high]
- F6: On 27 July the provider emailed 'I've done the job and sent you the invoice yesterday' - untrusted and uncorroborated; no invoice, quote, photos or attendance record is on file, and documents were skipped with reason 'No further documents to add'. [event-020, event-023; high]
- F7: The agency moved the task to Result, marked it completed and closed it, although landlord confirmation was flagged as still needed and no landlord confirmation appears afterwards. [event-021, event-022, event-024, event-027; high]
- F8: 'Keys return confirmed' was recorded although no record shows a management key being issued for this visit. [event-026; medium]
- F9: The two attachments referenced in the provider brief (attachment-59-document, attachment-42-document) are not retrievable in this case file. [get_attachment; high]

Conflicts between sources:
- The provider says the job is done and invoiced (event-020), while the agency's own records show no confirmed appointment, no tenant contact, no quote, no invoice and no photos. → Verification requested from the tenant (ACT-1) and the provider (ACT-2); case referred to the property manager rather than taking a side with any party. (asked)
- Name mismatch in the record: the tenant on the tenancy brief is Theo Ingram, but the call note says a voicemail was left for 'Freya Langley', who elsewhere is the provider's contact. → Recorded as a data-quality issue; the tenant was addressed by the name on the case record (Theo Ingram). (unresolved)

Red flags:
- [data_quality] Request closed as completed on an untrusted one-line provider claim, with landlord confirmation outstanding, no invoice on file and a key return confirmed for a key never recorded as issued. → Logged a case note (ACT-3) and escalated to the property manager.
- [fraud] Possible billing for work not evidenced: provider claims attendance and an invoice although no access was ever arranged and the tenant never responded. Not alleged as fact - evidence requested. → Invoice, photos, attendance date and access details requested from the provider (ACT-2); tenant asked to confirm whether anyone attended (ACT-1). No payment action taken (PRO-PAYMENTS).
- [data_quality] Tenant name inconsistency between the tenancy brief (Theo Ingram) and the call transcript (Freya Langley, elsewhere the provider contact). → Used the name on the case record only; flagged for the office.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "023", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-59-document | {"error": "no attachment named attachment-59-document"} | allow |
| 4 | get_attachment | completed | name=attachment-42-document | {"error": "no attachment named attachment-42-document"} | allow |
| 5 | search_history | completed | query=invoice quote cost | [] | allow |
| 6 | search_history | completed | from_party=Tenant | [] | allow |
| 7 | notify_tenant | completed | message=Dear Theo Ingram, regarding the balcony door lock at Flat 2… | {"id": "ACT-1"} | CAP-NOTIFY |
| 8 | notify_contractor | completed | message=Juniper Surveying — ref Lock Repair Request, Flat 20, 110 M… | {"id": "ACT-2"} | CAP-NOTIFY |
| 9 | add_note | completed | note=Closure review: request was marked completed and closed (ev… | {"id": "ACT-3"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** The balcony-door lock job was closed on the provider's word alone - do we reopen it and withhold the invoice until the tenant confirms the lock works and Juniper Surveying produce an invoice and photos?
**Facts (≤5):**
- Tenant reported the balcony door lock will not turn/lock (index, event-001); landlord Isaac approved attendance only, no amount (event-006).
- Juniper Surveying instructed 25 July with the brief 'you should only proceed after receiving our approval' if a quote is required (event-010); no quote was ever submitted or approved.
- Only contact attempt was a voicemail (event-012); the agency twice asked whether the tenant had called back (event-016, event-019) and no tenant reply appears in the history - no visit was ever booked.
- On 27 July the provider replied 'I've done the job and sent you the invoice yesterday' (event-020, untrusted); no invoice is on file and documents were skipped as 'No further documents to add' (event-023).
- Ticket moved to Result and closed (event-021, event-022, event-027) although landlord confirmation was flagged outstanding (event-024) and 'keys return confirmed' (event-026) with no record of a key being issued.
**Gap:** Whether any attendance took place and whether the lock now works: no tenant confirmation, no invoice, no photos, no access record. Also unknown whether this landlord has any standing spend cap on file (none visible).
**Options:**
- Hold the closure, withhold the invoice, await the tenant's and provider's replies (requests already sent, 3 working days); reopen and re-book if the tenant says no one attended.
- Accept the provider's claim, obtain the invoice and put it to the landlord for approval before any payment (the spend was never quoted or approved).
- Reopen now and instruct an alternative locksmith with a priced quote to the landlord, treating the Juniper job as unproven.
**Recommended:** Hold the closure and withhold the invoice until the tenant confirms the lock works and Juniper Surveying produce the invoice, photos and attendance date.
**Default if no answer:** If neither tenant nor provider replies within 3 working days, treat the work as unproven: no invoice to the landlord, reopen and re-book with a quote for the landlord's approval.
**Deadline:** 3 working days from 28 July 2025 for both replies; CLK-S11 runs from the report of 25 July 2025.
**Undo:** No spend committed by me; no contractor instructed and no invoice forwarded. The two verification messages (ACT-1, ACT-2) can be superseded by a call if the PM accepts the closure.
**Context:** event-006, event-010, event-012, event-016, event-019, event-020, event-023, event-024, event-026, event-027, ACT-1, ACT-2, ACT-3

Promises made or recorded:
- agency → tenant: Re-book a visit at a convenient time if nobody attended or the lock still does not work [open]
- provider → agency: Attendance date, work carried out, photos and a copy of the invoice by 3 working days from 28 July 2025 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
