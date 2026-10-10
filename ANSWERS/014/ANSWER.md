# ANSWER — Case 014 — Heating service request at 7 Mallowmere Walk

**Disposition:** ESCALATED · **Urgency:** emergency · **Case type:** no_heating · **Playbook:** emergency-hazard

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** No heating with a vulnerable occupant at 10°C: emergency diagnostic booked 15 Jan 09:00–11:00 at £168; welfare and interim warmth handed to the duty manager.
**Stage:** visit_scheduling
**Last update:** 2025-01-14 17:08:00 UTC (event-019) · **Decided:** 2026-10-10 15:41 UTC
**Next step:** Duty manager (Priya Noll) to make a welfare call to Leah Venn this evening and decide/fund interim warmth; contractor to confirm the 15 Jan 09:00–11:00 booking held to 17:30.

Definition of done (3/7 done):
- [x] made_safe: First safety action for the hazard sent to the occupant, acknowledged where possible — ACT-4: do not use the overheating heater, do not touch the boiler, gas first action, keep one room warm; follows event-012 and event-018
- [x] emergency_dispatch: Emergency contractor instructed under the emergency mandate with a confirmed attendance time — ACT-2 and ACT-3: Brackenridge Heat Services instructed for 15 Jan 09:00-11:00 (event-019); access booked ACT-1 on tenant consent event-013. Contractor's written confirmation of the booking still outs…
- [x] landlord_informed: Landlord told of the hazard, the dispatch and the expected cost band — ACT-5: hazard, dispatch and £168 incl. VAT cost band; earlier call event-009
- [ ] welfare: Vulnerable occupant identified; a welfare call or temporary measure arranged by a human — Vulnerability identified (event-003, event-004); no authority for heaters/transport/accommodation (event-007, event-017); handed to the duty manager in this escalation
- [ ] hazard_cleared: Contractor confirms the hazard is cleared, or a human owns the case until it is — Diagnostic not yet attended; booked 15 Jan 09:00-11:00
- [ ] follow_up_work: Any permanent repair raised as a maintenance request with the landlord's approval — No repair scope or quote yet; parts/remedial work excluded from the £168 call-out (event-006, event-019) and must be referred to the landlord within or above the £250 incident limit (event-014)
- [ ] closed: Outcome confirmed by a human and the request closed — Emergency case; a human confirms the outcome before closure

## 1. Decision

Treated as an emergency (no heating, January, vulnerable occupant, 10°C). Sent the tenant safety advice, instructed Brackenridge Heat Services for the £168 incl. VAT diagnostic in the 15 Jan 09:00–11:00 cancellation slot under CAP-DISPATCH-EMERGENCY (within the £250 make-safe ceiling), booked access on the tenant's existing consent, and informed the landlord. Escalating to the duty manager for tonight's welfare decision: no spending authority is on file for temporary heating, transport or accommodation, and the tenant's own heater is unsafe.

Safety actions taken first:
- Told the tenant not to use the overheating plug-in heater and not to investigate or restart the boiler (ACT-4; triggered by event-008, event-012)
- Gave the gas first action as a precaution: leave, no electrical switches, call 0800 111 999 if gas is ever smelled (ACT-4; triggered by event-003)
- Advised keeping one room warm, doors and curtains closed, and to call immediately if she feels unwell (ACT-4; triggered by event-018)
- Shared no medical details with the contractor — only that the occupant needs extra time to answer the door (ACT-2, ACT-3; PRO-PII, event-004)

Actions deliberately withheld:
- Did not commit spend on temporary heaters, transport or accommodation — no authority on file (event-007, event-017).
- Did not use event-014 as a landlord_approval_ref after the policy gate rejected it; dispatched under CAP-DISPATCH-EMERGENCY instead.
- Did not arrange access through the niece — she is not authorised to provide access or approve work (event-004).

