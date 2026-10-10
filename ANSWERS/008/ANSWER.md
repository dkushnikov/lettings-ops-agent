# ANSWER — Case 008 — Water ingress affecting two flats

**Disposition:** ESCALATED · **Urgency:** emergency · **Case type:** emergency_hazard · **Playbook:** emergency-hazard

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Active leak into Flat 2 onto a wet light fitting and bulging ceiling; emergency electrical make-safe instructed, parties updated, Flat 3 entry decision escalated.
**Stage:** work_in_progress
**Last update:** 2025-06-18 12:55:00 UTC (event-024) · **Decided:** 2026-10-10 15:39 UTC
**Next step:** Agency director / duty manager (Devra Senn) to decide on emergency entry to Flat 3 against the full tenancy wording, and to make a welfare call to Bevin Orlo (Flat 2) — before 17:30 today.

Definition of done (3/7 done):
- [x] made_safe: First safety action for the hazard sent to the occupant, acknowledged where possible — event-003 and event-017 (Arlen's instructions), reinforced this session by ACT-3; tenant acknowledged at event-004 and event-023
- [x] emergency_dispatch: Emergency contractor instructed under the emergency mandate with a confirmed attendance time — ACT-1 emergency electrical make-safe to Vellum Electrical, window 12:30-13:15 confirmed at event-014/event-018; plumber attended 10:30 (event-016, event-021)
- [x] landlord_informed: Landlord told of the hazard, the dispatch and the expected cost band — ACT-4 (hazard, dispatch and GBP 250 make-safe cap); earlier calls event-006, event-011, event-019
- [ ] welfare: Vulnerable occupant identified; a welfare call or temporary measure arranged by a human — No vulnerability recorded for either occupant (get_case_details, case file); welfare call to Bevin Orlo requested from the duty manager in the handover
- [ ] hazard_cleared: Contractor confirms the hazard is cleared, or a human owns the case until it is — No contractor report yet; electrician attendance window 12:30-13:15 open (event-018); source untraced and uncontrolled (event-016, event-021)
- [ ] follow_up_work: Any permanent repair raised as a maintenance request with the landlord's approval — No scope or quote possible until the source is traced in Flat 3; landlord told no repair above the cap starts without his approval (ACT-4)
- [ ] closed: Outcome confirmed by a human and the request closed — Open emergency handed to a human; closure requires confirmed outcome

## 1. Decision

Treated as an emergency hazard (water ingress onto a live ceiling light fitting with an enlarging ceiling bulge in Flat 2). Repeated the make-safe instructions to the Flat 2 occupant, instructed Vellum Electrical as an emergency make-safe attendance within the £250 ceiling (CAP-DISPATCH-EMERGENCY), sent the Flat 3 tenant the written scope and plumber's name she asked for plus a stopcock request, and updated the landlord. Entry to Flat 3 after the tenant's express refusal, with the landlord declining to authorise and no delegated override on the agency record, is not a decision I may take: escalated to the property manager/director under ESC-SAFETY and RTE-STAFF, with welfare follow-up for both flats.

Safety actions taken first:
- Repeated to the Flat 2 occupant: stay out of the bedroom, door closed, keep away from the bulging ceiling, do not touch the fitting, wet ceiling or nearby switches, do not operate an unfamiliar breaker, leave and call 999 on sparks, smoke, burning smell or falling material (ACT-3, triggered by event-023)
- Emergency electrical make-safe attendance instructed for the wet fitting in Flat 2, window 12:30-13:15, capped at the GBP 250 make-safe ceiling (ACT-1, triggered by event-002 and event-018)
- Asked the Flat 3 tenant in writing to turn off her stopcock or be talked through where it is - a damage-limiting step needing no entry (ACT-2, water first action)
- No entry to Flat 3 attempted and no key used, consent being withheld (event-009, event-020)

Actions deliberately withheld:
- Did not authorise or arrange entry to Flat 3 - tenant refuses consent (event-009, event-020), landlord has not authorised (event-019), no delegated override exists (event-022).
- Did not call schedule_access for Flat 3 - no tenant consent, so the consent field cannot be set truthfully.
- Did not instruct any riser valve to be operated - no valve confirmed to serve Flat 3 (event-016, event-021).
- Did not discuss liability or who pays for the Flat 2 ceiling damage (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Did not request landlord approval for a repair - no quote or scope exists until the source is traced.

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-EMERGENCY, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-EMERGENCY-REPAIR, ESC-SAFETY, ESC-CONFLICT, RTE-STAFF, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-LEGAL, PRO-PII
Rules applied by the policy gate: CAP-DISPATCH-EMERGENCY, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Water is entering Flat 2 through the bedroom ceiling at a light fitting, below Flat 3's bathroom; dripping has increased and a damp ceiling bulge is reportedly enlarging. [event-001, event-002, event-012, event-017, event-023; high]
- F2: The electrical safety of the wet fitting and its circuit is unestablished; the wall switch being off does not make it safe and on-site testing is required. [event-003, event-018; high]
- F3: Flat 2's occupant has left the bedroom, keeps the door closed, and reports no sparks, smoke or fallen material. [event-004, event-017, event-023; medium]
- F4: Brindle Flow Plumbing attended Flat 2 and the common riser at 10:30 with the building manager; no source located, riser labels do not confirm a Flat 3 branch, no valve operated. [event-016, event-021; high]
- F5: Vellum Electrical offered and maintained an attendance window of 12:30-13:15 for the wet fitting, subject to access, which Bevin Orlo agreed to provide. [event-014, event-015, event-018, event-023; high]
- F6: Flat 3's tenant withholds consent to entry until she returns, not before 17:30, and asked that no key be used; she requested the plumber's name and proposed work in writing before reconsidering. [event-009, event-020; high]
- F7: The landlord of Flat 3 is away, has no key, gave no standing permission, and has not authorised entry against the tenant's refusal; he asked the agency to check the full tenancy wording. [event-006, event-011, event-019; high]
- F8: The duty manager found no documented delegated authority for staff to override the occupant's refusal; the route is the full agreement plus an agency director decision, and emergency services if there is immediate danger. [event-022; high]
- F9: No occupant vulnerability (age, health, pregnancy, children, disability) is recorded anywhere in the case file for either flat. [get_case_details, event-001, event-002; medium]

Conflicts between sources:
- The landlord points to tenancy clauses for repairs on notice and emergency repairs but cannot say whether entry is permitted after a refusal; the duty manager finds no delegated authority to override. The difference decides whether anyone may enter Flat 3 before 17:30. → Full tenancy agreement to be retrieved and the entry decision taken by the agency director; recorded and escalated, no entry attempted. (unresolved)

Red flags:
- [safety_hazard] Water dripping onto a ceiling light fitting with unestablished circuit status, plus an enlarging ceiling bulge (collapse risk) in Flat 2. → Make-safe instructions repeated to the occupant (ACT-3); emergency electrician instructed to test and isolate (ACT-1); escalated under ESC-SAFETY.
- [data_quality] Common riser labels are incomplete and no valve can be confirmed as serving Flat 3, so no supply could be isolated from outside the flat. → Recorded; riser isolation not attempted; source tracing depends on Flat 3 access.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "008", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | assign_contractor | completed (ledger) | trade=electrician, description=EMERGENCY make-safe only, Flat 2, 8 Tallowmere Row, Ossin V…, urgency=emergency, estimated_cost_gbp=250, contractor_hint=Runa Elt, Vellum Electrical (already arranged, event-014) | {"id": "ACT-1"} | CAP-DISPATCH-EMERGENCY |
| 4 | notify_tenant | completed (ledger) | message=Ms Mallow (Flat 3) - as you asked on the call at 11:48 (eve… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_tenant | completed (ledger) | message=Mr Orlo (Flat 2) - thank you for the update at 12:38 (event… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_landlord | completed (ledger) | message=Mr Pell - update on Flat 3, 8 Tallowmere Row. Water is stil… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | add_note | completed (ledger) | note=Emergency hazard (water ingress onto live ceiling fitting +… | {"id": "ACT-5"} | CAP-LOG |
| 8 | definition_of_done | failed | facts=[{"id": "F1", "statement": "Water is entering Flat 2 throug…, assumptions=["Assumption: the GBP 250 figure on ACT-1 is the emergency…, uncertainty=["Whether the tenancy agreement contains an emergency-acces…, conflicts=[{"description": "Landlord points to tenancy clauses for 'r…, red_flags=[{"kind": "safety_hazard", "description": "Water dripping o… | unknown tool | - |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Flat 3, 8 Tallowmere Row: do we enter Flat 3 before 17:30 without the tenant's consent to stop an active leak, and who makes the welfare call to Flat 2?
**Facts (≤5):**
- Flat 2 (below): water dripping onto a bedroom ceiling light fitting, dripping faster and the ceiling bulge reportedly enlarging; occupant out of the room, no sparks/smoke, nothing fallen (event-012, event-017, event-023).
- Brindle Flow Plumbing and the building manager attended Flat 2 and the common riser at 10:30: no source found, riser labels incomplete, no valve confirmed to serve Flat 3, nothing isolated (event-016, event-021).
- Vellum Electrical instructed as emergency make-safe, window 12:30-13:15, capped GBP 250 under CAP-DISPATCH-EMERGENCY (ACT-1); the electrician says the fitting cannot be assumed safe from the wall-switch position (event-018).
- Flat 3 tenant Yara Mallow refuses entry before she returns at 17:30 and asked that no key be used (event-009, event-020); landlord Niko Pell is away, has no key and has not authorised entry (event-006, event-011, event-019).
- Duty manager found no documented delegated authority to override a refusal; full tenancy wording unchecked; route is the full agreement plus an agency director decision (event-022).
**Gap:** Whether the tenancy agreement contains an emergency-access clause that survives a refusal; whether the electrician has attended and isolated the circuit; the leak source and whether any valve can isolate Flat 3; whether Yara can or will turn off her stopcock.
**Options:**
- Obtain and read the full tenancy agreement now; if an emergency-access clause applies, the director authorises accompanied entry to Flat 3 with the plumber and a witness, notifying Yara first
- Hold entry until Yara returns at 17:30 and book the plumber for 17:30-18:30 with her consent; keep the Flat 2 bedroom isolated meanwhile
- If the ceiling collapses, water reaches the fitting uncontrolled, or there is any immediate danger, call emergency services and follow their direction (event-022)
**Recommended:** Pull the full tenancy agreement and get the director's decision within the hour; in parallel keep the 17:30 consented slot with Yara as the fallback and have the plumber on standby.
**Default if no answer:** No entry to Flat 3 before 17:30; electrician makes the Flat 2 circuit safe in the 12:30-13:15 window; plumber attends Flat 3 at 17:30 with Yara's consent; duty manager welfare-calls Bevin Orlo this afternoon.
**Deadline:** 2025-06-18 17:30 UTC (Yara's return; CLK-S11 reasonable time, CLK-AWAAB-PRS 24h as reference only)
**Undo:** ACT-1 (electrical make-safe) can be cancelled with Vellum Electrical only if Runa Elt has not yet attended; messages ACT-2 to ACT-4 cannot be unsent.
**Context:** event-012, event-016, event-018, event-020, event-022, event-023, ACT-1

Promises made or recorded:
- agency → landlord: Contact the landlord before any non-routine entry to Flat 3 and before any repair above the make-safe cap by before entry [open]
- agency → tenant (Flat 3): Non-destructive leak tracing only; nothing opened and no further work without contacting her first by at attendance [open]
- contractor (Vellum Electrical) → agency: Attend Flat 2 between 12:30 and 13:15 to inspect and test the wet fitting and circuit by 2025-06-18 13:15 UTC [open]
- tenant (Flat 2) → agency: Meet the electrician and stay out of the affected bedroom by 2025-06-18 13:15 UTC [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-AWAAB-PRS [proposed]: Awaab's Law emergency-hazard timescale (reference only) deadline 2025-06-19 08:12 UTC
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
