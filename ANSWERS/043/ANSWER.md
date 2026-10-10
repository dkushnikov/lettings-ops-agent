# ANSWER — Case 043 — Case 043: Washing Machine Repair Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Closed washing-machine ticket rests on an unverifiable provider completion claim and conflicting tenant identities; verification sent, escalated to decide if closure stands.
**Stage:** final_checks · **Hold:** Waiting for Provider — Oakfield Homes to confirm actual attendance date, works done, photos and invoice; tenant confirmation also outstanding.
**Last update:** 2026-04-15 23:20:17 UTC (event-025) · **Decided:** 2026-10-10 14:12 UTC
**Next step:** Property manager to decide whether to reverse the closure, pending the tenant's confirmation that the machine drains and Oakfield Homes' attendance date/invoice (both requested today).

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 — fault categorised as routine appliance repair; tenant had already cleared the filter, so no further damage-limiting step applied
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-013 — landlord Ava Rowan's own reply approving a contractor (CAP-DISPATCH-APPROVED)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008/event-010 Oakfield Homes instructed; tenant told at event-009 — but the brief at event-011 carries a conflicting tenant name and number
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No booked slot anywhere in the history; no reply from the provider confirming an appointment with the tenant (chased at event-014 and by me, ACT-2)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted (event-016 reports completion only); landlord's instruction at event-011/event-014 was to quote if parts or complexity arose
- [ ] work_result: Work result recorded from the provider — Only untrusted claim event-016 with an impossible date ("November 4th"); no photos or engineer detail — verification requested ACT-2
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-021 — "Skipped uploading one or more documents. Reason provided: not needed at this time"; photos/invoice now requested (ACT-2)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice or no-charge confirmation on file; event-017 told the landlord work was complete but passed no cost
- [ ] landlord_confirmation: Landlord confirmed completion — event-022 "Need confirmation from landlord" was never answered before closure at event-025
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued in the history; event-024 keys-return update is a system artefact carrying a validation error
- [x] closed: Request closed with a resolution that names who paid — event-025 — closed by the agency, but the resolution names no payer and rests on unverified evidence; validity referred to the property manager

## 1. Decision

The ticket was closed as completed on the strength of an untrusted provider email whose completion date ("November 4th", event-016) cannot belong to this job (reported 6 April 2026, instructed 13 April 2026), with no photos, no invoice, no tenant confirmation and the landlord-confirmation check still open (event-022). The same ticket also carries two different occupant identities (Isaac Quinn / 07700 900844 at event-009 and event-010 vs "Grace Ashford" / 07700 900641 at event-011), so it is not established which flat was attended — an authoritative-record conflict that changes the action (ESC-CONFLICT, RTE-STAFF). I did not re-open or re-dispatch (no duplicate work order) and did not decide liability or payment. In-authority reversible steps taken: tenant asked to confirm attendance and that the machine now drains (ACT-1); provider asked for the real attendance date, works done, photos and invoice (ACT-2); conflict recorded (ACT-3). A human must decide whether the closure stands.

Safety actions taken first:
- Safety-keyword pass: no gas, electrical, water-ingress, damp/mould, alarm or vulnerability content appears in this ticket; the fault is a non-draining washing machine with no water escape reported (event-001). No hazard red flag raised. Tenant asked to report immediately if water overflows (standing advice implicit in ACT-1 re-opening offer).

Actions deliberately withheld:
- Did not raise a second work order or re-dispatch Oakfield Homes (would duplicate the 13 April instruction, event-010).
- Did not tell the landlord the job is complete or confirm the earlier completion email (event-017), as completion is unverified.
- Did not decide who pays or whether the fault is tenant-caused (PRO-TENANT-LIABILITY).
- Did not tell any party which occupant record is correct; recorded the conflict instead (rule 2).

## 2. Authority and evidence

Authority cited: CAP-DISPATCH-APPROVED, CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, ESC-CONFLICT, RTE-STAFF, RTE-CONTRACTOR, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 6 April 2026 that the washing machine will not drain; filter removed and cleaned without effect. [index, event-001; high]
- F2: Property is Flat 8, 118 Meadow Row, Alderwick, ZZ3 6ZZ. [index, get_case_details; high]
- F3: Landlord Ava Rowan replied on 13 April 2026 approving dispatch of a contractor; no amount was named and no standing spend cap is on file. [event-003, event-013; high]
- F4: Oakfield Homes was assigned and instructed on 13 April 2026; the tenant was told they would be contacted to arrange a time. [event-008, event-009, event-010; high]
- F5: The agency's provider brief of 13 April 2026 gives the tenant as "Grace Ashford", 07700 900641, while the system records give Isaac Quinn, 07700 900844 on the same ticket. [event-009, event-010, event-011; high]
- F6: The only evidence of completion is a provider email of 15 April 2026 stating the repair was completed "on November 4th" — a date outside this job's timeline; no photos, invoice or engineer name. [event-016; high]
- F7: The landlord completion update of 15 April 2026 is addressed to "Miles Kendall" although the landlord on this case is Ava Rowan. [event-003, event-013, event-017; high]
- F8: The request was closed on 15 April 2026 with documents skipped, landlord confirmation still flagged as needed and a keys-return validation error. [event-021, event-022, event-024, event-025; high]
- F9: No visit window was ever booked or confirmed with the tenant anywhere in the visible history. [event-009, event-014, event-015; medium]

