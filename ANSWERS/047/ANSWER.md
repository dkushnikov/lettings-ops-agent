# ANSWER — Case 047 — Case 047: Bedroom Window Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window repair marked complete without evidence; reopened for verification, tenant and landlord asked to confirm, record conflict sent to the office, nothing dispatched.
**Stage:** on_hold · **Hold:** Waiting for Tenant — tenant to confirm whether the bedroom window was repaired and now closes/locks (ACT-2); landlord asked in parallel (ACT-3); 3-day wait, then property manager decides on re-instruction
**Last update:** 2024-06-11 19:30:18 UTC (event-036) · **Decided:** 2026-10-10 13:33 UTC
**Next step:** Tenant (Eliza Jenkins) to confirm whether the bedroom window was repaired and whether it now closes and locks (asked ACT-2, 3-day wait); landlord to confirm his contractor's attendance or authorise us to instruct and quote (ACT-3).

Definition of done (2/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-006 fault scoped to bedroom window; urgency set routine; tenant advised to report immediately if the window cannot be secured (ACT-2)
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No cap on file and no landlord approval for a window job; landlord's only reply concerns a different address (event-010); asked again ACT-3
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Oscar Turner assigned and briefed, tenant told, 2024-03-01 (event-016, event-017, event-018)
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever confirmed; provider silent after three chases (event-020, event-022, event-024, event-026)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever received from any provider (search_history: no contractor messages)
- [ ] work_result: Work result recorded from the provider — event-035 completion note has no provider report or source; tenant asked to confirm (ACT-2)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice on file and no skip reason recorded
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-036 marks completed without payment, but the reason is unevidenced; landlord asked whether his own contractor did the work (ACT-3)
- [ ] landlord_confirmation: Landlord confirmed completion — No landlord message confirming completion; asked ACT-3
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant arranges access directly (event-018)
- [ ] closed: Request closed with a resolution that names who paid — System marked it complete (event-036) without verification; closure not accepted — ACT-1, ACT-5

## 1. Decision

Did not accept the system closure. The window repair at Flat 24 is not verifiably done: the assigned provider (Oscar Turner) never replied to three chases, the completion note (event-035) and "completed without payment" flag (event-036) carry no provider report, photos, invoice, tenant confirmation or landlord message, and the landlord's only contractor arrangement on file is a plumber at a different address (event-010). I did not instruct any contractor — no standing spend cap is on file and the landlord has never approved a window job, so APR-SPEND-OVER-CAP / APR-ALWAYS-ASK apply. Within authority I logged the conflict (ACT-1), asked the tenant to confirm the current state of the window (ACT-2), asked the landlord to confirm whether his own contractor attended Flat 24 or whether we may instruct and quote (ACT-3), raised an office task on the Oscar Turner / "Dawson" record conflict (ACT-4) and put the ticket on hold (ACT-5). The case now waits on named parties, so it finishes as request_info rather than an escalation; the record conflict is with the office in parallel.

Safety actions taken first:
- Asked the tenant whether the window now closes and locks, with an instruction to report immediately if it cannot be secured (insecure property would move this to emergency handling) — ACT-2

Actions deliberately withheld:
- Did not dispatch a contractor: no standing spend cap on file and no landlord approval for a window job (APR-SPEND-OVER-CAP).
- Did not close the request: work result, documents, invoice/payment reason and landlord confirmation are all unevidenced (CAP-CLOSE).
- Did not tell any party which record is correct about the provider or the address (ESC-CONFLICT routing to the office).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-TENANT, RTE-LANDLORD, ESC-CONFLICT, CLK-S11, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 21 Feb 2024 that the bedroom window at Flat 24, 150 Copperfield Walk, Kingshaven, ZZ3 7ZZ is not closing properly. [index, event-001; high]
- F2: The toilet element of the original report was withdrawn by the tenant ('My mother managed to fix the toilet'), leaving only the window. [event-006, event-011; high]
- F3: Agency acknowledged the tenant on 22 Feb 2024 and told them the landlord had been asked. [event-003, event-013; high]
- F4: The landlord's only reply in the history says he arranged a plumber for Flat 18, 88 Alder Lane, Willowbank — a different property from this ticket — and says nothing about the window. [event-010; high]
- F5: No landlord approval for a window job and no standing spend cap appear anywhere in the record. [get_case_details, search_history; high]
- F6: Provider Oscar Turner was assigned and briefed on 1 Mar 2024 and the tenant was told he would attend; three reminders followed (4, 6, 8 Mar) and event-026 records 3+ unanswered reminders. [event-016, event-017, event-018, event-020, event-022, event-024, event-026; high]
- F7: No message from any contractor exists in the visible history (search_history from_party=Contractor returned no results); no quote, photos or invoice are on file. [search_history; high]
- F8: Holds from 11 Mar to 30 May 2024 cite 'awaiting update from Dawson', a name that appears nowhere else on the ticket. [event-027, event-028, event-029, event-030, event-031, event-032, event-033, event-034; high]
- F9: On 11 Jun 2024 system notes state 'Landlord's contractor confirmed job complete' and 'Task has been completed without payment', with no provider report, documents, tenant confirmation or landlord message behind them and no statement of which job or address. [event-035, event-036; high]
- F10: No visit slot was ever confirmed with the tenant; the last substantive contact with the tenant was 22 Feb 2024. [event-013, event-017, search_history; high]

Conflicts between sources:
- Who holds the window work order: the agency's assignment names provider Oscar Turner, while every hold note from 11 Mar onwards awaits 'Dawson'. → Not decided by me and not put to a party; recorded and sent to the office as a human task (ACT-4). Routine reversible steps continued meanwhile: tenant and landlord updated at the Flat 24 address on the agency's own record. (asked)
- Completion: system notes say the landlord's contractor completed the job (event-035/036), but the landlord's only stated arrangement was a plumber at a different address (event-010), the toilet was already withdrawn (event-006), and no provider report or documents exist for a window repair. → Closure treated as unverified; tenant asked whether the window was repaired and whether it now closes/locks (ACT-2), landlord asked whether his contractor attended Flat 24 (ACT-3). (asked)

Red flags:
- [data_quality] Ticket was marked complete without payment on the strength of an unsourced system note, while the assigned provider had never responded and the tenant was never asked; the landlord's reply refers to a different property (Flat 18, 88 Alder Lane). → Closure not accepted; conflict logged (ACT-1), office task raised (ACT-4), tenant and landlord asked to confirm.
- [safety_hazard] A bedroom window that will not close could leave the property insecure (security is an emergency definition). The tenant has not described it as insecure and reported it as a routine repair, so urgency is routine on current evidence. → Tenant told explicitly to contact us straight away if the window cannot be secured shut, in which case we treat it as urgent (ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "047", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=Dawson | [{"event": "event-027", "timestamp": "2024-03-11 18:26:36 UTC", "channel": "Hold", "from": "Agency / system", "to": "Not specified", "excerpt": "[2024-03-11 18… | allow |
| 4 | search_history | completed | from_party=Contractor | [] | allow |
| 5 | add_note | completed | note=Record conflict + unverified completion. (1) Provider of re… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_tenant | completed | message=Dear Eliza Jenkins, regarding the bedroom window at Flat 24… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_landlord | completed | message=Dear Mr Oakley, re Flat 24, 150 Copperfield Walk, Kingshave… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | create_human_task | completed | queue=property_manager, title=Case 047 — conflicting records: who held the window job, an…, summary=Flat 24, 150 Copperfield Walk — bedroom window not closing… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 9 | put_on_hold | completed | reason=Waiting for Tenant — reopened for verification: tenant aske…, until=3 days from today for tenant and landlord replies (agency 3… | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 047: The record carries red flags that need a human's confirmation (safety_hazard: A bedroom window that will not close could leave the property insecure (security is an emergency definition). The tenant has not described it as insecure and reported it as a routine repair, so urgency is routine on current evidence.); the case cannot end as needs_info.
**Facts (≤5):**
- A bedroom window that will not close could leave the property insecure (security is an emergency definition). The tenant has not described it as insecure and reported it as a routine repair, so urgency is routine on current evidence.
**Gap:** The record carries red flags that need a human's confirmation (safety_hazard: A bedroom window that will not close could leave the property insecure (security is an emergency definition). The tenant has not described it as insecure and reported it as a routine repair, so urgency is routine on current evidence.); the case cannot end as needs_info.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → tenant: Re-instruct a contractor and arrange a visit if the window was not repaired or is still faulty by On the tenant's reply [open]
- agency → landlord: No contractor instructed and no cost incurred until the landlord approves a quote [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day

## System notes

- reviewer: R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
