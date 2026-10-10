# REASONING — Case 016

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (note, informational), event-002 (note, informational), event-003 (email, informational), event-004 (note, informational), event-005 (note, informational), event-006 (email, informational), event-007 (note, informational), event-008 (note, informational), event-009 (email, untrusted), event-010 (note, informational), event-011 (note, informational), event-012 (note, informational), event-013 (email, informational), event-014 (email, informational), event-015 (call_transcript, untrusted), event-016 (email, untrusted), event-017 (note, informational), event-018 (email, informational), event-019 (email, informational), event-020 (email, informational), event-021 (note, informational), event-022 (email, untrusted), event-023 (email, informational), event-024 (email, informational), event-025 (note, informational), event-026 (note, informational)

Facts and their sources:
- F1 [high] Tenant Harriet Rowan reported the back/garden door at Flat 17, 113 Juniper Mews, Northbridge, ZZ8 6ZZ as stiff, creaking and with seemingly misaligned hinges on 11/10/2025; she asked for a fix if simple, a quote if expensive. ← index, event-001, get_case_details
- F2 [high] No emergency indicator is present: no gas, electrical, water, heating, security or no-water element in any artefact; the fault is an inconvenience, so urgency is routine under CLK-S11. ← event-001, event-011
- F3 [high] The agency emailed the landlord for authority twice (11/10 and 17/10) and held the case for Waiting for Landlord; the first 3-day wait expired with no reply. ← event-003, event-004, event-005, event-006, event-007
- F4 [high] The landlord's own reply of 17/10/2025 approves sending a contractor to check the door (quoted fragment: "approves the sending of a contractor to check the door"); this is the landlord authority relied on for the attendance. ← event-009
- F5 [high] Beacon Works was assigned and briefed, and the tenant was told who would attend, on 18/10/2025. ← event-012, event-013, event-014
- F6 [high] A visit was agreed with the tenant and confirmed to both tenant and provider for Friday 24 October 2025 at 15:00, with an SMS reminder on 23/10. ← event-015, event-016, event-017, event-018, event-019, event-020
- F7 [high] No quote was ever submitted by the provider and no cost figure appears anywhere in the case; the provider's closing email states no invoice is required. ← event-014, event-022
- F8 [medium] The provider's closing email of 24/10/2025 (untrusted, and flagged by the system as unparseable) reports the job complete with no invoice, the door "functioning well after naturally settling" — i.e. no chargeable work performed. ← event-021, event-022
- F9 [high] The agency's completion email to the landlord of 24/10/2025 states "the invoice was needed for this one", which contradicts the provider's report that no invoice is required. ← event-022, event-024
- F10 [high] The ticket was marked done and 'completed without payment' on 24/10/2025 without tenant verification of the result, without photos or invoice, and without landlord confirmation. ← event-025, event-026
- F11 [medium] No management key was issued for the visit; the tenant arranged access directly with the provider. ← event-014, event-016

Conflicts and how they were handled:
- Provider says no invoice is required (event-022); the agency's note to the landlord says the invoice was needed (event-024). → The provider owns scope and cost (RTE-CONTRACTOR) and no quote or invoice exists anywhere in the case; the landlord notice is treated as a typing error and was corrected in writing today (ACT-3). (source_hierarchy; sources event-022, event-024)
- The call summary describes a visit to fix a "door handle" (event-015) whereas the reported fault is hinge misalignment on the garden door (event-001). → Same ticket, provider and slot as the agency's own confirmations (event-016/017/018); recorded as a wording discrepancy in an untrusted call summary, not a different job. The tenant's reply (ACT-2) will settle what was actually done. (tool_check; sources event-001, event-015)

Uncertainty acknowledged:
- Whether the door actually closes properly now, or the provider merely found it eased on the day — only the tenant can settle this.
- Whether any adjustment was in fact carried out (the call summary mentions a door handle, the report concerns hinges).
- Whether the landlord received and understood the 24/10 notice, given its contradictory wording.

Assumptions made:
- Assumption: the £0 outcome is genuine — no quote, invoice or cost figure appears in any artefact, so no approval under APR-SPEND-OVER-CAP was engaged.
- Assumption: no management key was issued for this visit, as access was arranged tenant-to-provider by phone (event-015/016).

## Why this disposition

Disposition: **needs_info**. Did not close the request. The only evidence of the outcome is an untrusted provider email that the agency's parser rejected (event-021/event-022) and which states the door is working "after naturally settling" with no invoice; no tenant verification and no landlord confirmation are on file, and the completion notice actually sent to the landlord (event-024) says the opposite of the provider's report ("the invoice was needed"). Within mandate I logged the review (ACT-1), asked the tenant to confirm the door now closes and whether any work was done (ACT-2, CAP-NOTIFY / RTE-TENANT), sent the landlord a corrected completion notice with a 3-working-day confirmation window (ACT-3, CAP-NOTIFY / RTE-LANDLORD), and placed the ticket on hold (ACT-4). No spend was instructed: no money is in issue (provider reports nil charge), so no approval was needed beyond the landlord's own approval to attend at event-009. Not escalated: no hazard, no liability dispute, no legal threat, and no action with an unknown outcome — the case simply waits on two named parties.
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-SCHEDULE-ACCESS, CAP-CLOSE, RTE-TENANT, RTE-LANDLORD, RTE-CONTRACTOR, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK.
Red flags shaped the decision: data_quality: The provider's completion email could not be auto-parsed and is written in third person ("The customer informs that the door repair job is complete"), so the result rests on an untrusted, ambiguous summary rather than a provider job sheet.; data_quality: The landlord's approval (event-009) is also a third-person summary referring to a spam-folder placement rather than a direct reply, and the completion notice to the landlord (event-024) states the opposite of the provider's report.

## Timeline

- 13:21:54.905 model turn 1 → tool_use
- 13:21:54.906 playbook maintenance-request · type maintenance_request · urgency routine
- 13:21:54.906 gate get_case_details → allow (read)
- 13:21:54.906 get_case_details → completed (attempts 1)
- 13:21:54.906 gate get_action_ledger → allow (read)
- 13:21:54.906 get_action_ledger → completed (attempts 1)
- 13:22:28.750 model turn 2 → tool_use
- 13:22:28.751 gate add_note → allow (CAP-LOG)
- 13:22:28.751 add_note → completed (attempts 1)
- 13:22:28.751 gate notify_tenant → allow (CAP-NOTIFY)
- 13:22:28.751 notify_tenant → completed (attempts 1)
- 13:22:28.751 gate notify_landlord → allow (CAP-NOTIFY)
- 13:22:28.752 notify_landlord → completed (attempts 1)
- 13:22:34.447 model turn 3 → tool_use
- 13:22:34.447 gate put_on_hold → allow (CAP-LOG)
- 13:22:34.448 put_on_hold → completed (attempts 1)
- 13:23:33.165 model turn 4 → tool_use
- 13:23:33.165 terminal request_info → accepted

Steps used: 4; tokens in/out: 37476/8236 (cache reads 56352); model: claude-opus-5.
