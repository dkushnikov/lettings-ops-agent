# ANSWER — Case 041 — Case 041: Washing Machine Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Washing machine fault repaired by the landlord's own contractor at no agency cost; held for the tenant to confirm it works before closure, contractor-name conflict sent to the office.
**Stage:** on_hold · **Hold:** Waiting for Tenant — Turner to confirm the washing machine completes a cycle and drains/spins; asked 02/10 (ACT-2), chase after 3 days.
**Last update:** 2024-10-02 09:23:56 UTC (event-025) · **Decided:** 2026-10-10 13:31 UTC
**Next step:** Tenant (Turner) to confirm the washing machine is working; on confirmation the agency closes the request as completed without payment (landlord's own contractor).

Definition of done (6/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 fault logged; routine, no hazard; damage-limiting self-help given to tenant at event-009
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-003 agency sought approval; landlord chose to use his own operatives instead (event-011, event-021) — no agency spend
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's operative arranged by landlord (event-011); tenant told who would contact them (event-012)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-019 appointment booked for landlord's contractor 02/10; access handled direct by the landlord's contractor with the tenant (event-021)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No agency quote instructed; the £65.00 + VAT estimate at event-003 was superseded by the landlord using his own contractor
- [ ] work_result: Work result recorded from the provider — Landlord states the machine was fixed (event-023), but no provider report; tenant confirmation requested (ACT-2)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No agency-instructed provider, so no photos or invoice to the agency; landlord's contractor billed the landlord direct (event-025)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-025 — task recorded as completed without payment; no agency invoice arises
- [x] landlord_confirmation: Landlord confirmed completion — event-023 — landlord confirms the washing machine has been fixed
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; access given by the tenant direct
- [ ] closed: Request closed with a resolution that names who paid — Held for tenant confirmation of the repair (ACT-4) before closing as completed without payment

## 1. Decision

The landlord took the job in-house: the agency's quote (minimum £65.00 + VAT for an appliance engineer, event-003) was never instructed, so no agency spend and no dispatch authority were needed. The landlord confirmed on 02/10 that his contractor repaired the machine (event-023) and the system marked it completed without payment (event-025). I did not close the request: the only work result on file is the landlord's statement — no provider report, photos or invoice — and the tenant's last substantive word on the fault (event-014) was that it was unresolved. I asked the tenant to confirm the machine now works (ACT-2), put the request on hold pending that reply (ACT-4), and referred the contractor-name conflict between event-021 ("Willow Services") and event-023 ("Lantern Solutions") to the office (ACT-3) rather than picking a side in a message to a party.

Safety actions taken first:
- Checked the report against the emergency definitions: appliance fault only — no gas, electrical, water-ingress, heating-loss, security or vulnerability indicator in any artefact; emergency-hazard playbook not triggered.

Actions deliberately withheld:
- Did not close the request: work_result unverified by the tenant or a provider, contrary to CAP-CLOSE.
- Did not instruct an appliance engineer: no standing spend cap on file and the landlord elected to use his own contractor (APR-SPEND-OVER-CAP, event-011/event-021).
- Did not state in any party message which contractor attended, given the conflicting records.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, RTE-TENANT, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Turner reported on 19/09/2024 that the washing machine at Flat 18, 108 Lantern Quay does not spin or drain at the end of a cycle; had already cleared the filter and drained it twice. [event-001, get_case_details; high]
- F2: Agency quoted the landlord a minimum of £65.00 + VAT for an appliance engineer and asked for authority to instruct on 21/09. [event-003; high]
- F3: No landlord standing spend cap is on file in this case record; the landlord instead chose to send his own operative (Amelia) and later his own contractor. [event-011, event-021; medium]
- F4: Machine was new on 21 June 2021; a similar non-emptying fault was reported by previous tenants on 25 May 2023 and fixed by Lantern Solutions (blocked sink spigot). [event-011, event-021; medium]
- F5: Landlord's operative attended 29/09 but could not fix it; landlord then passed the tenant's details to a contractor. [event-021; high]
- F6: Landlord confirmed on 02/10 that the washing machine has been repaired and that a replacement towel rail part is on order. [event-023; medium]
- F7: The request was marked by the system as completed without payment on 02/10. [event-025; high]
- F8: On 24/09 the tenant reported the advised self-help drain step had been tried twice and had not resolved the fault; this predates the contractor attendance. [event-014; medium]

Conflicts between sources:
- Which firm attended the washing machine: event-021 says the landlord gave the tenant's details to 'Willow Services'; event-023 says 'Lantern Solutions have been and fixed the washing machine'. → Not decided by me; referred to the office via human task ACT-3. Does not change the action — no agency contractor was instructed and no agency spend arises. (asked)
- The landlord's 02/10 email is addressed to 'Bennett' and an internal note says 'Landlord has dealt with as per Bennett', while the case manager of record is Noah Ingram. → Referred to the office (ACT-3); the message is on this ticket and names this property, so treated as relating to this case. No name from a message body copied into another party's letter. (asked)
- Tenant said the fault was unresolved (24/09) while the landlord says it is fixed (02/10). → The tenant's message predates the contractor visit, so is likely superseded; tenant asked to confirm current state before closure (ACT-2). (asked)

Red flags:
- [data_quality] Contractor identity and case-owner name inconsistent across records (Willow Services vs Lantern Solutions; Bennett vs Noah Ingram). → Recorded as a conflict and referred to the property manager queue (ACT-3); not asserted to any party.
- [data_quality] Event-014 is a third-person summary of a tenant email ('The customer reports...') rather than the tenant's own words, and conflicts with event-015 sent one minute later. → Treated as evidence of an unresolved fault at that date only; tenant asked directly for the current position.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "041", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Washing machine, Flat 18, 108 Lantern Quay. Reported by ten… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_tenant | completed | message=Good afternoon Turner,  Your landlord has confirmed that hi… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | create_human_task | completed | queue=property_manager, title=Flat 18, 108 Lantern Quay — which contractor attended the w…, summary=Two landlord emails on file disagree about who held the job… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 6 | put_on_hold | completed | reason=Waiting for Tenant — confirmation that the washing machine…, until=2024-10-07 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Is the washing machine now completing a cycle and draining/spinning normally after the landlord's contractor attended? If not, what does it do now? (blocking; The only work result on file is the landlord's statement (event-023); the tenant's last report on the fault (event-014) said it was unresolved. Confirmation is needed before the request can be closed.)
- Ask **property_manager**: Which firm actually attended — Willow Services (event-021) or Lantern Solutions (event-023) — and who is the correct case owner (Noah Ingram vs 'Bennett')? (non-blocking; Two records on file disagree; needed for the attendance/warranty record, not for the repair itself.)

Promises made or recorded:
- agency → tenant: Take the matter straight back to the landlord if the machine is still faulty [open]
- landlord → agency: Towel rail replacement part to be fitted once received (no date given) [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
