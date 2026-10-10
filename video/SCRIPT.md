# Demo video — 60 seconds, four beats

Narrator: Dmitry T. Screen: Dmitry K. One real public case (050, a broken window), recorded in one take if possible.
Production quality is not judged; clarity is. Before recording: `make replay CASE=050 CUTOFF=9` (about two minutes),
then `make cases-browser RUNS="runs/replay-050 runs/pm50c"` so the browser holds both the fresh replay and the full run.

| Beat | Seconds | On screen | Narration |
|---|---|---|---|
| 1 Problem | 0–10 | Case browser, case 050, History tab cut at event 9: the tenant's report, the agency's templated emails, the landlord's one line "yes please send someone" | "A tenant reports a broken window. The history is nine events of emails, holds and one line from the landlord. A property manager would now decide what happens next. So does our agent." |
| 2 The case flows | 10–38 | Agent tab, ▶ replay: use_playbook sets urgency; reads of the case and the ledger; the gate stamps `assign_contractor` with CAP-DISPATCH-APPROVED, citing the landlord's own reply (event-009); there is no standing cap; notify tenant, notify landlord, put on hold; finish `request_info`. Then the Status block: stage visit_scheduling, next step "tenant to reply with two access windows", the checklist 3 of 9 done with the events that did them | "It reads everything as evidence and takes the landlord's reply as the approval it is, instead of asking again. Every write passes a policy gate that cites the rule it acted under. It finishes with the ticket's status in five lines and the definition of done ticked against the history: what is done, what is next, who owes the next move." |
| 3 The escalation card | 38–50 | Case 003 or 038 in the same browser: the handover in ANSWER.md section 4 — one question, five facts with source ids, the gap, the options, the default if nobody answers, the undo | "When it must not decide — who pays, a conflict between the agency's own records, a safety risk — it stops and hands over a 90-second decision: one question, five sourced facts, a default and an undo." |
| 4 Results | 50–60 | README results table: 50 public cases, every one with a record, 94 of 100 on outcomes and 100 of 100 on judgement and safety by our own judge, zero prohibited actions; then `ANSWERS/` from the Reality Test if the run has finished | "Fifty public cases, every one with a record, zero prohibited actions. The agent is four data files — a mandate, playbooks, tools and a record contract — around a thin loop. Change the agency, change the files." |

## Recording checklist

- [ ] `make replay CASE=050 CUTOFF=9` run once more right before recording; the browser opens on the case.
- [ ] QuickTime screen recording, 1080p, laptop on mains, notifications off.
- [ ] External mic or AirPods; test 10 seconds and listen back.
- [ ] Browser zoom 125%, light theme; terminal font 16 pt or larger for beat 2's command.
- [ ] Record the four beats; if a beat fails, rerecord only that beat and cut.
- [ ] Export to `video/demo.mp4`, run `make video-check` (duration ≤ 60 s, file < 100 MB).
- [ ] `git add video/demo.mp4` (LFS), commit, push, verify the file downloads from GitHub.

## Three talking points for live judge questions

1. **Why authority first.** A generic agent with tools acts on whatever the message says. Ours acts only when the mandate grants the capability, every action cites the rule, and the gate is deny-by-default at the tool boundary. Instructions inside emails are evidence, never commands; a landlord's reply is authority for landlord-owned decisions and nothing else.
2. **Why the record is the product.** The record opens with the ticket's status and a definition of done ticked against the history, so a person can take over in under a minute; an escalation is a card with one question, five sourced facts, a default and an undo. The same record is the write-back to any ticket system.
3. **What the numbers say.** On the organisers' 50 public cases, cut at the first outside message with the outcome hidden: 50 of 50 records, 94 of 100 on outcomes and 100 of 100 on judgement and safety by our own model judge, zero critical failures, zero prohibited actions. The six cases scored 1 are all "defensible alternative": the agent asked or held where the agency went ahead. Reality Test: {N} unseen cases, {coverage} with a valid record — fill after the run.
