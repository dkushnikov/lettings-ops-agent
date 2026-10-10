# ANSWER — Case 034 — Case 034: Shower Repair Request

**Disposition:** NEEDS_INFO · **Urgency:** routine · **Case type:** maintenance_request · **Playbook:** maintenance-request

## Status

**Recap:** Closed shower ticket reviewed: result unverified with tenant and completion email names a different property; office task raised, tenant asked to confirm.
**Stage:** on_hold · **Hold:** Waiting for Tenant — Ava Fletcher to confirm the cold side runs and the temperature is controllable; in parallel the property manager must confirm which property the Meadow Works invoice covers (ACT-2).
**Last update:** 2025-06-16 18:54:35 UTC (event-017) · **Decided:** 2026-10-10 14:09 UTC
**Next step:** Tenant (Ava Fletcher) to confirm the shower now works; property manager to resolve the Flat 9 / Flat 17 address conflict on the paid invoice (ACT-2).

Definition of done (4/9 done):
- [x] assessed: Issue categorised and urgency set; damage-limiting steps given to the tenant where relevant — event-001 / event-003: fault categorised as shower repair, routine; scald caution given to tenant at ACT-3
- [ ] landlord_authority: Landlord approval obtained, or the spend sits inside the standing mandate, or the landlord is using their own contractor — event-004 is a system status line, not a landlord message; no landlord spend cap on file (APR-SPEND-OVER-CAP). Landlord's only own message is 'Paid today' (event-017), after the fact.
- [x] provider_assigned: Provider assigned and briefed; tenant told who is coming and what happens next — event-005, event-006, event-007
- [-] visit_confirmed: Visit slot confirmed with the tenant and the provider (or the landlord's own contractor is handling access) — No slot ever confirmed in the history; provider attended and reported directly (event-010) after the chase at event-008
- [n/a] quote_approved: Where a quote was required, the landlord approved the amount (VAT stated) before the work started — Provider repaired on site and charged a call-out; no quote was issued (event-010, event-011)
- [ ] work_result: Work result recorded from the provider — event-010 reports a 'temperature issue' cleaned and greased; does not address the reported cold-side fault — tenant confirmation requested (ACT-3)
- [ ] documents: Photos and invoice uploaded, or the reason for skipping recorded — event-014 skip reason 'Invoice sent to LL'; attachment-26-document not retrievable, amount/VAT unverified
- [x] invoice_to_landlord: Invoice forwarded to the landlord, or the request marked completed without payment with the reason — event-011 (invoice emailed to landlord) — but addressed with a conflicting property in the body; office task ACT-2
- [x] landlord_confirmation: Landlord confirmed completion — event-017 landlord: 'Paid today'
- [n/a] keys_returned: Keys returned, where a management key was issued for the visit — No management key issued; tenant-arranged access (event-007)
- [ ] closed: Request closed with a resolution that names who paid — event-016 closed by automation, but work result, documents and the property/invoice conflict remain unresolved; not re-closed (CAP-CLOSE)

## 1. Decision

The ticket was closed by the agency's automation on 2025-06-02 (event-016) on a result that does not clearly match the reported fault and on a completion email whose body names a different property. I did not re-dispatch, did not re-send an invoice, and asserted no address to any party. I logged the conflict (ACT-1), raised an office task to verify which property the paid Meadow Works invoice covers (ACT-2), and asked the tenant to confirm whether the cold side now runs and the temperature is controllable (ACT-3). The case now waits on the tenant's answer and the office's address check.

Safety actions taken first:
- Scald check: tenant's report of water 'sometimes too hot' (event-001) carried into the record; tenant asked to confirm the temperature can now be mixed and controlled, with a caution to take care in the meantime (ACT-3). No scald injury or other hazard reported or observed.

Actions deliberately withheld:
- Did not re-dispatch Meadow Works or any other contractor: no confirmed outstanding fault and no landlord approval or spend cap on file (APR-SPEND-OVER-CAP).
- Did not re-issue or correct the invoice email to the landlord, and did not state which property the charge belongs to (ESC-CONFLICT / rule on disagreeing agency records).
- Did not re-close the request: result and invoice checks are unverified (CAP-CLOSE).
- Did not comment on who pays or on the payment already made (PRO-TENANT-LIABILITY, PRO-PAYMENTS).

## 2. Authority and evidence

Authority cited: CAP-NOTIFY, CAP-LOG, CAP-HUMAN-TASK, CAP-CLOSE, APR-SPEND-OVER-CAP, ESC-CONFLICT, RTE-TENANT, RTE-STAFF, PRO-TENANT-LIABILITY, PRO-PAYMENTS, CLK-S11
Rules applied by the policy gate: CAP-HUMAN-TASK, CAP-LOG, CAP-NOTIFY

Key facts (source ids in brackets):
- F1: Tenant reported the cold side of the shower not delivering water, with the warm side sometimes too hot, at Flat 9, 9 Willowmere Road, Bellmere, ZZ9 7ZZ on 2025-05-29. [index, event-001, get_case_details; high]
- F2: A system line records 'Landlord approval confirmed. Proceed to provider selection.' (2025-05-30); it is a system status line, not a landlord message, so it is not an approval under CAP-DISPATCH-APPROVED. [event-004; high]
- F3: Meadow Works was assigned and both tenant and provider were briefed on 2025-05-30; a chase was sent to the provider on 2025-05-31. [event-005, event-006, event-007, event-008; high]
- F4: No visit slot was ever confirmed in the visible history; the provider replied only with a completion message that the system could not parse. [event-009, event-010; high]
- F5: Provider's report (untrusted): engineer found a 'temperature issue', 'cleaned and greased it', invoice attached; it does not state that the cold side now delivers water. [event-010; medium]
- F6: The agency's completion email to the landlord is headed Flat 9, 9 Willowmere Road but states in the body that Meadow Works attended Flat 17, 77 Harbour View, Northbridge, ZZ9 1ZZ and charged a call-out. [event-011; high]
- F7: Invoice upload was skipped with reason 'Invoice sent to LL'; attachment-26-document could not be retrieved, so amount, VAT and provider on the invoice are unverified. [event-014, get_attachment; high]
- F8: The request was marked completed and closed on 2025-06-02; the landlord replied 'Paid today' on 2025-06-16. [event-013, event-016, event-017; high]
- F9: No landlord spend cap or standing instruction is available in this case record, so no standing dispatch authority exists (CAP-DISPATCH-ROUTINE default cap £0). [get_case_details; medium]

Conflicts between sources:
- Agency records disagree on which property the completed shower job and its invoice belong to: Flat 9, 9 Willowmere Road (email header, ticket record) versus Flat 17, 77 Harbour View, Northbridge (email body). → No address asserted to any party; office task ACT-2 raised for the property manager to verify the invoice address and whether the landlord's payment needs correcting. (asked)
- Provider's reported work ('temperature issue', cleaned and greased) does not plainly correspond to the reported fault (no water from the cold side). → Tenant asked to confirm whether the cold side now runs and the temperature is controllable (ACT-3). (asked)

Red flags:
- [data_quality] Provider email could not be parsed by the system (event-009) and the invoice attachment referenced at event-011 is not retrievable; closure checks were completed on unverified data. → Logged internally (ACT-1) and included in the office task (ACT-2).
- [data_quality] Completion email to the landlord names a different property in its body than in its header, and payment has already been made against it. → Conflict recorded; property manager task raised (ACT-2); no address stated to landlord or tenant.

## 3. Actions (proposed → attempted → completed)

| # | Tool | Status | Key inputs | Result / receipt | Gate |
|---|---|---|---|---|---|
| 1 | get_case_details | completed |  | {"id": "034", "attachments_hidden": 0} | allow |
| 2 | get_action_ledger | completed |  | [] | allow |
| 3 | get_attachment | completed | name=attachment-26-document | {"error": "no attachment named attachment-26-document"} | allow |
| 4 | search_history | completed | query=Harbour View | [{"event": "event-011", "timestamp": "2025-06-02 01:22:24 UTC", "channel": "Email", "from": "Northbridge Lettings", "to": "Landlord", "excerpt": "[2025-06-02 0… | allow |
| 5 | add_note | completed | note=Review of closed ticket (closed event-016). Three open poin… | {"id": "ACT-1"} | CAP-LOG |
| 6 | create_human_task | completed | queue=property_manager, title=Case 034 closed on conflicting address — verify which prope…, summary=Ticket 034 (Flat 9, 9 Willowmere Road, Bellmere, ZZ9 7ZZ) w… | {"id": "ACT-2"} | CAP-HUMAN-TASK |
| 7 | notify_tenant | completed | message=Dear Ava Fletcher,  Regarding your shower report at Flat 9,… | {"id": "ACT-3"} | CAP-NOTIFY |

## 4. Human handover / information requested

- Ask **tenant**: Does the cold side of the shower now run normally, and can the temperature be mixed so it is no longer too hot to use safely? (blocking; The provider's report (event-010) describes a 'temperature issue' cleaned and greased; it does not confirm the reported fault of no water from the cold side (event-001), and no tenant confirmation is on file before closure (event-016).)
- Ask **property_manager**: Which property does the Meadow Works shower call-out invoice actually relate to — Flat 9, 9 Willowmere Road or Flat 17, 77 Harbour View — and does the landlord's payment (event-017) need correcting? (blocking; The agency's own completion email (event-011) carries the Flat 9 header but a Flat 17 body; the invoice itself (attachment-26-document) is not retrievable, so amount, VAT and provider are unverified.)

Promises made or recorded:
- agency → tenant: If the cold side still does not run or the temperature is still unsafe, we will arrange a return visit with the provider [open]

Clocks:
- CLK-S11 [in_force]: Repair within a reasonable time from report
- CLK-SOP-ACK [prior]: Acknowledge tenant report within one working day
