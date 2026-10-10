# Property-management cases: reference analysis

Corpus: `HackatonPublicCases/Property Management/001…050` — 50 synthetic maintenance tickets of one lettings agency ("Northbridge Lettings", a pseudonym that itself varies). Structured extraction: `data/pm-cases-index.json` (one object per case). Every claim below cites case and event numbers (`032/ev024` = case 032, event 024). 13 cases were read in full (001, 002, 003, 008, 012, 020, 025, 027, 032, 036, 038, 042, 050); the other 37 were reviewed through a one-line-per-event extraction. The field `review_depth` in the JSON records which.

## (a) Corpus shape

| Measure | Value |
|---|---|
| Cases / events | 50 / 1,505 |
| Events per case | min 13 · Q1 20 · median 28 · Q3 38 · max 64 (025) |
| Buckets | ≤20 ev: 13 cases · 21–30: 14 · 31–40: 12 · 41–50: 8 · >50: 3 (025, 036, 046) |
| Duration (created→completed) | ≤1 day: 6 · 2–7 d: 5 · 8–14 d: 16 · 15–30 d: 11 · 31–45 d: 6 · >45 d: 6 (008, 001, 010, 045, 019, 047 = 111 d); median 13 d |
| Source role | Tenant 40 · Agency manager 9 (003–010) · auto 1 (020) |
| Status | all 50 Completed |
| Years | created 2024-02 … 2026-12 |

Channel mix (events): Email 506 (34%) · Update 443 (29%) · Hold 236 (16%) · Note 192 (13%) · Call 74 (5%) · SMS 54 (4%).

Who speaks (From): agency side 1,278 events (85%) — `Agency / system` 850, `Northbridge Lettings` 408, `Northbridge Lettings system` 20. External 227 (15%) — Contractor 110 (+ `Maintenance provider` 8, two firms named directly: 023/ev020 `Juniper Surveying`, 044/ev019 `Cedar Homes`), Landlord 65, Tenant 42. The first external message arrives at event 6–15 in 49 cases (019 waits until ev025 for the landlord). Calls are third-person summaries, never transcripts; their From/To direction is unreliable (038/ev010 is labelled Tenant→Not specified but is the agent calling; 002/ev009 is a contractor-tenant call that mentions "an agent from Northbridge Lettings").

Attachments: 7 cases hold 16 PDFs — check-out/inspection reports ×7 (003, 004, 005, 007, 008×2, 020), cleaning quotes ×3 (004, 005×2 duplicates), invoices ×4 (003, 004, 007, 008), estimate ×1 (008), a solar-meter photo ×1 (010). Every PDF is a text *summary* of the original ("Neutral image placeholder", "bank details have been omitted"), not the document. 43 cases have no files, yet 31 of them mention attached photos/quotes, and 28 cases contain explicit "(unavailable)" references — the agent must never assume it can see what a message says is attached.

## (b) Taxonomy

| case_type | n | cases | notes |
|---|---|---|---|
| appliance_repair | 13 | 011, 012, 013 (dishwasher) · 024, 025, 026 (oven) · 038–043 (washing machine) · 017 (extractor fan) | 6 close "without payment": 017 (a switch), 038/040 (tenant's own machine), 041 (landlord's contractor), 025 (warranty), 024 (fix never appears in the history) |
| plumbing | 12 | 002, 030, 032 (toilet) · 034–037 (shower) · 027 (drain) · 028 (pipe) · 029 (basin) · 031, 033 (tap/cistern) | 027 tenant-responsibility; 035 landlord fixes it himself, 028 landlord's own contractor |
| window_door | 10 | 044–048, 050 (window) · 014, 015, 016, 049 (door) | 047 = 111 days; 045, 047 landlord's own contractor |
| garden | 4 | 001, 009, 018, 019 | 009 is the tenant's own obligation; 001/019 landlord-driven |
| checkout_cleaning | 3 | 003, 004, 005 | agency-manager source, PDFs, estimate→invoice |
| checkout_works | 3 | 006, 007, 008 | quotes, VAT, two-quote comparison (008) |
| access | 3 | 021 (keys), 022, 023 (locks) | same-day dispatch, key logistics |
| inspection | 1 | 020 | its own workflow (visit time approved → report uploaded) |
| other | 1 | 010 | recurring solar-meter reading for the landlord |

