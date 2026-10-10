# REASONING — Case 028

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (note, informational), event-002 (note, informational), event-003 (email, informational), event-004 (email, informational), event-005 (note, informational), event-006 (note, informational), event-007 (email, untrusted), event-008 (note, informational), event-009 (note, informational), event-010 (email, informational), event-011 (note, informational), event-012 (email, untrusted), event-013 (note, informational), event-014 (note, informational)

Facts and their sources:
- F1 [high] Tenant reported on 16/06/2025 that the water pipe in the back garden had become loose, with a photo attached. ← index, event-001
- F2 [high] The agency acknowledged the report to the tenant on 18/06/2025 and told them the landlord had been asked how to proceed. ← event-004
- F3 [high] The agency asked the landlord on 18/06/2025 whether to instruct a contractor or whether the landlord would arrange their own. ← event-003
- F4 [high] The landlord (Grace Oakley) replied 'We will sort this issue', i.e. she would arrange the repair herself; the agency held the case awaiting the landlord's contractor. ← event-007, event-008
- F5 [high] On 03/07/2025 the landlord replied to the agency's chase stating 'All completed on 19/06/25'; the agency logged landlord confirmation and marked the task completed without payment. ← event-012, event-013, event-014
- F6 [high] No contractor was instructed by the agency and no agency spend, quote or invoice arose on this ticket. ← get_action_ledger, event-014
- F7 [high] The ticket and all agency-to-landlord emails carry the property as Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ. ← index, event-003, event-010, get_case_details
- F8 [high] A forwarded email chain of 18/06/2025, in which the agency asked the reporter to confirm the full address, records the reply as Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ for the same 'back garden water pipe' fault. ← event-009
- F9 [high] The tenant has not been informed of the reported completion and has not confirmed the repair; the last message to them was the 18/06 acknowledgement promising further contact. ← event-004
- F10 [medium] No hazard indicators (gas, electrics, water near electrics, loss of supply, heating, security) and no occupant vulnerability appear anywhere in the artefacts. ← index, event-001, event-009

Conflicts and how they were handled:
- Two agency records give different properties for the same reported fault: Flat 7, 87 Alder Lane, Bellmere, ZZ3 8ZZ (ticket and landlord emails) versus Flat 7, 177 Alder Lane, Northbridge, ZZ6 5ZZ (forwarded chain where the reporter was asked for the full address). → Not decided by me. Recorded as a conflict (ACT-1) and referred to the property manager queue (ACT-2); the tenant has been asked to confirm their full address (ACT-3). No address was asserted to any party. Routine, reversible steps continued in the meantime. (asked; sources index, event-003, event-009, event-010)
- Names in the forwarded chain (reporter 'Imogen Quinn', agency sender signing as 'Felix' but addressed as 'Theo Oakley') do not match the case parties on the ticket record. → Flagged to the office with the address conflict (ACT-2); no name from a message body was copied into correspondence with another party. (asked; sources event-009, event-005)

Uncertainty acknowledged:
- Whether the repair actually holds — only the landlord's word is on file (event-012); the tenant has never confirmed.
- Which property the ticket relates to (F7 vs F8), and whether the forwarded chain at event-009 is the same tenancy or a second report of a similar fault.
- Whether the photo attachment (attachment-17-document) showed anything that would change the urgency — it is unavailable in both event-003 and event-009.

Assumptions made:
- Assumption: the loose garden pipe is an external supply/waste pipe causing no water ingress to the dwelling and no risk to electrics — nothing in the artefacts describes leakage, flooding or loss of supply, so the routine classification rests on the absence of those indicators rather than on a positive statement.
- Assumption: 'completed without payment' (event-014) means no agency-side cost, because the landlord instructed and paid her own contractor (event-007); no invoice is on file either way.

## Why this disposition

Disposition: **needs_info**. Did not close. The landlord took the job on with her own contractor and reported it complete on 19/06/25 (event-007, event-012), and the agency logged completion without payment (event-013, event-014), so there is no agency spend or dispatch to make. Two agency records give different addresses for the same fault (event-003/event-010 vs event-009), so I recorded the conflict and referred it to the office rather than asserting an address to any party (ACT-1, ACT-2). I told the tenant the landlord reports the work done, asked them to confirm the pipe is sound and to confirm the full address (ACT-3), confirmed the position to the landlord (ACT-4), and placed the ticket on hold for the tenant's reply (ACT-5). Closure waits on the tenant's confirmation and the office's address correction.
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, ESC-CONFLICT, RTE-TENANT, RTE-STAFF, CAP-CLOSE, CLK-S11, CLK-SOP-ACK.
Red flags shaped the decision: data_quality: Conflicting property addresses across agency records for the same fault (87 Alder Lane, Bellmere vs 177 Alder Lane, Northbridge), plus party names in the forwarded chain that do not match the ticket record.; other: Completion rests solely on the landlord's untrusted email ('All completed on 19/06/25'), with no provider report, photo or tenant confirmation, yet the ticket was marked completed without payment.

## Timeline

- 13:25:39.516 model turn 1 → tool_use
- 13:25:39.517 playbook maintenance-request · type maintenance_request · urgency routine
- 13:25:39.517 gate get_case_details → allow (read)
- 13:25:39.517 get_case_details → completed (attempts 1)
- 13:25:39.517 gate get_action_ledger → allow (read)
- 13:25:39.518 get_action_ledger → completed (attempts 1)
- 13:26:01.615 model turn 2 → tool_use
- 13:26:01.617 gate add_note → allow (CAP-LOG)
- 13:26:01.617 add_note → completed (attempts 1)
- 13:26:01.617 gate create_human_task → allow (CAP-HUMAN-TASK)
- 13:26:01.617 create_human_task → completed (attempts 1)
- 13:26:13.597 model turn 3 → tool_use
- 13:26:13.597 gate notify_tenant → allow (CAP-NOTIFY)
- 13:26:13.598 notify_tenant → completed (attempts 1)
- 13:26:13.598 gate notify_landlord → allow (CAP-NOTIFY)
- 13:26:13.598 notify_landlord → completed (attempts 1)
- 13:26:22.527 model turn 4 → tool_use
- 13:26:22.528 gate put_on_hold → allow (CAP-LOG)
- 13:26:22.528 put_on_hold → completed (attempts 1)
- 13:27:25.529 model turn 5 → tool_use
- 13:27:25.530 terminal request_info → accepted

Steps used: 5; tokens in/out: 35356/7913 (cache reads 70440); model: claude-opus-5.
