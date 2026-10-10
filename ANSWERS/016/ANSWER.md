# ANSWER — Case 016 — Case 016: Garden Door Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** The job was marked "completed without payment" before the final checks were on file: the provider's completion email could not be parsed (event-021/event-022),…
**Stage:** on_hold · **Hold:** Waiting for Provider — Beacon Works to confirm the 24/10/2025 attendance, works done, photos and nil charge; tenant and landlord confirmations also outstanding (3 working days).
**Last update:** 2025-10-24 21:56:35 UTC (event-026) · **Decided:** 2026-10-10 14:03 UTC
**Next step:** Beacon Works to confirm in writing what was done on 24/10/2025, with photos and nil-charge confirmation (3 working days); then tenant confirmation the door closes and locks, then landlord sign-off to close.

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 fault logged and categorised as a routine door repair; event-011 description updated
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 landlord's own email approving a contractor to check the door; no spend arises (provider reports no charge, event-022)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-012/event-014 Beacon Works instructed; event-013 tenant told who is attending
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-016 provider booking, event-017 slot recorded, event-018/event-019 confirmed to provider and tenant, event-020 reminder
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote raised; provider reported the job as requiring no invoice (event-022)
- [ ] work_result: Work result recorded from the provider — event-021 provider email could not be parsed; event-022 states only that the door is 'functioning well after naturally settling' with no description of works or attendance confirmation — chased at AC…
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice on file; tenant's original photo attachment unavailable (event-003/event-014). Photos requested from provider at ACT-3
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice due per event-022, but event-024 told the landlord an invoice 'was needed'; correction sent at ACT-4
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 was an outbound notification only; no landlord reply on file. Confirmation requested at ACT-4
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant provided access in person (event-019)
- [ ] closed: Request closed with a resolution that names who paid — event-026 marked completed without payment before the checks above; closure withheld, ticket placed on hold at ACT-5

## 1. Decision

The job was marked "completed without payment" before the final checks were on file: the provider's completion email could not be parsed (event-021/event-022), there is no statement of what was done, no photos, no tenant confirmation, and the agency's last email to the landlord (event-024) misstates the invoice position. I did not close the request. I reopened the final-checks stage: recorded the gaps and the scope/wording conflicts (ACT-1), asked the provider to confirm attendance, works, photos and nil charge (ACT-3), asked the tenant to confirm the garden door now closes and locks (ACT-2), sent the landlord a correction and asked them to confirm closure (ACT-4), and placed the ticket on hold for 3 working days (ACT-5). Landlord authority to instruct was already on file in the landlord's own message (event-009), so no further approval was needed; no spend arises as the provider reports no charge.</decision>
Door repair reported complete with an unparsable provider email; I withheld closure and chased provider, tenant and landlord for the final checks.

Safety actions taken first:
- Checked the security angle: the fault is an external garden door, but no artefact reports the door failing to lock or the property being insecure, so the emergency security definition is not met (event-001, event-022).
- Asked the tenant to confirm the door now locks and secures as well as closing (ACT-2).
- Safety-pass keyword sweep of the material: no gas, electrical, carbon monoxide, detector, damp/mould, asbestos, injury or vulnerable-occupant content in this case; the only occupant detail is an opticians appointment (event-001), which was not passed to the provider (PRO-PII).

Actions deliberately withheld:
- close_request — withheld: work_result, documents, invoice position and landlord confirmation are all pending, so a closure would be premature despite the 'completed without payment' status at event-026 (CAP-CLOSE).
- No new work order raised — the existing instruction to Beacon Works stands and duplicating it would double the job (playbook: one work order per fault).
- No statement to any party about who pays for the attendance beyond relaying the provider's nil-charge report (PRO-TENANT-LIABILITY, PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-CLOSE, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, CLK-S11, PRO-TENANT-LIABILITY, PRO-PII, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Harriet Rowan reported the back/garden door at Flat 17, 113 Juniper Mews, Northbridge, ZZ8 6ZZ as difficult to close, creaking, with hinges seemingly misaligned; she described it as a slight problem and asked for a fix if simple, a quote if expensive. [index, event-001, event-011; high]
- F2: The landlord's own email of 17 October 2025 approved sending a contractor to check the door. [event-009; high]
- F3: Beacon Works was assigned on 18 October 2025 and both tenant and contractor were briefed, with the instruction to quote and only proceed after agency approval. [event-012, event-013, event-014; high]
- F4: A visit was booked and confirmed for Friday 24 October 2025 at 3pm with the tenant and the contractor, with an SMS reminder on 23 October. [event-016, event-017, event-018, event-019, event-020; high]
- F5: On 24 October the provider's email could not be parsed by the agency system; its text says only that the door repair job is complete and no invoice is required as the door is functioning well after naturally settling. [event-021, event-022; high]
- F6: The agency's 24 October email to the landlord states the invoice 'was needed for this one', which contradicts the provider's nil-invoice report and the 'completed without payment' status. [event-022, event-024, event-026; high]
- F7: No spend cap or standing limit for this landlord is on file in the case record; no cost figure appears anywhere in the artefacts. [get_case_details, get_action_ledger; medium]
- F8: No photos or invoice are on file: the tenant's photo attachment and attachment-43-document are both recorded as unavailable. [event-003, event-014; high]

