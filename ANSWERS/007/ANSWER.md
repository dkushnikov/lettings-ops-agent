# ANSWER — Case 007 — Television, bedroom light and door handle

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** access_scheduling · **Playbook:** access-scheduling

**Environment:** Case files only: write actions are recorded in this case's action ledger (ACT-n) as instructions ready to send; nothing was delivered to a real party.

## Status

**Recap:** Electrical visit booked 29 Sep after 15:00 on the window tenant and electrician both named; awaiting arrival time, landlord scope/TV answer, door-lock check.
**Stage:** visit_scheduling · **Hold:** Waiting for Provider — exact arrival time for the booked 29 Sep slot; also Waiting for Landlord on scope of the downstairs light and TV ownership/disposal (landlord auto-reply 7 Sep said he was away, event-007).
**Last update:** 2025-09-17 09:04:05 UTC (event-019) · **Decided:** 2026-10-10 15:38 UTC
**Next step:** Contractor (Rian Sol, Bracken Spark Services) to confirm an approximate arrival time for Mon 29 Sep after 15:00; Oren Pike to relay it to the tenant and send a reminder on the day.

Definition of done (5/6 done):
- [x] job_known: Purpose and urgency of the visit confirmed — event-001 (TV fault + downstairs light), event-005 (light added to record), event-017 (combined electrical visit instructed to Bracken Spark Services); urgency set routine — no burning smell/sparks/s…
- [x] windows_offered: Two contractor-confirmed windows offered to the tenant with the required notice — Tenant offered six windows (event-016); contractor confirmed one of them, 29 Sep after 15:00 (event-019). Only one contractor-confirmed window exists rather than two, but it matches the tenant's own…
- [x] tenant_agreed: Tenant agreed a window, or consented to entry with the management key — event-016 — tenant herself listed 29 September after 15:00 as available; dog to be taken out, contractor to call on arrival
- [x] booked: Visit booked and confirmed to both the tenant and the contractor (slot, access arrangement, pets noted) — ACT-1 schedule_access; confirmed to tenant ACT-3 and contractor ACT-4 with slot, access arrangement and pet note
- [ ] reminders: Reminder sent on the day; any reschedule confirmed to both sides — Day-of reminder due 29 Sep; arrival time to be relayed to tenant once the contractor answers (ACT-4)
- [n/a] keys: Key handover recorded and key return confirmed after the visit, where a key was issued — No key issued; tenant will be present at the property (event-016)
- [x] logged: Window, agreement and access arrangement logged — ACT-2 — window, consent basis, access arrangement and open gaps recorded

## 1. Decision

Booked the electrical visit for Mon 29 Sep 2025 after 15:00 — the one window both the tenant (event-016) and the electrician (event-019) had already named, so no fresh consent was needed (rule 2, CAP-SCHEDULE-ACCESS). Confirmed it to tenant and contractor with the access arrangement (tenant present, dog out, call on arrival), briefed the contractor as diagnosis-only with a written quote before any chargeable work, and gave the tenant damage-limiting advice (TV stays unplugged, keep using the lamp, isolate and call if burning smell/sparks/shock). Did not treat this as an emergency: the reported symptoms are a fuse-tripping appliance that is unplugged and a light the tenant has stopped using, with no burning smell, sparks or shock reported (event-001, event-015). Did not dispatch any new or additional work and did not commit spend: no standing cap is on file (event-004) and the landlord's "Please sort it" (event-003) answered a TV-only request (event-002), so it is not approval for the downstairs light or for any priced repair. Did not decide who owns or pays for the television (PRO-TENANT-LIABILITY) — put to the landlord. Did not open a work order for the rear-door handle, which exists only as a call remark with no report (event-015, event-018); asked the tenant the one question that decides its urgency (does the rear door still lock). Case now waits on three named parties, so request_info rather than escalation.

