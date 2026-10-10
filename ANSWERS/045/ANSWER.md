# ANSWER — Case 045 — Case 045: Kitchen Window and Patio Door Window Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Glazing job closed on the landlord's "all done" but he then asked about a new appointment; reopened, asked landlord and tenant to confirm, address conflict sent to the office.
**Stage:** on_hold · **Hold:** Waiting for Landlord — confirmation whether his own contractor has finished the kitchen window and patio door glazing or a further visit is due; 3 working days from 2025-04-04, then office to phone.
**Last update:** 2025-04-04 12:05:07 UTC (event-038) · **Decided:** 2026-10-10 13:33 UTC
**Next step:** Landlord to confirm whether the glazing work is complete or a further appointment is needed (asked ACT-2, 3 working day clock); tenant's answer on the state of the windows (ACT-3) corroborates.

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Fault categorised as blown glazing to kitchen window and patio door, routine; agency established the scope with the tenant at event-009. No damage-limiting advice applicable — no hazard reported (F12…
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-011, event-017 — landlord declined agency instruction and used his own contractor; no agency spend, so no cap or approval engaged (CAP-DISPATCH-ROUTINE not used).
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's own window firm handled the job (event-011, event-012); agency assigned no provider.
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — A visit was reported around 31 March/4 April (event-031, event-032) but never confirmed with the tenant on the ticket, and event-038 asks about a further appointment; tenant asked for the position an…
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-017 — landlord obtained his own quote and instructed his contractor to proceed. Amount, VAT and provider are not on the ticket; not an agency-payable quote.
- [ ] work_result: Work result recorded from the provider — Only the landlord's one-line "Good, all done!" (event-034), contradicted by event-038. No provider report, no photos.
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — Landlord's own contractor; no agency work order, so no agency photos or invoice exist. Tenant's three photos referenced at event-007 are unavailable on the ticket.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-037 — marked completed without payment; cost sits directly between landlord and his contractor (event-036).
- [ ] landlord_confirmation: Landlord confirmed completion — event-034 gave it, event-038 undermines it; re-confirmation requested (ACT-2).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; access was arranged direct with the tenant (event-012).
- [ ] closed: Request closed with a resolution that names who paid — Not re-closed: work_result, visit_confirmed and landlord_confirmation are open (CAP-CLOSE). Ticket on hold Waiting for Landlord (ACT-5).

## 1. Decision

Did not re-close the ticket. The agency closed it "completed without payment" on the landlord's "all done" (event-034, event-036, event-037), but the landlord's next message the same day asks whether a new appointment date has been arranged with the tenants (event-038), so completion is not verifiable and CAP-CLOSE's final checks are not met. No contractor instructed and no spend: the landlord used his own window firm (event-011, event-017), so CAP-DISPATCH-ROUTINE / APR-SPEND-OVER-CAP never engaged. I asked the landlord to confirm finished-or-further-visit (ACT-2), asked the tenant to confirm the state of the windows and offered to book access with 24 hours' notice (ACT-3, CAP-SCHEDULE-ACCESS), logged the status and address conflicts (ACT-1), referred the address data conflict to the office rather than asserting an address to any party (ACT-4, rule 2 / ESC-CONFLICT), and put the job on hold Waiting for Landlord (ACT-5). Routine, non-emergency: blown/failed glazing is not an emergency definition and no hazard keyword appears in the artefacts.

Safety actions taken first:
- Safety pass applied: no hazard keyword present in the artefacts — no gas, electrical, damp/mould, detector, or occupant-vulnerability content on this ticket. Glazing reported as blown (sealed-unit failure), not broken or insecure, so the property-not-secure emergency definition is not engaged and emergency-hazard was not substituted.
- Asked the tenant directly for the current condition of the kitchen window and patio door glazing so that any deterioration to broken or insecure glass is captured before closure (ACT-3).

Actions deliberately withheld:
- Did not re-close the request: work result, visit confirmation and landlord confirmation are all pending, and CAP-CLOSE permits closure only after the definition-of-done checks.
- Did not instruct a glazier or any contractor: no landlord standing cap is on file (default £0) and the landlord is using his own contractor; there is no job for the agency to dispatch (APR-SPEND-OVER-CAP, CAP-DISPATCH-ROUTINE).
- Did not assert to the landlord or tenant which of the six addresses is correct; referred it to the office instead (rule 2, ESC-CONFLICT).
- Did not escalate: no safety, vulnerability, legal threat, fraud or liability question arises; the open questions belong to the landlord and tenant, so the case finishes as request_info.
- Did not pass the tenant's contact details onward again or repeat them to any third party (PRO-PII).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-SCHEDULE-ACCESS, CAP-CLOSE, RTE-LANDLORD, RTE-TENANT, ESC-CONFLICT, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported kitchen window and patio door windows on 2025-01-14; the agency later characterised the fault as the windows being "blown" (failed double glazing) and the tenant supplied photographs but little description. [index, event-001, event-009; high]
- F2: The agency's own system required landlord approval before any instruction on this job ("Please complete landlord approval step first"). [event-002; high]
- F3: The tenant confirmed the request did not originate from the landlord. [event-006; medium]
- F4: The landlord elected to use his own contractors: an email relayed on 24 January instructs his contractor to quote for replacing the windows only, stating budget exists for the windows but not the patio door glass, which was to be quoted "for the future". [event-011; medium]
- F5: The tenant gave authorisation on 30 January for her contact details to be passed to the landlord's surveyor. [event-012; medium]
- F6: On 2025-02-15 the landlord said he had received a quote and asked his contractor to proceed; the agency kept the job open pending completion. The quote amount, VAT and provider were never recorded on the ticket. [event-017, event-018; high]
- F7: Between 1 March and 29 March the job sat on hold awaiting the landlord's window company to arrange a visit; a hold note of 29 March records "Visitng on Tuesday 6th June", a date inconsistent with the agency's 4 April question about "the visit on Monday". [event-027, event-028, event-029, event-030, event-031, event-032; medium]
- F8: On 2025-04-04 11:08 the landlord replied "Good, all done!"; the agency recorded "LL completed by himself" and "Task has been completed without payment". [event-034, event-036, event-037; high]
- F9: At 2025-04-04 12:05 the landlord asked whether a new appointment date has been arranged with the tenants, 57 minutes after confirming the job was done. [event-038; high]
- F10: No agency contractor was ever instructed and no agency spend arose on this job; all work was arranged directly by the landlord. [event-011, event-017, event-036, event-037, get_action_ledger; high]
- F11: The ticket names six different property addresses across its events; only the case record and event-032 use Flat 26, 116 Copperfield Walk, Alderwick, ZZ7 8ZZ. [get_case_details, event-003, event-011, event-020, event-023, event-032, event-038; high]
- F12: Nothing in the artefacts matches an emergency definition: no gas, electrical, water ingress, heating loss, insecurity or loss of water is reported; the glazing units are described as blown, not broken open. [event-001, event-009, event-011; medium]

Conflicts between sources:
- The landlord confirms the work is complete and then asks about arranging a new appointment with the tenants, 57 minutes apart. → Asked the landlord to confirm which is correct (ACT-2, 3 working day clock) and asked the tenant to report the state of the windows (ACT-3). Ticket held open rather than re-closed. (asked)
- Agency records disagree on the property: case record Flat 26, 116 Copperfield Walk, Alderwick vs Flat 12, 182 Meadow Row, Kingshaven on every outbound template, plus four further addresses in landlord and contractor messages. → Not decided by me. Conflict logged (ACT-1) and referred to the office (ACT-4). Tenant correspondence used the case-record address only; no address asserted to the landlord. (unresolved)
- Hold note of 29 March records a visit "Tuesday 6th June" while the agency asked on 4 April how "the visit on Monday" went. → Immaterial to the next step; noted as data quality. Completion is being confirmed with the landlord and tenant directly. (unresolved)

Red flags:
- [data_quality] Six different property addresses appear across one ticket, including in outbound agency emails to the tenant and landlord. Any one of them could have sent a contractor or a letter to the wrong flat. → Logged (ACT-1) and referred to the property manager queue (ACT-4); used only the case-record address with the tenant and no address with the landlord.
- [data_quality] Two landlord emails are written in the third person about the landlord himself ("Theo has arranged...", "Theo is inquiring..."), suggesting a relayed or machine-summarised message rather than the landlord's own words; both carry addresses that match no other record. → Treated as evidence only and put the question back to the landlord in his own channel for confirmation (ACT-2) rather than acting on the content.
- [other] Job was marked complete and "completed without payment" on a four-word landlord email with no provider report, photos or tenant confirmation, then contradicted within the hour. → Declined to re-close; held open pending landlord and tenant confirmation (ACT-5).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "045", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Reopening review. Conflict in the landlord's own statements… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Job Id: NBL-045-9445 — kitchen window and patio door glazin… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_tenant | completed | message=Job Id: NBL-045-9445 — kitchen window and patio door glazin… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | create_human_task | completed | queue=property_manager, title=Case 045 — address data conflict across ticket + job closed…, summary=Two issues for the office.  1) Which property. The agency's… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 7 | put_on_hold | completed | reason=Waiting for Landlord — landlord confirmed "all done" (event…, until=3 working days from 2025-04-04 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Is the kitchen window and patio door glazing work at this tenancy now finished by your own contractor, or is a further visit still due? If a further visit is due, should we arrange access with the tenant, and do you have a date or a contact for the contractor? (blocking; The landlord said "all done" (event-034) and then asked about a new appointment date with the tenants (event-038); completion cannot be confirmed and only the landlord can settle it, as it is his own contractor (RTE-LANDLORD).)
- Ask **tenant**: Are the kitchen window and the patio door glazing now repaired or replaced at your flat, or is work still outstanding? If a further visit is needed, which days and times suit you? (blocking; The tenant is the only party who can confirm the condition at the property and owns access consent (RTE-TENANT, CAP-SCHEDULE-ACCESS).)
- Ask **property_manager**: Which property does job NBL-045-9445 relate to, and please correct the job header: the case record says Flat 26, 116 Copperfield Walk, Alderwick, while the outbound templates say Flat 12, 182 Meadow Row, Kingshaven and four other addresses appear in the thread. (non-blocking; Agency records disagree about the property; the difference changes who is contacted and where any visit is booked (ESC-CONFLICT, rule 2 — recorded and referred, not decided in a message to a party).)

Promises made or recorded:
- agency → landlord: If no reply in 3 working days the job stays on hold awaiting the landlord and the office follows up by phone. by 3 working days from 2025-04-04 [open]
- agency → tenant: Any further visit will be agreed with the tenant first, with at least 24 hours' notice; no appointment confirmed without their agreement. [open]
- agency → landlord: Earlier promise by the agency to keep the job open until the work is finished — still open, hence not re-closing. [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- CLK-RRA-2025 [in_force]: Renters' Rights Act 2025 main provisions deadline 2026-05-01
