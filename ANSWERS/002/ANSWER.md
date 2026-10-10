# ANSWER — Case 002 — Gas record and boiler visit

**Disposition:** ESCALATED · **Urgency:** urgent · **Case type:** compliance_expiry · **Playbook:** compliance-expiry

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Gas check done 9 Oct but no signed CP12 issued; 12-month renewal point passed 16 Oct — chased Flintmere, briefed tenant and landlord, escalated for compliance.
**Stage:** on_hold · **Hold:** Waiting for Provider — Flintmere Gas Services to issue the signed CP12 for job NBL-48217 and to quote the lockout diagnostic; chased 18 Oct 2025 (ACT-1), provider has given no issue date (event-019, event-021).
**Last update:** 2025-10-18 16:35:00 UTC (event-024) · **Decided:** 2026-10-10 15:37 UTC
**Next step:** Property manager to decide whether to hold Flintmere to a deadline or instruct a second Gas Safe engineer to re-certify; Flintmere owes the signed CP12 and the diagnostic quote (chased 18 Oct, ACT-1).

Definition of done (4/7 done):
- [x] certificate_read: Certificate record read and the clock computed from the authoritative document — gas-portal-record.pdf read (job card, 'Customer document: Processing'); prior signed record dated 16 Oct 2024 per event-002; clock computed in ACT-4
- [ ] conflict_resolved: Any disagreement between the certificate and the CRM resolved by the source hierarchy and corrected — Portal job card says complete/satisfactory (gas-portal-record, event-015) but no signed statutory record exists (event-019, event-024); unresolved pending Flintmere's issue - recorded as a conflict a…
- [x] inspection_booked: Qualified contractor booked for the renewal or the remedial work — Annual check carried out 9 Oct 2025 by Flintmere, arranged by the landlord (event-005, event-008, event-009); re-certification not booked - awaiting the manager's decision
- [x] access_arranged: Access agreed with the tenant within the clock — Tenant gave 09:00-11:00 on 9 Oct (event-007) and the visit took place (event-008, event-009); further access offered after 21 Oct (event-022) and noted for any new visit
- [x] landlord_informed: Landlord told the status, the booking and the legal duty — ACT-3 - outstanding items, the 16 Oct 2024 record date and the CLK-GAS-CP12 renewal position sent to the landlord, following event-020
- [ ] certificate_filed: New certificate received and filed; remedials closed within their clock — No signed CP12 received; Flintmere chased with no issue date (ACT-1, event-019, event-021, event-024)
- [ ] closed: Request closed with the certificate reference — Cannot close: no certificate reference, and the boiler lockout decision sits with the landlord

## 1. Decision

Escalate to the property manager for compliance ownership. The annual gas check was carried out on 9 October 2025 but Flintmere has not issued the signed Landlord Gas Safety Record and has given no date; the last signed record on file is dated 16 October 2024, so the CLK-GAS-CP12 12-month renewal point passed on 16 October 2025 with the tenant in occupation. The playbook requires an expired or missing certificate with a tenant in occupation to be escalated so a human owns the statutory follow-up. Within authority I chased Flintmere in writing for the signed record, an issue date, the appliance list and a quote for the lockout diagnostic (ACT-1); told the tenant the portal screenshot is not her gas safety record and gave gas-emergency and heating-failure advice (ACT-2); gave the landlord the outstanding list she asked for on 17 October (ACT-3); and logged the finding (ACT-4). I did not dispatch a diagnostic: the boiler restarts on reset, heating is working and no gas smell is reported, so it is not an emergency; there is no standing spend cap on file and the landlord has twice refused spend without her written agreement (APR-SPEND-OVER-CAP, event-016, event-023). I did not issue gas-portal-record.pdf to the tenant as her certificate — it is a job-card screenshot marked "Customer document: Processing", and telling a tenant the property is certified while sources disagree is prohibited by the playbook.

Safety actions taken first:
- Gave the tenant gas-emergency instructions (no electrical switches, open windows, leave, call 0800 111 999) and told her to report immediately if the boiler fails to restart or heating is lost in cold months (ACT-2).
- Declined to tell the tenant the property's gas paperwork is in order while the signed record is unissued (playbook 'Never' clause).
- Asked Flintmere to confirm which appliances the 9 October check covered and whether the installation-detail query could change the satisfactory outcome (ACT-1).

