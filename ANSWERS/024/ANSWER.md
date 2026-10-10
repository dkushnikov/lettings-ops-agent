# ANSWER — Case 024 — Case 024: Oven repair request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Oven job was closed with no provider result; I reopened it in substance, chased Lantern Works, corrected the tenant, and referred the premature closure to the office.
**Stage:** on_hold · **Hold:** Waiting for Provider — Lantern Works to confirm attendance/appointment and any quote within 2 working days of the chase (ACT-2); tenant also asked to confirm the oven's current state and the fence/conservatory items (ACT-3).
**Last update:** 2026-08-26 01:28:41 UTC (event-032) · **Decided:** 2026-10-10 14:06 UTC
**Next step:** Lantern Works to reply within 2 working days with attendance status, an appointment window and any quote (amount + VAT); if they miss it, the property manager reallocates (ACT-5).

Definition of done (3/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 issue logged; urgency set routine (use_playbook); workaround advice given to tenant at event-003 and water-near-electrics advice at ACT-3
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-010 landlord approved sending an appliance repair contractor in reply to event-008 (attendance only, no amount named)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-011/event-013 Lantern Works instructed; tenant told at event-012
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No appointment anywhere in the history; provider chased for a window (ACT-2)
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote received from Lantern Works; landlord told any priced quote comes to them first (ACT-4)
- [ ] work_result: Work result recorded from the provider — No provider report on file; event-016 'fence and oven have both been fixed' is unsupported by any provider evidence
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-020/event-029 skip reason recorded ('invoices visible on Keystone Solutions') but no work photos or invoice document exists; event-017 'Invoice received' unsupported
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-030 marked completed without payment, but with no verified work result this status is unsafe; referred to office (ACT-5)
- [ ] landlord_confirmation: Landlord confirmed completion — event-021 'Need confirmation from landlord' never answered; landlord re-informed at ACT-4
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued — tenant arranges access directly with the provider (event-013); event-023/025/027 'Keys return confirmed' are system lines with a priority validation error
- [ ] closed: Request closed with a resolution that names who paid — Closure withheld: work result, quote, documents and landlord confirmation outstanding; ticket placed on hold (ACT-6)

## 1. Decision

The oven ticket was marked complete without any evidence of work: Lantern Works was instructed on 5 Aug 2026 (event-011, event-013) and has never reported attendance, a quote, a result or an invoice, yet the tenant was told the oven was fixed (event-016) and the task was completed without payment (event-030). I treated the completion as unverified, kept the ticket open, chased the provider with a 2-working-day deadline (ACT-2), corrected the tenant and asked whether the oven is still faulty plus which property the fence (event-015) and conservatory-roof (event-032) queries relate to (ACT-3), told the landlord no spend has been incurred and that any priced quote comes to them first (ACT-4), recorded the records conflict (ACT-1), referred the premature closure and the two off-ticket items to the office (ACT-5), and placed the case on hold (ACT-6). No spend authorised — the landlord's "yes please" (event-010) approves sending a contractor to look, not a priced repair (RTE-LANDLORD). No liability decided.

Safety actions taken first:
- Checked the report against the emergency definitions: an oven that cooks slowly is an appliance inconvenience — no gas smell, sparks, burning smell, water ingress, loss of heating/hot water or security failure is reported anywhere in the artefacts, so the case stays routine.
- Safety-pass keyword check: the only hazard-adjacent material is the tenant's mention of a leaking conservatory roof (event-032) — not reported at this flat and not described as near electrics; asked the tenant to tell us immediately if water is near lights or sockets and to avoid those electrics, and flagged it to the office (ACT-3, ACT-5).
- No occupant vulnerability is recorded in the case material; no health or family details shared with the contractor (PRO-PII).

Actions deliberately withheld:
- Did not close the request: work result, quote, documents and landlord confirmation are outstanding (CAP-CLOSE).
- Did not dispatch or re-dispatch a contractor at a cost: no standing cap on file and the landlord's approval names no amount (APR-SPEND-OVER-CAP); the existing instruction to Lantern Works stands — no duplicate work order.
- Did not decide who pays or whether the fault is tenant-related (PRO-TENANT-LIABILITY).
- Did not state a repair cost or an appointment date, as no artefact provides one (CAP-NOTIFY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, ESC-CONFLICT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 4 Aug 2026 that the oven does not cook properly — food still uncooked after 1.5 hours. [event-001, get_case_details; high]
- F2: The agency first suggested a settings workaround with a manual (the manual itself is unavailable); the tenant replied the oven has not worked since move-in despite trying the settings and asked for an inspection. [event-003, event-006; high]
- F3: The landlord was asked whether an appliance repair contractor could attend and replied 'Hi, yes please' on 5 Aug 2026 — approval to attend, with no amount named. [event-008, event-010; high]
- F4: Lantern Works was assigned and briefed on 5 Aug 2026 and told to quote and only proceed after the agency's approval; the tenant was told they would make contact. [event-011, event-012, event-013; high]
- F5: No message from the contractor exists on this ticket: no attendance, appointment, quote, work result or invoice document. [search_history; high]
- F6: On 26 Aug 2026 the tenant was told the fence and oven 'have both been fixed'; the request was then marked complete, documents skipped, landlord confirmation left outstanding and the task completed without payment. [event-016, event-019, event-020, event-021, event-029, event-030; high]
- F7: Two tenant messages concern items outside this ticket: a fence repair update (5 Aug) and a leaking conservatory roof (26 Aug); neither is evidenced at Flat 6, a flat. [event-015, event-032; medium]
- F8: No landlord standing spend cap is on file in this case record, so there is no standing authority to spend (default cap £0). [get_case_details, CAP-DISPATCH-ROUTINE; medium]

Conflicts between sources:
- The agency's status records say the oven job is complete and closed without payment, but no provider result, quote, photo or invoice exists; 'Invoice received' (event-017) is unsupported by any document. → Treated the completion as unverified: ticket kept open, provider chased (ACT-2), tenant told the 'fixed' message was sent in error (ACT-3), office asked to rule on reversing the closure (ACT-5). (asked)
- Tenant correspondence on this oven ticket references a fence and a leaking conservatory roof, which do not match the reported fault or obviously the property (a flat). → Asked the tenant which property these relate to and whether separate requests exist; referred to the office for routing (ACT-3, ACT-5). No side taken in messages to parties. (asked)

Red flags:
- [data_quality] Completion, 'invoice received' and 'keys return confirmed' status lines recorded with no underlying evidence, and key-return lines carry a priority validation error; the tenant was told the work was done. → Conflict logged (ACT-1), closure withheld, office task raised (ACT-5), tenant corrected (ACT-3).
- [other] Tenant emails on this ticket describe unrelated items (fence; leaking conservatory roof) — possible cross-ticket or cross-property contamination of the thread. → Asked the tenant to confirm the property and whether separate requests exist; flagged to the office for routing.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "024", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Contractor | [] | allow |
| 4 | search_history | completed | query=quote | [{"event": "event-012", "timestamp": "2026-08-05 03:31:19 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Tenant", "excerpt": "[2026-08-05 03:… | allow |
| 5 | search_history | completed | query=fence conservatory | [] | allow |
| 6 | add_note | completed | note=Record review (no contractor correspondence exists on this… | {"id": "ACT-1"} | CAP-LOG |
| 7 | notify_contractor | completed | message=Lantern Works — chase on the Oven Repair Request at Flat 6,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | notify_tenant | completed | message=Dear Imogen Clarke, regarding the oven at Flat 6, 56 Junipe… | {"id": "ACT-3"} | CAP-NOTIFY |
| 9 | notify_landlord | completed | message=Update on the oven repair at Flat 6, 56 Juniper Mews, North… | {"id": "ACT-4"} | CAP-NOTIFY |
| 10 | create_human_task | completed | queue=property_manager, title=Oven job closed with no provider result — reopen check + tw…, summary=Oven repair, Flat 6, 56 Juniper Mews (reported 4 Aug 2026,… | {"id": "ACT-5"} | CAP-HUMAN-TASK |
| 11 | put_on_hold | completed | reason=Waiting for Provider — Lantern Works to confirm attendance/…, until=2 working days from 2026-08-26 chase | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Lantern Works: have you contacted the tenant and attended Flat 6, 56 Juniper Mews for the oven repair instructed on 5 Aug 2026? If attended, send the work result and photos; if not, send your next appointment window and a quote (amount and VAT) before any chargeable work. (blocking; No provider correspondence exists on the ticket (history search); scope, attendance and quote are the contractor's to settle (RTE-CONTRACTOR).)
- Ask **tenant**: Is the oven still failing to cook properly at Flat 6, 56 Juniper Mews? (blocking; The ticket was closed as fixed (event-016) with no provider result; only the tenant can confirm the current state of the fault (RTE-TENANT).)
- Ask **tenant**: Are the fence query (5 Aug) and the leaking conservatory roof query (26 Aug) about this property, and were they reported as separate requests? If water is coming in near electrics, tell us immediately. (non-blocking; Both items are outside this oven ticket and a flat with a fence/conservatory is ambiguous; a leak near electrics would change urgency (RTE-TENANT, ESC-SAFETY).)

Promises made or recorded:
- agency → contractor: Reply required within 2 working days with attendance status, appointment window and any quote, else the job is referred for reallocation by 2 working days from the chase (ACT-2) [open]
- agency → tenant: Come back as soon as Lantern Works responds; no visit booked without the tenant agreeing a time [open]
- agency → landlord: Any quote (amount and VAT) will be sent for approval before chargeable work starts [open]
- agency → tenant: 'Fence and oven have both been fixed' (26 Aug) — unsupported by any provider evidence [broken]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
