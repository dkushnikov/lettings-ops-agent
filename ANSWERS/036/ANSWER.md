# ANSWER — Case 036 — Case 036: Shower Tap Repair

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Shower/bath tap reported complete at no charge; landlord updated, tenant and provider chased for confirmation and photos, request held at final checks, not closed.
**Stage:** final_checks · **Hold:** Waiting for Landlord — confirmation to close after the provider's no-charge completion; in parallel awaiting provider photos and tenant confirmation, reply-by 12/11/2026 (ACT-5)
**Last update:** 2026-11-07 07:14:06 UTC (event-052) · **Decided:** 2026-10-10 14:10 UTC
**Next step:** Landlord (Sawyer) to confirm completion so the request can be closed; provider to send photos and tenant to confirm the fault is resolved by 12/11/2026.

Definition of done (6/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001/event-002: issue logged and categorised as a shower repair; routine, no emergency definition met; no damage-limiting steps applicable to a broken tap knob
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-006 — landlord's own message approving a contractor; work ultimately carried out at no charge (event-050)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008, event-009, event-011 — Keystone Services assigned and briefed; tenant notified
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-016/event-018/event-019 (29/09) and event-038/event-039 (09:30 Wed 4 November)
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — No quote raised; provider confirmed no charge under his own guarantee (event-050, event-051)
- [x] work_result: Work result recorded from the provider — event-050 — provider reports job complete, new bath tap fitted
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — No photos or invoice received despite chases (event-048); provider chased again with reply-by 12/11/2026 (ACT-3)
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-052 marked completed without payment; landlord told there is no invoice and no cost (ACT-1)
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord asked to confirm closure (ACT-1); no reply yet
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — F9 — no management key issued; tenant provided access
- [ ] closed: Request closed with a resolution that names who paid — Held at final_checks (ACT-5); closure withheld until landlord confirmation, photos/skip reason and tenant confirmation are in

## 1. Decision

The repair is reported complete at no charge, but three closure checks are outstanding, so the request stays open on hold rather than being closed. I updated the landlord with the outcome and the no-charge basis, asked the tenant to confirm both the original and the 14/10 secondary fault are resolved, and chased the provider for the photos the landlord asked for (reply-by 12/11/2026). No spend decision was needed: the landlord approved instruction in their own message (event-006) and the provider confirms no charge (event-050). I did not close the request: landlord confirmation (RTE-LANDLORD) and documents are pending, and a closure with pending checklist items is not valid under CAP-CLOSE.

Safety actions taken first:
- Safety-pass check: no hazard keywords reported or observed in this case — no gas, electrical, water ingress, damp/mould, heating loss or security issue in any artefact; urgency confirmed routine, so no emergency capability engaged.
- No occupant vulnerability disclosed; no health or family data shared with the provider (PRO-PII).

Actions deliberately withheld:
- close_request — CAP-CLOSE: landlord confirmation and documents are still pending, so a closure now would be invalid despite the system's 'completed without payment' status line (event-052).
- Any statement on who pays or on the provider's guarantee liability — PRO-TENANT-LIABILITY / RTE-LANDLORD; the no-charge position is reported as the provider's own statement only.
- No new dispatch raised: one work order only, the existing provider holds the job (playbook step 3).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-CLOSE, RTE-LANDLORD, RTE-TENANT, RTE-CONTRACTOR, PRO-TENANT-LIABILITY, CLK-S11, CLK-SOP-ACK
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported on 24/09/2026 that the shower pull knob is broken and the cap comes off each use at Flat 13, 73 Juniper Mews, Northbridge, ZZ1 6ZZ. [index, event-001; high]
- F2: The landlord (Sawyer) approved instructing a contractor in their own reply 'Yes please!' on 25/09/2026. [event-006; high]
- F3: Keystone Services was assigned and briefed, and the tenant was told who was attending, on 25/09/2026. [event-008, event-009, event-011; high]
- F4: A visit was confirmed with tenant and provider for 29/09/2026 09:00-09:30, and later re-booked to 09:30 Wednesday 4 November after a part was ordered. [event-016, event-018, event-019, event-038, event-039; high]
- F5: The provider reported on 07/11/2026 that the job is complete, a new bath tap was fitted, and there is no charge because the tap he fitted in February was faulty; the agency recorded the task as completed without payment. [event-050, event-051, event-052; medium]
- F6: No quote or priced spend was ever put to the landlord, because the provider carried out the work at no cost under his own guarantee; the landlord also noted the taps are under guarantee. [event-043, event-050; medium]
- F7: The landlord asked for photos of the works and raised concern about the elapsed time; the agency chased the provider for photos on 07/11/2026 but none have been received. [event-043, event-045, event-048; high]
- F8: On 14/10/2026 the tenant reported a further symptom to the provider: shower and tap running simultaneously when a button is pressed; no record confirms this was resolved. [event-030; medium]
- F9: No management key was issued; the tenant gave access directly to the provider at agreed slots. [event-018, event-019; medium]

Conflicts between sources:
- The agency told the landlord the fitting visit was 03/11/26 (event-041) while the provider's confirmed booking was 09:30 Wednesday 4 November (event-038, event-039). → Provider's own booking confirmation governs the slot; difference is now moot as the work is reported complete (event-050). Recorded in the case note (ACT-4). (source_hierarchy)
- Hold at event-035 is logged as 'Waiting for Landlord' although the chase at event-034 was to the provider. → Administrative mislabel only; current hold set correctly to Waiting for Landlord for the closure confirmation (ACT-5). (tool_check)

Red flags:
- [data_quality] Provider's completion report is a short untrusted email with no photos and no invoice, and it describes a 'bath tap' where the tenant reported a shower pull knob; the job was auto-marked 'completed without payment' on that basis alone. → Closure withheld; photos and scope confirmation requested from the provider and working confirmation requested from the tenant (ACT-2, ACT-3, ACT-4).
- [other] Attachments referenced in the provider brief are listed as unavailable, and the tenant's video evidence could not be attached, so no visual record of the original fault exists. → Recorded; photos requested from the provider to give the landlord a record (ACT-3).

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "036", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_landlord | completed | message=Address: Flat 13, 73 Juniper Mews, Northbridge, ZZ1 6ZZ — S… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_tenant | completed | message=Dear Noah Bennett,  Flat 13, 73 Juniper Mews, Northbridge,… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | notify_contractor | completed | message=Address: Flat 13, 73 Juniper Mews, Northbridge, ZZ1 6ZZ — S… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | add_note | completed | note=Case 036 review. Work reported complete by provider 07/11/2… | {"id": "ACT-4"} | CAP-LOG |
| 7 | put_on_hold | completed | reason=Waiting for Landlord — confirmation to close following prov…, until=2026-11-12 | {"id": "ACT-5"} | CAP-LOG |

## 4. Human handover / information requested

- Ask **landlord**: Do you confirm the shower/bath tap job as complete and agree we close the request, recorded as completed without payment (new tap fitted free of charge under the provider's own guarantee)? (blocking; RTE-LANDLORD: landlord confirmation is a closure check; landlord had also raised concerns about the delay (event-043).)
- Ask **contractor**: Please send photos of the completed work and confirm whether the tenant's 14/10/2026 fault (shower and tap running simultaneously when the button is pressed) is also resolved. (non-blocking; Landlord specifically requested photos (event-043, event-048); documents item of the definition of done is otherwise unmet.)
- Ask **tenant**: Is the shower and tap now working correctly, including the fault you reported on 14/10/2026 where both ran at the same time? (non-blocking; RTE-TENANT: only the tenant can confirm the fault at the property is actually resolved before closure.)

Promises made or recorded:
- agency → landlord: Chase again rather than close if no reply within 3 working days by 2026-11-12 [open]
- agency → contractor: Photos and confirmation of the 14/10 fault requested, reply-by date given by 2026-11-12 [open]
- agency → tenant: Arrange a return visit if the shower or tap is still faulty [open]
- contractor → agency: Replace the faulty part free of charge and finish the job [kept]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
