# ANSWER — Case 021 — Case 021: Key Replacement Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Key replacement reported complete by the provider; closed prematurely, so I reopened final checks and chased the invoice, key handover and landlord confirmation.
**Stage:** on_hold · **Hold:** Waiting for Provider — Alder Compliance to send the invoice (VAT shown) and confirm the keys delivered to the office by 28 November 2024; landlord confirmation of completion also awaited (ACT-2).
**Last update:** 2024-11-23 04:22:42 UTC (event-029) · **Decided:** 2026-10-10 14:05 UTC
**Next step:** Alder Compliance to send the invoice and confirm the key drop-off at the office by 28 November 2024 (ACT-1); landlord Quinn to confirm completion (ACT-2).

Definition of done (6/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/index: snapped conservatory back door key, no spare; categorised routine — conservatory back door, no hazard and no loss of security of the main entry reported
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 — landlord's own email approving the works and the new keys; no standing spend cap on file, so this message is the authority (CAP-DISPATCH-APPROVED)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010/event-012 provider Alder Compliance instructed; tenant told who is attending at event-011
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot was ever recorded in the history (chase at event-018), but the provider attended and completed the job — event-020
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-025 — no quote required, repaired on site; no priced quote was ever issued
- [x] work_result: Work result recorded from the provider — event-020 — provider reports cylinder and handles replaced
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-025 — skip reason recorded: 'No quote required, repaired on site'. No photos supplied; invoice still requested at ACT-1
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice anywhere in the history and no cost figure recorded; requested from the provider at ACT-1 and the position explained to the landlord at ACT-2
- [ ] landlord_confirmation: Landlord confirmed completion — event-026 flagged it as needed; no request was sent before closure at event-029 — now asked at ACT-2
- [ ] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued for the visit (agency held no spare, event-003). The 4 new keys are a deliverable: provider promised the office drop-off 'tomorrow' (event-020) and event-028 records 'Key…
- [ ] closed: Request closed with a resolution that names who paid — event-029 marked the request closed while invoice, landlord confirmation and key-handover evidence were outstanding; file kept open at final checks (ACT-5). A resolution cannot name who paid with no…

## 1. Decision

Treated the ticket as still in final checks rather than closed: the automation closed it (event-029) while the invoice and the landlord's completion confirmation were still outstanding (event-026), and "documents skipped" was recorded with no cost anywhere on file (event-025). Landlord authority for the works is sound — the landlord's own email approved them (event-006) — and the provider has reported the work complete (event-020), so no new dispatch or spend decision was needed. I chased the provider for the invoice and written confirmation of the keys handed to the office, asked the landlord to confirm completion, updated the tenant, logged the data-quality points, and put the case on hold pending those two replies. No closure: a resolution cannot name who paid while no invoice exists.

Safety actions taken first:
- Safety-pass check: the only trigger word in the material is the security of a door lock. The snapped key was for the conservatory back door, not the property's main entry, and no report of the property being left insecure appears in the history (event-001, event-003); the lock has since been replaced (event-020), so no insecure-property emergency applies and no hazard red flag is recorded.
- No gas, electrical, damp/mould, detector or occupant-vulnerability content appears anywhere in the artefacts; nothing to test or record under the safety pass.

Actions deliberately withheld:
- Did not close the request: invoice, landlord confirmation and key-handover evidence are outstanding, so no resolution can name who paid (CAP-CLOSE).
- Did not instruct any further contractor spend: the works are already reported complete and no new quote exists (APR-SPEND-OVER-CAP).
- Did not state or apportion any cost, and did not suggest the tenant pays for the snapped key (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-DISPATCH-APPROVED, CAP-CLOSE, RTE-CONTRACTOR, RTE-LANDLORD, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Property is Flat 22, 148 Lantern Quay, Westmarsh, ZZ4 1ZZ; tenant on the record is Clara Jenkins. [index, get_case_details, event-011; high]
- F2: Reported fault: the key for the conservatory back door snapped and the tenants have no spare; the agency holds no spare for that door either. [event-001, event-003; high]
- F3: Scope instructed: replace the lock and supply 4 keys — 2 tenants, 1 agency, 1 landlord, the latter two to the office. [index, event-008, event-012; high]
- F4: The landlord (Quinn) approved the works and the new keys in their own email of 21 November 2024. [event-006; high]
- F5: Alder Compliance was instructed as the provider and briefed that any quote needed agency approval before proceeding. [event-010, event-012; high]
- F6: The provider reported on 22 November 2024 that the job is complete — cylinder and handles replaced — and that remaining keys would be dropped at the office the next day. [event-020; medium]
- F7: No cost, quote or invoice appears anywhere in the visible history; documents were skipped with the reason 'No quote required, repaired on site'. [event-025, search_history; high]
- F8: Landlord confirmation was flagged as required at 04:22 on 23 November and the request was marked closed 16 seconds later, with no confirmation request sent. [event-026, event-029; high]
- F9: No appointment slot was ever confirmed in the history; the provider was chased once for a booking before reporting the job done. [event-018, event-020; high]

Conflicts between sources:
- Agency note records 'Keys return confirmed' at 04:22 on 23 November, while the provider had only promised to drop the keys off 'tomorrow' (sent 16:04 on 22 November); the same note carries a validation error about priority. → Written confirmation of the key handover requested from the provider (ACT-1); item left pending rather than relying on the system note. (asked)
- Two different tenant phone numbers were sent to the provider: 07700 900625 (described as a code to enter when calling) and 07700 900336. → Logged for the office (ACT-4); no action needed as the provider reached the tenant and completed the job (event-020). (unresolved)
- System closed the request (event-029) while final checks flagged as outstanding (event-026) were incomplete. → Specific outstanding-item note beats the generic 'all checks completed' line; file kept at final checks and placed on hold (ACT-5). (source_hierarchy)

Red flags:
- [data_quality] Outbound agency emails to the contractor are addressed 'Hi Clara' / 'Good morning Clara' — Clara Jenkins is the tenant, not the provider; the provider is Alder Compliance. → Logged at ACT-4; my own messages address each party by their name on the case record.
- [data_quality] Request closed with invoice, landlord confirmation and key-handover evidence outstanding, and a key-return note that the provider's own message does not support. → Case kept at final checks and put on hold (ACT-5); the three outstanding items chased (ACT-1, ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "021", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice cost quote payment | [] | allow |
| 4 | search_history | completed | query=keys office drop off | [] | allow |
| 5 | notify_contractor | completed | message=Re: Key Replacement Request — Flat 22, 148 Lantern Quay, We… | {"id": "ACT-1"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Address: Flat 22, 148 Lantern Quay, Westmarsh, ZZ4 1ZZ  Dea… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Dear Clara Jenkins,  Re: Flat 22, 148 Lantern Quay, Westmar… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | add_note | completed | note=Final checks review. Work result is on file: contractor rep… | {"id": "ACT-4"} | CAP-LOG |
| 9 | put_on_hold | completed | reason=Waiting for Provider — Alder Compliance to supply the invoi…, until=2024-11-28 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **contractor**: Please send your invoice for the key/lock replacement at Flat 22, 148 Lantern Quay (VAT shown separately), and confirm in writing that the remaining keys have been delivered to our office and how many were handed in. (blocking; No invoice or cost figure exists anywhere on the file, so the invoice cannot be forwarded to the landlord and the resolution cannot name who paid; the key drop-off was only promised, not evidenced by the provider (event-020).)
- Ask **landlord**: Please confirm you are satisfied the works at Flat 22, 148 Lantern Quay are complete (cylinder and handles replaced, 4 keys supplied). (blocking; Landlord completion confirmation was flagged as required at event-026 but never requested before the file was closed at event-029.)

Promises made or recorded:
- agency → contractor: Chase again and flag outstanding items to the landlord if the invoice and key confirmation are not received by 2024-11-28 [open]
- agency → landlord: Forward the provider's invoice as soon as it arrives [open]
- agency → tenant: Go back to the provider if the new lock or either key is faulty, and not close the file until the provider's paperwork is in [open]
- contractor → agency: Drop the remaining keys at the office by 2024-11-23 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
