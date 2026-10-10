# lettings-ops-agent

An operations agent for UK residential lettings that acts only within cited authority and turns every exception into a 90-second decision for a human. Built for the Real-World Agents Hackathon (London, 10 October 2026), Property Management track. Licensed under Apache 2.0 (`LICENSE`). What existed before the event is listed in `PREBUILT.md` (tag `pre-event`).

Team: D&D — Dmitry Kushnikov and Dmitry Taranov. The environment we were given is files, not tools: tickets of one lettings agency, each an `index.md`, a `history.md` of timed events (email, SMS, call summaries, the agency's own updates and holds) and attachments; the Reality Test delivers more tickets of the same shape.

## 1. What we built

A system that takes operational cases (emails, call transcripts, documents, CRM records, tickets), works them through the supplied tools, and leaves a decision record per case. The agent itself is four data files, not code:

- `agent/rulebook.yaml` — the mandate: what it may do alone, what needs approval, what it must never do, which clocks it watches. Every rule has an id and a source.
- `agent/playbooks/*/SKILL.md` — how it works each case type (Agent Skills format; five playbooks).
- `agent/tools.yaml` — the tool manifest: read or write, idempotency, which authority a write needs, what the side effect is.
- the record contract in `harness/schema.py` — what it must leave behind: disposition, facts with sources, actions with status, promises, clocks, and a handover card when a human must decide.

The model and the loop are swappable. Playbooks say *how*; the rulebook says *whether*; a playbook cannot grant authority.

The case that shows it best is public case 050, a broken window, cut at the landlord's reply "yes please send someone". The agent read the approval from the history instead of asking again, instructed a glazier within the £250 standing cap under CAP-DISPATCH-ROUTINE, raised the urgency to urgent for the security risk, briefed the tenant and the landlord, and held the ticket for the tenant's access windows with a dated chase. Its record opens with the status block (stage visit_scheduling, next step: tenant to reply with two windows) and a checklist showing three of nine closing steps done, each citing the event or action that did it.

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
- **Review before done.** A deterministic reviewer (rules R1–R7) checks the record against the action log and can downgrade `resolved` to `needs_info` or `escalated`; an LLM review pass is available with `LOA_REVIEWER=llm`.

The Vision this serves, the structural domains, and the split between invariants and implementations are written up in VAST form in [`docs/VAST.md`](docs/VAST.md).
The system the agent lives inside (the ticket with its event stream, stages and hold, status block and definition of done; the four roles; the property, tenancy, quote and visit models) is in [`docs/system-design.md`](docs/system-design.md), with what is implemented today against what is designed.

Directory map: `harness/` runtime · `agent/` the agent definition · `mockworld/` test environment · `fixtures/` synthetic cases · `evalkit/` mutations, judge, reports and the case-corpus extractor · `tests/` · `ANSWERS/` Reality Test output · `data/` structured index of the organisers' public cases · `docs/` cheat-sheets, analysis and prompts · `video/` · `posts/`.

The organisers' 50 public Property Management cases are analysed in [`docs/pm-cases-analysis.md`](docs/pm-cases-analysis.md) (corpus shape, taxonomy, the agency's workflow as it actually runs, where humans step in, traps for an automated agent, vocabulary for playbooks) with a one-page [`docs/pm-cases-cheatsheet.md`](docs/pm-cases-cheatsheet.md). Both are written from `data/pm-cases-index.json`, rebuilt with `make pm-index`.

