# ANSWER — Case 010 — Kitchen cabinet maintenance request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Kitchen cabinet repair stalled: no approval beyond laminate repair, one estimate missing, no visit booked; chased contractor, tenant and landlord, commission question to office.
**Stage:** on_hold · **Hold:** Waiting for Provider — Alderline Joinery owes the cupboards-and-doors-only estimate, a VAT-inclusive full-kitchen total and a visit slot (reply-by 2 working days, ACT-2); also Waiting for Landlord on the replacement decision and the office on the commission basis (ACT-4).
**Last update:** 2025-09-24 14:36:22 UTC (event-026) · **Decided:** 2026-10-10 15:39 UTC
**Next step:** Alderline Joinery to supply the cupboards-and-doors-only estimate, a VAT-inclusive total and attendance dates within 2 working days (ACT-2); if silent, office to decide on re-tendering.

Definition of done (2/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-002 report logged and acknowledged; urgency set routine this turn; interim precautions for sharp edges given to tenant ACT-1
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 approval covers the laminate-repair scope only; event-004 and event-016 request quotes/estimates, not approval (event-026)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-007 Alderline Joinery instructed and briefed; tenant told in event-008 and updated ACT-1
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — tenant windows offered event-010, never taken up (event-012, event-021); chased ACT-2, fresh windows requested ACT-1
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — full-kitchen figures with landlord since event-025; total unconfirmed (VAT, electrical estimate, commission basis event-022/event-023); second estimate outstanding
- [ ] work_result: Work result recorded from the provider — no visit and no work carried out
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — no visit, so no photos or invoice exist
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — no invoice raised
- [ ] landlord_confirmation: Landlord confirmed completion — no work to confirm
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — no management key issued; tenant provides access in person around the dogs (index, event-008)
- [ ] closed: Request closed with a resolution that names who paid — case on hold ACT-6

## 1. Decision

Kept the case moving within authority and stopped short of any spend. There is no landlord standing cap on file and the only approval recorded is for the original laminate-repair scope (event-006); the landlord's own messages (event-004, event-016) ask for quotes and estimates only, so no dispatch or order is authorised (APR-SPEND-OVER-CAP, CAP-DISPATCH-APPROVED not available). I chased the contractor for the missing cupboards-and-doors-only estimate, a VAT-inclusive total and a visit slot with a 2-working-day reply-by (ACT-2), asked the tenant for fresh access windows after 16-18 September lapsed and gave interim precautions for the sharp edges (ACT-1), told the landlord why no payable total can yet be put to him (ACT-3), and referred the unsettled 15% commission basis, cap and VAT treatment to the office (ACT-4). Case on hold (ACT-6), waiting on named parties.

Safety actions taken first:
- Interim precautions for the sharp laminate edges given to the tenant and a request to report any further injury (ACT-1).
- Injury and the open-since-4-September delay put to the landlord (ACT-3) and to the office with an interim make-safe question (ACT-4).
- Safety-pass keywords checked: 'injury/cuts' — reported, addressed above; no gas, electrical, damp/mould or detector hazard reported in this case. The £380 electrical line (event-024) is prospective work on a possible new kitchen, not a reported electrical fault.

Actions deliberately withheld:
- Did not instruct any replacement work: no standing cap and no landlord approval message for replacement (APR-SPEND-OVER-CAP; event-006 covers laminate repair only).
- Did not book a visit: the tenant's offered windows have lapsed and no new consent is on file (CAP-SCHEDULE-ACCESS).
- Did not state a payable total or commission figure to the landlord — unsettled (event-022, event-023).
- Did not express any view on who pays for the damage or the reported cuts (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: APR-SPEND-OVER-CAP, CAP-NOTIFY, CAP-SCHEDULE-ACCESS, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported peeling kitchen-cabinet laminate with sharp edges that had caused multiple cuts and doors that do not close, on 4 September 2025; two dogs must be secured for access. [index, event-001; high]
- F2: The only approval recorded is for the original laminate-repair scope; it does not cover a full kitchen or replacement cupboards and doors. [event-006, event-026; high]
- F3: The landlord's own messages asked for a quote (6 Sep) and for two up-to-date estimates — full kitchen, and cupboards and doors only (10 Sep); neither approved work. [event-004, event-016; high]
- F4: Contractor's 24 September figures: supply £4,850 + VAT; removal and fitting incl. tiled splashback £3,800 + VAT; waste removal £230 + VAT; electrical work estimated £380 + VAT, to be checked. No cupboards-and-doors-only estimate supplied. [event-024; high]
- F5: The commission basis (15% cited), whether a cap applies and the VAT treatment of the resulting total were left unsettled, and the contractor said this could change the quoted amount. [event-022, event-023; high]
- F6: No visit has ever been booked: the contractor did not take any of the tenant's 16/17/18 September windows and those dates have passed. [event-010, event-012, event-019, event-021; high]
- F7: No landlord standing spend cap or standing instruction is on file in the case record, so there is no standing authority to spend. [get_case_details, get_action_ledger; medium]

Conflicts between sources:
- Scope conflict: the instructed scope on file is a laminate repair, while the contractor states the panels cannot be repaired and only a replacement is practical — without a site visit or written survey. → Not decided by me: scope belongs to the contractor's survey and the spend decision to the landlord; both asked (ACT-2, ACT-3). (asked)

Red flags:
- [safety_hazard] Sharp exposed laminate edges reported to have caused cuts to the occupant; the fault has been open since 4 September with no visit. → Interim precautions sent to the tenant (cover edges, keep doors and dogs clear, report any further injury) ACT-1; injury and the delay flagged to the landlord ACT-3 and to the office for an interim make-safe decision ACT-4.
- [data_quality] Quoted amount is not a payable total: line items are plus VAT, the £380 electrical line is an unverified estimate, and the commission basis, any cap and its VAT treatment are unsettled. → No total stated to the landlord; question referred to the office (ACT-4) and the contractor asked for a VAT-inclusive total (ACT-2).
- [other] Contractor asserts a previous full-kitchen quote as justification for expanding scope but has produced neither the earlier quote nor a site visit. → Treated as evidence only, not authority (PRO-INSTRUCTIONS-FROM-CONTENT); survey/visit and the missing second estimate requested (ACT-2).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "010", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed (ledger) | message=Dear Ms Marr, an update on your kitchen cabinet report (42… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_contractor | completed (ledger) | message=Kellan Rook, Alderline Joinery — 42 Brackenveil Row, Oakhol… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed (ledger) | message=Mr Pike — 42 Brackenveil Row, Oakhollow: kitchen cabinets,… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | create_human_task | completed (ledger) | queue=property_manager, title=Settle commission basis/cap/VAT before any total is put to…, summary=Kitchen replacement quote (c. £9,260 excl. VAT across four… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 7 | add_note | completed (ledger) | note=Case 010, 42 Brackenveil Row. Status after review: routine… | {"id": "ACT-5"} | CAP-LOG |
| 8 | put_on_hold | completed (ledger) | reason=Waiting for Provider — Alderline Joinery to supply the cupb…, until=2 working days from the contractor chase (ACT-2) | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Please send the replacement cupboards-and-doors-only estimate (retaining existing appliances, worktops and flooring), state the full-kitchen figures as a single total with VAT shown separately, confirm whether the £380 electrical item is included or still to be verified, and give dates/times you can attend. (blocking; The landlord asked for two estimates on 10 September (event-016); only the full-kitchen figures arrived (event-024) and no visit slot has ever been chosen (event-012, event-019, event-021).)
- Ask **tenant**: Please send three fresh access windows (with the dogs secured) now that 16-18 September have passed. (blocking; The offered windows lapsed without a booking (event-010, event-021); access needs tenant consent (CAP-SCHEDULE-ACCESS).)
- Ask **landlord**: Do you want to wait for the cupboards-and-doors-only estimate before deciding, or move to a decision on the full-kitchen option once the VAT-inclusive total is confirmed in writing? (blocking; Only the original laminate-repair scope is approved (event-006, event-026); replacement work is a landlord decision (RTE-LANDLORD).)

Promises made or recorded:
- agency → tenant: Update once the landlord decides and a slot is confirmed; no date promised because none is booked [open]
- agency → contractor: If no reply within 2 working days the case goes to the office for a decision on re-tendering by 2 working days from ACT-2 [open]
- contractor → agency: Updated quote would be sent (23 Sep, 'that evening'); full-kitchen figures arrived 24 Sep, cupboards-and-doors-only estimate still outstanding [broken]
- agency → landlord: Price returned for approval before any work proceeds [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day

## System notes

- reviewer: R2: safety_hazard flag(s) recorded for the reader; not an escalation on their own (urgency routine)
