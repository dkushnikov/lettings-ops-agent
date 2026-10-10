# REASONING — Case 014

## Compiled truth

- Case type: maintenance_request; urgency: routine; playbook: maintenance-request
- Received artefacts: index (record, authoritative), event-001 (note, informational), event-002 (note, informational), event-003 (note, informational), event-004 (note, informational), event-005 (email, informational), event-006 (email, informational), event-007 (note, informational), event-008 (note, informational), event-009 (email, untrusted), event-010 (note, informational), event-011 (call_transcript, informational), event-012 (note, informational), event-013 (email, informational), event-014 (note, informational), event-015 (note, informational), event-016 (email, untrusted)

Facts and their sources:
- F1 [high] Tenant reported the front door has to be slammed to shut and that the fridge-freezer contractor said it would "cause a shatter in glass" and would report it himself. ← index, event-001
- F2 [high] Follow-up call recorded that the door frame and door "literally wobble" when shutting. ← event-004
- F3 [high] Agency asked the landlord for authority to send someone out and placed the case on hold waiting for the landlord. ← event-005, event-007
- F4 [high] Landlord replied with a zero-cost workaround — put the key in to lift the latch, then close the door — and asked that a contractor look at it next month. ← event-010
- F5 [high] The workaround was relayed to the tenant by phone; she had already used it that morning, it worked, and she agreed to monitor and report any recurrence. ← event-011, event-012
- F6 [high] The landlord was updated that the workaround succeeded and the case would be closed, and he acknowledged; the request was marked completed without payment. ← event-013, event-015, event-016
- F7 [medium] No landlord standing spend cap is on file in this case record, so there is no standing authority to spend. ← get_case_details
- F8 [medium] The door can be closed and secured using the landlord's method; no report of the property being left insecure. ← event-012

Conflicts and how they were handled:
- AI intake classified the issue as "Appliances" and asked fridge/freezer clarifying questions, while the tenant's text and all later events describe a front door fault. → The tenant's own words and the agency's follow-up note govern: the case is a front door repair, classified routine. Noted at ACT-1. (source_hierarchy; sources event-002, event-001, event-004)
- Untrusted landlord-channel email (event-009) is a third-person system summary mentioning a workaround and a visit next month; the landlord's actual words appear at event-010. → Acted on the landlord's own message (event-010); the summary line was treated as evidence only. (source_hierarchy; sources event-009, event-010)

Uncertainty acknowledged:
- Whether the key/latch method is a durable fix or masks a worsening frame fault; only monitoring will show.
- Whether the fridge-freezer contractor's separate report (index, event-005) contains detail beyond the tenant's account — no contractor message is in the visible history.
- No tenancy or occupant record was available in this environment, so no vulnerability factors could be checked.

Assumptions made:
- Assumption: the landlord's "next month" (event-010, sent 2024-06-07) means July 2024; the diary task is raised on that basis and asks the office to confirm with the landlord.
- Assumption: no landlord standing spend cap exists for this property, since none appears in the case record; if one is on file in the CRM it does not change the outcome, as the landlord deferred the work rather than requesting it.

## Why this disposition

Disposition: **escalated**. No response to the landlord is required and no contractor is instructed. The landlord owns this decision and has already made it: a zero-cost workaround now (event-010), with a contractor inspection deferred to next month. The workaround was relayed to the tenant and confirmed working (event-011, event-012); the landlord was updated (event-013) and acknowledged (event-016). The agency completed the request without payment (event-015). I added the missing pieces within my authority: the tenant has been told a visit is intended but not yet booked and given the triggers that would make it urgent (ACT-2), and the landlord's July inspection promise has been diarised to the office so it is not lost (ACT-3). I did not dispatch: no standing spend cap is on file and the landlord's message defers the work rather than approving a priced job (APR-SPEND-OVER-CAP).
Authority relied on: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK.
Red flags shaped the decision: data_quality: Intake misclassification: issue logged as "Appliances" with fridge/freezer questions (all unanswered) for what is a front door fault; risk of the job being routed to the wrong trade.; safety_hazard: A contractor's reported view, quoted by the tenant, that the wobbling door could "cause a shatter in glass"; the inspection is deferred by a month. Not an emergency — the door still closes and locks using the landlord's method (event-012) — but a residual risk while deferred.

## Timeline

- 13:21:19.210 model turn 1 → tool_use
- 13:21:19.211 playbook maintenance-request · type maintenance_request · urgency routine
- 13:21:19.211 gate get_case_details → allow (read)
- 13:21:19.211 get_case_details → completed (attempts 1)
- 13:21:58.310 model turn 2 → tool_use
- 13:21:58.310 gate add_note → allow (CAP-LOG)
- 13:21:58.311 add_note → completed (attempts 1)
- 13:21:58.311 gate notify_tenant → allow (CAP-NOTIFY)
- 13:21:58.311 notify_tenant → completed (attempts 1)
- 13:21:58.311 gate create_human_task → allow (CAP-HUMAN-TASK)
- 13:21:58.311 create_human_task → completed (attempts 1)
- 13:22:43.621 model turn 3 → tool_use
- 13:22:43.622 terminal finalize → accepted

Steps used: 3; tokens in/out: 19814/6950 (cache reads 42264); model: claude-opus-5.

## Reviewer notes

- R2: red flags (safety_hazard) → escalated (checked before any needs_info rule)