The organisers' environment was adapted as files: `harness/adapters/dwelly.py` reads each case folder into artefacts with trust classes, hides the outcome, cuts the history at a decision point for our own evaluation, exposes read tools over the case and records write tools in a ledger with receipts. `harness/adapters/generic.py` (a tools module plus `agent/tools.yaml`) and `mockworld/` are the other two adapters; the harness does not know which one it is running against.

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
make sim-list                   # multi-actor scenarios (evalkit/actors/scenarios.yaml)
make sim SC=SC-01,SC-04         # play selected scenarios against the agent, graded, to the console
make sim-all                    # play every scenario (ARGS="--concurrency 4 -v" for more)
make rehearse                   # fresh clone → setup → run → verify
make mutate CASE=fixtures/F01-routine-tap   # adversarial variants along the Reality-Test axes
make rules-extract DOCS=<dir>   # environment documents → candidate rules in agent/rulebook_staging.md
make capacity N=20 C=4          # wall-time estimate for a batch
make video-check                # demo video ≤ 60 s
make secrets-scan               # gitleaks over the repository
```

Configuration lives in `.env` (see `.env.example`): model, effort, concurrency, per-case timeout, step cap, retry budget, token budget per minute.

### Running the multi-actor simulation

The simulator plays the scenarios in `evalkit/actors/scenarios.yaml` against the agent, with a tenant, landlord and contractor (`evalkit/actors/*.yaml`) replying in character between agent runs. A judge model then grades each episode against the scenario's checks and end state. Output goes to the console. The director and judge are models, so treat a verdict as evidence to read, not ground truth. It needs `ANTHROPIC_API_KEY` in `.env`.

```
make sim-list                                  # list the scenarios
make sim SC=SC-01                              # one scenario
make sim SC=SC-01,SC-04                        # several (comma-separated; "1" also means SC-01)
make sim SC=SC-02 ARGS="-v"                    # full message bodies and director notes
make sim-all ARGS="--concurrency 4"            # every scenario, four in parallel
```

The same commands without `make`:

```
uv run python -m harness.cli sim --list
uv run python -m harness.cli sim --scenario SC-01 --scenario SC-04 --max-ticks 8
uv run python -m harness.cli sim --all --sim-model claude-opus-5 --sim-effort medium --no-judge
```

Options (pass them through `ARGS="..."` with `make`):

- `--max-ticks N` — agent runs per scenario (default 10).
- `--concurrency N` — scenarios in parallel (default 2).
- `--model`, `--effort` — the agent's model and effort.
- `--sim-model`, `--sim-effort` — the director and judge model (defaults: the agent's model, effort `medium`).
- `--timeout`, `--max-steps`, `--reviewer rules|llm` — per-tick agent limits and reviewer, as for `run`.
- `--no-judge` — play the episodes without grading.
- `--verbose` / `-v` — full message bodies and director notes.
- `--scenarios PATH` — an alternative scenario file.

### How the Reality Test was run

<!-- TODO(event): exact command, start/end times, model id, concurrency, the runner's summary line, and the commit hash of the frozen code. -->

```
make freeze                     # tag freeze-1630, record the hash
git -C ../HackatonPublicCases pull                     # the Reality Test cases arrive at 16:30
ls "../HackatonPublicCases/HackatonChallendges/Property Management"   # expect NNN/ folders with index.md + history.md
make run ARGS="--adapter dwelly --id-style number --concurrency 6" \
  CASES="../HackatonPublicCases/HackatonChallendges/Property Management" OUT=ANSWERS
```

The same adapter and flags produced every number below; `--id-style number` writes `ANSWERS/<case number>/`.

### Results on the organisers' public cases

Protocol: all 50 public Property Management cases, each cut at the first message from an outside party
(`--auto-cutoff first-external`), with the overview, outcome and status hidden from the agent and handed only to the
judge (`--emit-expected`). The judge is a model (`claude-opus-5`, effort medium) scoring outcome and
judgement & safety 0–2 against the hidden outcome, with critical failures and prohibited actions as separate flags; a
model's verdict is evidence to read, not ground truth. Concurrency 6, about 16 minutes per full run.

| Run (10 October) | Records | Outcome | Judgement & safety | Critical / prohibited | needs_info · escalated · resolved |
|---|---|---|---|---|---|
| Morning, before tuning | 50/50 | 91/100 | 98/100 | 0 / 0 | 38 · 10 · 2 |
| Final (13:00) | 50/50 | 94/100 | 99/100 | 0 / 0 | 45 · 4 · 1 |

Between the two: the status block and the definition of done in every record, workflow stages and hold reasons as
mandate data, reviewer rule R8 (a case on hold is not resolved), landlord replies treated as authority for landlord-owned
decisions, a priced quote routed to the landlord before work starts, attachments gated by the decision point, a time
budget inside the loop. The 11 cases the morning judge scored lowest went 13 → 18 of 22 across the day's three passes.
Six cases still score 1 on outcome, all "defensible alternative": the agent asks or holds where the agency went ahead.
The corpus itself is described in [`docs/pm-cases-analysis.md`](docs/pm-cases-analysis.md); every record of every run
can be replayed step by step with `make cases-browser RUNS="runs/<run>"`.

Output per case: `ANSWERS/<case-id>/ANSWER.md`, `REASONING.md`, `trace.jsonl`, `_state.json`; run metadata in `ANSWERS/_run.json`. Cases that hit the timeout or an unrecoverable error still produce a record: an escalation with the state so far and a system note explaining why.

## 5. Models, APIs and external services

- Anthropic Claude via the official Python SDK (`anthropic`), Messages API with tool use, adaptive thinking and prompt caching. Model `claude-opus-5`, effort `high` (`LOA_MODEL`, `LOA_EFFORT`); the judge and the simulator's director use the same model at effort `medium`.
- The organisers' environment is files, not tools: a case is `index.md` (details, initial request, attachments list), `history.md` (every event with channel, from, to, time) and `attachments/`. The Dwelly adapter (`harness/adapters/dwelly.py`) turns them into artefacts with trust classes, offers read tools over them (`get_case_details`, `search_history`, `get_attachment`, `get_action_ledger`) and records write tools in a ledger with receipts (`assign_contractor`, `request_landlord_approval`, `notify_*`, `schedule_access`, `put_on_hold`, `add_note`, `create_human_task`, `close_request`). Nothing is sent anywhere.
- No speech-to-text was used: the corpus carries calls as written third-person summaries.
- Python packages: `pydantic`, `pyyaml`, `rich`, `pypdf`. No other services.

API keys are read from the environment and never committed; a pre-commit secret scan (gitleaks) and log redaction guard the traces.

## 6. Important assumptions

- The rulebook priors (`SRC-PRIORS`) reflect common UK lettings practice: a standing spend cap for routine repairs, landlord approval above it, emergency safety duties that override the cap, 24 hours' notice for access, statutory gas and electrical checks. Environment documents override priors where they were merged (`SRC-ENV`).
- Clocks are labelled by status. `in_force` rules cite statute; `sop` rules come from the environment; `proposed` rules (for example Awaab's Law for private tenancies, at consultation stage as of 9 October 2026) are reference points, not deadlines.
- Deciding that a repair is tenant-payable, sending legal correspondence, changing payment details and moving money are human decisions by construction.
- Every case ends with a record even when the model or a tool fails; a fallback escalation is a floor, not a score.

Forced by the environment:

- A case is one ticket at one decision point: the history as given is everything the agent may know. In our own
  evaluation the decision point is a cutoff in the public history; in the Reality Test it is the case as delivered.
- Writes are recorded, not executed: a `completed` action means the ledger accepted it with a receipt, not that an
  email left or a contractor was booked. The record says so in its execution notes.
- The agency's own events (`Agency / system`, `Northbridge Lettings`) are informational; every outside party is
  untrusted content. Names are inconsistent between events, so parties are resolved by role.
- No landlord instruction record exists in this environment, so there is no standing spend authority: a non-emergency
  dispatch needs the landlord's own approval in the visible history, cited by event id and checked by the environment,
  or it becomes a request to the landlord. A prior (a typical £250 cap) is never treated as a mandate.
- Under a cutoff an attachment is visible only once the visible history carries it (the agency's own file link, or an
  outside party's attachment-only email); the public corpus dates every document after its case.

## 7. Known limitations

- The gate enforces only what the rulebook can express (amounts, urgency, consent fields, approver). Nuanced policy stays with the reviewer pass and the human.
- Cross-case memory is per run only; no persistent learning.
- Voice is input only: transcripts are evidence ranked below documents and records.
- The mock world is a test fixture, not a model of any real operator.

On the day:

- One of fifty cases hit the 240-second budget and left an empty fallback record (found at 12:30, fixed: a time
  budget inside the loop, the live state kept on timeout, 360 seconds by default).
- Two records carried a stray tool-call tag in the decision text (fixed in the sanitiser).
- `make run` split a cases path with a space into two arguments; the Reality Test command would have failed (fixed).
- Not built: the Dispatcher's "which ticket does this message belong to" decision, a running Supervisor over live
  tickets, a structured resolution-and-payer object, tenancy and appliance models (`docs/system-design.md` §5).
- The multi-actor simulator (`make sim`) is a development instrument: its director and judge are models, and its
  scenarios' end states are still being calibrated against the agent's conservative dispositions.

## 8. What we would build next

- Delivered handovers: push the decision card into a real human queue with acknowledgement and re-escalation, and measure human minutes per exception.
- Cross-case ledger across runs: duplicates, conflicts and learned landlord preferences with provenance.
- Playbook compilation from an acquired agency's own SOPs as a repeatable process, with the staging review as the control point.
- Paired evaluations for every escalation trigger: a case that must escalate next to a similar case that must be completed, so caution cannot masquerade as judgement.
