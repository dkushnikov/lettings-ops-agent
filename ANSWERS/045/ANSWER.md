# ANSWER — Case 045 — Case 045: Kitchen Window and Patio Door Window Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window job closed as landlord-completed was re-opened by his later query about a new appointment; landlord and tenant asked to confirm, address conflict sent to the office.
**Stage:** on_hold · **Hold:** Waiting for Landlord — Theo Palmer to confirm whether the window work is complete or a further contractor visit is outstanding, and which property his 4 April query (event-038) relates to; reply chased by 3 working days. Tenant asked in parallel whether a contractor attended.
**Last update:** 2025-04-04 12:05:07 UTC (event-038) · **Decided:** 2026-10-10 14:14 UTC
**Next step:** Landlord to confirm whether the window work is finished or a further visit is outstanding, and at which property (asked ACT-1; 3-working-day clock); office to settle the address conflict (ACT-3).

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged the report; event-009 categorised it as blown sealed units; urgency set routine in use_playbook; no damage-limiting steps apply to failed glazing (ACT-4).
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-011 — landlord elected to use and fund his own contractor; event-017 — landlord accepted the quote and instructed the contractor to proceed. No agency spend engaged.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-012 — landlord's surveyor (Lantern Surveying) contacted the agency and tenant details were passed with the tenant's authorisation; provider is the landlord's own.
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-031 records a visit date and event-032/event-034 suggest it happened, but event-038 asks whether a new appointment has been arranged — unresolved; landlord and tenant asked (ACT-1, ACT-2).
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-017 — landlord had the quote and instructed the contractor himself; amount and VAT never came to the agency as the landlord bears the cost.
- [ ] work_result: Work result recorded from the provider — No provider report on file; the only completion evidence is the landlord's 'all done' (event-034), contradicted by event-038.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice from the landlord's contractor; three tenant window photos referenced at event-007 are unavailable. Skip reason cannot yet be recorded while completion is in doubt.
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-036, event-037 — landlord's own contractor, paid directly by the landlord; request was marked completed without payment.
- [ ] landlord_confirmation: Landlord confirmed completion — event-034 confirmed completion but event-038 contradicts it; re-confirmation requested (ACT-1).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; access was arranged directly between the tenant and the landlord's contractor (event-012).
- [ ] closed: Request closed with a resolution that names who paid — Closure withheld — see withheld_actions; case placed on hold (ACT-5) pending the landlord's confirmation.

## 1. Decision

Did not close and did not instruct anyone. The landlord confirmed completion on 4 April (event-034) and the request was marked completed without payment (event-036, event-037), but 52 minutes later the landlord asked whether a new appointment date had been arranged with tenants (event-038) — so completion is no longer established and the playbook's final checks cannot be signed off. The work was carried out by the landlord's own contractor at his own cost (event-011, event-017), so no agency spend authority was engaged and no dispatch is mine to make. I asked the landlord to confirm whether the work is finished or a further visit is outstanding and which property event-038 refers to (ACT-1), asked the tenant whether a contractor has attended and whether anything remains outstanding (ACT-2), referred the seven conflicting addresses on this one job id to the office rather than picking a side in a message to a party (ACT-3, per ESC-CONFLICT routing to RTE-STAFF via a human task), recorded the chronology and the safety check (ACT-4) and placed the case on hold (ACT-5).

Safety actions taken first:
- Safety pass run against the artefacts: no gas, electrical, water, heating, security or vulnerability indicator present — fault is failed glazing only; result recorded in the case note (ACT-4).
- Withheld closure of a request whose completion is contradicted by the landlord's own later message, so any outstanding glazing defect stays on the agency's books.

Actions deliberately withheld:
- close_request — completion contradicted by event-038; playbook final checks (work result, documents, landlord confirmation) cannot be signed off.
- assign_contractor — the landlord is using and paying his own contractor (event-011, event-017); no agency spend authority and no need for a dispatch.
- schedule_access — no confirmed need for a visit, no property identified with confidence and no tenant consent yet (CAP-SCHEDULE-ACCESS).
- Asserting a corrected property address to the landlord, tenant or contractor — conflict referred to the office instead.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-TENANT, ESC-CONFLICT, CAP-CLOSE, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY, PRO-PII
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the kitchen window and patio door windows on 14 Jan 2025; property on the authoritative case record is Flat 26, 116 Copperfield Walk, Alderwick, ZZ7 8ZZ. [index, event-001, get_case_details; high]
- F2: Agency understood the fault as blown/failed sealed units; no further detail was given by the tenant. [event-009; medium]
- F3: Tenant confirmed the repair was not requested by the landlord. [event-006; medium]
- F4: Landlord instructed his own contractor and limited budget to replacing the windows only; the blown patio door glass was to be quoted 'for the future'. [event-011; medium]
- F5: Tenant gave verbal authorisation on 30 Jan for her contact details to be passed to the landlord's surveyor (Lantern Surveying). [event-012; medium]
- F6: Landlord confirmed on 15 Feb that he had a quote and asked the contractor to proceed; the agency committed no spend at any point and no landlord standing spend cap is on file. [event-017, event-018; medium]
- F7: Landlord confirmed completion on 4 Apr ('Good, all done!'); the agency marked the request completed without payment, noting 'LL completed by himself'. [event-034, event-036, event-037; medium]
- F8: At 12:05 on 4 Apr the landlord asked whether a new appointment date had been arranged with tenants, naming Flat 5, 25 Harbour View, Cedarford — contradicting the completion confirmation 57 minutes earlier. [event-038; high]
- F9: No hazard keyword from the safety pass appears in the artefacts: the fault is failed glazing, with no gas, electrical, water ingress, heating loss, security failure or occupant vulnerability reported. Check made and recorded; no safety red flag raised. [event-001, event-009, ACT-4; high]
- F10: Outgoing agency correspondence under job id NBL-045-9445 carries at least five different property addresses in headers and bodies. [event-003, event-011, event-020, event-023, event-032, event-038; high]

