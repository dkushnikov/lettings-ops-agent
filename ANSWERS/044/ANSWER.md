# ANSWER — Case 044 — Case 044: Window Handle Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window handle repair reported closed on an unverified provider claim; chased Cedar Homes for the invoice/attendance, asked the tenant to confirm the fix, flagged the closure and tenant-identity conflict to the office.
**Stage:** final_checks · **Hold:** Waiting for Provider — Cedar Homes to send the invoice (amount/VAT), attendance date and scope within 2 working days (ACT-2); tenant confirmation of the repair also outstanding (ACT-3).
**Last update:** 2025-02-14 09:39:55 UTC (event-027) · **Decided:** 2026-10-10 13:33 UTC
**Next step:** Cedar Homes to supply the invoice and attendance/scope details within 2 working days; property manager to decide whether to reopen the request or close it without payment (ACT-4).

Definition of done (4/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged; window identified at event-007; categorised as Window Repair Request at event-014; urgency routine (use_playbook)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-012 landlord 'Please go ahead' in reply to event-009
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-013, event-015 provider briefed; event-014 tenant told Cedar Homes would attend
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No booking confirmation from provider; reminders event-017, event-018; chase flag event-020; completion claimed without a confirmed slot (event-019)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted; no amount on file (event-019). If an invoice arrives it must go to the landlord (event-015 'only proceed after receiving our approval')
- [ ] work_result: Work result recorded from the provider — Only the provider's unverified claim at event-019; details requested ACT-2, tenant confirmation requested ACT-3
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Skip reason 'not needed' recorded at event-023, but the invoice referenced at event-019 never arrived; requested at ACT-2
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice or amount on file; nothing forwarded (ACT-2 outstanding)
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 'Need confirmation from landlord'; no landlord message after event-012
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-026 keys return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-027 marked closed, but the resolution names no payer and the checks above were outstanding; reopen-or-stand referred to property manager at ACT-4

## 1. Decision

The ticket was marked closed (event-027) with its final checks incomplete, so I did not treat it as resolved. Landlord authority to instruct exists (event-012), so no new approval is needed to have had the work done; what is missing is verified proof of the work and the invoice. I chased Cedar Homes for the invoice, attendance date and scope (ACT-2), asked the tenant to confirm the repair was actually carried out (ACT-3), recorded the record conflict over the tenant's identity and the premature closure (ACT-1) and referred both to the office rather than picking a side with a party (ACT-4). No spend was instructed: no amount exists on any artefact, and the provider brief (event-015) required approval before proceeding, so I will not forward or endorse an unseen invoice.

Safety actions taken first:
- No safety-pass keyword applies: the fault is a non-opening window handle with no hazard, no detector/gas/electrical/damp content in the artefacts; property security is unaffected as the window is stuck shut (event-001, event-007).

Actions deliberately withheld:
- Did not forward or endorse an invoice to the landlord: no invoice or amount exists on file (event-019).
- Did not ask the landlord to confirm completion while the work result is unverified and no cost is known.
- Did not re-close or re-confirm the request: final checks (work result, documents, invoice, landlord confirmation) are not satisfied (CAP-CLOSE).
- Did not instruct any further contractor spend: no priced quote and no approval naming an amount (event-015, event-012).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-CONTRACTOR, RTE-TENANT, RTE-STAFF, ESC-CONFLICT, PRO-PAYMENTS, CAP-CLOSE, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 13 Jan 2025 that the window handle fell off and the window cannot be opened at Flat 21, 129 Juniper Mews, Northbridge, ZZ9 4ZZ. [index, event-001, get_case_details; high]
- F2: Tenant identified the affected window as the one at the top of the staircase, with a broken latch. [event-007; medium]
- F3: Landlord replied 'Please go ahead' on 9 Feb 2025 to the agency's request to send a contractor to fit a new handle; no amount was named. [event-009, event-012; high]
- F4: Cedar Homes was assigned and briefed, and the tenant was told who was attending, on 9 Feb 2025; the brief required approval before proceeding on any quoted work. [event-013, event-014, event-015, event-016; high]
- F5: No appointment confirmation was ever received from the provider; two reminders were sent and the system flagged 3+ reminders with no booking. [event-017, event-018, event-020; high]
- F6: Cedar Homes emailed on 11 Feb 2025 that the job was complete with an invoice attached; the invoice attachment is unavailable and no cost figure appears anywhere on file. [event-019; high]
- F7: Document upload was skipped with the reason 'not needed' and the request was closed on 14 Feb 2025 while landlord confirmation was still flagged as needed. [event-023, event-024, event-027; high]
- F8: Key return was confirmed on 14 Feb 2025; priority was not decreased. [event-026; high]
- F9: Agency records name two different tenants and two different tenant numbers for this ticket. [event-005, event-007, event-015, event-016; high]

Conflicts between sources:
- Tenant on this ticket is addressed as 'Harriet' (agency email and her reply) but as Nora Quinn in the provider brief and tenant notice; contact numbers differ (07700 900307 vs 07700 900251). → Not decided by me; referred to the office via human task (ACT-4). No version asserted to any party; messages addressed by property, not by name. (asked)
- Provider claims the job is complete (event-019) while the agency's own tracking records 3+ reminders with no booking confirmation (event-020), and the closure checklist shows landlord confirmation outstanding (event-024) yet the request was closed (event-027). → Invoice/attendance evidence requested from Cedar Homes (ACT-2) and confirmation requested from the tenant (ACT-3); reopen-or-stand decision put to the property manager (ACT-4). (asked)

Red flags:
- [data_quality] Completion claimed with an invoice that does not exist on file, no cost ever recorded, documents skipped as 'not needed', and the request closed with landlord confirmation outstanding. → Invoice and attendance evidence requested from the provider; closure referred to the property manager; no invoice endorsed or forwarded.
- [data_quality] Two tenant names and two tenant phone numbers on the same ticket. → Conflict recorded and referred to the office; parties addressed by property address only.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "044", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice complete quote cost | [] | allow |
| 4 | add_note | completed | note=Final-checks review. (1) Closure at event-027 ran ahead of… | {"id": "ACT-1"} | CAP-LOG |
| 5 | notify_contractor | completed | message=Re: Window Repair Request, Flat 21, 129 Juniper Mews, North… | {"id": "ACT-2"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Re: window handle repair at Flat 21, 129 Juniper Mews, Nort… | {"id": "ACT-3"} | CAP-NOTIFY |
| 7 | create_human_task | completed | queue=property_manager, title=Case 044 closed with final checks outstanding + tenant-iden…, summary=Window handle repair, Flat 21, 129 Juniper Mews. Closed at… | {"id": "ACT-4"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **contractor**: Please send the invoice (amount and VAT), the date and time you attended Flat 21, 129 Juniper Mews, what was carried out (was the handle replaced and the window now opens), and any photos. The invoice referred to in your 11 February email did not reach us. (blocking; Work result, documents and invoice-to-landlord checks cannot be completed from an untrusted completion claim with no invoice (event-019).)
- Ask **tenant**: Did Cedar Homes attend, and is the window handle now fitted and the window opening normally? (blocking; Independent confirmation that the reported repair actually happened; no visit was ever confirmed by the provider (event-017, event-018, event-020).)
- Ask **property_manager**: Should the closure at event-027 stand, or be reopened pending the invoice and tenant confirmation — and which tenancy record is correct (Harriet vs Nora Quinn, 07700 900307 vs 07700 900251)? (non-blocking; Reopening a closed request and resolving a conflict between agency records are not mine to decide (ESC-CONFLICT, RTE-STAFF).)

Promises made or recorded:
- agency → contractor: Invoice, attendance date/time, scope and photos requested, reply by close of business in two working days by 2 working days from this message [open]
- agency → tenant: If no one attended or the window is still broken, the job will be reinstated with the contractor [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
