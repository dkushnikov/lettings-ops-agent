# What existed before the event

Git tag `pre-event` marks the repository as it stood before 10:00 on Saturday 10 October 2026. Everything listed here was written on 9 October, before the team had any access to the hackathon environment.

## Built before the event

Harness (`harness/`), generic, environment-agnostic:

- `schema.py` — the data contract: Case, Artefact, ToolSpec, GateDecision, ActionRecord, DecisionState, Handover, Promise, Clock, RunMeta.
- `tools.py` — tool registry, bound tools, the environment adapter protocol, tool error classes.
- `rulebook.py` — loads `agent/rulebook.yaml`; evaluates capabilities, approvals and prohibitions for a proposed action.
- `playbooks.py` — loads Agent-Skills-format playbooks; selects by case type.
- `gate.py` — the policy gate at the tool boundary: deny-by-default for write tools.
- `executor.py` — read/write execution: retries for reads, idempotency keys and reconcile for writes, `unconfirmed` state.
- `loop.py` — the decision loop on the Anthropic Messages API with three terminal tools (`finalize`, `request_info`, `escalate`) and a step cap.
- `reviewer.py` — second-pass check of the planned record against the rulebook.
- `recorder.py` — JSONL trace, `ANSWER.md` and `REASONING.md` rendering, sanitisation of untrusted content, secret redaction.
- `runner.py` — batch execution: concurrency, per-case timeout, retry budget, checkpoints, token-bucket throttle, never-empty fallback, capacity estimate, run metadata.
- `cli.py` — `run`, `eval`, `rehearse`, `freeze`, `demo`, `mutate`, `rules-extract`.

Agent definition (`agent/`), priors only:

- `rulebook.yaml` — UK lettings maintenance priors (source SRC-PRIORS), with rule ids the record cites.
- `playbooks/*/SKILL.md` — five playbooks: maintenance-request, emergency-hazard, access-scheduling, compliance-expiry, contractor-failure.
- `rulebook_staging.md` — the template for rules extracted from environment documents.
- `tools.yaml` — manifest template for the mock world.

Mock world and evaluation:

- `mockworld/` — an in-memory lettings world with read and write tools and failure injection, used only as test fixtures.
- `fixtures/` — synthetic cases with expectations, one per exception axis.
- `evalkit/` — mutation generator and a rubric-based judge for our own development loop.
- `tests/` — unit tests for the gate, executor, runner, recorder and loaders.

Documents: `README.md` skeleton, `PLAN.md`, `RUNBOOK.md`, `SUBMISSION.md` template, `docs/domain-cheatsheet.md`, `docs/rules-extraction-prompt.md`, `posts/` drafts, `video/SCRIPT.md`.

## Built during the event (10 October)

- `harness/adapters/dwelly.py` — the organisers' case format (index.md, history.md, attachments) as artefacts with
  trust classes; decision points by cutoff; hidden outcome handed only to the judge; read tools and a write ledger.
- The record's status block (recap, stage and hold, last update, next step) and the definition-of-done checklist;
  workflow stages, side states, hold reasons and manual-mode triggers as mandate data in `agent/rulebook.yaml`;
  `definition_of_done` in all five playbooks.
- Reviewer rule R8 (resolved while on hold → needs_info); decision routing by owner; landlord replies as authority;
  a priced quote to the landlord before work; attachments gated by the decision point; a time budget inside the loop
  and the live state kept on timeout; tool-call markup stripped from records.
- `docs/system-design.md` (the ticket, roles, models; implemented vs designed), `docs/pm-cases-analysis.md` and
  `docs/pm-cases-cheatsheet.md` with `data/pm-cases-index.json` (`make pm-index`).
- `evalkit/report.py` (run report), `evalkit/casebrowser.py` (case browser with cutoffs, run overlay and step-by-step
  replay; `make replay`), `evalkit/simulate.py` with `evalkit/actors/` (multi-actor scenarios, by Dmitry Taranov).
- The Reality Test results in `ANSWERS/`, the video, the posts.

<!-- TODO(event): `git diff --stat pre-event..freeze-1630 | tail -1` at the freeze. -->