Conflicts between sources:
- Landlord states the work is complete (event-034) but then asks about arranging a new appointment with tenants (event-038). → Landlord asked to confirm status before the request is closed (ACT-1); case put back on hold (ACT-5). Closure withheld. (asked)
- The property on the authoritative case record (Flat 26, 116 Copperfield Walk, Alderwick) differs from the address printed on the agency's own job emails (Flat 12, 182 Meadow Row, Kingshaven) and from four further addresses quoted in message bodies. → Not decided by me; referred to the office as a human task (ACT-3) and the landlord asked which property his new-appointment query concerns (ACT-1). No address asserted to any party. (asked)
- Scope: the landlord's January instruction funds the windows only, with patio door glass deferred (event-011), while the tenant's report and the ticket title cover both. → Flagged for the office; patio door glass may remain outstanding even if the window replacement is complete. (unresolved)

Red flags:
- [data_quality] One job id (NBL-045-9445) carries seven different property addresses across agency emails and quoted correspondence; the authoritative record says Flat 26, 116 Copperfield Walk, Alderwick. Acting on any of them could send a contractor to the wrong occupied flat. → Referred to the office via human task (ACT-3); landlord asked to identify the property in his latest query (ACT-1); no address asserted to tenant or contractor.
- [data_quality] Quoted correspondence names inconsistent people for the same parties (contractor addressed as both 'Ruben Mercer' and 'Oakley'; landlord addressed as 'Theo' and 'Oakley'; a third-party 'Eliza Ingram' referring the survey), and a hold comment records a visit 'Tuesday 6th June' while the follow-up asks about a visit 'on Monday' in early April. → Names from message bodies not copied into any outgoing letter; parties addressed only by the case-record roles. Date discrepancy noted for the office.
- [other] Tenant contact details (email and mobile) were released to a third-party surveyor on 30 Jan. The file records the tenant's verbal authorisation, so the disclosure is covered, but the authorisation exists only as a staff note. → Recorded in the case note (ACT-4); no further personal data shared by me.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "045", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_landlord | completed | message=Job NBL-045-9445 — kitchen window and patio door glass, Fla… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_tenant | completed | message=Job NBL-045-9445 — kitchen window and patio door glass, Fla… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | create_human_task | completed | queue=property_manager, title=Case 045 NBL-045-9445: address conflict across agency recor…, summary=Conflict for the office to settle; no party has been told w… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 6 | add_note | completed | note=Case re-opened from "completed without payment" pending cla… | {"id": "ACT-4"} | CAP-LOG |
| 7 | put_on_hold | completed | reason=Waiting for Landlord — confirmation of whether the window w…, until=3 working days from 2025-04-04 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Is the kitchen window / patio door glass work at Flat 26, 116 Copperfield Walk, Alderwick finished, or is a further visit from your window contractor still outstanding? (blocking; Landlord said 'all done' (event-034) then asked about a new appointment (event-038); only the landlord can settle the status of his own contractor's work (RTE-LANDLORD).)
- Ask **landlord**: If a further appointment is outstanding, which property and which job does it relate to? Your message names Flat 5, 25 Harbour View, Cedarford, while this job's record is Flat 26, 116 Copperfield Walk, Alderwick. (blocking; Seven different addresses appear on this one job id; access must not be arranged at the wrong flat.)
- Ask **tenant**: Has a window contractor attended your flat and is the kitchen window and/or patio door glass now repaired? If not, has anyone given you a date for a further visit? (non-blocking; The tenant owns the facts about what has actually happened at the property and about any access window (RTE-TENANT).)

Promises made or recorded:
- agency → landlord: No access will be booked until the landlord confirms status and property; if no reply in 3 working days the request stays closed without payment and a fresh request is opened when the contractor makes contact. by 3 working days from 2025-04-04 [open]
- agency → tenant: Any further visit will be agreed with the tenant first, with at least 24 hours' notice. [open]
- agency → landlord: 'I'll keep this job open until its finished' — agency undertaking of 15 Feb; honoured by re-opening rather than closing on the contradicted completion. [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- RTE-LANDLORD [sop]: Landlord reply window deadline 3 working days from 2025-04-04
