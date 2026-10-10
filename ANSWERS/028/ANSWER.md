# ANSWER — Case 028 — Case 028: Loose Water Pipe in the Back Garden

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Loose garden water pipe; landlord's own contractor reported it done 19/06/25 — tenant now asked to confirm, address conflict referred to the office, ticket on hold.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation that the back-garden pipe was repaired by the landlord's contractor; office in parallel to resolve the address conflict. 3-day reply window.
**Last update:** 2025-07-03 17:05:12 UTC (event-014) · **Decided:** 2026-10-10 14:07 UTC
**Next step:** Tenant (Imogen Quinn) to confirm within 3 days whether the back-garden pipe is repaired; office to confirm the correct property record (ACT-2) before the ticket is closed.

Definition of done (4/7 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 (report); routine urgency set this turn; no damage-limiting steps needed beyond the leak warning given in ACT-1
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 — landlord elected to use her own contractor; no agency spend
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord's own contractor (event-007, event-008); agency assigned no provider
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — Access arranged directly by the landlord's contractor (event-008)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No agency quote; landlord's own cost (event-007)
- [ ] work_result: Work result recorded from the provider — Only the landlord's untrusted statement 'All completed on 19/06/25' (event-012); tenant confirmation requested (ACT-1)
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — Landlord's own contractor — agency holds no photos or report; attachment-17-document unavailable (get_attachment)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-014 — completed without payment; landlord bore her own contractor's cost
- [x] landlord_confirmation: Landlord confirmed completion — event-012, event-013
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; no agency visit
- [ ] closed: Request closed with a resolution that names who paid — Held open: tenant confirmation outstanding (ACT-1) and address conflict with the office (ACT-2); ACT-4 on hold

## 1. Decision

Landlord elected to use her own contractor and reported the repair complete on 19/06/25 (event-007, event-012), so there is no agency dispatch, spend or quote to arrange. Two gaps remained: the tenant was never told the outcome (last contact event-004), and the ticket record's address conflicts with the address the tenant herself gave in reply to our question (event-009), which changes which property was repaired. I notified the tenant and asked her to confirm the pipe is actually fixed (ACT-1), referred the address conflict to the office rather than picking a side with any party (ACT-2, per rule on conflicting agency records / ESC-CONFLICT), logged the review (ACT-3) and placed the ticket on hold Waiting for Tenant (ACT-4). Not closed: closure needs the tenant's confirmation and a corrected property record.

Safety actions taken first:
- Checked the artefacts against the emergency definitions: no leak, water ingress, water near electrics, loss of water supply or sewage reported — routine, not emergency.
- Tenant asked to report immediately any leak, overflowing water or water near electrics (ACT-1).

Actions deliberately withheld:
- Did not close the request despite event-014, because the repair is unverified with the tenant and the property record is in conflict.
- Did not assert either address to the tenant or the landlord (conflict referred to the office instead).
- Did not instruct a contractor: no agency spend authority on file and the landlord is using her own contractor.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE (not exercised — definition-of-done items pending), APR-SPEND-OVER-CAP (no agency spend: landlord used her own contractor), ESC-CONFLICT (records disagree — referred to the office), RTE-TENANT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 16/06/2025 that the water pipe in the back garden had become loose, with a photo attached. [index, event-001; high]
- F2: The report contains no emergency indicator: no leak, flooding, water near electrics, loss of water supply or sewage backing up is described anywhere in the artefacts. [event-001, event-009; medium]
- F3: The agency acknowledged to the tenant on 18/06/2025 that the request had gone to the landlord for a decision; this is the last contact with the tenant before today. [event-004; high]
- F4: The landlord (Grace Oakley) replied on 18/06/2025 'We will sort this issue', i.e. she is using her own contractor; no agency instruction or spend was authorised. [event-007; high]
- F5: The landlord confirmed on 03/07/2025 'All completed on 19/06/25'; the agency logged landlord confirmation and marked the task completed without payment. [event-012, event-013, event-014; high]
- F6: The ticket record and all agency emails give the property as Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ; the tenant, answering the agency's own question 'please confirm the full address', gave Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ. [index, event-003, event-010, event-009; high]
- F7: No landlord standing spend cap is on file in this case record, so there is no standing authority for agency spend; none was needed as the landlord used her own contractor. [get_case_details, event-007; medium]
- F8: No photos, contractor report or invoice are held by the agency; the referenced attachment (attachment-17-document) is unavailable. [get_attachment, event-003; high]

Conflicts between sources:
- Property address: ticket record and agency correspondence say Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ; the tenant's own confirmation on the same thread says Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ. The difference changes which property the landlord's contractor attended and whether the completed repair matches the reporting tenant. → Referred to the office via human task ACT-2; no address asserted to any party. Tenant asked only whether her pipe is repaired. (asked)

Red flags:
- [data_quality] Two agency records give different property addresses for the same ticket (event-009 vs the ticket record); also the forwarded email names 'Theo Oakley' as the sender of a message signed 'Felix', so names in message bodies are unreliable and were not copied into any party letter. → Human task raised with the office (ACT-2); internal note logged (ACT-3).
- [other] The ticket was marked 'completed without payment' and landlord-confirmed before the tenant had been told anything or the repair verified at the tenant's address. → Tenant notified and asked to confirm the repair (ACT-1); ticket held open rather than closed.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "028", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=address | [{"event": "event-003", "timestamp": "2025-06-18 21:18:28 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Landlord", "excerpt": "[2025-06-18 2… | allow |
| 4 | search_history | completed | from_party=Tenant | [] | allow |
| 5 | get_attachment | completed | name=attachment-17-document | {"error": "no attachment named attachment-17-document"} | allow |
| 6 | notify_tenant | completed | message=Good afternoon,  Update on your report of the loose water p… | {"id": "ACT-1"} | CAP-NOTIFY |
| 7 | create_human_task | completed | queue=property_manager, title=Case 028 — address conflict between ticket record and tenan…, summary=Two agency records disagree about which property this repai… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 8 | add_note | completed | note=Case 028 review. Routine repair (loose external water pipe,… | {"id": "ACT-3"} | CAP-LOG |
| 9 | put_on_hold | completed | reason=Waiting for Tenant — tenant asked to confirm the back-garde…, until=3 days from today (tenant reply) | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Has the loose water pipe in your back garden been repaired? The landlord's contractor reported the work completed on 19 June 2025 — please confirm, or tell us if it is still loose or leaking. (blocking; Work was done by the landlord's own contractor; the agency has no work result, photos or invoice, and the tenant was never told the outcome (last contact event-004).)
- Ask **property_manager**: Which property record is correct for this ticket: Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ (ticket record, event-003/004/010) or Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ (tenant's confirmation, event-009)? (non-blocking; Authoritative agency records disagree and the difference changes which property the landlord's contractor attended; referred via human task ACT-2.)

Promises made or recorded:
- agency → tenant: If the pipe is still loose or the work was not done, the job will be reopened and taken forward with the landlord. [open]
- agency → tenant: Further contact as soon as possible after the landlord responded (promised 18/06, delivered today). [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
