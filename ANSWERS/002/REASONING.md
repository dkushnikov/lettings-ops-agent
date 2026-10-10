# REASONING — Case 002

## Compiled truth

- Case type: compliance_expiry; urgency: urgent; playbook: compliance-expiry
- Received artefacts: index (record, authoritative), event-001 (email, untrusted), event-002 (note, informational), event-003 (email, untrusted), event-004 (email, informational), event-005 (email, untrusted), event-006 (email, untrusted), event-007 (email, untrusted), event-008 (email, untrusted), event-009 (note, untrusted), event-010 (email, untrusted), event-011 (note, untrusted), event-012 (email, untrusted), event-013 (note, informational), event-014 (email, untrusted), event-015 (email, untrusted), event-016 (email, untrusted), event-017 (email, untrusted), event-018 (email, informational), event-019 (email, untrusted), event-020 (email, informational), event-021 (email, untrusted), event-022 (email, untrusted), event-023 (email, untrusted), event-024 (note, informational), gas-portal-record (document, informational)

Facts and their sources:
- F1 [high] The last signed gas safety record on the tenancy file is dated 16 October 2024; no later record is in the file. ← event-002, event-024
- F2 [high] The landlord arranged the annual gas visit with Flintmere Gas Services for 9 October 2025 and instructed that the check only be carried out, with no additional repair costs authorised. ← event-005
- F3 [high] Engineer Tavin Rell attended on 9 October 2025, 09:05-10:02, and recorded the check as satisfactory; the job card lists a boiler and a cooker. ← event-009, gas-portal-record, event-019
- F4 [high] The document on the case file (gas-portal-record.pdf) is a landlord-supplied customer-portal screenshot of job NBL-48217 showing 'Customer document: Processing'; it is not a signed Landlord Gas Safety Record. ← event-012, event-013, gas-portal-record
- F5 [high] Flintmere's quality desk has paused issuing the signed paperwork while it reconciles an appliance installation detail against information held for the address, and has given no date; the engineer cannot resolve the query or see the office queue. ← event-019, event-021, event-024
- F6 [high] The tenant reported boiler lockouts on 1, 13 and 16 October 2025; each time the boiler restarted after a reset, heating was working and no gas smell was noticed. ← event-003, event-017, event-022
- F7 [high] Flintmere states a lockout diagnostic would be a separate job; no diagnostic has been booked and the landlord has not approved one or any further charge. ← event-019, event-020, event-023
- F8 [high] The landlord has paid Flintmere for the 9 October visit and has twice instructed that no extra charges be approved without her agreement; no standing spend cap is on file. ← event-005, event-016, event-023
- F9 [high] The tenant can provide access after 21 October 2025 for any further visit. ← event-022

Conflicts and how they were handled:
- Flintmere's portal/job card and coordinator say the gas check is complete and satisfactory, while the agency file shows no signed statutory record and Flintmere's own quality desk has paused issuance pending an appliance-installation query. → A portal status line is not a compliance certificate; under the source hierarchy only a compliance_certificate evidences the check. Unresolved until Flintmere issues the signed CP12 - escalated to the property manager; tenant told the screenshot is not her certificate (ACT-2). (unresolved; sources gas-portal-record, event-010, event-015, event-019, event-024)

Uncertainty acknowledged:
- Whether the appliance-installation query could change the 9 October outcome from satisfactory, or indicates an appliance at the property that was not on the job card.
- Whether a signed record exists in the landlord's portal account that has not been shared.
- The cause of the intermittent lockouts; no diagnostic has been carried out.

Assumptions made:
- Assumption: the file-review date of 18 October 2025 (event-024) is today's date, used to compute the CLK-GAS-CP12 position.
- Assumption: Flintmere Gas Services is Gas Safe registered, as the landlord engaged them for the statutory annual check (event-005); not independently verified from an authoritative record.

## Why this disposition

Disposition: **escalated**. Escalate to the property manager for compliance ownership. The annual gas check was carried out on 9 October 2025 but Flintmere has not issued the signed Landlord Gas Safety Record and has given no date; the last signed record on file is dated 16 October 2024, so the CLK-GAS-CP12 12-month renewal point passed on 16 October 2025 with the tenant in occupation. The playbook requires an expired or missing certificate with a tenant in occupation to be escalated so a human owns the statutory follow-up. Within authority I chased Flintmere in writing for the signed record, an issue date, the appliance list and a quote for the lockout diagnostic (ACT-1); told the tenant the portal screenshot is not her gas safety record and gave gas-emergency and heating-failure advice (ACT-2); gave the landlord the outstanding list she asked for on 17 October (ACT-3); and logged the finding (ACT-4). I did not dispatch a diagnostic: the boiler restarts on reset, heating is working and no gas smell is reported, so it is not an emergency; there is no standing spend cap on file and the landlord has twice refused spend without her written agreement (APR-SPEND-OVER-CAP, event-016, event-023). I did not issue gas-portal-record.pdf to the tenant as her certificate — it is a job-card screenshot marked "Customer document: Processing", and telling a tenant the property is certified while sources disagree is prohibited by the playbook.
Authority relied on: CLK-GAS-CP12, CLK-S11, ESC-SAFETY, ESC-CONFLICT, RTE-LANDLORD, RTE-CONTRACTOR, RTE-STAFF, APR-SPEND-OVER-CAP, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, PRO-LEGAL, PRO-PII.
Red flags shaped the decision: data_quality: The only gas document on file is a portal screenshot marked 'Customer document: Processing' (quoted fragment), supplied by the landlord rather than the issuer, and the issuer is reconciling an 'appliance installation detail' for the address - so the appliance inventory for the property may not match the job card (boiler; cooker).; safety_hazard: Gas-keyword check: the renewal point for the statutory gas safety record has passed with a tenant in occupation and the boiler is locking out intermittently. The tenant reports no gas smell and the boiler restarts on reset; heating is working, so the emergency definitions are not met on current facts.

## Timeline

- 15:34:59.940 model turn 1 → tool_use
- 15:34:59.940 playbook compliance-expiry · type compliance_expiry · urgency urgent
- 15:34:59.940 gate get_case_details → allow (read)
- 15:34:59.940 get_case_details → completed (attempts 1)
- 15:34:59.941 gate get_action_ledger → allow (read)
- 15:34:59.941 get_action_ledger → completed (attempts 1)
- 15:35:43.985 model turn 2 → tool_use
- 15:35:43.985 gate notify_contractor → allow (CAP-NOTIFY)
- 15:35:43.985 notify_contractor → completed (attempts 1)
- 15:35:43.985 gate notify_tenant → allow (CAP-NOTIFY)
- 15:35:43.985 notify_tenant → completed (attempts 1)
- 15:35:43.985 gate notify_landlord → allow (CAP-NOTIFY)
- 15:35:43.985 notify_landlord → completed (attempts 1)
- 15:35:43.986 gate add_note → allow (CAP-LOG)
- 15:35:43.986 add_note → completed (attempts 1)
- 15:36:56.378 model turn 3 → tool_use
- 15:36:56.379 terminal escalate → rejected: Invalid escalate record; fix the fields and call escalate again. Errors: 1 validation error for EscalatePayload
handove…
- 15:37:56.832 model turn 4 → tool_use
- 15:37:56.832 terminal escalate → accepted

Steps used: 4; tokens in/out: 42659/16594 (cache reads 42561); model: claude-opus-5.
