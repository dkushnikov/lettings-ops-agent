# ANSWER — Case 011 — Kitchen ceiling leak inspection at 16 Brindlewick Mews

**Disposition:** ESCALATED · **Urgency:** urgent · **Case type:** maintenance_request · **Playbook:** maintenance-request

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Leak repair halted by an unidentified ceiling lining; no surveyor sourced or priced and no spend authority, so escalated for an asbestos survey decision.
**Stage:** on_hold · **Hold:** Other — asbestos-suspect ceiling lining: office to source and price an accredited asbestos survey; landlord decision on further scope and cost pending (asked event-024, chased ACT-2).
**Last update:** 2025-06-13 15:26:00 UTC (event-024) · **Decided:** 2026-10-10 15:40 UTC
**Next step:** Property manager to source and price an accredited asbestos survey of the kitchen ceiling lining and put the quoted amount to Ossa Fenlow (landlord) for approval; tenant and contractor remain on hold meanwhile.

Definition of done (5/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — Urgency set urgent (use_playbook); issue categorised and damage-limiting advice given to tenant at event-019 and again in ACT-1
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-013 - landlord authorised the quoted plumbing scope; further scope expressly not authorised (event-022)
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-008 / event-014 - Mossbarrow Pipe Services instructed and briefed; tenant told who was coming (event-007, event-016)
- [x] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — event-015 proposed and event-016 tenant-confirmed 13 June 10:30-12:30; contractor attended (event-017)
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-013 approved the plumbing estimate before work started; no approved quote exists for any asbestos assessment (event-022, event-023)
- [ ] work_result: Work result recorded from the provider — event-023 - contractor left without opening the ceiling; the pipe repair is not done
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — Photographs requested at event-008; no photos or invoice recorded in the case file
- [ ] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — No invoice received; repair not carried out
- [ ] landlord_confirmation: Landlord confirmed completion — Landlord's decision on further assessment outstanding (event-024, chased ACT-2)
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant admitted the contractor in person (event-009, event-017)
- [ ] closed: Request closed with a resolution that names who paid — Leak unrepaired; case on hold (ACT-4) pending asbestos survey decision

## 1. Decision

Escalate to the property manager. The authorised plumbing repair is blocked by an unidentified, possibly asbestos-containing ceiling lining (event-017) with no survey on file (event-006, event-013, event-022); the instructed plumber cannot specify or price the required assessment (event-023), so the landlord's request for likely cost and timing (event-022) cannot be answered without the office sourcing and pricing an accredited asbestos surveyor. No standing spend cap is on file (default £0) and the landlord's approval covers the quoted plumbing scope only (event-013), so I have no authority to instruct a surveyor (APR-SPEND-OVER-CAP). In-authority reversible steps were completed first: damage-limiting advice and status to the tenant (ACT-1), a factual "no figure yet" update and own-surveyor option to the landlord (ACT-2), safety check recorded (ACT-3), case put on hold (ACT-4).

Safety actions taken first:
- Confirmed with the contractor that no drilling, cutting, sampling or removal occurred and that the hatch is closed (event-018, event-023)
- Tenant instructed not to disturb the ceiling or hatch, to keep the area and children clear, to limit use of the kitchen tap, to keep electricals away, and given explicit emergency triggers (sagging, widening crack, continuous dripping, water near electrics) - ACT-1
- Case placed on hold so no one opens the ceiling until the lining is identified (ACT-4)
- Asbestos check and its current result recorded in the case record (ACT-3)

Actions deliberately withheld:
- Did not instruct an asbestos surveyor or any further contractor: no spend authority on file and the landlord expressly limited her approval to the plumbing scope (APR-SPEND-OVER-CAP, event-022).
- Did not quote a cost or lead time for the survey: no artefact gives one (rule 6).
- Did not authorise the plumber to proceed with the opening: material unidentified (ESC-SAFETY).
- Did not express any view on who pays for the survey or the ceiling condition (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, APR-SPEND-OVER-CAP, RTE-LANDLORD, RTE-STAFF, ESC-SAFETY, ESC-VULNERABLE, PRO-PII, PRO-TENANT-LIABILITY, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant Iven Rell reported a brown damp patch and overnight drips at the kitchen ceiling of 16 Brindlewick Mews on 10 June 2025; no sagging or fallen ceiling. [index, event-001; high]
- F2: No light below the patch, kitchen sockets dry, no water near electrics at the time of report. [event-003; medium]
- F3: A young child is present in the flat and the tenant asked for a call on arrival; detail kept in the case record and not passed to the contractor. [event-007, event-004; high]
- F4: Contractor Kellan Orve (Mossbarrow Pipe Services) inspected on 11 June and saw moisture at a compression joint above the ceiling hatch while the tap was running; the joint is not reachable through the hatch. [event-009, event-011; high]
- F5: Estimate covers isolating the pipe, opening ~30 cm of ceiling lining, replacing the joint and making good; it excludes investigation, testing, removal and disposal of suspect material. No amount is stated in the case file. [event-011; high]
- F6: Landlord Ossa Fenlow authorised the quoted plumbing scope up to the estimate amount on 12 June, subject to safe working and prior contact before any scope or cost increase. [event-013; high]
- F7: Return visit was agreed with the tenant for 13 June 10:30-12:30; the contractor attended at 10:40 and was admitted. [event-015, event-016, event-017; high]
- F8: A pale, fibrous-looking lining is visible behind the painted ceiling board; the contractor could not identify it, did not touch it, and paused the work. No drilling, cutting, sampling or removal has occurred at any visit; hatch left closed. [event-017, event-018, event-023; high]
- F9: No survey, material assessment or ceiling alteration record exists: landlord has none, building manager has none and has not inspected the flat. [event-006, event-013, event-022; high]
- F10: The leak is recurring: tenant reported a small drip on 13 June when the kitchen tap was used and has stopped using that tap; ceiling not visibly sagging. [event-020; high]
- F11: Landlord confirmed on 13 June that her authorisation does not extend to a specialist material assessment and asked for likely cost and timing before considering further expenditure. [event-022; high]
- F12: The contractor cannot price work involving the unidentified lining and cannot specify what assessment would be required. [event-023; high]

Red flags:
- [safety_hazard] Unidentified pale, fibrous-looking ceiling lining in a flat of unknown construction date, directly in the zone of the authorised 30 cm opening, with a young child resident. Possible asbestos-containing material; no survey on file (event-006, event-013, event-022). → Contractor instructed not to drill, cut, sample or disturb (event-018, confirmed event-023); tenant instructed not to touch the hatch or ceiling (event-019, ACT-1); work held (ACT-4); escalated for an accredited survey decision
- [vulnerability] Young child in the property while a ceiling leak recurs and the kitchen tap is out of normal use. → Detail kept in the case record only, not shared with the contractor (PRO-PII, event-004); damage-limiting advice and emergency triggers given to the tenant (ACT-1); flagged in the handover

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "011", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | notify_tenant | completed (ledger) | message=Thank you for your update (13 June, 11:27) confirming a sma… | {"id": "ACT-1"} | CAP-NOTIFY |
| 4 | notify_landlord | completed (ledger) | message=Further to your email of 13 June (12:14) asking for the lik… | {"id": "ACT-2"} | CAP-NOTIFY |
| 5 | add_note | completed (ledger) | note=Safety check recorded (asbestos keyword). Unidentified pale… | {"id": "ACT-3"} | CAP-LOG |
| 6 | put_on_hold | completed (ledger) | reason=Other — authorised plumbing repair cannot proceed: unidenti…, until=2025-06-16 | {"id": "ACT-4"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Who sources and pays for an accredited asbestos survey of the kitchen ceiling lining at 16 Brindlewick Mews so the already-authorised pipe repair can proceed, and what cost and timing do we give the landlord?
**Facts (≤5):**
- Plumber found moisture at a compression joint above the kitchen ceiling; unreachable through the hatch, so a ~30 cm ceiling opening was quoted (event-011).
- Landlord Ossa Fenlow authorised the quoted plumbing scope only, subject to safe working, and must be asked before any scope or cost increase (event-013, event-022).
- On the return visit the plumber saw a pale, fibrous-looking lining behind the ceiling board, could not identify it, paused and left; no drilling, cutting, sampling or removal occurred and the hatch is closed (event-017, event-018, event-023).
- No survey or alteration record exists: landlord has none (event-013, event-022); building manager has none and has not inspected the flat (event-006).
- Leak is live - tenant reported a drip when the kitchen tap was used on 13 June and has stopped using the tap; a young child lives in the flat; ceiling not sagging (event-020, event-007).
**Gap:** No accredited asbestos surveyor sourced or priced - the instructed plumber states he cannot specify or price the assessment (event-023) - and no landlord spend cap is on file (default £0), so the cost and timing the landlord asked for (event-022) cannot be given and nobody can be instructed.
**Options:**
- Office sources an accredited asbestos surveyor, obtains a priced quote (sample and analysis) and puts it to the landlord for approval; repair resumes once the material is cleared or a licensed method is specified.
- Ask the landlord to appoint her own surveyor (already offered in ACT-2): no agency spend, but timing leaves our control while the leak continues.
- Wait for the landlord's reply to event-024 only: the leak recurs whenever the kitchen tap is used, the tenant is without normal use of the kitchen sink, and the s.11 reasonable-time clock from 10 June keeps running.
**Recommended:** Option 1: source and price an accredited asbestos survey now and put the quoted amount (with VAT and lead time) to the landlord; keep the plumbing instruction live but paused with Mossbarrow Pipe Services.
**Default if no answer:** If the landlord has not replied by 16 June (3-day wait from event-024, 13 June 15:26), the case returns to manual review as an expired landlord wait; the tenant stays on damage-limiting advice and the ceiling remains undisturbed.
**Deadline:** 2025-06-16
**Undo:** Nothing irreversible: no surveyor instructed, no spend committed, no ceiling opened. The hold (ACT-4) can be lifted and the plumber re-booked for the already-approved scope once the lining is cleared.
**Context:** event-011, event-013, event-017, event-022, event-023, event-024, ACT-1, ACT-2, ACT-4

Promises made or recorded:
- agency → tenant: Confirm the next appointment only once it is actually booked; no date promised [open]
- agency → landlord: Send the surveyor's quoted amount, VAT position and lead time for her decision once obtained [open]
- landlord → agency: Decide on any further assessment or repair scope by 2025-06-16 [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CLK-AWAAB-PRS [proposed]: Awaab's Law timescales (reference only)
