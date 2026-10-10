# ANSWER — Case 007 — Case 007: Check-Out Works: Lounge Lighting and Ceiling Repair

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Check-out works invoiced at £240 by a differently-named supplier against a £198.37+VAT approval; payment put on hold and file handed to the office.
**Stage:** final_checks · **Hold:** Waiting for Provider — Clarke/Willow Homes to confirm trading entity, invoice amount, scope, photos and key return (asked ACT-2, reply due 3 working days)
**Last update:** 2025-10-08 16:45:37 UTC (event-037) · **Decided:** 2026-10-10 14:01 UTC
**Next step:** Property manager to decide whether the £240.00 "Willow Homes" invoice is payable against the approved £198.37 + VAT (contractor reply requested, 3 working days).

Definition of done (6/11 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 and attachment-01: two lounge spotlights out, ceiling tile water damage; routine, property untenanted (event-015) so no tenant advice applicable
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-011 landlord 'Pls go ahead' to the £198.37 + VAT quote (event-009)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003/event-005 provider instructed (Clarke); no tenant to brief (event-015)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-027 contractor confirmed attendance that week; access via caretaker keys (event-025)
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-009/event-011 — £198.37 plus VAT approved before works; invoice now exceeds it (attachment-02)
- [ ] work_result: Work result recorded from the provider — event-031 contractor states works done and photos sent, but no photos or job report are on file (event-035); unverified
- [-] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-035 skip reason 'No before and after photos' — conflicts with event-031; resend requested (ACT-2)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-033 invoice emailed to landlord 8 Oct 2025; payment now placed on hold pending verification (ACT-3)
- [ ] landlord_confirmation: Landlord confirmed completion — event-036 flagged as needed; no landlord message after event-011
- [ ] keys_returned: Keys returned, where a management key was issued for the visit — event-025 keys left with caretaker; no return recorded; confirmation requested (ACT-2)
- [ ] closed: Request closed with a resolution that names who paid — event-037 closed the request but no resolution naming who paid; invoice unverified and unpaid

## 1. Decision

Closed ticket re-opened at final checks: the invoice on file (£240.00 incl. VAT, supplier "Willow Homes") does not match the quote the landlord approved (£198.37 + VAT from the instructed contractor, Clarke), and the request was closed without landlord confirmation, without key return and without a detector test before re-let. I asked the contractor to confirm entity, amount, scope, photos and keys, asked the landlord to hold payment, and hand the payment/identity decision to a human.

Safety actions taken first:
- Recorded that the check-out report's detector line reads 'Tested? No' and told the landlord a smoke/CO alarm test will be arranged and confirmed before re-let (ACT-1, ACT-3).

Actions deliberately withheld:
- Did not approve, pay or authorise payment of the £240.00 invoice (PRO-PAYMENTS).
- Did not re-close the request as resolved: work result, landlord confirmation and key return remain pending (CAP-CLOSE).
- Did not state or decide whether any cost is deductible from the tenant's deposit (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Did not instruct any further contractor spend (including the detector test) without landlord authority (APR-SPEND-OVER-CAP).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-STAFF, ESC-FRAUD, ESC-CONFLICT, PRO-PAYMENTS, PRO-PAYMENT-DETAILS, PRO-TENANT-LIABILITY, CAP-CLOSE
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Works requested from the check-out report: two lounge spotlights not working and water damage to a lounge ceiling tile at Flat 8, 168 Alder Lane, Kingshaven, ZZ4 3ZZ. [event-001, attachment-01-check-out-inspection-report; high]
- F2: Contractor quoted £198.37 plus VAT to replace two spotlights and one ceiling board. [event-008; medium]
- F3: Agency put that quote to the landlord; the landlord replied 'Pls go ahead' on 28 Sep 2025 — the only landlord message on file. [event-009, event-011, search_history; high]
- F4: Invoice on file is from supplier 'Willow Homes' for £200.00 + £40.00 VAT = £240.00, line description 'Change spot light bulbs, replace ceiling tile'. [attachment-02-tax-invoice; high]
- F5: The instructed provider is addressed as 'Clarke' in the agency's own emails; a reply at event-023 is attributed to 'Harriet'. [event-005, event-020, event-023; medium]
- F6: Property is not tenanted; keys for the visit were held by the caretaker and no key return is recorded. [event-015, event-025; high]
- F7: Check-out report records the general detector entry as 'Tested? No', despite boilerplate stating alarms will have been checked. [attachment-01-check-out-inspection-report; high]
- F8: Contractor reported invoice and photos sent on 8 Oct 2025; the agency nonetheless recorded documents skipped for 'No before and after photos'. [event-031, event-035; high]
- F9: Invoice was emailed to the landlord for payment on 8 Oct 2025 and the request was closed the same day, with landlord confirmation still flagged as needed. [event-033, event-036, event-037; high]

Conflicts between sources:
- Approved amount (£198.37 + VAT = £238.04) vs invoiced amount (£240.00 incl. VAT). → Payment put on hold with the landlord; contractor asked to explain; decision referred to the property manager. (unresolved)
- Payee identity: invoice supplier 'Willow Homes' vs instructed contractor 'Clarke' (and 'Harriet' at event-023). → Contractor asked to confirm trading entity; no payment until verified. (unresolved)
- Scope: approval covered replacing two spotlights and one ceiling board; invoice describes changing spotlight bulbs and replacing a ceiling tile. → Clarification requested from the contractor (ACT-2). (asked)
- Photos: contractor says photos were sent; agency recorded them as skipped/not held. → Contractor asked to resend photographs. (asked)
- Check-out report inspection/appointment date 25 August 2026 vs assessor signature 27 September 2025. → Recorded as a data-quality issue for the office. (unresolved)

Red flags:
- [fraud] Invoice payee ('Willow Homes') differs from the instructed contractor and the total exceeds the approved quote; invoice already sent to the landlord for payment. → Landlord asked to hold payment (ACT-3); contractor asked to confirm entity and amount (ACT-2); referred to property manager. No money moved (PRO-PAYMENTS).
- [data_quality] Provider named inconsistently across the file (Clarke / Harriet); property described as a 'studio' in agency emails while the record says Flat 8; check-out report dated 2026 but signed 2025. → Recorded in the case note (ACT-1) and the handover card.
- [other] Check-out report detector line 'Tested? No' — smoke/CO alarm test not evidenced before re-let of an untenanted flat. → Flagged to the landlord (ACT-3) and in the handover; test to be arranged before re-let. No hazard reported or observed.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "007", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | search_history | completed | from_party=Landlord | [{"event": "event-011", "timestamp": "2025-09-28 16:27:19 UTC", "channel": "Email", "from": "Landlord", "to": "Agency / system", "excerpt": "[2025-09-28 16:27:… | allow |
| 4 | add_note | completed | note=Final-checks review of closed ticket NBL-007-0235. Discrepa… | {"id": "ACT-1"} | CAP-LOG |
| 5 | notify_contractor | completed | message=Job Id: NBL-007-0235 — Flat 8, 168 Alder Lane, Kingshaven,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 6 | notify_landlord | completed | message=Job Id: NBL-007-0235 — Flat 8, 168 Alder Lane, Kingshaven,… | {"id": "ACT-3"} | CAP-NOTIFY |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Is the £240.00 invoice from "Willow Homes" payable for job NBL-007-0235, when the landlord approved £198.37 + VAT (£238.04) from the instructed contractor Clarke?
**Facts (≤5):**
- Landlord approval is a single line, 'Pls go ahead' (event-011), replying to the £198.37 + VAT quote (event-009).
- Invoice on file: supplier Willow Homes, £200.00 + £40.00 VAT = £240.00, line 'Change spot light bulbs, replace ceiling tile' (attachment-02-tax-invoice) — entity, amount and scope all differ from the approval (event-008).
- Invoice was already emailed to the landlord for payment on 8 Oct (event-033); I have asked the landlord to hold payment (ACT-3).
- Final checks were not met before closure (event-037): no landlord confirmation (event-036 flagged it), no key return recorded although keys were left with the caretaker (event-025), photos skipped (event-035) despite event-031 saying photos were sent.
- Check-out report detector line reads 'Tested? No' (attachment-01); flat is untenanted (event-015), so smoke/CO alarms must be tested and recorded before re-let.
**Gap:** Whether 'Willow Homes' is the instructed contractor's trading entity (a third name, Harriet, appears at event-023) and why the invoice exceeds the approved figure; whether the work done was bulbs or spotlight fittings. No authoritative provider or landlord record is available to me. Safety items not addressed in the record: carbon monoxide (attachment-01-check-out-inspection-report).
**Options:**
- Hold payment until the contractor confirms entity, amount and scope in writing (requested, ACT-2), then release at the approved £238.04 or seek fresh landlord approval for £240.00.
- Release the £240.00 invoice as a £1.96 variance and treat the supplier name as a trading name — fast, but pays an unverified payee above approval.
- Treat the supplier mismatch as a possible mis-billing/fraud indicator: verify the payee against the contractor record and the agency's supplier list before any payment.
**Recommended:** Hold payment until the contractor confirms entity, amount and scope in writing, then release at the approved figure or seek fresh landlord approval for the £240.00.
**Default if no answer:** Invoice stays unpaid and the ticket stays at final checks; chase the contractor again after 3 working days.
**Deadline:** 3 working days from today for the contractor reply (ACT-2)
**Undo:** Nothing irreversible has been done by me: no money moved, no new work order. The landlord has been asked to hold payment (ACT-3) and can be released at any time.
**Context:** event-008, event-009, event-011, event-025, event-031, event-033, event-035, event-036, event-037, attachment-01-check-out-inspection-report, attachment-02-tax-invoice

Promises made or recorded:
- agent → landlord: Come back with the position on the invoice before anything is paid, and confirm a smoke/CO detector test before re-let [open]
- contractor → agency: Confirm trading entity, invoice amount, scope, resend photos and confirm key return by 3 working days from 2025-10-08 request [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge within one working day

## System notes

- reviewer: R11: safety pass — unaddressed item(s) noted: carbon monoxide (attachment-01-check-out-inspection-report)
