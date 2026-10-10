"""Extract structure from the organisers' Property Management cases into a JSON index.

Reads <cases>/NNN/{index.md,history.md} with the Dwelly adapter's parsers and writes one object per case:
taxonomy, parties, channels, holds, update sequence, decision points, human interventions, money mentions,
quirks. `docs/pm-cases-analysis.md` and `docs/pm-cases-cheatsheet.md` were written from this index.

Run:
  make pm-index
  uv run python -m evalkit.pm_cases_extract --cases "../HackatonPublicCases/Property Management" \
      --out data/pm-cases-index.json [--stats runs/pm-cases-stats.json]
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

from harness.adapters.dwelly import parse_history, parse_index

DEFAULT_CASES = Path("../HackatonPublicCases/Property Management")
DEFAULT_OUT = Path("data/pm-cases-index.json")

AGENCY_MARKERS = ("agency", "system", "northbridge")

# ---------------------------------------------------------------- taxonomy
TYPE_RULES = [
    # (case_type, subtype, regex on title+request)
    ("inspection", "inspection", r"property inspection"),
    ("other", "solar_meter_reading", r"solar panel"),
    ("checkout_cleaning", "end_of_tenancy_clean", r"check[- ]?out clean|cleaning estimate"),
    ("checkout_works", "refurb_after_checkout", r"check[- ]?out works"),
    ("plumbing", "pipe", r"water pipe"),
    ("window_door", "door", r"garden door|shed door|front door repair"),
    ("garden", "garden", r"garden|hedge"),
    ("access", "keys", r"key replacement"),
    ("access", "lock", r"lock repair"),
    ("appliance_repair", "dishwasher", r"dishwasher"),
    ("appliance_repair", "oven", r"\boven\b"),
    ("appliance_repair", "washing_machine", r"washing machine"),
    ("appliance_repair", "extractor_fan", r"extractor fan"),
    ("plumbing", "shower", r"shower"),
    ("plumbing", "toilet", r"toilet"),
    ("plumbing", "drain", r"drain"),
    ("plumbing", "pipe", r"water pipe"),
    ("plumbing", "basin", r"basin"),
    ("plumbing", "tap", r"\btap\b|plumbing"),
    ("window_door", "window", r"window"),
    ("window_door", "door", r"door"),
]


def classify(title: str, request: str) -> tuple[str, str]:
    text = f"{title} {request}".lower()
    for ctype, sub, rx in TYPE_RULES:
        if re.search(rx, title.lower()):
            return ctype, sub
    for ctype, sub, rx in TYPE_RULES:
        if re.search(rx, text):
            return ctype, sub
    return "other", "unclassified"


# ---------------------------------------------------------------- helpers
def is_agency(sender: str) -> bool:
    s = sender.lower()
    return any(m in s for m in AGENCY_MARKERS)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def short(s: str, n: int = 140) -> str:
    s = norm(s)
    return s if len(s) <= n else s[: n - 1] + "…"


def parse_ts(ts: str) -> datetime:
    return datetime.strptime(ts.replace(" UTC", ""), "%Y-%m-%d %H:%M:%S")


HOLD_RE = re.compile(r"Put on hold(?: by (?P<who>[^.]+?))?\. Reason: (?P<reason>[^.]+?)(?:\.\s*Comment: (?P<comment>.*))?\.?$", re.S)

# System update phrases → canonical state labels (regex, label)
UPDATE_LABELS = [
    (r"^Please complete landlord approval step first", "ASK_LANDLORD_APPROVAL"),
    (r"^Please approve selection of provider and category", "SELECT_PROVIDER_AND_CATEGORY"),
    (r"^Waiting for landlord/tenant response before provider selection", "WAIT_LL_TENANT_3D"),
    (r"^Message received from landlord/tenant\. Please review and proceed manually", "LL_TENANT_REPLY_REVIEW"),
    (r"^No landlord/tenant response after \d+ days", "NO_LL_TENANT_REPLY_REVIEW"),
    (r"^Landlord approval confirmed", "LANDLORD_APPROVED"),
    (r"^Maintenance provider assigned|^New provider has been assigned", "PROVIDER_ASSIGNED"),
    (r"^Please check if we need to provide a response to landlord", "CHECK_REPLY_LANDLORD"),
    (r"^Please check if we need to provide a response to provider", "CHECK_REPLY_PROVIDER"),
    (r"^Please check if we need to provide a response to tenant", "CHECK_REPLY_TENANT"),
    (r"^\d\+ reminders have been sent to provider", "PROVIDER_REMINDERS_EXHAUSTED"),
    (r"^Email received from provider, but expected data could not be extracted", "PROVIDER_EMAIL_UNPARSED"),
    (r"^Visit date selected|^Task has been moved to Visit date confirmed|^Visit time approved|^Rescheduled visit time", "VISIT_SCHEDULED"),
    (r"^Resumed auto waiting for provider visit date", "WAIT_PROVIDER_VISIT"),
    (r"^Quote was approved by landlord", "QUOTE_APPROVED"),
    (r"^The request was updated to the start stage|^Job was updated to start stage", "BACK_TO_START_STAGE"),
    (r"^No work results", "NO_WORK_RESULTS_REVIEW"),
    (r"^Work results isset", "WORK_RESULTS_SELECT_STAGE"),
    (r"^Please add results of inspection", "ADD_INSPECTION_RESULTS"),
    (r"^Inspection document uploaded", "INSPECTION_UPLOADED"),
    (r"^Task has been moved to Result", "MOVED_TO_RESULT"),
    (r"^Request marked as completed, lets do the final checks", "FINAL_CHECKS"),
    (r"^Need confirmation from landlord", "NEED_LANDLORD_CONFIRMATION"),
    (r"^We need to check the key return", "CHECK_KEY_RETURN"),
    (r"^Keys return confirmed", "KEYS_RETURN_CONFIRMED"),
    (r"^All checks have been completed; the request is now closed", "CLOSED_ALL_CHECKS"),
    (r"^Task has been completed without payment", "CLOSED_WITHOUT_PAYMENT"),
    (r"^Task has been completed by supervisor", "CLOSED_BY_SUPERVISOR"),
    (r"^Resolved following instructions", "RESOLVED_NO_CONTRACTOR"),
    (r"^This task is closed, but we have received an email", "POST_CLOSE_EMAIL_REVIEW"),
    (r"^Paused automatically", "PAUSED_DEADLINE"),
    (r"NOT TENANTED", "PAUSED_NOT_TENANTED"),
    (r"^Manually updated|^Task manager was manually updated|^Task priority was manually updated", "MANUAL_EDIT"),
    (r"^done complete|^complete done", "CLOSED_FREE_TEXT"),
]


def label_update(body: str) -> str:
    b = norm(body)
    for rx, label in UPDATE_LABELS:
        if re.search(rx, b, re.I):
            return label
    return "OTHER_UPDATE:" + short(b, 60)


# What kind of external message is it (for decision points)
def classify_external(sender: str, body: str) -> str:
    b = norm(body).lower()
    s = sender.lower()
    if b.startswith("[") or "text/transcription" in b or "transcript absent" in b:
        return "placeholder_body"
    if "landlord" in s:
        if re.search(r"go ahead|yes please|please proceed|approve|that is fine|this is fine|please mend|please get|yes,? i'm happy|happy to|👍|ok to pay|^paid|please arrange|yes go|agrees|approves|yes that sounds", b):
            return "landlord_approval_or_payment"
        if re.search(r"update|status|inquir|resend|\?|arranged|has arranged|disappoint", b):
            return "landlord_query_or_pushback"
        return "landlord_other"
    if "tenant" in s:
        if re.search(r"still|not been resolved|not resolved|doesn't close|does not|has not worked|not working|no it's not", b):
            return "tenant_reports_unresolved"
        if re.search(r"thank|fixed|clear|working|resolved|sorted|managed to fix|will be fine|happy for", b):
            return "tenant_confirms_or_accepts"
        return "tenant_other"
    # contractor / maintenance provider / named firms
    if re.search(r"quote|estimate|£|gbp|cost|price|plus vat|\+ ?vat", b) and not re.search(r"invoice", b):
        return "contractor_quote"
    if re.search(r"invoice|complete|completed|done|finished|repaired|replaced|close (this )?job|no charge", b):
        return "contractor_completion_or_invoice"
    if re.search(r"book|appointment|schedule|arrange|visit|attend|call back|callback|voicemail|code|reach|minutes", b):
        return "contractor_scheduling"
    if re.search(r"attach|send|email|upload|contact information|mobile number", b):
        return "contractor_admin_request"
    return "contractor_other"


MONEY_RE = re.compile(r"£\s?\d[\d,]*(?:\.\d{1,2})?|\bGBP ?\d[\d,]*(?:\.\d{2})?|\b\d[\d,]*(?:\.\d{2})?\s?(?:GBP)\b")
ADDR_RE = re.compile(r"Flat \d+, \d+ [A-Z][a-z]+ [A-Z][a-z]+, [A-Z][a-z]+, ZZ\d \d?ZZ")
WEEKDAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
MONTHS = {m: i + 1 for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"])}
WD_DATE_RE = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\s+(?:the\s+)?(\d{1,2})(?:(?:st|nd|rd|th)(?:\s+(?:of\s+)?(January|February|March|April|May|June|July|August|September|October|November|December))?|\s+(January|February|March|April|May|June|July|August|September|October|November|December)|(?=/\d{2}\b))", re.I)
WD_DATE_RE2 = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),?\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?", re.I)
YEAR_DATE_RES = [
    re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b"),
    re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{2})\b"),
    re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b"),
    re.compile(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(January|February|March|April|May|June|July|August|September|October|November|December),?\s+(\d{4})\b", re.I),
    re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b", re.I),
    re.compile(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b", re.I),
]


def years_in(body: str) -> list[tuple[str, int]]:
    out = []
    for rx in YEAR_DATE_RES:
        for m in rx.finditer(body):
            g = m.groups()
            y = None
            for part in g:
                if part and part.isdigit() and len(part) == 4:
                    y = int(part)
            if y is None:
                yy = [p for p in g if p and p.isdigit() and len(p) == 2]
                if rx.pattern.startswith(r"\b(\d{1,2})/(\d{1,2})/(\d{2})") and yy:
                    y = 2000 + int(yy[-1])
            if y:
                out.append((m.group(0), y))
    return out


SYSTEM_NOTE_RX = re.compile(r"^(Request description:|\*?\*?\[?AI Intake|Added document|Skipped uploading|\[Text|\[No text|Text/transcription|Changed original task description|Note on invoice|Request summary with context)", re.I)

# Hand-verified quirks for cases read in full (event numbers checked against history.md).
MANUAL_QUIRKS: dict[int, list[str]] = {
    1: [
        "Landlord uses his own contractor; agency only chases. 'Landlord approval confirmed' (ev034) and 'Maintenance provider assigned' (ev035) are logged after the job already started (ev033) — stage bookkeeping lags reality.",
        "ev009 'Bit of a duplicate here' — a second ticket (flat 44) covers the same communal works; ev023 says only flats 26 and 44 reported it.",
        "Hold reason 'Waiting for Landlord' repeated 6 times (ev008–ev024) over 4 weeks before any decision; pigeon nesting delays the tree work (ev037).",
        "Closed 'without payment' (ev044) because the landlord pays the contractor directly (ev043).",
    ],
    2: [
        "Case opens with 'Landlord approval confirmed' (ev002) based on a phone call recorded only as a staff note (ev003) — no written landlord approval.",
        "Landlord's reply to the quote is 'Please approve this quote for works' (ev019) — reads as the landlord asking the agency to approve; treated as approval (ev021).",
        "Three contractor identities in one job: Riverside Works (ev005), 'Willow Utilities' (ev026 call), Ava Fletcher (ev034).",
        "Closed at ev040 but 'keeps coming into the dashboard' (Slack note ev044) → hold 'Other: system issues' (ev045) → 'Task has been completed by supervisor' (ev049). Auto-pause ev043 fired 2 days after closure.",
        "Tenant call ev031 mentions 'communication from another party' about the appointment — unexplained.",
    ],
    3: [
        "Invoice email says 'invoice from Cedar Solutions' (ev020) but the PDF is branded Keystone Maintenance with payee Bennett Ingram — three names for one contractor.",
        "Checkout report PDF appointment date is 16 March 2026 for a case that ran 22–24 July 2025.",
        "Duplicate hold ev011/ev012 one second apart; 'Validation: (Priority cannot be decreased to 5. Current priority is 6.)' appended to review prompts (ev006, ev013, ev016).",
        "Landlord's 'Paid' (ev023) arrives 2025-09-05, six weeks after closure (ev022) — post-close event.",
    ],
    8: [
        "Cross-property contamination: ev021 asks about quotes for Flat 5, 115 Juniper Mews and Flat 1, 101 Meadow Row; ev023 landlord discusses roof works at Flat 18, 8 Alder Lane and a quote for Flat 3, 43 Willowmere Road; ev027 chases payment for a previous job; ev028/ev045 refer to Flat 13, 83 Harbour View — all in a ticket for Flat 5, 55 Lantern Quay.",
        "VAT confusion: ev024/ev028 compare £1,370.00 vs £1,700.00+VAT; ev033/ev034 clarify Eliza Bennett doesn't charge VAT; ev036 restates.",
        "ev039 staff note: contractor asked whether willing to proceed because the landlord 'took a long time to pay' on the previous job — payment-risk judgement call.",
        "Estimate (£1,370) includes tap replacement; invoice is £1,190 because the tap did not need replacing (ev045) — invoice < estimate, scope changed.",
        "Attachment PDFs dated 5 January 2026 (reports) and 09/03/2026 (invoice) for a case that ran April–June 2025.",
        "'Property is NOT TENANTED — moved to Paused' (ev012) on a check-out job where that is expected; 13 free-text holds without a structured reason (ev005–ev032).",
    ],
    12: [
        "Request description cites an 'email dated 16th Sept 2025' — seven months before the case (2026-04-15); staff note ev004 explains the tenant replied to an unrelated sink email.",
        "Self-help checklist email sent twice (ev005/ev006, 8 seconds apart).",
        "Four provider names in one job: Riverside Compliance (ev014/015), Cedar Utilities (ev016 call), 'Harbour Homes' (SMS ev020), Meadow Services (ev021 call).",
        "'Keys return confirmed' (ev030) logged on a tenanted appliance repair — closing checklist noise; 'No work results' fired twice at the same second (ev022/ev023).",
        "Hold comments are personal workload notes ('so i can see what else is in my to do list', ev003; 'See notes……', ev009).",
    ],
    20: [
        "No 'Request description' event; inspection-specific workflow (Visit time approved → Rescheduled → Please add results → Inspection document uploaded).",
        "Tenant's reschedule request (ev006) handled via a staff note instructing someone else (ev007) — the note is an internal task, not a message.",
        "After closure the landlord raises an unapproved dog flap and a spare key after a lock change (ev020) — two new matters inside a closed inspection ticket.",
    ],
    25: [
        "Warranty status flips: landlord says under warranty (ev006); contractor says no longer under warranty (ev020, ev022); agency tells landlord '12 month warranty' expired (ev025); later a 2-year manufacturer warranty applies (ev042); repaired at no charge (ev062).",
        "Date drift: 'Harbour Services replaced the oven in March 2025' (ev014) inside a May-2024 case; 'Visit date selected - 22/05/2024' logged on 05-24 (ev027); 'Confirmed Time Slot: tomorrow, 21st June (21/06/2024)' sent on 24 May (ev028/ev029).",
        "Appointment conflict: ev053 'Friday, June 21st' vs ev054 'Thursday, June 25th' (25 June 2024 is a Tuesday) vs hold comment 'between 25/3' (ev056).",
        "'Pets:' field carries the fault description (ev028). Tenant named Leo Bennett in emails but Oliver Ashford in calls (ev053, ev058).",
        "Nine consecutive holds 'Waiting for Provider' with the same comment (ev021–ev040); ev039 call notes a month without an oven — an urgency signal never escalated.",
    ],
    27: [
        "No 'Request description' event; opens with 'Please approve selection of provider and category'.",
        "Tenant-responsibility template (ev002) with a 24-hour close ultimatum (ev004); tenant clears it with a plunger (ev007) → 'Resolved following instructions. No contractor required.' (ev009).",
        "After closure the tenant asks about garage parking (ev011); the agency answers inside the closed ticket (ev012) and raises duplicate holds 'Northbridge Lettings to close' (ev013/ev014).",
    ],
    32: [
        "'Visit date selected - 11/10/2026 04:15 pm' (ev013) logged on 2026-10-12, i.e. in the past, before the quote had even been approved; the slot is emailed to tenant and contractor (ev014/ev015).",
        "Call ev032 schedules 'May 1st' at Flat 29, 129 Lantern Quay, Northbridge — a different property and an impossible date for an October case; the hold comment copies it ('visit schedule may 1st', ev033).",
        "Landlord approval of a £172.51 + VAT quote is a thumbs-up emoji (ev024).",
        "Three identical holds 'Waiting for Landlord' (ev019, ev020, ev022); invoice attachment unavailable (ev035); closed by supervisor (ev036).",
    ],
    36: [
        "Outbound SMS self-identify as 'Isaac Kendall' instead of the agency (ev010, ev013, ev017, ev020, ev022, ev033, ev047).",
        "Contractor reveals the tap he fitted 'back in February' was faulty (ev025, ev050) → no charge; the landlord separately says the taps are under guarantee (ev043).",
        "Date conflict: agency tells landlord the fit is on 03/11/26 (ev041) while the contractor booked Wednesday 4 November (ev038/ev039). 'Bank holiday Wednesday' (ev028) is not a UK pattern.",
        "Hold reason 'Waiting for Landlord' (ev035) while actually chasing the provider; staff note ev031 is signed 'Freya Quinn Property Manager' though the handler is Leo Bennett.",
        "Landlord complains about missing photos and the delay (ev043) — escalation handled by a second staff member (hold ev046 by Imogen Mercer).",
    ],
    38: [
        "Three addresses in a 13-event case: case property vs 'Flat 18, 128 Meadow Row, Cedarford' (call ev004) vs 'Flat 9, 59 Alder Lane, Eastmere' (emails ev005/ev006).",
        "Call ev010 is labelled From: Tenant → Not specified but the transcript is the agent ('Eliza at Riverside Solutions') calling the tenant — direction/role inverted.",
        "Removal cost quoted as 'normally around £24.37-30' (ev005) — a pseudonymised number; tenant's pronouns alternate (her/he).",
        "Tenant-liability arrangement (tenant's own machine, takes it on leaving) recorded only in notes (ev011/ev012); no written confirmation to the tenant or landlord.",
    ],
    42: [
        "AI intake misclassifies a washing machine as 'Heating & Hot Water' and asks boiler questions (ev002); tenant answers 'It's the washing machine'.",
        "'Visit date selected - 23/02/2024 03:25 pm' (ev017) logged at 23:20 the same day — a slot already in the past; calls ev015/ev016 had agreed 'Tuesday at 1pm'.",
        "Invoice from Lantern Services for GBP 75.11 'due by July 22, 2026' (ev024) in a February-2024 case; the agency tells the landlord £75 + VAT (ev025).",
        "Hold 'waiting on contractors invoice' (ev021) precedes the contractor's call still trying to schedule the visit (ev022). 'Pets: multiple tenants in this property' (ev018) — field misuse.",
        "Tenant reply ev014 'Thank you for following up. I'll keep an eye on it' does not match any question asked.",
    ],
    50: [
        "Contractor quote is conditional ('either the handle or the lock', ev018); landlord approves both prices (ev021); agency tells contractor 'go ahead with whatever needed' (ev023) — open-ended authorisation.",
        "ev024 sends the contractor a different tenant name and phone (Eliza Langley, 07700 900931) from the one on the job (Harriet Turner, 07700 900009).",
        "Contractor invoice email asks for prompt payment and a review on social media (ev032); the invoice itself is unavailable; PDF re-requested (ev033/ev035).",
        "Closing note 'Landlord was given a quote of £49.40 incl VAT' (ev037) contradicts the £35 + VAT / £90 + VAT quotes (ev019).",
        "Provider named Stonebridge Works in templates (ev013–ev016) but Cedar Solutions in the invoice email (ev032).",
    ],
}


# Quirks verified against the script's compact timelines (one line per event) for cases not read in full.
TIMELINE_QUIRKS: dict[int, list[str]] = {
    4: [
        "'Property is NOT TENANTED — moved to Paused' (ev004) fires on a check-out clean, where an empty property is expected; staff carry on regardless.",
        "Quote approved by landlord (ev012) but the clean is deferred until another job (check-out works) finishes (ev013, ev019–ev023) — a dependency on a job outside this ticket.",
        "Checkout report PDF appointment date 23 June 2026 for a case that ran Oct–Nov 2025; the quote (£90) and invoice (£90) agree.",
    ],
    5: [
        "ev011 'the quote for Flat 27, 117 Lantern Quay hasnt attached' — contractor and agency are juggling another job in the same thread.",
        "ev020 contractor: 'Shouldn't it say quote approved on Northbridge Lettings? It looks like its waiting for me to send quote still?' — portal state lags the email thread.",
        "Invoice ping-pong ev026–ev033: the contractor cannot reply to the system address and asks to be emailed directly.",
        "Seven hold comments are placeholders ('[Text/transcription unavailable…]'); two quote PDFs with the same content; PDFs dated Feb/Mar 2025 for a Nov–Dec 2024 case; the quote has no stated total (calculated £205).",
    ],
    6: [
        "Tenant template email (ev004) sent on a check-out job where the tenant has vacated.",
        "Quote itemised only in email (£220 + £240 + £100 + £45, ev013/ev016); no attachment; contractor invoices the landlord directly (ev023).",
        "Hold ev018 says the contractor is attending 'Flat 12, 122 Juniper Mews, Westmarsh' — not this property (Flat 21, 11 Juniper Mews, Northbridge).",
    ],
    7: [
        "Quote £198.37 + VAT (ev008/ev009) but the invoice PDF is £200 + 20% VAT = £240.00 — invoice does not match the quote; supplier on the PDF is 'Willow Homes' while the contractor is addressed as Clarke.",
        "'NOT TENANTED — moved to Paused' (ev015) after the quote was approved; keys are with the caretaker (ev025).",
        "Checkout report PDF appointment date 25 August 2026 for a case that ran Sept–Oct 2025.",
    ],
    9: [
        "No 'Request description' event — the history starts with an email to the tenant; this is the tenant's own garden obligation picked up at an inspection.",
        "Emails ev011/ev016/ev017 ask about 'the garden at Flat 2, 72 Lantern Quay' — the case property is Flat 4, 174 Beacon Close; the same email is sent twice (ev003/ev004, ev016/ev017).",
        "Closed by free-text update 'complete done.Isaac' (ev023); the tenant's reply never arrives by email (ev019–ev021).",
    ],
    10: [
        "A recurring obligation (quarterly solar readings for the landlord) tracked as a ticket; holds say 'waiting for june' while the events run Nov 2024–Jan 2025 and the 'mid June' reading is sent in January (ev013).",
        "Closed by free-text 'done complete' (ev014); the landlord's reply after closure sets the next due date, 15th September (ev015) — needs a new reminder, not this ticket.",
    ],
    11: [
        "'No landlord/tenant response after 3 days' (ev006) is answered by simply restarting the timer (ev007).",
        "Contractor identity varies: Oakfield Homes (templates), Cedar Maintenance / Alder Maintenance (calls ev014/ev015); the contractor's report is pasted into a note as a forwarded email 'From: Oakfield Homes To: Juniper Surveying' (ev019).",
        "£95 quote for a replacement dial (ev019/ev020) approved by the landlord (ev022); the tenant will fit the knob themselves (ev025); invoice unavailable (ev030).",
    ],
    13: [
        "No 'Request description' event; three 'calls' are voicemail prompts (ev008–ev010); contractor emails have placeholder bodies (ev011, ev017) so '3+ reminders' fires (ev016) although the contractor had replied.",
        "ev028 tells the landlord the £162.85 invoice will 'come from the rent'; a stray call 24 days after closure (ev035) reaches the wrong person.",
    ],
    14: [
        "Landlord's email (ev009/ev010) gives a workaround (open the latch with the key) and defers the contractor to next month; the tenant is phoned (ev011) and the ticket closes the same day without payment.",
        "ev005 confirms a new fridge freezer was fitted (a different job) inside this thread.",
    ],
    15: [
        "ev003 'I hope you had a great Valentines weekend!' sent on 5 January; ev016 tells the landlord 'the door got sorted for Flat 10, 110 Meadow Row, Cedarford' — not this property.",
        "Invoice £68.97 from 'Keystone Homes' due 06/02/2025 (ev015) while the provider is 'Alder Homes'; closed by supervisor (ev018); 'Added document' note duplicated (ev017/ev019).",
    ],
    16: [
        "Landlord's reply went to spam: 'No landlord/tenant response after 3 days' (ev005) → the same email re-sent (ev006) → approval (ev009).",
        "Contractor says no invoice is required because the door settled (ev022) but the agency tells the landlord 'the invoice was needed for this one' (ev024) — contradiction (likely a typo for 'wasn't'). SMS self-identifies as 'Cedar Homes' (ev020).",
    ],
    17: [
        "Resolved by the landlord's one-line instruction (switch by the hob, ev008) relayed to the tenant (ev009); no contractor.",
        "The tenant's 'Thank you!' (ev007) triggers 'Message received from landlord/tenant. Please review and proceed manually.' (ev006) — a non-actionable reply treated as a decision point.",
    ],
    18: [
        "'Landlord approval confirmed' (ev005) one minute after emailing the tenant, with no landlord message in the history.",
        "Three reminders + '3+ reminders' (ev009–ev012) with no contractor reply ever; then 'garden maintenance has been done… invoiced off the rent' (ev013) — the work appears without any contractor event; invoice unavailable; closed by supervisor (ev017).",
    ],
    19: [
        "88 days. 'No landlord/tenant response after 3 days' (ev006) then silence until a new property manager takes over (ev008, 11 days later).",
        "Quote £500 + VAT 'approved' per note ev009, later 'around £600' (ev019); hold 'Contact landlord and get funds up front for invoices' (ev010) — payment-risk judgement.",
        "'Landlord approval confirmed' (ev032) and 'Maintenance provider assigned' (ev034) are logged after the work was done (ev031) because the new provider had no portal access (ev033); invoice deducted from rent (ev038).",
    ],
    21: [
        "Contractor asks for the tenant's contact details (ev015) although the job email (ev012) contained them; the reminder (ev018) goes out the same day the job completes (ev020).",
        "Landlord asks for four keys (tenant, landlord, agency) (ev006); 'Keys return confirmed' (ev028) is meaningful here — remaining keys dropped at the office.",
    ],
    22: [
        "No landlord step: provider assigned within two hours because the contractor is already nearby (ev004/ev005); the visit (2024-11-17 14:30) is logged at 15:59 the same day — already in the past (ev006).",
        "Call ev013 reports work at 'Flat 22, 42 Harbour View' and keys for 'Flat 18, 68 Harbour View' — other properties; the contractor's 'appointment confirmation' email (ev018) arrives after the work was done; the new key is added to the office set (ev020).",
    ],
    23: [
        "Request description 'Key lock not working' vs title 'Balcony Door Lock Repair' (re-described at ev007); the tenant-reminder SMS template is sent to the landlord (ev004); duplicate SMS to the tenant (ev014/ev015).",
        "Sender field is the company name 'Juniper Surveying' (ev020), not 'Contractor'; the job was done before the holds asking whether the tenants had called back were resolved (ev016/ev019 vs ev020).",
    ],
    24: [
        "Tenant first told 'perhaps on the wrong setting' with a manual (ev003); tenant insists it never worked (ev006).",
        "Tenant asks about a fence (ev015, unrelated); 20-day gap; then 'the fence and oven have both been fixed' (ev016) — no contractor visit or report appears in the history.",
        "'Keys return confirmed' logged three times (ev023, ev025, ev027) with 'Manually updated via synthetic-…' placeholders (ev026/ev028); 'Invoice sections not in use right now for HC' (ev020/ev029).",
        "After closure the tenant asks about a leaking conservatory roof (ev032) — a new issue in a closed ticket.",
    ],
    26: [
        "Hold 'Waiting for Provider' (ev005) before any provider is assigned; provider named Keystone Compliance (templates), Riverside Works (call ev016), 'Lantern Utilities' (SMS ev020), Keystone Utilities / Harbour Works (tenant, ev021/ev025).",
        "Appointment conflict: system 30/08/2025 10:00 (ev017–ev020) vs tenant's '8 September' (ev021, ev025, ev028); the agency defers: 'if Keystone Compliance have confirmed a date with you - please take that as the date' (ev023).",
        "The agency phones the tenant to verify the oven works before closing (ev029); 'Skipped uploading… approved by landlord in activity notes' (ev034).",
    ],
    28: [
        "Landlord's own contractor ('We will sort this issue', ev007); a forwarded email pasted as a note (ev009) carries the header 'Thursday, 18 June 2025' (a Wednesday) and 'Flat 7, 177 Alder Lane, Northbridge' (property is Flat 7, 87 Alder Lane, Bellmere).",
        "Landlord confirms 'All completed on 19/06/25' (ev012) only after a chase two weeks later (ev010).",
    ],
    29: [
        "No landlord step; 'Our maintenance provider Henry Quinn' is a person; the agency asks how the basin cracked (ev007) — liability probe — and the tenant says it was cracked at move-in (ev010): check-in inventory needed, never consulted.",
        "Hold ev012 refers to another job ('shared Beacon Utilities'); closure rests on a verbal 'job done' note (ev014) with no document; 'Keys return confirmed' six days later (ev021).",
    ],
    30: [
        "'Landlord approval confirmed' (ev005) before the landlord's reply, which is only 'Thanks Ava 👍' (ev010).",
        "Provider named Willow Services in templates but the job email goes to 'Riverside Works' (ev008); calls come from 'Keystone Solutions' / 'Beacon Works' (ev018, ev021).",
        "3 reminders → '3+ reminders' (ev015) → manual chase (ev016) → 'Resumed auto waiting for provider visit date (5 days)' (ev017).",
        "'Monday 20th' (ev020–ev026) — 20 October 2024 was a Sunday; the 'rescheduled' template (ev031/ev032) is sent for an unchanged slot; provider missed the confirmed date (ev037); LL pays contractor directly (ev040); a stray call 22 days after closure (ev042).",
    ],
    31: [
        "Tenant's request mentions a water-leakage letter from 'Oakfield Services' two weeks earlier — never followed up; 'Landlord approval confirmed' (ev003) with no landlord contact in the history.",
        "Provider Meadow Solutions (templates) vs 'Harbour Services' (call ev010) vs SMS from 'Keystone Solutions' (ev014); contractor email placeholder (ev016) → 'expected data could not be extracted' (ev015).",
        "Contractor chases closure twice (ev021, ev022) over 11 days before the agency closes (ev023).",
    ],
    33: [
        "'Please approve selection of provider and category' (ev002) yet the landlord is asked first (ev003); duplicate holds ev005/ev006.",
        "Contractor piggybacks on a gas-safety visit 'scheduled for today' (ev013) → visit logged as 2026-10-03 00:00, the day before (ev014).",
        "Completion email (ev037) names 'Flat 21, 161 Meadow Row, Cedarford' — not this property (Flat 19, 159 Juniper Mews) — and is accepted as the work result (ev038).",
    ],
    34: [
        "Request says 'Just to add to prev request' — a second ticket for the same shower; 'Landlord approval confirmed' (ev004) with no landlord message.",
        "Agency's email to the landlord (ev011) says the contractor 'attended to an issue with the shower at Flat 17, 77 Harbour View, Northbridge' — wrong property (case is Flat 9, 9 Willowmere Road); landlord 'Paid today' two weeks after closure (ev017).",
    ],
    35: [
        "Same-day resolution: the agency phones the landlord (ev004), sends the photo (ev005), and the landlord fixes it himself; closure rests on a phone confirmation note (ev011/ev012). No contractor.",
    ],
    37: [
        "'Please approve selection…' (ev002) then the landlord is asked anyway (ev003) with a free-text hold 'LL to approve contractor' (ev005).",
        "Visit 2024-04-04 12:00 logged at 16:32 the same day (ev018, in the past); the agency's FYI to the landlord (ev023) names 'Flat 8, 68 Willowmere Road, Bellmere' — wrong property (case is Flat 14, 44 Lantern Quay); attachment unavailable (ev024); closed by supervisor (ev025).",
    ],
    39: [
        "Agency asks the tenant to check nothing is stuck before sending someone (ev003, liability triage); hold 'Waiting for Landlord' (ev008) but no landlord message appears — 'I have asked the landlord' (ev007).",
        "Appointment confusion: call ev015 'Sunday between twelve and two' at 'Flat 20, 130 Harbour View, Bellmere' (wrong property); contractor email 'Monday 12 till 2' (ev017); system logs 13/09/2025 (a Saturday) (ev018); SMS self-identifies as 'Keystone Homes' (ev021).",
        "125 days after closure the tenant 'confirms receipt of an email about the setup of a Direct Debit with Meadow Maintenance' (ev029) — unrelated and phishing-like.",
    ],
    40: [
        "Tenant fixes it himself by swapping machines (ev008) at the same time the landlord approves a visit (ev009); closed 'no further action' (ev011/ev012) the same day.",
        "Landlord asks four days after closure whether any action is needed (ev013) — nobody told the landlord the ticket was closed.",
    ],
    41: [
        "Hold 'Held awaiting response from contractor' (ev004) when the wait is for the landlord; landlord uses his own contractor; landlord emails are pasted as notes (ev011, ev017, ev021, ev023) rather than logged as events.",
        "Tenant tried the drain-pump advice twice without success (ev014); 'Tuesday 02/10' (ev019) — 2 October 2024 was a Wednesday; closed without payment once the landlord says it is fixed (ev023–ev025).",
    ],
    43: [
        "Landlord silent for five days → a different staff member ('Jenkins, filling in for Theo') texts the landlord from 'Lantern Maintenance' (ev006).",
        "Provider assigned (ev008) and job sent (ev010/ev011) before the landlord's approval arrives (ev013); contractor 'completed the repair on November 4th' (ev016) in an April case; landlord addressed as 'Ava' (ev003) then 'Miles Kendall' (ev017).",
    ],
    44: [
        "27 days before the first email to the landlord (ev009): holds 'Will email LL' (ev003) and 'Waiting to hear from LL' (ev004) with no email sent; the tenant is asked which window (ev005/ev007).",
        "Contractor completes (ev019) while reminders continue; '3+ reminders… Please check what's happening' fires the day after completion (ev020); invoice unavailable.",
    ],
    45: [
        "The Property field (Flat 26, 116 Copperfield Walk, Alderwick) differs from the address in every email until ev032 (Flat 12, 182 Meadow Row, Kingshaven); further addresses in ev020, ev023, ev038.",
        "Agency first asks the tenant 'Was this requested by your landlord?' (ev003) — 'no' (ev006); the landlord then arranges his own window company; 11 holds across 10 weeks.",
        "'Visitng on Tuesday 6th June' (ev031, in March; 6 June 2025 is a Friday) then 'How was the visit on Monday?' (ev032); closed on 'Good, all done!' (ev034); after closure the landlord asks about appointments at 'Flat 5, 25 Harbour View' (ev038).",
    ],
    46: [
        "Contractor proposes extra work mid-job ('Our hinges are £90 plus VAT, can we please do while there', ev015) → agency seeks landlord approval (ev016) → approved (ev018) → 'go ahead' (ev020): the correct upsell handling.",
        "Contractor asks for the tenant's number (ev024) although the template included it; 'expected data could not be extracted' fires on a smiley reply (ev032/ev033); invoice requested 'in PDF… as the other formats' (ev038); invoice attachment unavailable (ev043).",
    ],
    47: [
        "Tenant's reply mentions 'My mother managed to fix the toilet' (ev006) — a second issue; the landlord replies about a plumber at 'Flat 18, 88 Alder Lane, Willowbank' (ev010) — wrong property and wrong issue.",
        "Provider is a person (Oscar Turner); 3 reminders + '3+ reminders' (ev020–ev026); eight holds 'Held awaiting update from Dawson' over three months with reasons alternating Provider/Landlord (ev027–ev034); closed on 'Landlord's contractor confirmed job complete' (ev035) after 111 days.",
    ],
    48: [
        "Contractor's completion emails (ev016/ev017) are for 'Flat 7, 177 Beacon Close, Kingshaven' — not this property (Flat 20, 120 Lantern Quay); the agency then logs a past visit date (ev018) and sends appointment confirmations (ev019/ev020) after the 'completion'.",
        "'Quote was approved by landlord' (ev026) although no quote was ever sent to the landlord; 'Added document(s): quote (contents unavailable)' (ev024); 'Hi yes thats fine Ruben' (ev022) to the contractor with no stated question.",
    ],
    49: [
        "Landlord approves the tenant fixing the door themselves or a contractor (ev007); 'Landlord approval confirmed. Proceed to provider selection.' (ev009) although no provider is needed; closed when the tenants fix it (ev013) after a 'if no reply will close off the job' hold (ev012).",
    ],
}


def extract_case(case_dir: Path) -> dict:
    n = int(case_dir.name)
    idx = parse_index((case_dir / "index.md").read_text(encoding="utf-8"))
    events = parse_history((case_dir / "history.md").read_text(encoding="utf-8"))
    att_dir = case_dir / "attachments"
    files = sorted(p.name for p in att_dir.iterdir()) if att_dir.exists() else []
    d = idx.details
    created = parse_ts(d.get("created", ""))
    completed = parse_ts(d.get("completed", "")) if d.get("completed") else None
    prop = d.get("property", "")
    ctype, sub = classify(idx.title, idx.initial_request)

    channels = Counter(e.channel for e in events)
    parties = Counter(e.sender for e in events)

    # ---- decision points
    decision_points = []
    for i, e in enumerate(events):
        if is_agency(e.sender):
            continue
        nxt = next((x for x in events[i + 1 :] if is_agency(x.sender)), None)
        decision_points.append(
            {
                "event": e.number,
                "trigger": f"{e.sender} {e.channel}→{e.recipient}: {short(e.body, 110)}",
                "why": classify_external(e.sender, e.body),
                "next_event": nxt.number if nxt else None,
                "agency_response": (f"{nxt.channel}→{nxt.recipient}: {short(nxt.body, 110)}" if nxt else "none (end of history)"),
            }
        )
    # hold reason changes
    last_reason = None
    for e in events:
        if e.channel != "Hold":
            continue
        m = HOLD_RE.search(norm(e.body))
        reason = m.group("reason").strip() if m else "free-text"
        if last_reason is not None and reason != last_reason:
            decision_points.append({"event": e.number, "trigger": f"Hold: {short(e.body, 110)}", "why": f"hold_reason_changed: {last_reason} → {reason}", "next_event": None, "agency_response": ""})
        last_reason = reason
    decision_points.sort(key=lambda x: x["event"])

    # ---- human interventions
    interventions = []
    for e in events:
        b = norm(e.body)
        if e.channel == "Hold":
            m = HOLD_RE.search(b)
            if m:
                who = (m.group("who") or "unnamed").strip()
                what = f"hold: {m.group('reason').strip()}" + (f" — {short(m.group('comment') or '', 100)}" if m.group("comment") else "")
                interventions.append({"event": e.number, "kind": "hold", "who": who, "what": what})
            else:
                interventions.append({"event": e.number, "kind": "hold_free_text", "who": "unnamed", "what": f"hold: {short(b, 100)}"})
        elif e.channel == "Update":
            lab = label_update(b)
            if lab in ("CHECK_REPLY_LANDLORD", "CHECK_REPLY_PROVIDER", "CHECK_REPLY_TENANT", "LL_TENANT_REPLY_REVIEW", "NO_LL_TENANT_REPLY_REVIEW", "NO_WORK_RESULTS_REVIEW", "PROVIDER_REMINDERS_EXHAUSTED", "PROVIDER_EMAIL_UNPARSED", "WORK_RESULTS_SELECT_STAGE", "ADD_INSPECTION_RESULTS", "POST_CLOSE_EMAIL_REVIEW", "CHECK_KEY_RETURN"):
                interventions.append({"event": e.number, "kind": "review_prompt", "who": "system→staff", "what": lab})
            elif lab in ("ASK_LANDLORD_APPROVAL", "SELECT_PROVIDER_AND_CATEGORY", "NEED_LANDLORD_CONFIRMATION"):
                interventions.append({"event": e.number, "kind": "approval_prompt", "who": "system→staff", "what": lab})
            elif lab in ("LANDLORD_APPROVED", "QUOTE_APPROVED"):
                interventions.append({"event": e.number, "kind": "approval_recorded", "who": "staff (on landlord's behalf)", "what": lab})
            elif lab in ("MANUAL_EDIT",):
                interventions.append({"event": e.number, "kind": "manual_edit", "who": "staff", "what": short(b, 80)})
            elif lab in ("CLOSED_BY_SUPERVISOR",):
                interventions.append({"event": e.number, "kind": "supervisor_close", "who": "supervisor", "what": lab})
            elif lab in ("PAUSED_NOT_TENANTED", "PAUSED_DEADLINE"):
                interventions.append({"event": e.number, "kind": "auto_pause_needs_human", "who": "system→staff", "what": lab})
            elif lab in ("KEYS_RETURN_CONFIRMED",):
                interventions.append({"event": e.number, "kind": "manual_check", "who": "staff", "what": lab})
            elif lab in ("CLOSED_FREE_TEXT",):
                interventions.append({"event": e.number, "kind": "manual_close", "who": "staff", "what": short(b, 80)})
        elif e.channel == "Note" and is_agency(e.sender):
            if re.match(r"^Estimate approved", b):
                interventions.append({"event": e.number, "kind": "approval_recorded", "who": "staff", "what": "Estimate approved"})
            elif not SYSTEM_NOTE_RX.match(b):
                interventions.append({"event": e.number, "kind": "staff_note", "who": "staff", "what": short(b, 110)})
        elif e.channel == "Call" and is_agency(e.sender):
            interventions.append({"event": e.number, "kind": "staff_call", "who": "staff", "what": f"call→{e.recipient}: {short(b, 100)}"})
        elif not is_agency(e.sender) and "landlord" in e.sender.lower():
            if classify_external(e.sender, b) == "landlord_approval_or_payment":
                interventions.append({"event": e.number, "kind": "landlord_approval", "who": "Landlord", "what": short(b, 100)})

    # ---- money
    money = []
    for e in events:
        for m in MONEY_RE.finditer(e.body):
            raw = m.group(0)
            amt = float(re.sub(r"[^\d.]", "", raw)) if re.search(r"\d", raw) else None
            s = max(0, m.start() - 60)
            t = min(len(e.body), m.end() + 60)
            money.append({"event": e.number, "amount_gbp": amt, "raw": raw, "context": f"{e.sender}→{e.recipient}: …{short(e.body[s:t], 130)}…"})

    # ---- update sequence (state trace)
    update_sequence = [f"{e.number:03d}:{label_update(e.body)}" for e in events if e.channel == "Update"]
    closure = next((label_update(e.body) for e in reversed(events) if e.channel == "Update" and label_update(e.body).startswith(("CLOSED", "RESOLVED"))), "NONE")

    # ---- holds
    hold_reasons = Counter()
    holders = Counter()
    for e in events:
        if e.channel == "Hold":
            m = HOLD_RE.search(norm(e.body))
            if m:
                hold_reasons[m.group("reason").strip()] += 1
                holders[(m.group("who") or "unnamed").strip()] += 1
            else:
                hold_reasons["free-text"] += 1

    # ---- quirks (automatic)
    quirks = []
    seen = {}
    dups = []
    for e in events:
        key = (e.channel, e.sender, norm(e.body))
        if key in seen and len(key[2]) > 40 and e.channel != "Update":
            dups.append(f"ev{e.number:03d}=ev{seen[key]:03d}({e.channel})")
        seen.setdefault(key, e.number)
    if dups:
        quirks.append("Duplicate events (identical channel/sender/body): " + ", ".join(dups))
    unavail = [e.number for e in events if re.search(r"unavailable|contents not described|could not be read", e.body, re.I) and re.search(r"attach|invoice|photo|pdf|document|image|report|quote", e.body, re.I)]
    if unavail:
        quirks.append(f"Attachments referenced but unavailable in {len(unavail)} events: " + ", ".join(f"ev{x:03d}" for x in unavail))
    placeholders = [e.number for e in events if re.search(r"^\[?(Text|No text)/?transcript|Text/transcription|synthetic-[0-9a-f]{6,}|PDF contents unavailable|\[Attachment #\d+ — unavailable\]", norm(e.body))]
    if placeholders:
        quirks.append(f"Placeholder text in {len(placeholders)} events: " + ", ".join(f"ev{x:03d}" for x in placeholders))
    if not files and any(re.search(r"attach", e.body, re.I) for e in events):
        quirks.append("Messages refer to attachments/photos but the case has no attachment files")
    # other properties
    others = []
    for e in events:
        for a in ADDR_RE.findall(e.body):
            if a != prop:
                others.append((e.number, a))
    if others:
        quirks.append("Other property addresses mentioned: " + "; ".join(f"ev{n_:03d} {a}" for n_, a in others[:6]) + (f" (+{len(others)-6} more)" if len(others) > 6 else ""))
    # dates with a year outside the case window
    yrs = set()
    if completed:
        yrs = {created.year, completed.year}
    else:
        yrs = {created.year}
    odd_years = []
    last_year = max(yrs)
    for e in events:
        for txt, y in years_in(e.body):
            if y > last_year:
                odd_years.append(f"ev{e.number:03d} '{txt}'")
    if odd_years:
        quirks.append("Impossible future dates (case ran in " + "/".join(str(y) for y in sorted(yrs)) + "): " + ", ".join(dict.fromkeys(odd_years)))
    # weekday mismatch
    wd_bad = []
    for e in events:
        ets = parse_ts(e.timestamp)
        for m in WD_DATE_RE2.finditer(e.body):
            wd, mon, day = m.group(1).lower(), MONTHS[m.group(2).lower()], int(m.group(3))
            try:
                dt = datetime(ets.year, mon, day)
            except ValueError:
                continue
            if WEEKDAYS[dt.weekday()] != wd:
                wd_bad.append(f"ev{e.number:03d} '{m.group(0)}' is a {WEEKDAYS[dt.weekday()].title()} in {ets.year}")
        for m in WD_DATE_RE.finditer(e.body):
            wd, day = m.group(1).lower(), int(m.group(2))
            mon = MONTHS[m.group(3).lower()] if m.group(3) else None
            if mon is None:
                mon = ets.month if day >= ets.day else (ets.month % 12 + 1)
                y = ets.year if not (mon == 1 and ets.month == 12) else ets.year + 1
            else:
                y = ets.year
            try:
                dt = datetime(y, mon, day)
            except ValueError:
                continue
            if WEEKDAYS[dt.weekday()] != wd:
                wd_bad.append(f"ev{e.number:03d} '{m.group(0)}' is a {WEEKDAYS[dt.weekday()].title()} ({dt:%Y-%m-%d})")
    if wd_bad:
        quirks.append("Weekday/date mismatch: " + "; ".join(dict.fromkeys(wd_bad)))
    # visit date in the past relative to the logging event
    past_visits = []
    for e in events:
        if e.channel == "Update":
            vd = None
            m = re.search(r"Visit date (?:selected|confirmed/rescheduled) - (\d{2})/(\d{2})/(\d{4})(?: (\d{1,2}):(\d{2}) ?(am|pm)?)?", e.body)
            if m:
                hh = int(m.group(4) or 0)
                if m.group(6) == "pm" and hh < 12:
                    hh += 12
                vd = datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)), hh, int(m.group(5) or 0))
            m2 = re.search(r"Visit date confirmed/rescheduled - (\d{4})-(\d{2})-(\d{2})(?: (\d{2}):(\d{2}))?", e.body)
            if m2:
                vd = datetime(int(m2.group(1)), int(m2.group(2)), int(m2.group(3)), int(m2.group(4) or 0), int(m2.group(5) or 0))
            if vd is not None and vd < parse_ts(e.timestamp):
                past_visits.append(f"ev{e.number:03d} slot {vd:%Y-%m-%d %H:%M} logged {e.timestamp[:16]}")
    if past_visits:
        quirks.append("Visit slot logged after it had already passed: " + "; ".join(past_visits))
    # 'tomorrow' with a date not one day away
    tmr = []
    for e in events:
        if "tomorrow" in e.body.lower():
            m = re.search(r"\((\d{2})/(\d{2})/(\d{4})\)", e.body)
            if m:
                dd = datetime(int(m.group(3)), int(m.group(2)), int(m.group(1))).date()
                delta = (dd - parse_ts(e.timestamp).date()).days
                if delta != 1:
                    tmr.append(f"ev{e.number:03d} 'tomorrow' but slot is {dd} ({delta:+d} days)")
    if tmr:
        quirks.append("'Tomorrow' inconsistent with the slot date: " + "; ".join(tmr))
    # events after completion
    if completed:
        after = [e.number for e in events if parse_ts(e.timestamp) > completed + timedelta(minutes=1)]
        if after:
            quirks.append(f"{len(after)} event(s) after the Completed timestamp: " + ", ".join(f"ev{x:03d}" for x in after))
    # long gaps
    gaps = []
    for a, b in zip(events, events[1:], strict=False):
        g = (parse_ts(b.timestamp) - parse_ts(a.timestamp)).days
        if g >= 14:
            gaps.append(f"{g} days between ev{a.number:03d} and ev{b.number:03d}")
    if gaps:
        quirks.append("Long gaps: " + "; ".join(gaps))
    # provider / agency name variety
    names = set()
    for e in events:
        for m in re.finditer(r"Our maintenance provider \**([A-Z][A-Za-z]+ [A-Z][A-Za-z]+)\**", e.body):
            names.add(m.group(1))
        for m in re.finditer(r"^Dear ([A-Z][A-Za-z]+ (?:Services|Works|Solutions|Utilities|Compliance|Maintenance|Homes|Surveying)),", e.body, re.M):
            names.add(m.group(1))
        for m in re.finditer(r"Maintenance Provider Name: ([A-Z][A-Za-z]+ [A-Z][A-Za-z]+)", e.body):
            names.add(m.group(1))
    if len(names) > 1:
        quirks.append("Provider named inconsistently across templates: " + ", ".join(sorted(names)))
    selfnames = set(m.group(1) for e in events for m in re.finditer(r"Hello, this is ([A-Z][A-Za-z]+ [A-Z][A-Za-z]+)!", e.body))
    if selfnames - {"Northbridge Lettings"}:
        quirks.append("Outbound SMS self-identify as: " + ", ".join(sorted(selfnames)))
    # intake classification category
    intake = None
    for e in events:
        if "AI Intake" in e.body:
            m = re.search(r"Issue:\**\s*\n?\s*\**\s*([^\n*]+)", e.body)
            intake = norm(m.group(1)) if m else "?"
            break
    if any(abs((parse_ts(b.timestamp) - parse_ts(a.timestamp)).total_seconds()) < 0 for a, b in zip(events, events[1:], strict=False)):
        quirks.append("Timestamps out of order")
    quirks.extend(MANUAL_QUIRKS.get(n, []))
    quirks.extend(TIMELINE_QUIRKS.get(n, []))

    outcome = norm(idx.outcome)
    outcome_summary = re.split(r"(?<=[.!?])\s", outcome)[0] if outcome else ""

    return {
        "number": n,
        "title": re.sub(r"^Case \d{3}: ", "", idx.title),
        "source_role": d.get("source_role"),
        "status": d.get("status"),
        "created": d.get("created"),
        "completed": d.get("completed"),
        "duration_days": (completed - created).days if completed else None,
        "property": prop,
        "n_events": len(events),
        "channels": dict(channels),
        "parties": dict(parties),
        "n_attachments": len(files),
        "attachment_names": files,
        "case_type": ctype,
        "case_subtype": sub,
        "intake_classification": intake,
        "initial_request": short(idx.initial_request, 300),
        "first_external_event": next((e.number for e in events if not is_agency(e.sender)), None),
        "n_holds": channels.get("Hold", 0),
        "hold_reasons": dict(hold_reasons),
        "holders": dict(holders),
        "update_sequence": update_sequence,
        "closure": closure,
        "decision_points": decision_points,
        "human_interventions": interventions,
        "money": money,
        "outcome_summary": outcome_summary,
        "quirks": quirks,
        "review_depth": "full_history_read" if n in MANUAL_QUIRKS else "compact_timeline_reviewed",
    }


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="Extract a JSON index from Property Management case folders.")
    ap.add_argument("--cases", type=Path, default=DEFAULT_CASES, help="directory holding NNN/ case folders")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT, help="JSON index to write")
    ap.add_argument("--stats", type=Path, default=None, help="optional corpus aggregates JSON (for write-ups)")
    args = ap.parse_args(argv)
    if not args.cases.is_dir():
        raise SystemExit(f"cases directory not found: {args.cases}")
    cases = [extract_case(d) for d in sorted(args.cases.iterdir()) if d.is_dir() and re.fullmatch(r"\d{3}", d.name)]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(cases, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    # aggregates
    stats: dict = {}
    stats["n_cases"] = len(cases)
    stats["events"] = {"total": sum(c["n_events"] for c in cases), "min": min(c["n_events"] for c in cases), "max": max(c["n_events"] for c in cases), "median": sorted(c["n_events"] for c in cases)[len(cases) // 2], "dist": sorted(c["n_events"] for c in cases)}
    ch = Counter()
    for c in cases:
        ch.update(c["channels"])
    stats["channels"] = dict(ch.most_common())
    pa = Counter()
    for c in cases:
        pa.update(c["parties"])
    stats["parties"] = dict(pa.most_common())
    stats["source_roles"] = dict(Counter(c["source_role"] for c in cases))
    stats["taxonomy"] = {t: sorted(c["number"] for c in cases if c["case_type"] == t) for t in sorted(set(c["case_type"] for c in cases))}
    stats["subtypes"] = {t: sorted(c["number"] for c in cases if c["case_subtype"] == t) for t in sorted(set(c["case_subtype"] for c in cases))}
    stats["closure"] = {t: sorted(c["number"] for c in cases if c["closure"] == t) for t in sorted(set(c["closure"] for c in cases))}
    hr = Counter()
    hd = Counter()
    for c in cases:
        hr.update(c["hold_reasons"])
        hd.update(c["holders"])
    stats["hold_reasons"] = dict(hr.most_common())
    stats["holders"] = dict(hd.most_common())
    ik = Counter()
    iw = Counter()
    for c in cases:
        for i in c["human_interventions"]:
            ik[i["kind"]] += 1
            iw[i["what"] if i["kind"] in ("review_prompt", "approval_prompt", "approval_recorded", "auto_pause_needs_human", "manual_check", "supervisor_close") else (i["what"].split(" — ")[0] if i["kind"] == "hold" else i["kind"])] += 1
    stats["intervention_kinds"] = dict(ik.most_common())
    stats["intervention_reasons"] = dict(iw.most_common())
    dp = Counter()
    for c in cases:
        for p in c["decision_points"]:
            dp[p["why"].split(":")[0]] += 1
    stats["decision_point_kinds"] = dict(dp.most_common())
    stats["decision_points_per_case"] = {c["number"]: len(c["decision_points"]) for c in cases}
    ul = Counter()
    for c in cases:
        for u in c["update_sequence"]:
            ul[u.split(":", 1)[1]] += 1
    stats["update_labels"] = dict(ul.most_common())
    stats["attachments"] = {c["number"]: c["attachment_names"] for c in cases if c["n_attachments"]}
    stats["money_cases"] = {c["number"]: [m["raw"] for m in c["money"]] for c in cases if c["money"]}
    stats["durations"] = {c["number"]: c["duration_days"] for c in cases}
    stats["intake"] = {c["number"]: c["intake_classification"] for c in cases if c["intake_classification"]}
    stats["quirk_counts"] = {c["number"]: len(c["quirks"]) for c in cases}
    stats["entry_update"] = dict(Counter(c["update_sequence"][0].split(":", 1)[1] if c["update_sequence"] else "NONE" for c in cases))
    if args.stats:
        args.stats.parent.mkdir(parents=True, exist_ok=True)
        args.stats.write_text(json.dumps(stats, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {args.out} ({len(cases)} cases)" + (f" and {args.stats}" if args.stats else ""))
    print("taxonomy:", {k: len(v) for k, v in stats["taxonomy"].items()})
    print("closure:", {k: len(v) for k, v in stats["closure"].items()})
    print("intervention kinds:", stats["intervention_kinds"])
    print("top intervention reasons:", list(stats["intervention_reasons"].items())[:12])
    print("decision point kinds:", stats["decision_point_kinds"])


if __name__ == "__main__":
    main()
