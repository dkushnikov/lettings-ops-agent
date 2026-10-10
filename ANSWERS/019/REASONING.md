# REASONING — Case 019

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (note, informational), event-002 (note, informational), event-003 (email, informational), event-004 (email, informational), event-005 (note, informational), event-006 (note, informational), event-007 (note, informational), event-008 (note, informational), event-009 (note, informational), event-010 (note, informational), event-011 (note, informational), event-012 (email, informational), event-013 (note, informational), event-014 (note, informational), event-015 (note, informational), event-016 (note, informational), event-017 (note, informational), event-018 (note, informational), event-019 (email, informational), event-020 (note, informational), event-021 (note, informational), event-022 (email, informational), event-023 (note, informational), event-024 (note, informational), event-025 (email, untrusted), event-026 (note, informational), event-027 (note, informational), event-028 (note, informational), event-029 (email, informational), event-030 (note, informational), event-031 (note, informational), event-032 (note, informational), event-033 (note, informational), event-034 (note, informational), event-035 (note, informational), event-036 (note, informational), event-037 (note, informational), event-038 (email, informational), event-039 (note, informational), event-040 (note, informational), event-041 (note, informational), event-042 (note, informational), event-043 (note, informational), event-044 (note, informational)

Facts and their sources:
- F1 [high] Tenant requested rubbish/construction-waste removal, ground levelling, gravel covering and making the garden safe at Flat 25, 185 Copperfield Walk on 17 Jan 2025. ← index, event-001, get_case_details
- F2 [high] The agency's own process flagged that landlord approval was required before provider selection. ← event-002, event-005
- F3 [high] The only landlord message in the history approving work is 'Please go ahead with the removal' (25 Mar 2025); it names no amount and covers removal only. ← event-025
- F4 [high] The agency told the landlord the disposal quote would be around £600 because the material left in the garden is a specialised builders' material needing proper disposal. ← event-019
- F5 [medium] An earlier internal note records a different figure and provider: £500+VAT approved, Harbour Compliance going ahead. ← event-009
- F6 [high] The invoice came by email from a new provider with no portal access, so no work order was raised in the system. ← event-033
- F7 [high] Tenant was offered two attendance days on 9 Apr 2025 and the clearance was recorded as done on 12 Apr 2025. ← event-029, event-031
- F8 [high] Invoice was emailed to the landlord on 16 Apr 2025 with a statement that it would be deducted from the rental amount; the invoice attachment is unavailable. ← event-038, get_attachment
- F9 [high] Document upload was skipped with reason 'not applicable'; no provider work-result report or photos are on file. ← event-042
- F10 [high] The file recorded 'Need confirmation from landlord' at 09:15 and was closed as 'All checks have been completed' at 09:16 on 16 Apr 2025, with no landlord confirmation in between. ← event-043, event-044
- F11 [medium] No landlord standing spend cap is on file in this case record, so there is no standing authority for further spend. ← get_case_details, CAP-DISPATCH-ROUTINE
- F12 [high] The tenant chased for an update on 13 Mar 2025 and was never sent the outcome of the completed clearance before this review. ← event-018, event-029

Conflicts and how they were handled:
- Provider and amount disagree across agency records: £500+VAT with Harbour Compliance (event-009) vs c.£600 with Oakley's contractor (event-019) vs an unnamed new off-portal provider who invoiced (event-033). → Not decided by me. Conflict recorded and referred to the office via human task ACT-3; no provider named to any party in my messages. (asked; sources event-009, event-019, event-033)
- Closure status conflicts with the final-checks record: landlord confirmation was outstanding (event-043) yet the request was closed as fully checked (event-044). → Landlord asked to confirm completion (ACT-2); ticket placed on hold (ACT-5) rather than left closed. (asked; sources event-043, event-044)
- Scope conflict: the approved and completed work covers removal only (event-025, event-031), while the tenant's request also covered levelling and gravel (event-001). → Landlord asked whether to quote for levelling/gravel; tenant told those items are not approved and nothing is booked. (asked; sources event-001, event-025, event-031)