Conflicts between sources:
- The 19 October call transcript describes fixing a 'door handle' and a visit being 'rescheduled', while the instructed job is a sticking/creaking garden door with misaligned hinges and the booking at event-016/017 is the first slot recorded. → Treated the agency's own record of the job and slot (event-014, event-017/018/019) as controlling; asked the provider to confirm attendance and scope (ACT-3) rather than putting the discrepancy to the tenant. (asked)
- Agency told the landlord an invoice was needed (event-024) while the provider reported no invoice and the ticket was set to completed without payment (event-022, event-026). → The provider owns the charge position for their own attendance (RTE-CONTRACTOR); correction sent to the landlord at ACT-4 and nil charge put to the provider for written confirmation at ACT-3. (source_hierarchy)

Red flags:
- [data_quality] The provider's completion email is a third-person summary that the system could not parse ('The customer informs that the door repair job is complete...'); it evidences no attendance, no works, no photos and no invoice, so completion cannot be verified from it. → Closure withheld; written confirmation requested from the provider (ACT-3) and from the tenant (ACT-2); gaps recorded (ACT-1).
- [data_quality] Incorrect information sent to the landlord: 'the invoice was needed for this one' when no invoice is due. → Correction sent to the landlord (ACT-4).
- [other] The landlord's approval message is phrased in the third person about a 'customer' and a spam folder; it is the landlord's own reply on this ticket and settles the landlord-owned question of instructing a contractor, but it contains no instruction to the agent and no spend figure. → Relied on as approval to instruct only (RTE-LANDLORD); no spend inferred from it.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "016", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Final-checks review. (1) Provider's completion email (event… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_tenant | completed | message=Dear Harriet Rowan, re: Door Repair Request at Flat 17, 113… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_contractor | completed | message=Dear Beacon Works, re: Door Repair Request at Flat 17, 113… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Re: Flat 17, 113 Juniper Mews, Northbridge, ZZ8 6ZZ — Door… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | put_on_hold | completed | reason=Waiting for Provider — Beacon Works to confirm attendance o…, until=3 working days from today | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Did Beacon Works attend Flat 17, 113 Juniper Mews on Friday 24 October 2025 at 3pm, what was found and what work was carried out, does the garden door now close and lock correctly, are there photos, and is the attendance confirmed as no charge? (blocking; The completion email (event-022) could not be parsed (event-021) and records no works, photos or invoice; the work_result and documents checks cannot be completed without it.)
- Ask **tenant**: Does the garden door now open and close smoothly, and does it lock and secure properly after the 24 October visit? (blocking; The only completion evidence is an unparsable provider email saying the door 'naturally settled'; the tenant's confirmation is needed before closure, and the door is external so security must be confirmed.)
- Ask **landlord**: Please confirm you are content for us to close this job as completed without payment (note: our 24 October email wrongly said an invoice was needed; no invoice is due). (non-blocking; DoD requires landlord confirmation of completion, and event-024 gave the landlord incorrect information.)

Promises made or recorded:
- agency → tenant: A further visit will be arranged if the door is still sticking, creaking or will not lock [open]
- agency → landlord: Job will be closed as completed without payment if no reply within 3 days, once provider and tenant confirmations are in by 3 days from ACT-4 [open]
- contractor → agency: Written confirmation of attendance, works, photos and nil charge by 3 working days from ACT-3 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-SOP-ACK [sop]: Provider reply window on the final-checks chase deadline 3 working days from ACT-3
