# ANSWER — Case 001 — Case 001: Communal Garden and Hedge Maintenance Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Landlord's own contractor completed the communal garden works and bills the landlord direct; tenant and landlord updated, file held for landlord's completion confirmation before closing.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation that Riverside Services' works are complete and settled directly, plus documents or an agreed skip reason; 3-day reply window from today's chase (ACT-2, ACT-4).
**Last update:** 2025-12-11 21:51:18 UTC (event-044) · **Decided:** 2026-10-10 13:19 UTC
**Next step:** Landlord (Rowan) to confirm the works are complete and settled with Riverside Services, and whether any completion paperwork exists; tenant to flag anything still outstanding. Then close as completed without payment.

Definition of done (6/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 — AI intake categorised as External & Communal, severity ROUTINE, with tenant Q&A; no damage-limiting advice needed for grounds maintenance
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-022 and event-026 — landlord's own emails confirm quotes received and 'go ahead given'; landlord uses and pays his own contractor, so no agency spend (CAP-DISPATCH-APPROVED not needed)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-035 provider assigned; tenant told Riverside Services instructed at event-025
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-033 — landlord's own contractor handled access to the communal grounds; job started 20 Nov 2025. Tenant told the indicative date at event-031
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-022/event-026 — landlord received Riverside Services' quotes and approved; amount not disclosed to the agency as the landlord contracts and pays direct
- [x] work_result: Work result recorded from the provider — event-042 contractor call confirming completion and invoicing; event-043 'Job done and LL pays directly'
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice on file; skip reason (landlord's own contractor, invoices landlord direct) proposed to the landlord at ACT-2 and awaiting his confirmation
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-044 — task completed without payment; Riverside Services invoices the landlord direct (event-043), no agency invoice
- [ ] landlord_confirmation: Landlord confirmed completion — ACT-2 — confirmation requested from the landlord today; no landlord message in the history confirms completion
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — External communal works; no management key issued (event-002 access Q&A: no access considerations)
- [ ] closed: Request closed with a resolution that names who paid — Held at final_checks pending landlord confirmation and the documents position (ACT-4)

## 1. Decision

No dispatch or spend by the agency: the landlord approved the works in his own words (event-022, event-026) and used his own contractor, Riverside Services, paying direct (event-043, event-044). The provider confirmed completion by phone (event-042). I kept the outstanding promise to the tenant by telling them the works are reported complete and asking them to flag anything left (ACT-1), asked the landlord to confirm completion and the document position (ACT-2), logged the review and the data-quality discrepancies (ACT-3) and placed the ticket on hold pending the landlord (ACT-4). I did not close: landlord confirmation and the documents/skip reason are still open, and only the landlord and tenant can settle them.

Safety actions taken first:
- Safety pass: no hazard keyword applies — report is weeds, hedge and uncleared ground; no alarms, gas, electrics, damp or occupant vulnerability in any artefact (event-001, event-002). Pigeon nesting (event-037) was handled by delaying the trimming, which is the correct course.

Actions deliberately withheld:
- Did not close the request: landlord confirmation and the documents/skip reason remain pending (CAP-CLOSE requires the final checks first).
- Did not instruct or chase a contractor on the agency's behalf: the provider is the landlord's own and is paid by him (event-043); no agency spend authority is engaged.
- Did not state any cost to any party, as no quote figure exists in the artefacts.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, RTE-LANDLORD, RTE-TENANT, CAP-CLOSE, PRO-INSTRUCTIONS-FROM-CONTENT, PRO-PAYMENTS
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant of Flat 26, 46 Copperfield Walk reported on 10 Oct 2025: communal garden full of weeds, hedge along the side path overgrown, and a strip of land at the side not cleared as expected last summer. [index, event-001; high]
- F2: Intake categorised the issue as External & Communal, severity ROUTINE; one cat at the property; no access codes or alarms. [event-002; high]
- F3: The landlord's own message confirmed quotes received from Riverside Services and gave the go-ahead for the garden works. [event-022, event-026; high]
- F4: The contractor is the landlord's own (Riverside Services, contact Freya); the landlord arranged the booking and the start date directly. [event-023, event-026, event-033; high]
- F5: Tenant was told on 5 Nov 2025 that Riverside Services had been instructed and on 6 Nov 2025 that works were hoped to start around 19 Nov 2025; work actually started 20 Nov 2025 and was delayed by a pigeon nest in a tree to be trimmed. [event-025, event-031, event-033, event-037; high]
- F6: On 11 Dec 2025 the contractor confirmed by phone that the job (including tree removal) is complete and will be invoiced to the landlord; the agency recorded the task as completed without payment. [event-042, event-043, event-044; high]
- F7: No landlord confirmation of completion and no photos or invoice are on the case file. [get_case_details, get_action_ledger; high]
- F8: No hazard, vulnerability, liability dispute or spend by the agency arises on this case; the work is grounds maintenance funded by the landlord. [event-002, event-043; high]

Conflicts between sources:
- An internal hold note says the works are 'an external job for the development and not for the tenants so no contact needed' (event-036), while the agency had already promised the reporting tenants updates (event-023, event-025, event-031). → The express promise to the tenant stands; the tenant has now been told the works are reported complete (ACT-1). No decision changed for the landlord or contractor. (source_hierarchy)
- Caller identified as 'Leo from Juniper Homes' (event-039) although the agency of record is Northbridge Lettings; landlord emails carry third-party names (Grace Nolan, Harper, Felix Kendall) inconsistent with the landlord addressed as Rowan elsewhere. → Treated as summarisation noise in untrusted/auto-summarised records; the property and parties on the agency's own record (get_case_details) were used, and no name from a message body was copied into another party's letter. Recorded as a data-quality red flag, not acted on. (tool_check)

Red flags:
- [data_quality] Several agency emails and call notes contain placeholder property strings ('synthetic-bca83b5565b3', 'synthetic-f00fcbada17f', 'synthetic-eae38b44a3ac') instead of the address, and landlord emails are auto-summaries naming people inconsistently with the case record. → Logged at ACT-3; all outgoing messages used the address on the agency record and no names from message bodies were relayed to other parties.
- [other] Scope verification gap: the only contractor completion detail on file is a call summary about 'removing a tree' (event-042), which does not evidence the weeds, side-path hedge or side strip the tenant reported. → Tenant asked to confirm whether any part of the original report remains outstanding (ACT-1); file held open rather than closed.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "001", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed | message=Hello, an update on your report of the communal garden weed… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed | message=Address: Flat 26, 46 Copperfield Walk, Kingshaven, ZZ5 7ZZ… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | add_note | completed | note=Case review. Landlord approval in his own words at event-02… | {"id": "ACT-3"} | CAP-LOG |
| 6 | put_on_hold | completed | reason=Waiting for Landlord: confirmation that the Riverside Servi…, until=3 days from today's chase (landlord reply window) | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Please confirm the communal garden / hedge works at 46 Copperfield Walk are complete to your satisfaction and are being settled directly with Riverside Services, and whether any completion paperwork or photos exist for our file. (blocking; RTE-LANDLORD: landlord confirmation and the documents position are the last two definition-of-done items before closure; the landlord commissioned and pays for the work.)
- Ask **tenant**: Do the communal garden, the side-path hedge and the strip of land at the side now look done, or is any part of your original report still outstanding? (non-blocking; RTE-TENANT: the reporter is the only party who can verify the scope on the ground; the contractor call (event-042) only mentions tree removal, not the weeds, hedge and side strip.)

Promises made or recorded:
- Northbridge Lettings → tenant: Confirm the contractor's start date once known by 2025-11-06 [kept]
- Northbridge Lettings → landlord: Keep the tenants at Flat 26 and 44 informed of the works [kept]
- Northbridge Lettings → tenant: Tell the tenant the works are reported complete and take any outstanding element back to the landlord [open]
- Northbridge Lettings → landlord: File any completion paperwork Riverside Services send, or record the agreed skip reason [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
