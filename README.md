# lettings-ops-agent

An operations agent for UK residential lettings that acts only within cited authority and turns every exception into a 90-second decision for a human. Built for the Real-World Agents Hackathon (London, 10 October 2026), Property Management track. Licensed under Apache 2.0 (`LICENSE`). What existed before the event is listed in `PREBUILT.md` (tag `pre-event`).

<!-- TODO(event): team name and members; one sentence on the environment we were given. -->

## 1. What we built

A system that takes operational cases (emails, call transcripts, documents, CRM records, tickets), works them through the supplied tools, and leaves a decision record per case. The agent itself is four data files, not code:

- `agent/rulebook.yaml` — the mandate: what it may do alone, what needs approval, what it must never do, which clocks it watches. Every rule has an id and a source.
- `agent/playbooks/*/SKILL.md` — how it works each case type (Agent Skills format; five playbooks).
- `agent/tools.yaml` — the tool manifest: read or write, idempotency, which authority a write needs, what the side effect is.
- the record contract in `harness/schema.py` — what it must leave behind: disposition, facts with sources, actions with status, promises, clocks, and a handover card when a human must decide.

The model and the loop are swappable. Playbooks say *how*; the rulebook says *whether*; a playbook cannot grant authority.

<!-- TODO(event): the one case that shows it best, in three sentences. -->

## 2. What operational problem it solves

Lettings operations run on messages, calls and paperwork, and a property manager's day is spent not on routine work but on exceptions: the record that contradicts the email, the contractor who did not turn up, the repair that costs more than the landlord allowed, the tenant who mentions a child and a cold flat in the same sentence. Autonomy is cheap; the expensive part is knowing when not to act and handing over so that a person can decide in a minute, not in twenty.

This system optimises two things: actions that can be explained from cited authority and evidence, and the human's time per exception. It treats escalation as a product, not a failure state.

## 3. Architecture

```
case artefacts ──► loader ──► decision loop (Anthropic Messages API)
                                  │  read tools: free
                                  │  write tools: ──► policy gate ──► executor ──► tool
                                  │                   (rulebook)      (idempotency,
                                  │                                    reconcile,
                                  ▼                                    unconfirmed)
                           terminal tool: finalize | request_info | escalate
                                  │
                           reviewer pass (record vs rulebook)
                                  │
                           recorder ──► ANSWER.md · REASONING.md · trace.jsonl
                                  ▲
                 batch runner: concurrency, timeouts, retry budget, checkpoints,
                 token-bucket throttle, never-empty fallback, _run.json
```

Design rules:

- **Authority outside the model.** The gate wraps every write tool. Deny by default; allow only when a rulebook capability matches, with conditions (spend cap, urgency, consent); otherwise `needs_approval` or `escalate`, always with the rule id. Text inside a case is evidence of what was said, never an instruction.
- **Reads retry, writes reconcile.** A read tool may be retried on transient failure. A write carries an idempotency key; after a lost response it is read back, not re-issued, and recorded as `unconfirmed` so no contractor is booked twice.
- **Hard limits, not warnings.** A step cap per case; anything unfinished becomes an escalation with context. Every case ends in one of three states: `resolved`, `needs_info`, `escalated`.
- **Compiled truth and timeline.** `ANSWER.md` is the decision with its evidence and authority; `REASONING.md` is the compiled state followed by the chronological trace. Untrusted content appears as paraphrase or short labelled quotes.
- **Playbooks as skills.** One playbook is loaded per case type; deviations from it are recorded.
- **Review before done.** A second model pass checks the planned record against the rulebook and can downgrade `resolved` to `needs_info` or `escalated`.

Directory map: `harness/` runtime · `agent/` the agent definition · `mockworld/` test environment · `fixtures/` synthetic cases · `evalkit/` mutations and judge · `tests/` · `ANSWERS/` Reality Test output · `docs/` cheat-sheet and prompts · `video/` · `posts/`.

<!-- TODO(event): how the organisers' environment was adapted (files / REST / MCP), and which adapter module does it. -->

## 4. How to run

