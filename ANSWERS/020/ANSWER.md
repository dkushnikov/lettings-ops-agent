# ANSWER — Case 020 — Kitchen socket maintenance request

**Disposition:** ESCALATED · **Urgency:** emergency · **Case type:** electrical_fault · **Playbook:** emergency-hazard

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Kitchen socket burning smell reclassified as an electrical emergency: tenant given safety advice, emergency electrician instructed to make safe, landlord told, handed to manager.
**Stage:** work_in_progress
**Last update:** 2025-04-12 16:42:00 UTC (event-025) · **Decided:** 2026-10-10 15:43 UTC
**Next step:** Property manager to make a welfare call to the tenant this evening, confirm the electrician's attendance/ETA, and obtain landlord or on-call manager approval for any remedial repair above the £250 make-safe ceiling.

Definition of done (2/7 done):
- [x] made_safe: First safety action for the hazard sent to the occupant, acknowledged where possible — ACT-1 — electrical first action sent to tenant (isolate circuit if safe, do not touch socket, 999 if smoke/sparks); no such guidance had been given before (event-009, event-025)
- [ ] emergency_dispatch: Emergency contractor instructed under the emergency mandate with a confirmed attendance time — ACT-2 — emergency electrician instructed for make-safe (≤£250); attendance time not yet confirmed by the contractor
- [x] landlord_informed: Landlord told of the hazard, the dispatch and the expected cost band — ACT-3 — hazard, dispatch and £250 make-safe cost band sent to landlord
- [ ] welfare: Vulnerable occupant identified; a welfare call or temporary measure arranged by a human — 10-year-old child in occupation (event-004); welfare call is a human action — in this escalation card
- [ ] hazard_cleared: Contractor confirms the hazard is cleared, or a human owns the case until it is — No inspection or isolation has taken place (event-023, event-025); property manager owns the case until the electrician confirms it is made safe
- [ ] follow_up_work: Any permanent repair raised as a maintenance request with the landlord's approval — No quote exists yet; remedial repair above £250 needs landlord / on-call manager approval (APR-EMERGENCY-REPAIR)
- [ ] closed: Outcome confirmed by a human and the request closed — Emergency cases are never closed without a human confirming the outcome (playbook step 7)

## 1. Decision

