# ANSWER — Case 042 — Case 042: Washing Machine Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Closed washing-machine repair reopened at final checks: invoice amount, attendance date and landlord confirmation unreconciled; asked contractor, landlord and tenant.
**Stage:** final_checks · **Hold:** Waiting for Provider — Lantern Services to confirm attendance date, work done and invoice total (3 working days, from ACT-2); then Waiting for Landlord for confirmation of completion (ACT-3).
**Last update:** 2024-02-28 20:51:40 UTC (event-031) · **Decided:** 2026-10-10 14:12 UTC
**Next step:** Lantern Services to confirm attendance date, work carried out and the final invoice total incl. VAT within 3 working days; then landlord (Mercer) to confirm completion at that cost before the ticket can stand as closed.

Definition of done (5/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (categorised Heating & Hot Water, ROUTINE); tenant acknowledged event-005
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-008 landlord's own email approving an engineer
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010, event-012, event-013
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-017/018/019 slot confirmed to tenant and provider, though the recorded time conflicts with event-016
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-029 — job completed on the call-out, no quote produced
- [ ] work_result: Work result recorded from the provider — event-025 reports the repair, but event-022 shows the contractor still scheduling on 27/02; confirmation requested from contractor (ACT-2) and tenant (ACT-4)
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-029 skip reason recorded
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-025 states the cost but the invoice (event-024, GBP 75.11, due 22/07/2026) is unreconciled; landlord told it follows (ACT-3)
- [ ] landlord_confirmation: Landlord confirmed completion — event-030 flagged it as needed; no landlord reply in the history; requested at ACT-3
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant gave access (event-002 — no access considerations)
- [ ] closed: Request closed with a resolution that names who paid — event-031 closed the request, but the resolution does not name who paid and items above remain open

## 1. Decision

The ticket was closed at event-031 with final-check items unresolved: no landlord confirmation of completion on file (event-030 flagged "Need confirmation from landlord"), the provider invoice figure is unreconciled (GBP 75.11 with a 22 July 2026 due date at event-024 vs "£75 + VAT" reported at event-025), and event-022 shows the contractor still seeking to schedule a visit on 27/02, which conflicts with the completion report of 28/02. Within my mandate I recorded the inconsistencies (ACT-1) and asked the three owning parties for the facts that settle them: contractor for attendance date, work done and invoice total (RTE-CONTRACTOR); landlord for confirmation that the job is complete at that cost (RTE-LANDLORD); tenant for confirmation the machine now heats on 60°C+ (RTE-TENANT). No new dispatch, no spend and no payment were made; liability was not decided. The repair itself (appliance wiring to the heating element) carries no reported hazard — no burning smell, sparks or shock risk in any artefact, and the property's own hot water was unaffected (event-002) — so no emergency switch and no safety red flag, only the recorded check.

Safety actions taken first:
- Safety-pass check: reported work was replacement of wiring to the appliance heating element; no burning smell, sparks, shock risk, gas or water hazard reported in any artefact and the property's own hot water was unaffected (event-002) — no emergency criteria met, routine retained.
- Told the tenant to stop using the appliance and report immediately if a burning smell, sparks or tripping electrics appear (ACT-4).

Actions deliberately withheld:
- Did not re-close the request or re-affirm closure while work result, invoice and landlord confirmation remain unconfirmed (CAP-CLOSE).
- Did not instruct any further contractor attendance or spend — no landlord approval naming an amount (APR-SPEND-OVER-CAP).
- Did not approve, pay or dispute the invoice (PRO-PAYMENTS).
- Did not share occupancy or tenant personal detail with the provider beyond the job need (PRO-PII).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, RTE-CONTRACTOR, RTE-LANDLORD, RTE-TENANT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-PII, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the washing machine does not heat water on cycles of 60°C or above; property hot water supply unaffected and no pets or access constraints. [index, event-001, event-002; high]
- F2: Intake classified the issue as Heating & Hot Water, severity ROUTINE, medium confidence. [event-002; high]
- F3: Landlord replied 'Yes please arrange an engineer, thank you' on 23/02 20:22 UTC — approval to instruct, with no amount named. [event-008; high]
- F4: Lantern Services was assigned and briefed; tenant was told who was attending. [event-010, event-012, event-013; high]
- F5: A visit was recorded as 23/02/2024 15:25 and confirmed to both tenant and provider, though the call transcripts record a slot agreed for 'Tuesday at 1pm'. [event-015, event-016, event-017, event-018, event-019; medium]
- F6: On 27/02 the contractor called the tenant asking for a callback to schedule his visit. [event-022; medium]
- F7: Contractor invoice email states GBP 75.11 due by 22 July 2026. [event-024; medium]
- F8: Agency told the landlord on 28/02 that the engineer repaired the fault by replacing the wiring to the heating element for £75 + VAT. [event-025; high]
- F9: Document upload was skipped with the reason 'Job completed on call out, no photos or quote'. [event-029; high]
- F10: The ticket recorded that landlord confirmation was still needed and was then closed 53 seconds later with no landlord reply in the visible history. [event-030, event-031; high]
- F11: No landlord standing spend cap or standing instruction is on file in this case record; the only authority to spend is the landlord's own approval at event-008. [get_case_details; medium]

Conflicts between sources:
- Completion report (28/02) versus the contractor still trying to schedule a visit on 27/02. → Asked Lantern Services to confirm the actual attendance date and work carried out (ACT-2); asked the tenant to confirm the machine now heats (ACT-4). (asked)
- Invoice amount/date mismatch: GBP 75.11 due 22 July 2026 versus £75 + VAT reported to the landlord. → Asked the contractor for the final total and VAT position before the invoice is forwarded (ACT-2); landlord told the figure is being reconciled (ACT-3). (asked)
- Recorded visit slot 23/02 15:25 versus the transcripts' 'Tuesday at 1pm'; the confirmation was also sent at 23:21 UTC on 23/02, after the slot it confirms. → Recorded in the case note (ACT-1); attendance date put to the contractor. (unresolved)

Red flags:
- [data_quality] Provider confirmation email passed 'Pets: multiple tenants in this property' to the contractor although the tenant answered 'No' to pets; occupancy detail shared without need (PRO-PII). → Recorded in the case note (ACT-1); no further occupant detail shared with the provider.
- [data_quality] Invoice email carries an implausible due date (22 July 2026) for a February 2024 job and a total that does not match the £75 + VAT reported to the landlord. → Asked the contractor to confirm the total and VAT; no payment made or authorised (PRO-PAYMENTS).
- [data_quality] Intake captured the appliance make as 'Harbour Surveying', which is not a plausible appliance brand and was then repeated in letters to landlord and tenant. → Not repeated in my messages to any party.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "042", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Contractor | [{"event": "event-015", "timestamp": "2024-02-23 22:49:31 UTC", "channel": "Call", "from": "Contractor", "to": "Tenant", "excerpt": "[2024-02-23 22:49:31 UTC]… | allow |
| 4 | add_note | completed | note=Final-checks review of closed ticket NBL-042. Record incons… | {"id": "ACT-1"} | CAP-LOG |
| 5 | notify_contractor | completed | message=Lantern Services — job NBL-042, Flat 20, 120 Alder Lane, Ce… | {"id": "ACT-2"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Re: job NBL-042, Flat 20, 120 Alder Lane, Cedarford, ZZ9 0Z… | {"id": "ACT-3"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Dear Noah, regarding job NBL-042 at Flat 20, 120 Alder Lane… | {"id": "ACT-4"} | CAP-NOTIFY |

## 4. Human handover / information requested

- Ask **contractor**: On job NBL-042 (Flat 20, 120 Alder Lane): what date and time did your engineer attend, what work was carried out, was the machine tested heating on a 60°C cycle, and what is the final invoice total — is GBP 75.11 inclusive or exclusive of VAT? (blocking; Invoice email (event-024) states GBP 75.11 due 22 July 2026 while the completion report (event-025) says £75 + VAT; event-022 shows the contractor still scheduling on 27/02 after the recorded visit date (event-017).)
- Ask **landlord**: Do you confirm job NBL-042 at Flat 20, 120 Alder Lane is complete and are you content with the appliance engineer's charge (to be confirmed as £75 + VAT or GBP 75.11 incl.) before we forward the invoice? (blocking; event-030 recorded that landlord confirmation was still needed, and the ticket was closed at event-031 without a landlord reply in the history.)
- Ask **tenant**: Did the engineer attend, and is the washing machine now heating properly on 60°C or higher cycles? (non-blocking; Confirms the work result independently given the conflicting scheduling/completion records (event-022 vs event-025).)

Promises made or recorded:
- agency → contractor: Reply requested within 3 working days on attendance date, work done and invoice total by 3 working days from ACT-2 [open]
- agency → landlord: Invoice will be forwarded once the provider's final figure and VAT position are reconciled [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
