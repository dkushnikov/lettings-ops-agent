# ANSWER — Case 006 — Case 006: Check-Out Works: Carpet Replacement and Repainting

**Disposition:** ESCALATED · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Check-out works logged complete and auto-closed, but provider/property records conflict, landlord completion confirmation is missing and alarm testing is unrecorded — escalated.
**Stage:** final_checks · **Hold:** Waiting for Landlord — completion confirmation required by event-024 has not been received; office must also settle the provider/address conflict first.
**Last update:** 2024-10-29 15:55:08 UTC (event-027) · **Decided:** 2026-10-10 13:19 UTC
**Next step:** Property manager to resolve which provider attended which address, obtain the landlord's written completion confirmation (event-024 requirement), and confirm smoke/CO alarms tested before the flat is remarketed.

Definition of done (7/10 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 logged the brief (burnt carpet, repaint); routine check-out works, vacant property; tenant and provider briefed at event-004 and event-005
- [x] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-015 — landlord's own message 'Pls go ahead' in reply to the priced quote at event-013
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-003/event-005 assigned and briefed Cedar Utilities; tenant told at event-004 — but event-013/016/020 name Sawyer; conflict recorded at ACT-1
- [ ] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever confirmed: reminders at event-006, event-007, event-008 ('3+ reminders'); provider reply event-012 gave no appointment details
- [x] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — event-013 quote (£220 + £240 + £100 + £45 = £605, VAT not stated) approved by landlord at event-015 before work; approval relayed to provider at event-016
- [x] work_result: Work result recorded from the provider — event-020 'Sawyer completed'; agency system note only — no provider report, photos or invoice on file
- [x] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-023 skip reason recorded: 'Sawyer invoices landlord directly'
- [n/a] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-023 — provider invoices the landlord directly; no invoice passes through the agency
- [ ] landlord_confirmation: Landlord confirmed completion — event-024 required it; no landlord message confirming completion exists in the history after that date
- [x] keys_returned: Keys returned, where a management key was issued for the visit — event-026 'Keys return confirmed'
- [ ] closed: Request closed with a resolution that names who paid — event-027 closed the request, but landlord confirmation and visit confirmation are unevidenced and the resolution does not name who paid

## 1. Decision

Do not accept the closure. The ticket was auto-closed at event-027 with two agency records in conflict (provider: Cedar Utilities at event-003/005 vs Sawyer at event-013/016/020; address: Flat 21 Northbridge vs event-018 "Flat 12, 122 Juniper Mews, Westmarsh"), with no landlord confirmation of completion on file against the requirement raised at event-024, and with no record of smoke/CO alarm testing on a flat that suffered a carpet burn and is being prepared to remarket. Conflicts between agency records that change the action, and the safety check before move-in, are for a person (ESC-CONFLICT, ESC-SAFETY, RTE-STAFF). Conflict recorded internally (ACT-1); no message sent to landlord, tenant or provider taking a side.

Safety actions taken first:
- Flagged the missing smoke/CO alarm test before the flat is described as ready for move-in or remarketed (event-013 context).
- Did not endorse the closure or state the property is ready.

Actions deliberately withheld:
- Did not message the landlord, tenant or provider naming one side of the provider/address conflict (rule of engagement 2).
- Did not re-instruct or chase any provider — the works are already logged complete (event-020); a chase risks duplicate work orders.
- Did not close or re-close the request: landlord confirmation and visit confirmation are unevidenced (CAP-CLOSE).
- Did not decide who pays for the burnt carpet (PRO-TENANT-LIABILITY).

## 2. Authority and evidence

Authority cited: ESC-CONFLICT, ESC-SAFETY, RTE-STAFF, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, RTE-LANDLORD, PRO-INSTRUCTIONS-FROM-CONTENT, CAP-DISPATCH-APPROVED
Rules applied by the policy gate: CAP-LOG

Key facts (source ids in brackets):
- F1: Case is check-out works at Flat 21, 11 Juniper Mews, Northbridge ZZ7 0ZZ: replace burnt carpet and repaint throughout, after tenant Harriet Ellis vacated. [index, event-001, event-004; high]
- F2: The maintenance provider assigned and briefed, and named to the tenant, was Cedar Utilities. [event-003, event-004, event-005; high]
- F3: The quote, the go-ahead and the completion record are all against a provider called Sawyer; no event records Cedar Utilities being stood down. [event-013, event-016, event-020; high]
- F4: An agency hold note places Sawyer at Flat 12, 122 Juniper Mews, Westmarsh ZZ8 7ZZ during the works window. [event-018; high]
- F5: Landlord approved the quote totalling £605 (paint £220, carpet ~27 sqm £240, bathroom vinyl £100, chrome sink waste £45); VAT was not stated. [event-013, event-015; high]
- F6: Approved scope includes bathroom vinyl and a sink waste, which were not in the instructed brief, and the quote describes a 'studio'. [event-001, event-013; high]
- F7: No appointment was ever confirmed; three or more reminders were sent to the provider and the only provider reply contained no appointment details. [event-006, event-007, event-008, event-012; high]
- F8: Landlord confirmation of completion was flagged as required and no landlord confirmation appears in the history before the request was closed. [event-024, event-027; high]
- F9: Keys return was confirmed; priority could not be decreased below 1. [event-026; high]
- F10: No record anywhere in the case of smoke or carbon monoxide alarm testing, although the flat is being prepared to remarket after fire damage to a carpet. [event-001, event-013, get_case_details; high]

Conflicts between sources:
- Agency records disagree on who holds the job: Cedar Utilities (assigned/briefed) vs Sawyer (quoted, instructed, completed). → Recorded internally (ACT-1) and put to the office; no party told which is correct. (unresolved)
- Agency records disagree on the property the instructed provider attended: Flat 21, 11 Juniper Mews, Northbridge vs Flat 12, 122 Juniper Mews, Westmarsh. → Escalated to property manager; works were billed against the Northbridge ticket. (unresolved)
- Approved and completed scope exceeds the instructed brief (bathroom vinyl, sink waste) and describes a 'studio'. → Landlord did approve the wider list at event-015; flagged to the office alongside the address conflict. (unresolved)
- System states all checks completed, but the landlord confirmation required at event-024 is not evidenced. → Closure challenged; landlord confirmation still owed. (unresolved)

Red flags:
- [data_quality] Provider identity and property address conflict between agency records in the same ticket (Cedar Utilities / Sawyer; Flat 21 Northbridge / Flat 12 Westmarsh); £605 of works may be recorded against the wrong address. → Recorded in the case note (ACT-1) and put to the property manager; no party was told which record is right.
- [safety_hazard] Works follow fire damage to a carpet and the flat is being readied to remarket; no smoke or CO alarm test is recorded anywhere in the case. → Raised in the handover as a check required before the flat is called ready for move-in.
- [data_quality] The only provider reply is an untrusted parsed summary that references 'the studio' and gives no appointment details ('does not mention appointment details'), and the automation flagged it for manual handling. → Treated as evidence only; no scope or booking inferred from it.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "006", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | add_note | completed | note=Post-closure review of check-out works, Flat 21, 11 Juniper… | {"id": "ACT-1"} | CAP-LOG |

## 4. Human handover / information requested

**To:** property_manager
**Question:** Before this closure stands: which provider attended which address, and can the landlord's completion confirmation and an alarm test be evidenced for Flat 21, 11 Juniper Mews?
**Facts (≤5):**
- Provider assigned and briefed was Cedar Utilities (event-003, event-005; tenant told event-004), but the quote, go-ahead and completion are all recorded against 'Sawyer' (event-013, event-016, event-020).
- Event-018 places Sawyer at a different property — Flat 12, 122 Juniper Mews, Westmarsh ZZ8 7ZZ — in the window between approval and completion.
- Landlord approved £220 paint + £240 carpet + £100 bathroom vinyl + £45 sink waste = £605, VAT not stated (event-013, event-015); the vinyl and sink waste go beyond the instructed brief (event-001).
- Event-024 required landlord confirmation of completion; no landlord message confirming it appears in the history, yet event-027 closed the request as all checks complete.
- Works follow a burnt carpet and the flat is being readied to remarket (event-013); no record anywhere of smoke or CO alarm testing.
**Gap:** No record shows Cedar Utilities being stood down or Sawyer formally instructed; no visit slot was ever confirmed (3+ reminders, event-006/007/008; provider reply event-012 gave no appointment details); no landlord completion confirmation; no alarm test record.
**Options:**
- Reopen final checks: confirm with the office which provider holds the job and that the £605 works were carried out at Flat 21, request the landlord's written completion confirmation, and have alarms tested and recorded before remarketing.
- Treat the works as verified on the strength of event-020 and leave the closure standing — accepts the risk that £605 of works were billed against the wrong address and that the flat is remarketed without an alarm test.
- Instruct a brief post-works inspection (including alarm test) at Flat 21 before remarketing, then close with a resolution naming the payer.
**Recommended:** Reopen final checks: resolve the provider/address conflict with the office, obtain the landlord's written completion confirmation, and record an alarm test before the flat is remarketed.
**Default if no answer:** Ticket stays at final_checks on hold (Waiting for Landlord); no further spend is instructed and the flat is not described as ready for move-in.
**Undo:** Nothing irreversible was done by me: one internal note (ACT-1). No party was messaged and no work was instructed.

Promises made or recorded:
- Agency → Tenant: Provider (named as Cedar Utilities) would contact the tenant to arrange a time, then the quote would be approved with the landlord [broken]
- Agency → Contractor: Provider to confirm a start and completion date for the approved works [open]

Clocks:
- CLK-S11 [in_force]: Repairs within a reasonable time once reported
- CLK-SOP-ACK [prior]: Acknowledge report within one working day
- CLK-GAS-CP12 [in_force]: Gas safety record renewed every 12 months
