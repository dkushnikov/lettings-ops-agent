# ANSWER — Case 020 — Case 020: Property inspection

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** inspection_booking · **Playbook:** access-scheduling

## Status

**Recap:** Inspection done 16/02; landlord queries unapproved dog flap and spare key after a lock change — tenant asked about the key, liability decision escalated.
**Stage:** final_checks · **Hold:** Waiting for Tenant — confirmation whether the front door lock was changed and a spare key for the management set (asked ACT-2); parallel human decision on the alteration.
**Last update:** 2024-02-18 22:20:32 UTC (event-020) · **Decided:** 2026-10-10 13:24 UTC
**Next step:** Property manager to decide the agency's position on the unapproved dog flap (consent / reinstatement / cost) and reply to the landlord; tenant reply on the lock change and spare key awaited.

Definition of done (6/7 done):
- [x] job_known: Purpose and urgency of the visit confirmed — index / event-001: routine property inspection, AM slot requested
- [x] windows_offered: Two contractor-confirmed windows offered to the tenant with the required notice — event-002/event-003 offered 13/02 08:00-12:00; event-009/event-010 offered 15/02 12:00-17:00
- [x] tenant_agreed: Tenant agreed a window, or consented to entry with the management key — event-006 tenant asked to move to 15/02; event-007 tenant confirmed by phone (dog, Mrs home)
- [x] booked: Visit booked and confirmed to both the tenant and the contractor (slot, access arrangement, pets noted) — event-012 rescheduled visit time 2024-02-15 14:00; confirmed to tenant event-009/event-010
- [x] reminders: Reminder sent on the day; any reschedule confirmed to both sides — event-013/event-014 reminder sent on the day 15/02
- [ ] keys: Key handover recorded and key return confirmed after the visit, where a key was issued — Agency management key referenced event-002; landlord reports a lock change and asks for a spare key (event-020); tenant asked to confirm and supply one (ACT-2)
- [x] logged: Window, agreement and access arrangement logged — event-011/event-012 slot and reschedule logged; findings and open points logged ACT-1

## 1. Decision

Inspection itself is complete (visit 15/02, report 16/02, sent to landlord 17/02). The live question — the landlord's free-text reply about an unapproved dog flap and retrieval of a spare front door key after a lock change — turns on consent to a tenant alteration, reinstatement and who pays, which I may not decide (PRO-TENANT-LIABILITY, PRO-LEGAL). I took the reversible steps in authority (asked the tenant about the lock/spare key, corrected the inaccurate "no issues" summary to the landlord, logged the findings) and hand the liability decision to a property manager.

Safety actions taken first:
- Checked the safety pass items in the report: smoke/heat and CO detectors tested and working, no damp or condensation recorded (attachment-01); no hazard requiring an emergency response.