Actions deliberately withheld:
- Did not dispatch a lockout diagnostic: no standing spend cap on file, landlord refused spend without written agreement (APR-SPEND-OVER-CAP; event-016, event-023), and the fault does not meet an emergency definition (boiler restarts, heating working, no gas smell).
- Did not send gas-portal-record.pdf to the tenant as her gas safety record.
- Did not book an access window: no visit is authorised, so a slot would be a promise with no booking behind it (CAP-NOTIFY).
- Did not state legal consequences of the missed renewal to the landlord or tenant (PRO-LEGAL); stated the clock only.
- Did not pass the tenant's contact number into the maintenance-thread copy (PRO-PII, event-011).

## 2. Authority and evidence

Authority cited: CLK-GAS-CP12, CLK-S11, ESC-SAFETY, ESC-CONFLICT, RTE-LANDLORD, RTE-CONTRACTOR, RTE-STAFF, APR-SPEND-OVER-CAP, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, PRO-LEGAL, PRO-PII
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: The last signed gas safety record on the tenancy file is dated 16 October 2024; no later record is in the file. [event-002, event-024; high]
- F2: The landlord arranged the annual gas visit with Flintmere Gas Services for 9 October 2025 and instructed that the check only be carried out, with no additional repair costs authorised. [event-005; high]
- F3: Engineer Tavin Rell attended on 9 October 2025, 09:05-10:02, and recorded the check as satisfactory; the job card lists a boiler and a cooker. [event-009, gas-portal-record, event-019; high]
- F4: The document on the case file (gas-portal-record.pdf) is a landlord-supplied customer-portal screenshot of job NBL-48217 showing 'Customer document: Processing'; it is not a signed Landlord Gas Safety Record. [event-012, event-013, gas-portal-record; high]
- F5: Flintmere's quality desk has paused issuing the signed paperwork while it reconciles an appliance installation detail against information held for the address, and has given no date; the engineer cannot resolve the query or see the office queue. [event-019, event-021, event-024; high]
- F6: The tenant reported boiler lockouts on 1, 13 and 16 October 2025; each time the boiler restarted after a reset, heating was working and no gas smell was noticed. [event-003, event-017, event-022; high]
- F7: Flintmere states a lockout diagnostic would be a separate job; no diagnostic has been booked and the landlord has not approved one or any further charge. [event-019, event-020, event-023; high]
- F8: The landlord has paid Flintmere for the 9 October visit and has twice instructed that no extra charges be approved without her agreement; no standing spend cap is on file. [event-005, event-016, event-023; high]
- F9: The tenant can provide access after 21 October 2025 for any further visit. [event-022; high]

Conflicts between sources:
- Flintmere's portal/job card and coordinator say the gas check is complete and satisfactory, while the agency file shows no signed statutory record and Flintmere's own quality desk has paused issuance pending an appliance-installation query. → A portal status line is not a compliance certificate; under the source hierarchy only a compliance_certificate evidences the check. Unresolved until Flintmere issues the signed CP12 - escalated to the property manager; tenant told the screenshot is not her certificate (ACT-2). (unresolved)

