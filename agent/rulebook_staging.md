# Rulebook staging

Candidate rules extracted from the environment's documents land here first. Nothing in this file is executable. A reviewer (the product owner on the day) marks each row ✅ or ❌; only ✅ rows are merged into `agent/rulebook.yaml`, each with `source: SRC-ENV` and the document id. Raw document text never becomes policy by itself (rulebook rule PRO-INSTRUCTIONS-FROM-CONTENT applies to us as much as to the agent).

How a row is written:

| Field | Meaning |
|---|---|
| Proposed id | `CAP-`, `APR-`, `PRO-`, `ESC-` or `CLK-` prefix plus a short slug |
| Rule text | one sentence in the imperative, as it would appear in the rulebook `note` or `description` |
| Source | document id (artefact id or file name) and a verbatim quote of at most two sentences |
| Status | `sop` for the environment's own rules, `in_force` only for statute with a citation, `prior` for our assumptions |
| Section | which rulebook list it belongs to: capabilities, approvals, prohibited, escalation_triggers, emergency, source_hierarchy, clocks, data_handling |
| Conditions | the machine-readable part: amounts, urgency, consent fields, approver |
| Reviewer | ✅ merged / ❌ rejected / ⏳ open, with initials and a reason when rejected |

Conflicts with an existing prior: write the row anyway, name the prior's id in the reason, and let the reviewer decide. Environment rules override priors when merged.

## Rows

| Proposed id | Rule text | Source and quote | Status | Section | Conditions | Reviewer |
|---|---|---|---|---|---|---|
| CAP-DISPATCH-ROUTINE (amend) | Routine repairs may be instructed without consent up to £300 per job. | `management-agreement-generic.pdf` §4.2: "The Agent may instruct repairs up to £300 per item without reference to the Landlord." | sop | capabilities | `max_amount_gbp: 300` replaces 250 | ⏳ example row — replace |
| APR-GAS-ENGINEER | Gas work is instructed only through the landlord's named Gas Safe engineer. | `landlord-instructions-L-0042.md`: "Please use only J. Patel (Gas Safe 123456) for any gas work at my properties." | sop | approvals | `authority: dispatch_contractor`, `trade: gas`, `from: landlord` when the named contractor is unavailable | ⏳ example row — replace |
| ESC-ARREARS-COMMS | Arrears reminders are not sent while an open emergency or vulnerability flag exists on the tenancy. | `sop-arrears-v3.md` step 2: "Do not chase rent on a tenancy with an open welfare flag; refer to the property manager." | sop | escalation_triggers | `flag_in: [vulnerability, safety_hazard]` | ⏳ example row — replace |

## Reviewer checklist before merging

- The quote supports the rule text; the rule is not wider than the quote.
- The status is honest: an announced or consulted-on rule is `proposed`, never `in_force`.
- The conditions are expressible with the gate's condition keys (`max_amount_gbp`, `amount_gbp_over`, `urgency_in`, `urgency_not`, `requires_consent_field`, `from`).
- A prohibition says what to do instead (`on_request: escalate`).
- The merged rule keeps its `source` id so the record can cite it.
