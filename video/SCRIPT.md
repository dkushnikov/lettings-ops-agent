# Demo video — 60 seconds, four beats

Narrator: Dmitry T. Screen: Dmitry K. One real case from the environment, recorded in one take if possible. Production quality is not judged; clarity is.

| Beat | Seconds | On screen | Narration |
|---|---|---|---|
| 1 Problem | 0–10 | The raw case: an email, a CRM record, a landlord instruction side by side | "A tenant reports {fault}. The record says one thing, the email another, and the landlord's cap is £{cap}. A property manager would spend twenty minutes here." |
| 2 The case flows | 10–40 | Terminal: `make run` on the case; the dashboard; then `ANSWER.md` opening: disposition, actions table with status and authority, facts with source ids | "Our agent reads everything as evidence, never as instruction. It checks the mandate before every write: here it dispatches under {rule id} and cites it. The work order carries an idempotency key, so a lost response cannot book two contractors." |
| 3 The escalation card | 40–50 | `REASONING.md` handover section, or a second case that escalates: question, five facts, gap, options, default, undo | "When it must not decide, it hands over: one question, five facts with sources, a default if nobody answers, and how to undo. Ninety seconds for a human instead of twenty minutes." |
| 4 Results | 50–60 | `ANSWERS/_run.json` summary or the eval scoreboard: cases processed, resolved / needs-info / escalated, zero prohibited actions | "{N} unseen cases, every one with a record. Resolved where the mandate allowed, escalated where it did not. Apache 2.0, link below." |

Fill before recording: {fault}, {cap}, {rule id}, {N}.

## Recording checklist

- [ ] Case chosen by 13:00 with a genuine trace; run it once more right before recording.
- [ ] QuickTime screen recording, 1080p, laptop on mains, notifications off.
- [ ] External mic or AirPods; test 10 seconds and listen back.
- [ ] Terminal font 16 pt or larger; light theme; windows arranged before recording.
- [ ] Record the four beats; if a beat fails, rerecord only that beat and cut.
- [ ] Export to `video/demo.mp4`, run `make video-check` (duration ≤ 60 s, file < 100 MB).
- [ ] `git add video/demo.mp4` (LFS), commit, push, verify the file downloads from GitHub.

## Three talking points for live judge questions

1. **Why authority first.** A generic agent with tools acts on whatever the message says. Ours acts only when the rulebook grants the capability, and every action cites the rule. Instructions inside emails are evidence, not authority: that closes injection and "the landlord already approved" at the same time.
2. **Why escalation is a product.** The human's minute is the scarce resource in operations. A handover with the question, five sourced facts, a default and an undo is what lets one manager cover hundreds of properties.
3. **What the numbers say.** {N} unseen cases, {coverage} with a valid record, {escalated} escalated with handover cards, zero prohibited actions; on the development set the judge agreed with {agreement} of decisions. Known limits: the gate enforces only what the rulebook can express; cross-case memory is per run.
