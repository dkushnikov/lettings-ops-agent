# ANSWER — Case 033 — Case 033: Bathroom Tap Plumbing Request

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Tap repair at Flat 19 was closed on a completion report naming a different address; I reopened to hold, queried provider and tenant, and flagged it to the office.
**Stage:** on_hold · **Hold:** Waiting for Provider — Juniper Solutions to confirm which property the completed works, photos and invoice relate to and whether the 13/10/2026 visit at Flat 19 went ahead; reply sought within 2 working days (ACT-3, ACT-5).
**Last update:** 2026-10-15 00:16:26 UTC (event-044) · **Decided:** 2026-10-10 13:29 UTC
**Next step:** Juniper Solutions to confirm the property and supply photos/invoice for Flat 19, 159 Juniper Mews (2 working days); office to decide whether the closure stands before any invoice is paid.

Definition of done (6/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Issue logged and categorised as a plumbing request (event-001, event-010); urgency set routine (use_playbook); damage-limiting advice given to the tenant (ACT-4)
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-008 — landlord's own message agreeing a contractor be instructed
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-009, event-010, event-011 — Juniper Solutions assigned; tenant and provider briefed
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-033, event-034, event-035 — 13/10/2026 12:00 confirmed with tenant and provider
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-023 landlord approval; event-026 recorded as approved. Amount and VAT not verifiable — quote attachment unavailable (get_attachment)
- [ ] work_result: Work result recorded from the provider — event-037 reports completion but names a different property (Flat 21, 161 Meadow Row, Cedarford); provider and tenant asked to confirm (ACT-3, ACT-4)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-040 skipped as 'Not required' despite photos/invoice being requested at event-029; photos/invoice for this address requested from the provider (ACT-3)
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No event shows an invoice forwarded to the landlord; not forwarded by me while the invoice may relate to another property (ACT-1, ACT-2)
- [ ] landlord_confirmation: Landlord confirmed completion — event-041 flagged confirmation still needed; no landlord confirmation of completion in the history
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-043 — keys return confirmed
- [ ] closed: Request closed with a resolution that names who paid — event-044 closed the request, but the resolution names no payer and work_result, documents, invoice and landlord confirmation are unresolved; ticket placed back on hold (ACT-5)

## 1. Decision

The ticket was closed (event-044) on a completion message that names a different property (event-037), with documents skipped (event-040) and landlord confirmation still outstanding (event-041). I did not confirm completion to the landlord, forward any invoice, or raise a second work order. I recorded the conflict (ACT-1), referred the mis-matched completion/invoice and the premature closure to the office (ACT-2), asked the provider which property the works, photos and invoice relate to and whether the 13/10 visit at Juniper Mews went ahead (ACT-3), asked the tenant whether a plumber attended and the tap is repaired, with damage-limiting advice (ACT-4), and placed the request on hold pending the provider (ACT-5). No cost is stated anywhere: the quote attachment referenced at event-020 is not retrievable.

Safety actions taken first:
- Gave the tenant damage-limiting advice: contain the leak, avoid the shower if water cannot be contained, use the stopcock and call us as an emergency if water reaches electrics or cannot be stopped (ACT-4)
- Raised the unverified gas safety check / TRV thread with the office rather than treating it as done (ACT-2)

Actions deliberately withheld:
- Did not forward any invoice to the landlord or confirm completion while the completion evidence names another property (PRO-PAYMENTS, ESC-CONFLICT)
- Did not re-close the request: final-check items remain pending (CAP-CLOSE)
- Did not raise a second work order or re-dispatch, to avoid duplicating the instructed job (playbook: contractor-failure)
- Did not state any quote or invoice amount: the quote attachment is not retrievable
- Did not decide who pays for the works or any mis-billed invoice (PRO-TENANT-LIABILITY)

## 2. Authority and evidence

Authority cited: CAP-LOG, CAP-NOTIFY, CAP-HUMAN-TASK, RTE-CONTRACTOR, RTE-TENANT, RTE-LANDLORD, ESC-CONFLICT, CAP-CLOSE, PRO-PAYMENTS, PRO-TENANT-LIABILITY, CLK-S11, CLK-GAS-CP12
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the bathroom tap squirting water when the shower runs at Flat 19, 159 Juniper Mews, Kingshaven, ZZ9 2ZZ on 2026-10-03. [index, event-001, get_case_details; high]
- F2: The landlord's own message agreed to a contractor being instructed for this property. [event-008; high]
- F3: Juniper Solutions was assigned; tenant and contractor were briefed. [event-009, event-010, event-011; high]
- F4: The contractor reported attending, said the bath taps need replacing and recommended changing the TRV, and a quote was sent to the landlord. [event-019, event-020; medium]
- F5: The landlord's own message approved raising an order for the works at this property; the system recorded the quote as approved. [event-023, event-026; high]
- F6: A visit was booked and confirmed with tenant and contractor for 13/10/2026 12:00. [event-032, event-033, event-034, event-035; high]
- F7: The completion message with images and invoice names Flat 21, 161 Meadow Row, Cedarford, ZZ5 7ZZ — not this ticket's property. [event-037; high]
- F8: Document upload was skipped with reason 'Not required' although photos and an invoice had been requested from the provider. [event-029, event-040; high]
- F9: Landlord confirmation of completion was flagged as still needed, and the request was then closed. [event-041, event-044; high]
- F10: Keys return was confirmed, with a validation line 'Priority cannot be decreased to 0. Current priority is 1.' [event-043; high]
- F11: No quote amount is available: the attachment referenced at event-020 could not be retrieved (get_attachment returned 'no attachment named attachment-03-document'). [event-020, get_attachment; high]

Conflicts between sources:
- The ticket's property is Flat 19, 159 Juniper Mews, Kingshaven ZZ9 2ZZ, but the completion message carrying the images and invoice names Flat 21, 161 Meadow Row, Cedarford ZZ5 7ZZ. This changes the action: the job may be unfinished here, or another property's invoice may be billed to this landlord. → Conflict recorded (ACT-1), office task raised (ACT-2), provider asked which property the works relate to (ACT-3) and tenant asked whether the tap was repaired (ACT-4). Ticket placed on hold (ACT-5); no invoice forwarded and no completion confirmed to the landlord. (asked)
- An earlier contractor message said a 'service and gas safety check' was scheduled and later recommended a TRV change; neither is within the reported tap fault and no gas safety record is available to check. → Non-blocking question put to the provider about any gas work and the engineer's Gas Safe status; flagged to the office for CP12 verification (CLK-GAS-CP12). (asked)
- The visit stage was first recorded as confirmed for 03/10/2026, a date before/on the day of the report and before the quote was approved. → Recorded as a data-quality issue in the office task; superseded in practice by the 13/10/2026 booking (event-033). (unresolved)

Red flags:
- [data_quality] Completion message with images and invoice names a different property (quoted: 'Flat 21, 161 Meadow Row, Cedarford, ZZ5 7ZZ') from the ticket's Flat 19, 159 Juniper Mews; the ticket was nonetheless marked completed and closed. → Conflict noted (ACT-1), office task raised (ACT-2), provider queried (ACT-3), tenant queried (ACT-4), ticket on hold (ACT-5); no invoice forwarded, no payment, no completion confirmed
- [fraud] Risk that an invoice for another address is billed against this landlord's property; amount not verifiable as the quote attachment is missing. → Referred to property_manager before any payment (ACT-2); PRO-PAYMENTS observed
- [safety_hazard] Contractor messages mention a 'service and gas safety check' and a TRV change, outside the reported tap fault and unverified against any gas safety record. → Non-blocking question to the provider on gas work and Gas Safe registration (ACT-3); flagged to the office (ACT-2)
- [data_quality] Visit recorded as confirmed for 03/10/2026, the day of the report and before any quote approval; later superseded by the 13/10/2026 booking. → Recorded in the office task (ACT-2)

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "033", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-03-document | {"error": "no attachment named attachment-03-document"} | allow |
| 4 | search_history | completed | query=invoice completed images | [] | allow |
| 5 | add_note | completed | note=Conflict on final checks. Completion evidence (event-037, c… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed | queue=property_manager, title=Case 033 closed on completion evidence naming a different p…, summary=Ticket: tap squirting at Flat 19, 159 Juniper Mews, Kingsha… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_contractor | completed | message=Dear Juniper Solutions, re the Plumbing request at Flat 19,… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_tenant | completed | message=Dear Leo Fletcher, regarding your report of the bathroom ta… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | put_on_hold | completed | reason=Waiting for Provider — completion evidence (event-037) name…, until=2 working days from today for the provider's reply | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Review case 033: The record carries red flags that need a human's confirmation (fraud: Risk that an invoice for another address is billed against this landlord's property; amount not verifiable as the quote attachment is missing.; safety_hazard: Contractor messages mention a 'service and gas safety check' and a TRV change, outside the reported tap fault and unverified against any gas safety record.); the case cannot end as needs_info.
**Facts (≤5):**
- Risk that an invoice for another address is billed against this landlord's property; amount not verifiable as the quote attachment is missing.
- Contractor messages mention a 'service and gas safety check' and a TRV change, outside the reported tap fault and unverified against any gas safety record.
**Gap:** The record carries red flags that need a human's confirmation (fraud: Risk that an invoice for another address is billed against this landlord's property; amount not verifiable as the quote attachment is missing.; safety_hazard: Contractor messages mention a 'service and gas safety check' and a TRV change, outside the reported tap fault and unverified against any gas safety record.); the case cannot end as needs_info.
**Default if no answer:** Case stays open in the human queue; no automated action.

Promises made or recorded:
- agency → tenant: Confirm the position with the provider and come back to the tenant; rebook if the tap was not repaired by on the provider's reply (2 working days sought) [open]
- agency → contractor: Nothing processed until the provider confirms which property the works and invoice relate to by 2 working days [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-GAS-CP12 [in_force]: Gas safety record renewed every 12 months

## System notes

- reviewer: R2: red flags (fraud, safety_hazard) → escalated (checked before any needs_info rule)
