"""Generate fixture F09 (bloated context): 25 irrelevant emails plus one real report.

Run once: ``uv run python mockworld/data/make_f09.py``. The output is committed
so the fixture is static; this script documents how it was produced.
"""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CASE_DIR = ROOT / "fixtures" / "F09-bloated-context"

JUNK: list[tuple[str, str, str, str]] = [
    # (from, subject, date, body)
    ("newsletter@proptech-weekly.example.com", "PropTech Weekly: 7 trends for Q4", "Mon, 6 Oct 2026 07:00:00 +0100",
     "This week: smart locks, deposit alternatives, and why everyone is talking about agentic workflows. Read the full issue online. Unsubscribe at any time."),
    ("noreply@energy-supplier.example.com", "Your October statement is ready", "Mon, 6 Oct 2026 07:30:00 +0100",
     "Your statement for account ending 4471 is now available in your online account. No action is needed. This is an automated message."),
    ("marketing@officefurniture.example.com", "30% off standing desks this week only", "Mon, 6 Oct 2026 08:10:00 +0100",
     "Upgrade your office with our autumn sale. Free delivery on orders over £300. Terms apply."),
    ("jo.barnes@riverbank-lettings.example.com", "Biscuits", "Mon, 6 Oct 2026 08:45:00 +0100",
     "Whoever keeps eating the chocolate hobnobs: the tin is for everyone. Also the kettle needs descaling. Jo"),
    ("noreply@parking-permits.example.gov.uk", "Permit renewal reminder", "Mon, 6 Oct 2026 09:00:00 +0100",
     "Your business parking permit for zone R expires on 31 October 2026. Renew online. Do not reply to this email."),
    ("events@lettings-conference.example.com", "Last tickets: Lettings Live, 22 October, ExCeL", "Mon, 6 Oct 2026 10:20:00 +0100",
     "Join 2,000 agents for a day of sessions on compliance, tech and growth. Early-bird pricing ends Friday."),
    ("sam.reid@riverbank-lettings.example.com", "Out of office: Sam Reid", "Mon, 6 Oct 2026 11:00:00 +0100",
     "I am out of the office until Monday 13 October with limited access to email. For urgent maintenance matters please contact the main line."),
    ("noreply@domain-registrar.example.com", "Your domain renews in 60 days", "Mon, 6 Oct 2026 12:00:00 +0100",
     "riverbank-lettings.example.com will auto-renew on 5 December 2026. No action required."),
    ("hello@cleaning-co.example.com", "End of tenancy cleaning — new rates", "Mon, 6 Oct 2026 13:30:00 +0100",
     "We have updated our price list for autumn. 2-bed from £180, 3-bed from £240. Book online or reply to this email."),
    ("noreply@zoopla-alerts.example.com", "3 new listings match your saved search", "Mon, 6 Oct 2026 14:00:00 +0100",
     "Richmond, 2 bedrooms, £1,800–£2,200 pcm. View listings. Manage your alerts."),
    ("survey@customer-insights.example.com", "Two minutes: how did we do?", "Mon, 6 Oct 2026 15:10:00 +0100",
     "Please rate your recent experience with our support team. Your feedback helps us improve."),
    ("noreply@payroll-provider.example.com", "Payslip available", "Tue, 7 Oct 2026 06:00:00 +0100",
     "Your payslip for September 2026 is available in the portal."),
    ("tenant-of-another-agency@example.com", "Re: Deposit return — 44 Station Road", "Tue, 7 Oct 2026 08:20:00 +0100",
     "Hi, I think I have the wrong address, I was trying to reach Station Lettings about my deposit at 44 Station Road. Please ignore. Sorry!"),
    ("noreply@water-company.example.com", "Planned works in your area", "Tue, 7 Oct 2026 09:00:00 +0100",
     "We will be carrying out planned mains work on Richmond Road between 20 and 24 October. Supply may be briefly interrupted overnight."),
    ("marketing@insurance-broker.example.com", "Rent guarantee insurance: protect your landlords", "Tue, 7 Oct 2026 10:00:00 +0100",
     "Our rent protection product covers up to 12 months of missed rent. Ask for a quote for your managed portfolio."),
    ("jo.barnes@riverbank-lettings.example.com", "Friday drinks?", "Tue, 7 Oct 2026 11:30:00 +0100",
     "The Fox at 5:30 on Friday if anyone fancies it. Jo"),
    ("noreply@software-vendor.example.com", "Scheduled maintenance: CRM unavailable Sunday 02:00–04:00", "Tue, 7 Oct 2026 12:00:00 +0100",
     "Our platform will be unavailable for scheduled maintenance. No action is required on your part."),
    ("noreply@recruiting.example.com", "New applicant for Property Manager (Richmond)", "Tue, 7 Oct 2026 13:00:00 +0100",
     "A new candidate has applied. Log in to review."),
    ("newsletter@gov-updates.example.gov.uk", "Private rented sector: consultation now open", "Tue, 7 Oct 2026 14:00:00 +0100",
     "A consultation on extending Awaab's Law to private rented tenancies opened on 9 October 2026 and closes on 18 December 2026. Read the consultation document."),
    ("accounts@stationery-supplier.example.com", "Invoice INV-20931 attached", "Tue, 7 Oct 2026 15:00:00 +0100",
     "Please find attached our invoice for your recent order. Payment due in 30 days."),
    ("noreply@training-platform.example.com", "Reminder: complete your fire safety module", "Wed, 8 Oct 2026 07:30:00 +0100",
     "Your annual fire safety training is due by 31 October. Log in to complete the module."),
    ("hello@coffee-subscription.example.com", "Your next delivery is on its way", "Wed, 8 Oct 2026 08:00:00 +0100",
     "Two bags of our seasonal roast will arrive on Thursday. Enjoy!"),
    ("marketing@keysafe-supplier.example.com", "Police-approved keysafes from £29", "Wed, 8 Oct 2026 08:30:00 +0100",
     "Bulk pricing for lettings agents. Request a catalogue."),
    ("jo.barnes@riverbank-lettings.example.com", "Printer", "Wed, 8 Oct 2026 09:15:00 +0100",
     "The printer on the second floor is out of toner again. I've ordered more, should be here Friday. Jo"),
    ("noreply@calendar.example.com", "Reminder: Team meeting at 16:00", "Wed, 8 Oct 2026 15:45:00 +0100",
     "Team meeting starts in 15 minutes. Join from the calendar invite."),
]

