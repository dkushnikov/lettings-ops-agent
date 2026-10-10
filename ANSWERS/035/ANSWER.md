# ANSWER — Case 035 — Case 035: Shower Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Landlord repaired the shower himself and confirmed completion; held at final checks pending tenant confirmation of the repair and a smoke-alarm test.
**Stage:** on_hold · **Hold:** Waiting for Tenant - tenant to confirm the shower repair is complete and that the smoke alarm nearest the bathroom sounds on test; 3-day wait, then manual-mode review.
**Last update:** 2025-10-12 23:23:41 UTC (event-013) · **Decided:** 2026-10-10 14:09 UTC
**Next step:** Tenant to confirm the shower works and that the smoke alarm sounds on test (asked ACT-1; 3-day clock, then the office reviews before closure).

Definition of done (5/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 (Plumbing, ROUTINE) plus tenant Q&A confirming bathroom shower; no damage-limiting steps applicable to low pressure
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-005/event-006 - landlord elected to supply the parts and carry out the work himself; no agency spend
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-006 - landlord acting as his own provider; tenant told he would make contact
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-006 - landlord arranging access directly with the tenant; no agency booking made
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote: landlord supplied parts and labour at his own cost
- [ ] work_result: Work result recorded from the provider — event-011/event-012 record the landlord's phone confirmation only; tenant confirmation requested at ACT-1
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No contractor photos or invoice exist - landlord did the work himself (event-005, event-012); skip reason recorded at ACT-2
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-013 - task completed without payment; no agency invoice
- [x] landlord_confirmation: Landlord confirmed completion — event-011, event-012 - landlord rang to confirm the work was done
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; landlord attended by arrangement with the tenant
- [ ] closed: Request closed with a resolution that names who paid — Held open pending tenant confirmation of the repair and the smoke-alarm test (ACT-1, ACT-3)

## 1. Decision

The landlord took the job on himself — he obtained the parts and arranged to fit them with the tenant directly (event-005, event-006) — and then telephoned to confirm completion (event-011, event-012); the task was marked completed without payment (event-013). No agency contractor was instructed and no agency spend arose, so no approval under APR-SPEND-OVER-CAP / APR-ALWAYS-ASK was needed. I did not close the request: the landlord's call summary (event-004) refers to water damage affecting a smoke detector and to new smoke detectors, and nothing in the file records that an alarm was tested, and no party has confirmed the shower itself is working. I messaged the tenant asking for both confirmations (ACT-1), noted the position (ACT-2) and put the ticket on hold Waiting for Tenant (ACT-3).

Safety actions taken first:
- Asked the tenant to test the smoke alarm nearest the bathroom and to report immediately if it does not sound or is missing/damaged (ACT-1).
- Recorded the untested-detector question in the case record so it cannot be closed silently (ACT-2).

Actions deliberately withheld:
- Did not close the request: work_result unverified and the smoke-alarm check unresolved (CAP-CLOSE requires the final checks first).
- Did not instruct a contractor: the landlord is doing the work himself and there is no spend authority on file (APR-SPEND-OVER-CAP).
- Did not comment on who pays for any damage discussed in the landlord call (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-CLOSE, RTE-TENANT, CLK-S11, CLK-SOP-ACK, PRO-TENANT-LIABILITY
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported very low shower pressure and a loose hose connection at Flat 23, 63 Meadow Row, Bellmere, ZZ6 6ZZ on 2025-10-12. [index, event-001; high]
- F2: Intake classified the issue as Plumbing, severity ROUTINE, medium confidence; tenant confirmed it is the bathroom shower and 'the flow is very less'; no pets. [event-002; high]
- F3: No emergency definition is met: water supply is present, no leak, flood, water near electrics, no loss of heating or security. [event-001, event-002; high]
- F4: Agency sent the landlord a photo of the shower and told the tenant the landlord would obtain the parts and contact the tenant directly to fit them. [event-005, event-006; high]
- F5: Landlord telephoned and confirmed he had sorted the work; the task was recorded as completed without payment. [event-011, event-012, event-013; medium]
- F6: The landlord call summary refers to water damage affecting a smoke detector and ceiling repairs, and to new smoke detectors having been fitted; no test result for any alarm is recorded in the file. [event-004; medium]
- F7: No landlord standing spend cap or standing instruction is on file in this case record; no agency contractor was instructed and no agency spend arose. [get_action_ledger, event-003; medium]
- F8: Tenant replied 'That's great, thank you' to the arrangement that the landlord would supply and fit the parts. [event-009; high]

Red flags:
- [data_quality] Completion rests on two internal one-line notes of a landlord phone call ('ll rang and confirmed this is all done'); no tenant verification and no document evidence of the repair. → Asked the tenant to confirm; ticket held open rather than closed (ACT-1, ACT-3).
- [other] Safety pass keyword check: the landlord call summary mentions water damage affecting a smoke detector and new smoke detectors, with no test recorded. No hazard is reported or observed, so this is logged as an open check, not a hazard. → Tenant asked to test the alarm nearest the bathroom and report the result (ACT-1); check recorded at ACT-2.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "035", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=smoke detector water damage ceiling | [] | allow |
| 4 | search_history | completed | query=landlord parts fit arrange | [] | allow |
| 5 | notify_tenant | completed | message=Hello, an update on your shower report at Flat 23, 63 Meado… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | add_note | completed | note=Case review. Repair route: landlord elected to supply parts… | {"id": "ACT-2"} | CAP-LOG |
| 7 | put_on_hold | completed | reason=Waiting for Tenant - confirmation that the landlord's showe…, until=3 days from today | {"id": "ACT-3"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Has the landlord carried out the shower work, and are the water pressure and hose connection now normal? (blocking; Only the tenant can confirm the repair at the fixture; the landlord's phone confirmation (event-011, event-012) is second-hand and the request cannot be closed without a work result verified at the property.)
- Ask **tenant**: Please press the test button on the smoke alarm nearest the bathroom/hallway - does it sound? Is any alarm missing or damaged? (blocking; event-004 records water damage affecting a smoke detector at the flat; no test result exists in the file. Safety pass item that must be resolved before the ticket can be called resolved.)

Promises made or recorded:
- agency → tenant: Landlord will obtain the parts and contact the tenant to arrange fitting [kept]
- agency → tenant: Re-open the job if the shower is still not right, and treat a failed or missing smoke alarm as a priority [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
