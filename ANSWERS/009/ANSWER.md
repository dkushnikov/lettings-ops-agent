# ANSWER — Case 009 — Case 009: Front garden maintenance follow-up

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Tenant-done front garden tidy reported complete; held for photo confirmation and which-property confirmation, with the address discrepancy referred to the office.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation that the completed work and photos are for Flat 4, 174 Beacon Close, and re-send of the photos; 3-day wait from today's message (ACT-3, ACT-4).
**Last update:** 2024-03-06 09:44:07 UTC (event-023) · **Decided:** 2026-10-10 14:01 UTC
**Next step:** Tenant (Bennett) to confirm the garden completed is the front garden at Flat 4, 174 Beacon Close and re-send photos (3-day wait); office in parallel to confirm the Beacon Close / Lantern Quay discrepancy (ACT-2).

Definition of done (1/4 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — index / event-001: front garden maintenance picked up at inspection, categorised routine; no hazard, so no damage-limiting advice applicable (F7).
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — Tenant is doing the work himself (event-006, event-013); no spend and no contractor, so no landlord mandate or cap is engaged.
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No provider required — tenant-performed garden maintenance (event-006).
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No contractor visit needed; no access required (ACT-3 confirms to the tenant that no visit is needed).
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote exists; no cost to the landlord.
- [ ] work_result: Work result recorded from the provider — Tenant stated completion (event-013) and the agency recorded 'complete done' (event-023), but the reply evidencing it could not be parsed (event-020) and the property named in the chasers is inconsis…
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Photos promised (event-013) but none visible on the ticket (get_case_details: attachments_hidden 0); re-send requested (ACT-3).
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice — tenant carried out the work at no cost to the landlord (F3).
- [n/a] landlord_confirmation: Landlord confirmed completion — No landlord decision or spend arose on this ticket (F3).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; no visit arranged.
- [ ] closed: Request closed with a resolution that names who paid — Closure withheld pending photos and property confirmation (ACT-4); CAP-CLOSE requires the final checks first.

## 1. Decision

Did not close. The work is tenant-performed garden tidy with no spend and no contractor, and the agency has already treated it as finished (event-022, event-023) — but two things stop a clean closure: the completion photos are not on the ticket (the tenant's reply at event-020 could not be parsed, no attachment visible), and three chasers (event-011, event-016, event-017) ask about the garden at "Flat 2, 72 Lantern Quay, Eastmere, ZZ4 0ZZ" while the ticket and address block say Flat 4, 174 Beacon Close, Westmarsh. I recorded the conflict (ACT-1), referred the address discrepancy to the office rather than picking a side with a party (ACT-2), asked the tenant the single tenant-owned question — which garden the completed work and photos cover (ACT-3) — and put the case on hold for the tenant (ACT-4). No approval, dispatch or spend was needed or taken: no contractor is involved and no cost falls on the landlord.

Actions deliberately withheld:
- Did not close the request despite event-023 marking it 'complete done' — work result and documents are unevidenced (CAP-CLOSE).
- Did not tell the tenant which address is correct or that an error was made on another property's file — referred to the office instead (ESC-CONFLICT, rule on record conflicts).
- Did not state or imply that the tenant is liable for the garden or for any cost (PRO-TENANT-LIABILITY).
- Did not instruct a gardener or any contractor: no landlord cap is on file and no landlord approval exists in the history (APR-SPEND-OVER-CAP).
- Did not pass the tenant's family medical circumstances (event-007) to any third party (PRO-PII).

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-HUMAN-TASK, RTE-TENANT, ESC-CONFLICT, PRO-TENANT-LIABILITY, PRO-PII, CAP-CLOSE, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Case property of record is Flat 4, 174 Beacon Close, Westmarsh, ZZ5 5ZZ; the issue is front garden maintenance picked up at an inspection. [index, get_case_details, event-001; high]
- F2: The garden work is being done by the tenant personally, not by an instructed contractor: on 13 Feb he said he had not finished it due to a family medical situation and would do it that weekend and send a photo. [event-006, event-007; high]
- F3: No contractor has been instructed, no quote exists and no cost to the landlord arises on this ticket; the landlord does not appear in any visible event. [get_action_ledger, index; high]
- F4: On 26 Feb the tenant emailed that the work 'will be finished this evening' with photos 'tomorrow morning'. [event-013, event-014; medium]
- F5: Three outgoing chasers carry the Beacon Close address block but ask about the garden at 'Flat 2, 72 Lantern Quay, Eastmere, ZZ4 0ZZ'. [event-011, event-016, event-017; high]
- F6: The tenant's 6 March reply could not be parsed ('does not contain the client's answer'); the agency then recorded that the email came through and marked the matter 'complete done'. No photo attachment is visible on the ticket. [event-019, event-020, event-021, event-022, event-023, get_case_details; medium]
- F7: Safety pass: no gas, electrical, water, damp/mould, alarm or hazard keyword is reported or observed anywhere in the visible events; the only health reference is the tenant's mother having been in hospital, which is a family circumstance explaining delay, not an occupant hazard or loss of essential service. [event-007, index; high]

Conflicts between sources:
- Agency records disagree on which property's garden is being chased: ticket and address blocks say Flat 4, 174 Beacon Close; the body of three chasers says Flat 2, 72 Lantern Quay, Eastmere. → Not resolved by me. Referred to the office via human task (ACT-2) and the tenant asked to confirm which garden their completed work covers (ACT-3); no view on the address stated to any party. (asked)
- The ticket is marked 'complete done' (event-023) although the tenant's reply that triggered it could not be parsed and no photos are visible on the file. → Held rather than closed; tenant asked to re-send photos and confirm the property (ACT-3, ACT-4). (asked)

Red flags:
- [data_quality] Three outgoing emails to this tenant quote a different property's full address (Flat 2, 72 Lantern Quay, Eastmere) under the Beacon Close address block — a template or copy error that also disclosed another property's address to this tenant. → Conflict noted (ACT-1) and referred to the office for correction (ACT-2); not repeated to the tenant as fact.
- [data_quality] Tenant reply of 6 March could not be parsed and no photo attachment is on the ticket, yet the file was marked 'complete done' two minutes later. → Closure withheld; tenant asked to re-send photos (ACT-3), case put on hold (ACT-4).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "009", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Record conflict + evidence gaps. (1) Case property is Flat… | {"id": "ACT-1"} | CAP-LOG |
| 4 | create_human_task | completed | queue=property_management_office, title=Case 009 — chaser emails name a different property than the…, summary=Ticket property: Flat 4, 174 Beacon Close, Westmarsh ZZ5 5Z… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 5 | notify_tenant | completed | message=Good afternoon, and thank you for your email of 6 March — i… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | put_on_hold | completed | reason=Waiting for Tenant — confirmation that the completed front…, until=3 days from today (standard tenant wait) | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Please confirm the front garden work you have completed, and the photos you sent, relate to Flat 4, 174 Beacon Close, Westmarsh, ZZ5 5ZZ, and re-send the photos if they did not attach. (blocking; Completion evidence is not on the ticket (event-020 unparsed, no attachment) and three chasers named a different property (event-011, event-016, event-017). RTE-TENANT owns which property and the facts of the work.)
- Ask **property_manager**: Which property's front garden does Case 009 cover — Flat 4, 174 Beacon Close (ticket) or Flat 2, 72 Lantern Quay (quoted in three chasers)? Is there a parallel Lantern Quay ticket, or is this a template error to correct? (non-blocking; Agency records disagree and it changes whether the Beacon Close garden has actually been dealt with (ACT-2 raised).)

Promises made or recorded:
- agency → tenant: Once the photos and property confirmation arrive, the file is updated and the tenant will not be chased about this again; no visit and no cost to the tenant for this check. [open]
- tenant → agency: Send photos confirming the front garden work is complete by 27 February 2024 (promised 'tomorrow morning' on 26 Feb) [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
