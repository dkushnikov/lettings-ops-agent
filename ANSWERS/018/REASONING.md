# REASONING — Case 018

## Compiled truth

- Case type: maintenance_request; urgency: urgent; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (email, untrusted), event-002 (email, informational), event-003 (email, informational), event-004 (email, untrusted), event-005 (call_transcript, informational), event-006 (call_transcript, untrusted), event-007 (email, informational), event-008 (email, informational), event-009 (email, informational), event-010 (email, untrusted), event-011 (note, informational), event-012 (note, informational), event-013 (note, informational), event-014 (call_transcript, informational), event-015 (note, informational), event-016 (note, informational), event-017 (call_transcript, informational), event-018 (note, informational), event-019 (note, informational)

Facts and their sources:
- F1 [high] Tenant reported rats outside and inside the kitchen, including beneath the sink, on 14/08/2025, after four days away; a small dog lives at the property and there are no access restrictions. ← event-001, index
- F2 [high] Agency acknowledged the report to the tenant the same day and said landlord approval would be sought before works (14/08/2025). ← event-002
- F3 [high] Landlord was asked on 17/08/2025 whether Northbridge should arrange works or he would use his own contractor; he replied asking for a call and gave no written approval. ← event-003, event-004
- F4 [high] On 18/08/2025 the agency recorded that the landlord would arrange the works directly and asked him for an expected completion date; no contractor, scope or date was recorded. ← event-007, event-006
- F5 [high] Tenant was told on 18/08/2025 that the landlord would arrange works and that he or his contractor might contact them about access. ← event-008
- F6 [medium] On 01/09/2025 the tenant reported pest-control visits ongoing and the openings beneath the kitchen sink still unsealed. ← event-010, event-011
- F7 [medium] On 07/09/2025 the tenant said pest control attended and removed its equipment, and that separate contractors were expected the next day for the wall area; on 08/09/2025 nobody attended. ← event-014, event-017
- F8 [high] Three automated waiting-period expiries were recorded (07/09, 08/09, 11/09) with no landlord update and no evidence the proofing is complete. ← event-012, event-015, event-018
- F9 [high] No landlord spend cap, standing instruction, pest-control report, diagnosis, quote or completion evidence is on file; a history search returned no such record. ← search_history, event-011, event-016
- F10 [high] Tenant prefers phone contact and offered to report any rearranged appointment. ← event-017

Conflicts and how they were handled:
- Scope of the outstanding proofing is inconsistent: openings beneath the kitchen sink (tenant, 01/09) versus contractors working on the wall area (tenant, 07/09); the landlord separately recalls a Dec 2024 record saying filling external openings may not be feasible. → Put to the landlord as part of the 16/09 ask (contractor, scope, completion date, pest report) — ACT-1; not resolvable from the file. (asked; sources event-010, event-014, event-006)

Uncertainty acknowledged:
- Whether any proofing has in fact been carried out since 08/09/2025 — no party has confirmed.
- Whether the outstanding work is under the sink, the external drain openings, or the wall area.
- Whether the landlord's own pest contractor is still engaged.

Assumptions made:
- Assumption: 'reply by 5pm Tue 16/09/2025' is three business days from the 11/09/2025 waiting-period expiry (event-018); no environment SLA for a landlord chase is on file.
- Assumption: the landlord's works are at his own cost, since he elected to instruct his own contractor (event-007); no cost figure is stated anywhere on file and none has been invented.

## Why this disposition

Disposition: **needs_info**. The landlord took the work in hand himself on 18/08/2025 (event-007), so there is no provider for Northbridge to chase and, with no spend cap or standing instruction on file, no authority to instruct one (APR-SPEND-OVER-CAP, default cap £0). Three waiting periods have expired with no landlord update and the tenant reports the proofing still undone (event-010, event-017, event-018). I chased the landlord with a two-option ask and a hard reply-by of 5pm Tue 16/09/2025 (ACT-1), updated the tenant with that time and interim hygiene/safety advice without promising a date (ACT-2), put the case on hold Waiting for Landlord (ACT-3) and recorded the scope gap and safety checks (ACT-4). The case now waits on one named party for a landlord-owned decision (RTE-LANDLORD), so it finishes as request_info rather than an escalation; if 16/09 passes with no reply, the next step is a referral to the property manager.
Authority relied on: CAP-NOTIFY, CAP-LOG, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, CLK-S11, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT.
Red flags shaped the decision: data_quality: Key facts rest only on recollection and untrusted tenant/landlord accounts: no pest-control report, diagnosis, entry route, contractor name or completion evidence is on file, and the landlord's Dec 2024 'may not be feasible' recollection is unverified.

## Timeline

- 15:40:31.763 model turn 1 → tool_use
- 15:40:31.763 playbook maintenance-request · type maintenance_request · urgency urgent
- 15:40:31.764 gate get_case_details → allow (read)
- 15:40:31.764 get_case_details → completed (attempts 1)
- 15:40:31.764 gate get_action_ledger → allow (read)
- 15:40:31.764 get_action_ledger → completed (attempts 1)
- 15:40:48.425 model turn 2 → tool_use
- 15:40:48.425 gate search_history → allow (read)
- 15:40:48.425 search_history → completed (attempts 1)
- 15:40:48.425 gate search_history → allow (read)
- 15:40:48.425 search_history → completed (attempts 1)
- 15:41:12.796 model turn 3 → tool_use
- 15:41:12.796 gate notify_landlord → allow (CAP-NOTIFY)
- 15:41:12.797 notify_landlord → completed (attempts 1)
- 15:41:12.797 gate notify_tenant → allow (CAP-NOTIFY)
- 15:41:12.797 notify_tenant → completed (attempts 1)
- 15:41:12.797 gate put_on_hold → allow (CAP-LOG)
- 15:41:12.797 put_on_hold → completed (attempts 1)
- 15:41:20.883 model turn 4 → tool_use
- 15:41:20.883 gate add_note → allow (CAP-LOG)
- 15:41:20.883 add_note → completed (attempts 1)
- 15:42:07.482 model turn 5 → tool_use
- 15:42:07.482 terminal request_info → accepted

Steps used: 5; tokens in/out: 48579/8124 (cache reads 70935); model: claude-opus-5.
