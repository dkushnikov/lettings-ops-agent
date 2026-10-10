# ANSWER — Case 038 — Case 038: Washing Machine Replacement Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Tenant-supplied washing machine replacement approved by landlord (event-009); no spend instructed, address conflict sent to the office, ticket on hold for completion confirmation.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation that the old machine is removed and his own machine installed (and landlord's confirmation of the inventory change); 3-day wait to 2025-07-31, then chase (ACT-5).
**Last update:** 2025-07-28 08:08:18 UTC (event-013) · **Decided:** 2026-10-10 13:31 UTC
**Next step:** Tenant (Ruben) to confirm the old machine is out and his own machine installed; landlord to confirm the inventory change — then update inventory and close as completed without payment.

Definition of done (3/7 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (Appliances/Power failure, ROUTINE, containment step given); extended with electrical-safety advice at ACT-3
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 landlord 'Yes this is fine' replying to event-005; no agency spend instructed (event-013)
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Tenant supplies and installs his own machine; old machine removed by tenant's family (event-010, event-011) — no provider required
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No agency or contractor visit needed (event-010)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote: no agency-instructed work; landlord pre-agreed only a possible removal charge of c.£24.37-30 (event-005, event-009) which is not expected to arise
- [ ] work_result: Work result recorded from the provider — Tenant asked to confirm old machine removed and replacement installed (ACT-3); no confirmation yet
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No invoice or photos expected as the agency instructed no work; skip reason to be recorded once the tenant confirms the swap (ACT-3)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-013 task marked completed without payment — no agency-instructed cost to forward
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord asked to confirm the inventory change / that he does not wish to own a replacement (ACT-4)
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant in occupation and no contractor access (event-002)
- [ ] closed: Request closed with a resolution that names who paid — Held at ACT-5 pending tenant and landlord confirmations; resolution will name that no party was charged by the agency

## 1. Decision

No contractor or spend is needed: the tenant is replacing the washing machine with his own and the landlord approved that arrangement in his own email (event-009, answering the agency email that named Flat 9 — event-005). I relayed the confirmed arrangement to the tenant with damage-limiting/safety advice about the property's electrics, asked the landlord to confirm the inventory change, flagged to the office the conflict between the call note naming a different property (event-004) and the ticket/email address (event-005), and placed the ticket on hold. The request is not closed because the swap has not been confirmed done: I need the tenant's confirmation that the old machine is out and his machine is installed, and the landlord's confirmation of the inventory change. I did not decide liability or ownership (PRO-TENANT-LIABILITY); event-012's "tenants liability" wording is recorded as an agreement between the parties, not an agency decision.

Safety actions taken first:
- Told the tenant that if the socket or plug is scorched or smells burnt, if the fuse board/RCD trips, or if there are sparks, he must stop using the socket and report it immediately, as the property's electrics are the landlord's responsibility (ACT-3) — the reported 'power failure' is attributed to the appliance only, with no property electrical symptom in any artefact (event-001, event-002).
- Advised the tenant to use a competent installer for any plumbing or electrical connection of the new machine (ACT-3).

Actions deliberately withheld:
- Did not dispatch a contractor: no trade or spend is required — the tenant supplies and installs his own machine and his family removes the old one (event-010); any removal spend would need the landlord's priced approval (APR-SPEND-OVER-CAP).
- Did not close the request: the replacement is not verifiably done and the inventory change is unconfirmed, so closing would leave work_result, documents and landlord_confirmation pending (CAP-CLOSE).
- Did not adopt or communicate the 'tenants liability' wording of event-012 (PRO-TENANT-LIABILITY).
- Did not ask the landlord or tenant to resolve the Flat 18 / Flat 9 record discrepancy; sent it to the office instead (ACT-2).
- Did not lower the numeric priority from 8 (event-008).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, APR-SPEND-OVER-CAP, CAP-CLOSE
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property on the ticket is Flat 9, 59 Alder Lane, Eastmere, ZZ4 4ZZ; tenant reported the LG washing machine dead ('power failure', 'can't be fixed') on 26/07/2025 and offered to replace it with his own, to remain his property. [index, event-001; high]
- F2: Intake classified the issue Appliances / Power failure, severity ROUTINE, confidence high; containment step given was to photograph the machine and any error codes. No access constraints, no pets. [event-002; high]
- F3: No emergency definition is met: an inoperative washing machine is not heating, hot water, water ingress, gas, security or an electrical hazard; no hazard symptom is reported anywhere in the artefacts. [event-001, event-002; high]
- F4: The agency emailed the landlord on 27/07 naming Flat 9, 59 Alder Lane, asking approval for the tenant to replace the machine with her own and for the landlord to cover any removal charge of about £24.37-30. [event-005; high]
- F5: Landlord Henry Ingram replied 'Yes this is fine' on 27/07 14:27 — his own approval of the arrangement described in event-005. [event-009; high]
- F6: On 28/07 the tenant was told the landlord agreed and said his brother will take the old machine to the tip, so no removal contractor or charge is expected. [event-010, event-011; high]
- F7: No contractor has been instructed and no money has been committed by the agency on this ticket; the system marked the task completed without payment on 28/07. [event-013; high]
- F8: No landlord standing spend cap is on file in this case record; authority for this case rests on the landlord's own approval event rather than a cap. [get_case_details; medium]
- F9: System validation note records that priority could not be decreased to 5 from the current 8; priority left unchanged. [event-008; high]

Conflicts between sources:
- The call note of 27/07 06:59 records the approval call to the landlord as concerning 'Flat 18, 128 Meadow Row, Cedarford, ZZ5 9ZZ', while the ticket, the email sent two minutes later and the tenant correspondence all name Flat 9, 59 Alder Lane, Eastmere. → Treated the landlord's approval (event-009) as given for Flat 9, because it replies to the email that names Flat 9 (event-005). Did not raise the discrepancy with the landlord or tenant; sent it to the office as a human task (ACT-2) to correct the record and confirm no separate job exists at the Cedarford address. (asked)
- The 28/07 call has the agency caller introducing herself as 'Eliza at Riverside Solutions'; the agency of record is Northbridge Lettings. → Recorded as a data-quality point in the office task (ACT-2); does not change the action. (unresolved)
- Internal note states the tenant replaces the machine 'under tenants liability'; deciding tenant liability is not an agency-agent decision. → Treated as a record of what the tenant offered (event-001) and the landlord accepted (event-009), not as a liability determination by me (PRO-TENANT-LIABILITY). (source_hierarchy)

Red flags:
- [data_quality] Two agency records name different properties for the same approval conversation (Flat 18, Meadow Row, Cedarford in event-004 vs Flat 9, Alder Lane in event-005), and the agency caller is named as a different firm in event-010. → Human task raised to the property manager queue (ACT-2); approval treated as applying to the ticket address only, no party asked to arbitrate.
- [other] Internal note and system status closed the task as 'completed without payment' and recorded 'tenants liability' before the replacement was confirmed done and before the inventory was updated. → Ticket kept open on hold pending tenant confirmation; liability wording not adopted as an agency decision.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "038", "attachments_hidden": 0} | allow |
| 2 | add_note | completed | note=Case review. Facts: appliance (LG washing machine) at Flat… | {"id": "ACT-1"} | CAP-LOG |
| 3 | create_human_task | completed | queue=property_manager, title=Case 038 — agency records name two different properties for…, summary=Ticket property is Flat 9, 59 Alder Lane, Eastmere ZZ4 4ZZ… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 4 | notify_tenant | completed | message=Dear Ruben, about the broken washing machine at Flat 9, 59… | {"id": "ACT-3"} | CAP-NOTIFY |
| 5 | notify_landlord | completed | message=Dear Mr Ingram, thank you for your approval regarding the w… | {"id": "ACT-4"} | CAP-NOTIFY |
| 6 | put_on_hold | completed | reason=Waiting for Tenant — tenant to confirm the old machine has…, until=2025-07-31 (3-day wait; chase tenant and landlord if no rep… | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Please confirm once the old LG washing machine has been taken away and your own machine is installed, so we can update the inventory and close the request; and tell us if any removal charge arises after all. (blocking; work_result and documents cannot be recorded until the swap is confirmed; landlord agreed to cover a removal charge if one arises (event-005, event-009).)
- Ask **landlord**: Please confirm you are content for the inventory to be updated to show no landlord-owned washing machine at Flat 9, 59 Alder Lane, with the tenant's own machine leaving with him at the end of the tenancy; or tell us if you would prefer to own a replacement, in which case we will obtain quotes for your approval. (non-blocking; RTE-LANDLORD: inventory/fixtures change and any landlord-funded replacement are the landlord's decision.)

Promises made or recorded:
- agency → tenant: Come back to the tenant once the landlord replied [kept]
- agency → tenant: Confirmed the landlord agrees to the tenant-owned replacement and to cover a removal charge if one arises; will update the inventory and close once the swap is confirmed [open]
- agency → landlord: Will update the inventory to show no landlord-owned washing machine and obtain quotes for approval if he prefers to own a replacement [open]
- tenant → agency: Tenant's brother to take the old machine to the tip [open]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day deadline 2025-07-28
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [sop]: 3-day wait for tenant/landlord reply before manual chase deadline 2025-07-31
