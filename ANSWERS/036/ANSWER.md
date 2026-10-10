# ANSWER — Case 036 — Case 036: Shower Tap Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Shower tap repair reported complete at no charge; chased provider for photos, asked tenant to confirm the fix and landlord to sign off; case on hold.
**Stage:** on_hold · **Hold:** Waiting for Provider — photographs and works date from Keystone Services (reply-by 12:00, 10 Nov 2026); tenant confirmation of the repair and landlord sign-off also outstanding.
**Last update:** 2026-11-07 07:14:06 UTC (event-052) · **Decided:** 2026-10-10 13:30 UTC
**Next step:** Keystone Services to send photographs of the completed work and the works date by 12:00 on 10 November 2026; if nothing arrives, record photos as not supplied and put the closure question to the landlord.

Definition of done (6/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (fault logged: broken shower pull knob, cap comes off); routine — no emergency keyword in any artefact
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 landlord's own email 'Yes please!'; confirmed event-007
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008 provider assigned; event-011 provider briefed; event-009 tenant told Keystone Services would attend
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-016/018/019 slot 29/09/2026 confirmed with both sides; later rebooked by provider with tenant, event-038/event-039 (9.30am Wed 4th)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was raised; contractor confirmed the work is free of charge under guarantee (event-050)
- [x] work_result: Work result recorded from the provider — event-050: 'this job is complete a new bath tap was fitted no charge' (quoted, untrusted provider email); tenant verification requested at ACT-1
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice supplied despite requests at event-048 and event-034; chased again at ACT-2 with reply-by 12:00 10 Nov 2026
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice due — recorded completed without payment, reason faulty tap replaced under guarantee (event-051, event-052); nil cost reported to landlord at ACT-3
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord last wrote asking for an update and photos (event-040, event-043); sign-off requested at ACT-3
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provided access directly to the provider (event-019)
- [ ] closed: Request closed with a resolution that names who paid — Held open — documents and landlord confirmation outstanding; ACT-5 hold until 10 Nov 2026

## 1. Decision

The repair is reported complete at no charge, but three closure checks are outstanding, so the ticket stays open on hold rather than being closed. Landlord authority for the instruction is already on file (event-006, the landlord's own "Yes please!", system-confirmed at event-007), and no spend decision arises because the contractor has confirmed the work is free of charge under the guarantee on the tap he fitted in February (event-050, consistent with event-025 and the agency's own "completed without payment" entry at event-052). Within my mandate I have: asked the tenant to confirm the shower and tap now work, including the extra symptom she reported to the contractor on 14 October (event-030); chased Keystone Services for the photographs the landlord has twice asked for (event-043, event-045) with a reply-by of 12:00 on 10 November 2026; reported the outcome and the nil cost to the landlord and told him we will seek his sign-off once photos and tenant confirmation are in; logged the file note and placed the case on hold. I did not close the request: documents, landlord confirmation and tenant verification are still pending, and a closure with those open would be premature. I did not decide liability for the faulty tap or accept the contractor's "no charge" as a final financial position for the landlord to sign — the landlord confirms that (RTE-LANDLORD, PRO-TENANT-LIABILITY).

Safety actions taken first:
- Safety pass run over all artefacts: no gas, electrical, detector, damp/mould, asbestos, injury or vulnerability keywords present in this case; no hazard advice required.
- Checked the report against the emergency definitions: a broken shower knob is not loss of water supply, water ingress or water near electrics, so the emergency-hazard playbook was not triggered.

Actions deliberately withheld:
- Did not call close_request: documents and landlord confirmation are still pending and the tenant has not verified the fix; closing now would fail the playbook's final checks.
- Did not dispatch any further contractor or incur spend: no new work is needed on the evidence, and there is no standing cap on file (APR-SPEND-OVER-CAP).
- Did not state who bears the cost of the faulty February tap (PRO-TENANT-LIABILITY, PRO-PAYMENTS).
- Did not quote the 03/11 or 04/11 date to the tenant or landlord as a completion date, since no booking record confirms which visit did the work.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-REQUEST-APPROVAL, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 13, 73 Juniper Mews, Northbridge, ZZ1 6ZZ; tenant on the case record is Noah Bennett. [index, get_case_details, event-019; high]
- F2: Fault reported 2026-09-24: shower pull knob broken, cap comes off each use; tenant has a video she could not attach. [event-001; high]
- F3: Landlord approved instructing a contractor in his own email of 2026-09-25 ('Yes please!'). [event-006, event-007; high]
- F4: Keystone Services was assigned and briefed; tenant notified of the provider. [event-008, event-009, event-011; high]
- F5: A visit was agreed for 29/09/2026 09:00-09:30 and confirmed to both tenant and provider. [event-015, event-016, event-018, event-019; high]
- F6: The job ran on because the tap the contractor fitted in February was faulty; a replacement part/tap was ordered and promised free of charge. [event-025, event-031; medium]
- F7: Contractor booked the installation for 9.30am Wednesday 4th (November) after confirming delivery of new taps. [event-038, event-039; medium]
- F8: Contractor confirmed on 2026-11-07 that the job is complete, a new bath tap was fitted, and there is no charge as the February tap was faulty. [event-050; medium]
- F9: The agency recorded the task as completed without payment, reason: no charge as faulty tap now replaced. [event-051, event-052; high]
- F10: The landlord has asked for photographs and raised concern about the length of time the works have taken; photographs have not been supplied. [event-040, event-043, event-045, event-048; medium]
- F11: On 2026-10-14 the tenant reported to the contractor that the shower and tap ran at the same time when a button was pressed; no record shows this symptom was verified as resolved. [event-030; medium]
- F12: No landlord standing spend cap is on file in this case record; the default cap is £0, so authority rests on the landlord's own approval event. [get_case_details, get_action_ledger; medium]

Conflicts between sources:
- Agency told the landlord the fitting visit was 03/11/26, while the contractor's own booking was 9.30am Wednesday 4th November. → Contractor owns scheduling (RTE-CONTRACTOR), so 4 November is the better record; immaterial now that the work is reported complete. Logged as data quality at ACT-4; no date quoted to any party. (source_hierarchy)
- Hold at event-035 was labelled 'Waiting for Landlord' while the outstanding item was a provider update/invoice. → Corrected: hold re-set as Waiting for Provider (ACT-5). (tool_check)

Red flags:
- [data_quality] Key events in this case are untrusted third-party summaries (call transcripts event-012/015/028/029/030/038, provider emails event-025/037/039/050, landlord emails event-040/043). Completion and nil cost rest on the provider's own single-line email (event-050) with no photos or invoice. → Treated as evidence only; sought independent confirmation from tenant (ACT-1) and documents from provider (ACT-2) before closure.
- [other] The 'no charge' position is the contractor's own statement about his own earlier workmanship; who ultimately bears any cost is not the agent's decision. → No liability determination made (PRO-TENANT-LIABILITY); nil-cost position reported to the landlord for his confirmation (ACT-3).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "036", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed | message=Dear Noah Bennett, regarding the shower/tap repair at Flat… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_contractor | completed | message=Keystone Services — Shower Repair Request, Flat 13, 73 Juni… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed | message=Dear Sawyer, update on the shower/tap repair at Flat 13, 73… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | add_note | completed | note=Case 036 review. Work result: contractor email event-050 (2… | {"id": "ACT-4"} | CAP-LOG |
| 7 | put_on_hold | completed | reason=Waiting for Provider — photographs of completed work and co…, until=2026-11-10 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Please send photographs of the completed shower/bath tap work at Flat 13, 73 Juniper Mews, the date the work was carried out, and written confirmation that no invoice will follow. (blocking; The landlord has twice requested photographs (event-043, event-045) and the file needs a documented work result and nil-cost confirmation before closure.)
- Ask **tenant**: Is the shower and tap now working correctly, including the fault you reported on 14 October where the shower and tap ran at the same time when the button was pressed? (blocking; Work result is only evidenced by the contractor's own email (event-050); tenant verification is needed before the job can be closed, and event-030 suggests a possible residual fault.)
- Ask **landlord**: Once photographs and the tenant's confirmation are in, are you happy for us to close this job as completed at no charge under the guarantee on the February tap? (non-blocking; RTE-LANDLORD: landlord confirmation of completion is a closure check and the landlord has raised concerns about delay and missing photos (event-043).)

Promises made or recorded:
- agency → contractor: If no photographs/works date by the reply-by time, we will record photos as not supplied and note that in the landlord's report. by 2026-11-10 12:00 [open]
- agency → landlord: Revert once photographs and the tenant's confirmation are in, and seek his sign-off to close. [open]
- agency → tenant: Arrange a return visit if the shower or tap is still not right. [open]
- contractor → tenant: Fit the replacement tap free of charge once the part arrived. [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-PROVIDER-REPLY [sop]: Provider reply-by for photographs deadline 2026-11-10 12:00
