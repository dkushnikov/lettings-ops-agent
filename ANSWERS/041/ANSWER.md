# ANSWER — Case 041 — Case 041: Washing Machine Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Landlord's own contractor reportedly fixed the washing machine; tenant asked to confirm before closure, case on hold, no agency spend.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation that the washing machine completes a full cycle after the landlord's operative attended (event-023); landlord also asked for the attending firm and the towel rail part date (ACT-3). Review in 3 days.
**Last update:** 2024-10-02 09:23:56 UTC (event-025) · **Decided:** 2026-10-10 14:12 UTC
**Next step:** Tenant to confirm the washing machine now spins and drains (asked ACT-2; 3-day wait, then chase or close).

Definition of done (6/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (fault logged), event-009 (damage-limiting drain-pump advice to tenant); urgency set routine this turn.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-011/event-021: landlord declined agency instruction and used his own operatives; no agency spend (event-025).
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's own operatives (event-021); tenant told who would contact them (event-012).
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-019: appointment booked for the landlord's contractor on Tuesday 02/10; access handled directly with the tenant.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No agency quote proceeded; the £65.00 + VAT estimate (event-003) was never instructed.
- [ ] work_result: Work result recorded from the provider — Landlord reports the machine fixed (event-023) but no provider report and no tenant confirmation; tenant asked (ACT-2).
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice available — work carried out by the landlord's own contractor outside agency instruction (event-021, event-023); reason recorded in ACT-1.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-025: completed without payment; no agency cost arose (ACT-1).
- [x] landlord_confirmation: Landlord confirmed completion — event-023: landlord confirmed the washing machine has been fixed.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant gave access directly (event-012, event-019).
- [ ] closed: Request closed with a resolution that names who paid — Held pending tenant confirmation (ACT-4) and the outstanding towel rail part (event-023).

## 1. Decision

The landlord handled this repair with his own operatives and reported the washing machine fixed (event-023); the agency instructed no contractor and incurred no spend (event-025). Because the tenant had previously reported that the advised self-help steps failed (event-014), I did not close the request: I asked the tenant to confirm the machine now spins and drains, asked the landlord to confirm which firm attended and the towel rail part fitting date, and placed the case on hold (Waiting for Tenant).

Safety actions taken first:
- Safety-pass check: no gas, electrical, damp/mould, detector or occupant-vulnerability keyword appears in the artefacts for this appliance fault; standing water was contained by the tenant draining the machine (event-001) and no water-near-electrics risk was reported, so no hazard flag raised.

Actions deliberately withheld:
- Did not instruct an appliance engineer: the landlord declined agency instruction and used his own contractor (event-011, event-021); no standing spend cap is on file (APR-SPEND-OVER-CAP).
- Did not close the request: work result is unverified by tenant or provider and the towel rail part is outstanding (CAP-CLOSE).
- Did not comment on who pays for any call-out (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, RTE-TENANT, RTE-LANDLORD, APR-SPEND-OVER-CAP, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 19/09/2024 that the washing machine at Flat 18, 108 Lantern Quay does not spin or drain at the end of any cycle; tenant had already cleaned the filter and manually drained twice. [index, event-001; high]
- F2: No hazard reported: no water ingress, no electrical fault, no loss of an essential service; a washing machine is a non-essential appliance, so the case is routine under CLK-S11. [event-001; high]
- F3: Agency emailed the landlord on 21/09 advising an appliance engineer at a minimum of £65.00 + VAT and asked for approval to arrange it. [event-003; high]
- F4: The landlord did not approve agency instruction; he said he would use his own people — operative Amelia to contact the tenant for access and also check the towel rail. [event-011, event-012; high]
- F5: Self-help drain-pump advice was sent to the tenant on 24/09; the tenant reported it did not resolve the fault. [event-009, event-014; medium]
- F6: Amelia attended on 29/09 but could not fix the machine; the landlord then passed the job to a firm he named as Willow Services, noting the machine was fitted new on 21 June 2021. [event-021; high]
- F7: An appointment for the landlord's contractor was booked for Tuesday 02/10. [event-019; high]
- F8: On 02/10 the landlord emailed confirming the washing machine has been fixed (attributing the work to Lantern Solutions) and that a replacement towel rail part has been ordered and will be fitted on receipt. [event-023; high]
- F9: No agency contractor was instructed and no agency spend arose; the request was marked completed without payment. [event-024, event-025, get_action_ledger; high]
- F10: The same fault history exists at the property: in May 2023 previous tenants reported the machine not emptying and Lantern Solutions unblocked the sink spigot. [event-011; medium]

Conflicts between sources:
- Provider identity for the successful repair: event-021 says the landlord passed the job to Willow Services; event-023 says Lantern Solutions attended and fixed it. → Both statements come from the landlord and both describe his own contractor; no agency instruction or invoice turns on it. Asked the landlord to confirm for the record (ACT-3); not action-changing, so not escalated. (asked)
- Two tenant emails one minute apart on 24/09: one reports the advised fix did not work (event-014), the other only thanks the agency for the update (event-015). → Treated the substantive report (event-014) as the fault status at that date; superseded by the landlord's 02/10 repair report (event-023), which is being verified with the tenant. (source_hierarchy)

Red flags:
- [data_quality] Correspondence names are inconsistent: landlord emails address 'Bennett' (event-023, event-024) while the case manager on file is Noah Ingram (event-017). Names in message bodies were not copied into letters to other parties. → Recorded in case note ACT-1; parties addressed only by their case-record roles.
- [data_quality] Conflicting contractor names for the completed repair (Willow Services vs Lantern Solutions). → Non-blocking question put to the landlord (ACT-3); logged in ACT-1.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "041", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Status review. Landlord took the job on with his own operat… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_tenant | completed | message=Good afternoon,  Your landlord has confirmed to us that his… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed | message=Good afternoon,  Thank you for confirming the washing machi… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | put_on_hold | completed | reason=Waiting for Tenant — confirmation that the washing machine…, until=3 days from today | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Is the washing machine now spinning and draining normally on a full cycle following the landlord's operative's visit? If not, please tell us what it is still doing. (blocking; The tenant earlier reported the advised steps had not resolved the fault (event-014); completion must be verified before the request is closed.)
- Ask **landlord**: Which firm carried out the repair (event-021 names Willow Services, event-023 names Lantern Solutions), and what is the expected fitting date for the ordered towel rail part? (non-blocking; Record accuracy and a timescale to give the tenant; does not block closure of the washing machine item.)

Promises made or recorded:
- agency → tenant: Keep the request open until the tenant confirms the machine is working; take the repair forward again if it is not. [open]
- landlord → agency/tenant: Fit the ordered replacement towel rail part once received. [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
