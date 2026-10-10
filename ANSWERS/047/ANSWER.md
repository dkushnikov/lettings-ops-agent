# ANSWER — Case 047 — Case 047: Bedroom Window Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Window repair reportedly done by the landlord's own contractor but unverified; stood down the agency provider, asked tenant and landlord to confirm, referred record conflicts to the office.
**Stage:** on_hold · **Hold:** Waiting for Tenant — tenant to confirm the bedroom window is repaired and now closes and locks; landlord to confirm their contractor's completion and any invoice. 3-day reply window from today.
**Last update:** 2024-06-11 19:30:18 UTC (event-036) · **Decided:** 2026-10-10 14:14 UTC
**Next step:** Tenant (Eliza Jenkins) to confirm the bedroom window has been repaired and now closes and locks (asked ACT-1, 3-day clock); landlord confirmation requested in parallel (ACT-2).

Definition of done (2/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-015 issue categorised as window repair; urgency set routine this session (use_playbook, ACT-5); no damage-limiting steps applicable to a window that will not close beyond the security…
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Landlord asked on 22 Feb (event-004, event-011) and never answered on the window; his only reply named a different property (event-010). Re-asked ACT-2. No spend cap on file (F8).
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-016, event-018 (Oscar Turner instructed); tenant told who was coming (event-017). Provider now stood down pending office review (ACT-3).
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot was ever confirmed: three chases unanswered (event-020, event-022, event-024, event-026). No tenant consent to any window exists, so schedule_access was not used.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever received from any provider; no amount is on file (event-026).
- [ ] work_result: Work result recorded from the provider — Only an unsourced system note claims completion (event-035); no provider report. Confirmation requested from tenant and landlord (ACT-1, ACT-2).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice on file; no skip reason recorded by the agency (event-036 states only 'completed without payment').
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Request marked completed without payment (event-036); no agency-side invoice exists. Landlord asked whether any invoice follows from his own contractor (ACT-2).
- [ ] landlord_confirmation: Landlord confirmed completion — event-035 is a system note, not a landlord message; confirmation requested (ACT-2).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued; no visit was ever confirmed (event-020 to event-026).
- [ ] closed: Request closed with a resolution that names who paid — Not closed: work result, documents and landlord confirmation outstanding; ticket placed on hold (ACT-6).

## 1. Decision

Did not close the request. The only evidence of completion is an unsourced system note (event-035) and a "completed without payment" flag (event-036); no provider report, photo, invoice or landlord message supports it, and the agency's own instructed provider (Oscar Turner, event-018) never confirmed anything after three chases (event-020, event-022, event-024, event-026). Within my mandate I: asked the tenant to confirm the window is repaired and now closes and locks (ACT-1); asked the landlord to confirm their own contractor completed the Flat 24 window works and whether an invoice follows (ACT-2); stood Oscar Turner down to prevent a duplicate visit or charge (ACT-3); referred the three record conflicts (property named by the landlord, "Dawson" vs Oscar Turner, unverified completion) to the office rather than picking a side with any party (ACT-4); recorded the safety check and the absence of a spend cap (ACT-5); and placed the ticket on hold (ACT-6). No spend was authorised: no landlord standing cap is on file and the landlord never approved window works (APR-SPEND-OVER-CAP).

Safety actions taken first:
- Checked the file against the safety keyword list: no gas, electrical, water, heating, damp/mould, detector or vulnerability content present (F9).
- Asked the tenant explicitly whether the bedroom window now closes and locks securely, so that a still-insecure window is re-triaged as a security emergency rather than closed as routine (ACT-1, ACT-5).

Actions deliberately withheld:
- Did not close the request: completion is unverified and the playbook's final checks (work result, documents, landlord confirmation) are not satisfied (CAP-CLOSE).
- Did not instruct or re-instruct any contractor at agency cost: no landlord spend cap is on file and no landlord approval of window works exists (APR-SPEND-OVER-CAP).
- Did not tell any party which property or which contractor is the correct one; the conflict went to the office instead (ESC-CONFLICT routing to RTE-STAFF via create_human_task).
- Did not state or imply who pays for the repair (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, ESC-CONFLICT, RTE-TENANT, RTE-LANDLORD, RTE-CONTRACTOR, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Eliza Jenkins reported on 21 Feb 2024 that the bedroom window at Flat 24, 150 Copperfield Walk, Kingshaven, ZZ3 7ZZ is not closing properly. [index, event-001, event-017; high]
- F2: The toilet element of the original report was withdrawn by the tenant on 22 Feb: the tenant said her mother fixed it and only the window needs attention. [event-006, event-011; high]
- F3: The agency asked the landlord on 22 Feb whether to send its own contractor or the landlord's; the landlord's only reply named a plumber for Flat 18, 88 Alder Lane, Willowbank, ZZ3 5ZZ, a different property, and never answered on the window. [event-004, event-010, event-011; high]
- F4: On 1 Mar the agency assigned maintenance provider Oscar Turner and briefed tenant and provider; the brief states the provider should only proceed after agency approval if a quote is required. [event-016, event-017, event-018; high]
- F5: Three reminders were sent to the provider (4, 6, 8 Mar) with no reply; on 10 Mar the system flagged 3+ reminders with no response. [event-020, event-022, event-024, event-026; high]
- F6: Every hold note from 11 Mar to 30 May records 'Held awaiting update from Dawson', a name that appears nowhere else on the file; the holds switch from 'Waiting for Provider' to 'Waiting for Landlord' without any new message. [event-027, event-028, event-029, event-030, event-031, event-032, event-033, event-034; high]
- F7: On 11 Jun a system note states the landlord's contractor confirmed the job complete, and the task was marked completed without payment; no provider report, photo, invoice or landlord message supports this. [event-035, event-036; medium]
- F8: No landlord standing spend cap or instruction document is on file in this case, so there is no standing authority to spend and no landlord approval of window works exists. [get_case_details, event-010; high]
- F9: No gas, electrical, water, heating, damp/mould or occupant-vulnerability content appears anywhere in the file; the tenant did not report the property as insecure. [event-001, event-006; high]
- F10: The tenant was acknowledged within one working day of the report (22 Feb) and updated again on 22 Feb and 1 Mar. [event-003, event-013, event-017; high]

Conflicts between sources:
- The ticket property is Flat 24, 150 Copperfield Walk, Kingshaven; the landlord's only reply (event-010) names Flat 18, 88 Alder Lane, Willowbank and a plumber. The reply explicitly names a different property, so it cannot be read as an instruction for this job. → Not decided with any party. Conflict referred to the office (ACT-4) and the landlord asked to confirm the Flat 24 window works (ACT-2); the agency's own record of the address was kept for all outgoing messages. (asked)
- Who held the job: the agency assigned Oscar Turner (event-016/018) while eight hold notes record 'awaiting update from Dawson' (event-027 to event-034). → Referred to the office (ACT-4); meanwhile the contractor named on the agency's own work order was contacted to confirm attendance and stood down (ACT-3). (asked)
- Completion status: a system note says the landlord's contractor completed the job and the task was closed without payment (event-035, event-036), but the agency's instructed provider never confirmed any booking or visit and there is no work result from any provider. → Treated as unverified; the request was not closed and confirmation was sought from the tenant and the landlord. (asked)

Red flags:
- [data_quality] Completion recorded with no supporting provider report, photo, invoice or landlord message, following eight identical hold notes naming a person ('Dawson') who appears nowhere else on the file; the agency's instructed provider was never stood down and could still attend or charge. → Request left open, provider stood down (ACT-3), confirmations requested from tenant and landlord (ACT-1, ACT-2), office task raised (ACT-4).
- [data_quality] Outgoing agency messages are signed under two different brands ('Meadow Solutions' and 'Northbridge Lettings') for the same ticket, and the landlord's email in event-004 quotes a request text that differs from the ticket description. → Noted for the office in ACT-4; no party was told which brand or text is correct.
- [other] A repair reported on 21 Feb 2024 ran to 11 Jun 2024 without a confirmed visit — relevant to the reasonable-time duty under s.11 Landlord and Tenant Act 1985. → Recorded as clock CLK-S11 and included in the office task.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "047", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed | message=Dear Eliza Jenkins — regarding the bedroom window at Flat 2… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed | message=Flat 24, 150 Copperfield Walk, Kingshaven, ZZ3 7ZZ — bedroo… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_contractor | completed | message=Window Repair Request, Flat 24, 150 Copperfield Walk, Kings… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | create_human_task | completed | queue=property_manager, title=Case 047 — reconcile conflicting records before closure (pr…, summary=Window repair, Flat 24, 150 Copperfield Walk (tenant report… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 7 | add_note | completed | note=Safety check recorded: the fault is a bedroom window that "… | {"id": "ACT-5"} | CAP-LOG |
| 8 | put_on_hold | completed | reason=Waiting for Tenant — confirmation that the bedroom window h…, until=3 days from today | {"id": "ACT-6"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Has anyone attended and repaired the bedroom window at Flat 24, 150 Copperfield Walk, and does the window now close and lock securely? (blocking; Only an unsourced system note (event-035) says the job is complete; the tenant's confirmation is needed before the request can be closed, and a window that still will not lock would be a security matter (RTE-TENANT).)
- Ask **landlord**: Please confirm that your own contractor carried out and completed the bedroom window repair at Flat 24, 150 Copperfield Walk, and whether any invoice or paperwork will follow to us. (blocking; Landlord confirmation of completion and of who paid is required by the playbook's final checks; the landlord's only reply on file (event-010) named a different address, Flat 18, 88 Alder Lane (RTE-LANDLORD).)
- Ask **contractor**: Oscar Turner: did you book or attend any visit at Flat 24, 150 Copperfield Walk, and has any charge been raised? (non-blocking; He was instructed (event-018) and never replied to three chases; needed to rule out a duplicate visit or charge (RTE-CONTRACTOR).)

Promises made or recorded:
- agency → tenant: Landlord would be asked and the tenant updated on his response [kept]
- agency → tenant: Provider Oscar Turner would contact the tenant to arrange a time or quote [broken]
- agency → tenant: Confirm the repair outcome and re-triage immediately if the window still does not close or lock by 3 days from today [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day deadline 2024-02-22