Uncertainty acknowledged:
- The invoiced amount and the identity of the attending contractor cannot be established: the invoice attachment is unavailable and the records conflict (event-009, event-019, event-033).
- Whether the landlord accepted the rent-deduction method announced at event-038 is unknown.
- Whether the garden is now safe and usable as the tenant asked is unverified — no photos or provider result on file (event-042).

Assumptions made:
- Assumption: no landlord standing spend cap exists for this property, since none appears in the case record; on that basis any further spend needs the landlord's priced approval.
- Assumption: the clearance element was in fact carried out, based on the agency's own note (event-031) and the invoice email (event-038); no provider report or photo evidence exists to verify it.

## Why this disposition

Disposition: **escalated**. The clearance element was approved by the landlord (event-025) and carried out (event-031, event-038), but the file was closed at event-044 one minute after event-043 recorded "Need confirmation from landlord", with no landlord confirmation, no provider work result, and the tenant's levelling/gravel items never quoted, decided or answered. I did not instruct any contractor — there is no landlord cap on file and no priced approval for further work (APR-SPEND-OVER-CAP). I updated the tenant, put the two open questions to the landlord with a 3-working-day reply-by, raised a human task for the provider/amount conflict and the rent-deduction entry, and put the ticket on hold pending the landlord's reply.
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, ESC-CONFLICT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11.
Red flags shaped the decision: data_quality: Request closed as 'all checks completed' one minute after a note saying landlord confirmation was still needed; no work-result report, no photos, invoice attachment unavailable.; other: Agency message states the invoice would be processed and 'deduct[ed] off the rental amount' — money movement sits outside the agent mandate (PRO-PAYMENTS).; safety_hazard: Waste described as 'a specialised builders material that needs disposing of properly' (quoted, untrusted-origin relay); no asbestos or other hazard is named anywhere in the artefacts and the tenant reported no injury. Garden surface still un-levelled, so the tenant was asked to report anything left unsafe.

## Timeline

- 13:22:47.347 model turn 1 → tool_use
- 13:22:47.347 playbook maintenance-request · type maintenance_request · urgency routine
- 13:22:47.348 gate get_case_details → allow (read)
- 13:22:47.348 get_case_details → completed (attempts 1)
- 13:22:47.348 gate get_action_ledger → allow (read)
- 13:22:47.348 get_action_ledger → completed (attempts 1)
- 13:23:02.227 model turn 2 → tool_use
- 13:23:02.227 gate search_history → allow (read)
- 13:23:02.227 search_history → completed (attempts 1)
- 13:23:02.227 gate get_attachment → allow (read)
- 13:23:02.227 get_attachment → completed (attempts 1)
- 13:23:33.524 model turn 3 → tool_use
- 13:23:33.524 gate notify_tenant → allow (CAP-NOTIFY)
- 13:23:33.524 notify_tenant → completed (attempts 1)
- 13:23:33.524 gate notify_landlord → allow (CAP-NOTIFY)
- 13:23:33.524 notify_landlord → completed (attempts 1)
- 13:23:33.524 gate create_human_task → allow (CAP-HUMAN-TASK)
- 13:23:33.524 create_human_task → completed (attempts 1)
- 13:23:33.525 gate add_note → allow (CAP-LOG)
- 13:23:33.525 add_note → completed (attempts 1)
- 13:23:39.981 model turn 4 → tool_use
- 13:23:39.982 gate put_on_hold → allow (CAP-LOG)
- 13:23:39.983 put_on_hold → completed (attempts 1)
- 13:24:56.005 model turn 5 → tool_use
- 13:24:56.007 terminal request_info → accepted

Steps used: 5; tokens in/out: 59486/8792 (cache reads 70440); model: claude-opus-5.

## Reviewer notes

- R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
