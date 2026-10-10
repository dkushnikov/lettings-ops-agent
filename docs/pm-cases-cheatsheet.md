# PM cases cheat-sheet (50 Northbridge Lettings tickets)

Data: `data/pm-cases-index.json` · full analysis: `docs/pm-cases-analysis.md` · cite as `NNN/evMMM`.

**Shape.** 50 cases, 1,505 events, 13–64 per case (median 28), median 13 days. 85% of events are the agency's own (system + staff); Contractor 120, Landlord 65, Tenant 42. Channels: Email 34% · Update 29% · Hold 16% · Note 13% · Call 5% · SMS 4%. Only 7 cases have files (16 PDFs, all text summaries); 28 cases say "(unavailable)".

**Types.** appliance_repair 13 · plumbing 12 · window_door 10 · garden 4 · checkout_cleaning 3 · checkout_works 3 · access 3 · inspection 1 · other 1. Source: Tenant 40, Agency manager 9 (003–010), auto 1 (020).

## State machine (exact system phrases)

```
Request description → "Please complete landlord approval step first" (25) | "Please approve selection of provider and category" (15)
LANDLORD  email LL "…instruct a contractor to attend or … arrange your own contractor?"
          "Waiting for landlord/tenant response before provider selection (3 days)."
          "Message received from landlord/tenant. Please review and proceed manually." | "No landlord/tenant response after 3 days. Please review manually."
          "Please check if we need to provide a response to landlord. If not, please return this request to auto mode."
          → "Landlord approval confirmed. Proceed to provider selection."
DISPATCH  "Maintenance provider assigned" → tenant "Our maintenance provider X will be attending…" + provider "This is a new Y for the property at Z…
          If the job requires quotation, please reply… only proceed after receiving our approval." + SMS "Please check your email…"
          reminders (+1/+3/+5 d) "This is a friendly reminder that we are awaiting the confirmation that the appointment has been booked…"
          → "3+ reminders have been sent to provider. Please check what's happening."
          provider reply → "Please check if we need to provide a response to provider…" | "Email received from provider, but expected data could not be extracted. Please review manually."
SCHEDULE  "Visit date selected - DD/MM/YYYY HH:MM am" → "We are providing the confirmed appointment details for the **Y** at Z: Confirmed Time Slot: …"
          → SMS "Your Y appointment is scheduled for … To reschedule call …" → (+3 d) "No work results; we need to check what is happening"
QUOTE     email LL "Please find attached a quote… approve for me to raise an order" → "Quote was approved by landlord" / "Estimate approved"
          → provider "Landlord approved your quote… Please ensure a photo or video… along with the invoice" → "…updated to the start stage to arrange a visit."
CLOSE     "Work results isset, please select next stage" | "Task has been moved to Result" → "Request marked as completed, lets do the final checks"
          → "Added document(s)…" / "Skipped uploading one or more documents. Reason provided: …" → invoice to LL → "Need confirmation from landlord"
          → "We need to check the key return before completing the request" → "Keys return confirmed" → "All checks have been completed; the request is now closed" (25)
          | "Task has been completed without payment" (17) | "Task has been completed by supervisor" (5)
PAUSE     "Property is **NOT TENANTED** — moved to Paused" (4) · "Paused automatically: exceeded visit/move-out/hold deadline by N days" (1) · "Manually updated via Change Mode" (28; 35 manual edits in all)
```

**Holds.** `Put on hold by <staff>. Reason: Waiting for Landlord | Waiting for Provider | Waiting for Tenant | Other. Comment: …` — Provider 70, Landlord 49, Other 22, Tenant 8, plus 87 free-text holds. The Comment is the real state. Same comment repeated = stall (047 ×8, 025 ×9).

**Roles.** Tenant (TT/T) · Landlord (LL) · Contractor = Maintenance provider · `Agency / system` = automation · `Northbridge Lettings` = staff · supervisor. Resolve by From/To role, never by name (names are re-pseudonymised between events; firms change name mid-job; SMS self-identify as other firms).

**Why humans step in (635 events).** Holds 236 · "please check whether to reply" prompts 65 · approval-gate prompts 67 · landlord approval emails 40 · approvals recorded by staff 26 · timers 31 (no work results 16, 3+ reminders 6, no reply 4, pauses 5) · manual overrides 42 · parse failures 6 · key-return checks 25 · staff notes/calls 92 · other prompts 5.

**Traps.** Wrong-property messages (16 cases: 033/ev037, 048/ev016, 045 throughout) · invoices/payment asks for other work (008/ev027, 050/ev032, 042/ev024, 039/ev029) · tenant-liability framing (027/ev002, 012/ev005, 029/ev010, 038/ev012) · dates (025, 026, 030, 036, 045; visit dates logged in the past; PDFs dated after the case) · placeholders "[Text/transcription unavailable…]" (23 cases) · duplicates (27 cases) · "👍" or "Please approve this quote" taken as approval (030, 032, 002) · approval logged without a landlord message (002, 004, 007, 018, 030, 031, 034) · post-close new issues (020, 024, 027, 040).

## Look at these first

| # | Case | What it shows |
|---|---|---|
| 1 | 038 | 13 ev: tenant-owned replacement, liability, £24.37 removal, closed without payment |
| 2 | 027 | tenant-responsibility template → plunger → closed → unrelated parking question in a closed ticket |
| 3 | 003 | checkout clean with real PDFs: estimate → "Estimate approved" → invoice → "Paid" after close |
| 4 | 012 | self-help checklist (liability wording) → "still doesn't close" → engineer |
| 5 | 050 | full happy path + invoice email asking for prompt payment and a review (ev032); £49.40 note vs £35/£90 quotes |
| 6 | 025 | 64 ev: warranty flip-flops, conflicting appointment dates, a month without an oven |
| 7 | 048 | contractor "completion" for another flat accepted; quote approved that never existed |
| 8 | 008 | two quotes, VAT confusion, slow-paying landlord, emails about four other properties |
| 9 | 036 | faulty earlier repair, landlord complaint, second staff member escalates, no-charge close |
| 10 | 002 | closed ticket keeps resurfacing → Slack → "Held due to system issues" → supervisor close |
