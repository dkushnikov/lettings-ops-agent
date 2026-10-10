# ANSWER — Case 004 — Front entrance lock report

**Disposition:** NEEDS_INFO · **Urgency:** urgent · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Front-door lock outstanding since 27 Aug; landlord's own contractor has not confirmed completion, so chased contractor, tenant and landlord and held the ticket.
**Stage:** on_hold · **Hold:** Waiting for Landlord — decision whether Dorian Wren completes on a stated date or we may instruct our locksmith (3-day email window); also Waiting for Provider (Wren's firm date) and Waiting for Tenant (confirmation the door still locks).
**Last update:** 2025-09-16 08:33:00 UTC (event-023) · **Decided:** 2026-10-10 15:36 UTC
**Next step:** Landlord (Tomas Elde) to reply within 3 days confirming a date for his contractor or authorising Northbridge Lettings to instruct its own locksmith (quote to follow for approval).

Definition of done (3/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Urgency set to urgent (use_playbook); fault categorised at intake and acknowledged event-002; tenant given the insecure-door escalation instruction in ACT-1
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Landlord approved repair in principle (event-006) and then elected to use his own contractor (event-011, event-016) — the job sits on the landlord's own contractor, no agency spend committed
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's contractor Dorian Wren assigned by the landlord (event-016); agency provider stood down (event-017); tenant told who is coming (event-013, ACT-1)
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No confirmed date or window from Dorian Wren (event-018, event-019, event-023); chased in ACT-2
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No priced quote exists — the landlord's own contractor is carrying out the work; if the landlord switches to our locksmith a quote will go to him (ACT-3)
- [ ] work_result: Work result recorded from the provider — Contractor left to obtain a lock and did not return with a date (event-020); no result recorded (event-023)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice; work not completed
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice; landlord's own contractor would bill him directly
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord asked to confirm the route and completion (ACT-3); no reply yet
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provides access in person (event-013)
- [ ] closed: Request closed with a resolution that names who paid — Repair unresolved and reportedly worse (event-020); ticket on hold (ACT-6)

## 1. Decision

Kept the landlord's own contractor in place (his instruction of 1–2 Sept overrides the earlier general approval), made no dispatch and committed no spend (no standing cap on file). Chased Dorian Wren for a firm date with a reply-by, put the contractor-choice decision to the landlord with a 3-day reply window, asked the tenant to confirm the door still locks with an emergency route if it does not, passed the three unowned side issues (blind, door glazing, over-hot water) to the office, and placed the ticket on hold.

Safety actions taken first:
- Told the tenant that if the front door cannot be locked or the property left secure she must contact us immediately and we will treat it as an emergency and arrange a same-day locksmith make-safe (ACT-1)
- Asked the contractor to confirm whether the door is currently secure (ACT-2)
- Flagged the security dimension and the s.11 clock to the landlord (ACT-3)
- Referred the over-hot water scald check to the office queue and advised the tenant to avoid full-temperature hot water meanwhile (ACT-4, ACT-1)

Actions deliberately withheld:
- Did not instruct Peregrine Keyworks or any locksmith: the landlord's later instruction bars another contractor and no standing spend cap is on file (event-011, event-016; APR-SPEND-OVER-CAP).
- Did not book an access window: no contractor date exists to book against, and I will not promise a date no booking backs (CAP-NOTIFY).
- Did not express any view on who pays for the worsened lock or the earlier wasted visit (PRO-TENANT-LIABILITY).
- Did not close the request: work result, documents, invoice and landlord confirmation all pending.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-REQUEST-APPROVAL, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY, CAP-DISPATCH-EMERGENCY
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 27 Aug 2025 that the front-door lock is loose and intermittent, the door sometimes catches, a newly cut spare key does not work, but the door could then be locked by hand. [index, event-001; high]
- F2: Agency acknowledged the report to the tenant on 27 Aug 2025 and asked the landlord for approval the same day. [event-002, event-003; high]
- F3: Agency note of 1 Sept records the landlord's approval to proceed with lock repair or replacement, and his agreement that the tenant may do skirting-board paint touch-ups at her own expense. [event-006, event-005; high]
- F4: On 1 Sept the landlord emailed instructing the agency not to instruct another contractor and to wait for his own contractor; on 2 Sept he named Dorian Wren, said Wren was away until 9 Sept and asked the agency to liaise with him directly. [event-011, event-016; high]
- F5: Agency's selected locksmith Peregrine Keyworks was stood down on 2 Sept; no agency-provider visit was ever confirmed. [event-012, event-017; high]
- F6: Tenant offered access windows 4 Sept 11:00-13:00, 8 Sept 10:00-12:00, 9 Sept 10:00-12:00 and on 2 Sept said she was flexible on those days. [event-009, event-013; high]
- F7: On 9 Sept the tenant reported Dorian Wren attended, initially disputed the fault, then said a new lock was needed, left to obtain one and said he would return the following week without a date; she said the lock is now worse than before. [event-020; medium]
- F8: On 16 Sept the tenant said the contractor was meant to come that day after 10:00 with no narrower time; no attendance, repair or replacement is confirmed in the record. [event-023, event-022; high]
- F9: No standing spend cap or preferred-contractor mandate for this landlord appears in the authoritative case record; the only authority in the history is the landlord's own messages. [get_case_details, event-006, event-011; medium]
- F10: On 9 Sept the tenant raised three further matters with no recorded owner or status: a broken bedroom blind, glazing in a door, and hot water she says is too hot. [event-021; high]

Conflicts between sources:
- Landlord stated on 1 Sept that the front-door work 'should already have been done'; no completion record exists and the tenant reports the fault is worse. → Case record shows no work order completed and no attendance confirmation (event-018, event-019); the landlord's belief is treated as mistaken and the position restated to him factually in ACT-3. (tool_check)
- Landlord's 1 Sept general approval to proceed (event-006) versus his later instruction not to instruct another contractor and to wait for his own (event-011, event-016). → Both are landlord instructions; the later one governs. No agency dispatch made; the choice has been put back to the landlord with a 3-day window (ACT-3). (source_hierarchy)

Red flags:
- [safety_hazard] Front-door lock reported as worse after a partial contractor visit, on a repair that affects security of the property; tenant has not confirmed the door still locks. → Asked the tenant directly whether the door can still be locked and secured, with instruction to contact us immediately if not, in which case a same-day locksmith make-safe would be arranged under CAP-DISPATCH-EMERGENCY (up to £250) and the landlord told immediately (ACT-1). Landlord told the security point (ACT-3).
- [other] Tenant-reported hot water 'too hot' — scald-risk check with no recorded owner. → Passed to the office queue to log and check the outlet temperature/thermostatic setting; tenant advised to avoid the hot tap at full temperature meanwhile (ACT-4, ACT-1). No occupant vulnerability is recorded on this case.
- [data_quality] Landlord asserts the front-door work 'should already have been done' and reports a Saturday visit by his contractor to an empty property; neither is supported by any completion or attendance record. → Recorded as a conflict and the factual position restated to the landlord (ACT-3, ACT-5).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "004", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed (ledger) | message=Dear Ms Vale, regarding the front-door lock at 18 Larkspur… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_contractor | completed (ledger) | message=For the attention of Dorian Wren (contractor instructed by… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed (ledger) | message=Dear Mr Elde, front entrance lock, 18 Larkspur Quay — statu… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | create_human_task | completed (ledger) | queue=property_management, title=18 Larkspur Quay — three unowned tenant issues raised 9 Sep…, summary=On 9 September (event-021) the tenant raised three matters… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 7 | add_note | completed (ledger) | note=Lock, 18 Larkspur Quay. Authority position: landlord approv… | {"id": "ACT-5"} | CAP-LOG |
| 8 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — decision whether his contractor (Dor…, until=3 days from today (landlord reply window); contractor reply… | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Will Dorian Wren fit the replacement front-door lock on a stated date, or do you authorise Northbridge Lettings to instruct its own locksmith (priced quote to you for approval before work starts)? (blocking; RTE-LANDLORD: choosing/confirming the contractor and any spend is the landlord's decision; his 1 Sept instruction bars us from instructing another provider and no standing spend cap is on file.)
- Ask **contractor**: Dorian Wren: did you attend on 16 September, what was done, is the door currently secure, and what is your firm date and two-hour arrival window to fit the replacement lock? (blocking; RTE-CONTRACTOR: attendance and availability are the contractor's to confirm; no visit or completion is recorded (event-018, event-019, event-023).)
- Ask **tenant**: Did Mr Wren attend on 16 September and fit a new lock, and can the front door currently be locked and left secure when you are out and overnight? (blocking; RTE-TENANT: whether the door still secures decides whether this stays urgent or becomes an emergency make-safe (lock reported worse at event-020).)

Promises made or recorded:
- agency → tenant: Come back with a confirmed appointment once the contractor or landlord gives a date; treat the door as an emergency make-safe if it cannot be locked [open]
- agency → landlord: Send a priced quote for approval before any agency-instructed work starts [open]
- agency → contractor: Report back to the landlord if no firm date is given by 12:00 on the second working day by 12:00 on the second working day from today [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day

## System notes

- reviewer: R2: safety_hazard flag(s) recorded for the reader; not an escalation on their own (urgency urgent)
