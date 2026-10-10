# ANSWER — Case 022 — Washer-dryer maintenance and replacement update

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Washer-dryer E13 unresolved since 20 Aug; landlord's self-arranged replacement has no delivery date and the tenant says nothing arrived — landlord chased, tenant updated, case on hold.
**Stage:** on_hold · **Hold:** Waiting for Landlord — delivery/installation date, installer details and outcome of the 9 September engineer visit requested 2025-09-25, reply-by 2025-09-29 (ACT-2, ACT-4); secondary wait on the tenant to clarify event-031.
**Last update:** 2025-09-25 09:08:19 UTC (event-031) · **Decided:** 2026-10-10 15:43 UTC
**Next step:** Landlord (Nessa Orin) to supply the delivery/installation date and installer details by 29 September 2025; if none, put a quote recommendation for supply, install and disposal to her for approval.

Definition of done (2/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — index + event-007: E13, appliance unusable, categorised routine (no emergency definition engaged); acknowledged event-001.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-010, event-027, event-029: landlord is using her own insurer/retailer route; no agency spend engaged.
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Provider is the landlord's own retailer/installer; name and contact not supplied — requested in ACT-2.
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — 9 September window was passed to the tenant (event-019, event-020) but the replacement delivery/installation has no date (event-029, event-030); chased in ACT-2.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No agency quote raised; landlord purchased the replacement directly (event-027, event-029). Landlord's quote request of 21 September (event-028) was superseded by event-029.
- [ ] work_result: Work result recorded from the provider — No outcome recorded for the 9 September visit (event-022 unanswered); event-031 'job is completed' is ambiguous and contradicted by event-030.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No service report, order confirmation or invoice on file; requested from the landlord in ACT-2.
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Costs sit with the landlord's insurer/direct purchase; no agency invoice to forward (event-010, event-029).
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord has not confirmed delivery or installation completion; asked in ACT-2.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant is home for access (event-009, event-013).
- [ ] closed: Request closed with a resolution that names who paid — Case on hold (ACT-4); work result and delivery unconfirmed.

## 1. Decision

The washer-dryer (E13) is being handled by the landlord through her own insurer/manufacturer route and now a replacement she purchased herself, so no agency spend or dispatch arises and no contractor of ours is instructed (event-010, event-027, event-029). The case cannot be closed: the landlord says delivery, installation and disposal were arranged (event-029) while the tenant says nothing has arrived (event-030), and no date exists in any artefact. I chased the landlord for the delivery/installation date, installer details and the 9 September visit outcome with a reply-by of 29 September (ACT-2), answered the tenant's question that the replacement is still planned without promising a date and asked them to clarify their ambiguous "the job is completed" (ACT-3), recorded the conflict and the mm/cm data error (ACT-1), and placed the ticket on hold (ACT-4). I did not treat event-031 as completion and did not close the request.

Safety actions taken first:
- Safety pass: no hazard keyword condition arises on the facts — the fault is an appliance error code with water already drained by the tenant (index); no water ingress, electrical fault, burning smell or hazard is reported anywhere in the artefacts, and no vulnerable-occupant detail is recorded. No emergency definition engaged, so no make-safe step was required.
- Tenant advised of status without a promised date; no occupant health or family data shared with any third party (PRO-PII).

Actions deliberately withheld:
- Did not close the request on the strength of event-031 ('Yes, the job is completed') — ambiguous and contradicted by event-030.
- Did not instruct a contractor: no agency spend authority on file and the landlord is using her own supplier (APR-SPEND-OVER-CAP, F9).
- Did not book an access window: no delivery or installation date exists to book against (CAP-NOTIFY).
- Did not comment on who bears the cost of the appliance or the delay (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-REQUEST-APPROVAL, RTE-LANDLORD, RTE-TENANT, APR-SPEND-OVER-CAP, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported washer-dryer error E13 at 8 Brackenmere Walk on 2025-08-20; draining the water did not fix it. [index, get_case_details; high]
- F2: Tenant confirmed by phone on 2025-08-26 that the machine was unusable and laundry was waiting. [event-007; high]
- F3: The landlord chose to handle the fault through her insurer and the manufacturer's service arrangement rather than an agency contractor. [event-004, event-010, event-011; high]
- F4: An engineer visit was reported for 2025-09-09, 12:00-17:00; the tenant acknowledged the window on 2025-09-07. No booking confirmation document was supplied and no visit outcome was ever reported. [event-018, event-019, event-020, event-021, event-022; high]
- F5: On 2025-09-14 the landlord said a replacement washing machine was needed, implying the repair route failed. [event-023; medium]
- F6: On 2025-09-19 and 2025-09-21 the landlord said a new machine had been ordered and that delivery, setup and disposal of the old unit were arranged; no date was given. [event-027, event-029; medium]
- F7: On 2025-09-24 the tenant said no replacement had arrived and there was no packaging at the property. [event-030; high]
- F8: The existing appliance is integrated and fixed to the cabinet door; rear connections were not inspected; tenant's clearance estimate is ~835 mm against a proposed 825 mm unit. [event-025, event-026; medium]
- F9: No landlord standing spend cap or standing instruction is on file in this case record; no agency contractor has been instructed and no agency spend arises. [get_case_details, get_action_ledger; medium]
- F10: The tenant requires at least three hours' notice of attendance and is generally home. [event-013; high]

Conflicts between sources:
- Landlord states delivery, setup and disposal were arranged on 21 September; tenant states on 24 September that nothing had been delivered and no packaging was present. No delivery date exists in any artefact. → Landlord asked for the delivery/installation date and installer details with a 29 September reply-by (ACT-2); tenant kept informed without a promised date (ACT-3). (asked)
- Tenant's 2025-09-25 reply 'Yes, the job is completed' contradicts their 2025-09-24 statement that no replacement had arrived, and the same message asks whether the washing-machine change is still happening. → Not treated as completion; tenant asked to clarify which job it refers to (ACT-3). Request left open. (asked)
- Landlord described appliance heights as 825 cm and 820 cm; the agency corrected this to millimetres when asking the tenant to measure. → Read as millimetres; recorded as a data-quality issue in ACT-1. Fit remains unverified because rear connections were not inspected. (tool_check)

Red flags:
- [data_quality] Landlord quoted appliance dimensions in cm ('825 cm high', previous '820 cm') where mm was meant; tenant's 835 mm clearance is an estimate and the integrated unit's rear connections were never inspected, so fit and disconnection requirements are unverified. → Recorded in case note ACT-1; installer scope (disconnection, door refit, removal) put to the landlord in ACT-2.
- [other] Repeated third-party claims with no supporting document: insurer approval, engineer booking for 9 September and 'sorted it' delivery arrangement were all reported by the landlord with no confirmation attached. → Treated as untrusted evidence only; no date promised to the tenant and order/installer reference requested from the landlord (ACT-2, ACT-3).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "022", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=engineer attended repair outcome completed | [] | allow |
| 4 | search_history | completed | query=delivery installation date replacement | [] | allow |
| 5 | add_note | completed (ledger) | note=Status review 2025-09-25. Fault: washer-dryer error E13, re… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_landlord | completed (ledger) | message=Dear Ms Orin,  Re: 8 Brackenmere Walk, Vellumford — washer-… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_tenant | completed (ledger) | message=Dear Mr Dalen,  Re: 8 Brackenmere Walk — washer-dryer (erro… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — delivery/installation date, installe…, until=2025-09-29 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: What is the confirmed delivery and installation date/time window for the replacement washing machine, who is the retailer/installer (name plus contact or order reference), and will they disconnect the old integrated unit, refit the cabinet door and take the old machine away? (blocking; You confirmed on 21 September that delivery, setup and disposal were arranged (event-029), but the tenant reported on 24 September that nothing had arrived (event-030) and no date is on file; without it no access can be booked.)
- Ask **landlord**: Did the engineer attend on 9 September and what was the outcome — is there a service report or insurer/manufacturer reference? (non-blocking; The visit was only reported as expected (event-021); no outcome was ever recorded, and the work result is needed before the case can be closed.)
- Ask **tenant**: Your message said 'Yes, the job is completed' — does that refer to a different job, or has something been done to the washer-dryer? Did an engineer attend on 9 September, and is the appliance working now? (blocking; Event-031 is ambiguous and contradicts event-030; the agency's 10 September question (event-022) was never answered.)

Promises made or recorded:
- agency → tenant: Pass on the delivery/installation window as soon as the landlord provides it; no date promised. [open]
- agency → landlord: If no date by 29 September, put a recommendation for an agency quote (supply, install, disposal) to the landlord for approval. by 2025-09-29 [open]
- landlord → agency: Delivery, setup of the new machine and disposal of the old unit arranged. [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- APR-SPEND-OVER-CAP [sop]: Landlord reply window deadline 2025-09-29
