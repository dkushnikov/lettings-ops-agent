# ANSWER — Case 040 — Case 040: Washing Machine Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Washing machine job closed too early: tenant swapped in his own machine, landlord approved an inspection; reopened, landlord and tenant asked, case on hold.
**Stage:** on_hold · **Hold:** Waiting for Tenant — return date and two access windows (asked ACT-3); and Waiting for Landlord — decision on the faulty machine in the garage and inventory amendment (asked ACT-2). Chase both after 3 days (by 31 Dec 2026).
**Last update:** 2026-12-28 06:30:32 UTC (event-013) · **Decided:** 2026-10-10 14:12 UTC
**Next step:** Tenant to give his return date and two access windows; in parallel the landlord to confirm whether the faulty machine is to be inspected/repaired (quote with VAT then goes to him for approval before any work).

Definition of done (1/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 — categorised Appliances/washing machine not starting, ROUTINE, containment steps given to tenant
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 landlord agrees to someone attending, but names no amount and predates knowledge of the tenant's swap; no standing cap on file — amount approval requested at ACT-2
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No contractor instructed; dispatch withheld until access date and an approved figure exist
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Tenant away on holiday (event-008); return date and windows requested at ACT-3
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote obtained; landlord told at ACT-2 that any quote (incl. VAT) comes to him before work
- [ ] work_result: Work result recorded from the provider — No visit has taken place
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No provider documents exist yet
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-012 marked 'completed without payment', but that closure was premature — no inspection took place and the landlord's approved check is still outstanding
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord is instead chasing for an update (event-013); answered at ACT-2
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provides access (event-002: no access codes/alarms)
- [ ] closed: Request closed with a resolution that names who paid — Reopened at ACT-1; case on hold at ACT-4 pending tenant and landlord replies

## 1. Decision

Reopened a ticket that had been closed prematurely. The tenant self-swapped the appliance (event-008) and the landlord approved an inspection minutes later (event-009), while the agency promised the tenant a visit "when you're back" (event-010) and then marked the job complete without payment (event-011, event-012). No contractor is instructed and no spend is committed: there is no standing spend cap on file and the landlord's approval names no amount, so a priced quote must be approved before work (APR-SPEND-OVER-CAP, RTE-LANDLORD). I replied to the landlord's chase (event-013) with the position and the decision he owns, asked the tenant for a return date and access windows plus a leak/electrical check after the DIY swap, logged the reopening and the premature closure, and put the case on hold. The ticket now waits on two named parties, so it finishes as request_info rather than an escalation; no safety hazard has been reported by any party.

Safety actions taken first:
- Asked the tenant to confirm there is no leak, damp patch, drip or socket/plug issue following the DIY machine swap on pipework with no isolation valves, and to report any water or electrical sign immediately for emergency handling (ACT-3).
- Confirmed no occupant vulnerability, no loss of an essential service and no hazard reported in any artefact; ESC-VULNERABLE and ESC-SAFETY not triggered.

Actions deliberately withheld:
- Did not instruct a contractor: although the landlord approved an inspection in his own message (event-009, CAP-DISPATCH-APPROVED), no amount is named, no standing cap is on file, and the tenant is away with no access date — dispatching would book nothing and could commit unapproved spend (APR-SPEND-OVER-CAP).
- Did not schedule access: no tenant consent or return date on file (CAP-SCHEDULE-ACCESS).
- Did not close the request: multiple definition-of-done items are pending.
- Did not decide whether the tenant bears any cost or consequence for swapping the appliance himself, or whether the landlord's appliance is now his liability (PRO-TENANT-LIABILITY).
- Did not state a repair cost or an appointment date — no quote or booking exists.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-SCHEDULE-ACCESS, APR-SPEND-OVER-CAP, CAP-DISPATCH-APPROVED, RTE-LANDLORD, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 15, 55 Alder Lane, Northbridge, ZZ1 6ZZ; tenant reported the Juniper NBL-040-4451 washing machine fills with water but does not start the cycle, no error codes, reset tried. [index, event-001, get_case_details; high]
- F2: Intake classified the issue Appliances / washing machine not starting, severity ROUTINE, confidence high; containment advice given to the tenant; no pets, no access codes or alarms. [event-002; high]
- F3: The tenant's report states there are no isolation valves on the water pipes and offers their own machine as a replacement, asking for the existing machine to be checked first. [index, event-001; high]
- F4: Agency asked the landlord on 24 Dec 10:02 how to proceed and told the tenant at 10:04 it would revert; a 3-day wait was logged. [event-004, event-005, event-006; high]
- F5: On 24 Dec 11:47 the tenant emailed that he had swapped the machines himself and stored the faulty one in the garage, as he was leaving for holiday soon. [event-008; medium]
- F6: On 24 Dec 12:12 the landlord emailed agreeing to have someone attend the flat to check the washing machine issue; no amount, contractor or date is named. [event-009; medium]
- F7: At 14:42 the agency told the tenant 'I will have someone check this when you're back at a later date' and then marked the ticket 'Completed- no further action' / 'completed without payment'. [event-010, event-011, event-012; high]
- F8: On 28 Dec the landlord asked for an update and whether any action is required from his side. [event-013; medium]
- F9: No contractor has been instructed and no cost has been incurred on this ticket; the action ledger was empty before my actions. [get_action_ledger; high]
- F10: No landlord standing spend limit is on file for this property, so the default cap of £0 applies and any spend needs the landlord's approval of a named amount. [CAP-DISPATCH-ROUTINE, APR-SPEND-OVER-CAP; high]
- F11: No leak, water ingress, electrical fault or occupant vulnerability has been reported by any party; the safety keywords present (electrical/water adjacency of an appliance swap) are checks, not reported hazards. [index, event-002, event-008; medium]

Conflicts between sources:
- The ticket was closed as complete and 'without payment' while an open promise to the tenant (a later inspection) and the landlord's approval for an inspection both remained live. → Treated the closure as premature: reopened and put on hold (ACT-1, ACT-4). The landlord's own chase (event-013) confirms he does not regard the matter as finished. No party was told the ticket was or was not validly closed. (tool_check)
- Sequencing: the landlord approved an engineer visit 25 minutes after the tenant said he had already swapped the machines, so it is unclear whether the landlord knew the swap had happened when he approved. → Put to the landlord at ACT-2: confirm whether he still wants the faulty machine inspected now that the tenant's own machine is in use. (asked)

Red flags:
- [data_quality] Ticket marked 'Completed- no further action' and 'completed without payment' (event-011, event-012) while an inspection promised to the tenant (event-010) and approved by the landlord (event-009) was still outstanding — the landlord's chase (event-013) shows the closure was wrong. → Reopened and logged at ACT-1; case placed on hold at ACT-4; landlord given the true position at ACT-2.
- [other] Appliance swap carried out by the tenant himself on pipework the report says has no isolation valves (event-008, index) — risk of leak or a poorly made electrical/water connection, though no leak or fault has been reported. → Asked the tenant to confirm no leak, damp or socket issue and to report any water or electrical sign immediately as an emergency (ACT-3). Not recorded as a safety_hazard: nothing has been reported or observed.
- [data_quality] Party messages are third-person summaries naming 'Rowan' (tenant email) and 'Oliver' (landlord email); names inside message bodies were not copied into letters to other parties. → Addressed each party by role only; no cross-quoting of names.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "040", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=holiday return access date washing machine swapped garage | [] | allow |
| 4 | search_history | completed | query=approval cap contractor instruct | [] | allow |
| 5 | add_note | completed | note=Reopening for follow-up. Ticket was marked "Completed- no f… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_landlord | completed | message=Address: Flat 15, 55 Alder Lane, Northbridge, ZZ1 6ZZ — was… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Address: Flat 15, 55 Alder Lane, Northbridge, ZZ1 6ZZ — was… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | put_on_hold | completed | reason=Waiting for Tenant — return date and two access windows for…, until=3 days from 2026-12-28 (chase both parties if no reply) | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: What date do you return to the property, and which two access windows suit you for an appliance engineer to inspect the faulty machine (24 hours' notice minimum)? (blocking; No visit can be booked without the tenant's consent and availability (CAP-SCHEDULE-ACCESS, RTE-TENANT); the history gives no return date.)
- Ask **tenant**: Since the machines were swapped with no isolation valves on the pipes, has there been any leak, damp patch, drip or any issue with the socket/plug? (non-blocking; Safety check on a DIY swap involving water and a socket; no hazard has been reported, this confirms it (ESC-SAFETY check, not a reported hazard).)
- Ask **landlord**: Should the faulty Juniper NBL-040-4451 machine now in the garage be inspected/repaired, disposed of, or left with the tenant's own machine in use — and do you want the inventory amended to record the tenant's machine? (blocking; Landlord owns the decision on works at his cost and on the appliance/inventory (RTE-LANDLORD); his approval at event-009 predates knowing the tenant had already swapped the machines.)
- Ask **landlord**: Please confirm a spend figure (or a standing limit) we may work to; otherwise we will return with the engineer's quote including VAT for approval before any work starts. (blocking; No standing cap is on file (default £0) and event-009 names no amount (APR-SPEND-OVER-CAP).)

Promises made or recorded:
- Northbridge Lettings → tenant: Someone will check the washing machine when the tenant is back from holiday [open]
- Northbridge Lettings → tenant: Update the tenant once the landlord replies; no date given until an engineer is confirmed [open]
- Northbridge Lettings → landlord: Obtain a quote and put the amount including VAT to him for approval before any work starts; hold the file open pending his reply [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-LANDLORD-REPLY [sop]: 3-day wait for landlord/tenant reply deadline 2026-12-31
