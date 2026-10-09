# Saturday 10 October 2026 — plan and gates

All times BST. The plan changes at four points: 10:15 (shape of the environment → adapter type), 11:00 (gate), 13:00 (demo case chosen), 14:00 (scope freeze). Everything else holds.

## Roles

| | Dmitry Taranov — operator, judge, product | Dmitry Kushnikov — builder, runtime |
|---|---|---|
| Owns | What the agent may do: rulebook content via staging and approval · golden run · verdicts on records (dev and mutated cases) · which mutations to apply · demo case, script, narration · README narrative, assumptions, limitations · posts, submission form · rehearsal from a fresh clone · **time and gates** | Adapter to the environment, choice of inner loop · gate as enforcement, executor, runner, traces · capacity and rate limits · review of coding-agent diffs on gate and renderer · freeze ritual, tags, hashes, push, LFS · the Reality Test run |
| Together | 10:00–10:30 topology and golden run · the 11:00 gate decision · 15:00 rehearsal · 16:30 run (Dmitry K. drives, Dmitry T. verifies the checklist) | |

Protocol: five-minute sync at the top of every hour. The judge's verdict on a case is final; the builder fixes it or writes it into limitations. Gates are announced by Dmitry T.; technical choices are Dmitry K.'s. Rulebook and playbook edits are Dmitry T.'s to make directly; code changes go through Dmitry K. After 14:00 no new abstractions and no refactors.

## Schedule

| Time | What | Deliverable |
|---|---|---|
| 09:00–09:30 | Table with power, Wi-Fi, `make check` on both laptops | two green laptops |
| 09:30–10:00 | Briefing: ask the questions below, write answers here | answers |
| 10:00–10:15 | **Topology**: files / REST / MCP / starter kit; case boundary; count; expected outcomes present? | adapter choice on paper |
| 10:15–10:30 | **Golden run**: two real dev cases solved by hand (one routine, one approval or conflict); expected tool effects written down | two reference cases |
| 10:30–11:00 | Adapter (K.) · rulebook from environment documents via staging (T.) | first real case runs |
| **11:00** | **Gate**: one real case end to end — record written, tools called or recorded. No → B-minimal: classify → evidence → safe deterministic actions only → otherwise escalate | go / cut |
| 11:00–13:00 | All dev cases through the system; 3–5 real cases mutated per axis; eval loop: T. reads records and rules, K. fixes gate, rulebook, handlers | scoreboard; **demo case chosen by 13:00** |
| 13:00–13:30 | Lunch | — |
| 13:30–15:00 | Hardening; measure case latency, tokens, rate limits → set concurrency; README real content; **14:00 scope freeze** | README 80 %; capacity plan |
| 15:00–15:30 | **Rehearsal** from a fresh clone, T. drives, K. does not touch the keyboard; tag `rehearsal` | `make rehearse` green |
| 15:30–16:00 | Video: T. narrates, K. drives; posts finished | `video/demo.mp4` ≤ 60 s in repo via LFS |
| 16:00–16:30 | **Feature freeze**. Repo public; secrets scan, LFS, LICENSE, README, PREBUILT, form fields; tag `freeze-1630`, hash into SUBMISSION.md | submission minus results |
| **16:30–17:00** | **Reality Test**: count cases, print the capacity estimate, launch the batch, watch the dashboard; 16:50 stop launching optional reruns; every case has a record; commit and push `ANSWERS/`; submit | submitted before 17:00 |
| 17:00–19:00 | Demos, People's Choice, posts, networking | — |

## Briefing questions (09:30)

1. Code freeze: 16:30 (rules §4) or 17:00 (rules §7)? Is the demo video due before 16:30 or may it be added after 17:00?
2. How is the environment delivered: files, REST mocks, MCP servers, a starter framework?
3. What is a case: one folder, one ticket id, one thread? How must `ANSWERS/<n>` be numbered to match your case ids?
4. How many Reality Test cases should we expect, and how many development cases?
5. Do development cases come with expected outcomes or rubrics?
6. What are the "frameworks" you provide? Is any of it mandatory?
7. Tokens: Anthropic API keys or console credits? Rate limits per team?
8. Where is the submission form and when does it open?
9. Are partner mentors on site, and are there office hours?
10. May we publish the supplied data, documents and traces in the public repository under Apache 2.0, or only our code and outputs?
11. How does the commit containing Reality Test results relate to the frozen code hash: one hash or two?
12. Do the supplied tools keep state that judges inspect (work orders created, messages sent), or is only `ANSWERS/` evaluated?

## Kill signals

- 11:00 no end-to-end case → B-minimal.
- 12:30 no dev case with a correct decision → policy reduced to "act only on an explicit rule, otherwise escalate".
- 14:00 agent loops or exceeds the step cap → lower the cap, route unfinished cases to escalate.
- 15:00 video not scripted → T. writes the script instead of polishing README.
- 16:40 batch not fitting the window → reduce concurrency only on 429s; otherwise let it run; the fallback closes the rest.

## Done at 17:00

- [ ] `ANSWERS/<case-id>/` for 100 % of supplied cases, generated by the system, traces alongside
- [ ] No empty case folder; every escalation has a handover card
- [ ] Repository public, Apache 2.0, `make setup && make run` works from a fresh clone
- [ ] README's eight sections filled; `PREBUILT.md` separates Friday from Saturday
- [ ] `video/demo.mp4` ≤ 60 s inside the repository
- [ ] LinkedIn and X posts published with the repository link
- [ ] Form: repo URL, team, track, members, hash, results path, video path, post URLs