Safety actions taken first:
- Assessed the electrical reports against the emergency definitions: fuse-tripping appliance is unplugged (event-001) and the flickering/popping light is out of use with a lamp in its place (event-015); no burning smell, sparks or shock risk reported, so not handled as an emergency.
- Gave the tenant damage-limiting advice: keep the TV unplugged, do not use the downstairs light, and if a burning smell, scorch marks, sparks or a shock occur, isolate that circuit at the consumer unit if safe and call immediately, treating it as an emergency out of hours (ACT-3).
- Briefed the electrician to establish whether the fault is confined to the appliance or involves the socket/circuit, and to make safe and report immediately if anything unsafe is found (ACT-4).
- Asked the tenant whether the rear door still locks, so a possible property-security defect is not left sitting as an unlogged call remark (ACT-3).
- Withheld the tenant's household details from the contractor; passed only the address, slot, dog and call-on-arrival instruction (PRO-PII).

Actions deliberately withheld:
- Did not dispatch any contractor or commit spend: no standing cap on file (event-004) and no landlord approval covering a priced job (APR-SPEND-OVER-CAP).
- Did not instruct repair, replacement or disposal of the television — ownership and liability are unresolved (PRO-TENANT-LIABILITY).
- Did not raise a work order for the rear-door handle before knowing whether the door still secures.
- Did not re-ask the tenant to confirm 29 September: she offered that window herself (event-016).
- Did not close the request: no work has been carried out.

## 2. Authority and evidence

Authority cited: CAP-SCHEDULE-ACCESS, CAP-NOTIFY, CAP-LOG, RTE-CONTRACTOR, RTE-LANDLORD, RTE-TENANT, APR-SPEND-OVER-CAP, PRO-TENANT-LIABILITY, PRO-PII, CLK-S11
Rules applied by the policy gate: CAP-LOG, CAP-NOTIFY, CAP-SCHEDULE-ACCESS

Key facts (source ids in brackets):
- F1: Tenant reported a Samsung TV in an upstairs bedroom that trips a fuse when plugged in (now unplugged) and a downstairs bedroom light that flickers and pops when switched on; access must be pre-arranged because of a dog. [index, event-001; high]
- F2: The landlord's approval request of 4 Sep covered the TV only; it did not include the downstairs light. [event-002; high]
- F3: Landlord replied on 5 Sep 'Please sort it. I don't remember leaving a TV.' — no mention of the light, and no statement on TV ownership, replacement or disposal. [event-003; high]
- F4: No spending limit and no disposal instruction are recorded for this landlord. [event-004; high]
- F5: The downstairs light was added to the maintenance record on 5 Sep, after the landlord's TV-only approval request. [event-005; high]
- F6: A landlord auto-reply on 7 Sep said he was away and gave no further instructions. [event-007; high]
- F7: The first electrical contractor was stood down on 11 Sep and scheduling restarted with Bracken Spark Services. [event-011; high]
- F8: Tenant gave availability on 16 Sep: 23, 24, 29 and 30 Sep after 15:00; 25 Sep and 2 Oct after 12:30. Dog will be taken out; contractor to call on arrival rather than knock. [event-016; high]
- F9: Electrician Rian Sol (Bracken Spark Services) proposed attending 29 September after 15:00, with no exact arrival time and no appointment confirmation yet sent. [event-019; high]
- F10: Tenant's belief that the TV's main board is 'fried' is her own view after changing fuses, not a technician's diagnosis; she is open to the TV being removed. [event-015; medium]
- F11: Tenant is using a lamp instead of the downstairs bedroom light and can manage without it for now. [event-015; high]
- F12: The rear-door handle has come off; raised on the 16 Sep call only, no separate report received and no handyman assigned. Whether the door still locks is unknown. [event-015, event-018; high]

Conflicts between sources:
- Scope mismatch: the landlord approved works on a request that covered the television only (event-002, event-003), but the instructed visit covers both the television and the downstairs bedroom light (event-005, event-017). → Attendance on the already-instructed visit left in place (reversible, no extra call-out); landlord asked to confirm the light is within scope and told any repair comes back as a priced quote before work starts (ACT-5, RTE-LANDLORD). (asked)
- Television ownership unclear: the landlord does not remember leaving a TV (event-003), the tenant treats it as the property's and is content for it to be removed (event-015). This decides who pays for repair, replacement or disposal. → Not decided by the agent (PRO-TENANT-LIABILITY). Put to the landlord as a direct question (ACT-5); the electrician will establish whether the fault is in the appliance or the circuit (ACT-4). (asked)

