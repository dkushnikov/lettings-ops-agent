# REASONING — Case 009

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (email, informational), event-002 (note, informational), event-003 (email, informational), event-004 (email, informational), event-005 (note, informational), event-006 (call_transcript, informational), event-007 (note, informational), event-008 (note, informational), event-009 (email, informational), event-010 (note, informational), event-011 (email, informational), event-012 (note, informational), event-013 (email, untrusted), event-014 (note, informational), event-015 (note, informational), event-016 (email, informational), event-017 (email, informational), event-018 (note, informational), event-019 (call_transcript, informational), event-020 (email, untrusted), event-021 (note, informational), event-022 (email, informational), event-023 (note, informational)

Facts and their sources:
- F1 [high] Case property is Flat 4, 174 Beacon Close, Westmarsh, ZZ5 5ZZ; the item is front garden maintenance picked up at an inspection. ← index, get_case_details
- F2 [high] The garden work is being carried out by the tenant, not by a contractor: every agency message asks the tenant to confirm they 'managed to sort the front garden maintenance' and send photos. ← event-001, event-009
- F3 [high] No hazard, loss of service or spend appears anywhere in the case; no contractor, access window or landlord approval has been involved at any point. ← index, event-001, event-023
- F4 [medium] Tenant stated on 13 February that the work was delayed by a family medical situation and would be done that weekend with a photo to follow. ← event-006, event-007
- F5 [medium] Tenant emailed on 26 February (untrusted) that the work 'will be finished this evening' with photos the next morning; no photos are on file. ← event-013, event-014
- F6 [high] The tenant's 6 March email could not be parsed and contained no answer; the same day's note records that the tenant's email had still not been received despite a resend during the call. ← event-019, event-020, event-021
- F7 [high] Minutes after that note, the agency told the tenant 'it has come through this time' (event-022) and marked the case 'complete done' (event-023) — with no photo, inspection result or other completion evidence on file. ← event-021, event-022, event-023
- F8 [high] Three agency chasers ask about the garden at 'Flat 2, 72 Lantern Quay, Eastmere, ZZ4 0ZZ' while carrying the Flat 4, 174 Beacon Close header address. ← event-011, event-016, event-017
- F9 [medium] No landlord spend cap or standing instruction is on file for this property; none is needed, as the case involves no spend. ← get_case_details

Conflicts and how they were handled:
- The agency's own outgoing emails disagree about which property the garden item concerns: case record and email headers say Flat 4, 174 Beacon Close; the bodies of event-011, event-016 and event-017 say Flat 2, 72 Lantern Quay, Eastmere. → Acted on the case record address (crm_record/ticket outranks email bodies) for the tenant chaser, and referred the discrepancy to the office via create_human_task (ACT-3) rather than asserting a correction to a party. (source_hierarchy; sources index, event-011, event-016, event-017)
- Event-021 records the tenant's email as not received; event-022 and event-023, minutes later, state it came through and the job is complete. → Treated completion as unevidenced; ticket left open and the office asked whether photos arrived outside the ticket. (unresolved; sources event-021, event-022, event-023)

Uncertainty acknowledged:
- Whether any photos were received outside this ticket before event-023 was marked complete.
- Whether the garden has in fact been done — the last direct evidence is the tenant's own 26 February statement (event-013).
- Whether the tenancy makes front garden upkeep the tenant's obligation; no tenancy agreement is on file in this case, so no liability position is stated (PRO-TENANT-LIABILITY).

Assumptions made:
- Assumption: the Lantern Quay wording in event-011/016/017 is a template error rather than a second ticket, since the header address and the case record both say Flat 4, 174 Beacon Close — put to the office for confirmation rather than relied on.
- Assumption: 13 March 2024 as the tenant reply-by is my own working date, set roughly a week after the last contact (event-022); no artefact sets a deadline.

## Why this disposition

Disposition: **needs_info**. Kept the ticket open rather than accepting the "complete done" marking. No evidence of completion is on file: the tenant's promised photos (event-013) never arrived in a readable form (event-020 unparsable; event-021 records non-receipt), yet event-022 and event-023 treat it as received and done. The work is tenant-performed garden upkeep — no spend, contractor, access or landlord authority is engaged, so no dispatch or approval step applies. Recorded the conflict between the case record address (Flat 4, 174 Beacon Close) and the Lantern Quay address used in three agency chasers, referred it to the office (ACT-3) rather than arbitrating it to a party, re-asked the tenant for photos at the address on the agency's own record with a reply-by of 13 March 2024 (ACT-2), and held the ticket (ACT-4).
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-TENANT, RTE-STAFF, PRO-PII, PRO-TENANT-LIABILITY, CLK-SOP-ACK.
Red flags shaped the decision: data_quality: Three chasers sent to the tenant name a different property in the body than in the header, which may explain the stalled correspondence.; data_quality: Case marked 'complete done' with no completion evidence, immediately after a note recording that the tenant's email had not arrived.; vulnerability: Tenant disclosed a family medical situation (relative in hospital) as the reason for delay. No loss of essential service or hazard, so ESC-VULNERABLE is not triggered; relevant only to the tone and pace of chasing.

## Timeline

- 13:19:47.208 model turn 1 → tool_use
- 13:19:47.208 playbook maintenance-request · type maintenance_request · urgency routine
- 13:19:47.208 gate get_case_details → allow (read)
- 13:19:47.208 get_case_details → completed (attempts 1)
- 13:19:47.209 gate get_action_ledger → allow (read)
- 13:19:47.209 get_action_ledger → completed (attempts 1)
- 13:20:24.559 model turn 2 → tool_use
- 13:20:24.560 gate add_note → allow (CAP-LOG)
- 13:20:24.560 add_note → completed (attempts 1)
- 13:20:24.560 gate notify_tenant → allow (CAP-NOTIFY)
- 13:20:24.560 notify_tenant → completed (attempts 1)
- 13:20:24.560 gate create_human_task → allow (CAP-HUMAN-TASK)
- 13:20:24.561 create_human_task → completed (attempts 1)
- 13:20:24.561 gate put_on_hold → allow (CAP-LOG)
- 13:20:24.561 put_on_hold → completed (attempts 1)
- 13:21:15.994 model turn 3 → tool_use
- 13:21:15.995 terminal request_info → accepted

Steps used: 3; tokens in/out: 22771/7660 (cache reads 42264); model: claude-opus-5.