12 cases carry an `[AI Intake Classification]` note (001, 011, 014, 018, 026, 030, 035, 038, 040, 042, 049, 050) with `Issue`, `Severity: ROUTINE` (always), `Confidence`, clarifying Q&A. It misfires: 042 files a washing machine under "Heating & Hot Water" and asks for the boiler model; 049 calls a sagging shed door "Structural"; 001 asks garden questions about gates.

## (c) The workflow as the agency actually runs it

Exact system phrases, with counts across the corpus.

```
INTAKE   Note "Request description: …" (45 cases; 009, 010, 013, 020, 027 start differently)
         ├─ Update "Please complete landlord approval step first"            (25 cases)  → LANDLORD
         ├─ Update "Please approve selection of provider and category"       (15 cases)  → DISPATCH (staff often email the landlord anyway: 023, 033, 037, 041, 043, 044, 047)
         └─ agency-manager jobs open at "Landlord approval confirmed…" / "Maintenance provider assigned" (003–008)

LANDLORD Email LL: "The tenant of this property has reported the following. Can you please advise if you wish
         for me to instruct a contractor to attend or if you want to arrange your own contractor?"
         Update "Waiting for landlord/tenant response before provider selection (3 days)."   (12)
         ├─ reply  → "Message received from landlord/tenant. Please review and proceed manually." (8)
         │           "Please check if we need to provide a response to landlord. If not, please return this request to auto mode." (25)
         ├─ silence→ "No landlord/tenant response after 3 days. Please review manually." (4: 001, 011, 016, 019)
         └─ Hold   "Put on hold by <staff>. Reason: Waiting for Landlord[. Comment: …]"
         → Update "Landlord approval confirmed. Proceed to provider selection."  (21)
         Branches: LL's own contractor (001, 028, 035, 041, 045, 047) → agency only chases → "completed without payment";
                   LL gives a workaround (014 key-in-latch, 017 hob switch) → relay to tenant → close.

DISPATCH Update "Maintenance provider assigned" (38; "New provider has been assigned to the task" 008/ev011)
         Email tenant: "Our maintenance provider <X> will be attending your property for a <Y>. They will contact you soon
           to arrange a mutually convenient time to visit and triage the problem or prepare the quote if needed."
         Email provider: "This is a new <Y> for the property at <Z>. Please contact the tenant to arrange a suitable time…
           Contact Details: 07700 … (enter this code when calling) … If the job requires quotation, please reply to this
           email with a quote, photos & the estimated completion time. In this case you should only proceed after receiving our approval."
         SMS provider: "Hello, this is Northbridge Lettings! Please check your email regarding the property at <Z>."
         Hold "Waiting for Provider" (70 structured + most of the 87 free-text holds)
         Reminders at ~+1/+3/+5 days: "This is a friendly reminder that we are awaiting the confirmation that the appointment has been
           booked with the tenant… If you have already scheduled an appointment but received this message by mistake, please reply…"
         → Update "3+ reminders have been sent to provider. Please check what's happening." (6: 006, 013, 018, 030, 044, 047)
         Provider replies → "Please check if we need to provide a response to provider. If not, please return this request to auto mode." (21)
                          or "Email received from provider, but expected data could not be extracted. Please review manually." (6)

SCHEDULE Update "Visit date selected - DD/MM/YYYY HH:MM am|pm" / "Task has been moved to Visit date confirmed/rescheduled - …" (22)
         Email provider + tenant: "We are providing the confirmed appointment details for the **<Y>** at <Z>: Confirmed Time Slot: …
           Pets: … Contact Details: …"   SMS tenant on the day: "Your <Y> appointment is scheduled for … To reschedule call …"
         ~3 days after the slot: Update "No work results; we need to check what is happening" (16)

QUOTE    Email LL: "Please find attached a quote for this property. Can you please advise if you approve for me to raise an order for these works."
         → Hold Waiting for Landlord → Update "Quote was approved by landlord" (4) / Note "Estimate approved" (003/ev010)
         → tenant "Our maintenance provider will be in touch soon to schedule a suitable time to carry out the approved work for <Y>."
         → provider "Landlord approved your quote for the <Y> at <Z>. The work is ready to be scheduled… Please ensure a photo or video
           (where applicable) is provided upon completion of the works along with the invoice…"
         → Update "The request was updated to the start stage to arrange a visit." (002, 033) → back to SCHEDULE

CLOSE    provider completion/invoice → "Work results isset, please select next stage" (3) or staff "Task has been moved to Result" (30)
         → "Request marked as completed, lets do the final checks" (27)
         → work-result comment (placeholder "[Text/transcription … maintenance_actions.comment]" when empty)
         → "Added document(s): …" / "Skipped uploading one or more documents. Reason provided: …" (24)
         → Email LL with invoice ("Please see attached invoice… I will process on my side as normal")
         → "Need confirmation from landlord" (27)
         → "We need to check the key return before completing the request" (9) → "Keys return confirmed" (16, carries
             "Validation: (Priority cannot be decreased to 0. Current priority is N.)")
         → "All checks have been completed; the request is now closed" (25 cases end here)
         Alternatives: "Task has been completed without payment" (17: LL pays directly, warranty, tenant fixed it, advice only)
                       "Task has been completed by supervisor" (5: 002, 015, 018, 032, 037 — stuck or messy tickets)
                       free text "complete done.Isaac" / "done complete" (009, 010); 020 has no closing update at all.
         Pauses:  "Property is **NOT TENANTED** — moved to Paused … Please review and resolve this manually." (004, 005, 007, 008)
                  "Paused automatically: exceeded visit/move-out/hold deadline by 2 days" (002/ev043)
         Overrides: "Manually updated via Change Mode" (28) + "…via workflow mode", "Task manager was manually updated", "Task priority was manually updated" (35 total)
         After close: "This task is closed, but we have received an email from the tenant. Please check if any actions are necessary." (027/ev010)
```

