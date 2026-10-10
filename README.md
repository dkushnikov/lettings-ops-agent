# lettings-ops-agent

An operations agent for UK residential lettings. It acts only where its rules allow, and hands every exception to a human as a decision they can make in about 90 seconds.

Built by team D&D (Dmitry Kushnikov and Dmitry Taranov) for the Real-World Agents Hackathon, London, 10 October 2026, Property Management track. Licensed under Apache 2.0 (`LICENSE`). What existed before the event is listed in `PREBUILT.md` (tag `pre-event`).

The organisers gave us files, not tools: tickets from one lettings agency. Each ticket has an `index.md`, a `history.md` of timed events (emails, SMS, call summaries, the agency's own updates) and attachments. The Reality Test delivers more tickets in the same format.

## 1. What we built

An agent for the maintenance desk of a residential lettings agency. It works each ticket the way a careful property manager would: reads what tenants, landlords and contractors sent, does what it is allowed to do on its own, and asks the right person when a decision is theirs. A companion browser demo, Lettings Village (https://github.com/dkushnikov/dwelly-hackaton-demo), is a pixel village where tenants, landlords, contractors and Dwelly operators share six homes; it drives this same agent and shows every decision with its evidence, policy gate, next owner and handover.

There are three actors besides the agent: landlord, tenant and contractor. The agent works each ticket for them. It reads the messages, calls and documents, does what it is allowed to do on its own, and asks the right person when a decision is theirs. A simulator plays all three actors (`evalkit/actors/`), so we can test the agent in multi-turn conversations, not just on single snapshots.

The agent is defined by four files, not code:

- `agent/rulebook.yaml`: what the agent may do alone, what needs approval, what it must never do, and which deadlines it watches. Every rule has an id and a source.
- `agent/playbooks/*/SKILL.md`: how to handle each type of case (five playbooks, in Agent Skills format).
- `agent/tools.yaml`: the list of tools, whether each one reads or writes, and what authority a write needs.
- `harness/schema.py`: what the agent must leave behind for each case: the outcome, facts with sources, actions taken, promises, deadlines, and a handover card when a human must decide.

Playbooks say *how* to do something; the rulebook says *whether* the agent may. A playbook cannot grant permission. The model and the loop can be swapped.

Example: public case 050, a broken window, at the point where the landlord replies "yes please send someone". The agent took that reply as approval instead of asking again. It sent a glazier on that approval, citing the landlord's event (CAP-DISPATCH-APPROVED), raised the urgency because the flat was not secure, updated the tenant and the landlord, and put the ticket on hold until the tenant offers access times, with a date to chase. The record shows the current stage, the next step, and three of nine closing steps done, each linked to the event that did it.

An escalation is a 90-second decision for a person, not a shrug. From public case 018 in the final run (a gardening job the agency told the landlord was done, with nothing on file): **Question:** was the work actually carried out, and who authorises offsetting its cost against the rent? **Gap:** no evidence of the visit, no cost figure, no invoice, no landlord approval of any amount; the landlord's reply is a thanks whose signature does not match the landlord record. **Options:** verify with the tenant and the contractor and, if the work was done, obtain the invoice and forward it; if not, correct the record with the landlord and reassign; if the garden is communal, refer to block management and close without payment. **Recommended:** verify first; no rent offset until an invoice exists. **If nobody answers:** the case stays on hold and the job is reassigned after two working days.

## 2. What operational problem it solves

Property management tools have two problems:

- **They are outdated, clunky and need manual input.** Someone has to read every email, copy it into a CRM, chase every party and remember every deadline. Most landlords, tenants and contractors are not technical.
- **They are reactive.** They only act on what someone types in. Nothing happens until a person notices a problem and logs it, so a missed reply or an expired certificate stays hidden until it becomes a complaint.

Our system is proactive and visual. The agent reads incoming messages itself, tracks deadlines (access notice, landlord approval, safety checks), chases people when a deadline passes, and books routine repairs within the landlord's limit without being asked. The game interface shows every property in a way anyone can read.

Most of a property manager's day goes on exceptions, not routine work: a record that contradicts an email, a contractor who didn't turn up, a repair that costs more than the landlord allowed. The hard part is not acting, it is knowing when *not* to act and handing over cleanly. So the agent is built to explain every action with the rule and evidence behind it, and to keep the human's time per exception short.

## 3. Architecture

The browser demo is a view over the same records: it runs the agent through the harness contract (an environment adapter with `load_cases` and `tools_for`, the record files it writes back) and renders each decision as a story. Nothing in this repository depends on it.

To deploy against a real ticket system, implement `build_registry(case)` for its API in a module the generic adapter loads (`harness/adapters/generic.py`); `agent/tools.yaml` annotates each tool for the gate (read or write, the authority a write needs, the amount field). The gate, rulebook, reviewer and recorder are unchanged, and writes stay deny-by-default until the rulebook grants them. In the hackathon environment writes go to a per-case ledger; every record says so under its header.

```
case files ──► loader ──► decision loop (Anthropic Messages API)
                              │  read tools: always allowed
                              │  write tools ──► policy gate ──► executor ──► tool
                              │                  (rulebook)      (no duplicate writes)
                              ▼
                       finish: finalize | request_info | escalate
                              │
                       reviewer (checks the record against the rulebook)
                              │
                       recorder ──► ANSWER.md · REASONING.md · trace.jsonl

batch runner: parallel cases, timeouts, retries, rate limiting, a record even on failure
```

How it is built:

- **Permissions live outside the model.** Every write tool goes through a gate. By default it is denied; it is allowed only when a rulebook rule matches (spend limit, urgency, consent). Otherwise it needs approval or is escalated, always citing the rule. Text inside a case is treated as evidence, never as an instruction.
- **No double bookings.** Reads can be retried. Each write has an idempotency key; if the response is lost, the agent checks what happened instead of sending it again.
- **Every case ends in one of three states:** `resolved`, `needs_info` or `escalated`. There is a step limit per case; anything unfinished becomes an escalation with context.
- **Two outputs per case.** `ANSWER.md` is the decision with its evidence and authority. `REASONING.md` is the full step-by-step trace.
- **A reviewer checks the work.** Rules R1–R11 (and R3a) compare the record with what actually happened, and can downgrade `resolved` to `needs_info` or `escalated`. An LLM reviewer is available with `LOA_REVIEWER=llm`.

The adapter `harness/adapters/dwelly.py` reads the organisers' case folders, hides the real outcome, can cut the history at a chosen point for our own testing, and records write tools in a ledger instead of sending anything. Two other adapters (`harness/adapters/generic.py` and `mockworld/`) plug into the same harness.

Folders: `harness/` runtime · `agent/` agent definition · `mockworld/` test environment · `fixtures/` synthetic cases · `evalkit/` simulator, judge, reports · `tests/` · `ANSWERS/` Reality Test output · `data/` index of the public cases · `docs/` design and analysis · `video/` · `posts/`.

More detail:

- [`docs/system-design.md`](docs/system-design.md): tickets, stages, roles and data models, and what is built versus designed.
- [`docs/VAST.md`](docs/VAST.md): vision and architecture principles.
- [`docs/pm-cases-analysis.md`](docs/pm-cases-analysis.md) and [`docs/pm-cases-cheatsheet.md`](docs/pm-cases-cheatsheet.md): analysis of the organisers' 50 public cases (rebuild with `make pm-index`).

## 4. How to run it

### The browser demo

Lettings Village lives in its own repository (https://github.com/dkushnikov/dwelly-hackaton-demo): Python 3.12 and `uvicorn`, no npm dependencies, quick start in its README. It loads this repository's agent through the harness contract.

### The agent

You need Python 3.12, [uv](https://docs.astral.sh/uv/), an Anthropic API key, and `git-lfs` for the video.

```
git clone https://github.com/dkushnikov/lettings-ops-agent
cd lettings-ops-agent
cp .env.example .env            # add ANTHROPIC_API_KEY
make setup                      # install dependencies
make check                      # lint + tests
make demo                       # one synthetic case end to end
make run CASES=fixtures OUT=runs/dev   # process cases, write records
make eval                       # score records against expected results
```

Other commands:

```
make sim-list                   # list multi-actor scenarios
make sim SC=SC-01,SC-04         # play chosen scenarios against the agent
make sim-all                    # play every scenario
make board                      # one HTML page over every run under runs/ (case runs and sim episodes)
make rehearse                   # fresh clone → setup → run → verify
make mutate CASE=fixtures/F01-routine-tap   # generate harder variants of a case
make rules-extract DOCS=<dir>   # draft rules from an agency's documents
make capacity N=20 C=4          # estimate run time for a batch
make video-check                # check the demo video is ≤ 60 s
make secrets-scan               # scan the repo for secrets
```

Settings (model, effort, concurrency, timeouts, limits) live in `.env`; see `.env.example`.

### Multi-actor simulation

The simulator plays the scenarios in `evalkit/actors/scenarios.yaml`. A tenant, landlord and contractor reply in character between agent runs, then a judge model grades each episode. Results print to the console and go to `runs/sim/<timestamp>/` (`summary.json` plus one JSON per episode: the transcript, the agent's records, the grade); `make board` builds one HTML page over every run. The actors and the judge are models, so read a verdict as evidence, not as ground truth.

```
make sim SC=SC-01                       # one scenario ("1" also works)
make sim SC=SC-02 ARGS="-v"             # show full messages
make sim-all ARGS="--concurrency 4"     # all scenarios, four at a time
```

Without `make`: `uv run python -m harness.cli sim --scenario SC-01 --max-ticks 8`.

Options (pass with `ARGS="..."`):

- `--max-ticks N`: agent runs per scenario (default 10).
- `--concurrency N`: scenarios in parallel (default 2).
- `--model`, `--effort`: the agent's model and effort.
- `--sim-model`, `--sim-effort`: the actors' and judge's model (default: the agent's model, effort `medium`).
- `--timeout`, `--max-steps`, `--reviewer rules|llm`: limits and reviewer for each agent run.
- `--no-judge`: skip grading.
- `-v`: full messages and actor notes.
- `--scenarios PATH`: use a different scenario file.
- `--out DIR`: where the episode files go (default `runs/sim/<YYYYMMDD-HHMMSS>`); `--list` writes nothing.

### Reality Test

<!-- TODO(event): exact command, start/end times, model id, concurrency, the runner's summary line, and the commit hash of the frozen code. -->

```
make freeze                     # tag freeze-1630, record the hash
git -C ../HackatonPublicCases pull      # Reality Test cases arrive at 16:30
make run ARGS="--adapter dwelly --id-style number --concurrency 6 --deadline 16:52" \
  CASES="../HackatonPublicCases/Property Management" OUT=ANSWERS
```

Each case gets `ANSWERS/<case number>/ANSWER.md`, `REASONING.md`, `trace.jsonl` and `_state.json`; run details are in `ANSWERS/_run.json`. A case that times out or fails still gets a record: an escalation with what was done so far and why it stopped.

### Results on the 50 public cases

Each case was cut at the first message from an outside party. The agent did not see the real outcome; only the judge did. The judge (`claude-opus-5`, effort medium) scored outcome and judgement & safety from 0 to 2 per case, and flagged critical failures and prohibited actions. A full run takes about 16 minutes at concurrency 6.

| Run (10 October) | Records | Outcome | Judgement & safety | Critical / prohibited | needs_info · escalated · resolved |
|---|---|---|---|---|---|
| Morning, before tuning | 50/50 | 91/100 | 98/100 | 0 / 0 | 38 · 10 · 2 |
| Midday (13:00) | 50/50 | 94/100 | 99/100 | 0 / 0 | 45 · 4 · 1 |
| Final (15:00) | 50/50 | 94/100 | 100/100 | 0 / 0 | 48 · 1 · 1 |

What changed between the runs: a status block and closing checklist in every record, a reviewer rule that a case on hold is not resolved, landlord replies treated as approval, priced quotes sent to the landlord before work starts, a time budget inside the loop; then no standing spend without a limit on file, a landlord's approval as a verifiable event, an emergency make-safe ceiling, a safety pass over the case material, and a reviewer that treats a safety keyword as a finding rather than an escalation. Six cases still score 1 on outcome; in all of them the agent asks or waits where the agency went ahead. The judge's noise is about one point per case, so a two-point difference between runs is not a signal.

Provenance: these are our own judge's scores (`evalkit/judge.py`, `claude-opus-5` at effort medium) on the 50 public cases the agent was tuned on; read them as a regression signal, not a benchmark. `needs_info` is the correct wait on a named party (usually the landlord's approval or a tenant's access window) with the next step and a chase date in the record, not a give-up; under a cutoff most public cases are mid-flight, so most records end there. A judge built separately from this repository, with its own rubric and 38 unseen mutated cases (core, hard and nightmare sets), scored the agent 94.3 at `1acac37` against 75.8 for a plain `claude-opus-5` baseline: 38 of 38 cases above 50, no critical or prohibited failures, no fallbacks, 842 s of wall time at concurrency 6. Its three lowest cases (70–78) are a contractor chase without a reply-by time, partial first-line advice for a drain, and one whose disposition label the judge itself flips between runs. Replay any run step by step with `make cases-browser RUNS="runs/<run>"`.

## 5. Models, APIs and external services used

- **Anthropic Claude** through the official Python SDK (`anthropic`): Messages API with tool use, adaptive thinking and prompt caching. The agent uses `claude-opus-5` at effort `high` (`LOA_MODEL`, `LOA_EFFORT`); the judge and the simulated actors use the same model at effort `medium`.
- **The organisers' case files.** The adapter gives the agent read tools (`get_case_details`, `search_history`, `get_attachment`, `get_action_ledger`) and write tools (`assign_contractor`, `request_landlord_approval`, `notify_*`, `schedule_access`, `put_on_hold`, `add_note`, `create_human_task`, `close_request`). Writes go into a ledger; nothing is actually sent.
- **No speech-to-text:** calls arrive as written summaries.
- **Python packages:** `pydantic`, `pyyaml`, `rich`, `pypdf`. No other services.

API keys come from the environment and are never committed. A pre-commit secret scan (gitleaks) and log redaction protect the traces.

## 6. Key assumptions

- Landlords, tenants and contractors are not technical and won't learn a CRM. The interface has to explain itself.
- The default rules follow common UK lettings practice: a standing spend limit for routine repairs, landlord approval above it, emergency safety work that overrides the limit, 24 hours' notice for access, and statutory gas and electrical checks. An agency's own documents override these defaults.
- Every deadline is labelled: law in force, agency procedure, or proposed law (for example Awaab's Law for private tenancies, still in consultation as of 9 October 2026). Proposed rules are guidance, not deadlines.
- Some decisions are always human: whether the tenant pays for a repair, legal letters, changing payment details and moving money.
- Every case ends with a record, even when the model or a tool fails.

Assumptions forced by the environment:

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

- Emergency authority covers making safe (attendance, isolation, temporary heaters, boarding, a locksmith) up to £250 without approval; the repair above that is put to the on-call manager or the landlord at once. Before a case can end as resolved, a deterministic safety pass checks every document and message for safety words the record did not address.

## 7. Known limitations

Open findings are kept in [`docs/findings.md`](docs/findings.md) with their state; the ones that matter most:

- A landlord's cited approval is verified for provenance (the event exists and the landlord wrote it), not for consent:
  what it approves, for how much, and whether a later message withdrew it is the model's reading, cited in the record
  for a person to check.
- An emergency dispatch rests on the model's own urgency assessment; the reviewer therefore escalates every emergency
  dispatch for a person to confirm.

- The gate can only enforce what the rulebook can express (amounts, urgency, consent, approver). Subtler policy is left to the reviewer and the human.
- No memory between runs, and no learning over time.
- The agent is proactive inside a ticket, but nothing yet watches all live tickets in the background.
- Not built yet: matching an incoming message to the right ticket, a structured record of who pays, and tenancy and appliance models (see `docs/system-design.md` §5).
- The simulator is a development tool. Its actors and judge are models, and its scenarios are still being tuned.

Found and fixed on the day:

- One of 50 cases hit the 240-second limit and left an empty record. Fixed with a time budget inside the loop and a 540-second default (six slow steps fit).
- Two records contained a stray tool-call tag. Fixed in the text sanitiser.
- `make run` broke on a case path containing a space, which would have failed the Reality Test. Fixed.

## 8. What we'd build next

- **Contractor ratings across landlords.** Every job a contractor does for any landlord feeds one shared rating, so a landlord can pick a reliable contractor they have never used.
- **Live contractor tracking.** Show the contractor moving towards the property on a map, like an Amazon or Deliveroo courier, so the tenant and landlord know when they will arrive.
- **Adding new properties.** A simple screen to add a property to the portfolio, with an estimated cost.
