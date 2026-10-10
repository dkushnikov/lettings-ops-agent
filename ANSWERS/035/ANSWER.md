# ANSWER — Case 035 — Case 035: Shower Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Shower repair done by the landlord himself and confirmed by him; held for the tenant's confirmation and a smoke-alarm test before closing.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation the shower is working and that the smoke alarm(s) sound on test; reply chased by 15 Oct 2025, then the office task (ACT-3) carries the detector question to the landlord.
**Last update:** 2025-10-12 23:23:41 UTC (event-013) · **Decided:** 2026-10-10 13:30 UTC
**Next step:** Tenant (Palmer) to confirm the shower is repaired and that the smoke alarm(s) sound on test; if confirmed, the office closes the request as completed without payment (landlord's own work).

Definition of done (5/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 — categorised Plumbing, severity ROUTINE, tenant Q&A taken (bathroom shower, low flow, no pets)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 — landlord is using his own labour and parts; event-013 completed without payment, so no agency spend arises
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-006 — landlord doing the work himself; no contractor instructed by the agency
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-006 — landlord to contact the tenant directly to arrange fitting; access handled by the landlord
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No priced quote: landlord supplied parts and labour (event-006)
- [ ] work_result: Work result recorded from the provider — Landlord reported completion by phone (event-011, event-012); tenant confirmation outstanding (ACT-1)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No contractor photos or invoice exist — landlord's own work (event-006, event-013); shower picture referenced at event-005 is unavailable
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-013 — task completed without payment; no invoice to forward
- [x] landlord_confirmation: Landlord confirmed completion — event-011, event-012 — landlord rang and confirmed he has sorted this
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; access arranged by the landlord with the tenant (event-006)
- [ ] closed: Request closed with a resolution that names who paid — Held open pending tenant confirmation and the smoke-alarm safety question (ACT-1, ACT-3, ACT-4)

## 1. Decision

No contractor instruction and no agency spend: the landlord took the job on himself, supplied the parts and arranged access with the tenant directly (event-006), and confirmed by phone that it is done (event-011, event-012); the ticket was marked completed without payment (event-013). I did not close it as resolved for two reasons: the tenant has never been told the job is finished or confirmed it, and the landlord call summary (event-004) raises a smoke-detector/water-damage item the record does not resolve. I asked the tenant to confirm the shower and to test the alarms (ACT-1), raised an office task for the detector and ceiling item (ACT-3), and put the case on hold pending the tenant's reply (ACT-4).

Actions deliberately withheld:
- Did not instruct a plumber: the landlord is doing the work himself and there is no standing spend cap on file (APR-SPEND-OVER-CAP, event-006).
- Did not close the request: work result unconfirmed by the tenant and the smoke-detector safety item unaddressed (CAP-CLOSE).
- Did not decide who pays for the water damage / ceiling repair mentioned at event-004 (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, RTE-TENANT, RTE-LANDLORD, ESC-SAFETY, CLK-S11, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported low shower pressure and a loose shower hose at the shower head at Flat 23, 63 Meadow Row, Bellmere, ZZ6 6ZZ on 12 Oct 2025. [index, event-001; high]
- F2: Intake classified the issue as Plumbing, severity ROUTINE; tenant confirmed it is the bathroom shower with very low flow and no pets at the property. [event-002; high]
- F3: No emergency definition is met: no leak flow, no water near electrics, no loss of water supply, heating or security reported. [event-001, event-002; medium]
- F4: A system status line required the landlord approval step before instructing anyone. [event-003; high]
- F5: The agency sent the landlord a photo of the shower and told the tenant the landlord would obtain the parts and contact them directly to fit them. [event-005, event-006; high]
- F6: The landlord telephoned and confirmed the work has been done; the request was marked completed without payment. [event-011, event-012, event-013; high]
- F7: The landlord call summary of 12 Oct records discussion of costs for water damage affecting a smoke detector and ceiling repairs, and of completed work including new smoke detectors; it does not say whether a detector at this flat is damaged, replaced or tested. [event-004; medium]
- F8: The tenant's only reply on the ticket was an acknowledgement of the plan; no confirmation of completion has come from the tenant. [event-009; high]
- F9: No landlord standing spend cap is on file in this case record, so there is no standing authority to spend. [get_case_details, get_action_ledger; medium]

Conflicts between sources:
- Ticket marked completed without payment (event-013) while the tenant has had no completion message and the safety-pass detector item at event-004 is unresolved. → Kept the ticket open on hold; asked the tenant the two blocking questions and raised an office task for the detector item rather than confirming closure. (asked)

Red flags:
- [safety_hazard] Call summary refers to water damage affecting a smoke detector and to ceiling repairs at the flat (quoted fragment, untrusted summary); detector status unverified. → Tenant asked to test the alarms (ACT-1); office task raised for the property manager to confirm replacement/testing with the landlord (ACT-3); case not closed as resolved.
- [data_quality] The shower photo referenced in the landlord email is unavailable, so the fault was never assessed from evidence by the agency; completion rests on the landlord's phone call alone. → Tenant confirmation requested before closure (ACT-1).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "035", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=smoke detector water damage ceiling | [] | allow |
| 4 | search_history | completed | query=landlord parts fit shower | [] | allow |
| 5 | notify_tenant | completed | message=Hello, an update on your shower report (low pressure and lo… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | add_note | completed | note=Case review. Repair route: landlord elected to supply parts… | {"id": "ACT-2"} | CAP-LOG |
| 7 | create_human_task | completed | queue=property_manager, title=Smoke detector / ceiling water damage at Flat 23, 63 Meadow…, summary=Raised from Case 035 (shower repair, landlord self-repair,… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 8 | put_on_hold | completed | reason=Waiting for Tenant — confirmation that the landlord's showe…, until=2025-10-15 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 035: The record carries red flags that need a human's confirmation (safety_hazard: Call summary refers to water damage affecting a smoke detector and to ceiling repairs at the flat (quoted fragment, untrusted summary); detector status unverified.); the case cannot end as needs_info.
**Facts (≤5):**
- Call summary refers to water damage affecting a smoke detector and to ceiling repairs at the flat (quoted fragment, untrusted summary); detector status unverified.
**Gap:** The record carries red flags that need a human's confirmation (safety_hazard: Call summary refers to water damage affecting a smoke detector and to ceiling repairs at the flat (quoted fragment, untrusted summary); detector status unverified.); the case cannot end as needs_info.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → tenant: Landlord would get the parts and contact the tenant to arrange fitting [kept]
- agency → tenant: Re-open the job with the landlord if the tenant says the work is not finished [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-GAS-CP12 [in_force]: Gas safety record

## System notes

- reviewer: R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
