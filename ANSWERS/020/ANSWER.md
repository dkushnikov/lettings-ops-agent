# ANSWER — Case 020 — Case 020: Property inspection

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** inspection_booking · **Playbook:** access-scheduling

## Status

**Recap:** Inspection done 16/02/2024, no issues; landlord's reply raises an unapproved dog flap and a missing spare key after a lock change — referred to the property manager.
**Stage:** final_checks
**Last update:** 2024-02-18 22:20:32 UTC (event-020) · **Decided:** 2026-10-10 14:05 UTC
**Next step:** Property manager to decide with the landlord whether the dog flap stays or is reinstated and at whose cost; tenant to supply a spare front door key (asked today, ACT-1).

Definition of done (6/7 done):
- [x] job_known: Purpose and urgency of the visit confirmed — event-002/event-017: routine property inspection with photos for the landlord
- [x] windows_offered: Two contractor-confirmed windows offered to the tenant with the required notice — event-002 (13/02 AM window) and event-009 (15/02 PM window) offered to the tenant with more than 24 hours' notice
- [x] tenant_agreed: Tenant agreed a window, or consented to entry with the management key — event-006 tenant requested 15/02; event-007 agency spoke to tenant who confirmed the date, dog and occupant at home
- [x] booked: Visit booked and confirmed to both the tenant and the contractor (slot, access arrangement, pets noted) — event-012 rescheduled visit time 2024-02-15 14:00; confirmed to tenant by SMS and email (event-009, event-010)
- [x] reminders: Reminder sent on the day; any reschedule confirmed to both sides — event-013/event-014 reminder on the day; reschedule confirmed to the tenant at event-009/event-010
- [ ] keys: Key handover recorded and key return confirmed after the visit, where a key was issued — event-020 landlord asks for a spare front door key after a lock change; tenant asked to confirm and supply one (ACT-1)
- [x] logged: Window, agreement and access arrangement logged — event-011/event-012 slot and arrangement logged; ACT-3 note records post-inspection follow-ups

## 1. Decision

Inspection is complete and reported; the open items are the landlord's post-inspection questions — an unapproved dog flap installation and recovery of a spare front door key after a lock change. Deciding whether the dog flap is removed/reinstated and who pays is a tenant-liability decision reserved to a human (PRO-TENANT-LIABILITY), and the lock change affects the agency's management key. In-authority steps done first: tenant written to for the spare key and the facts of the alteration (ACT-1), landlord answered with the report findings and asked to confirm consent (ACT-2), case noted (ACT-3). Handing to the property manager to settle the alteration/liability question with the landlord.

Safety actions taken first:
- Safety pass: report checklist confirms smoke/heat and carbon monoxide detectors tested and working on 16/02/2024; no damp or condensation recorded (attachment-01). No hazard reported or observed.
- Security point noted: if the front door lock has been changed, the agency may no longer hold a working management key - tenant asked to supply a spare (ACT-1).

Actions deliberately withheld:
- Did not decide or state that the dog flap, its removal or any making-good is tenant-payable (PRO-TENANT-LIABILITY).
- Did not mention deposit deductions or any tenancy consequence to the tenant (PRO-LEGAL).
- Did not instruct any contractor for reinstatement: no landlord approval and no spend cap on file (APR-SPEND-OVER-CAP).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, PRO-TENANT-LIABILITY, PRO-LEGAL, RTE-LANDLORD, RTE-STAFF, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Inspection at Flat 12, 162 Beacon Close was first booked for 13/02/2024 08:00-12:00 (visit time approved 2024-02-13 11:00). [event-002, event-004; high]
- F2: Tenant asked to move the visit to Friday 15 February because of their dog; the agency spoke to the tenant and rescheduled to 15/02/2024 12:00-17:00 (visit time 2024-02-15 14:00) and confirmed by SMS and email. [event-006, event-007, event-009, event-010, event-012; high]
- F3: A same-day reminder was sent to the tenant on 15/02/2024. [event-013, event-014; high]
- F4: The inspection report is dated 16 February 2024 (assessor signature 16/02/2024 16:32:45) and the document was uploaded with 'Inspection issues: NO', issue date 2024-02-16, expiring 2024-08-14. [attachment-01-property-inspection-report, event-018; high]
- F5: Report checklist records carbon monoxide detectors and smoke/heat detectors tested and working, and no evidence of damp, condensation, smoking or non-tenants; evidence of pets Yes. [attachment-01-property-inspection-report; high]
- F6: The report records a dog flap installed by the tenants in the back door, noted in the utility-room overview, and one defect: sticker-type marks on the Bedroom 1 wall beside the window for the tenant to remove and make good. [attachment-01-property-inspection-report; high]
- F7: The results summary was emailed to the landlord on 17/02/2024 with the report attached, stating no issues were identified. [event-017; high]
- F8: The landlord's reply of 18/02/2024 raises a dog flap installation that was not approved and asks about retrieval of a spare front door key following a lock change. [event-020; medium]
- F9: No lock change is recorded in the inspection report or anywhere else in the visible history; the only key arrangement mentioned is the agency's management key for access in the tenant's absence. [attachment-01-property-inspection-report, event-002; medium]
- F10: No landlord spend cap or standing authority is on file in the case record, so any priced work would need landlord approval. [get_case_details; medium]