Red flags:
- [data_quality] The only gas document on file is a portal screenshot marked 'Customer document: Processing' (quoted fragment), supplied by the landlord rather than the issuer, and the issuer is reconciling an 'appliance installation detail' for the address - so the appliance inventory for the property may not match the job card (boiler; cooker). → Not treated as a certificate; not issued to the tenant as the gas safety record; Flintmere asked to confirm the appliances covered and the nature of the query (ACT-1); logged (ACT-4) and escalated.
- [safety_hazard] Gas-keyword check: the renewal point for the statutory gas safety record has passed with a tenant in occupation and the boiler is locking out intermittently. The tenant reports no gas smell and the boiler restarts on reset; heating is working, so the emergency definitions are not met on current facts. → Tenant given National Gas Emergency 0800 111 999 advice and told to report any failure to restart or loss of heating immediately (ACT-2); compliance follow-up escalated to the property manager.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "002", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_contractor | completed (ledger) | message=Flintmere Gas Services — ref job NBL-48217, 8 Brindlewick R… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_tenant | completed (ledger) | message=Dear Ms Pell,  Thank you for your updates, most recently on… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_landlord | completed (ledger) | message=Dear Ms Wold,  You asked on 17 October what is still outsta… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | add_note | completed (ledger) | note=Compliance position 18/10/2025: last signed gas record on t… | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** The gas safety record for 8 Brindlewick Row is unissued and the 12-month renewal point passed on 16 October 2025 with the tenant in occupation. Do we hold Flintmere to a deadline, or instruct a second Gas Safe engineer to re-certify and put the cost to the landlord?
**Facts (≤5):**
- Last signed gas record on the tenancy file is dated 16 Oct 2024 (event-002); CLK-GAS-CP12 renewal point passed 16 Oct 2025, tenant in occupation.
- Flintmere attended 9 Oct 2025 (engineer Tavin Rell) and recorded the check satisfactory (event-009, gas-portal-record), but its quality desk has paused issuing the signed record pending an 'appliance installation detail' reconciliation with no date (event-019); the engineer cannot resolve it (event-021).
- The only document on file is a landlord-supplied portal screenshot marked 'Customer document: Processing' (event-012, gas-portal-record) - not the statutory record; the tenant has been told this plainly (ACT-2).
- Boiler locked out on 1, 13 and 16 Oct (event-003, event-017, event-022), each time self-resolving on reset, heating working, no gas smell; Flintmere says a diagnostic is a separate job (event-019).
- No standing spend cap on file and the landlord has refused extra spend without written agreement (event-005, event-016, event-023); nothing dispatched, no cost committed. Tenant can give access after 21 Oct (event-022).
**Gap:** Why Flintmere's quality desk has paused issuance and whether the appliance-installation query could change the satisfactory outcome; whether the 9 Oct check covered every gas appliance at the property; whether any later signed record exists in the landlord's portal account.
**Options:**
- Hold Flintmere to a short written deadline for the signed CP12 and escalate to their management if missed
- Instruct a second Gas Safe engineer to re-inspect and certify now, seeking the landlord's approval for the cost in parallel
- Ask the landlord to approve re-certification and the lockout diagnostic as a single visit after 21 October
- Continue waiting on Flintmere's quality desk with no deadline (not recommended - the renewal point has passed)
**Recommended:** Hold Flintmere to a short written deadline for the signed CP12 (the check was carried out and recorded satisfactory); if it is not produced, instruct a second Gas Safe engineer and put the cost to the landlord, ideally combined with the lockout diagnostic in one visit after 21 October.
**Default if no answer:** Chaser to Flintmere stands; no contractor dispatched and no spend committed.
**Deadline:** CLK-GAS-CP12 renewal point already passed on 16 October 2025; review by 21 October 2025 when tenant access becomes available
**Undo:** Withdraw the chaser to Flintmere if the signed CP12 arrives; nothing has been dispatched and no cost committed.
**Context:** event-002, event-005, event-009, event-012, event-016, event-019, event-021, event-022, event-023, event-024, gas-portal-record, ACT-1, ACT-2, ACT-3, ACT-4

Promises made or recorded:
- agency → tenant: Send the signed gas safety record as soon as Flintmere issues it [open]
- agency → tenant: Come back with a visit slot, agreed with her first, once a diagnostic is authorised [open]
- agency → landlord: Obtain Flintmere's written quote for the lockout diagnostic for her decision before any spend [open]
- Flintmere Gas Services → agency: Issue the signed CP12 for job NBL-48217 and confirm an issue date, the appliances covered and the installation-detail query [open]
- contractor (Riva Morn, Flintmere) → agency: Office paperwork from the 9 October visit to be provided - stated as 'still being processed' on 9, 11 and 14 October [broken]

Clocks:
- CLK-GAS-CP12 [in_force]: Gas safety record renewed every 12 months deadline 2025-10-16
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
