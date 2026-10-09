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

## Built during the event

- The adapter from the organisers' data and tools to the harness (`harness/adapters/` or `mockworld` replaced).
- Rulebook content extracted from the environment's documents and merged with source SRC-ENV.
- Playbook edits reflecting the environment's workflows.
- All handling specific to the provided cases, the demo case, the video, and the Reality Test results in `ANSWERS/`.

<!-- TODO(event): list the files changed after `pre-event`, e.g. `git diff --stat pre-event..freeze-1630`. -->
