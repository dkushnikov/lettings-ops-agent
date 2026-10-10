# ANSWER — Case 009 — Case 009: Front garden maintenance follow-up

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Front garden tidy from inspection: completion unevidenced despite "complete done", so photos re-requested from tenant and address discrepancy referred to the office.
**Stage:** on_hold · **Hold:** Waiting for Tenant — photos of the completed front garden at Flat 4, 174 Beacon Close requested by 13 March 2024 (ACT-2); office in parallel asked to resolve the Lantern Quay address discrepancy and confirm whether photos arrived outside the ticket (ACT-3).
**Last update:** 2024-03-06 09:44:07 UTC (event-023) · **Decided:** 2026-10-10 13:21 UTC
**Next step:** Tenant (Bennett) to email photos of the completed front garden by 13 March 2024; if none, the office decides on an inspection visit or closure without photos.

Definition of done (1/4 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — index / event-001 — front garden item categorised from the inspection; urgency routine, no hazard or spend (ACT-1).
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Tenant-performed garden upkeep; no spend or contractor engaged, so no landlord authority is required (F2, F3).
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider needed; the tenant is doing the work (event-001, event-006).
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No contractor visit required; no access requested in the case.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote exists; zero-cost item.
- [ ] work_result: Work result recorded from the provider — Tenant stated the work would be finished (event-013) but no photo or inspection result is on file; event-023's 'complete done' is unsupported (F6, F7).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Photos requested since 1 February (event-001) and re-requested with a 13 March reply-by (ACT-2); none received readably (event-020, event-021).
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No cost incurred; nothing to invoice.
- [n/a] landlord_confirmation: Landlord confirmed completion — No landlord-funded work; landlord has not been involved in this ticket.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; no contractor visit.
- [ ] closed: Request closed with a resolution that names who paid — Not closed — work result and documents outstanding and the address discrepancy unresolved; ticket held (ACT-4).

## 1. Decision

Kept the ticket open rather than accepting the "complete done" marking. No evidence of completion is on file: the tenant's promised photos (event-013) never arrived in a readable form (event-020 unparsable; event-021 records non-receipt), yet event-022 and event-023 treat it as received and done. The work is tenant-performed garden upkeep — no spend, contractor, access or landlord authority is engaged, so no dispatch or approval step applies. Recorded the conflict between the case record address (Flat 4, 174 Beacon Close) and the Lantern Quay address used in three agency chasers, referred it to the office (ACT-3) rather than arbitrating it to a party, re-asked the tenant for photos at the address on the agency's own record with a reply-by of 13 March 2024 (ACT-2), and held the ticket (ACT-4).

Actions deliberately withheld:
- Did not close the request despite event-023's 'complete done' — no work result or documents on file.
- Did not tell the tenant that the Lantern Quay reference was definitely an error, or that a second property exists; that is the office's to settle.
- Did not state or imply that the tenant is liable for garden works or for any cost of remedying them (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Did not instruct a gardener or raise any spend — no landlord cap on file and no approval in the history.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-TENANT, RTE-STAFF, PRO-PII, PRO-TENANT-LIABILITY, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Case property is Flat 4, 174 Beacon Close, Westmarsh, ZZ5 5ZZ; the item is front garden maintenance picked up at an inspection. [index, get_case_details; high]
- F2: The garden work is being carried out by the tenant, not by a contractor: every agency message asks the tenant to confirm they 'managed to sort the front garden maintenance' and send photos. [event-001, event-009; high]
- F3: No hazard, loss of service or spend appears anywhere in the case; no contractor, access window or landlord approval has been involved at any point. [index, event-001, event-023; high]
- F4: Tenant stated on 13 February that the work was delayed by a family medical situation and would be done that weekend with a photo to follow. [event-006, event-007; medium]
- F5: Tenant emailed on 26 February (untrusted) that the work 'will be finished this evening' with photos the next morning; no photos are on file. [event-013, event-014; medium]
- F6: The tenant's 6 March email could not be parsed and contained no answer; the same day's note records that the tenant's email had still not been received despite a resend during the call. [event-019, event-020, event-021; high]
- F7: Minutes after that note, the agency told the tenant 'it has come through this time' (event-022) and marked the case 'complete done' (event-023) — with no photo, inspection result or other completion evidence on file. [event-021, event-022, event-023; high]
- F8: Three agency chasers ask about the garden at 'Flat 2, 72 Lantern Quay, Eastmere, ZZ4 0ZZ' while carrying the Flat 4, 174 Beacon Close header address. [event-011, event-016, event-017; high]
- F9: No landlord spend cap or standing instruction is on file for this property; none is needed, as the case involves no spend. [get_case_details; medium]

Conflicts between sources:
- The agency's own outgoing emails disagree about which property the garden item concerns: case record and email headers say Flat 4, 174 Beacon Close; the bodies of event-011, event-016 and event-017 say Flat 2, 72 Lantern Quay, Eastmere. → Acted on the case record address (crm_record/ticket outranks email bodies) for the tenant chaser, and referred the discrepancy to the office via create_human_task (ACT-3) rather than asserting a correction to a party. (source_hierarchy)
- Event-021 records the tenant's email as not received; event-022 and event-023, minutes later, state it came through and the job is complete. → Treated completion as unevidenced; ticket left open and the office asked whether photos arrived outside the ticket. (unresolved)

Red flags:
- [data_quality] Three chasers sent to the tenant name a different property in the body than in the header, which may explain the stalled correspondence. → Conflict recorded (ACT-1); office asked to confirm which property and correct the file (ACT-3); tenant chaser sent against the case-record address with an apology for the confusion (ACT-2).
- [data_quality] Case marked 'complete done' with no completion evidence, immediately after a note recording that the tenant's email had not arrived. → Did not close the request; photos re-requested and the marking flagged to the office.
- [vulnerability] Tenant disclosed a family medical situation (relative in hospital) as the reason for delay. No loss of essential service or hazard, so ESC-VULNERABLE is not triggered; relevant only to the tone and pace of chasing. → Kept inside the case record, not shared with third parties (PRO-PII); chaser worded without pressure and offers the tenant the option to report what is holding the work up.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "009", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Record review. Case property per authoritative case record:… | {"id": "ACT-1"} | CAP-LOG |
| 4 | notify_tenant | completed | message=Good afternoon,  Re: front garden maintenance at Flat 4, 17… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | create_human_task | completed | queue=property_manager, title=Case 009 — address discrepancy in chasers and unevidenced "…, summary=Two things for the office to settle on Case 009 (front gard… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 6 | put_on_hold | completed | reason=Waiting for Tenant — photos of the completed front garden a…, until=2024-03-13 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Please reply with one or two photos of the front garden at Flat 4, 174 Beacon Close, Westmarsh, ZZ5 5ZZ as it stands now, or tell us what is holding the work up. (blocking; The agency has chased since 1 February (event-001) and the promised photos (event-013) have never arrived readably (event-020, event-021); photographic evidence is the only thing that can close the inspection item.)
- Ask **property_manager**: Is there a second garden ticket at Flat 2, 72 Lantern Quay, Eastmere, ZZ4 0ZZ, or was that address a template error in event-011/016/017 — and were any tenant photos received outside this ticket before event-023 was marked complete? (non-blocking; The agency's own emails name two properties and the completion marking has no supporting evidence; both change what happens next.)

Promises made or recorded:
- agency → tenant: File will be updated on receipt of photos; if something is holding the work up we will record that instead. by 2024-03-13 [open]
- tenant → agency: Send photos of the completed front garden (promised 13 Feb and again 26 Feb) by 2024-02-27 [broken]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