Red flags:
- [data_quality] The landlord's 'Please sort it' is being carried as authority for a scope it never covered: it answered a TV-only approval request, while the instructed visit now also covers the downstairs light. No spend cap is on file either, so no quote can be approved on it. → Scope put back to the landlord and the diagnosis-only limit stated to the contractor; no spend committed (ACT-4, ACT-5).
- [other] The rear-door handle exists only as a remark in a call transcript with no work order; without a check on whether the door still locks, a potential security defect could be lost between tickets. → Direct question to the tenant with a same-day route to urgent handling if the door does not lock (ACT-3).

## 3. Actions (proposed → attempted → completed)

Writes in this environment are recorded in the case ledger, not delivered: `completed (ledger)` means the ledger accepted the instruction and returned a receipt.

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "007", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | schedule_access | completed (ledger) | window=Monday 29 September 2025, after 15:00 — electrician Bracken…, tenant_consent=True | {"id": "ACT-1"} | CAP-SCHEDULE-ACCESS |
| 4 | add_note | completed (ledger) | note=Access booked for 29 Sep 2025 after 15:00. Consent basis: t… | {"id": "ACT-2"} | CAP-LOG |
| 5 | notify_tenant | completed (ledger) | message=Ada Pell — 8 Vellum Court, Brindlewick. Electrical visit no… | {"id": "ACT-3"} | CAP-NOTIFY |
| 6 | notify_contractor | completed (ledger) | message=Rian Sol, Bracken Spark Services — job confirmed: 8 Vellum… | {"id": "ACT-4"} | CAP-NOTIFY |
| 7 | notify_landlord | completed (ledger) | message=Mr Corin Wex — 8 Vellum Court, Brindlewick. Update and two… | {"id": "ACT-5"} | CAP-NOTIFY |

## 4. Human handover / information requested

- Ask **contractor**: Please confirm an approximate arrival time for the booked visit on Monday 29 September 2025 after 15:00 at 8 Vellum Court, and confirm you will phone the tenant on arrival rather than knock. (blocking; Contractor proposed the date but gave no arrival time (event-019); the tenant needs a window and the dog must be taken out (RTE-CONTRACTOR).)
- Ask **landlord**: Do you approve the downstairs bedroom light being investigated and quoted alongside the television on the same visit; and was the Samsung television left by you as part of the let — do you want it repaired, replaced, disposed of or left to the tenant? Also, would you like to set a standing spending limit for this property? (non-blocking; The 5 Sep approval (event-003) answered a TV-only request (event-002); the light was added later (event-005). Ownership/payment for the TV is the landlord's to settle, not the agent's (RTE-LANDLORD, PRO-TENANT-LIABILITY). No spend cap is on file (event-004).)
- Ask **tenant**: Does the rear door still close and lock securely now that the handle has come off? (non-blocking; Raised on the call only, no report logged (event-015, event-018). If the door cannot be secured it becomes an emergency security job; if it locks, it is a routine handyman item.)

Promises made or recorded:
- agency → tenant: Electrician will attend Monday 29 September 2025 after 15:00; engineer to phone on arrival rather than knock by 2025-09-29T15:00:00Z [open]
- agency → tenant: Send the electrician's approximate arrival time once received by 2025-09-29 [open]
- contractor → agency: Attend 8 Vellum Court on 29 September after 15:00 and confirm an approximate arrival time by 2025-09-29 [open]
- agency → landlord: Any repair will be sent as a priced quote for approval before work starts; this visit is diagnosis only [open]
- tenant → agency: Submit the rear-door handle as a separate report [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported deadline 2025-09-29
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
- CAP-SCHEDULE-ACCESS [sop]: 24 hours' notice of access deadline 2025-09-28
