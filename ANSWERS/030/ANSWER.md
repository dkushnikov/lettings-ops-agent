# ANSWER — Case 030 — Case 030: Plumbing request: slow-filling toilet and bathroom tap

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Plumbing repair reported complete by the provider; chased the tenant to verify the tap and the landlord to confirm completion, and referred the provider-identity conflict to the office.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation of completion and of the firm to record (ACT-1, 3 working days); tenant verification of the repair also outstanding (ACT-2)
**Last update:** 2024-11-15 23:29:55 UTC (event-042) · **Decided:** 2026-10-10 13:29 UTC
**Next step:** Landlord (Freya, per event-004) to confirm the works are accepted and settled directly, and to confirm the instructed provider; tenant to confirm the basin cold tap and WC fill are right (both chased, 3 working days).

Definition of done (5/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-002 — AI intake classified Plumbing / ROUTINE with tenant Q&A; toilet drains away, so no emergency definition met
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-004 told the landlord a job had been raised; landlord replied 'Thanks' (event-010). No quote or amount ever arose, and the landlord settles with the contractor directly (event-040)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-006 provider assigned; brief issued event-008; tenant told who is attending event-007 — but the firm named differs between event-004/008 and event-007 onwards (referred to the office, ACT-3)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-024 tenant confirmed 20 Oct PM; event-027 slot recorded 2024-10-20 13:00; missed and rescheduled (event-037), attended 24 Oct (event-039)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote was ever submitted and no amount appears in the file; the landlord pays the contractor directly (event-040)
- [x] work_result: Work result recorded from the provider — event-039 — new Fluidmaster bottom-entry ball valve fitted to the WC; basin taps reported fine. Tenant verification requested (ACT-2) because the tap was the original complaint
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice on file; skip reason recorded in ACT-4 — landlord settles with the contractor directly, so no invoice passes through the agency
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-041 — task completed without payment; event-040 'LL pays contractor directly'
- [ ] landlord_confirmation: Landlord confirmed completion — ACT-1 — asked the landlord to confirm acceptance of the completed works; 3 working days
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued: tenant confirmed someone would be home (event-024), which beats the boilerplate key line in event-032
- [ ] closed: Request closed with a resolution that names who paid — Held pending landlord confirmation and tenant verification (ACT-5)

## 1. Decision

Did not close. The provider reports the job complete (event-039) and the request was marked completed without payment because the landlord pays the contractor directly (event-040, event-041), but two definition-of-done items remain open: landlord confirmation of completion, and verification that the originally reported fault — the basin cold tap "isn't working at all" (event-001) — is actually resolved, since the only evidence is the provider's second-hand account of what the tenants said. I asked the landlord to confirm completion and which firm to record (ACT-1), asked the tenant to confirm both the WC fill and the basin tap are right (ACT-2), referred the contradiction in our own records about the instructed provider to the office (ACT-3), logged the file note (ACT-4) and put the case on hold (ACT-5). No dispatch and no spend were made: no quote exists, no amount appears in the file, and no standing cap is on file.

Actions deliberately withheld:
- Did not close the request: landlord confirmation and tenant verification are still pending, and a closure with pending checklist items is not a valid closure (CAP-CLOSE).
- Did not dispatch or re-dispatch a contractor: the work is reported complete and no new spend is authorised — no cap is on file (APR-SPEND-OVER-CAP).
- Did not tell any party which firm holds the job, as the agency's own records disagree; recorded the conflict and asked the office instead.
- Did not state or attribute any cost; no amount appears anywhere in the file.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-TENANT, CAP-CLOSE, PRO-PAYMENTS, PRO-INSTRUCTIONS-FROM-CONTENT
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 2 Oct 2024 that the only WC fills by trickling and the bathroom basin cold tap does not work at all; the WC drains away normally and there are pets at the property. [index, event-001, event-002; high]
- F2: Urgency is routine: no emergency definition is met — the WC drains, water supply and other taps are available, no hazard keyword and no vulnerability is disclosed anywhere in the file. [event-002, get_case_details; high]
- F3: The agency raised and briefed a work order on 2 Oct and told the tenant a provider would attend. [event-006, event-007, event-008; high]
- F4: The only landlord message in the visible history is 'Thanks Ava' (2 Oct), replying to the agency's note that a job had been raised; it names no amount. [event-004, event-010, search_history; high]
- F5: No spend cap or standing limit for this landlord is on file, and no quote or cost figure appears anywhere in the case. [get_case_details, get_action_ledger; medium]
- F6: The tenant confirmed on 14 Oct that someone would be home for the 20 Oct PM slot; the slot was recorded as 2024-10-20 13:00. [event-024, event-027; high]
- F7: The provider missed the confirmed 20 Oct appointment; the case was held and the visit moved to the following day group, with the work reported done on 24 Oct. [event-034, event-037, event-039; high]
- F8: The provider reported the job complete on 24 Oct: a new Fluidmaster bottom-entry ball valve supplied and installed to the WC, with the basin taps reported fine by the tenants. [event-039; medium]
- F9: The landlord pays the contractor directly and the request was marked completed without payment through the agency. [event-040, event-041; high]
- F10: No management key was issued for the visit: the tenant stated someone would be home, which contradicts the boilerplate access line in the agency's own confirmation email. [event-024, event-032; medium]
- F11: A contractor called the tenant on 15 Nov 2024, three weeks after completion; the transcript records only the greeting, so the purpose is unknown. [event-042; low]

Conflicts between sources:
- Agency records disagree on which firm holds the job: Riverside Works is named in the email to the landlord and in the work-order brief; Willow Services is named in the tenant brief, every chaser and every booking confirmation. Three different contact numbers appear for the same job (07700 900781, 07700 900552, 07700 900511). → Not decided by me. Referred to the property manager (ACT-3) and the landlord asked which firm to record (ACT-1). Meanwhile routine steps continued at the address on the agency's own record; no party was told which firm is correct. (asked)
- Access method: the agency's confirmation email carries a boilerplate line that access was granted with the agency key, while the tenant stated someone would be home. → The tenant's own reply settles a tenant-owned fact (RTE-TENANT) and a specific statement beats boilerplate: no key was issued, so key return does not arise. (source_hierarchy)
- The original report says the basin cold tap is not working at all; the completion report says the basin taps were fine, with no work recorded on them. → Tenant asked to confirm both the WC fill and the basin tap before closure (ACT-2); the job will be reopened with the provider if the tap is still faulty. (asked)

Red flags:
- [data_quality] Four different provider names attach to this one job across the file — Riverside Works and Willow Services in agency records, plus 'Keystone Solutions' and 'Isaac Ingram from Beacon Works' in untrusted inbound call summaries — alongside three contact numbers. With the landlord paying the contractor direct, this carries a risk of a wrong or duplicate invoice. → Referred to the property manager for CRM correction and duplicate-invoice check (ACT-3); landlord asked to confirm the firm to record (ACT-1). No firm confirmed to any party by me.
- [data_quality] Inbound signatures are inconsistent with the case record: the contractor email signs 'Sawyer' (event-020), the tenant reply signs 'Maya Harper' (event-024) although the tenancy names Amelia Ingram & Amelia Dawson, and emails to the provider address 'Theo' and 'Ruben'. → Parties addressed only by the names on the case record; no name from a message body copied into another party's letter.
- [other] Contractor-to-tenant call on 15 Nov 2024, three weeks after the job was reported complete; the transcript contains no substance, so it is unknown whether something remains outstanding. → Flagged in the human task (ACT-3) and covered by the tenant verification request (ACT-2).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "030", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=key collect office keys | [] | allow |
| 4 | search_history | completed | query=Riverside Works | [{"event": "event-004", "timestamp": "2024-10-02 03:22:47 UTC", "channel": "Email", "from": "Agency / system", "to": "Landlord", "excerpt": "[2024-10-02 03:22:… | allow |
| 5 | search_history | completed | from_party=Landlord | [{"event": "event-010", "timestamp": "2024-10-02 05:04:33 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2024-10-02 05:04:… | allow |
| 6 | notify_landlord | completed | message=Flat 7, 31 Willowmere Road, Alderwick, ZZ4 0ZZ — plumbing r… | {"id": "ACT-1"} | CAP-NOTIFY |
| 7 | notify_tenant | completed | message=Dear Amelia Ingram & Amelia Dawson,  Flat 7, 31 Willowmere… | {"id": "ACT-2"} | CAP-NOTIFY |
| 8 | create_human_task | completed | queue=property_manager, title=Case 030 — agency records disagree on which plumber held th…, summary=Flat 7, 31 Willowmere Road, Alderwick, ZZ4 0ZZ. Plumbing jo… | {"id": "ACT-3"} | CAP-HUMAN-TASK |
| 9 | add_note | completed | note=Case 030 status review. Work reported complete by provider… | {"id": "ACT-4"} | CAP-LOG |
| 10 | put_on_hold | completed | reason=Waiting for Landlord — confirmation that the completed work…, until=3 working days from today | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the plumbing works at Flat 7, 31 Willowmere Road are complete and accepted, and that the contractor's invoice is being settled directly with you? (blocking; landlord_confirmation is a definition-of-done item and the request was marked completed without payment through the agency (event-040, event-041))
- Ask **landlord**: Which firm should be recorded as the instructed plumber for this job — Riverside Works (named to you at event-004) or Willow Services (all later correspondence, event-007/028)? (non-blocking; Our own records disagree; the landlord pays the contractor directly, so the wrong name on file risks a wrong or duplicate invoice)
- Ask **tenant**: Are both faults now resolved — the toilet filling at a normal rate, and the cold tap on the bathroom hand basin running properly? (blocking; The original report said the tap was not working at all (event-001); the only evidence it is fine is the provider's second-hand account (event-039))

Promises made or recorded:
- agency → landlord: Chase once more before closing if no reply within 3 working days by 3 working days from ACT-1 [open]
- agency → tenant: Reopen the job with the plumber if either fault persists; otherwise close after 3 working days by 3 working days from ACT-2 [open]
- agency → tenant: Provider to attend 20 Oct 2024 PM (confirmed slot) by 2024-10-20 13:00 [broken]
- provider → agency: Attend and complete the plumbing job by 2024-10-24 [kept]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
