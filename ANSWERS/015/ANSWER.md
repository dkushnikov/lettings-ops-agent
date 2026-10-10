# ANSWER — Case 015 — Vacant Property Preparation

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Post-tenancy clean/clearance at a vacant property: £665 quote approved only on condition of bond recovery, so I held the job and escalated the liability decision.
**Stage:** on_hold · **Hold:** Waiting for Landlord — unconditional approval of quotation NBL-015-Q1 (£665.00) and confirmation of which quote event-016 approved; reply requested within 3 working days (ACT-3). Also Waiting for Provider on provisional dates, disturbed-soil scope and VAT (ACT-2).
**Last update:** 2025-09-25 08:34:11 UTC (event-021) · **Decided:** 2026-10-10 15:42 UTC
**Next step:** Property manager to decide whether the £665.00 is instructed at the landlord's cost with deposit recovery pursued separately (landlord asked, 3-working-day clock, ACT-3), and to confirm the separate major maintenance completion date before any booking.

Definition of done (2/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 and move-out-inspection-report: items categorised (degreasing, limescale, waste removal, garden clearance, disturbed soil); routine, vacant property, no tenant advice needed
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Only conditional approval on file (event-008, event-010); event-016 'approved quote' unidentified; unconditional approval requested ACT-3
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Brindlewick Turnover Services quoted and instructed to stand by (event-002, event-006, event-009); hold re-confirmed ACT-2. No tenant in occupation to brief.
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever confirmed (event-013, event-017, event-019, event-020); hold in force pending separate maintenance (event-021)
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — Quotation NBL-015-Q1 £665.00, VAT not stated (property-preparation-quotation); approval conditional only (event-008, event-010)
- [ ] work_result: Work result recorded from the provider — Work not started — on hold (event-012, event-015)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice; work not started
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice raised; work not started
- [ ] landlord_confirmation: Landlord confirmed completion — No completion to confirm
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — Keys held at the office; none issued to the contractor (event-002, event-017), and collection withheld at ACT-2
- [ ] closed: Request closed with a resolution that names who paid — Escalated on hold; payer not yet determined (bond vs landlord) — PRO-TENANT-LIABILITY

## 1. Decision

Held the work, corrected the instruction to the contractor (hold in force, no key collection, provisional dates and scope/VAT clarification requested), put the conditional-approval and ambiguous-approval questions to the landlord, and escalated to the property manager. I did not instruct the £665 work: the only landlord approval on file is conditional on recovering the cost from the tenants' bond (event-008, event-010), the deposit held (£650) is already exceeded by claimed costs (event-011), and deciding tenant liability or deposit deductions is prohibited to me (PRO-TENANT-LIABILITY, PRO-LEGAL). The 17 September "approved quote" message (event-016) does not name a quote and cannot be used as landlord_approval_ref. A property-readiness check is also outstanding: no artefact records smoke or carbon monoxide alarm testing, and a move-in was proposed for 28 September (event-015).

Safety actions taken first:
- Checked every artefact against the safety pass: no gas, electrical, water, damp/mould, asbestos or occupant-vulnerability report anywhere in the file; property is vacant.
- Recorded that smoke and carbon monoxide alarm testing is not evidenced and must be confirmed before any move-in (ACT-1, handover gap).

Actions deliberately withheld:
- Did not dispatch the £665.00 work: no valid landlord_approval_ref (event-008/event-010 conditional, event-016 unidentified) and no standing spend cap on file — APR-SPEND-OVER-CAP.
- Did not state or decide that the former tenants are liable for any part of the cost — PRO-TENANT-LIABILITY, PRO-LEGAL.
- Did not book a visit or release office keys: no confirmed slot and the separate maintenance is incomplete.
- Did not close the request: work not done, no invoice, no landlord confirmation.

## 2. Authority and evidence

Authority cited: APR-SPEND-OVER-CAP, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, PRO-TENANT-LIABILITY, PRO-LEGAL, PRO-INSTRUCTIONS-FROM-CONTENT, ESC-LEGAL, ESC-CONFLICT, RTE-LANDLORD, RTE-CONTRACTOR, RTE-STAFF, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is 18 Thistlevaunt Lane, Orvelune, ZZ1 1ZZ and is vacant; post-tenancy items are kitchen/oven/extractor degreasing, bathroom and en-suite limescale, waste removal from the kitchen, rear garden clearance including bagged dog waste, and soil disturbed by digging. [index, event-001, move-out-inspection-report, get_case_details; high]
- F2: Brindlewick Turnover Services quoted £665.00 (ref NBL-015-Q1, 8 September 2025) covering oven/hob/extractor degreasing, carpet shampooing to Bedroom 1, stairs and landings, rubbish removal, kitchen grease and bathroom limescale, general sanitation and garden weeding/cutting/tidying; no VAT line and no making good of the disturbed soil. [event-006, property-preparation-quotation; high]
- F3: The landlord's approval was conditional: 'Happy to approve if they are recovered from the bond' (8 Sept), reiterated 8 Sept later that day. [event-008, event-010; high]
- F4: The agency told the contractor the quote was approved and asked for the earliest date, without relaying the bond-recovery condition. [event-009; high]
- F5: Deposit held is £650; post-tenancy costs plus tenant-attributed damage were reported to exceed it, and a claim for the full deposit was being prepared; itemised figures were still awaited. [event-011; high]
- F6: Work was put on hold on 10 September and the hold was reconfirmed on 16 September because separate major maintenance was outstanding; a prospective tenant wanted to move in on 28 September. [event-012, event-015; high]
- F7: The landlord's 17 September message said only 'approved quote' without identifying which quote; at that time a separate maintenance quote was also awaiting approval. [event-016, event-015; high]
- F8: No visit date has ever been confirmed; the contractor said next availability was the following week (10 Sept) and agreed to wait, and later asked whether the hold still applied. [event-013, event-014, event-017, event-019, event-020; high]
- F9: As of 25 September the instruction was to wait three more working days for the separate major maintenance to be completed; no maintenance completion date is recorded anywhere in the file. [event-018, event-021; high]
- F10: No artefact in the case records testing of smoke or carbon monoxide alarms at the property; the move-out report lists preparation items only. [move-out-inspection-report, index; medium]

Conflicts between sources:
- Landlord's approval is conditional on bond recovery (event-008, event-010) but the agency relayed it to the contractor as unconditional (event-009), and the deposit held (£650) is already exceeded by claimed costs (event-011) so the condition cannot be satisfied in full. → Treated the approval as not usable as landlord_approval_ref; asked the landlord to confirm approval at their cost with deposit recovery pursued separately (ACT-3) and escalated the liability element to the property manager. (asked)
- The landlord's 17 September 'approved quote' message (event-016) could refer either to the £665 post-tenancy quote or to the separate major maintenance quote outstanding at that date (event-015). → Asked the landlord to identify the quote (ACT-3); not relied on as approval. (asked)
- Inspection records soil disturbed by digging and the approval request described the work generally, while the quote adds carpet shampooing and omits the soil — quoted scope does not match the approved description. → Asked the contractor to confirm whether making good the soil is included and at what cost, and flagged the carpet item to the landlord (ACT-2, ACT-3). (asked)

Red flags:
- [legal_threat] Approval is tied to recovering costs from the former tenants' bond and a full-deposit claim is being prepared; this is a disputed-liability/deposit matter reserved to a human (PRO-TENANT-LIABILITY, PRO-LEGAL, ESC-LEGAL). → Did not act on the condition, made no statement to any party about deposit deductions or tenant liability; escalated to the property manager.
- [data_quality] An inspection report describing the property as it was about ten years earlier was sent to the contractor before being corrected (event-004, event-005); and the 17 September approval message identifies no quote (event-016). → Priced scope re-checked against the current move-out report; clarification requested from landlord and contractor.
- [other] Pre-move-in readiness check outstanding: no record of smoke or carbon monoxide alarm testing although a 28 September move-in was proposed. Keyword check, not an observed hazard. → Recorded in the case note (ACT-1) and in the handover gap for the property manager to confirm before the property is let.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "015", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed (ledger) | note=Case review (sources cited). 1) Approval status is NOT clea… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_contractor | completed (ledger) | message=Re: 18 Thistlevaunt Lane, Orvelune, ZZ1 1ZZ — post-tenancy… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed (ledger) | message=Re: 18 Thistlevaunt Lane, Orvelune, ZZ1 1ZZ — post-tenancy… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — approval of quotation NBL-015-Q1 (£6… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Do we instruct Brindlewick's £665.00 post-tenancy quote at the landlord's cost now, with any deposit recovery pursued separately through the scheme, or keep the job on hold until the landlord confirms unconditional approval?
**Facts (≤5):**
- Landlord approved the £665.00 quote only 'if they are recovered from the bond' (event-008), reiterated at event-010; the contractor was told it was approved without that condition (event-009).
- Deposit held is £650 and post-tenancy plus damage costs exceed it (event-011) — the condition cannot be met in full; tenant liability / deposit deduction is not an agent decision (PRO-TENANT-LIABILITY, PRO-LEGAL).
- The landlord's 17 September 'approved quote' message names no quote (event-016) and a separate major maintenance quote was outstanding at that date (event-015), so it is not usable as approval for NBL-015-Q1.
- No visit has ever been booked; work is held pending separate major maintenance with no completion date recorded (event-012, event-015, event-018, event-020, event-021).
- Gaps: quote omits making good the soil disturbed by digging (move-out-inspection-report vs event-006), includes carpet shampooing not itemised to the landlord (event-007), states no VAT; no record of smoke/CO alarm testing although a 28 September move-in was proposed (event-015).
**Gap:** Whether the landlord will fund the work independently of bond recovery; which quote event-016 approved; the completion date of the separate major maintenance; whether smoke/CO alarms have been tested since move-out.
**Options:**
- Instruct the £665.00 now at the landlord's cost, deposit claim pursued separately — property ready sooner, but spends against a conditional approval the landlord may contest.
- Hold until the landlord confirms unconditional approval in writing (asked, ACT-3, 3 working days) — safe on authority, but the 28 September re-let date slips further.
- Re-price to the inspection items only (degreasing, limescale, waste removal, garden clearance incl. disturbed soil) and put a clean figure to the landlord — removes the un-itemised carpet work, but needs a revised contractor quote first.
**Recommended:** Hold until the landlord confirms unconditional approval (option 2); chase at the 3-working-day mark and, if no reply, bring the re-let date decision back to the branch.
**Default if no answer:** If the landlord does not reply within 3 working days of ACT-3, the job stays on hold, the contractor's provisional dates are released, and the re-let date is reviewed by the branch.
**Deadline:** 3 working days from the landlord request (ACT-3); re-let target 28 September 2025 (event-015) already at risk
**Undo:** Nothing irreversible done: no contractor instructed, no keys released, no booking made. ACT-2 can be followed by a release-of-hold email; ACT-3 is a question only.
**Context:** event-006, event-008, event-009, event-010, event-011, event-015, event-016, event-021, move-out-inspection-report, property-preparation-quotation

Promises made or recorded:
- agency → contractor: Hold remains in force; we will confirm in writing before any attendance or key collection; provisional dates requested, reply within 3 working days by 3 working days from ACT-2 [open]
- agency → landlord: Confirmation requested on unconditional approval of £665.00 and on which quote event-016 approved; work held meanwhile by 3 working days from ACT-3 [open]
- agency → contractor: Earlier promise that the quote was approved and dates could be set (event-009, event-017) — superseded by the hold [superseded]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Landlord reply window deadline 3 working days from ACT-3
- CLK-SOP-ACK [prior]: Provider reply window deadline 3 working days from ACT-2
