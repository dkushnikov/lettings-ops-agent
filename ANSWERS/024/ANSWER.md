# ANSWER — Case 024 — Case 024: Oven repair request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Oven repair closed as "fixed" with no provider evidence; chased Lantern Works, asked tenant if oven works, flagged unevidenced closure to office, ticket on hold.
**Stage:** on_hold · **Hold:** Waiting for Provider — Lantern Works to confirm attendance/quote or offer a slot by 28 Aug 2026 (ACT-1); secondary wait on Tenant to confirm current oven status (ACT-2).
**Last update:** 2026-08-26 01:28:41 UTC (event-032) · **Decided:** 2026-10-10 13:26 UTC
**Next step:** Lantern Works to confirm by 28 Aug 2026 whether they attended and what was done, or offer an appointment window (chased ACT-1); office task ACT-3 to decide on reopening and the invoice query.

Definition of done (3/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-006 fault described; urgency set routine (use_playbook); settings workaround relayed at event-003.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-010 — landlord approved instructing an appliance repair contractor in reply to event-008.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-011, event-013 (Lantern Works briefed), event-012 (tenant told who is coming).
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No contractor contact or slot anywhere in the history (search_history); chased ACT-1, tenant asked ACT-2.
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote ever received; event-013 required one before work. RTE-LANDLORD applies once an amount exists.
- [ ] work_result: Work result recorded from the provider — event-016 claims the oven was fixed but no provider report exists (search_history); claim unverified.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-020 skip reason given ('invoices visible in the portal'), but no photos or work evidence exist to support the claimed completion.
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-017 'Invoice received' vs event-030 'completed without payment'; landlord told to hold any invoice (ACT-5).
- [ ] landlord_confirmation: Landlord confirmed completion — event-021 records confirmation still needed; none received.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued — no visit took place on the evidence; event-023/025/027 'keys return confirmed' entries carry a validation error and are not reliable.
- [ ] closed: Request closed with a resolution that names who paid — event-030 closed the task without payment, but the checklist above is unmet and no resolution names who paid; reopening referred to the office (ACT-3).

## 1. Decision

Reopened in substance: the ticket's closure is not supported by evidence. The oven was reported faulty on 4 Aug 2026 (event-001) and confirmed still faulty by the tenant on 5 Aug (event-006); the landlord approved instructing an appliance repair contractor (event-010) and Lantern Works were briefed (event-013). No contractor communication, visit, quote or work result exists in the history (search_history, from_party=Contractor: nil), yet the tenant was told on 26 Aug that the oven "and fence" were fixed (event-016) and the task was closed without payment (event-030) with landlord confirmation still outstanding (event-021). I did not raise a second work order (duplicate risk against event-013). I chased the instructed provider with a reply-by date, asked the tenant whether the oven now works and which property the fence / conservatory items belong to, told the landlord to hold any invoice for this job pending evidence of work, put the ticket on hold, and raised a human task for the office on the unevidenced closure and possible invoice for unperformed work. Case now waits on the provider and the tenant.

Safety actions taken first:
- Checked the report against the emergency definitions: an electric oven cooking slowly, with no burning smell, sparks, shock risk, gas smell, or loss of heating/hot water/water/security reported — routine, no make-safe step required.
- No occupant vulnerability disclosed anywhere in the artefacts; no health or family details passed to the contractor (PRO-PII).

Actions deliberately withheld:
- Did not raise a second work order — the existing instruction to Lantern Works stands (event-013) and a duplicate would risk two charges.
- Did not close the request: the definition-of-done items above are unmet and no artefact evidences the repair.
- Did not accept the 'both fixed' message to the tenant as a work result, nor repeat it to the landlord.
- Did not decide who pays or whether any invoice is payable (PRO-TENANT-LIABILITY, PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, ESC-CONFLICT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-PII, APR-SPEND-OVER-CAP
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the oven barely heating — food uncooked after 1.5 hours — at Flat 6, 56 Juniper Mews on 4 Aug 2026. [index, event-001; high]
- F2: The agency first suggested a settings workaround with a manual (the attachment is unavailable); the tenant replied that the oven has not worked since move-in despite trying the suggested settings and asked for an inspection. [event-003, event-006; high]
- F3: The landlord was asked to approve sending an appliance repair contractor and replied 'Hi, yes please' on 5 Aug 2026 — authority to instruct, with no amount named and no standing spend cap on file. [event-008, event-010; high]
- F4: Lantern Works were assigned and briefed on 5 Aug 2026 and told to quote first and only proceed after the agency's approval; the tenant was told they would make contact. [event-011, event-012, event-013; high]
- F5: No message from the contractor appears anywhere in the visible history: no tenant contact, no visit, no quote, no completion report. [search_history; high]
- F6: On 26 Aug 2026 the tenant was told the 'fence and oven have both been fixed'; 'Invoice received' was logged, documents were skipped, landlord confirmation was recorded as still needed, and the task was completed without payment. [event-016, event-017, event-020, event-021, event-030; high]
- F7: Tenant correspondence on this ticket references a fence repair and a leaking conservatory roof, neither of which matches this ticket's subject or a flat. [event-015, event-032; medium]
- F8: No quote amount, invoice value or payer has ever been stated on this ticket. [search_history; high]

Conflicts between sources:
- The agency's own records disagree about whether the oven was repaired: event-016 states the oven was fixed and event-030 closes the task, but no provider attendance, quote or work result exists (F5). → Not resolved in a message to any party; conflict recorded and referred to the office (ACT-3) while the provider is chased (ACT-1) and the tenant asked for the current state (ACT-2). (asked)
- 'Invoice received' (event-017) against 'Task completed without payment' (event-030) for a job with no evidence of work. → Landlord told to hold any invoice for this job pending evidence of work (ACT-5); office asked to verify (ACT-3). (asked)

Red flags:
- [data_quality] Ticket closed and the tenant told the work was done with no provider evidence of any kind; keys-return entries repeated three times with a 'Priority cannot be decreased' validation error, suggesting the workflow was force-advanced manually. → Closure not accepted; human task raised to the office (ACT-3) and ticket placed on hold (ACT-6).
- [data_quality] Tenant emails on this ticket concern a fence and a leaking conservatory roof — subjects that do not match an oven repair at a flat; likely misrouted or cross-contaminated correspondence. → Tenant asked to confirm the address and issue so they can be logged separately (ACT-2); office asked to identify the correct ticket (ACT-3).
- [fraud] Possible billing irregularity: an invoice was recorded for a job with no recorded attendance or work result. Not alleged against any named party — flagged for verification only. → Landlord advised to hold any invoice pending evidence of work (ACT-5); office asked to verify (ACT-3). No payment action taken (PRO-PAYMENTS).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "024", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Contractor | [] | allow |
| 4 | search_history | completed | query=quote | [{"event": "event-012", "timestamp": "2026-08-05 03:31:19 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Tenant", "excerpt": "[2026-08-05 03:… | allow |
| 5 | notify_contractor | completed | message=Lantern Works — re: Oven Repair Request, Flat 6, 56 Juniper… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_tenant | completed | message=Dear Imogen Clarke,  Re: oven not heating properly, Flat 6,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | create_human_task | completed | queue=property_manager, title=Oven job closed as "fixed" with no provider evidence — Flat…, summary=Conflict between agency records; office decision needed. -… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 8 | add_note | completed | note=Case 024 review: closure at event-016/event-030 is not supp… | {"id": "ACT-4"} | CAP-LOG |
| 9 | notify_landlord | completed | message=Re: Flat 6, 56 Juniper Mews — oven repair (your approval to… | {"id": "ACT-5"} | CAP-NOTIFY |
| 10 | put_on_hold | completed | reason=Waiting for Provider — Lantern Works to confirm attendance/…, until=2026-08-28 | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 024: The record carries red flags that need a human's confirmation (fraud: Possible billing irregularity: an invoice was recorded for a job with no recorded attendance or work result. Not alleged against any named party — flagged for verification only.); the case cannot end as needs_info.
**Facts (≤5):**
- Possible billing irregularity: an invoice was recorded for a job with no recorded attendance or work result. Not alleged against any named party — flagged for verification only.
**Gap:** The record carries red flags that need a human's confirmation (fraud: Possible billing irregularity: an invoice was recorded for a job with no recorded attendance or work result. Not alleged against any named party — flagged for verification only.); the case cannot end as needs_info.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → contractor: If no reply by 28 Aug 2026 the job is referred back to the office for reallocation. by 2026-08-28 [open]
- agency → tenant: Checking the completion claim; no visit will be booked without the tenant agreeing a time; Lantern Works asked to respond by 28 Aug 2026. by 2026-08-28 [open]
- agency → landlord: A priced quote will be put to the landlord for approval before any repair work starts. [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day

## System notes

- reviewer: R2: red flags (fraud) → escalated (checked before any needs_info rule)
