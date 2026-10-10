# ANSWER — Case 009 — Bedroom Window Maintenance Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** The landlord took this job on himself with his own contractor (event-014, event-016), so no agency dispatch or spend arose; no contractor was ever instructed b…
**Stage:** on_hold · **Hold:** Waiting for Landlord — confirmation of completion of his own contractor's window work plus report/invoice or skip reason, and the correct gas safety record for this property; reply requested within 3 working days (ACT-2, ACT-5).
**Last update:** 2025-09-10 18:20:00 UTC (event-020) · **Decided:** 2026-10-10 15:39 UTC
**Next step:** Landlord (Dorian Pike) to confirm the window work is complete and at his own cost and send the contractor's report/invoice or a skip reason (requested ACT-2, 3 working days); on his reply the case can be closed.

Definition of done (3/7 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 fault logged (window will not close/seal, handle works, hinges suspected); urgency set routine at use_playbook; tenant kept informed of progress event-007, event-012, event-017 and ACT-3.
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-014 and event-016: landlord elected to inspect and arrange the work himself with his own contractor; no agency spend arose, so no cap or approval applied.
- [n/a] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — Landlord used his own contractor (event-014, event-018 contractor attended); the agency instructed no provider.
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-015 tenant agreed 10:00-12:00 the following morning; event-016 landlord agreed to attend; a contractor subsequently attended per event-018.
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No agency quote existed; the landlord commissioned and bears the cost of his own contractor (event-014).
- [ ] work_result: Work result recorded from the provider — Tenant states work finished and that contractor 'Richard' would send a report (event-020); no report received from the provider — requested from the landlord at ACT-2.
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice held; requested from the landlord, with a skip reason to be recorded if none exists (ACT-2).
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — Work arranged and paid for directly by the landlord's own contractor (event-014); the agency has no invoice to forward. To be recorded as completed without agency payment once the landlord confirms.
- [ ] landlord_confirmation: Landlord confirmed completion — Requested at ACT-2; 3 working days.
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant present for access (event-015, event-008).
- [ ] closed: Request closed with a resolution that names who paid — Case on hold (ACT-5) pending the landlord's confirmation; closure must name who paid.

## 1. Decision

The landlord took this job on himself with his own contractor (event-014, event-016), so no agency dispatch or spend arose; no contractor was ever instructed by Northbridge Lettings. The tenant reports the work is finished (event-020), but no provider report, photographs or invoice exists and the landlord has not confirmed completion or who paid, so the request cannot be closed. I asked the landlord to confirm completion and send the report/invoice or a skip reason (ACT-2), asked the tenant the one open safety-relevant question — that the window now closes and locks (ACT-3) — referred the misfiled certificates to the compliance queue (ACT-4) and put the case on hold pending the landlord's reply (ACT-5). No escalation: nothing here requires a human to decide liability, legal or safety; the outstanding items are landlord-owned facts (RTE-LANDLORD) and one tenant-owned confirmation (RTE-TENANT).</decision>
Landlord self-managed window repair reported done by tenant; chased landlord for completion confirmation and report/invoice, flagged a gas record filed for the wrong property.

Safety actions taken first:
- Checked the file for emergency definitions: no gas, electrical, water-ingress, heating-loss or security failure reported or observed; handle operates and the fault is sealing (event-001).
- Asked the tenant to confirm the window now shuts, seals and locks, with an instruction to report immediately if it does not, so the security aspect is verified before closure (ACT-3).
- Gas and electrical certificate keywords in the material checked: the only gas record on file belongs to another property and is therefore not evidence of compliance here; routed to compliance (ACT-4).

Actions deliberately withheld:
- Did not close the request: work result, documents and landlord confirmation are outstanding and a closure must name who paid (CAP-CLOSE).
- Did not instruct any contractor: the landlord is using his own and no agency spend is authorised (no standing cap on file; APR-SPEND-OVER-CAP).
- Did not state or imply who pays for the repair beyond the landlord's own arrangement (PRO-TENANT-LIABILITY).
- Did not treat the forwarded gas record as evidence of compliance for this property.

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, RTE-LANDLORD, RTE-TENANT, PRO-TENANT-LIABILITY, PRO-INSTRUCTIONS-FROM-CONTENT, CLK-S11, CLK-GAS-CP12, CLK-EICR
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Case property is 24 Bramblewick Lane, Alderfen, ZZ1 1ZZ; tenant Elena Voss reported on 12 Aug 2025 that a bedroom window will not close or seal, handle works, hinges suspected. [index, event-001, get_case_details; high]
- F2: The landlord, Dorian Pike, chose to inspect the window himself before sending a contractor and thought it might only need lubrication; he agreed to attend 10:00-12:00 the following morning. [event-014, event-016; high]
- F3: The tenant consented to and confirmed that access window (10:00-12:00 the following morning). [event-015; high]
- F4: On 2 Sep 2025 the tenant reported that a contractor had said parts needed ordering and would make contact the following week. [event-018; medium]
- F5: On 10 Sep 2025 the tenant reported 'All jobs was done' and said the contractor, Richard, would send a report; no report, photos or invoice has reached the agency. [event-020; medium]
- F6: The agency has never instructed a contractor on this case and no agency spend or quote arose; the action ledger held no prior actions. [get_action_ledger, event-014; high]
- F7: The case attachment forwarded-document.pdf is a Landlord Gas Safety Record, reference NBL-009-GSR-25, inspected 8 Sep 2025 by engineer Rellan Voss, boiler and hob, outcome satisfactory — but its property line reads 8 Thistledown Mews, Vellumby, not the case property. [forwarded-document, get_attachment; high]
- F8: The landlord forwarded an electrical installation condition report on 19 Aug 2025 and the gas record on 10 Sep 2025, both without a covering message. [event-011, event-019; high]
- F9: On 27 Aug 2025 the tenant raised that rain and falling temperatures made the partly open window a concern, and that they would not return calls from unknown numbers without a voicemail because of scam concerns. [event-013, event-008; high]
- F10: No hazard was reported or observed at the property: the handle works and the fault is sealing/draught; no gas, electrical, water or security failure was described. [event-001, event-013; medium]

Conflicts between sources:
- The gas safety record attached to this case names 8 Thistledown Mews, Vellumby, while the case property is 24 Bramblewick Lane, Alderfen; it is impossible to tell from the file whether the landlord misforwarded a certificate or the certificate itself is mislabelled. → Not decided by me. Referred to the compliance queue (ACT-4) and the landlord asked to supply the correct record for this property or identify the property the forwarded record belongs to (ACT-2). It does not change the window repair action. (asked)

Red flags:
- [data_quality] Safety certificate filed against the wrong case: forwarded Landlord Gas Safety Record NBL-009-GSR-25 names 8 Thistledown Mews, Vellumby, not 24 Bramblewick Lane. An EICR was also forwarded with no property detail. Risk that this property's CP12/EICR compliance is not actually evidenced. → Compliance queue task raised (ACT-4) and correct record requested from the landlord (ACT-2); no certificate accepted as evidence of compliance for this property.
- [other] Tenant received repeated calls from an unfamiliar number with no voicemail and would not call back for fear of a scam; the caller is unverified in the file. → Told the tenant the agency will always leave a voicemail or message and will coordinate contact, and that they need never return an unidentified number (ACT-3).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "009", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=forwarded-document.pdf | {"name": "forwarded-document.pdf", "text": "G A S  S A F E T Y  R E C O R D Forwarded Landlord Gas Safety Record\nLandlord Gas Safety Record\nRecord reference:… | allow |
| 4 | add_note | completed (ledger) | note=Window repair at 24 Bramblewick Lane: landlord Dorian Pike… | {"id": "ACT-1"} | CAP-LOG |
| 5 | notify_landlord | completed (ledger) | message=Dear Mr Pike,  Re: 24 Bramblewick Lane, Alderfen — bedroom… | {"id": "ACT-2"} | CAP-NOTIFY |
| 6 | notify_tenant | completed (ledger) | message=Dear Ms Voss,  Re: 24 Bramblewick Lane — bedroom window.  T… | {"id": "ACT-3"} | CAP-NOTIFY |
| 7 | create_human_task | completed (ledger) | queue=compliance, title=Misfiled safety certificates on case 009 — gas record names…, summary=Case 009 (24 Bramblewick Lane, Alderfen) attachment forward… | {"id": "ACT-4"} | CAP-HUMAN-TASK |
| 8 | put_on_hold | completed (ledger) | reason=Waiting for Landlord — confirmation that the window work he…, until=3 working days from ACT-2 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Please confirm the bedroom window work at 24 Bramblewick Lane is complete and was carried out and paid for by your own contractor, and send the contractor's report or invoice (or confirm there is none). (blocking; Landlord confirmation and the work result/documents are the outstanding definition-of-done items; the landlord arranged the work directly, so only he holds these facts (RTE-LANDLORD).)
- Ask **landlord**: The Landlord Gas Safety Record you forwarded on 10 September (NBL-009-GSR-25, inspection 8 September 2025) names 8 Thistledown Mews, Vellumby. Please send the current gas safety record for 24 Bramblewick Lane, or confirm which property that record belongs to. (non-blocking; The certificate attached to this case does not match the case property; CLK-GAS-CP12 compliance for this property cannot be evidenced from it (also referred to the compliance queue, ACT-4).)
- Ask **tenant**: Please confirm the bedroom window now shuts fully, seals and locks. (non-blocking; The tenant's 'All jobs was done' (event-020) is second-hand about the contractor's work; confirming the window closes and locks is the safety/security check that must be recorded before closure (RTE-TENANT).)

Promises made or recorded:
- agency → landlord: Request for confirmation of completion, contractor report/invoice or skip reason, and the correct gas safety record; reply asked within 3 working days, case stays open until then. by 3 working days from ACT-2 [open]
- agency → tenant: Completion recorded and landlord asked to confirm; any report that the window still does not close or lock will be treated as a priority; the agency will always leave a voicemail and coordinate contact. [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge a tenant report within one working day
- CLK-GAS-CP12 [in_force]: Gas safety record renewed every 12 months
- CLK-EICR [in_force]: EICR every 5 years; remedials within 28 days
