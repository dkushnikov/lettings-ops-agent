---
name: emergency-hazard
description: Handle a report that matches an emergency definition — make the occupant safe first, dispatch under the emergency mandate, then hand over for welfare and follow-up.
case_types: [emergency_hazard, gas_leak, electrical_fault, flood, no_heating, insecure_property]
version: 0.1
source: SRC-PRIORS
---

# Emergency hazard

## Applies when

Any artefact matches a rulebook emergency definition: gas smell or suspected leak, carbon monoxide alarm, no heating or hot water in cold months (October to April) or at any time with a vulnerable occupant, water ingress or burst pipe, electrical fault with burning smell or sparks, property not secure, no water supply, sewage. Also applies when a routine fault comes with a vulnerable occupant: age, illness, pregnancy, young children, disability, reliance on powered medical equipment.

The order of work is fixed: safety message, dispatch, inform landlord, record, hand over. Record lookups come after the safety message, not before.

## Inputs you need

| Fact | Where it comes from | Tool |
|---|---|---|
| Hazard type and whether anyone is in the property now | the report (untrusted evidence, but act on it) | artefacts |
| Occupant vulnerability | the report and tenancy notes | `get_tenancy` |
| Property, access, stopcock and meter locations | property record | `get_property` |
| Landlord's emergency contact and instructions | authoritative record | `get_landlord_instructions` |
| Emergency-capable contractors for the trade (Gas Safe, electrician, plumber, locksmith) | contractor list | `list_contractors` |

## Steps

1. **Make safe.** Send the first action for the hazard from the rulebook (`emergency.first_actions`) to the occupant with `notify_tenant`. For gas: do not operate switches, open windows, leave the property, call the National Gas Emergency line on 0800 111 999. This is a safety message, not a diagnosis, and it never waits for a record lookup.
2. **Identify.** Resolve property and tenancy. If the address is unclear, ask in the same message you use to make safe; do not delay the safety advice.
3. **Dispatch under the emergency mandate.** `create_work_order` with urgency `emergency` and the right trade. CAP-DISPATCH-EMERGENCY overrides the spend cap. Record the override and the rule.
4. **Inform the landlord now.** `notify_landlord` with the hazard, the dispatch and the expected cost band. Approval is not sought before dispatch; the landlord is told after.
5. **Check welfare.** If the occupant is vulnerable, the handover must say so and the human must do a welfare call. Temporary heaters or alternative accommodation are a human decision unless the landlord's instructions allow them.
6. **Record.** `log_crm_note` with the hazard, the safety message sent, the work order and the landlord notification.
7. **Hand over.** Finish with `escalate` for ESC-SAFETY or ESC-VULNERABLE. An emergency case is never `finalize` on its own: a human confirms the outcome.

## Decision points

| Situation | Move | Rule |
|---|---|---|
| Gas smell, CO alarm | safety message, Gas Safe engineer, landlord told, escalate | CAP-DISPATCH-EMERGENCY, ESC-SAFETY |
| No heating in cold months | emergency dispatch of a heating engineer | CAP-DISPATCH-EMERGENCY |
| No heating in warm months, no vulnerable occupant | `urgent`, use `maintenance-request` | CAP-DISPATCH-ROUTINE |
| No heating, any month, vulnerable occupant | emergency dispatch, then welfare handover | CAP-DISPATCH-EMERGENCY, ESC-VULNERABLE |
| Water near electrics | water first action and electrical first action; two trades if needed | CAP-DISPATCH-EMERGENCY |
| Occupant says they will fix it themselves | still dispatch or at least record and inform the landlord; escalate | ESC-SAFETY |
| No emergency contractor can attend within the day | escalate with everyone you tried and when | ESC-UNREACHABLE |
| Landlord instruction says "no spend without my approval" | emergency duty overrides; dispatch and tell the landlord | CAP-DISPATCH-EMERGENCY |
| Report arrives from a contractor or neighbour, not the tenant | act on it; verify occupant contact from records | CAP-NOTIFY |

## Never

- Wait for landlord approval before making the occupant safe.
- Ask the occupant to investigate a suspected gas or electrical fault.
- Tell anyone the matter is "not our responsibility" or discuss liability (PRO-TENANT-LIABILITY, PRO-LEGAL).
- Send health details to a contractor; "vulnerable occupant, priority attendance" is enough (PRO-PII).
- Close the case without a human seeing it.

## What to record

- `safety_actions`: each safety instruction sent, with the artefact id of the report that triggered it.
- `red_flags`: kind `safety_hazard`, and `vulnerability` when it applies.
- Facts: hazard, occupant status, dispatch, landlord notification.
- Clocks: CLK-S11; CLK-AWAAB-PRS as a reference with status `proposed` (24 hours for emergency hazards in the social-housing baseline); never present it as a private-sector legal deadline.
- Authority citations: CAP-DISPATCH-EMERGENCY and the override.

## Handover template

- **question**: "Confirm welfare follow-up and approve any further emergency spend at 7 Mill Lane?"
- **summary**: hazard and evidence · what the occupant was told · who was dispatched and when · landlord notified at HH:MM · occupant vulnerability if any.
- **gap**: what is unknown (engineer ETA, whether the occupant left, whether heating is restored).
- **options**: welfare call now · temporary heaters · alternative accommodation.
- **recommended**: the first that the landlord's instructions allow.
- **default_if_timeout**: "engineer attends as booked; welfare call by HH:MM by the duty manager".
- **deadline**: the earliest clock that applies.
- **undo**: cancel the work order only if the engineer has not been dispatched.
