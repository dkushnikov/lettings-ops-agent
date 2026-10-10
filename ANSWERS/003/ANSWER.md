# ANSWER — Case 003 — Bathroom and kitchen maintenance

**Disposition:** NEEDS_INFO · **Urgency:** urgent · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Taps repaired; vent leak and bedroom damp still uninvestigated — landlord asked to approve a £150 damp inspection, contractor chased for a corrected priced invoice.
**Stage:** on_hold · **Hold:** Waiting for Landlord — approval of the £150 damp/roof-ingress inspection (ACT-1, reply-by 3 working days); in parallel Waiting for Provider (corrected priced invoice and visit findings, ACT-4, by 19/09) and Waiting for Tenant (damp/mould status, vulnerability, key, ACT-2).
**Last update:** 2025-09-14 09:20:00 UTC (event-023) · **Decided:** 2026-10-10 15:37 UTC
**Next step:** Landlord (Owen Vale) to approve the £150 damp/roof-ingress inspection so a specialist can be instructed and an access window agreed with the tenant.

Definition of done (2/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 report; event-002 acknowledged within one working day; urgency set urgent for the ingress/damp element; damage-limiting advice on water near electrics given at ACT-2
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-004 approved the original attendance, but the gate rejected it as spend authority for the new damp inspection; approval requested at ACT-1
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Plumber assigned and briefed for the taps (event-008); no provider yet assigned for the vent/damp scope — dispatch blocked, awaiting ACT-1
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-017/event-019 revised slot 12 Sept late morning, confirmed with tenant and contractor; access occurred (event-020). A further visit for the damp scope is not yet bookable.
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No priced quote exists for the vent/damp works; the tap invoice (event-022) carries no amount
- [ ] work_result: Work result recorded from the provider — Tap works recorded at event-022; no result for the vent ingress or bedroom damp (event-021) — contractor asked at ACT-4
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Invoice received (event-023) but names a different property and no amount; corrected copy requested at ACT-4; no visit report or photos
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Not forwarded — address and amount unresolved (ACT-3 explains; office verification at ACT-5)
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord updated at ACT-3; no confirmation of completion, and scope is incomplete
- [ ] keys_returned: Keys returned, where a management key was issued for the visit — Key arrangement offered (event-006/event-011) but tenant let the contractor in (event-020); key issue/return status queried at ACT-2 and ACT-4
- [ ] closed: Request closed with a resolution that names who paid — Scope incomplete and invoice unverified; not closed

## 1. Decision

Taps are complete (event-022) but the bathroom vent ingress and bedroom damp from the 3 September report were never investigated (event-021). I could not dispatch a damp/roof specialist: the gate rejected event-004 as spend authority and no landlord cap is on file (APR-SPEND-OVER-CAP), so I requested landlord approval of a £150 inspection (ACT-1). I chased the contractor for a corrected, priced invoice and findings (ACT-4), asked the tenant about mould/worsening, vulnerability and keys (ACT-2), updated the landlord (ACT-3), and sent the invoice/property mismatch plus the landlord's unactioned insurance and roof-history requests to the office (ACT-5). No payment approved; nothing closed.

Safety actions taken first:
- Advised the tenant to contact us immediately if water comes in heavily or appears near a light fitting, socket or consumer unit (emergency route) — ACT-2
- Asked the tenant to disclose any vulnerable occupant so ESC-VULNERABLE can be applied — ACT-2
- Recorded the damp/mould check and requested a specialist inspection with moisture readings and photographs — ACT-1, ACT-6

Actions deliberately withheld:
- Did not retry the blocked contractor dispatch for the damp inspection (gate rejected the approval reference; approval requested instead).
- Did not forward the invoice to the landlord for payment while the property address and amount are unverified (PRO-PAYMENTS).
- Did not decide who pays or whether the ingress is an insurance matter (PRO-TENANT-LIABILITY; referred to the office).
- Did not close the request — scope incomplete.

Execution notes (what the runtime observed about the actions above):
- Action 4 assign_contractor: FAILED (rejected: event-004 is not a landlord message in the visible history (sender: Owen Vale (Landlord)); only the landlord'…); no effect recorded.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-REQUEST-APPROVAL, APR-SPEND-OVER-CAP, CAP-DISPATCH-APPROVED, CAP-HUMAN-TASK, CAP-LOG, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, CLK-S11, PRO-PAYMENTS, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-DISPATCH-APPROVED, CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY, CAP-REQUEST-APPROVAL

Key facts (source ids in brackets):
- F1: Tenant reported on 03/09/2025: dripping kitchen tap, bathroom hot tap dripping and hard to close, water through the bathroom vent in heavy rain, damp patches on the smaller bedroom ceiling and wall. [index, event-001; high]
- F2: Landlord Owen Vale replied 04/09 'Yes, please proceed' and asked the agency to check building insurance cover and review the flat's history of repeated roof leaks. [event-004; high]
- F3: The insurance and roof-history requests were logged as not completed and were still unaddressed in the 05/09 landlord update. [event-005, event-012; high]
- F4: Visit rebooked to Friday 12 September late morning after the contractor's 'Please cancel / Booked for tomorrow' messages; tenant agreed by phone; access took place on 12 September. [event-014, event-015, event-016, event-017, event-020; high]
- F5: Invoice NBL-003-INV-14 dated 14/09 covers a new kitchen mixer tap and a new brass insert and chrome head on the basin hot tap; it states no amount and gives the property as 'Flat 4, 28 Larkspur Quay, Brindlewick', not the instructed Flat 4, 8-12 Juniper Mews. [tap-works-invoice, event-022, index; high]
- F6: No findings were recorded for the bathroom vent ingress or the bedroom damp; the invoice covers taps only. [event-021, event-022; high]
- F7: No landlord standing spend cap is on file for this property, so default authority is £0 for non-emergency spend. [get_case_details, mandate CAP-DISPATCH-ROUTINE; medium]
- F8: Dispatch of a roofing/damp inspection citing event-004 as approval was rejected by the policy gate. [assign_contractor tool result; high]

Conflicts between sources:
- The contractor's invoice bills 'Flat 4, 28 Larkspur Quay, Brindlewick' while the agency record and the instruction name 'Flat 4, 8-12 Juniper Mews, Vellumford'; the contractor also called the building '8-10 Juniper Mews' on arrival before the tenant corrected him. → Not decided by me. Corrected invoice requested from the contractor (ACT-4) and the mismatch referred to the office for verification before any payment (ACT-5); no payment approved. (asked)
- Contractor said on 11/09 'Please cancel appointment. Job was done today', then corrected to 'Booked for tomorrow'; access in fact occurred on 12/09. → Agency note event-017 and the 12/09 access call event-020 supersede the cancellation message; the 12/09 late-morning visit stands. (source_hierarchy)

Red flags:
- [data_quality] Invoice NBL-003-INV-14 names a different property and omits the charge amount; contractor also misstated the building number on arrival. → Corrected priced invoice requested (ACT-4); mismatch referred to the office (ACT-5); invoice not forwarded for payment (ACT-3).
- [safety_hazard] Reported water ingress through the bathroom vent in heavy rain and damp patches to a bedroom ceiling and wall, uninvestigated since 03/09 — damp/mould keyword check. → Specialist inspection put to the landlord for approval (ACT-1); tenant asked to confirm mould, worsening and any vulnerable occupant, and advised to report water near electrics immediately as an emergency (ACT-2).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "003", "attachments_hidden": 0} | allow |
| 2 | get_attachment | completed | name=tap-works-invoice.pdf | {"name": "tap-works-invoice.pdf", "text": "B I L L I N G  D O C U M E N T Copper Finch Plumbing — Tap Works Invoice\nCopper Finch Plumbing\nInvoice reference:… | allow |
| 3 | get_action_ledger | completed |  | [] | allow |
| 4 | assign_contractor | failed | trade=roofing / damp investigation, description=Flat 4, 8-12 Juniper Mews, Vellumford, ZZ1 1ZZ. Outstanding…, urgency=urgent, estimated_cost_gbp=150, landlord_approval_ref=event-004 | rejected: event-004 is not a landlord message in the visible history (sender: Owen Vale (Landlord)); only the landlord's own message approves spend | CAP-DISPATCH-APPROVED |
| 5 | request_landlord_approval | completed (ledger) | subject=Damp / roof-ingress inspection at Flat 4, 8-12 Juniper Mews…, amount_gbp=150, rationale=The plumber's visit on 12/09 covered the taps only (invoice… | {"id": "ACT-1"} | CAP-REQUEST-APPROVAL |
| 6 | notify_tenant | completed (ledger) | message=Update on your maintenance report of 3 September (ref 003,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_landlord | completed (ledger) | message=Flat 4, 8-12 Juniper Mews, Vellumford — maintenance ref 003… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_contractor | completed (ledger) | message=Copper Finch Plumbing — ref NBL-003-INV-14, our maintenance… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | create_human_task | completed (ledger) | queue=property_manager, title=Invoice/property mismatch + unactioned landlord requests —…, summary=Two items need a person.  1. Records disagree on the proper… | {"id": "ACT-5"} | CAP-HUMAN-TASK |
| 10 | add_note | completed (ledger) | note=Ref 003. Dispatch of roofing/damp inspection was blocked by… | {"id": "ACT-6"} | CAP-LOG |
| 11 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — approval of the £150 damp/roof-ingre…, until=2025-09-19 | {"id": "ACT-7"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you approve a roofing/damp specialist attending Flat 4, 8-12 Juniper Mews for an inspection and written report at an estimated £150 (inspection only; any repair quoted separately for your approval)? (blocking; No standing spend cap on file and the 4 Sept 'please proceed' was not accepted as authority for this new instruction (APR-SPEND-OVER-CAP); the vent ingress and bedroom damp have been open since 3 September (CLK-S11).)
- Ask **contractor**: Please send a corrected invoice for NBL-003-INV-14 showing the property we instructed (Flat 4, 8-12 Juniper Mews, Vellumford) and the amount with VAT, and confirm (a) whether the bathroom vent ingress and bedroom damp were looked at on 12 September and any findings, (b) whether an office key was collected and returned. (blocking; The invoice bills a different address and states no amount, so it cannot be forwarded to the landlord; scope and key status are unresolved.)
- Ask **tenant**: Since 3 September, has the vent leaked again, have the damp patches grown, is there visible mould or smell, is anyone in the household vulnerable (respiratory condition, young child, pregnancy, disability), and did the plumber use an office key or did you let him in? (non-blocking; Determines whether urgency must be raised to emergency/welfare escalation and whether a management key is outstanding.)

Promises made or recorded:
- agency → tenant: Contact the tenant to agree an access window, with at least 24 hours' notice, once the landlord approves the damp inspection [open]
- agency → landlord: Forward the corrected, priced invoice once it matches this property; come back on the insurance and roof-leak history after office review [open]
- contractor → agency: Corrected priced invoice, confirmation of what was inspected, and key status by 2025-09-19 [open]
- landlord → agency: Decision on the £150 damp/roof-ingress inspection by 3 working days from ACT-1 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- CLK-AWAAB-PRS [proposed]: Damp/mould timescales (reference only)

## System notes

- reviewer: R2: safety_hazard flag(s) recorded for the reader; not an escalation on their own (urgency urgent)
