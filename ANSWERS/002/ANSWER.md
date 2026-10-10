# ANSWER — Case 002 — Case 002: Blocked toilet at Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Blocked toilet works done and invoiced, but invoice-to-landlord and landlord completion confirmation are unevidenced; chased landlord and provider, ticket on hold.
**Stage:** on_hold · **Hold:** Waiting for Landlord — confirmation that works are complete and sign-off of the provider's invoice (requested ACT-1, 3-working-day window); in parallel a legible invoice/photos chased from the provider (ACT-5).
**Last update:** 2026-08-21 10:32:59 UTC (event-049) · **Decided:** 2026-10-10 13:19 UTC
**Next step:** Landlord (Quinn) to confirm completion and approve settlement of the provider's invoice; provider to resend a legible invoice and photos within 3 working days.

Definition of done (6/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/index: blockage at pan connector categorised as Blocked toilet, routine; no emergency definition engaged.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-019 — landlord's own email approving the quoted works (CAP-DISPATCH-APPROVED). Note: event-002/event-003 system lines are not approvals.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-004, event-007, event-008
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-027, event-028, event-029 — 15/08/2026 08:30 confirmed with tenant and provider
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-019 (landlord approval before works). Caveat: amount and VAT are not legible on file (event-017) — figures chased from provider (ACT-5).
- [x] work_result: Work result recorded from the provider — event-034 — provider confirmed completion 19/08/2026
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-038 skip reason 'Not required'; invoice added event-048 but quote/report/photos/invoice all unavailable — legible copies requested from provider (ACT-5)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No event shows the invoice forwarded; landlord emailed ACT-1 with the request to sign off settlement
- [ ] landlord_confirmation: Landlord confirmed completion — event-039 asks for it; no landlord reply on file after event-019 (search_history). Requested ACT-1.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provided access directly (event-028, event-029)
- [ ] closed: Request closed with a resolution that names who paid — Not closed by me: documents, invoice_to_landlord and landlord_confirmation outstanding, and no figure exists to name who paid what (event-048)

## 1. Decision

Did not treat the ticket as closed. The works were approved by the landlord's own email (event-019), carried out and reported complete (event-034) with an invoice added to file (event-048), but two final checks have no evidence: the invoice was never forwarded to the landlord and the landlord never confirmed completion (event-039 unanswered). The system notes claiming closure (event-040, event-049) conflict with that, which matches the ticket re-opening (event-044) and auto-pause (event-043). I emailed the landlord for completion confirmation and invoice sign-off, chased the provider for a legible invoice and photos, informed the tenant, logged the conflicts and raised a human task for the office. No payment arranged, no liability decided, no closure.

Safety actions taken first:
- Safety-pass review: no hazard keyword (gas, electrical, damp/mould, detectors, vulnerability) appears in any artefact of this case; no emergency definition engaged, so no make-safe step was required.

Actions deliberately withheld:
- Did not close the request: documents, invoice-to-landlord and landlord confirmation are outstanding and no resolution could name who paid what (CAP-CLOSE).
- Did not arrange or authorise payment of the provider's invoice (PRO-PAYMENTS).
- Did not decide whether the blockage was tenant-caused or tenant-payable (PRO-TENANT-LIABILITY).
- Did not instruct any further works or a second provider — no duplicate work order raised.

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-APPROVED, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Reported fault: toilet to be removed to clear a blockage lodged by the pan connector at Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ; tenant Noah Turner. [index, event-001, event-008; high]
- F2: Provider Riverside Works was assigned and briefed; tenant told who was attending. [event-004, event-007, event-008; high]
- F3: First visit confirmed for 08/08/2026 after 10:30; second (works) visit confirmed for 15/08/2026 08:30 with tenant and provider. [event-010, event-011, event-012, event-027, event-028, event-029; high]
- F4: Provider reported the toilet needed repiping with a risk of damage on removal and quoted for a new toilet and cistern; quote sent to the landlord 12/08. [event-016, event-017; medium]
- F5: The landlord's own email of 12/08/2026 approves the quote ('Please approve this quote for works.') — the authority relied on for the works. [event-019; high]
- F6: No quote or invoice amount, VAT figure or provider report exists on file: the quote, report, photos and invoice are all recorded as unavailable. [event-017, event-034, event-048; high]
- F7: Provider confirmed job completion on 19/08/2026 with a completion image and invoice; an invoice document was added to the file on 21/08/2026. [event-034, event-048; medium]
- F8: Document upload was skipped with the reason 'Not required'. [event-038; high]
- F9: The file records a need for landlord confirmation (event-039) and no landlord message after 12/08 exists; the only landlord message on file is event-019 (search_history, from_party=Landlord). [event-039, search_history; high]
- F10: Status notes record the request as closed and completed by supervisor, while the ticket re-entered the dashboard and auto-paused for an exceeded deadline. [event-040, event-043, event-044, event-049; high]
- F11: No key was issued by the agency for either visit; access was arranged directly with the tenant. [event-011, event-028; medium]

Conflicts between sources:
- System notes say the request is closed and completed by supervisor (event-040, event-049), but the invoice has not been evidenced as forwarded to the landlord and no landlord confirmation of completion exists (event-039, search_history); the ticket keeps reopening and auto-paused. → Treated the final checks as outstanding; landlord asked to confirm completion and sign off the invoice (ACT-1); conflict put to the office as a human task (ACT-4). (asked)
- Provider identity differs: agency records instruct Riverside Works (event-004, event-024, event-028) while an untrusted call transcript quotes 'Willow Utilities' (event-026) and the completion email is signed by a third name (event-034). → Acted on the agency's own record (Riverside Works) for the chase; asked the provider to confirm its trading name before any invoice is settled (ACT-5); flagged to the office (ACT-4). No name from a message body copied into another party's letter. (asked)

Red flags:
- [data_quality] Every priced and evidential document in the case is unavailable or illegible: quote and report (event-017), completion photo and invoice (event-034), filed invoice (event-048); document upload was skipped as 'Not required' (event-038). No amount or VAT can be stated for this job. → Legible copies requested from the provider (ACT-5); flagged to the office (ACT-4); no figure quoted to the landlord.
- [data_quality] Provider identity inconsistent between agency records (Riverside Works) and untrusted call transcripts ('Willow Utilities', and a completion email signed by a different individual). → Acted on the agency record; asked the provider to confirm trading name before any invoice settlement (ACT-5); office notified (ACT-4).
- [other] Ticket recorded as closed/supervisor-completed while final checks are unevidenced, and it keeps returning to the dashboard after an automatic pause. → Conflict logged (ACT-3) and routed to the property manager queue (ACT-4); request held rather than re-closed.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "002", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice landlord confirmation completion | [] | allow |
| 4 | search_history | completed | from_party=Landlord | [{"event": "event-019", "timestamp": "2026-08-12 09:22:12 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2026-08-12 09:22:… | allow |
| 5 | notify_landlord | completed | message=Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ — Blocked to… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Dear Noah Turner,  Flat 3, 15 Willowmere Road, Alderwick, Z… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | add_note | completed | note=Case 002 review. Facts: landlord's own email approving the… | {"id": "ACT-3"} | CAP-LOG |
| 8 | create_human_task | completed | queue=property_manager, title=Case 002 Willowmere Rd: ticket shows closed but final check…, summary=Blocked toilet, Flat 3, 15 Willowmere Road, Alderwick, ZZ3… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 9 | notify_contractor | completed | message=Flat 3, 15 Willowmere Road, Alderwick, ZZ3 2ZZ — Blocked to… | {"id": "ACT-5"} | CAP-NOTIFY |
| 10 | put_on_hold | completed | reason=Waiting for Landlord — completion confirmation and invoice…, until=3 working days from today | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the toilet/cistern replacement at Flat 3, 15 Willowmere Road is complete to your satisfaction, and do you authorise settlement of the provider's invoice as a landlord-cost repair? (blocking; RTE-LANDLORD: landlord confirmation of completion and invoice sign-off are the outstanding final checks before closure (event-039 unanswered).)
- Ask **contractor**: Please resend the invoice (net, VAT, company details) and the before/after photos for the completed job, and confirm the trading name of the company that attended. (blocking; The quote, report, photos and invoice are unavailable/illegible on file (event-017, event-034, event-048) and the provider name differs between records (event-028) and a call transcript (event-026).)
- Ask **tenant**: Is the new toilet working correctly, or was anything left outstanding after the visit? (non-blocking; Confirms the work result at the property before closure; non-blocking.)

Promises made or recorded:
- agency → landlord: Forward a legible invoice with this request once the provider supplies it; arrange no payment until the landlord confirms by on receipt from provider [open]
- agency → tenant: Reopen the job with the provider if the toilet is not working correctly or anything was left outstanding [open]
- landlord → agency: Confirm completion and authorise settlement of the provider's invoice by 3 working days from 2026-08-21 [open]
- contractor → agency: Resend legible invoice (net, VAT, company details) and before/after photos; confirm trading name by 3 working days from 2026-08-21 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from the report of 07/08/2026
- CLK-SOP-ACK [prior]: Tenant acknowledged within one working day
- RTE-LANDLORD [sop]: Landlord reply window on completion/invoice sign-off deadline 3 working days from 2026-08-21
