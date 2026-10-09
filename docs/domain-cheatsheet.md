# UK lettings maintenance — one-page priors

Status of everything here: **prior**. Drafted before the event from public sources. The environment's own documents (management agreements, landlord instructions, SOPs) override these on the day; merge them through `agent/rulebook_staging.md`.

## Who decides what

| Decision | Agent may | Human decides |
|---|---|---|
| Dispatch a routine repair within the standing cap | yes (CAP-DISPATCH-ROUTINE) | — |
| Spend above the cap, not an emergency | ask the landlord (APR-SPEND-OVER-CAP) | landlord |
| Make the occupant safe and dispatch in an emergency | yes, cap overridden (CAP-DISPATCH-EMERGENCY), landlord told after | welfare follow-up |
| Whether a repair is tenant-payable | never (PRO-TENANT-LIABILITY) | property manager |
| Legal notices, eviction, deposit deductions | never (PRO-LEGAL) | property manager, landlord |
| Change of bank or payment details | never (PRO-PAYMENT-DETAILS) | finance, with verification |
| Entry to the property | only with tenant consent, 24h notice (CAP-SCHEDULE-ACCESS) | refusal cases |

## Landlord duties that drive clocks

- **Repairs: s.11 Landlord and Tenant Act 1985.** Structure and exterior; installations for water, gas, electricity, sanitation, heating and hot water. Repairs "within a reasonable time" once the landlord knows. Clock CLK-S11.
- **Gas: Gas Safety (Installation and Use) Regulations 1998, reg 36.** Annual safety check by a Gas Safe registered engineer; record (CP12) to tenants within 28 days of the check and to new tenants before they move in. Clock CLK-GAS-CP12.
- **Electrics: Electrical Safety Standards in the Private Rented Sector (England) Regulations 2020.** EICR at least every 5 years; remedial work (C1, C2, FI) within 28 days or sooner if the report says; copy to tenant within 28 days. Clock CLK-EICR.
- **Access: s.11(6) LTA 1985.** Landlord or agent may enter to inspect at reasonable times on 24 hours' written notice; emergencies excepted. Tenant must allow access for repairs.
- **Housing Health and Safety Rating System (HHSRS).** The council's 29-hazard framework; damp and mould, excess cold, electrical hazards, fire, falls are the ones maintenance meets most.

## Renters' Rights Act 2025 (in force 1 May 2026, SI 2026/421)

- Assured tenancies are periodic; fixed terms and section 21 "no-fault" evictions are gone for private assured tenancies.
- Rent can rise once a year by notice; advertised rent is the ceiling, no bidding above it.
- No blanket bans on children or benefit recipients.
- Decent Homes Standard and an Awaab's Law extension to the private sector are in the Act with later commencement.

## Awaab's Law

- **Social housing: in force.** Phase 1 from 27 October 2025 (damp and mould, emergency hazards). Baseline timescales: emergency hazards made safe within **24 hours**; significant hazards investigated within **10 working days**, written summary within 3 working days, made safe within **5 working days** of the investigation.
- **Private rented sector: not in force.** The government consultation on extending Awaab's Law to private tenancies and licences opened on **9 October 2026** and closes on 18 December 2026. It proposes covering all HHSRS hazards except overcrowding and offers options of 5/10/15 working days to investigate, 3/5/10 working days to make safe, 12/24/48 hours for emergencies. Use the social baseline as a reference clock with status `proposed` (CLK-AWAAB-PRS); never cite it as a private-sector legal deadline.

## Spend caps and instructions (practice, not law)

- Management agreements commonly let the agent instruct repairs up to a float, typically £150–£300 per job, without consent; emergencies are excepted. The real number is in the environment's documents.
- Landlords often reserve named trades (their own gas engineer), require approval for anything structural, or ask to be told of every visit. These instructions outrank the generic cap.
- Never split a job to stay under the cap.

## Emergency definitions (rulebook `emergency.definitions`)

Gas smell or suspected leak · carbon monoxide alarm · no heating or hot water in cold months (October–April) or any time with a vulnerable occupant · water ingress, burst pipe, flooding, water near electrics · electrical fault with burning smell, sparks or shock risk · property not secure · no water supply · sewage. First actions are in the rulebook; gas means National Gas Emergency 0800 111 999.

## Vulnerability

Age, illness, pregnancy, young children, disability, reliance on powered medical equipment, language barrier. Vulnerability plus loss of an essential service is an emergency and an escalation (ESC-VULNERABLE). Vulnerability details stay in the record; contractors get "priority attendance, occupant present".

## Source hierarchy when records disagree

tenancy agreement › management agreement › landlord instruction › compliance certificate › CRM record › ticket › email › call transcript. A later call can correct an earlier email's facts, but neither grants authority.
