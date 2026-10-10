# ANSWER — Case 028 — Case 028: Loose Water Pipe in the Back Garden

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Loose garden water pipe; landlord's own contractor reported it complete 19/06/25 — tenant asked to confirm the repair and the address conflict referred to the office.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation that the pipe is repaired and confirmation of the full property address; 3 working days (ACT-5). Office also to resolve the address conflict (ACT-2).
**Last update:** 2025-07-03 17:05:12 UTC (event-014) · **Decided:** 2026-10-10 13:27 UTC
**Next step:** Tenant to confirm the repair is complete and the full property address (asked ACT-3; 3 working day clock); office to resolve which address the ticket belongs to (ACT-2).

Definition of done (4/7 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 report logged and categorised; acknowledged to the tenant at event-004. Urgency routine: a loose external garden pipe with no flooding, no water near electrics and no loss of supply reporte…
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 — landlord Grace Oakley: 'We will sort this issue', i.e. the landlord used her own contractor; no agency spend arose.
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's own contractor handled the work (event-007, event-012); no agency provider instructed. Tenant was told the position at ACT-3.
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Access arranged directly by the landlord's own contractor (event-007); no agency access booking needed.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote sought or received by the agency; landlord bore the work at her own cost (event-007, event-012).
- [ ] work_result: Work result recorded from the provider — Landlord states 'All completed on 19/06/25' (event-012), but no provider report, photo or tenant confirmation is on file; tenant asked to confirm at ACT-3.
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice available to the agency — work carried out by the landlord's own contractor outside agency instruction (event-007, event-012); skip reason recorded at ACT-1.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-014 — request marked 'completed without payment'; no agency invoice exists because the landlord instructed and paid her own contractor (event-007).
- [x] landlord_confirmation: Landlord confirmed completion — event-012 landlord's own message confirming completion; logged at event-013; acknowledged back to the landlord at ACT-4.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued; access was arranged by the landlord (event-007).
- [ ] closed: Request closed with a resolution that names who paid — Held open pending the tenant's confirmation that the pipe is repaired (ACT-3, ACT-5) and the office's resolution of the address conflict (ACT-2).

## 1. Decision

Did not close. The landlord took the job on with her own contractor and reported it complete on 19/06/25 (event-007, event-012), and the agency logged completion without payment (event-013, event-014), so there is no agency spend or dispatch to make. Two agency records give different addresses for the same fault (event-003/event-010 vs event-009), so I recorded the conflict and referred it to the office rather than asserting an address to any party (ACT-1, ACT-2). I told the tenant the landlord reports the work done, asked them to confirm the pipe is sound and to confirm the full address (ACT-3), confirmed the position to the landlord (ACT-4), and placed the ticket on hold for the tenant's reply (ACT-5). Closure waits on the tenant's confirmation and the office's address correction.

Safety actions taken first:
- Checked the artefacts against the safety-pass terms and the emergency definitions: no mention of gas, electrics, water ingress into the dwelling, loss of water supply, heating, security, damp/mould, alarms or occupant vulnerability — routine classification confirmed (index, event-001, event-009).

Actions deliberately withheld:
- Did not close the request (CAP-CLOSE): work result unverified by the tenant and the address conflict is unresolved — a closure with pending checklist items would be premature.
- Did not dispatch a contractor: the landlord elected to use her own and reports the work done (event-007, event-012); instructing now would duplicate the work order and create unauthorised spend (APR-ALWAYS-ASK / APR-SPEND-OVER-CAP, no cap on file).
- Did not state either address to the tenant or landlord as the correct one; referred the conflict to the office instead (rule 2, ESC-CONFLICT).
- Did not copy the names appearing in the forwarded email body into correspondence with other parties (rule 7).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, ESC-CONFLICT, RTE-TENANT, RTE-STAFF, CAP-CLOSE, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 16/06/2025 that the water pipe in the back garden had become loose, with a photo attached. [index, event-001; high]
- F2: The agency acknowledged the report to the tenant on 18/06/2025 and told them the landlord had been asked how to proceed. [event-004; high]
- F3: The agency asked the landlord on 18/06/2025 whether to instruct a contractor or whether the landlord would arrange their own. [event-003; high]
- F4: The landlord (Grace Oakley) replied 'We will sort this issue', i.e. she would arrange the repair herself; the agency held the case awaiting the landlord's contractor. [event-007, event-008; high]
- F5: On 03/07/2025 the landlord replied to the agency's chase stating 'All completed on 19/06/25'; the agency logged landlord confirmation and marked the task completed without payment. [event-012, event-013, event-014; high]
- F6: No contractor was instructed by the agency and no agency spend, quote or invoice arose on this ticket. [get_action_ledger, event-014; high]
- F7: The ticket and all agency-to-landlord emails carry the property as Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ. [index, event-003, event-010, get_case_details; high]
- F8: A forwarded email chain of 18/06/2025, in which the agency asked the reporter to confirm the full address, records the reply as Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ for the same 'back garden water pipe' fault. [event-009; high]
- F9: The tenant has not been informed of the reported completion and has not confirmed the repair; the last message to them was the 18/06 acknowledgement promising further contact. [event-004; high]
- F10: No hazard indicators (gas, electrics, water near electrics, loss of supply, heating, security) and no occupant vulnerability appear anywhere in the artefacts. [index, event-001, event-009; medium]

Conflicts between sources:
- Two agency records give different properties for the same reported fault: Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ (ticket and landlord emails) versus Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ (forwarded chain where the reporter was asked for the full address). → Not decided by me. Recorded as a conflict (ACT-1) and referred to the property manager queue (ACT-2); the tenant has been asked to confirm their full address (ACT-3). No address was asserted to any party. Routine, reversible steps continued in the meantime. (asked)
- Names in the forwarded chain (reporter 'Imogen Quinn', agency sender signing as 'Felix' but addressed as 'Theo Oakley') do not match the case parties on the ticket record. → Flagged to the office with the address conflict (ACT-2); no name from a message body was copied into correspondence with another party. (asked)

Red flags:
- [data_quality] Conflicting property addresses across agency records for the same fault (87 Alder Lane, Bellmere vs 177 Alder Lane, Northbridge), plus party names in the forwarded chain that do not match the ticket record. → Conflict noted in the case record (ACT-1) and referred to the property manager queue (ACT-2); tenant asked to confirm the address (ACT-3). No address asserted to any party.
- [other] Completion rests solely on the landlord's untrusted email ('All completed on 19/06/25'), with no provider report, photo or tenant confirmation, yet the ticket was marked completed without payment. → Did not close; asked the tenant to confirm the repair before closure (ACT-3, ACT-5).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "028", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Address conflict on file: case record and agency emails say… | {"id": "ACT-1"} | CAP-LOG |
| 4 | create_human_task | completed | queue=property_manager, title=Case 028 — address conflict between agency records (87 Alde…, summary=Two agency records disagree on the property for this repair… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 5 | notify_tenant | completed | message=Good afternoon,  Further to your report of the loose water… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Good afternoon, Grace,  Thank you for confirming that the b… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | put_on_hold | completed | reason=Waiting for Tenant — tenant asked to confirm the pipe is re…, until=3 working days from today | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Is the back garden water pipe now repaired and secure following the landlord's contractor's visit, reported as completed on 19 June 2025? (blocking; The only evidence of completion is the landlord's own message (event-012); the tenant has never been told or asked to confirm, and the playbook requires a work result before closure.)
- Ask **tenant**: Please confirm the full address, including postcode, of the property where the loose pipe was reported. (blocking; The ticket and landlord correspondence say Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ (index, event-003, event-010); the forwarded email chain gives Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ (event-009).)

Promises made or recorded:
- agency → tenant: Further contact as soon as possible after the landlord responded [kept]
- agency → tenant: Close the request as completed by the landlord's contractor if no reply within 3 working days; the tenant may reopen by replying by 3 working days from ACT-3 [open]
- agency → landlord: Let the landlord know if anything further is reported by the tenant [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-SOP-ACK [sop]: Tenant reply window on completion confirmation deadline 3 working days from the message at ACT-3