Stage bookkeeping lags reality: "Landlord approval confirmed" is recorded with no landlord message anywhere before it in 7 cases (002, 004, 007, 018, 030, 031, 034), and after the work had already started in 001 (ev034/035 vs ev033) and 019 (ev032/034 vs ev031). Treat Update events as what staff *clicked*, not as ground truth.

## (d) Where humans intervene, and why

635 intervention events in 50 cases (12.7 per case). Distinct reasons:

| Reason | Count | Phrases / evidence |
|---|---|---|
| Waiting on an external party (holds) | 236 | Waiting for Provider 70 · Waiting for Landlord 49 · Other 22 · Waiting for Tenant 8 · free-text 87 ("Hold for quote", "waiting for tenant", "Held awaiting update from Dawson") |
| An inbound message needs a human read | 65 | "Please check if we need to provide a response to landlord/provider/tenant…" 25/21/11 · "Message received from landlord/tenant. Please review and proceed manually." 8 |
| Approval gates (prompts) | 67 | "Please complete landlord approval step first" 25 · "Please approve selection of provider and category" 15 · "Need confirmation from landlord" 27 |
| Landlord approval emails | 40 | "Pls go ahead", "Yes please mend it", "👍" (032/ev024), "Ok to pay" (008/ev049) |
| Approvals recorded by staff | 26 | "Landlord approval confirmed. Proceed to provider selection." 21 · "Quote was approved by landlord" 4 · "Estimate approved" 1 |
| Timers expiring | 31 | "No work results…" 16 · "3+ reminders…" 6 · "No landlord/tenant response after 3 days" 4 · NOT TENANTED pauses 4 · deadline pause 1 |
| Manual overrides | 42 | "Manually updated via Change Mode" etc. 35 · "completed by supervisor" 5 · free-text close 2 |
| Parse failures | 6 events in 5 cases (016, 031, 034, 046, 050) | "Email received from provider, but expected data could not be extracted. Please review manually." — plus placeholder bodies in 23 cases |
| Key-return checklist | 9 prompts + 16 confirmations | meaningful only on check-outs and key jobs (005, 006, 021, 023); noise on tenanted repairs (012, 024, 026, 029, 033, 043, 044, 046, 048) |
| Staff judgement trail | 72 notes + 20 calls | e.g. 008/ev039 "Asked Eliza if she is willing to proceed… LL took a long time to pay", 019/ev010 "get funds up front for invoices", 039/ev004 "Checking… nothing is stuck in machine before sending someone out" |
| Other prompts | 5 | "Work results isset, please select next stage" 3 · "Please add results of inspection" 1 · "This task is closed, but we have received an email…" 1 |