Execution notes (what the runtime observed about the actions above):
- Action 3 assign_contractor: FAILED (rejected: event-014 is not a landlord message in the visible history (sender: Owen Pike (Landlord)); only the landlord'…); no effect recorded.

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-EMERGENCY, CAP-NOTIFY, CAP-SCHEDULE-ACCESS, CAP-LOG, CAP-HUMAN-TASK, ESC-VULNERABLE, ESC-SAFETY, RTE-STAFF, PRO-PII, CLK-S11
Rules applied by the policy gate: CAP-DISPATCH-APPROVED, CAP-DISPATCH-EMERGENCY, CAP-LOG, CAP-NOTIFY, CAP-SCHEDULE-ACCESS

Key facts (source ids in brackets):
- F1: Heating failed at 7 Mallowmere Walk: radiators cold, controller unresponsive, boiler display blank; hot water still available; no gas smell or visible leak. [event-001, event-003; high]
- F2: Living-room temperature 12°C at 10:10 and 10°C at 16:25 on 14 January. [event-008, event-018; medium]
- F3: The tenant has a mobility impairment, cannot use stairs quickly, asked that attendees call from outside, and asked that medical details not be shared with contractors. [event-003, event-004; high]
- F4: The tenant's only plug-in heater overheats; the contractor advised it should not be used and the tenant confirmed she will not use it. [event-012, event-013; high]
- F5: Contractor offered a 15 January 09:00-11:00 cancellation slot held only until 17:30, same £168 incl. VAT diagnostic call-out, no parts or repair included. [event-019, event-006; high]
- F6: The tenant consented to access on 15 January with at least 30 minutes' notice and a direct call, cannot guarantee 17 January due to a hospital appointment, and the agency holds no key. [event-013; high]
- F7: The landlord confirmed the standing £250 urgent-repair incident authority was not withdrawn and the £168 diagnostic may be authorised without further consent; later work must stay within the incident limit or be referred. [event-014; high]
- F8: No spending authority exists for temporary heating equipment, transport or accommodation. [event-007, event-017; high]
- F9: The landlord is travelling and may not respond promptly. [event-010; medium]
- F10: An adult niece sometimes stays but is not authorised to approve work or provide access. [event-004; high]

Conflicts between sources:
- The landlord's 11:06 message asked for a quote before committing non-emergency expenditure, which appeared to conflict with the £250 standing urgent-repair authority on the property record. → The landlord's own 12:47 message confirmed the £250 incident authority stands and the £168 diagnostic may be authorised (event-014); the dispatch was in any case made under the emergency make-safe mandate. (asked)

Red flags:
- [vulnerability] Occupant with a mobility impairment in a 10°C property with no heating and no safe heater. → Emergency dispatch, safety advice, escalated for a welfare call and interim-warmth decision.
- [safety_hazard] Tenant's plug-in heater casing becomes unusually hot — fire/electrical risk; tenant has stopped using it on the contractor's advice. → Instructed the tenant in writing not to use it (ACT-4); flagged in the handover.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "014", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | assign_contractor | failed | trade=heating engineer (Gas Safe), description=No heating at 7 Mallowmere Walk, Larkfen: radiators cold, h…, urgency=emergency, estimated_cost_gbp=168, contractor_hint=Daniel Hart, Brackenridge Heat Services | rejected: event-014 is not a landlord message in the visible history (sender: Owen Pike (Landlord)); only the landlord's own message approves spend | CAP-DISPATCH-APPROVED |
| 4 | schedule_access | completed (ledger) | window=15 January 2025, 09:00-11:00 (engineer to call Leah Venn at…, tenant_consent=True | {"id": "ACT-1"} | CAP-SCHEDULE-ACCESS |
| 5 | assign_contractor | completed (ledger) | trade=heating engineer (Gas Safe), description=No heating at 7 Mallowmere Walk, Larkfen: radiators cold, h…, urgency=emergency, estimated_cost_gbp=168, contractor_hint=Daniel Hart, Brackenridge Heat Services | {"id": "ACT-2"} | CAP-DISPATCH-EMERGENCY |
| 6 | notify_contractor | completed (ledger) | message=Brackenridge Heat Services – please book the 15 January 09:… | {"id": "ACT-3"} | CAP-NOTIFY |
| 7 | notify_tenant | completed (ledger) | message=Ms Venn – update before close of office. Safety first: plea… | {"id": "ACT-4"} | CAP-NOTIFY |
| 8 | notify_landlord | completed (ledger) | message=Mr Pike – 7 Mallowmere Walk, Larkfen. Total heating failure… | {"id": "ACT-5"} | CAP-NOTIFY |
| 9 | add_note | completed (ledger) | note=Emergency classification: no heating in a cold month (Janua… | {"id": "ACT-6"} | CAP-LOG |
| 10 | definition_of_done | failed | facts=[{"id": "F1", "statement": "Heating failed at 7 Mallowmere…, clocks=[{"rule_id": "CLK-S11", "name": "Repairs within a reasonabl…, promises=[{"by": "agency", "to": "tenant", "what": "Duty manager to…, red_flags=[{"kind": "vulnerability", "description": "Occupant with a…, safety_actions=["Told the tenant not to use the overheating plug-in heater… | unknown tool | - |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Confirm the welfare call tonight and decide/fund interim warmth (heater delivery, transport or accommodation) for the vulnerable occupant at 7 Mallowmere Walk — no spending authority for these is on file.
**Facts (≤5):**
- No heating since 14 Jan: boiler display blank, controller unresponsive, hot water still on, no gas smell or leak (event-001, event-003).
- Living room 12°C at 10:10 and 10°C at 16:25; occupant has a mobility impairment and cannot use stairs quickly (event-008, event-018, event-003).
- Her only plug-in heater overheats; the engineer advised it must not be used and she has agreed not to (event-012, event-013).
- Brackenridge Heat Services instructed for the 15 Jan 09:00-11:00 cancellation slot, £168 incl. VAT diagnostic only, no parts (ACT-2, ACT-3, event-019); access booked on her confirmed consent with 30 minutes' notice and a direct call (ACT-1, event-013).
- Landlord confirmed the £250 urgent-repair incident limit covers the £168 call-out (event-014) but is travelling; duty file shows no limit for heaters, transport or accommodation (event-007, event-017).
**Gap:** Whether the contractor accepted the 15 Jan booking before the 17:30 hold expired; whether the niece's entrance is step-free; whether the occupant stays in the property tonight; the cost of any repair found on 15 Jan (not yet quoted).
**Options:**
- Welfare call to Leah Venn this evening and an overnight check-in
- Fund and deliver a safe temporary heater from an approved supplier
- Fund transport to her niece's home tonight, subject to her confirming a step-free entrance
- Fund alternative accommodation if the niece's home is not accessible
**Recommended:** Welfare call this evening plus a delivered temporary heater; arrange transport to the niece only once she confirms a step-free entrance.
**Default if no answer:** Engineer attends 15 Jan 09:00-11:00 as instructed; duty manager calls the tenant this evening and she remains in the property with no interim heating.
**Deadline:** Tonight, 14 Jan 2025 — contractor hold expires 17:30; welfare decision needed before an unheated night
**Undo:** The 15 Jan work order and access slot can be cancelled with the contractor and the tenant while the engineer has not attended.
**Context:** event-003, event-008, event-012, event-013, event-014, event-017, event-018, event-019, ACT-1, ACT-2, ACT-3, ACT-4, ACT-5

Promises made or recorded:
- agency → tenant: Duty manager to call this evening about interim warmth, transport or accommodation by 2025-01-14 evening [open]
- agency → landlord: Any repair quote from the 15 January visit will be put to the landlord before work is committed by 2025-01-15 [open]
- contractor → agency: Confirm the 15 January 09:00-11:00 booking and phone the tenant 30 minutes before arrival by 2025-01-14 17:30 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported deadline 2025-01-15
- CLK-AWAAB-PRS [proposed]: 24-hour emergency-hazard reference timescale (social-housing baseline, not a private-sector deadline) deadline 2025-01-15 08:12
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