Conflicts between sources:
- Landlord summary email says no issues identified; the report records a dog flap and a Bedroom 1 defect. → Specific report lines beat the general 'no issues' statement; findings restated to the landlord (ACT-2). (source_hierarchy)

Red flags:
- [data_quality] Landlord correspondence names are inconsistent: event-017 addresses 'Oliver Bennett', the landlord reply at event-020 names 'Felix Clarke'. Not copied into any outbound letter. → Recorded in the case note (ACT-3); parties addressed only by the case record's property/role.
- [data_quality] event-016 note has no text ('Text/transcription absent'), so the inspector's own comment on the visit is unavailable; findings taken from the report document instead. → Relied on attachment-01 and event-018 for the result.
- [other] The landlord summary email states 'No issues were identified during the inspection' while the report records a dog flap installation and a Bedroom 1 defect; the specific report lines prevail. → Correct findings restated to the landlord (ACT-2) and set out in the handover.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "020", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed | message=Hello, the inspection at Flat 12, 162 Beacon Close, Cedarfo… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed | message=Thank you for your reply about the inspection at Flat 12, 1… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | add_note | completed | note=Inspection completed 16/02/2024 (attachment-01; event-018 d… | {"id": "ACT-3"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** The landlord says a dog flap was installed without approval and wants the spare front door key back after a lock change. Does the flap stay or is it reinstated, and at whose cost?
**Facts (≤5):**
- Inspection completed 16/02/2024; report records all 11 areas Good/Good, no damp, condensation, smoking or non-tenants; smoke/heat and CO detectors tested and working (attachment-01, event-018).
- Report notes a dog flap installed in the back door (utility-room overview) and evidence of pets - small dog and fish tank (attachment-01).
- Only defect: sticker-type marks on Bedroom 1 wall beside the window, tenant to remove and make good (attachment-01).
- Landlord free-text reply (event-020, untrusted) raises the unapproved dog flap and asks about retrieval of a spare front door key after a lock change; no lock change is recorded in the inspection report.
- Tenant asked today to confirm the lock change, supply a spare key to the office, and confirm whether consent was given for the flap (ACT-1); landlord answered with the findings and asked to confirm consent (ACT-2).
**Gap:** Whether the landlord ever consented to the flap, whether a lock change actually occurred and when, and whether the agency's management key still works.
**Options:**
- Landlord consents to the dog flap remaining; log consent and close once the spare key is received.
- Require reinstatement of the back door at end of tenancy; property manager to set terms with landlord and tenant.
- Instruct a contractor to quote for reinstatement now - needs landlord approval (no spend cap on file).
- If the tenant will not provide a key for the changed lock, property manager to handle the access/tenancy point.
**Recommended:** Obtain the landlord's position on the flap (consent or reinstatement at end of tenancy) and secure the spare key from the tenant before closing; no contractor instruction without a priced quote approved by the landlord (RTE-LANDLORD).
**Default if no answer:** No action; case stays open at final_checks awaiting the landlord's position and the tenant's spare key.
**Undo:** Outbound messages ACT-1/ACT-2 can be followed up with a correction; no booking or spend has been made.
**Context:** event-012, event-017, event-018, event-020, attachment-01-property-inspection-report

Promises made or recorded:
- agency → tenant: Inspection visit on 15/02/2024 between 12:00 and 17:00 (rescheduled from 13/02) by 2024-02-15 [kept]
- agency → landlord: Come back on the dog flap and spare key once the tenant replies and the property manager has the landlord's position [open]
- tenant → agency: Remove the Bedroom 1 sticker marks and make good; confirm lock change and provide a spare front door key [open]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge party correspondence within one working day