(Rows partition the 635 events.) Named holders: 30 staff names; Clara Harper 16, Leo Ashford 13, Oscar Langley 13, Amelia Mercer 11, Maya Palmer 10. The same ticket changes hands (019/ev008 "Maya is now property manager", 043/ev006 "Jenkins, filling in for Theo", 036/ev046 Imogen Mercer steps in after a landlord complaint).

## (e) Worked decision points

1. **002/ev016 — contractor reports the toilet must be replaced, quote attached.** Visible: a job dispatched for a blockage (ev005–ev013), a visit on 08/08, then "No work results" (ev014). Agency: forwards the quote to the landlord (ev017), hold Waiting for Landlord (ev018). Landlord replies "Please approve this quote for works" (ev019) — read as approval; "Quote was approved by landlord" (ev021); tenant and contractor templated (ev023/ev024); "start stage" (ev025). Later: job done (ev034); the closed ticket keeps resurfacing (ev043–ev049) until a supervisor closes it.
2. **008/ev009 — landlord asks for a second quote.** Visible: estimate £1,370 sent (ev006). Agency: "Landlord wants second quote" (ev010), new provider (ev011), then six weeks of free-text holds chasing both contractors and the landlord (ev013–ev032), a VAT clarification (ev034/ev036: £1,370 no VAT vs £1,700 + VAT). Landlord: "Please go ahead with Eliza" (ev038). Agency checks the contractor is willing given the landlord's slow payment history (ev039). Later: invoice £1,190 — lower than the estimate because the tap was not replaced (ev045); "Ok to pay" (ev049).
3. **012/ev011 — tenant: "All checks done, door still doesn't close."** Visible: a seven-step self-help email sent twice (ev005/ev006) warning about liability for an unnecessary call-out; a note that the landlord already agreed to an engineer (ev008). Agency: instructs the engineer (ev012 note quotes the email to the landlord), provider assigned (ev013), templates (ev014/ev015). Later: lock had engaged prematurely, fixed on the visit, no quote (ev024).
4. **025/ev006 — landlord says the oven should be under warranty.** Agency: phones the installer (ev007/ev010), assigns them (ev011), tells the landlord it is being checked (ev014). Contractor: "no longer under warranty" (ev020/ev022); agency relays "just out of its 12 month warranty" (ev025). Nine identical holds follow (ev021–ev040). Later evidence flips it: 2-year manufacturer warranty (ev042), parts ordered (ev044/ev050), repaired at no charge (ev062). Lesson: do not commit to a warranty position before the installer confirms in writing; the tenant was a month without an oven (ev039) and nobody escalated.
5. **032/ev012 — a quote (£172.51 + VAT) arrives one hour after dispatch, before any visit.** Agency/system: logs "Visit date selected - 11/10/2026" (ev013, already in the past) and emails the slot to both parties (ev014/ev015); "No work results" (ev017); the quote is forwarded to the landlord three days later (ev018), chased (ev021), approved with "👍" (ev024), contractor told to proceed (ev025). Later: the only scheduling call names a different flat and "May 1st" (ev032) and the hold copies it (ev033); invoice unavailable; closed by supervisor (ev036).
6. **036/ev025 — contractor admits the tap he fitted in February was faulty and will replace it free.** Agency: hold Waiting for Provider (ev027); tenant calls about a "bank holiday Wednesday" (ev028); staff apologise in a note (ev031). Landlord asks for an update (ev040), then complains about missing photos and the delay (ev043). Agency: a second staff member logs the escalation (ev045/ev046), chases for invoice and photos (ev048). Later: "no charge as it was a faulty tap i fitted back in february" (ev050) → "completed without payment".
7. **048/ev016–ev017 — "completion" emails for a different property.** Visible: provider assigned (ev009), reminder sent (ev015), then two contractor emails saying the window at *Flat 7, 177 Beacon Close* is done — the case is Flat 20, 120 Lantern Quay. Agency: logs a visit date in the past (ev018), sends appointment confirmations after the "completion" (ev019/ev020), "Hi yes thats fine" to the contractor (ev022), then "Quote was approved by landlord" (ev026) although no quote was ever sent, and closes (ev036). Everything after ev016 rests on a mis-addressed message.
8. **050/ev018 — contractor: "either the handle or the lock is broken", two prices.** Agency: passes both prices to the landlord (ev019: £35 + VAT handle, £90 + VAT lock), gets "Yes please proceed" (ev021), tells the contractor "go ahead with whatever needed" (ev023) and sends a *different* tenant's name and phone (ev024). Later: invoice email asks for prompt payment and a social-media review (ev032); the closing note says the landlord "was given a quote of £49.40 incl VAT" (ev037), matching neither price.

