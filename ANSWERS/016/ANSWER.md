# ANSWER — Case 016 — Smoke alarm maintenance request

**Disposition:** ESCALATED · **Urgency:** urgent · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Smoke alarm unmounted and untested since 7 Aug; landlord's own fitter left it incomplete — tenant advised, landlord chased for details or authority, escalated for fire-safety and welfare review.
**Stage:** on_hold · **Hold:** Waiting for Landlord — electrician's name and firm date, or authority for us to instruct (ACT-2, reply-by 3 working days); in parallel with the property-manager review.
**Last update:** 2025-09-22 08:48:00 UTC (event-017) · **Decided:** 2026-10-10 15:42 UTC
**Next step:** Landlord (Ronan Vale) to supply the electrician's details and a firm attendance date, or approve Northbridge Lettings instructing an electrician (ACT-2, 3-working-day clock); property manager to decide on the fire-safety override and welfare follow-up.

Definition of done (1/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-002 categorised and acknowledged same day; urgency set urgent and interim fire-safety advice given in ACT-1
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Landlord elected to use his own electrician (event-004) but it was left incomplete (event-010); approval or details re-requested in ACT-2, no reply yet
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider identity on file; landlord's fitter never named (event-007, event-010)
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No confirmed appointment; the 31/08 attendance was unconfirmed and incomplete (event-009, event-010)
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote exists; £120 in ACT-2 is my assumption, awaiting the landlord
- [ ] work_result: Work result recorded from the provider — Alarm still unmounted and untested (event-010, event-014)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos, no invoice, no alarm test record on file
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Landlord is arranging and paying his own contractor; no agency invoice exists unless the override in the handover is authorised
- [ ] landlord_confirmation: Landlord confirmed completion — Completion confirmation requested on 07/08 (event-005) and chased; never received
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; the tenant is in occupation and grants access
- [ ] closed: Request closed with a resolution that names who paid — Cannot close: alarm not mounted or tested (event-014); case on hold (ACT-4) and escalated

## 1. Decision

Escalate to the property manager for fire-safety and welfare review while the case sits on hold with the landlord. A smoke alarm has been out of service at an occupied property since 7 August 2025 (event-001), the landlord's own fitter left it unmounted on 31 August (event-010) and nothing on file shows it mounted or tested (event-014). The occupant was hospitalised and discharged in September and asked for contact to be reduced (event-011, event-012, event-013), and an unverified person attended the property on 20 September who was not sent by this agency (event-015, event-016). That combination — vulnerability plus a fire-safety device out of service, plus an unidentified caller — is ESC-VULNERABLE, ESC-SAFETY and ESC-FRAUD, which a person must decide, not me. Within my own authority I have: sent the tenant one consolidated message with interim fire-safety advice and caller-verification advice (ACT-1); asked the landlord, with a 3-working-day reply-by, either for his electrician's details and a firm date or for authority for us to instruct our own (ACT-2, APR-SPEND-OVER-CAP — no spend cap on file, so no standing authority); recorded the file note (ACT-3) and placed the case on hold (ACT-4). I did not instruct a contractor: there is no landlord approval in the visible history for an agency-instructed job and no standing cap, and the matter does not meet an emergency definition in the mandate.

Safety actions taken first:
- Told the tenant to treat the property as having no working smoke alarm on that storey, to keep internal doors closed at night and escape routes clear, and not to refit the mains alarm themselves (ACT-1).
- Told the tenant that no visit is booked by the agency and to admit no one without a name given in advance and photo ID (ACT-1).
- Recorded that the alarm must be mounted and tested, with the test result on file, before this request can be closed (ACT-3).

Actions deliberately withheld:
- Did not instruct a contractor: no landlord approval for an agency-instructed job in the visible history and no spend cap on file (APR-SPEND-OVER-CAP).
- Did not book an access window: no provider and no tenant-agreed slot (CAP-SCHEDULE-ACCESS requires tenant consent).
- Did not treat the case as an emergency dispatch: a detached smoke alarm is not in the mandate's emergency definitions, so the £250 make-safe ceiling was not used.
- Did not state or imply who pays for the fitter's abortive visit (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-REQUEST-APPROVAL, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, ESC-VULNERABLE, ESC-SAFETY, ESC-FRAUD, RTE-LANDLORD, RTE-STAFF, PRO-PII, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY, CAP-REQUEST-APPROVAL

Key facts (source ids in brackets):
- F1: Tenant Elise Rowan reported on 07/08/2025 that the smoke alarm at 26 Tallowmere Close had come away from the ceiling; no photos supplied. [index, event-001, get_case_details; high]
- F2: The agency acknowledged the report the same morning, 07/08/2025 (NBL-016). [event-002; high]
- F3: The landlord replied on 07/08/2025 that he would use his own electrician; no name, scope or date given. [event-004; high]
- F4: On 12/08/2025 the landlord said the electrician would contact the tenant and complete the work by the following weekend at the latest; no contractor details or appointment followed. [event-007; high]
- F5: On 02/09/2025 the tenant reported that a fitter had attended, removed the bracket and could not refit the alarm because the box contained no bracket; the alarm remained unmounted. [event-010; high]
- F6: There is no evidence on file that the alarm has been mounted or tested at any point since. [event-014, search_history; high]
- F7: The tenant was in hospital on 07/09/2025, was discharged on 11/09/2025, and asked the agency to reduce contact while recovering. [event-011, event-012, event-013; high]
- F8: An unannounced person attended the property on Saturday 20/09/2025 and was refused entry; identity, organisation and purpose were never verified, and no agency visit was booked. [event-015, event-016; high]
- F9: No landlord spend cap or standing instruction is recorded for this landlord, so the default standing authority is nil. [search_history, get_case_details; medium]
- F10: No quote, invoice or contractor identity for the alarm work exists anywhere in the case file. [search_history, get_action_ledger; high]

Conflicts between sources:
- The landlord's 12/08 promise that the work would be completed by the following weekend (event-007) conflicts with the tenant's accounts of 27/08, 02/09 and 11/09 that it was not done (event-009, event-010, event-013). → Tenant's first-hand, later accounts of the state of the alarm are preferred; treated as outstanding and chased with the landlord (ACT-2). (source_hierarchy)

Red flags:
- [safety_hazard] Smoke alarm detached and left unmounted and untested at an occupied property since 07/08/2025 - a fire-detection device out of service for over six weeks. → Interim fire-safety advice to the tenant (ACT-1); landlord pressed for a date or authority to instruct (ACT-2); escalated to the property manager.
- [vulnerability] Occupant hospitalised 07/09-11/09/2025 and asked for reduced contact while recovering; vulnerability combined with a fire-safety device out of service (ESC-VULNERABLE). → Contact limited to one consolidated message (ACT-1); health details withheld from any contractor brief (PRO-PII); welfare follow-up handed to the property manager.
- [fraud] Unidentified caller at the property on 20/09/2025 claiming to be there 'to check something'; not arranged by this agency and never verified. → Tenant told no visit was booked by us and to admit no one without a name given in advance and photo ID (ACT-1); referred to the property manager.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "016", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=spend cap approval standing instruction contractor | [] | allow |
| 4 | search_history | completed | query=smoke alarm tested mounted | [] | allow |
| 5 | notify_tenant | completed (ledger) | message=Dear Ms Rowan, about request NBL-016 (smoke alarm, 26 Tallo… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | request_landlord_approval | completed (ledger) | subject=NBL-016, 26 Tallowmere Close: smoke alarm still unmounted s…, amount_gbp=120, rationale=Reported 7 August (event-001). You said you would use your… | {"id": "ACT-2"} | CAP-REQUEST-APPROVAL |
| 7 | add_note | completed (ledger) | note=NBL-016 status review. Fault: smoke alarm detached from cei… | {"id": "ACT-3"} | CAP-LOG |
| 8 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — reply to ACT-2: electrician's name a…, until=3 working days from the approval request (reply-by stated t… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** A smoke alarm at 26 Tallowmere Close has been out of service for over six weeks and the landlord's own electrician has not completed it: do we override and instruct our own electrician now at the landlord's cost, and who takes the welfare and unidentified-caller follow-up?
**Facts (≤5):**
- Smoke alarm came away from the ceiling, reported by the tenant 07/08/2025 (event-001); no evidence on file that it has been mounted or tested since (event-014).
- Landlord said he would use his own electrician (event-004) and promised completion 'by the following weekend at the latest' on 12/08 (event-007) - not met.
- Tenant reported on 02/09 that a fitter removed the bracket and could not refit the alarm because the box contained no bracket; alarm left unmounted (event-010).
- Tenant was in hospital on 07/09, discharged 11/09, and asked us to stop repeated calls and emails while unwell (event-012, event-013).
- On 20/09 an unannounced caller attended and was refused entry; identity, organisation and authority never verified, and not arranged by this agency (event-015, event-016).
**Gap:** No landlord spend cap or standing instruction on file (search_history: no results), so there is no standing authority to spend. No electrician name, no quote and no confirmed appointment anywhere in the history. Whether the 20/09 caller was connected to the alarm work is unknown. Whether the alarm head is serviceable, and whether it is mains-wired or battery, has never been established.
**Options:**
- Wait the 3 working days for the landlord's reply to ACT-2, then act on his answer - keeps his chosen contractor and cost control, but the alarm stays out of service meanwhile.
- Override now: instruct a vetted electrician to fit the correct bracket and alarm head and test it, recharged to the landlord - fastest route to a working alarm, but the spend goes ahead without his approval and may be disputed.
- Treat it as a fire-safety emergency and dispatch today under the emergency make-safe ceiling - removes the risk immediately, but a detached smoke alarm is not in the mandate's emergency definitions.
**Recommended:** Option 2 if the landlord has not answered ACT-2 within the 3 working days; in either case book the visit with the tenant in advance with a named attendee, given the unverified caller.
**Default if no answer:** If the landlord does not reply by the 3-working-day reply-by, the case returns to this queue for a decision on instructing our own electrician; the alarm remains out of service until then.
**Deadline:** Landlord reply-by: 3 working days from ACT-2. CLK-S11 'reasonable time' running since 07/08/2025.
**Undo:** Nothing irreversible has been done: no contractor instructed, no access booked, no spend committed. ACT-2 can be withdrawn by a follow-up email to the landlord and the hold (ACT-4) lifted at any time.
**Context:** event-001, event-004, event-007, event-010, event-012, event-013, event-014, event-015, event-016, ACT-1, ACT-2, ACT-3, ACT-4

Promises made or recorded:
- agency → tenant: We will contact you to agree a time before anyone attends; nothing is booked yet. [open]
- agency → landlord: Any quote above the £120 assumed figure will be put to the landlord before work starts. [open]
- landlord → agency: Electrician to contact the tenant and complete the work by the following weekend at the latest (said 12/08/2025). by 2025-08-17 [broken]
- agency → tenant: Pause in proactive contact while the tenant recovered. [kept]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- APR-SPEND-OVER-CAP [sop]: Landlord reply-by on the approval request deadline 3 working days from ACT-2
