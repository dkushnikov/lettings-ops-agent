# REASONING — Case 001

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (note, informational), event-002 (note, informational), event-003 (note, informational), event-004 (email, informational), event-005 (note, informational), event-006 (note, informational), event-007 (email, untrusted), event-008 (note, informational), event-009 (email, informational), event-010 (note, informational), event-011 (email, untrusted), event-012 (note, informational), event-013 (email, informational), event-014 (note, informational), event-015 (email, untrusted), event-016 (note, informational), event-017 (email, informational), event-018 (note, informational), event-019 (note, informational), event-020 (note, informational), event-021 (note, informational), event-022 (email, untrusted), event-023 (email, informational), event-024 (note, informational), event-025 (email, informational), event-026 (email, untrusted), event-027 (email, informational), event-028 (note, informational), event-029 (email, untrusted), event-030 (note, informational), event-031 (email, informational), event-032 (note, informational), event-033 (note, informational), event-034 (note, informational), event-035 (note, informational), event-036 (note, informational), event-037 (note, informational), event-038 (note, informational), event-039 (call_transcript, informational), event-040 (note, informational), event-041 (call_transcript, informational), event-042 (call_transcript, informational), event-043 (note, informational), event-044 (note, informational)

Facts and their sources:
- F1 [high] Tenant of Flat 26, 46 Copperfield Walk reported on 10 Oct 2025: communal garden full of weeds, hedge along the side path overgrown, and a strip of land at the side not cleared as expected last summer. ← index, event-001
- F2 [high] Intake categorised the issue as External & Communal, severity ROUTINE; one cat at the property; no access codes or alarms. ← event-002
- F3 [high] The landlord's own message confirmed quotes received from Riverside Services and gave the go-ahead for the garden works. ← event-022, event-026
- F4 [high] The contractor is the landlord's own (Riverside Services, contact Freya); the landlord arranged the booking and the start date directly. ← event-023, event-026, event-033
- F5 [high] Tenant was told on 5 Nov 2025 that Riverside Services had been instructed and on 6 Nov 2025 that works were hoped to start around 19 Nov 2025; work actually started 20 Nov 2025 and was delayed by a pigeon nest in a tree to be trimmed. ← event-025, event-031, event-033, event-037
- F6 [high] On 11 Dec 2025 the contractor confirmed by phone that the job (including tree removal) is complete and will be invoiced to the landlord; the agency recorded the task as completed without payment. ← event-042, event-043, event-044
- F7 [high] No landlord confirmation of completion and no photos or invoice are on the case file. ← get_case_details, get_action_ledger
- F8 [high] No hazard, vulnerability, liability dispute or spend by the agency arises on this case; the work is grounds maintenance funded by the landlord. ← event-002, event-043

Conflicts and how they were handled:
- An internal hold note says the works are 'an external job for the development and not for the tenants so no contact needed' (event-036), while the agency had already promised the reporting tenants updates (event-023, event-025, event-031). → The express promise to the tenant stands; the tenant has now been told the works are reported complete (ACT-1). No decision changed for the landlord or contractor. (source_hierarchy; sources event-023, event-025, event-031, event-036)
- Caller identified as 'Leo from Juniper Homes' (event-039) although the agency of record is Northbridge Lettings; landlord emails carry third-party names (Grace Nolan, Harper, Felix Kendall) inconsistent with the landlord addressed as Rowan elsewhere. → Treated as summarisation noise in untrusted/auto-summarised records; the property and parties on the agency's own record (get_case_details) were used, and no name from a message body was copied into another party's letter. Recorded as a data-quality red flag, not acted on. (tool_check; sources event-007, event-022, event-039)

Uncertainty acknowledged:
- No quote amount or VAT figure is anywhere on file — the landlord contracted Riverside Services directly, so the agency never held the price.
- Whether the 'no man's land' strip at the side of the property was within the contractor's scope is unknown.

Assumptions made:
- Assumption: the 'tree removal' discussed at event-042 forms part of the same communal garden instruction rather than a separate job; the tenant has been asked to verify the reported scope rather than this being treated as settled.

## Why this disposition

Disposition: **needs_info**. No dispatch or spend by the agency: the landlord approved the works in his own words (event-022, event-026) and used his own contractor, Riverside Services, paying direct (event-043, event-044). The provider confirmed completion by phone (event-042). I kept the outstanding promise to the tenant by telling them the works are reported complete and asking them to flag anything left (ACT-1), asked the landlord to confirm completion and the document position (ACT-2), logged the review and the data-quality discrepancies (ACT-3) and placed the ticket on hold pending the landlord (ACT-4). I did not close: landlord confirmation and the documents/skip reason are still open, and only the landlord and tenant can settle them.
Authority relied on: CAP-NOTIFY, CAP-LOG, RTE-LANDLORD, RTE-TENANT, CAP-CLOSE, PRO-INSTRUCTIONS-FROM-CONTENT, PRO-PAYMENTS.
Red flags shaped the decision: data_quality: Several agency emails and call notes contain placeholder property strings ('synthetic-bca83b5565b3', 'synthetic-f00fcbada17f', 'synthetic-eae38b44a3ac') instead of the address, and landlord emails are auto-summaries naming people inconsistently with the case record.; other: Scope verification gap: the only contractor completion detail on file is a call summary about 'removing a tree' (event-042), which does not evidence the weeds, side-path hedge or side strip the tenant reported.

## Timeline

- 13:17:57.344 model turn 1 → tool_use
- 13:17:57.344 playbook maintenance-request · type maintenance_request · urgency routine
- 13:17:57.345 gate get_case_details → allow (read)
- 13:17:57.345 get_case_details → completed (attempts 1)
- 13:17:57.345 gate get_action_ledger → allow (read)
- 13:17:57.345 get_action_ledger → completed (attempts 1)
- 13:18:28.429 model turn 2 → tool_use
- 13:18:28.431 gate notify_tenant → allow (CAP-NOTIFY)
- 13:18:28.431 notify_tenant → completed (attempts 1)
- 13:18:28.431 gate notify_landlord → allow (CAP-NOTIFY)
- 13:18:28.431 notify_landlord → completed (attempts 1)
- 13:18:28.431 gate add_note → allow (CAP-LOG)
- 13:18:28.431 add_note → completed (attempts 1)
- 13:18:32.942 model turn 3 → tool_use
- 13:18:32.943 gate put_on_hold → allow (CAP-LOG)
- 13:18:32.943 put_on_hold → completed (attempts 1)
- 13:19:26.770 model turn 4 → tool_use
- 13:19:26.771 terminal request_info → accepted

Steps used: 4; tokens in/out: 45734/7233 (cache reads 56352); model: claude-opus-5.
