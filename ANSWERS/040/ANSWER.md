# ANSWER — Case 040 — Case 040: Washing Machine Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Washing machine fault: tenant fitted their own machine; ticket reopened, landlord asked whether an engineer still attends and at what cost; tenant asked for access dates.
**Stage:** on_hold · **Hold:** Waiting for Landlord — decision on whether to send an engineer for his machine and a spend figure; in parallel Waiting for Tenant for return date and access windows. Chase 31/12/2026.
**Last update:** 2026-12-28 06:30:32 UTC (event-013) · **Decided:** 2026-10-10 13:31 UTC
**Next step:** Landlord to confirm whether an engineer should attend to inspect/repair/remove his machine and the maximum spend (no cap on file); tenant to give return date and two access windows.

Definition of done (1/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (ROUTINE classification, containment steps to tenant); urgency re-set routine via use_playbook
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 approves attendance but names no amount and predates the tenant's swap; no standing cap on file — landlord re-asked at ACT-2
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No contractor instructed; spend unauthorised (APR-SPEND-OVER-CAP)
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Tenant away; return date and two access windows requested at ACT-3
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote exists; landlord asked for a ceiling or a quote-first instruction (ACT-2)
- [ ] work_result: Work result recorded from the provider — No provider has attended; tenant swapped the machine themselves (event-008)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice; none exist yet
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-012 marked completed without payment, but the ticket was reopened (ACT-4) as work remains undecided
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord is chasing for an update (event-013); reply sent ACT-2, awaiting his decision
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provides access (event-002: no access constraints)
- [ ] closed: Request closed with a resolution that names who paid — Ticket on hold (ACT-4); closure would be premature with items above pending

## 1. Decision

Reopened the prematurely closed ticket: the tenant self-swapped the machine (event-008) but the landlord's approval to send someone (event-009) and the agency's promise of a later check (event-010) were still live when it was marked completed without payment (event-011/012). No spend is authorised — no standing cap is on file and the landlord's approval names no amount — so I did not instruct a contractor. Updated the landlord in answer to his chase (event-013) and asked him to decide whether an engineer still attends and at what cost ceiling; asked the tenant for a return date and two access windows and gave leak-watch advice for the valve-less pipework. Case on hold, Waiting for Landlord.

Safety actions taken first:
- Asked the tenant to check for water under/behind the newly fitted machine (no isolation valves) and to report any leak immediately as an emergency (ACT-3).

Actions deliberately withheld:
- Did not instruct a contractor: no standing spend cap on file and the landlord's approval (event-009) names no amount and predates the tenant's swap (APR-SPEND-OVER-CAP).
- Did not book an access window: tenant is away and has given no return date (CAP-SCHEDULE-ACCESS).
- Did not re-close the request: definition-of-done items are still pending (CAP-CLOSE).
- Did not decide who bears the cost of the faulty machine or the swap (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, APR-SPEND-OVER-CAP, CAP-DISPATCH-ROUTINE, CAP-SCHEDULE-ACCESS, RTE-LANDLORD, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 15, 55 Alder Lane, Northbridge, ZZ1 6ZZ; tenant reported 23/12/2026 that the washing machine fills but the cycle never starts, no error codes, resets tried. [index, event-001, get_case_details; high]
- F2: Intake classified the issue Appliances / washing machine not starting, severity ROUTINE, with containment advice shown to the tenant; no access constraints, no pets. [event-002; high]
- F3: The pipework has no isolation valves, and the tenant offered to supply their own machine if a swap were needed. [event-001; high]
- F4: Agency acknowledged the tenant on 24/12 and emailed the landlord the same day asking how to proceed and whether to send someone. [event-004, event-005; high]
- F5: Tenant emailed on 24/12 that the faulty machine had been swapped for their own and stored in the garage ahead of a holiday (untrusted, tenant-owned fact). [event-008; medium]
- F6: Landlord emailed on 24/12 agreeing for someone to attend and check the washing machine; the message names no amount and predates knowledge of the swap. [event-009; medium]
- F7: Agency told the tenant it would have someone check 'at a later date' when they are back — an open promise with no booking. [event-010; high]
- F8: Ticket was marked 'Completed - no further action' and 'completed without payment' on 24/12 while the landlord's approval and the promised later visit were still open. [event-011, event-012; high]
- F9: Landlord chased for an update on 28/12 and asked whether any action is required from his side. [event-013; medium]
- F10: No landlord standing spend cap is on file for this property; default cap is £0, so any spend needs the landlord's own approval naming an amount. [CAP-DISPATCH-ROUTINE, APR-SPEND-OVER-CAP, get_case_details; high]

Conflicts between sources:
- Agency status records say the task is completed without payment (event-011, event-012), but the same history holds an open landlord approval to attend (event-009) and an unbooked promise of a later visit to the tenant (event-010), and the landlord is now chasing (event-013). → Treated the ticket as live: no party was told it was closed, the landlord's chase is unanswered. Recorded in the case note (ACT-1), ticket placed on hold (ACT-4) pending the landlord's decision rather than re-closed. (tool_check)
- Tenant says the machine was already swapped by them (event-008); landlord, writing 25 minutes later, agrees to send someone to check the machine (event-009) apparently unaware of the swap. → Landlord told of the swap and asked whether his instruction to attend still stands and for what purpose (ACT-2). (asked)

Red flags:
- [data_quality] Ticket closed as 'completed without payment' (event-011, event-012) with the landlord's approval and a promised visit still outstanding; the landlord's chase (event-013) shows the closure was premature. → Recorded in case note (ACT-1), ticket reopened and placed on hold (ACT-4); landlord updated (ACT-2).
- [other] Tenant self-installed their own appliance on pipework with no isolation valves (event-001, event-008) — possible leak and liability/ownership questions over the landlord's machine now stored in the garage. → Leak-watch advice to the tenant with instruction to report water immediately (ACT-3); cost/liability expressly left undecided (PRO-TENANT-LIABILITY) and flagged to the landlord (ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "040", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Case status review. Facts from visible history: routine app… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_landlord | completed | message=Flat 15, 55 Alder Lane, Northbridge, ZZ1 6ZZ — washing mach… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_tenant | completed | message=Flat 15, 55 Alder Lane, Northbridge, ZZ1 6ZZ — washing mach… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | put_on_hold | completed | reason=Waiting for Landlord — reply needed on whether an engineer…, until=2026-12-31 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Now that the tenant has fitted their own washing machine, do you still want an engineer to attend when they are back — to inspect/repair your machine, to remove it, or neither? If yes, what maximum amount may we spend (no standing limit is on file), or shall we obtain a quote for your approval first? If you prefer your own contractor, say so and we will arrange access. (blocking; RTE-LANDLORD: choosing a contractor and authorising any spend is the landlord's decision; the 24/12 approval (event-009) predates the tenant's swap and names no amount.)
- Ask **tenant**: What date are you back at the property, and which two access windows suit you for an engineer visit? Also, has any water appeared under or behind the newly fitted machine (the pipes have no isolation valves)? (blocking; RTE-TENANT: access consent and windows, and confirmation that the self-install is not leaking.)

Promises made or recorded:
- agency → tenant: Someone will be arranged to check the machine at a later date once the tenant is back [open]
- agency → tenant: We will come back to the tenant with access windows once the landlord replies [open]
- agency → landlord: Request held open pending his reply on attendance and spend limit by 2026-12-31 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-MANUAL-WAIT [sop]: Landlord/tenant reply wait (3 days) deadline 2026-12-31
