# ANSWER — Case 046 — Case 046: Bedroom Window Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window hinge repair was closed with no work result and no landlord confirmation on file; chased provider, tenant and landlord and asked the office to reopen for final checks.
**Stage:** final_checks · **Hold:** Waiting for Provider - Lantern Utilities to send a legible PDF invoice, completion date and photos within 2 working days of ACT-2; also Waiting for Landlord for confirmation of completion (ACT-3) and Waiting for Tenant for confirmation the window now closes (ACT-1).
**Last update:** 2025-10-07 12:32:30 UTC (event-052) · **Decided:** 2026-10-10 14:14 UTC
**Next step:** Lantern Utilities to supply the PDF invoice, completion date and photos (chased, 2 working days); in parallel the landlord to confirm completion and the tenant to confirm the window closes, then the office reopens and re-closes the request naming who paid.

Definition of done (7/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged the fault and event-004 acknowledged it to the tenant on 12 Sept; routine, no damage-limiting steps applicable to a rusted hinge
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 - landlord's own reply agreeing to a contractor
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010 provider assigned; event-012 provider briefed; event-011 tenant told Lantern Utilities would attend
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-027 provider booked 30/09/2025; event-030 and event-031 confirmed slot 10:00-17:00 to provider and tenant; event-035 reminder
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-015 quote GBP 90 plus VAT; event-018 landlord's own approval; event-020 go-ahead to provider after approval
- [ ] work_result: Work result recorded from the provider — event-036 'No work results'; event-041 is only 'Attached invoice' with the attachment unavailable; chased at ACT-2
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-048 skip reason 'not applicable'; no photos and no readable invoice on file - photos and PDF re-requested at ACT-2
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-042 and event-043 invoice emailed to landlord, though the attachment is recorded as unavailable
- [ ] landlord_confirmation: Landlord confirmed completion — event-049 'Need confirmation from landlord'; no landlord reply in the history; requested again at ACT-3
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-051 keys return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-052 closed the request, but the resolution does not name who paid and work_result and landlord_confirmation were outstanding; office asked to reopen at ACT-5

## 1. Decision

The agency ran the repair to a closure at event-052, but two definition-of-done items have no supporting evidence: a provider work result and the landlord's confirmation of completion. Authority for the spend is sound (landlord's own approval of GBP 90 plus VAT at event-018, given after the quote at event-015 and before the go-ahead at event-020), so no new approval is needed and no new work order was raised - raising one would duplicate the job booked at event-027. Within mandate I chased the provider for a legible PDF invoice, completion date and photos, asked the tenant to confirm the window now closes, asked the landlord to confirm completion, recorded the data-quality issues, and raised an office task to reopen the request for final checks (I cannot reopen a closed ticket). The case now waits on three named parties, so it ends as request_info rather than an escalation: nothing here requires a human to decide liability, legal or safety.

Safety actions taken first:
- Safety-pass check: no safety keyword material in this case - no gas, electrical, damp, mould or detector content, and no occupant vulnerability is reported. Checked the insecure-property emergency definition against the report: the tenant describes a window that does not close properly because of a rusted hinge, with no report of a window that cannot be secured, breakage or a break-in, so the case stays routine. The tenant has been asked to confirm the window now closes and secures (ACT-1); if it does not, urgency is to be raised, not lowered (priority rule).

Actions deliberately withheld:
- Did not close the request: work_result and landlord_confirmation are pending, and CAP-CLOSE allows closure only after the final checks.
- Did not dispatch or re-instruct a contractor: the job at event-020 was already instructed on the landlord's approval at event-018; a second work order would duplicate it.
- Did not request further landlord approval: the approved GBP 90 plus VAT covers the only quoted work (APR-SPEND-OVER-CAP not engaged).
- Did not state who pays or comment on the invoice being settled (PRO-PAYMENTS, PRO-TENANT-LIABILITY).
- Did not pass tenant contact or occupancy detail beyond what the job needs (PRO-PII).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, CAP-CLOSE, CAP-DISPATCH-APPROVED
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 11 Sept 2025 that the bedroom window at Flat 23, 143 Willowmere Road, Alderwick does not close properly and a hinge is rusted. [index, event-001, get_case_details; high]
- F2: No landlord spend cap or standing instruction is available in this environment; the authority relied on is the landlord's own approval in the history. [get_case_details, event-007, event-018; medium]
- F3: The landlord agreed to a contractor attending (12 Sept, 10:06) and then approved GBP 90 plus VAT for the hinge (12 Sept, 16:03); the agency instructed the provider to proceed afterwards at 16:38. [event-007, event-018, event-020; high]
- F4: Lantern Utilities booked the visit for 30 September 2025 and the slot 10:00-17:00 was confirmed to both tenant and provider on 16 September. [event-027, event-029, event-030, event-031; high]
- F5: No work result was ever recorded; the agency noted the absence on 2 October and the provider's only reply is 'Attached invoice' on 7 October with the attachment unavailable. [event-036, event-038, event-041, event-043; high]
- F6: The system asked for landlord confirmation of completion on 7 October; no landlord reply follows in the visible history, and the request was closed 74 minutes later. [event-049, event-052; high]
- F7: Agency emails name the landlord as both 'Grace' and 'Felix', and provider emails are signed 'Jenkins' and 'Mercer' for the same provider. [event-003, event-007, event-008, event-015, event-016, event-022; high]