Reclassified as an electrical emergency (burning smell + warm socket face persisting ~8.5 hours, child in occupation). Sent the rulebook electrical first action to the tenant (ACT-1), instructed an emergency electrician for make-safe attendance up to £250 under CAP-DISPATCH-EMERGENCY (ACT-2, overriding the landlord's "handyman only / keep costs controlled" instruction at event-006/event-016), informed the landlord of the hazard, dispatch and cost band (ACT-3), logged the file note (ACT-4). Escalating to the property manager for welfare follow-up (ESC-VULNERABLE), confirmation of attendance, and the repair-spend decision above the £250 make-safe ceiling (APR-EMERGENCY-REPAIR) — the landlord has not replied to the authority requests at event-020 and event-024.

Safety actions taken first:
- ACT-1: sent the electrical first action to the tenant — do not touch or use the socket, isolate the kitchen circuit at the consumer unit if safe (main switch if the breaker cannot be identified), do not open the consumer unit, leave and call 999 if smoke, sparks or a stronger burning smell, keep a window open (triggered by event-001, event-017, event-025)
- ACT-2: emergency electrician instructed for same-day make-safe attendance under CAP-DISPATCH-EMERGENCY (≤£250)
- ACT-3: landlord informed of the hazard, the dispatch and the cost band immediately after dispatch
- Declined to rely on a general handyman for a suspected fixed-wiring fault (event-011, event-015)
- Did not authorise entry on landlord-held keys in the tenant's absence; the landlord's SMS (event-021) is ambiguous and unconfirmed

Actions deliberately withheld:
- Did not instruct the handyman to enter using landlord-held keys in the tenant's absence (event-019, event-021) — no tenant consent for unaccompanied access.
- Did not seek landlord approval before the make-safe dispatch (emergency duty overrides APR-ALWAYS-ASK / APR-SPEND-OVER-CAP).
- Did not commit to any repair cost or allocate liability for the fault (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-EMERGENCY, APR-EMERGENCY-REPAIR, CAP-NOTIFY, CAP-LOG, ESC-SAFETY, ESC-VULNERABLE, PRO-PII, PRO-TENANT-LIABILITY, CLK-S11, CLK-AWAAB-PRS
Rules applied by the policy gate: CAP-DISPATCH-EMERGENCY, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported a hot/burning smell at the kitchen counter socket and a warm socket face at 08:14 on 2025-04-12 after a kettle was used; kettle unplugged. [index, event-001; high]
- F2: At 16:42 the faint burning smell was still noticeable, the socket unused, no breaker switched off and the fridge still powered. [event-025; high]
- F3: Occupant household includes a 10-year-old child; tenant was alone with him at the property during the day. [event-004; high]
- F4: No emergency-response guidance had been communicated to the tenant before this agent's message. [event-009, event-025; high]
- F5: The landlord's handyman Rowan Pike does not carry out fixed-wiring repairs and has no electrical test equipment; he did not enter the property and no inspection or isolation took place. [event-011, event-015, event-023; high]
- F6: Landlord asked for costs to be controlled, nominated his handyman, and has not approved an electrician call-out or any electrical repair; he did not answer the authority requests at 13:14 and 15:02. [event-006, event-016, event-020, event-024; high]
- F7: Tenant consented to a contractor visit and to sharing symptoms and access details on 2025-04-12 (event-013); she is back at the property from about 16:30. [event-013, event-025; high]

Conflicts between sources:
- Landlord instructs attendance by a general handyman; the handyman states he cannot carry out or test fixed wiring, so his attendance cannot make a suspected electrical fault safe. → Emergency safety duty (CAP-DISPATCH-EMERGENCY, s.11) overrides the landlord's cost/contractor instruction for making safe; qualified electrician dispatched and landlord informed (ACT-2, ACT-3). (source_hierarchy)

Red flags:
- [safety_hazard] Reported burning smell and heat at a kitchen socket persisting ~8.5 hours with no isolation, inspection or safety advice — potential loose connection / overheating accessory with fire risk. → Emergency reclassification, safety-first message to tenant (ACT-1), emergency electrician dispatched (ACT-2), landlord notified (ACT-3), escalated to property manager.
- [vulnerability] 10-year-old child in the household at a property with a suspected electrical fire risk (ESC-VULNERABLE). → Welfare follow-up requested in the handover; no health or family detail shared with the contractor beyond 'priority attendance'.
- [data_quality] Landlord's instruction to use a general handyman conflicts with the handyman's own statement that he cannot do fixed-wiring work or test; the tenant's warmth report changed from touch to near-touch with no photo, reading or test available. → Recorded; emergency duty applied regardless (playbook decision point: landlord instruction does not delay make-safe).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "020", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed (ledger) | message=Nora — treating this as an electrical emergency. Please do… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | assign_contractor | completed (ledger) | trade=electrician, description=EMERGENCY make-safe at 8 Brindlewick Row, Oakhollow, ZZ1 1Z…, urgency=emergency, estimated_cost_gbp=250 | {"id": "ACT-2"} | CAP-DISPATCH-EMERGENCY |
| 5 | notify_landlord | completed (ledger) | message=Mr Vane — update on 8 Brindlewick Row. The kitchen socket r… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | add_note | completed (ledger) | note=Case 020 reclassified emergency (electrical fault with burn… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Confirm welfare follow-up at 8 Brindlewick Row and approve any emergency electrical spend above the £250 make-safe ceiling tonight?
**Facts (≤5):**
- Burning smell and warm kitchen socket reported 08:14 and still present at 16:42; no smoke or sparks (event-001, event-017, event-025).
- No inspection or circuit isolation has taken place: the landlord's handyman could not get access and does not do fixed-wiring work or carry test equipment (event-011, event-015, event-023).
- Tenant sent the electrical first action at ACT-1 (isolate kitchen circuit if safe, do not use the socket, 999 if smoke or sparks); she is back at the property from 16:30 (event-025).
- Emergency electrician instructed for make-safe attendance today, ceiling £250, CAP-DISPATCH-EMERGENCY (ACT-2); landlord informed (ACT-3).
- Household includes a 10-year-old child (event-004); landlord has not answered the authority requests at event-020 and event-024.
**Gap:** Electrician's ETA and whether attendance is confirmed tonight; whether the tenant managed to isolate the circuit; the cost of any remedial repair (no quote yet); whether the landlord authorises key access in the tenant's absence (his SMS at event-021 is ambiguous and unconfirmed).
**Options:**
- Welfare call to the tenant this evening and confirm the electrician's ETA
- Pre-authorise remedial electrical work above £250 with the on-call manager so the electrician can complete on the same visit
- If no electrician can attend tonight, agree with the tenant that the kitchen circuit stays isolated overnight and book first thing tomorrow
**Recommended:** Welfare call this evening plus confirmation of the electrician's ETA; take the repair quote to the landlord or on-call manager as soon as it arrives.
**Default if no answer:** Electrician attends as instructed for make-safe only (max £250); kitchen circuit remains isolated and the socket unused until an electrician has tested it.
**Deadline:** 2025-04-12 evening — make-safe attendance today (CLK-S11; CLK-AWAAB-PRS 24-hour emergency timescale is a proposed reference only)
**Undo:** Cancel the electrician work order only if the electrician has not yet been dispatched or attended.
**Context:** event-001, event-004, event-011, event-015, event-016, event-021, event-023, event-025, ACT-1, ACT-2, ACT-3

Promises made or recorded:
- agency → tenant: Emergency electrician instructed to attend today to inspect and make safe; contractor to contact tenant with a time by 2025-04-12 evening [open]
- agency → landlord: Any remedial repair beyond making safe will be quoted and sent for approval before it is carried out [open]
- contractor (Rowan Pike) → agency: Attend 13:00–15:00 and report before doing work by 2025-04-12 15:00 [broken]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported deadline Make safe same day
- CLK-AWAAB-PRS [proposed]: Emergency hazard 24-hour reference (social-housing baseline) deadline 2025-04-13 08:14
- CLK-EICR [in_force]: EICR / remedial work within 28 days
