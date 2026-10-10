# ANSWER — Case 018 — Kitchen maintenance report

**Disposition:** NEEDS_INFO · **Urgency:** urgent · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Rats in kitchen; landlord is doing the works himself but proofing is undone after 4 weeks — chased landlord for a completion date or written authority to instruct, reply-by 16/09.
**Stage:** on_hold · **Hold:** Waiting for Landlord — Gareth Vale to give the proofing completion date and pest report, or written authority for Northbridge to instruct a pest contractor; reply-by 5pm Tue 16/09/2025 (ACT-1, ACT-3).
**Last update:** 2025-09-11 14:30:00 UTC (event-019) · **Decided:** 2026-10-10 15:42 UTC
**Next step:** Landlord (Gareth Vale) to reply by 5pm Tue 16/09/2025 with the proofing completion date and pest-control report, or written authority for Northbridge to instruct and quote; if no reply, refer to the property manager.

Definition of done (2/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Urgency set to urgent (rats inside the kitchen, event-001); acknowledged event-002; hygiene and escalation advice given to tenant in ACT-2
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Landlord elected to arrange the works with his own contractor (event-006, event-007); no Northbridge spend authorised
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's contractor not named on file; asked in ACT-1. No Northbridge provider may be instructed (no cap on file, APR-SPEND-OVER-CAP)
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Expected proofing visit did not take place (event-017); no slot confirmed
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — Works are at the landlord's own arrangement and cost; no Northbridge quote exists
- [ ] work_result: Work result recorded from the provider — No completion evidence or pest-control report on file (event-011, event-018)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Pest-control report promised to the tenant by the contractor (event-001) never received; requested from the landlord in ACT-1
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No agency-instructed work; landlord pays his own contractor direct
- [ ] landlord_confirmation: Landlord confirmed completion — Confirmation requested 18/08 (event-007) and chased 11/09 (ACT-1); not received
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant reports no access restrictions (event-001)
- [ ] closed: Request closed with a resolution that names who paid — Case on hold Waiting for Landlord (ACT-3)

## 1. Decision

The landlord took the work in hand himself on 18/08/2025 (event-007), so there is no provider for Northbridge to chase and, with no spend cap or standing instruction on file, no authority to instruct one (APR-SPEND-OVER-CAP, default cap £0). Three waiting periods have expired with no landlord update and the tenant reports the proofing still undone (event-010, event-017, event-018). I chased the landlord with a two-option ask and a hard reply-by of 5pm Tue 16/09/2025 (ACT-1), updated the tenant with that time and interim hygiene/safety advice without promising a date (ACT-2), put the case on hold Waiting for Landlord (ACT-3) and recorded the scope gap and safety checks (ACT-4). The case now waits on one named party for a landlord-owned decision (RTE-LANDLORD), so it finishes as request_info rather than an escalation; if 16/09 passes with no reply, the next step is a referral to the property manager.

Safety actions taken first:
- Safety pass: no gas, electrical, water or structural hazard reported or observed; rodent-related electrical risk named as a check — tenant asked to report gnawed cables, burning smell or any bite/illness immediately, which would switch the case to emergency-hazard (ACT-2).
- No occupant vulnerability disclosed (household includes a small dog; no access restrictions) — ESC-VULNERABLE not triggered (event-001).
- No tenant health or household detail shared outside the case record (PRO-PII).

Actions deliberately withheld:
- Did not instruct a pest-control contractor: no landlord spend cap on file (default £0) and no written landlord approval in the history (APR-SPEND-OVER-CAP, CAP-DISPATCH-APPROVED).
- Did not book an access window: no provider and no date exist to offer (CAP-NOTIFY).
- Did not state or imply who pays for the treatment or proofing (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, CLK-S11, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported rats outside and inside the kitchen, including beneath the sink, on 14/08/2025, after four days away; a small dog lives at the property and there are no access restrictions. [event-001, index; high]
- F2: Agency acknowledged the report to the tenant the same day and said landlord approval would be sought before works (14/08/2025). [event-002; high]
- F3: Landlord was asked on 17/08/2025 whether Northbridge should arrange works or he would use his own contractor; he replied asking for a call and gave no written approval. [event-003, event-004; high]
- F4: On 18/08/2025 the agency recorded that the landlord would arrange the works directly and asked him for an expected completion date; no contractor, scope or date was recorded. [event-007, event-006; high]
- F5: Tenant was told on 18/08/2025 that the landlord would arrange works and that he or his contractor might contact them about access. [event-008; high]
- F6: On 01/09/2025 the tenant reported pest-control visits ongoing and the openings beneath the kitchen sink still unsealed. [event-010, event-011; medium]
- F7: On 07/09/2025 the tenant said pest control attended and removed its equipment, and that separate contractors were expected the next day for the wall area; on 08/09/2025 nobody attended. [event-014, event-017; medium]
- F8: Three automated waiting-period expiries were recorded (07/09, 08/09, 11/09) with no landlord update and no evidence the proofing is complete. [event-012, event-015, event-018; high]
- F9: No landlord spend cap, standing instruction, pest-control report, diagnosis, quote or completion evidence is on file; a history search returned no such record. [search_history, event-011, event-016; high]
- F10: Tenant prefers phone contact and offered to report any rearranged appointment. [event-017; high]

Conflicts between sources:
- Scope of the outstanding proofing is inconsistent: openings beneath the kitchen sink (tenant, 01/09) versus contractors working on the wall area (tenant, 07/09); the landlord separately recalls a Dec 2024 record saying filling external openings may not be feasible. → Put to the landlord as part of the 16/09 ask (contractor, scope, completion date, pest report) — ACT-1; not resolvable from the file. (asked)

Red flags:
- [data_quality] Key facts rest only on recollection and untrusted tenant/landlord accounts: no pest-control report, diagnosis, entry route, contractor name or completion evidence is on file, and the landlord's Dec 2024 'may not be feasible' recollection is unverified. → Recorded in ACT-4; documentary evidence requested from the landlord in ACT-1.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "018", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=approval cap contractor instruct | [] | allow |
| 4 | search_history | completed | from_party=Landlord | [{"event": "event-004", "timestamp": "2025-08-17 15:25:13 UTC", "channel": "Email", "from": "Gareth Vale (Landlord)", "to": "Tara Wren (Property Manager, North… | allow |
| 5 | notify_landlord | completed (ledger) | message=Re: 14 Mosswold Crescent, Brindlewick — rat activity in the… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_tenant | completed (ledger) | message=Re: 14 Mosswold Crescent — rats in the kitchen.  Thank you… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — landlord elected to arrange the pest…, until=2025-09-16 17:00 UTC | {"id": "ACT-3"} | CAP-LOG |
| 8 | add_note | completed (ledger) | note=Case state 11/09/2025: landlord-arranged works, no Northbri… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Please confirm by 5pm on Tue 16/09/2025 either (a) the contractor, scope and completion date for the kitchen proofing work you are arranging, with a copy of the pest-control report, or (b) your written authority for Northbridge Lettings to instruct a pest-control contractor to inspect, identify the entry route and quote for proofing (quote to you for approval before work starts). (blocking; Landlord elected to arrange the works himself (event-007); no completion evidence after three expired waits (event-012, event-015, event-018) and no spend authority on file, so Northbridge cannot instruct anyone.)
- Ask **tenant**: Please call us with any further rat sightings, and immediately if you see gnawed cables or pipework, smell burning, or anyone is bitten or unwell. (non-blocking; Keeps the urgency assessment current and would trigger the emergency route (electrical/safety) if the position changes; tenant prefers phone contact (event-017).)

Promises made or recorded:
- agency → landlord: If no reply by 5pm Tue 16/09/2025, the case will be referred to the property manager; no contractor instructed and no cost incurred without his written approval. by 2025-09-16 17:00 [open]
- agency → tenant: We will call the tenant with the next update after the landlord's 16/09/2025 reply-by time. by 2025-09-16 17:00 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