Conflicts between sources:
- Two different occupant identities and phone numbers on the same ticket: Isaac Quinn / 07700 900844 (system records) vs "Grace Ashford" / 07700 900641 (provider brief). It is therefore unverified which occupant, and which flat, the provider attended. → Recorded, not decided in a message to any party; put to the property manager and the provider asked which contact was used (ACT-2). (unresolved)
- Provider's claimed completion date ("November 4th") is incompatible with the report date (6 April 2026) and instruction date (13 April 2026). → Provider asked to confirm the actual attendance date, works done, photos and invoice (ACT-2); tenant asked to confirm attendance and that the machine drains (ACT-1). (asked)
- Ticket closed as all-checks-complete while the system itself still recorded landlord confirmation as outstanding. → Validity of the closure referred to the property manager. (unresolved)

Red flags:
- [data_quality] Completion claim carries a date ("November 4th") that cannot belong to this job, with no photos, invoice or engineer name; closure was based on it. → Provider asked for the actual attendance date and evidence (ACT-2); closure validity escalated.
- [data_quality] Conflicting occupant name/phone on the same ticket, and a landlord update addressed to a name that is not this landlord. → Conflict recorded (ACT-3) and put to the property manager; no party was told which record is correct.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "043", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed | message=Dear Isaac Quinn, re: Flat 8, 118 Meadow Row, Alderwick, ZZ… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_contractor | completed | message=Oakfield Homes — ref: Washing Machine Repair Request, Flat… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | add_note | completed | note=Review of closed ticket. (1) Landlord authority is on file:… | {"id": "ACT-3"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Does the closure of this washing-machine repair stand, or do we re-open it — given completion is evidenced only by a provider email dated "November 4th" and the ticket holds two different tenant identities?
**Facts (≤5):**
- Tenant reported washing machine not draining on 6 Apr 2026; filter already cleared by tenant (event-001).
- Landlord Ava Rowan approved sending a contractor in her own reply (event-013); no standing spend cap on file, so no priced quote was ever approved.
- Oakfield Homes instructed 13 Apr 2026 (event-010); only completion evidence is untrusted email event-016: repair done "on November 4th" — impossible for this job.
- Provider brief event-011 names tenant "Grace Ashford" / 07700 900641, while event-009 and event-010 name Isaac Quinn / 07700 900844 — same ticket, two occupants; which flat was attended is unverified.
- Final checks were nominal: documents skipped (event-021), landlord confirmation still flagged as needed (event-022), keys update carried a validation error (event-024), closed at event-025; landlord update event-017 was addressed to "Miles Kendall", not Ava Rowan.
**Gap:** No photos, no invoice, no visit booking, no tenant confirmation that the machine drains, and no reliable attendance date; the correct occupant record for this flat is unresolved.
**Options:**
- Hold the closure for 3 working days pending the tenant's and provider's replies already sent, then re-open if either fails to confirm.
- Re-open now and re-instruct Oakfield Homes for a confirmed, booked visit with the tenant on the agency's own record (Isaac Quinn, 07700 900844), landlord authority already on file at event-013.
- Leave closed as-is and accept event-016 — risk: a live s.11 repair left unfixed and an unverified job possibly attended at the wrong flat.
**Recommended:** Hold the closure for 3 working days pending the replies already sent, then re-open if unconfirmed; correct the occupant record on the CRM either way.
**Default if no answer:** If neither the tenant nor Oakfield Homes replies within 3 working days, re-open the ticket and re-instruct for a booked visit under the landlord's existing approval (event-013).
**Deadline:** 3 working days from 15 Apr 2026 replies (CLK-S11: repair within a reasonable time from the 6 Apr 2026 report)
**Undo:** Nothing irreversible was done by me: only two verification messages (ACT-1, ACT-2) and an internal note (ACT-3). No work order was raised and no money committed.
**Context:** event-001, event-009, event-010, event-011, event-013, event-016, event-017, event-021, event-022, event-024, event-025

Promises made or recorded:
- agency → tenant: If no one attended or the fault persists, the job will be re-opened straight away on the tenant's reply [open]
- agency → contractor: Final checks and any invoice to the landlord stay on hold until attendance date, works done, photos and invoice are confirmed [open]