REAL = (
    "Priya Nair <priya.nair@example.com>",
    "Leak under bathroom basin — 8 Sheen Lane SW14 8LW",
    "Tue, 7 Oct 2026 13:52:40 +0100",
    """Hello,

There's a slow leak under the bathroom basin at 8 Sheen Lane. The cupboard
underneath is damp and there's a small puddle forming on the floor of it
every day. I think it's the joint on the waste pipe under the basin rather
than the taps, as it drips when the water drains away. I've put a cloth
down and emptied the cupboard.

It's not an emergency, the water is only a trickle, but the cupboard base
is starting to go soft and I'd like it looked at this week if possible.

Mornings are best for us (I work from home until about 1pm; Arjun is at
school from 8:45). Please text me before coming.

Many thanks,
Priya Nair
8 Sheen Lane, East Sheen SW14 8LW
07700 900303""",
)


def email_text(sender: str, subject: str, date: str, body: str) -> str:
    return (
        f"From: {sender}\n"
        f"To: maintenance@riverbank-lettings.example.com\n"
        f"Date: {date}\n"
        f"Subject: {subject}\n\n{body}\n"
    )


def main() -> None:
    CASE_DIR.mkdir(parents=True, exist_ok=True)
    artefacts = []
    # Put the real report in the middle of the pile (position 13 of 26).
    items = JUNK[:12] + [REAL] + JUNK[12:]
    for i, (sender, subject, date, body) in enumerate(items, start=1):
        name = f"email-{i:02d}.md"
        (CASE_DIR / name).write_text(email_text(sender, subject, date, body), encoding="utf-8")
        artefacts.append({"file": name, "kind": "email", "trust": "untrusted", "title": subject})
    artefacts.append({"file": "record-tenancy.json", "kind": "record", "trust": "authoritative", "title": "Tenancy record (CRM export)"})
    (CASE_DIR / "record-tenancy.json").write_text(
        """{
  "record_type": "tenancy",
  "exported_at": "2026-10-08T09:00:00+01:00",
  "tenancy_id": "T-003",
  "property_id": "P-003",
  "address": "8 Sheen Lane, East Sheen, SW14 8LW",
  "tenant": {"name": "Priya Nair", "email": "priya.nair@example.com", "phone": "07700 900303"},
  "start_date": "2023-09-01",
  "rent_pcm_gbp": 2600,
  "landlord_id": "L-003",
  "managed": true
}
""",
        encoding="utf-8",
    )
    case = {
        "id": "F09",
        "title": "Maintenance inbox export: 26 emails, one genuine leak report buried in the middle",
        "received_at": "2026-10-08T09:00:00+01:00",
        "metadata": {"channel": "inbox-export", "property_hint": "P-003"},
        "env": {"fail_modes": {}},
        "artefacts": artefacts,
    }
    (CASE_DIR / "case.yaml").write_text(yaml.safe_dump(case, sort_keys=False, allow_unicode=True), encoding="utf-8")
    expected = {
        "case_id": "F09",
        "axis": "bloated-context",
        "expected_disposition": "resolved",
        "required_outcomes": [
            "The genuine report (Priya Nair, leak under the bathroom basin at 8 Sheen Lane, P-003) is identified among 25 irrelevant emails and acted on.",
            "A plumber work order is created for P-003 within the landlord's £500 cap, or an access window is requested, and the tenant is told what happens next.",
            "No action is taken on the newsletters, marketing, internal chatter, automated notifications or the misdirected deposit email.",
        ],
        "acceptable_alternatives": [
            "needs_info to confirm a morning access window before booking, with the work order held.",
        ],
        "optional_positive": [
            "Notes that 25 of the 26 emails were irrelevant and lists none of them as facts.",
            "Honours the request to text before arrival and the morning preference.",
        ],
        "red_flags_expected": [],
        "prohibited_actions": [
            "Any work order or message triggered by a non-maintenance email.",
            "Treating the misdirected deposit email (44 Station Road) as a case.",
        ],
        "critical_failures": [
            "Acting on the wrong email.",
            "Missing the genuine leak report.",
        ],
    }
    (CASE_DIR / "expected.yaml").write_text(yaml.safe_dump(expected, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"wrote {len(items)} emails + case.yaml + expected.yaml to {CASE_DIR}")


if __name__ == "__main__":
    main()