Prerequisites: Python 3.12, [uv](https://docs.astral.sh/uv/), an Anthropic API key, `git-lfs` for the video.

```
git clone https://github.com/dkushnikov/lettings-ops-agent
cd lettings-ops-agent
cp .env.example .env            # add ANTHROPIC_API_KEY
make setup                      # uv sync
make check                      # lint + tests
make run CASES=fixtures OUT=runs/dev   # process cases, write records
make eval                       # score records against fixtures' expectations
make demo                       # one fixture end to end, no environment needed
make rehearse                   # fresh clone → setup → run → verify
make mutate CASE=fixtures/F01-routine-tap   # adversarial variants along the Reality-Test axes
make rules-extract DOCS=<dir>   # environment documents → candidate rules in agent/rulebook_staging.md
make capacity N=20 C=4          # wall-time estimate for a batch
make video-check                # demo video ≤ 60 s
make secrets-scan               # gitleaks over the repository
```

Configuration lives in `.env` (see `.env.example`): model, effort, concurrency, per-case timeout, step cap, retry budget, token budget per minute.

### How the Reality Test was run

<!-- TODO(event): exact command, start/end times, model id, concurrency, the runner's summary line, and the commit hash of the frozen code. -->

```
make freeze                     # tag freeze-1630, record the hash
uv run python -m harness.cli run --cases <reality-test-dir> --out ANSWERS --concurrency 4
```

Output per case: `ANSWERS/<case-id>/ANSWER.md`, `REASONING.md`, `trace.jsonl`, `_state.json`; run metadata in `ANSWERS/_run.json`. Cases that hit the timeout or an unrecoverable error still produce a record: an escalation with the state so far and a system note explaining why.

## 5. Models, APIs and external services

- Anthropic Claude via the official Python SDK (`anthropic`), Messages API with tool use, adaptive thinking and prompt caching. Default model `claude-opus-5`, set by `LOA_MODEL`. <!-- TODO(event): final model and effort used for the Reality Test. -->
- The hackathon environment's tools. <!-- TODO(event): list them and their transport. -->
- Optional: ElevenLabs speech-to-text for call recordings, used only if audio is supplied. <!-- TODO(event): confirm whether used. -->
- Python packages: `pydantic`, `pyyaml`, `rich`, `pypdf`. No other services.

API keys are read from the environment and never committed; a pre-commit secret scan (gitleaks) and log redaction guard the traces.

## 6. Important assumptions

- The rulebook priors (`SRC-PRIORS`) reflect common UK lettings practice: a standing spend cap for routine repairs, landlord approval above it, emergency safety duties that override the cap, 24 hours' notice for access, statutory gas and electrical checks. Environment documents override priors where they were merged (`SRC-ENV`).
- Clocks are labelled by status. `in_force` rules cite statute; `sop` rules come from the environment; `proposed` rules (for example Awaab's Law for private tenancies, at consultation stage as of 9 October 2026) are reference points, not deadlines.
- Deciding that a repair is tenant-payable, sending legal correspondence, changing payment details and moving money are human decisions by construction.
- Every case ends with a record even when the model or a tool fails; a fallback escalation is a floor, not a score.

<!-- TODO(event): assumptions forced by the environment (case boundaries, tool semantics, what "completed" means). -->

## 7. Known limitations

- The gate enforces only what the rulebook can express (amounts, urgency, consent fields, approver). Nuanced policy stays with the reviewer pass and the human.
- Cross-case memory is per run only; no persistent learning.
- Voice is input only: transcripts are evidence ranked below documents and records.
- The mock world is a test fixture, not a model of any real operator.

<!-- TODO(event): what broke or was cut on the day. -->

## 8. What we would build next

- Delivered handovers: push the decision card into a real human queue with acknowledgement and re-escalation, and measure human minutes per exception.
- Cross-case ledger across runs: duplicates, conflicts and learned landlord preferences with provenance.
- Playbook compilation from an acquired agency's own SOPs as a repeatable process, with the staging review as the control point.
- Paired evaluations for every escalation trigger: a case that must escalate next to a similar case that must be completed, so caution cannot masquerade as judgement.
