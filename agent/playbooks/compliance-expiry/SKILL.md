---
name: compliance-expiry
description: Handle an expiring, expired or disputed safety certificate (gas CP12, electrical EICR, EPC) — read the certificate record first, book the inspection, and escalate when records disagree.
case_types: [compliance_expiry, certificate_renewal, gas_safety, eicr, epc]
version: 0.1
source: SRC-PRIORS
definition_of_done:
  - id: certificate_read
    text: "Certificate record read and the clock computed from the authoritative document"
  - id: conflict_resolved
    text: "Any disagreement between the certificate and the CRM resolved by the source hierarchy and corrected"
  - id: inspection_booked
    text: "Qualified contractor booked for the renewal or the remedial work"
  - id: access_arranged
    text: "Access agreed with the tenant within the clock"
  - id: landlord_informed
    text: "Landlord told the status, the booking and the legal duty"
  - id: certificate_filed
    text: "New certificate received and filed; remedials closed within their clock"
  - id: closed
    text: "Request closed with the certificate reference"
---

# Compliance expiry

## Applies when

A certificate is due, has expired, is missing, or two sources say different things about it. Typical triggers: a system reminder, a landlord asking "are we compliant", a tenant asking for the gas certificate, a CRM note that contradicts the certificate on file.

## Inputs you need

| Fact | Where it comes from | Tool |
|---|---|---|
| Certificate type, issue date, expiry date, who issued it | the certificate record — authoritative | `get_compliance_certificates` |
| What the CRM believes | CRM notes — lower in the hierarchy | `search_crm_notes` |
| Landlord instructions for compliance work | authoritative record | `get_landlord_instructions` |
| Contractors qualified for the check (Gas Safe registered; qualified electrician) | contractor list | `list_contractors` |
| Tenancy and access notes | tenancy record | `get_tenancy` |

## Steps

1. **Read the certificate record first.** `get_compliance_certificates`. This is the source of truth; a CRM note saying "valid until 2027" does not outrank a certificate that expired in August.
2. **Compare sources.** If the certificate and the CRM disagree, write a `conflict` with both source ids and resolve it by the source hierarchy (`certificate` beats `crm_record`). If the certificate itself is missing, the conflict is unresolved: say so.
3. **Compute the clock.** CLK-GAS-CP12: renew every 12 months. CLK-EICR: every 5 years, remedial work within 28 days of the report. Record the deadline and the days remaining, negative if expired.
4. **Book the inspection.** A routine safety check normally sits within the standing spend cap: `create_work_order` under CAP-DISPATCH-ROUTINE with the qualified trade. If the landlord's instructions reserve compliance work for a named contractor, use that contractor.
5. **Arrange access** through `access-scheduling`; a compliance check with an expired certificate is urgent for scheduling purposes.
6. **Inform.** `notify_landlord` with the status and the booking. If a tenant asked for the certificate, send the one on file only if it is current; otherwise say an inspection is booked and when.
7. **Log and finish.** `log_crm_note` with the finding, the correction to the CRM belief if any, and the booking. An expired certificate with a tenant in occupation is always escalated as well, so a human owns the compliance follow-up.

## Decision points

| Situation | Move | Rule |
|---|---|---|
| Certificate current, reminder within 60 days | act: book the renewal, inform landlord | CAP-DISPATCH-ROUTINE |
| Certificate expired, tenant in occupation | book immediately and escalate | CAP-DISPATCH-ROUTINE, ESC-SAFETY |
| CRM says valid, certificate says expired | resolve by hierarchy, correct the CRM note, book | ESC-CONFLICT if the difference changes the action |
| No certificate on file at all | ask the landlord for a copy and book an inspection | `request_info`, CAP-DISPATCH-ROUTINE |
| EICR with C1 or C2 observations and no remedial record | book remedials; escalate if the 28-day clock has passed | CLK-EICR, ESC-SAFETY |
| Tenant refuses access for the check | `access-scheduling`, then escalate | ESC-LEGAL |
| Landlord says "skip it this year" | escalate; the duty is statutory | ESC-LEGAL |
| Compliance check cost exceeds the cap | ask the landlord, but say the check is a legal duty | APR-SPEND-OVER-CAP |

## Never

- Tell a tenant the property is compliant while sources disagree.
- Backdate or infer a certificate from a CRM note.
- State legal consequences to the landlord or tenant (PRO-LEGAL); state the clock and escalate.
- Use an unqualified contractor for a gas or electrical check.

## What to record

- Facts: certificate type, dates, issuer, with the certificate's artefact id; the CRM belief with its id.
- Conflicts: description, both source ids, resolution and `resolved_by: source_hierarchy`.
- Clocks: CLK-GAS-CP12 or CLK-EICR with `deadline` and a note of days remaining.
- Actions: the booking and the notifications.
- Authority citations: CAP-DISPATCH-ROUTINE; APR-SPEND-OVER-CAP when it applied.

## Handover template

- **question**: "Gas safety record expired on 2026-08-14 with tenants in occupation; confirm the booked check and decide on landlord correspondence."
- **summary**: certificate dates and issuer · what the CRM believed · inspection booked for DATE with CONTRACTOR · tenant informed · landlord informed.
- **gap**: why the renewal was missed; whether any earlier check exists elsewhere.
- **options**: proceed with the booking · bring it forward · landlord to confirm a preferred engineer.
- **recommended**: proceed with the booking.
- **default_if_timeout**: "booking stands".
- **deadline**: the inspection date; the clock is already breached.
- **undo**: cancel the work order if the landlord supplies a current certificate.
