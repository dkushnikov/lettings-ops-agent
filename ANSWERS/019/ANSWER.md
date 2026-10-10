# ANSWER — Case 019 — Case 019: Garden Maintenance Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Garden clearance done and invoiced, but the ticket closed with landlord confirmation and the levelling/gravel scope outstanding; landlord asked, case held.
**Stage:** on_hold · **Hold:** Waiting for Landlord — confirmation of completion and of the invoiced amount (event-038), plus a decision on quoting the levelling and gravel; 3-day wait from today's email (ACT-4).
**Last update:** 2025-04-16 09:16:13 UTC (event-044) · **Decided:** 2026-10-10 14:05 UTC
**Next step:** Landlord (Jenkins) to confirm the clearance is complete and the invoice matches their approval, and to say whether to quote the levelling/gravel (emailed ACT-4; 3-day clock). In parallel the property manager resolves the provider/price conflict and the rent deduction (ACT-2).

Definition of done (6/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged and acknowledged to tenant event-004; routine garden works, no emergency definition met
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-025 landlord's own message: 'Please go ahead with the removal' — covers the clearance only
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-034 maintenance provider assigned; event-033 new provider invoicing by email (identity conflicts with event-009)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-029 slots offered to tenant; event-031 records the work as carried out
- [ ] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No landlord message names an amount; event-009 (£500+VAT) and event-019 (~£600) conflict and event-036 is an agency note, not a landlord approval; invoice amount not on file (event-038 attachment una…
- [x] work_result: Work result recorded from the provider — event-031 'This was done, awaiting the invoice from contractor'; event-037 task moved to Result
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-042 skip reason 'not applicable'; no photos or invoice copy on file
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-038 invoice emailed to landlord
- [ ] landlord_confirmation: Landlord confirmed completion — event-043 'Need confirmation from landlord'; no landlord reply in history; chased ACT-4
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant was at the property for access (event-016, event-029)
- [ ] closed: Request closed with a resolution that names who paid — event-044 closed the request, but quote approval, landlord confirmation and the levelling/gravel scope remain open; case reopened and held (ACT-5)

## 1. Decision

Ticket was closed (event-044) with the playbook's final checks incomplete: the landlord never confirmed completion (event-043 flagged this one minute before closure), no invoice amount is on file, and the levelling and gravel parts of the tenant's request (event-001) were never quoted or authorised — the landlord's own approval covers the removal only (event-025). I did not instruct any contractor or authorise any spend: there is no standing cap on file and no landlord approval naming an amount (APR-SPEND-OVER-CAP). In-authority steps taken: internal note of the findings; tenant updated with the status and the fact that levelling/gravel await the landlord; landlord asked to confirm completion, check the invoice against their approval, and decide whether to quote the remaining scope; human task raised with the office for the provider/price conflict between agency records and for the rent-deduction stated in event-038 (PRO-PAYMENTS is outside my authority). Case reopened and held pending the landlord's reply.

Safety actions taken first:
- Safety pass run over all artefacts: no gas, CO, electrical, water-ingress, damp/mould, asbestos, injury or vulnerable-occupant content found; 'specialised builders material' (event-019) refers to disposal cost, with no hazard reported or observed. No emergency route triggered.

Actions deliberately withheld:
- Did not close the request: quote approval and landlord confirmation are still pending (event-043).
- Did not instruct a contractor for the levelling/gravel: no standing cap on file and no landlord approval naming an amount (APR-SPEND-OVER-CAP).
- Did not act on or endorse the rent deduction stated in event-038 (PRO-PAYMENTS).
- Did not tell any party which provider or price is correct; the conflict went to the office instead (ACT-2).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-TENANT, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant requested four items at Flat 25, 185 Copperfield Walk: removal of rubbish/construction waste, levelling, gravel covering, making the garden usable. [index, event-001; high]
- F2: The landlord's only own-message approval reads 'Please go ahead with the removal' and names no amount. [event-025; high]
- F3: Agency records give conflicting provider and price: £500+VAT with Harbour Compliance 'approved' (event-009), ~£600 via Oakley's contractor (event-019), and a new provider invoicing by email with no portal job (event-033). [event-009, event-019, event-033; high]
- F4: The clearance was carried out and the invoice was emailed to the landlord; the invoice attachment is unavailable, so no final amount is on file. [event-031, event-038; high]
- F5: Landlord confirmation was recorded as outstanding and the request was closed one minute later with no landlord reply in the history. [event-043, event-044; high]
- F6: The agency told the landlord it would process the invoice and deduct it from the rental amount. [event-038; high]
- F7: No gas, electrical, water, damp/mould, asbestos or occupant-vulnerability content appears in any artefact; the tenant's 'safe' refers to the unusable garden surface. [event-001, search_history; medium]
- F8: No landlord standing spend cap is on file in this case record. [get_case_details, get_action_ledger; medium]

Conflicts between sources:
- Who carried out the job and at what price: Harbour Compliance at £500+VAT (event-009) vs Oakley's contractor at ~£600 (event-019) vs an unnamed new provider invoicing by email (event-033). → Not resolved in a message to any party; conflict recorded and referred to the property manager (ACT-2), while routine steps (tenant update, landlord confirmation chase) continued. (asked)
- Closure status: event-044 states all checks completed, but event-043 records landlord confirmation still needed and no quote approval naming an amount exists. → The specific line (event-043, confirmation needed) beats the general closure line; ticket treated as open and placed on hold. (source_hierarchy)

Red flags:
- [data_quality] Request closed with final checks incomplete (no landlord confirmation, no invoice copy, no amount, documents skipped as 'not applicable'). → Recorded in note ACT-1 and human task ACT-2; ticket reopened and held.
- [other] Agency stated it would deduct the contractor invoice from the rental amount — a money movement outside agent authority (PRO-PAYMENTS), made without a verified invoice amount. → Referred to the property manager for verification (ACT-2); no payment action taken by me.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "019", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=invoice amount VAT paid | [] | allow |
| 4 | search_history | completed | from_party=Tenant | [] | allow |
| 5 | add_note | completed | note=Review of closed ticket (event-044 "All checks have been co… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed | queue=property_manager, title=Case 019 closed with items outstanding — provider/price con…, summary=Flat 25, 185 Copperfield Walk. Ticket closed at event-044 w… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_tenant | completed | message=Hello, an update on your garden request for Flat 25, 185 Co… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_landlord | completed | message=Address: Flat 25, 185 Copperfield Walk, Alderwick, ZZ4 0ZZ.… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | put_on_hold | completed | reason=Waiting for Landlord — confirmation that the clearance is c…, until=3 days from today's contact | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the garden clearance is complete and that the invoice emailed to you on 16 April matches the amount you approved? Our file shows two different figures (£500 + VAT at event-009, around £600 at event-019) and we hold no copy of the invoice. (blocking; Landlord confirmation and invoice sign-off are landlord-owned decisions (RTE-LANDLORD); event-043 flagged confirmation outstanding and it is not in the history.)
- Ask **landlord**: Your approval (event-025) covered the removal only. Do you want us to obtain a quote for levelling the ground and laying gravel, or should the request be closed at the clearance? (blocking; The remaining scope is spend at the landlord's cost with no standing cap on file (APR-SPEND-OVER-CAP).)
- Ask **tenant**: Is anything still left in the garden after the clearance, and is the ground surface still unusable? (non-blocking; Confirms the work result on the ground before the landlord decides on the remaining scope (RTE-TENANT).)

Promises made or recorded:
- agency → tenant: Come back to the tenant once the landlord replies on levelling and gravel by On landlord reply [open]
- agency → landlord: Hold the file until the landlord responds on completion, invoice check and remaining scope by 3 days from ACT-4 [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
