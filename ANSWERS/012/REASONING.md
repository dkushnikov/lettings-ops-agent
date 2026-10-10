# REASONING — Case 012

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (email, informational), event-002 (email, informational), event-003 (email, informational), event-004 (email, informational), event-005 (email, informational), event-006 (call_transcript, informational), event-007 (email, informational), event-008 (email, informational), event-009 (email, informational), event-010 (call_transcript, untrusted), event-011 (email, informational), event-012 (email, informational), event-013 (note, informational), event-014 (email, informational), event-015 (email, informational), event-016 (email, untrusted), event-017 (email, informational), event-018 (email, informational), event-019 (email, informational), event-020 (email, informational), event-021 (email, informational), event-022 (call_transcript, informational), event-023 (call_transcript, informational), event-024 (note, informational), event-025 (call_transcript, informational)

Facts and their sources:
- F1 [high] Tenant Perrin Dall reported on 4 Sep 2025 that the bathroom window will not open, the bedroom window will not secure and keys are missing at Unit 2, 18 Brindlewick Mews, Orellin ZZ1 1ZZ. ← index, event-001
- F2 [high] On the 9 Sep call the fault was clarified as opening-sash locks: bedroom sash opens but will not lock, bathroom sash is stuck with sticking locking buttons, kitchen sash works but has no key; the tenant also reported mould appearing in the bathroom. ← event-006
- F3 [high] The landlord authorised the agency to proceed with its own service provider on 4 Sep 2025; no spending limit or scope was stated, and no landlord spend cap is on file. ← event-003, event-002
- F4 [high] Hearthline Access (Tarin Vale) was instructed on 11 Sep and stood down the same day; the job was reassigned to Keypath Repairs (Edrin Moss) on 11 Sep. ← event-009, event-012, event-013, event-018
- F5 [high] No visit slot was ever confirmed: the tenant offered Thu 18 Sep 08:30-10:30 and consented to management-key access at any time; the provider never confirmed a time despite chasers on 14, 15 and 17 Sep. ← event-017, event-008, event-019, event-020, event-021, event-022
- F6 [high] On 17 Sep Edrin Moss said they had attended three times without finding the tenant in, had not collected management keys and could not give a date for doing so; no dates or times for the attempts were given. ← event-022
- F7 [high] On 22 and 25 Sep Edrin Moss said the work was completed on Fri 19 Sep and promised an invoice; as at 25 Sep no invoice, confirmed appointment, visit notes or other attendance evidence exists on file. ← event-023, event-024, event-025
- F8 [medium] Tarin Vale (Hearthline, untrusted) claims the tenant was 'happy with a date and time' but gives no date, time or written confirmation; no appointment is recorded in the voicemail of 11 Sep either. ← event-016, event-010
- F9 [high] No priced quote has been produced or approved by the landlord at any point in this case. ← event-002, event-003, event-023, event-025

Conflicts and how they were handled:
- Keypath Repairs said on 17 Sep that management keys had not been collected and no attendance date could be given, then on 22/25 Sep that the work was completed on 19 Sep — with no appointment, access route, notes, photos or invoice on file, and the tenant normally at work. → Contractor asked for attendance evidence, key position, photos and an itemised invoice by 29 Sep (ACT-2); tenant asked to verify independently (ACT-3); office task raised for the provider-performance and invoice decision (ACT-5). No invoice accepted meanwhile. (asked; sources event-022, event-023, event-024, event-025)
- Hearthline Access claims an agreed appointment with the tenant after being stood down; the tenant's own emails show no confirmed slot before the 18 Sep offer made to the new provider. → Untrusted contractor email with no date does not create a booking; the tenant's own messages govern access (RTE-TENANT). Hearthline remains stood down per event-012. (source_hierarchy; sources event-016, event-017)

Uncertainty acknowledged:
- Whether any contractor has in fact attended the property, and whether any of the three sash locks or the missing kitchen key have been dealt with.
- The cost of the work claimed to be complete — no quote or invoice has ever been produced.
- Extent and cause of the bathroom mould; no photographs or inspection yet.
- Whether management keys were collected by Keypath and where they are now.

