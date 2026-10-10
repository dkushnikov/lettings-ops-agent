# Plan: operating practices to bring over from Atlas

Written 10 October 2026, 14:00, during the hackathon. Atlas is the author's personal agent system (identity, memory,
schedulers, observability). Its identity and memory layers do not belong here; four of its operating practices do,
because each of them was done by hand today and cost time or caught a defect late. In order of value.

## 1. A regression gate before any freeze or merge (`make regress`)

What Atlas has: a verifier agent with fresh context runs after every change, and promotion to the machines is refused
when the canary suite is red.

What it looks like here: `make regress` runs a fixed subset of public cases (the eleven that scored lowest at the start,
plus the seven with attachments and the two wrong-property traps) through the agent and the judge, compares the totals
with `runs/baseline.json` (outcome, judgement & safety, critical, prohibited, fallbacks, dispositions), prints the
per-case diff, and exits non-zero on any drop beyond the judge's noise band (one point per case, two in total).
`make freeze` and the merge checklist call it first. Today this loop was run by hand four times (`runs/eval10`,
`eval11b`, `eval11c`, `eval11d`); the judge's variance was measured at about one point per case.

Effort: half a day. Pieces exist: the runner, the judge, `runs/eval10-compare.py`.

## 2. A runs board (`make board`)

What Atlas has: a pulse board — every scheduled job with its last result, age and red/green state, read at the start of
every session.

What it looks like here: one page over `runs/`: every run with its commit, counts, dispositions, judge totals, wall time,
links into the case browser and the report; simulation runs with their scenario verdicts; newest first. Being built
today as `evalkit/runsboard.py`.

Effort: done today or tomorrow.

## 3. A findings log with triage states (`docs/findings.md`)

What Atlas has: findings from automated checks are recorded as intent records, each with a state (`fix`, `schedule --due`,
`dismiss --until --why`), and the brief shows the open count until each one is closed.

What it looks like here: every finding from a judge (ours, an independent one, the simulator's grader, a human reviewer)
gets a line: date, source, case or scenario, the claim, state, commit or reason. Today's entries would be: the
independent judge's four findings (F1 closed before it arrived, F2 fixed in `e1fdb35`, F3 fixed in rule 5 and the
reviewer, F4 scheduled to the playbook owner); the council review's blockers; the simulator's fifteen PARTIAL verdicts
scheduled to the scenario owner. The README's "known limitations" section is then generated from the open lines.

Effort: an hour for the file and the discipline; a script later.

## 4. Every artefact persisted, every run resumable

What Atlas has: session logs with a resume point, run records for every council consultation, and the rule that a
session end cannot be relied on, so state is written as it happens.

What it looks like here: the harness already writes `_run.json`, `_cutoffs.yaml`, `_expected/` and four files per
case; the simulator will write `runs/sim/<stamp>/` (today); add a `CHANGELOG.md` line per committed change with the
commit and the numbers that justified it (the status block kept in the author's notes today), and a `--resume` on the
simulator matching the runner's checkpoint behaviour.

Effort: an hour today for the changelog; the simulator resume later.

## Not brought over

- Identity, memory, privacy tiers: the agent is defined by its four data artefacts; its only persistent memory is the
  ticket.
- The multi-model council as a module: it is used as a review gate before a release (today, before the freeze), not as
  part of the runtime.
- Scheduling and the coordination locks: there is one runner and no concurrent writers yet.