Conflicts between sources:
- The landlord is addressed as 'Grace' in the agency's outgoing emails but the landlord's replies and the agency's later emails use 'Felix'. → The landlord's own replies settle landlord-owned questions, so the approval at event-018 stands regardless of the name used. The name discrepancy is a CRM data-quality item flagged to the office (ACT-5); no name was copied into any party letter. (source_hierarchy)
- Event-052 states all checks were completed, while event-036, event-048 and event-049 show the work result, documents and landlord confirmation were outstanding. → The specific records of missing items beat the general closing status line; the ticket is treated as at final_checks and the office is asked to reopen (ACT-5). (tool_check)

Red flags:
- [data_quality] Closure line claims all checks complete while the work result, photos and landlord confirmation are absent from the record; the invoice attachment is unreadable so the invoiced total is unverified against the approved GBP 90 plus VAT. → Chased provider for a PDF invoice, completion date and photos (ACT-2); asked landlord to confirm completion (ACT-3); asked tenant to confirm the window closes (ACT-1); office task to reopen (ACT-5).
- [data_quality] Inconsistent party names in the agency's own correspondence: landlord 'Grace' vs 'Felix'; provider contacts 'Jenkins' vs 'Mercer' for Lantern Utilities. → Recorded in the case note (ACT-4) and referred to the office (ACT-5); no name from a message body was reused in a letter to another party.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "046", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=confirm completion work result photos invoice, from_party=Landlord | [] | allow |
| 4 | search_history | completed | query=invoice completed attended window, from_party=Contractor | [] | allow |
| 5 | search_history | completed | query=invoice | [{"event": "event-038", "timestamp": "2025-10-07 10:41:42 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Contractor", "excerpt": "[2025-10-07… | allow |
| 6 | notify_tenant | completed | message=Hello Freya, regarding the bedroom window repair at Flat 23… | {"id": "ACT-1"} | CAP-NOTIFY |
| 7 | notify_contractor | completed | message=Window Repair Request - Flat 23, 143 Willowmere Road, Alder… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | notify_landlord | completed | message=Re: Flat 23, 143 Willowmere Road, Alderwick, ZZ2 6ZZ - bedr… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | add_note | completed | note=Review of closed ticket. Checklist gaps at closure (event-0… | {"id": "ACT-4"} | CAP-LOG |
| 10 | create_human_task | completed | queue=property_management, title=Case 046 closed with final checks outstanding - reopen to c…, summary=Flat 23, 143 Willowmere Road - bedroom window hinge. The re… | {"id": "ACT-5"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **contractor**: Please send the invoice for the Flat 23, 143 Willowmere Road window hinge repair as a PDF (the 7 October attachment could not be opened), confirm the date the work was completed and what was done, and attach photos. Does the invoiced total match the approved GBP 90 plus VAT? (blocking; No work result is on file (event-036) and the only provider reply is event-041 with an unavailable attachment, so completion and the amount are unverified.)
- Ask **landlord**: Please confirm you are satisfied the window repair is complete, and tell us whether the invoice emailed on 7 October opened at your end. (blocking; Landlord confirmation was requested by the system at event-049 and no reply appears in the history, yet the request was closed at event-052.)
- Ask **tenant**: Did Lantern Utilities attend on 30 September 2025, and does the bedroom window now close and secure properly? (non-blocking; Tenant-owned fact about the fault; the only independent check that the repair actually happened.)

Promises made or recorded:
- agency → contractor: If no PDF invoice, completion date and photos arrive within 2 working days, we will chase again and flag the job to the property manager as unverified. by 2 working days from ACT-2 [open]
- agency → tenant: If the window still does not close, we will arrange a return visit. [open]
- agency → landlord: Resend the invoice if the attachment did not open at the landlord's end. [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