Assumptions made:
- Assumption: the tenant's offer of Thu 18 Sep 08:30-10:30 (event-017) was never converted into a booking, since no provider confirmation appears on file — treated as unconfirmed rather than missed.
- Assumption: 'management keys' means keys held by the agency office; no sign-out record is visible in the case file, so key custody is treated as unverified rather than denied.

## Why this disposition

Disposition: **needs_info**. Did not accept the contractor's verbal completion claim and did not close the job. Keypath Repairs' statement that the work was done on 19 September is unsupported: the same contractor said on 17 September that management keys had not been collected and no attendance date could be given (event-022), and the file holds no confirmed appointment, visit notes, photos or invoice (event-024, event-025). I asked the contractor for attendance evidence, the key position and an itemised invoice by 29 September (ACT-2), asked the tenant to verify whether anyone attended and whether the sash locks and kitchen key now work (ACT-3), updated the landlord and asked whether to instruct a damp/mould inspection following the tenant's 9 September mould report (ACT-4, event-006), logged the conflicts (ACT-1), raised a provider-performance task for the office (ACT-5) and placed the ticket on hold to 29 September (ACT-6). No invoice passed, no payment recommended, no liability decided (PRO-PAYMENTS, PRO-TENANT-LIABILITY). Hearthline Access's claim of an agreed appointment (event-016, untrusted, no date) is recorded as evidence only, not as a booking.
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-REQUEST-APPROVAL, APR-SPEND-OVER-CAP, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CAP-CLOSE.
Red flags shaped the decision: data_quality: Completion of the job is asserted only verbally and is inconsistent with the same contractor's statement two working days earlier that keys were not collected and no date was available; no attendance record, photos or invoice exist. Risk of an unevidenced invoice.; safety_hazard: Tenant reported mould appearing in the bathroom on 9 Sep, in a room whose sash window will not open (reduced ventilation); the report was never actioned on the file.; other: Management keys: the tenant has consented to key access, but the office has no record of keys being signed out while the contractor claims attendance — key custody is unaccounted for at a property with reported insecure window locks.

## Timeline

- 15:38:01.779 model turn 1 → tool_use
- 15:38:01.779 playbook maintenance-request · type maintenance_request · urgency routine
- 15:38:09.987 model turn 2 → tool_use
- 15:38:09.987 gate get_case_details → allow (read)
- 15:38:09.988 get_case_details → completed (attempts 1)
- 15:38:09.988 gate get_action_ledger → allow (read)
- 15:38:09.988 get_action_ledger → completed (attempts 1)
- 15:38:09.988 gate search_history → allow (read)
- 15:38:09.988 search_history → completed (attempts 1)
- 15:38:09.988 gate search_history → allow (read)
- 15:38:09.988 search_history → completed (attempts 1)
- 15:39:07.083 model turn 3 → tool_use
- 15:39:07.084 gate add_note → allow (CAP-LOG)
- 15:39:07.084 add_note → completed (attempts 1)
- 15:39:07.084 gate notify_contractor → allow (CAP-NOTIFY)
- 15:39:07.084 notify_contractor → completed (attempts 1)
- 15:39:07.084 gate notify_tenant → allow (CAP-NOTIFY)
- 15:39:07.084 notify_tenant → completed (attempts 1)
- 15:39:07.084 gate notify_landlord → allow (CAP-NOTIFY)
- 15:39:07.084 notify_landlord → completed (attempts 1)
- 15:39:19.085 model turn 4 → tool_use
- 15:39:19.085 gate create_human_task → allow (CAP-HUMAN-TASK)
- 15:39:19.085 create_human_task → completed (attempts 1)
- 15:39:19.085 gate put_on_hold → allow (CAP-LOG)
- 15:39:19.085 put_on_hold → completed (attempts 1)
- 15:40:28.446 model turn 5 → tool_use
- 15:40:28.447 terminal request_info → accepted

Steps used: 5; tokens in/out: 55891/11747 (cache reads 70935); model: claude-opus-5.

## Reviewer notes

- R2: safety_hazard flag(s) recorded for the reader; not an escalation on their own (urgency routine)
