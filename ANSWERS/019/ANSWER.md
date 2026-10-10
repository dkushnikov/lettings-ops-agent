# ANSWER — Case 019 — Case 019: Garden Maintenance Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Garden clearance was approved and done, but the file closed with landlord confirmation and the levelling/gravel scope unresolved; both are now back with the landlord.
**Stage:** on_hold · **Hold:** Waiting for Landlord — completion confirmation and decision on levelling/gravel scope; reply-by 3 working days from ACT-2, then refer to property manager.
**Last update:** 2025-04-16 09:16:13 UTC (event-044) · **Decided:** 2026-10-10 13:24 UTC
**Next step:** Landlord (Jenkins) to confirm the clearance is complete and say whether to quote for levelling and gravelling (emailed ACT-2; 3-working-day clock).

Definition of done (5/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged and categorised; routine urgency, no emergency definition matched; tenant asked at ACT-1 to report anything left unsafe.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-025 landlord approval for the removal element only.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-034 provider assigned; conflict over which provider recorded in ACT-3 and ACT-4.
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-029 slots offered to tenant; event-031 attendance recorded as completed.
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-019 quoted c.£600 and event-009 records £500+VAT; the landlord's approval (event-025) names no amount, so no approved figure is on file.
- [ ] work_result: Work result recorded from the provider — Only the agency's internal note event-031; no provider result report or photos (event-042).
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-042 — upload skipped, reason 'not applicable'; invoice attachment at event-038 unavailable.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-038 invoice emailed to the landlord.
- [ ] landlord_confirmation: Landlord confirmed completion — event-043 flagged it as needed; not received. Requested again at ACT-2.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant was present for access (event-016, event-029).
- [ ] closed: Request closed with a resolution that names who paid — event-044 closed the file with items above still open; ticket returned to on_hold at ACT-5 pending the landlord's reply.

## 1. Decision

The clearance element was approved by the landlord (event-025) and carried out (event-031, event-038), but the file was closed at event-044 one minute after event-043 recorded "Need confirmation from landlord", with no landlord confirmation, no provider work result, and the tenant's levelling/gravel items never quoted, decided or answered. I did not instruct any contractor — there is no landlord cap on file and no priced approval for further work (APR-SPEND-OVER-CAP). I updated the tenant, put the two open questions to the landlord with a 3-working-day reply-by, raised a human task for the provider/amount conflict and the rent-deduction entry, and put the ticket on hold pending the landlord's reply.

Safety actions taken first:
- Asked the tenant to report immediately, with photos, any material left behind or any part of the garden still unsafe after the clearance (ACT-1).

Actions deliberately withheld:
- Did not instruct any contractor for levelling or gravelling: no cap on file and no priced landlord approval (APR-SPEND-OVER-CAP).
- Did not re-close the request: final-check items remain pending (event-043).
- Did not process, confirm or reverse any rent deduction (PRO-PAYMENTS).
- Did not name a provider or an amount to the tenant or landlord while the agency records conflict (ESC-CONFLICT, rule 2).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, ESC-CONFLICT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant requested rubbish/construction-waste removal, ground levelling, gravel covering and making the garden safe at Flat 25, 185 Copperfield Walk on 17 Jan 2025. [index, event-001, get_case_details; high]
- F2: The agency's own process flagged that landlord approval was required before provider selection. [event-002, event-005; high]
- F3: The only landlord message in the history approving work is 'Please go ahead with the removal' (25 Mar 2025); it names no amount and covers removal only. [event-025; high]
- F4: The agency told the landlord the disposal quote would be around £600 because the material left in the garden is a specialised builders' material needing proper disposal. [event-019; high]
- F5: An earlier internal note records a different figure and provider: £500+VAT approved, Harbour Compliance going ahead. [event-009; medium]
- F6: The invoice came by email from a new provider with no portal access, so no work order was raised in the system. [event-033; high]
- F7: Tenant was offered two attendance days on 9 Apr 2025 and the clearance was recorded as done on 12 Apr 2025. [event-029, event-031; high]
- F8: Invoice was emailed to the landlord on 16 Apr 2025 with a statement that it would be deducted from the rental amount; the invoice attachment is unavailable. [event-038, get_attachment; high]
- F9: Document upload was skipped with reason 'not applicable'; no provider work-result report or photos are on file. [event-042; high]
- F10: The file recorded 'Need confirmation from landlord' at 09:15 and was closed as 'All checks have been completed' at 09:16 on 16 Apr 2025, with no landlord confirmation in between. [event-043, event-044; high]
- F11: No landlord standing spend cap is on file in this case record, so there is no standing authority for further spend. [get_case_details, CAP-DISPATCH-ROUTINE; medium]
- F12: The tenant chased for an update on 13 Mar 2025 and was never sent the outcome of the completed clearance before this review. [event-018, event-029; high]

Conflicts between sources:
- Provider and amount disagree across agency records: £500+VAT with Harbour Compliance (event-009) vs c.£600 with Oakley's contractor (event-019) vs an unnamed new off-portal provider who invoiced (event-033). → Not decided by me. Conflict recorded and referred to the office via human task ACT-3; no provider named to any party in my messages. (asked)
- Closure status conflicts with the final-checks record: landlord confirmation was outstanding (event-043) yet the request was closed as fully checked (event-044). → Landlord asked to confirm completion (ACT-2); ticket placed on hold (ACT-5) rather than left closed. (asked)
- Scope conflict: the approved and completed work covers removal only (event-025, event-031), while the tenant's request also covered levelling and gravel (event-001). → Landlord asked whether to quote for levelling/gravel; tenant told those items are not approved and nothing is booked. (asked)

Red flags:
- [data_quality] Request closed as 'all checks completed' one minute after a note saying landlord confirmation was still needed; no work-result report, no photos, invoice attachment unavailable. → Ticket reopened to on_hold, landlord asked to confirm, human task raised (ACT-3, ACT-5).
- [other] Agency message states the invoice would be processed and 'deduct[ed] off the rental amount' — money movement sits outside the agent mandate (PRO-PAYMENTS). → Referred to the property manager for verification; I took no payment action.
- [safety_hazard] Waste described as 'a specialised builders material that needs disposing of properly' (quoted, untrusted-origin relay); no asbestos or other hazard is named anywhere in the artefacts and the tenant reported no injury. Garden surface still un-levelled, so the tenant was asked to report anything left unsafe. → Tenant invited to report any remaining unsafe condition or material left behind (ACT-1); no emergency definition matched, so the maintenance-request playbook was kept.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "019", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=Harbour Compliance Oakley contractor quote invoice | [] | allow |
| 4 | get_attachment | completed | name=attachment-83-document | {"error": "no attachment named attachment-83-document"} | allow |
| 5 | notify_tenant | completed | message=Hello, an update on your garden request (Flat 25, 185 Coppe… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Hi Jenkins,  Re: Flat 25, 185 Copperfield Walk, Alderwick —… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | create_human_task | completed | queue=property_manager, title=Case 019 garden works — provider/quote conflict, rent deduc…, summary=Flat 25, 185 Copperfield Walk. Three items a person must se… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 8 | add_note | completed | note=Reviewed closed file. Clearance works evidenced at event-03… | {"id": "ACT-4"} | CAP-LOG |
| 9 | put_on_hold | completed | reason=Waiting for Landlord — completion confirmation (flagged unm…, until=3 working days from the landlord email (ACT-2) | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 019: The record carries red flags that need a human's confirmation (safety_hazard: Waste described as 'a specialised builders material that needs disposing of properly' (quoted, untrusted-origin relay); no asbestos or other hazard is named anywhere in the artefacts and the tenant reported no injury. Garden surface still un-levelled, so the tenant was asked to report anything left unsafe.); the case cannot end as needs_info.
**Facts (≤5):**
- Waste described as 'a specialised builders material that needs disposing of properly' (quoted, untrusted-origin relay); no asbestos or other hazard is named anywhere in the artefacts and the tenant reported no injury. Garden surface still un-levelled, so the tenant was asked to report anything left unsafe.
**Gap:** The record carries red flags that need a human's confirmation (safety_hazard: Waste described as 'a specialised builders material that needs disposing of properly' (quoted, untrusted-origin relay); no asbestos or other hazard is named anywhere in the artefacts and the tenant reported no injury. Garden surface still un-levelled, so the tenant was asked to report anything left unsafe.); the case cannot end as needs_info.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → tenant: Come back with the landlord's decision on levelling and gravelling; no date booked for those items [open]
- agency → landlord: Refer the file to the property manager if no reply within 3 working days [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from the 17 Jan 2025 report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- RTE-LANDLORD [sop]: Landlord reply-by on completion confirmation and remaining scope

## System notes

- reviewer: R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
