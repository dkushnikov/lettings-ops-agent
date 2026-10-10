# ANSWER — Case 046 — Case 046: Bedroom Window Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** The repair itself was properly authorised and carried out, but the branch's system closed the ticket (event-052) with two definition-of-done items unmet: no pr…
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation of completion so the £90 + VAT invoice can be processed (3 working days from ACT-3); also Waiting for Provider for a completion report and a readable PDF invoice (ACT-4).
**Last update:** 2025-10-07 12:32:30 UTC (event-052) · **Decided:** 2026-10-10 13:34 UTC
**Next step:** Landlord to confirm completion and that the invoice may be processed (requested ACT-3, 3 working days); in parallel Lantern Utilities to send a completion report and a clean PDF invoice (ACT-4).

Definition of done (6/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 issue logged; event-004 tenant acknowledged within one working day (CLK-SOP-ACK). Routine: no insecurity or hazard alleged by the tenant.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-007 — landlord's own email agreeing to a contractor attending.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010/event-012 Lantern Utilities instructed; tenant briefed at event-011.
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-027 provider booked 30/09/2025; confirmed to provider (event-030) and tenant (event-031); reminder event-035.
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-015 quote £90 + VAT; landlord's own approval at event-018; provider instructed to proceed event-020.
- [ ] work_result: Work result recorded from the provider — event-036 'No work results'; only event-041 'Attached invoice' with attachment unavailable (event-043). Completion report chased at ACT-4; tenant asked to confirm at ACT-2.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-048 skipped as 'not applicable', but a priced invoice exists and is unreadable on file; clean PDF requested at ACT-4.
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-042 and event-043 — invoice forwarded to the landlord.
- [ ] landlord_confirmation: Landlord confirmed completion — event-049 'Need confirmation from landlord'; no landlord reply after event-043. Requested at ACT-3 with a 3-working-day reply time.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — event-051 keys return confirmed; no management key was issued — the tenant gave access for the 30/09 slot.
- [ ] closed: Request closed with a resolution that names who paid — event-052 closed the request, but work_result, documents and landlord_confirmation were unmet at that moment; not re-closed by me (CAP-CLOSE).

## 1. Decision

The repair itself was properly authorised and carried out, but the branch's system closed the ticket (event-052) with two definition-of-done items unmet: no provider work result and no landlord confirmation. I did not re-close it. I chased the provider for a completion report and a readable PDF invoice, asked the tenant to confirm the window now closes and secures, asked the landlord to confirm completion so the invoice can be processed, and raised a human task about the inconsistent landlord contact name on which the £90 + VAT spend authority rests. No payment made or authorised (PRO-PAYMENTS); no liability decided (PRO-TENANT-LIABILITY).</decision>
Window hinge repair authorised and attended, but ticket was closed without a provider work result or landlord confirmation; both chased, case reopened at final checks.

Safety actions taken first:
- Checked the report against the emergency definitions: a window that will not close can engage 'property not secure', but neither the tenant nor any later event alleged the flat was insecure, so the routine classification was retained and recorded (ACT-1).
- Asked the tenant to confirm the window now closes and secures, so that an unresolved security defect cannot be buried by the closure (ACT-2).

Actions deliberately withheld:
- Did not re-close the request: three definition-of-done items are outstanding (CAP-CLOSE).
- Did not process or authorise payment of the invoice (PRO-PAYMENTS).
- Did not name 'Grace' or 'Felix' in any outbound message, since the agency's own records disagree (rule 7).
- Did not escalate to a manager as the case needs no human decision beyond the office data-quality task; it waits on named parties (rule 5).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, PRO-PAYMENTS, PRO-TENANT-LIABILITY, PRO-PII, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the bedroom window not closing properly with a rusted hinge at Flat 23, 143 Willowmere Road, Alderwick, ZZ2 6ZZ. [index, event-001, get_case_details; high]
- F2: The landlord's own email authorised a contractor to attend 'when convenient'. [event-007; high]
- F3: The provider quoted hinges at £90 plus VAT and asked to fit while on site. [event-015; high]
- F4: The landlord's own email approved that amount ('Yes, I'm happy to ahead with that'); the agency instructed the provider to proceed. [event-018, event-020; high]
- F5: Visit confirmed for 30/09/2025, 10:00-17:00, to both provider and tenant; SMS reminder sent 29/09. [event-027, event-029, event-030, event-031, event-035; high]
- F6: No provider completion report exists; the agency recorded 'No work results' on 02/10 and the provider's 07/10 invoice email has an unavailable attachment. [event-036, event-041, event-043; high]
- F7: Landlord confirmation of completion was flagged as required and never received. [event-049, event-042, event-043; high]
- F8: The request was nonetheless marked closed as 'all checks completed'. [event-052; high]
- F9: The agency's own outbound emails address the landlord as 'Grace' in two messages and 'Felix' in two others; the approving replies are signed or phrased as Felix. [event-003, event-016, event-008, event-042, event-007, event-018; high]
- F10: Two occupant mobile numbers were released to the provider in response to a request for the tenant's mobile. [event-024, event-025; high]
- F11: The provider's messages are signed by two different individuals, 'Jenkins' and 'Mercer'. [event-015, event-022; medium]

