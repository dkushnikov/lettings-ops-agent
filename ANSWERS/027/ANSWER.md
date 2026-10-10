# ANSWER — Case 027 — Case 027: Blocked Bath Drain Request

**Disposition:** RESOLVED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Bath drain cleared by the tenant with a plunger; no contractor, no cost — request closed without payment, parking enquiry passed to the office.
**Stage:** closed
**Last update:** 2026-05-14 11:53:19 UTC (event-017) · **Decided:** 2026-10-10 13:26 UTC
**Next step:** Property manager to chase block management on the tenant's underground parking space enquiry and revert to the tenant (human task ACT-3); no action outstanding on the repair.

Definition of done (3/4 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Case record (slow-draining bath, 2 days, no hazard); damage-limiting advice (plunger/drain cleaner) given at event-002
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No spend arose — tenant cleared the blockage himself (event-007); no contractor instructed (event-009)
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-009 'No contractor required'; tenant resolved the fault (event-007)
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No visit needed — no provider instructed (event-009)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever raised (event-016, event-017)
- [x] work_result: Work result recorded from the provider — Result reported by the tenant: plunger cleared the drain (event-007); recorded by the agency at event-016
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No contractor attendance, so no photos or invoice exist; skip reason logged at ACT-1
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Request marked completed without payment (event-017); no invoice to forward
- [n/a] landlord_confirmation: Landlord confirmed completion — Landlord was never involved: no instruction, spend or access on the landlord's account anywhere in the visible history
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued — no visit took place
- [x] closed: Request closed with a resolution that names who paid — ACT-4: closed with a resolution naming that nobody paid (completed without payment)

## 1. Decision

Closed the repair: the reported fault was resolved by the tenant with no contractor and no spend, so no landlord authority, quote, provider or invoice step applied. Confirmed closure and the absence of any charge to the tenant, and handed the one outstanding non-maintenance promise (underground parking enquiry) to the property manager's queue.

Safety actions taken first:
- Checked the report and all later artefacts against the emergency definitions and the safety-pass keyword list: no gas, electrical, damp/mould, detector, vulnerability or injury content appears anywhere in this case, so no make-safe step or welfare escalation was triggered.

Actions deliberately withheld:
- Did not instruct a plumber: the fault is resolved (event-007) and there is no landlord approval or standing cap on file (APR-SPEND-OVER-CAP).
- Did not confirm or deny that the tenant is liable for drain blockages (PRO-TENANT-LIABILITY).
- Did not answer the parking-space question substantively: no block management reply exists and it is outside the maintenance mandate.

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-HUMAN-TASK, CAP-CLOSE, PRO-TENANT-LIABILITY, APR-SPEND-OVER-CAP, CLK-S11, CLK-SOP-ACK, RTE-STAFF
Rules applied by the policy gate: CAP-CLOSE, CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported a bath/shower draining slowly over about 2 days at Flat 10, 30 Copperfield Walk, Willowbank, ZZ2 3ZZ on 17/04/2026. [index, get_case_details; high]
- F2: No hazard keyword or emergency condition appears in the report or any later artefact (no gas, electrics, water ingress, heating loss, insecurity or loss of water supply), so the case is routine. [index, event-002, event-007; high]
- F3: The agency advised self-help (drain cleaner and plunger) and stated that a tenant-caused blockage would be billed to the tenant, offering to instruct a contractor on that basis. [event-002; high]
- F4: Tenant confirmed on 28/04/2026 that a plunger cleared the blockage: quoted fragment 'its now clear'. [event-007; high]
- F5: No contractor was instructed and the job was recorded as completed without payment. [event-009, event-016, event-017; high]
- F6: A separate tenant enquiry about renting an underground parking space was raised on 09/05/2026; the agency said it had contacted block management and would update the tenant, and the tenant acknowledged on 14/05/2026. No reply from block management is visible. [event-011, event-012, event-015; high]
- F7: No landlord spend cap or standing instruction for this property is available in this environment (no landlord-instruction record or tool returned one). [search_history; medium]

Conflicts between sources:
- The ticket was marked resolved/closed (event-009, event-010) while a later tenant email on the same ticket (event-011, parking enquiry) remained unanswered in substance, and two 'Northbridge Lettings to close' holds (event-013, event-014) sit against an unfinished enquiry. → Repair closed on its own merits (ACT-4); the unrelated parking enquiry separated out and handed to the property manager's queue (ACT-3) so the open promise is not lost in the closure. (tool_check)

Red flags:
- [other] event-002 asserts to the tenant, before any inspection, that internal-drain blockages are the tenant's responsibility and that call-out costs 'will be billed to you'. Liability is not an agent decision (PRO-TENANT-LIABILITY). No cost arose, so no liability determination was needed; I neither repeated nor endorsed the statement, and the file notes it. → Recorded in the case note (ACT-1) and flagged to the property manager in the handover task (ACT-3); tenant told explicitly there is no charge for this report (ACT-2).
- [data_quality] event-011 is written in third person ('The customer is inquiring about...') and concerns parking, not the drain — an unrelated topic appended to a closed maintenance ticket. event-015 names an individual ('Noah') from a message body; not copied into other parties' correspondence. → Treated as a separate enquiry and routed to the office queue rather than worked as maintenance; name not reused in outbound messages.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "027", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=parking garage block management | [] | allow |
| 4 | search_history | completed | query=landlord approval cap contractor | [] | allow |
| 5 | add_note | completed | note=Drain thread: tenant reported slow-draining bath 17/04 (cas… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_tenant | completed | message=Job NBL-027-8010 — Flat 10, 30 Copperfield Walk, Willowbank… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | create_human_task | completed | queue=property_manager, title=Flat 10, 30 Copperfield Walk — open promise: underground pa…, summary=The maintenance element of job NBL-027-8010 is finished: te… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 8 | close_request | completed | resolution=Blocked bath drain at Flat 10, 30 Copperfield Walk cleared… | {"id": "ACT-4"} | CAP-CLOSE |

## 4. Human handover / information requested

No human action needed.

Promises made or recorded:
- Agency → Tenant: Update the tenant once block management replies about an available underground parking space [open]
- Agency → Tenant: Close the maintenance request with no charge to the tenant, and reopen/look again if the bath drains slowly again [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
