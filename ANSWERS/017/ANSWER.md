# ANSWER — Case 017 — Flat entrance door maintenance request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Fire-resisting entrance door catches at top and latches only on a firm pull; decorating quote £186 sent to landlord for approval, fire-door inspection escalated to the property manager.
**Stage:** quote_approval · **Hold:** Waiting for Landlord — £186.00 quote approval requested (ACT-3); also awaiting Brindlewick Court building management reply to the 12 Feb scope query (event-018).
**Last update:** 2025-02-12 16:10:00 UTC (event-019) · **Decided:** 2026-10-10 15:41 UTC
**Next step:** Property manager to decide on commissioning a competent fire-door inspection and chase Brindlewick Court building management (query of 12 Feb, event-018, unanswered); landlord separately to approve or decline the £186.00 decorating quote (ACT-3; quote lapses 28 February).

Definition of done (2/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 acknowledgement and triage questions; event-010 contractor's visual assessment; urgency set routine; damage-limiting advice to tenant at ACT-1
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 authorised inspection only; event-017 is a question about the quote, no cap on file; priced approval request sent at ACT-3
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Pale Finch Decorating attended for inspection only (event-010); no provider instructed for the repair (get_action_ledger)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Inspection visit confirmed and attended 7 Feb 10:30-12:00 (event-008, event-009, event-010); no further visit due until work is approved
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — £186.00 quote with the landlord; approval requested at ACT-3, quotation valid to 28 Feb (event-016)
- [ ] work_result: Work result recorded from the provider — No repair work carried out
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Quotation on file (fire-door-quotation.pdf); no invoice or completion photos as no work has been done
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice exists
- [ ] landlord_confirmation: Landlord confirmed completion — No completion to confirm
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provided access in person (event-009)
- [ ] closed: Request closed with a resolution that names who paid — Open: quote with landlord, fire-door inspection decision with the property manager

## 1. Decision

Reversible steps taken within mandate (tenant updated with damage-limiting advice, landlord sent the confirmed scope, priced approval request for £186.00 recorded, case note logged). No contractor instructed: no standing spend cap is on file and the landlord's 11 February email is a question, not an approval (APR-SPEND-OVER-CAP, event-017). Escalating the fire-safety strand to the property manager: the door is a fire-resisting flat entrance door that latches only on a firm pull, was recorded as closing slowly, has no inspection or certification record, and the quoted work is decorative only — commissioning a competent fire-door inspection and dealing with building management's consultation requirement sit with a person (ESC-SAFETY, RTE-STAFF).

Safety actions taken first:
- Told the tenant to close the door firmly on each use so it latches fully, not to wedge or prop it open, and to report immediately if it stops latching or if damage appears to the edge, frame or seals (ACT-1).
- Told the landlord that the quoted painting does not address the catching/slow closing of a fire-resisting door (ACT-2).
- Referred the fire-door inspection and building-management consultation to the property manager rather than booking decorative work over an unresolved fire-door defect.

Actions deliberately withheld:
- Did not instruct Pale Finch Decorating: no standing spend cap on file and event-017 is a question, not an approval naming the amount (APR-SPEND-OVER-CAP, CAP-DISPATCH-APPROVED not satisfied).
- Did not book an access window: no work is approved and the tenant asked for advance notice (CAP-SCHEDULE-ACCESS).
- Did not state who pays for any fire-door inspection or remedial work (PRO-TENANT-LIABILITY).
- Did not give the contractor the occupant's home-care/health detail (PRO-PII).
- Did not state or imply that the door is or is not compliant as a fire door — no competent inspection exists.

## 2. Authority and evidence

Authority cited: APR-SPEND-OVER-CAP, CAP-REQUEST-APPROVAL, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, ESC-SAFETY, RTE-LANDLORD, RTE-STAFF, PRO-TENANT-LIABILITY, PRO-PII, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY, CAP-REQUEST-APPROVAL

Key facts (source ids in brackets):
- F1: Property is 14 Lantern Mews, Brindlewick, ZZ1 1ZZ; reporter is the tenant Iona Vale. [index, get_case_details, event-001; high]
- F2: Reported fault: flaking paint on the flat-side face of the entrance door and the leaf catching near the top when closing; it latches after a firm pull. [event-001, event-003, event-010, event-015; high]
- F3: Building file lists the flat entrance doors as fire-resisting; no door-by-door inspection sheet or certification record is available in the building office. [event-005, event-013; high]
- F4: A common-area check about a month before the report recorded this flat entrance door as closing slowly, with no gap measurement or door-set inspection. [event-013; medium]
- F5: Building management asked to be consulted before any drilling, alteration or change to the door or its hardware; the agency's 12 February scope query is unanswered. [event-005, event-013, event-018, event-019; high]
- F6: Contractor attendance on 7 February was visual only: no hardware removal, no clearance measurement, no inspection of concealed construction, no fire-performance test. [event-010, event-011; high]
- F7: Quotation NBL-017-Q1 from Pale Finch Decorating, dated 7 February, valid to 28 February: £186.00 including materials and labour for surface preparation and repainting the flat-side face and visible top edge; VAT not stated separately. [fire-door-quotation, event-011, event-016; high]
- F8: The quotation expressly excludes adjustment of door, frame or hinges, hardware removal or replacement, alterations to seals or threshold, and any fire-door survey, test, certification or fire-safety opinion. [fire-door-quotation, event-016; high]
- F9: Landlord authorised an inspection on 4 February and asked for a price before any chargeable work; no spending limit and no authority for replacement was given. [event-007; high]
- F10: Landlord's 11 February email asks whether the quotation can be approved from the repair budget and asks for scope and any building response to be confirmed before work is booked; it is a question, not an approval of a named amount. [event-017; high]
- F11: No work has been booked and no contractor has been instructed for the repair. [event-019, get_action_ledger; high]
- F12: Tenant access constraints: visits after 10:00 because of a home-care visit for a family member; access confirmed after 10:30 on 7 February; tenant asked that personal items are not photographed and wants advance notice of further access. [event-003, event-009, event-015; high]

Conflicts between sources:
- The decorating quotation treats the job as surface work on an ordinary door, while the building record classes the door as fire-resisting and a prior check noted slow closing — the painting scope does not address the operational defect. → Strands separated: decorating quote to the landlord for a priced decision; fire-door performance referred to the property manager with building management consultation outstanding. (unresolved)

Red flags:
- [safety_hazard] A fire-resisting flat entrance door that contacts the frame at the top, was recorded as closing slowly, and latches only on a firm pull — a self-closing/latching fire door in a block that may not close and latch unaided. No inspection or certification record exists. → Tenant advised to close the door firmly each time so it latches fully and not to wedge or prop it open, and to report immediately if it stops latching (ACT-1); landlord informed (ACT-2); escalated to the property manager for a competent fire-door inspection decision and building-management consultation.
- [data_quality] Quotation total £186.00 gives no VAT breakdown; building office holds no door schedule, no gap measurement and no certification for this door. → Recorded in the case note (ACT-4) and flagged to the landlord rather than inventing a VAT figure.
- [vulnerability] Occupant household includes a family member receiving a scheduled home-care visit; access restricted to after 10:00. No loss of an essential service, so ESC-VULNERABLE is not triggered on its own. → Detail kept in the case record only; contractors will be given the access window and the no-photography request, not the health/family detail (PRO-PII).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "017", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed (ledger) | message=Hello Ms Vale — an update on your entrance door (reported 3… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed (ledger) | message=Mr Moss — 14 Lantern Mews, flat entrance door. Status after… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | request_landlord_approval | completed (ledger) | subject=Pale Finch Decorating quote NBL-017-Q1 — repaint flat-side…, amount_gbp=186.0, rationale=Your email of 11 February asked whether the quotation can b… | {"id": "ACT-3"} | CAP-REQUEST-APPROVAL |
| 6 | add_note | completed (ledger) | note=Fire-door issue separated from the decorating quote. Door i… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Do we commission a competent fire-door inspection at 14 Lantern Mews (and who is asked to pay), given the fire-resisting flat entrance door latches only on a firm pull and no inspection record exists?
**Facts (≤5):**
- Flat entrance doors at Brindlewick Court are listed as fire-resisting; building management holds no door-by-door inspection sheet or certification record and asks to be consulted before any change to the door or hardware (event-005, event-013).
- A common-area check last month noted this door closing slowly; no gap measurement or door-set inspection was done (event-013).
- Tenant reports the door catches at the top and latches only on a firm pull, consistently since the visit; no injury or access failure (event-003, event-015).
- Pale Finch Decorating attended 7 Feb visually only and quoted £186.00 (VAT not stated) for sanding and repainting the flat-side face and top edge, valid to 28 Feb; it excludes adjustment, hardware, seals, fire-door survey and certification (event-010, event-011, event-016, fire-door-quotation.pdf).
- Landlord authorised inspection and asked whether the quote can be approved from the repair budget, with scope and the building response confirmed first; no spend cap is on file and no job has been instructed (event-007, event-017, event-019).
**Gap:** Whether the top-edge contact and slow closing affect the door's fire performance cannot be established from any record: no door schedule, no certification, no measured clearances, and the only attendance was a decorator's visual look. Building management has not answered the 12 Feb scope query. VAT treatment of the £186.00 is not stated on the quotation.
**Options:**
- Instruct a competent fire-door inspector (FDIS or equivalent) to survey the door set and report, after obtaining a price and the landlord's approval, and consult Brindlewick Court first — resolves the fire-safety question but adds cost and delay.
- Ask Brindlewick Court building management to inspect or confirm responsibility for the fire door as part of the block's fire-door regime (Fire Safety (England) Regulations 2022 checks) before any landlord spend — may be the correct cost owner but depends on their response time.
- Approve the £186.00 decorating work alone once building management confirms no objection — the tenant's paint complaint is resolved but the catching/latching defect on a fire door is left unaddressed; not recommended as a standalone outcome.
**Recommended:** Chase Brindlewick Court for the block's fire-door inspection position (option 2) and in parallel obtain a price for an independent fire-door inspection for the landlord's decision (option 1); hold the decorating work until the door operation is settled, so any adjustment happens before repainting.
**Default if no answer:** If nothing is decided by 28 February the decorating quotation lapses and must be re-quoted; the fire-door defect remains open and the tenant continues to use a door that latches only on a firm pull.
**Deadline:** 2025-02-28 (quotation validity, event-016); fire-door strand should not wait on it — CLK-S11 reasonable-time clock runs from 3 February (event-001)
**Undo:** Nothing irreversible has been done: no contractor instructed, no visit booked, no money committed. The £186.00 approval request to the landlord (ACT-3) can be withdrawn by a follow-up email.
**Context:** event-003, event-005, event-010, event-011, event-013, event-015, event-016, event-017, event-018, event-019, fire-door-quotation, ACT-1, ACT-2, ACT-3, ACT-4

Promises made or recorded:
- agency → tenant: No visit arranged without agreeing a window in advance, after 10:00; the no-photography request will be passed to any attending contractor [open]
- agency → landlord: A separate approval request for the £186.00 quote, and referral of the fire-door inspection question [kept]
- contractor → agency: Quotation price held available through 28 February 2025 by 2025-02-28 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- CLK-AWAAB-PRS [proposed]: Awaab's Law timescales (private tenancies)
