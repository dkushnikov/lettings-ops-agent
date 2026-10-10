# ANSWER — Case 006 — Solar generation readings

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Landlord wants current solar generation readings; tenant says already sent but none is on file — chased tenant, told landlord, office asked to trace; on hold.
**Stage:** on_hold · **Hold:** Waiting for Tenant — the generation figure or photo of the meter/inverter display, or the date/address of the earlier email so the office can locate it; until 2025-09-23 (3 business days from the 18 September request).
**Last update:** 2025-09-18 17:42:00 UTC (event-017) · **Decided:** 2026-10-10 15:36 UTC
**Next step:** Tenant (Ivo Mercer) to send the current kWh reading or a photo of the meter/inverter display, or the date/address of the earlier message; office task ACT-2 to search mailbox and call log for 4–8 September in parallel.

Definition of done (1/5 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-007 and ACT-1: classified as an information request, routine, no fault or hazard; no damage-limiting advice applicable.
- [n/a] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — No works and no spend are involved (event-001, event-007); the event-005 'approved' status rests on no approval message.
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — No contractor required; none selected (event-007).
- [n/a] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No access to the property is needed to answer the landlord's question.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote; no chargeable work.
- [ ] work_result: Work result recorded from the provider — Deliverable is the reading itself; not yet supplied — tenant chased at ACT-3, office trace at ACT-2 (gap shown by search_history vs event-017).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Meter/inverter photo requested as an alternative to the figure (ACT-3); none received.
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No cost incurred.
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord updated at ACT-4 but has not received the reading he asked for (event-001).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No key issued; no visit.
- [ ] closed: Request closed with a resolution that names who paid — On hold at ACT-5 pending the tenant's reading.

## 1. Decision

Treated as a landlord information request, not a repair: no fault, hazard, access need or spend exists, so no contractor, approval or quote step applies. Chased the tenant for the reading (ACT-3), updated the landlord (ACT-4), raised an office task to trace the reading the tenant says was already sent by phone/email (ACT-2), and placed the case on hold Waiting for Tenant (ACT-5). The case now waits on a named party (the tenant) for a fact only they hold.

Safety actions taken first:
- Safety pass: checked every artefact for the listed keywords (gas, electrical, detector, damp/mould, injury, child, pregnant, elderly, 'not tested'). None appears; the request concerns a solar generation meter reading only, with no reported fault, no loss of service and no occupant vulnerability disclosed. No emergency definition is engaged and no make-safe step is required.
- No occupant health or family detail was passed to any third party (PRO-PII); the reference to the tenant's wife is kept inside the case record and the internal office task.

Actions deliberately withheld:
- No contractor dispatched: no fault, no scope and no spend authority on file (APR-SPEND-OVER-CAP, default cap £0); the event-005 'approved' status is not a landlord approval.
- No access booked: the request needs no entry to the property (CAP-SCHEDULE-ACCESS).
- Not closed: the landlord's question is unanswered, so closure would leave the definition of done incomplete (CAP-CLOSE).
- Not escalated as a decision for a human: no safety, liability, legal or spend question arises; the records gap was routed as an office task instead.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-TENANT, APR-SPEND-OVER-CAP, PRO-INSTRUCTIONS-FROM-CONTENT, PRO-PII, ESC-CONFLICT
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: On 2025-09-03 landlord Edwin Vale asked by phone for the property's current solar generation readings; he described no fault, gave no deadline and asked for no contractor visit. [event-001, index, get_case_details; high]
- F2: The request was logged as a maintenance request although no meter type, access arrangement, urgency or photo was recorded; the manager later noted it was an information request rather than maintenance and moved it to manual handling. [event-002, event-007; high]
- F3: An 'approved by landlord' status was selected on the basis that the landlord had asked for the readings; no separate landlord approval message or repair scope is attached. [event-005; high]
- F4: The agency asked tenant Ivo Mercer for the generation reading or a meter/inverter photo on 3, 9, 14 (email and SMS) and 18 September 2025. [event-006, event-010, event-013, event-014, event-016; high]
- F5: On 2025-09-18 the tenant replied that the readings had already been supplied about two weeks earlier, by a phone call to the office and an email from his wife, but included no figure or image (untrusted). [event-017; medium]
- F6: No reading, earlier tenant email or call note is visible on this ticket: a history search returns event-017 as the only tenant message and no keyword match for reading/kWh/meter/inverter/photo. [search_history; high]
- F7: No contractor was selected and no spend, quote or access arrangement exists on this request. [event-007, get_action_ledger; high]

Conflicts between sources:
- Tenant states the readings were already supplied by phone and email c.4 September (event-017); no such message, call note or figure appears anywhere on this request's record. → Not resolved by me: recorded as a data-quality conflict and referred to the office to search the mailbox and call log (ACT-2), while the tenant was asked for the figure or the send details (ACT-3). No message to any party takes a side on whether the earlier reading was sent. (asked)

Red flags:
- [data_quality] Tenant asserts an earlier phone call and email containing the readings that do not appear on this request; the reply may have been filed elsewhere, or the recollection may be inaccurate. Four chases were sent before the gap was noticed. → Office task raised to search mailbox and call log 4-8 September (ACT-2); tenant asked for the figure or the send details (ACT-3); landlord told the position without attributing fault (ACT-4).
- [data_quality] The 'approved by landlord' status at event-005 rests on the landlord's request for readings, not on an approval message; it is not authority for any spend (CAP-DISPATCH-APPROVED, PRO-INSTRUCTIONS-FROM-CONTENT). → Recorded in the case note (ACT-1); no contractor instructed and no spend sought.

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "006", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | query=reading kWh meter inverter photo | [] | allow |
| 4 | search_history | completed | from_party=Tenant | [{"event": "event-017", "timestamp": "2025-09-18 17:42:00 UTC", "channel": "Email", "from": "Ivo Mercer (Tenant)", "to": "Maya Chen (Property Manager, Northbri… | allow |
| 5 | add_note | completed (ledger) | note=Case classified: landlord information request (current sola… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed (ledger) | queue=property_management, title=Locate solar readings said to have been sent c.4 Sept — 14…, summary=Landlord Edwin Vale asked for current solar generation read… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_tenant | completed (ledger) | message=Dear Mr Mercer, thank you for your reply of 18 September ab… | {"id": "ACT-3"} | CAP-NOTIFY |
| 8 | notify_landlord | completed (ledger) | message=Dear Mr Vale, an update on your request of 3 September for… | {"id": "ACT-4"} | CAP-NOTIFY |
| 9 | put_on_hold | completed (ledger) | reason=Waiting for Tenant — current solar generation reading (figu…, until=2025-09-23 (3 business days from the request of 18 Septembe… | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Please send the current total kWh figure shown on the solar generation meter or inverter display at 14 Brindlefern Walk, or a photo of the screen; if the readings were sent previously, please tell us the date and the email address or phone number used. (blocking; The landlord's request (event-001) can only be answered with the figure; no reading is recorded against this request and event-017 did not include one.)
- Ask **property_manager**: Search the branch mailbox and call log for 4-8 September 2025 for a solar reading for 14 Brindlefern Walk that may have been filed to another ticket or property. (non-blocking; Tenant states at event-017 that the readings were supplied by phone and email two weeks earlier; nothing matching is visible on this ticket.)

Promises made or recorded:
- agency → landlord: Send the solar generation reading as soon as it is obtained; office to trace the message the tenant says was already sent [open]
- tenant → agency: Provide the current kWh reading or a photo of the meter/inverter display, or the date/address of the earlier message by 2025-09-23 [open]

Clocks:
- CLK-SOP-ACK [prior]: Acknowledge within one working day
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