Conflicts between sources:
- The agency's own correspondence is inconsistent about the landlord's first name (Grace vs Felix), and the spend authority for £90 + VAT rests on replies signed 'Felix'. → Not decided by me and not raised with any party in correspondence; referred to the office to reconcile against the management agreement before the invoice is paid (ACT-5). Outbound letters carry no landlord first name. (asked)
- System closure states all checks complete, while the case's own notes show work result, documents and landlord confirmation unmet. → The specific notes beat the general closure line; ticket treated as at final_checks, not resolved. (source_hierarchy)

Red flags:
- [data_quality] Landlord addressed by two different first names across the agency's own emails, on a file where landlord replies are the sole spend authority. → Recorded; office task raised (ACT-5); no name used in outbound correspondence.
- [data_quality] Provider correspondence signed by two different names ('Jenkins', 'Mercer') and an unparseable reply consisting of an emoji (event-033), plus an invoice attachment that cannot be opened. → Readable PDF invoice and a completion report requested from the provider (ACT-4).
- [other] Closure of the request while its own final-check items were outstanding. → Ticket reported at final_checks with the pending items itemised; not re-closed.
- [other] Two occupant mobile numbers disclosed to the contractor where one access contact was sufficient (PRO-PII). → Flagged to the office for review (ACT-5); no further occupant data shared by me.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "046", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [{"event": "event-007", "timestamp": "2025-09-12 10:06:25 UTC", "channel": "Email", "from": "Landlord", "to": "Northbridge Lettings", "excerpt": "[2025-09-12 1… | allow |
| 4 | search_history | completed | query=invoice | [{"event": "event-038", "timestamp": "2025-10-07 10:41:42 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Contractor", "excerpt": "[2025-10-07… | allow |
| 5 | add_note | completed | note=Final-checks review of closed ticket. Approval trail is sou… | {"id": "ACT-1"} | CAP-LOG |
| 6 | notify_tenant | completed | message=Dear Freya Grant, regarding the bedroom window repair at Fl… | {"id": "ACT-2"} | CAP-NOTIFY |
| 7 | notify_landlord | completed | message=Address: Flat 23, 143 Willowmere Road, Alderwick, ZZ2 6ZZ… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_contractor | completed | message=Address: Flat 23, 143 Willowmere Road, Alderwick, ZZ2 6ZZ —… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | create_human_task | completed | queue=property_manager, title=Case 046 — closed before landlord confirmation; landlord co…, summary=Flat 23, 143 Willowmere Road. Request was closed by the sys… | {"id": "ACT-5"} | CAP-HUMAN-TASK |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the bedroom window hinge replacement at Flat 23, 143 Willowmere Road is complete to your satisfaction and that the contractor's invoice (approved at £90 plus VAT) may be processed as normal? (blocking; RTE-LANDLORD: landlord confirmation is the outstanding final check flagged at event-049; no landlord reply exists after the invoice was sent at event-042/event-043.)
- Ask **contractor**: Please send a completion report for the 30/09/2025 visit (date attended, work done, photos) and a clean PDF copy of your invoice — the file sent on 7 October cannot be opened. (blocking; RTE-CONTRACTOR: event-036 recorded 'No work results'; the only completion evidence is a one-line email (event-041) with an unavailable attachment (event-043).)
- Ask **tenant**: Did the engineer attend on 30 September and complete the hinge replacement, and does the bedroom window now close and secure properly? (non-blocking; RTE-TENANT: independent confirmation that the reported fault is actually resolved before the file is closed; no tenant feedback exists in the history.)

Promises made or recorded:
- agency → landlord: Will keep the request open pending confirmation rather than treat it as settled if no reply; will forward a clean PDF invoice once the provider supplies it by 3 working days from 2025-10-07 request [open]
- agency → tenant: If the window still does not close or work was left unfinished, we will raise it with the provider directly [open]
- agency → tenant: Earlier promise that the agency or contractor would be in touch to arrange a visit [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- RTE-LANDLORD [sop]: Landlord confirmation reply window deadline 3 working days from the request
