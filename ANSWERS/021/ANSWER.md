# ANSWER — Case 021 — Hot-water service report

**Disposition:** NEEDS_INFO · **Urgency:** urgent · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** No hot water since 6 May on the landlord's own-contractor route; completion unverified, so I chased the tenant for confirmation and the landlord for the plumber's report, and held the case.
**Stage:** on_hold · **Hold:** Waiting for Tenant — confirmation hot water/boiler power restored and letterbox detail (reply-by 19 May 17:00); in parallel Waiting for Landlord — plumber's report/invoice and confirmation of any gas or electrical work (same reply-by).
**Last update:** 2025-05-16 16:05:00 UTC (event-021) · **Decided:** 2026-10-10 15:43 UTC
**Next step:** Tenant (Iris Vale) to confirm by 19 May 17:00 whether hot water and boiler power are working and describe the letterbox fault; if still not working, or if no reply, the property manager re-opens the repair with the landlord and seeks authority to instruct an agency contractor.

Definition of done (2/8 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-003, event-004, event-005 — fault taken from the tenant, categorised Electrical, urgency set to urgent; tenant had already checked the boiler switch (event-001).
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-010, event-015 — landlord chose to use his own contractor; no agency spend authorised or needed.
- [ ] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-010, event-018 — landlord's own plumber attended but was never named to the agency; tenant was told the landlord would arrange the work (event-008).
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot was ever confirmed to the agency; attendance on 14 May is reported second-hand (event-018).
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — Landlord-managed repair at the landlord's own cost; no quote came to the agency.
- [ ] work_result: Work result recorded from the provider — event-018 — hearsay only; report requested from the landlord (ACT-2) and confirmation from the tenant (ACT-1).
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos, report or gas/electrical check record on file; requested at ACT-2.
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — The landlord instructed and will pay his own contractor directly (event-010); no agency invoice arises.
- [ ] landlord_confirmation: Landlord confirmed completion — event-018 — landlord believes it is fixed but gave no description or documentation; written confirmation requested (ACT-2).
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key was issued; access was handled by the household (event-003, event-008).
- [ ] closed: Request closed with a resolution that names who paid — Case on hold to 19 May 17:00 (ACT-4); open secondary report of a faulty letterbox (event-017).

## 1. Decision

Kept the case open on the landlord-managed route and did not instruct an agency contractor: the landlord elected to use his own contractor (event-010, event-015), there is no standing spend cap on file and no landlord approval naming an amount, so APR-SPEND-OVER-CAP blocks any dispatch. Completion is unverified — the only evidence is the landlord relaying a text from his plumber (event-018), with no report, invoice or record of gas/electrical checks, and no tenant confirmation (event-019, event-020 unanswered). Asked the tenant to confirm restoration and to describe the letterbox fault promised a follow-up on 13 May (ACT-1), and asked the landlord for the plumber's report/invoice, confirmation of any gas or electrical work and the engineer's registration, plus a spend limit if he wants us to take over (ACT-2). Case on hold to 19 May 17:00 (ACT-4). No liability decided (PRO-TENANT-LIABILITY).

Safety actions taken first:
- Asked the landlord to confirm whether any gas appliance or electrical work was done on the boiler and by whom, with Gas Safe / NICEIC registration (ACT-2) — the fault was logged as electrical (event-005) and a plumber attended (event-018).
- Asked the tenant whether the front door still locks and closes securely in connection with the letterbox fault, and told them to report immediately if the property is insecure (ACT-1) — an insecure property is an emergency under the rulebook.
- Occupant language need and the presence of birds held in the case record only; contractors to be told the access window and 'birds present, keep doors and windows shut' and nothing more (ACT-3, PRO-PII).

Actions deliberately withheld:
- Did not instruct an agency contractor: no standing spend cap on file and no landlord message approving a priced job (APR-SPEND-OVER-CAP); the landlord's 12 May remark that we 'could' send one the next day names no amount and is superseded by his 15 May report that his plumber had attended (event-015, event-018).
- Did not close the request: work result, documents, invoice and landlord/tenant confirmation are all missing (CAP-CLOSE).
- Did not state or imply who pays for any call-out (PRO-TENANT-LIABILITY).
- Did not schedule access: no visit to book while the landlord's contractor route stands and no tenant consent or slot is on file (CAP-SCHEDULE-ACCESS).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, APR-SPEND-OVER-CAP, RTE-TENANT, RTE-LANDLORD, PRO-TENANT-LIABILITY, PRO-PII, CAP-CLOSE, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 6 May 2025 that the shower and hot water were not working and that the boiler had no power despite the switch being checked. [index, event-001, event-003; high]
- F2: The agency acknowledged the report on 6 May 2025 and treated the loss of hot water as urgent. [event-002, event-004; high]
- F3: The file was categorised as Electrical on the strength of 'no boiler power'; no inspection, diagnosis or agency contractor attendance is recorded. [event-005; high]
- F4: The landlord, Ravi Sethi, elected to arrange his own contractor on 6 May and the agency approval workflow was stopped; no agency appointment was booked. [event-007, event-010; high]
- F5: On 11 May the tenant reported 'Nothing done about it'; on 13 May the tenant again reported no hot water and that nobody had attended. [event-012, event-017; high]
- F6: On 12 May the landlord said his plumber would likely attend that evening and that the agency could send its own contractor the next day if he did not; no agency contractor was booked and no amount or cap was named. [event-015; high]
- F7: On 15 May the landlord said his plumber attended on 14 May and fixed the issue, based on a text from the plumber; no work description, report, invoice or record of boiler/electrical checks was provided. [event-018; high]
- F8: The tenant has not confirmed restoration: a voicemail and an email on 15 May are unanswered as at the last entry on 16 May. [event-019, event-020, event-021; high]
- F9: The tenant reported a non-working letterbox on 13 May and the agency promised to follow up; no detail or assessment was recorded. [event-017; high]
- F10: No standing spend cap or landlord standing instruction is on file for this property, and no landlord message approves a priced agency job. [get_case_details, event-010, event-015; medium]
- F11: Access notes: a household member may be at home but does not speak English, and small birds are kept at the property. [event-001, event-003; high]

Conflicts between sources:
- The fault was categorised as electrical (no boiler power) but the landlord sent a plumber, and the reported fix carries no description of any electrical or gas check. → Asked the landlord what was found and done and whether any gas or electrical work was carried out, with the engineer's registration (ACT-2). (asked)
- Landlord states the fault is fixed; the tenant has given no confirmation and the last tenant contact (13 May) said it was still not working. → Asked the tenant to confirm by 19 May 17:00 (ACT-1); case held open rather than closed. (asked)

Red flags:
- [other] The tenant was told on 6 May that a call-out 'might be chargeable' if an inspection found only a switch left off, before any inspection took place; liability is not the agent's to decide. → Recorded in the case note (ACT-3); no liability statement made to either party; goes to a manager if charging is raised (PRO-TENANT-LIABILITY, ESC-LEGAL).
- [data_quality] Completion rests on a second-hand account of a plumber's text message, with no report, invoice or confirmation from the property. → Documentation requested from the landlord and confirmation from the tenant before any closure (ACT-1, ACT-2, ACT-4).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "021", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed (ledger) | message=Hello Iris, re maintenance request NBL-021 (17 Wrenfold Qua… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed (ledger) | message=Dear Mr Sethi, re 17 Wrenfold Quay, Larkhollow — maintenanc… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | add_note | completed (ledger) | note=NBL-021 status review. Fault: no hot water / boiler reporte… | {"id": "ACT-3"} | CAP-LOG |
| 6 | put_on_hold | completed (ledger) | reason=Waiting for Tenant — confirmation that hot water and boiler…, until=2025-05-19 17:00 UTC | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **tenant**: Is the hot water and the boiler power now working at 17 Wrenfold Quay after the landlord's plumber attended on 14 May? Please reply by 17:00 on 19 May 2025. (blocking; Completion is only hearsay from the landlord (event-018); the tenant owns the fact of whether the fault is cured (RTE-TENANT). Voicemail and email of 15 May are unanswered (event-019, event-020).)
- Ask **tenant**: Regarding the letterbox you reported on 13 May: what exactly is faulty (flap, lock, or the box), does the front door still lock and close securely, and is it your own door or a shared/communal letterbox? (non-blocking; Promised follow-up on event-017 with no detail captured; door security would change the urgency to emergency (security definition).)
- Ask **landlord**: Please send the plumber's report or invoice for the 14 May visit, confirm what was found and done, state whether any gas appliance or electrical work was carried out and by whom (Gas Safe / NICEIC registration), and confirm nothing is outstanding. If you want Northbridge to take the job over, give us a spend limit. (blocking; Landlord owns the choice of contractor and the spend (RTE-LANDLORD); no documentation exists for a boiler fault first categorised as electrical (event-005) that a plumber attended (event-015, event-018), and no standing cap is on file.)

Promises made or recorded:
- agency → tenant: Follow up on the letterbox report of 13 May [open]
- agency → tenant: Reply-by 17:00 on 19 May 2025 requested for confirmation of hot water and letterbox details; repair goes back to the landlord the same day if it is still not working by 2025-05-19 17:00 [open]
- agency → landlord: Reply-by 17:00 on 19 May 2025 requested for the plumber's report/invoice and confirmation of any gas or electrical work by 2025-05-19 17:00 [open]
- landlord → agency: Own contractor to attend and complete the hot-water repair [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-GAS-CP12 [in_force]: Gas safety record
