# REASONING — Case 021

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (note, informational), event-002 (note, informational), event-003 (email, informational), event-004 (note, informational), event-005 (note, informational), event-006 (email, untrusted), event-007 (email, informational), event-008 (note, informational), event-009 (note, informational), event-010 (note, informational), event-011 (email, informational), event-012 (email, informational), event-013 (email, untrusted), event-014 (note, informational), event-015 (email, untrusted), event-016 (email, informational), event-017 (note, informational), event-018 (email, informational), event-019 (note, informational), event-020 (email, untrusted), event-021 (email, informational), event-022 (note, informational), event-023 (note, informational), event-024 (note, informational), event-025 (note, informational), event-026 (note, informational), event-027 (note, informational), event-028 (note, informational), event-029 (note, informational)

Facts and their sources:
- F1 [high] Property is Flat 22, 148 Lantern Quay, Westmarsh, ZZ4 1ZZ; tenant on the brief is Clara Jenkins. ← index, get_case_details, event-011
- F2 [high] Fault reported 21/11/2024: key snapped in the conservatory back door; no spare held by the tenant or the agency. Scope: replace the lock and supply 4 keys (2 tenant, 1 office, 1 landlord). ← event-001, event-003, index
- F3 [high] Landlord's own email approves the works and the new key sets. ← event-006
- F4 [high] Provider Alder Compliance was assigned and briefed; tenant was told who would attend. ← event-010, event-011, event-012
- F5 [high] No visit slot was ever confirmed in the history; the provider went from acknowledging the chase to reporting the job complete. ← event-018, event-020
- F6 [medium] Provider reported the job complete — cylinder and handles replaced — and said remaining keys would be dropped to the office the next day. ← event-020
- F7 [high] No quote, cost figure or invoice appears anywhere in the case; documents were skipped with reason 'No quote required, repaired on site'. ← event-025, search_history
- F8 [high] System flagged 'Need confirmation from landlord' (event-026); no landlord reply follows before the request was closed at event-029. ← event-026, event-029
- F9 [high] 'Keys return confirmed' was recorded at event-028 with no delivery receipt, 16 minutes of system time after the skip note and the day after the provider's promise. ← event-028, event-020
- F10 [medium] Nothing in the case matches an emergency definition: the fault is a snapped key to a conservatory back door, the property is not reported insecure, and no hazard, vulnerability or essential-service loss is mentioned. ← event-001, event-003

Conflicts and how they were handled:
- Agency records disagree on whether the office and landlord key sets have been returned: event-028 states 'Keys return confirmed' while the only underlying evidence is the provider's promise at event-020 to deliver them 'tomorrow'. → Provider asked for the handover date; office asked to check the key log (ACT-2, ACT-5). Not asserted either way to any party. (asked; sources event-020, event-028)
- Tenant contact number differs between agency messages: 07700 900625 in the brief and reminder, 07700 900336 in the number sent to the provider. → Recorded and sent to the office queue (ACT-5); no number repeated to any party. (unresolved; sources event-012, event-016, event-018)

Uncertainty acknowledged:
- Whether the office and landlord key sets were actually delivered on 23/11 is unknown — no receipt on file.
- The cost of the works is unknown; no figure has ever been stated, so who pays cannot be named in a resolution.
- No tenant confirmation that the new lock operates correctly; completion rests on the provider's own untrusted email (event-020).

Assumptions made:
- Assumption: the conservatory back door is not the property's only secure external access, since neither tenant nor agency raised security at any point (event-001, event-003); if that is wrong the urgency would rise.

## Why this disposition

Disposition: **needs_info**. The job itself is done and authorised, but the automation closed the ticket (event-029) with three definition-of-done items unevidenced: no invoice or cost on file, no landlord confirmation of completion, and a "Keys return confirmed" flag (event-028) backed only by the provider's promise to deliver the keys the next day (event-020). I did not re-close or re-dispatch. I logged the gap, chased the provider for the invoice and a key-handover confirmation, asked the landlord to confirm completion, asked the tenant to confirm the door locks and how many keys were left, and sent the premature-closure/key-log conflict to the office queue. The case now waits on named parties, so it finishes as request_info rather than an escalation.
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, RTE-CONTRACTOR, RTE-TENANT, ESC-CONFLICT, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK.
Red flags shaped the decision: data_quality: Request closed as 'All checks have been completed' while invoice, landlord confirmation and key-return evidence were all missing; closure note names no payer.; data_quality: Agency emails to the provider are addressed 'Hi Clara' / 'Good morning Clara' — Clara Jenkins is the tenant, not the provider; names in message bodies are unreliable.; other: Landlord approval at event-006 is a third-person summary ('Quinn approves the maintenance action'), not a first-person reply, and carries no price.

## Timeline

- 13:23:25.822 model turn 1 → tool_use
- 13:23:25.822 playbook maintenance-request · type maintenance_request · urgency routine
- 13:23:25.822 gate get_case_details → allow (read)
- 13:23:25.822 get_case_details → completed (attempts 1)
- 13:23:25.823 gate get_action_ledger → allow (read)
- 13:23:25.823 get_action_ledger → completed (attempts 1)
- 13:23:50.583 model turn 2 → tool_use
- 13:23:50.584 gate search_history → allow (read)
- 13:23:50.584 search_history → completed (attempts 1)
- 13:23:50.584 gate get_attachment → allow (read)
- 13:23:50.584 get_attachment → completed (attempts 1)
- 13:24:19.613 model turn 3 → tool_use
- 13:24:19.614 gate add_note → allow (CAP-LOG)
- 13:24:19.614 add_note → completed (attempts 1)
- 13:24:19.614 gate notify_contractor → allow (CAP-NOTIFY)
- 13:24:19.614 notify_contractor → completed (attempts 1)
- 13:24:19.614 gate notify_tenant → allow (CAP-NOTIFY)
- 13:24:19.614 notify_tenant → completed (attempts 1)
- 13:24:19.615 gate notify_landlord → allow (CAP-NOTIFY)
- 13:24:19.615 notify_landlord → completed (attempts 1)
- 13:24:19.615 gate create_human_task → allow (CAP-HUMAN-TASK)
- 13:24:19.615 create_human_task → completed (attempts 1)
- 13:25:16.535 model turn 4 → tool_use
- 13:25:16.536 terminal request_info → accepted

Steps used: 4; tokens in/out: 37659/8892 (cache reads 56352); model: claude-opus-5.