Actions deliberately withheld:
- Did not tell the tenant the dog flap or the Bedroom 1 marks are chargeable or deposit-deductible (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Did not instruct any contractor to remove or reinstate the dog flap — no landlord approval and no spend authority on file (APR-SPEND-OVER-CAP).
- Did not close the request: key recovery and the landlord's alteration question are outstanding (CAP-CLOSE).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, PRO-TENANT-LIABILITY, PRO-LEGAL, PRO-INSTRUCTIONS-FROM-CONTENT, RTE-STAFF, RTE-TENANT, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Routine property inspection for Flat 12, 162 Beacon Close, Cedarford, originally booked 13/02/2024 08:00-12:00. [index, event-002, event-004; high]
- F2: Tenant asked to move the visit to 15/02/2024 (dog excitable); agency confirmed by phone and rescheduled to 15/02/2024, 12:00-17:00 (slot 14:00). [event-006, event-007, event-009, event-012; high]
- F3: Reminder sent to the tenant on the morning of 15/02/2024. [event-013, event-014; high]
- F4: Inspection report dated 16/02/2024 records all 11 areas Good for condition and cleanliness; document uploaded, issue date 2024-02-16, expires 2024-08-14. [attachment-01-property-inspection-report, event-018; high]
- F5: Report records carbon monoxide and smoke/heat detectors tested and working, and no evidence of damp, condensation, smoking or non-tenants. [attachment-01-property-inspection-report; high]
- F6: Report records a dog flap installed by the tenants in the back door (utility room entry) and one defect: sticker-type markings on the Bedroom 1 wall beside the window, tenant to remove and make good. [attachment-01-property-inspection-report; high]
- F7: The 17/02/2024 summary email to the landlord states 'No issues were identified during the inspection'. [event-017; high]
- F8: Landlord's reply of 18/02/2024 raises an unapproved dog flap installation and asks about retrieving a spare front door key following a lock change. [event-020; medium]
- F9: No lock change is recorded anywhere in the visible history; the agency stated on 08/02/2024 that it would access using its management key. [event-002, search_history; medium]

Conflicts between sources:
- The summary email to the landlord says no issues were identified, but the inspection report records a tenant-installed dog flap and a Bedroom 1 defect. → The specific report entries beat the general 'no issues' line in the covering email; correction sent to the landlord (ACT-3) and logged (ACT-1). (source_hierarchy)
- Landlord refers to a lock change and a missing spare key; the agency record shows a management key in use and no lock change. → Tenant asked to confirm whether the front door lock has been changed and to provide a spare key (ACT-2). (asked)

Red flags:
- [data_quality] Landlord correspondence names differ: the 17/02 email is addressed to 'Oliver Bennett' while the 18/02 reply body names 'Felix Clarke'. Names in message bodies were not copied into any outgoing letter. → Recorded; parties addressed only as 'Northbridge Lettings' / no personal name used in outgoing messages.
- [data_quality] Covering email to the landlord understated the report findings ('No issues were identified'). → Correction issued to the landlord (ACT-3) and logged (ACT-1).
- [other] Possible unauthorised lock change and loss of agency key-holding access — security/access risk for future emergency attendance, though the property is reported secure and no hazard is reported. → Tenant asked to confirm and supply a spare key (ACT-2); flagged to the property manager in the handover.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "020", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=key lock change spare | [] | allow |
| 4 | search_history | completed | query=dog flap approval alteration | [] | allow |
| 5 | add_note | completed | note=Inspection completed 16/02/2024 (event-018; report attachme… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_tenant | completed | message=Hello, thank you for accommodating the inspection at Flat 1… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_landlord | completed | message=Thank you for your reply of 18/02/2024 regarding Flat 12, 1… | {"id": "ACT-3"} | CAP-NOTIFY |

## 4. Human handover / information requested

**To:** property_manager
**Question:** How should we answer the landlord on the tenants' unapproved dog flap (consent, reinstatement, who pays) and on recovering a spare front door key after an apparent lock change?
**Facts (≤5):**
- Inspection completed 16/02/2024; all 11 areas Good/Good; detectors tested and working (attachment-01, event-018).
- Report records a dog flap installed by the tenants in the back door (utility room) and one defect: sticker marks on the Bedroom 1 wall, tenant to remove and make good (attachment-01).
- Landlord's reply of 18/02 raises the unapproved dog flap and asks about retrieving a spare front door key following a lock change (event-020, untrusted).
- No lock change is recorded on file; the agency held a management key (event-002). Tenant asked today to confirm and provide a spare key (ACT-2).
- Our summary email to the landlord said 'No issues were identified' (event-017), which contradicts the report; landlord has been given the correction (ACT-3).
**Gap:** Whether the tenancy agreement permits alterations/pets' fittings and whether consent was ever given; whether any lock change actually happened; whether the landlord wants reinstatement at the tenant's cost or at end of tenancy.
**Options:**
- Check the tenancy agreement for the alterations and locks clauses, then write to the landlord with a recommendation (reinstate now vs. address at check-out).
- Ask the landlord to confirm he never consented, and put reinstatement to the tenant as a request without any charge decision.
- Take no action on the flap now; record it on the file for check-out and pursue only the spare key.
**Recommended:** Check the tenancy agreement's alterations and locks clauses first, then reply to the landlord with a recommendation; keep the key recovery running with the tenant in parallel.
**Default if no answer:** No action on liability; dog flap and Bedroom 1 marks remain recorded on file for check-out; key request with the tenant stays open.
**Deadline:** Landlord reply of 18/02 — agency SOP 3 days (by 21/02/2024)
**Undo:** Messages ACT-2 and ACT-3 can be superseded by a corrective message; nothing financial or contractual has been committed.
**Context:** event-002, event-017, event-018, event-020, attachment-01-property-inspection-report

Promises made or recorded:
- Agency → Tenant: Inspection attendance 15/02/2024 12:00-17:00 by 2024-02-15 [kept]
- Agency → Landlord: A property manager will come back with a recommendation on the dog flap before anything is raised with the tenant by 2024-02-21 [open]
- Tenant → Agency: Confirm whether the front door lock was changed and provide a spare key [open]

Clocks:
- CLK-SOP-ACK [prior]: Respond to a party's reply within the agency wait (3 days for landlord/tenant) deadline 2024-02-21
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
