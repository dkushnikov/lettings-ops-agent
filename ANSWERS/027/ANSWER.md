# ANSWER — Case 027 — Case 027: Blocked Bath Drain Request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Bath drain cleared by tenant himself; ticket closed without payment, no charge raised, and the unrelated parking enquiry passed to the property manager.
**Stage:** closed
**Last update:** 2026-05-14 11:53:19 UTC (event-017) · **Decided:** 2026-10-10 14:07 UTC
**Next step:** Property manager to chase block management on the tenant's parking-space enquiry and reply to the tenant (human task ACT-2); no action outstanding on the repair.

Definition of done (3/4 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Case index (slow-draining bath, 2 days); event-002 gave plunger/drain-cleaner self-help steps; urgency routine — no overflow, smell or hazard reported
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No contractor instructed and no spend arose (event-007, event-017)
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Tenant resolved the fault before any provider was needed (event-007)
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No visit required (event-007)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever sought; no works
- [x] work_result: Work result recorded from the provider — event-007: tenant confirms drain now clear after plunging; corroborated by event-016
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No attendance, no photos or invoice exist; skip reason recorded in ACT-1 and ACT-4
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-017 — task completed without payment; no invoice to forward
- [n/a] landlord_confirmation: Landlord confirmed completion — Landlord was never involved: no cost, no access, no instruction (no landlord event in history)
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; no visit
- [x] closed: Request closed with a resolution that names who paid — ACT-4 — closed, resolution names who paid (nobody; completed without payment)

## 1. Decision

Closed the maintenance request as resolved without payment: the tenant cleared the slow bath drain himself (event-007), no contractor attended and no cost arose, so no landlord authority, quote or invoice step applied. Told the tenant it is closed with no charge (ACT-3). The tenant's separate parking-space enquiry, which caused the reopen, is not a maintenance matter and depends on block management, a third party I cannot contact: handed to the property manager queue with the outstanding promise (ACT-2). Recorded for the office that event-002 asserted tenant liability for a call-out, which is a human decision (PRO-TENANT-LIABILITY); no charge was raised, so nothing to reverse.

Safety actions taken first:
- Safety pass run over all artefacts: no gas, electrical, detector, damp/mould, overflow, sewage or vulnerability indicators present (F6); no hazard red flag raised.
- Tenant reminded to report immediately if water overflows, backs up or a drain smell appears, as that would be treated as urgent (ACT-3).

Actions deliberately withheld:
- Did not confirm or repeat the tenant-liability position in event-002 (PRO-TENANT-LIABILITY).
- Did not dispatch a contractor: the fault is resolved and there is no standing spend authority on file.
- Did not promise the tenant a date for the block management/parking answer (CAP-NOTIFY).

## 2. Authority and evidence

Authority cited: CAP-CLOSE, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, RTE-STAFF
Rules applied by the policy gate: CAP-CLOSE, CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported a bath draining over hours, for about 2 days, at Flat 10, 30 Copperfield Walk, Willowbank, ZZ2 3ZZ on 17/04/2026. [index, get_case_details; high]
- F2: The agency replied on 17/04 with self-help steps (plunger, drain cleaner) and stated that a tenant-caused blockage call-out would be billed to the tenant. [event-002; high]
- F3: On 28/04 the tenant reported the drain is now clear after using a plunger. [event-007; high]
- F4: No contractor was instructed and no spend was incurred; the agency recorded the task as completed without payment on 14/05. [event-009, event-016, event-017; high]
- F5: The ticket was reopened only because a tenant email about registering for a garage parking space arrived on this job id; the agency said block management had been asked and the tenant is awaiting that update. [event-010, event-011, event-012, event-015; high]
- F6: No hazard keyword or condition appears in the material: no overflow, sewage smell, water near electrics, loss of water or heating, and no occupant vulnerability is disclosed. [index, event-002, event-007; high]

Red flags:
- [prohibited_request] Agency template (event-002) decided and communicated tenant liability for a potential call-out ("the full cost ... will be billed to you"); liability is a human decision under PRO-TENANT-LIABILITY. → Recorded in case note ACT-1 and flagged to the property manager queue (ACT-2); no charge was raised, so nothing to reverse. I made no liability statement to the tenant.
- [data_quality] An unrelated enquiry (garage parking space) was filed against the maintenance job id, reopening a closed repair ticket. → Repair closed on its own merits; parking enquiry handed to property manager as a separate matter (ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "027", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=parking block management | [] | allow |
| 4 | search_history | completed | from_party=Landlord | [] | allow |
| 5 | add_note | completed | note=Review of reopened ticket NBL-027-8010 (Flat 10, 30 Copperf… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed | queue=property_manager, title=Open promise to tenant: underground parking space enquiry (…, summary=The maintenance ticket NBL-027-8010 (blocked bath drain) is… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_tenant | completed | message=Job Id: NBL-027-8010 — Flat 10, 30 Copperfield Walk, Willow… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | close_request | completed | resolution=Blocked/slow bath drain at Flat 10, 30 Copperfield Walk res… | {"id": "ACT-4"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Agency → Tenant: Update the tenant on underground parking space availability once block management responds [open]
- Agency → Tenant: Repair request closed with no charge to the tenant; report again if the drain slows or water backs up [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day

## System notes

- reviewer: R2: prohibited_request flag(s) recorded for the reader; not an escalation on their own (urgency routine)