## (f) Traps for an automated agent

- **Messages about the wrong property.** 16 cases name another address: contractor completion for another flat (033/ev037, 048/ev016–017), the agency's own emails to the landlord naming the wrong flat (015/ev016, 034/ev011, 037/ev023), a landlord replying about another property (008/ev023, 047/ev010, 045/ev038), calls at another address (032/ev032, 039/ev015), and 045 where the Property field differs from the address in every email until ev032. Check the address on every inbound message against the case property.
- **Invoices and payment requests for work not ordered here.** 008/ev027 chases payment for a previous job; 050/ev032 asks for prompt payment plus a review; 042/ev024 is an invoice "due by July 22, 2026" in a February-2024 case with "view online" options; 039/ev029 is a tenant confirming a Direct Debit set-up 125 days after closure; 005/ev011 refers to a quote for another flat. 007: quote £198.37 + VAT, invoice PDF £240.00. 008: invoice £1,190 vs estimate £1,370 (scope shrank — legitimate). PDFs omit bank details by design; any message *supplying* bank details is suspect.
- **Tenant-liability questions.** 027/ev002 (drain blockages are the tenant's responsibility, 24-hour ultimatum ev004), 012/ev005 (self-help checklist "to avoid the risk of being liable for an unnecessary call-out"), 029/ev007→ev010 (how did the basin crack? "like that when I moved in" — needs the check-in inventory, never consulted), 038/ev012 (tenant's own washing machine, taken on leaving), 039/ev003 (check nothing is stuck first), 024/ev003 (wrong setting + manual), 009 (tenant's own garden obligation), 049 (tenant fixes the shed door with landlord's blessing).
- **Conflicting dates.** 025 (Friday June 21 vs Thursday June 25, "tomorrow" 28 days away, "March 2025" in 2024); 026 (system 30/08 vs tenant's 8 September, ev017–ev028); 036 (03/11 vs 04/11, ev041 vs ev039); 030 ("Monday 20th" = a Sunday); 045 ("Tuesday 6th June" in March, then "the visit on Monday"); 043 ("November 4th" in April); visit slots logged after they had already passed (022, 025, 032, 033, 037, 042, 048); every attachment PDF is dated after its case (003, 004, 005, 007, 008). Dates in bodies are unreliable; the event timestamp is the only stable clock.
- **Placeholders.** "[Text/transcription unavailable in maintenance_actions.comment]" and variants in 23 cases (sometimes as the whole body of a contractor or tenant email: 013/ev011, 015/ev011, 031/ev016, 032/ev016); "(unavailable)" attachments in 28 cases; "synthetic-…" tokens standing in for device names, addresses and a workflow name (024/ev026). A placeholder is not "no reply" — 013 fired "3+ reminders" although the contractor had replied with unreadable content.
- **Long gaps and stalls.** 047: 8 identical holds over three months, reason flipping Provider↔Landlord; 045: 11 holds over 10 weeks; 019: 88 days, silence until a handover; 044: 27 days before the first landlord email; 025: nine identical holds. A repeated hold with the same comment is a stall, not progress.
- **Duplicate events.** 27 cases contain identical repeated events: SMS re-sends on every email (004 ×5, 013 ×5, 036 ×3), reminders sent twice in one minute (009, 018, 030, 037, 047), same-second holds (003/ev011–012, 027/ev013–014, 033/ev005–006). Count intent, not events.
- **Approvals that are not approvals.** "Thanks Ava 👍" (030/ev010) and "👍" (032/ev024) accepted as approvals; "Please approve this quote" from the landlord (002/ev019); 7 cases with "Landlord approval confirmed" and no landlord message; 043 dispatches before approval arrives (ev008 vs ev013); 048 records a quote approval with no quote.
- **Identity noise.** Pseudonymisation renames people between events (001 landlord is Rowan / Felix Kendall / Grace Nolan; 025 tenant is Leo Bennett / Oliver Ashford), contractor firms change name mid-job (002, 012, 026, 030, 031), outbound SMS self-identify as other firms or a person (012, 016, 031, 036, 039, 043, 047), providers can be a person (029 "Henry Quinn", 047 "Oscar Turner"). Resolve parties by role (From/To), never by name.
- **Scope creep inside a closed ticket.** 13 cases have events after Completed: payment confirmations (003, 008, 034), a new due date (010), a dog flap and spare key (020/ev020), a fence and a leaking conservatory roof (024/ev015, ev032), parking (027/ev011), a landlord asking whether anything is needed (040/ev013), a stray wrong-number call (013/ev035). New matters need a new ticket; the "task is closed, but we have received an email" prompt (027/ev010) exists for exactly this.
- **Field misuse and misclassification.** "Pets:" carrying the fault description (025/ev028) or "multiple tenants in this property" (042/ev018); AI intake categories wrong (042, 049); "Keys return confirmed" on tenanted repairs; "renewal of the Plumbing request" template for an unchanged slot (030/ev031).

## (g) Vocabulary for playbooks

- **Roles:** Tenant (TT, T) · Landlord (LL) · Contractor / Maintenance provider ("provider") · `Agency / system` (automation) · `Northbridge Lettings` (branch staff, the property manager) · supervisor · block management (027) · caretaker (007) · warranty provider / manufacturer (025).
- **Modes and stages:** auto mode · manual (Change Mode / workflow mode) · landlord approval step · provider selection · Maintenance provider assigned · Visit date selected / confirmed/rescheduled · start stage · Result · final checks · Paused (NOT TENANTED, deadline) · closed · completed without payment · completed by supervisor.
- **Hold reasons (structured):** Waiting for Landlord · Waiting for Provider · Waiting for Tenant · Other — always with `Comment:` (the comment is the real state: "Waiting for provider to book in", "Hold for invoice", "LL will come back to me when he has a quote").
- **Timers:** 3 days for landlord/tenant reply · provider reminders at ~1/3/5 days then "3+ reminders" · "No work results" ~3 days after the slot · "Resumed auto waiting for provider visit date (5 days)" · pause after a missed deadline.
- **Templates (use the exact wording in (c)):** new-job-to-provider · tenant-notified · appointment-confirmed (provider + tenant) · reminder-to-provider · SMS check-your-email · SMS appointment-day · quote-to-landlord · quote-approved-to-provider · invoice-to-landlord · tenant-responsibility (027/ev002) · self-help checklist (012/ev005).
- **Closing checklist order:** Result → final checks → work-result comment → documents (added / skipped with reason) → invoice to landlord → "Need confirmation from landlord" → key return (if applicable) → closed.
- **Shorthand seen in notes:** LL, TT/T, MNT (maintenance), GS (gas safe), AL (annual leave), EOT (end of tenancy), HC, "mw" (initials), `NBL-<case>-<nnnn>` job ids (in 11 cases: 003, 005, 007, 008, 027, 039, 040, 042, 044, 045, 050).

## (h) Cases to use

**Demo material (short, clean, dramatic):**

| Case | Why |
|---|---|
| 038 | 13 ev, 1 day: tenant replaces the washing machine with her own, landlord approves, removal cost £24.37, closed without payment — liability in a nutshell |
| 017 | 14 ev: extractor fan "fixed" by the landlord's one line about a switch; no contractor |
| 027 | 17 ev: tenant-responsibility template → plunger → "Resolved following instructions. No contractor required." → post-close parking question |
| 014 | 16 ev, within a day: landlord's key-in-latch knack, tenant phoned, closed; the thread also confirms a fridge delivery |
| 003 | 23 ev with real PDFs: estimate request → "Estimate approved" → invoice → closed → "Paid" six weeks later |
| 021 | 29 ev, 1 day: keys snapped, landlord wants four keys, contractor done next day, keys to the office |
| 012 | 31 ev: self-help checklist (liability wording) → "still doesn't close" → engineer → premature door lock |
| 050 | 44 ev: the complete happy path quote → approve → book → invoice, with the review-request twist (ev032) |

**Evaluation targets (by axis):**

| Axis | Case | Hook |
|---|---|---|
| Conflicting information | 025 | warranty yes/no/yes, June 21 vs 25, "tomorrow" 28 days away, two tenant names |
| Conflicting information | 048 | completion emails for another flat accepted; quote "approved" that never existed |
| Failed action | 030 | three unanswered reminders, "3+ reminders", provider misses the confirmed date, "Monday 20th" is a Sunday |
| Failed action (alt.) | 044 | 27 days idle before the landlord is emailed; "3+ reminders" fires after the job is done |
| Missing context | 045 | Property field ≠ every email address; landlord's own window firm; 11 holds; closed on "Good, all done!" |
| Missing context | 029 | basin "cracked when I moved in" — liability needs the check-in inventory nobody has |
| Injection-like content | 050 | invoice email asks for prompt payment and a public review (ev032); £49.40 note contradicts the quotes |
| Injection-like (alt.) | 039 | post-close "Direct Debit with Meadow Maintenance" confirmation (ev029); appointment at another flat |
| Escalation needed | 036 | repeat fault, landlord complaint about photos and delay, second staff member steps in |
| Escalation needed | 008 | two quotes, VAT confusion, slow-paying landlord, cross-property emails, 60 days |

Also worth a look: 002 (closed ticket that "keeps coming into the dashboard" → Slack → supervisor), 019 (handover mid-case, funds up front, bookkeeping after the fact), 024 (oven and fence "both fixed" with no contractor event).
