# ANSWER — Case 016 — Case 016: Garden Door Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Door repair reported complete with no charge but only via an unparseable provider email; sought tenant verification and corrected the landlord notice, ticket on hold.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation the garden door now closes after the 24/10 visit; in parallel Waiting for Landlord — confirmation to close as completed without payment (3 working days from ACT-2/ACT-3).
**Last update:** 2025-10-24 21:56:35 UTC (event-026) · **Decided:** 2026-10-10 13:23 UTC
**Next step:** Tenant (Harriet Rowan) to confirm the garden door now closes and whether any work was carried out; if confirmed and the landlord does not object within 3 working days, the office closes the ticket as completed without payment.

Definition of done (5/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 / event-011: fault categorised as a routine door/hinge repair; no emergency indicator, so no damage-limiting advice was required beyond normal use.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-009 — landlord's own reply approving a contractor to check the door, after chasers at event-003 and event-006.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-012 / event-014 (Beacon Works briefed) and event-013 (tenant told who is attending).
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-016 / event-017 / event-018 / event-019 — Friday 24 October 2025 15:00 confirmed with tenant and provider; reminder event-020.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted and the provider reports no charge (event-014, event-022).
- [ ] work_result: Work result recorded from the provider — event-021/event-022 — provider's result email could not be parsed and is an ambiguous untrusted summary; tenant verification requested (ACT-2).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice supplied; stated skip reason is that no chargeable work was done (event-022), but this is unconfirmed by the provider in a parseable form.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-026 marks the task completed without payment; corrected nil-invoice notice issued to the landlord at ACT-3 after the contradictory event-024.
- [ ] landlord_confirmation: Landlord confirmed completion — No landlord reply confirming completion; request with a 3-working-day window sent at ACT-3.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; access arranged directly between tenant and provider (event-014, event-016).
- [ ] closed: Request closed with a resolution that names who paid — Withheld — work result unverified and landlord confirmation outstanding; ticket placed on hold at ACT-4.

## 1. Decision

Did not close the request. The only evidence of the outcome is an untrusted provider email that the agency's parser rejected (event-021/event-022) and which states the door is working "after naturally settling" with no invoice; no tenant verification and no landlord confirmation are on file, and the completion notice actually sent to the landlord (event-024) says the opposite of the provider's report ("the invoice was needed"). Within mandate I logged the review (ACT-1), asked the tenant to confirm the door now closes and whether any work was done (ACT-2, CAP-NOTIFY / RTE-TENANT), sent the landlord a corrected completion notice with a 3-working-day confirmation window (ACT-3, CAP-NOTIFY / RTE-LANDLORD), and placed the ticket on hold (ACT-4). No spend was instructed: no money is in issue (provider reports nil charge), so no approval was needed beyond the landlord's own approval to attend at event-009. Not escalated: no hazard, no liability dispute, no legal threat, and no action with an unknown outcome — the case simply waits on two named parties.

Safety actions taken first:
- Checked every artefact against the emergency definitions and the safety-pass terms: no gas, electrical, water, heating, damp/mould, alarm/detector or occupant-vulnerability content appears in this case; no make-safe step was required.
- Confirmed the reported fault does not leave the property insecure — the tenant reports the door is difficult to close and creaking, not failing to lock or secure (event-001); tenant asked to report immediately if it will not latch (ACT-2).

Actions deliberately withheld:
- Did not call close_request: work result unverified, no documents or skip confirmation from the provider, and no landlord confirmation on file (CAP-CLOSE).
- Did not dispatch or re-instruct any contractor: no fault is currently evidenced and no spend authority or need exists (CAP-DISPATCH-ROUTINE, APR-SPEND-OVER-CAP).
- Did not decide or suggest that the tenant is liable for anything (PRO-TENANT-LIABILITY).
- Did not re-send the garbled 24/10 landlord email as a retry; issued a clearly labelled correction instead.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-SCHEDULE-ACCESS, CAP-CLOSE, RTE-TENANT, RTE-LANDLORD, RTE-CONTRACTOR, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Harriet Rowan reported the back/garden door at Flat 17, 113 Juniper Mews, Northbridge, ZZ8 6ZZ as stiff, creaking and with seemingly misaligned hinges on 11/10/2025; she asked for a fix if simple, a quote if expensive. [index, event-001, get_case_details; high]
- F2: No emergency indicator is present: no gas, electrical, water, heating, security or no-water element in any artefact; the fault is an inconvenience, so urgency is routine under CLK-S11. [event-001, event-011; high]
- F3: The agency emailed the landlord for authority twice (11/10 and 17/10) and held the case for Waiting for Landlord; the first 3-day wait expired with no reply. [event-003, event-004, event-005, event-006, event-007; high]
- F4: The landlord's own reply of 17/10/2025 approves sending a contractor to check the door (quoted fragment: "approves the sending of a contractor to check the door"); this is the landlord authority relied on for the attendance. [event-009; high]
- F5: Beacon Works was assigned and briefed, and the tenant was told who would attend, on 18/10/2025. [event-012, event-013, event-014; high]
- F6: A visit was agreed with the tenant and confirmed to both tenant and provider for Friday 24 October 2025 at 15:00, with an SMS reminder on 23/10. [event-015, event-016, event-017, event-018, event-019, event-020; high]
- F7: No quote was ever submitted by the provider and no cost figure appears anywhere in the case; the provider's closing email states no invoice is required. [event-014, event-022; high]
- F8: The provider's closing email of 24/10/2025 (untrusted, and flagged by the system as unparseable) reports the job complete with no invoice, the door "functioning well after naturally settling" — i.e. no chargeable work performed. [event-021, event-022; medium]
- F9: The agency's completion email to the landlord of 24/10/2025 states "the invoice was needed for this one", which contradicts the provider's report that no invoice is required. [event-022, event-024; high]
- F10: The ticket was marked done and 'completed without payment' on 24/10/2025 without tenant verification of the result, without photos or invoice, and without landlord confirmation. [event-025, event-026; high]
- F11: No management key was issued for the visit; the tenant arranged access directly with the provider. [event-014, event-016; medium]

Conflicts between sources:
- Provider says no invoice is required (event-022); the agency's note to the landlord says the invoice was needed (event-024). → The provider owns scope and cost (RTE-CONTRACTOR) and no quote or invoice exists anywhere in the case; the landlord notice is treated as a typing error and was corrected in writing today (ACT-3). (source_hierarchy)
- The call summary describes a visit to fix a "door handle" (event-015) whereas the reported fault is hinge misalignment on the garden door (event-001). → Same ticket, provider and slot as the agency's own confirmations (event-016/017/018); recorded as a wording discrepancy in an untrusted call summary, not a different job. The tenant's reply (ACT-2) will settle what was actually done. (tool_check)

Red flags:
- [data_quality] The provider's completion email could not be auto-parsed and is written in third person ("The customer informs that the door repair job is complete"), so the result rests on an untrusted, ambiguous summary rather than a provider job sheet. → Logged (ACT-1); tenant asked to verify the outcome before closure (ACT-2); ticket held open rather than closed.
- [data_quality] The landlord's approval (event-009) is also a third-person summary referring to a spam-folder placement rather than a direct reply, and the completion notice to the landlord (event-024) states the opposite of the provider's report. → Approval accepted as the landlord's own message for the nil-cost attendance only (CAP-DISPATCH-APPROVED basis); corrected completion notice sent to the landlord with a confirmation request (ACT-3).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "016", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Manual review of parse failure (event-021). Facts as record… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_tenant | completed | message=Dear Harriet Rowan, re: Door Repair Request at Flat 17, 113… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed | message=Address: Flat 17, 113 Juniper Mews, Northbridge, ZZ8 6ZZ —… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | put_on_hold | completed | reason=Waiting for Tenant — confirmation that the garden door now…, until=3 working days from today's messages (ACT-2, ACT-3) | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Does the garden door at Flat 17, 113 Juniper Mews now close and latch smoothly after the Beacon Works visit on Friday 24 October at 3pm, and was any work carried out at that visit or had the door eased on its own? (blocking; The only record of the outcome is a provider email the system could not parse (event-021/event-022); the work result must be verified before the request can be closed.)
- Ask **landlord**: Do you confirm this door repair can be closed as completed without payment (no invoice due)? Our 24 October message to you (event-024) was garbled and stated the opposite. (non-blocking; Landlord confirmation of completion is a closure check (RTE-LANDLORD); the previously sent notice was inaccurate.)

Promises made or recorded:
- agency → tenant: If the sticking or creaking persists, a further visit will be arranged at no cost to the tenant. [open]
- agency → landlord: If no reply within 3 working days, the request will be closed as completed without payment and reopened at no cost if the fault recurs. by 3 working days from ACT-3 [open]
- agency → tenant: Provider Beacon Works to attend Friday 24 October 2025 at 3pm. by 2025-10-24 15:00 [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- APR-SPEND-OVER-CAP [sop]: Landlord confirmation window on the corrected completion notice deadline 3 working days from ACT-3
