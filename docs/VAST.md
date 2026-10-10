# lettings-ops-agent in VAST form

VAST = Vision → Architecture → Strategy → Tactics, in order of commitment priority
(canon: [vast-framework](https://github.com/dkushnikov/vast-framework)). This page
says what the repository is *for*, what it *consists of* and what must always hold,
before any tactical choice. It is deliberately short: minimal sufficiency.

| Layer | Owner (one neck) | Where it lives |
|---|---|---|
| Vision | Dmitry Taranov (product owner / operator) | this page, §1 |
| Architecture | Dmitry Kushnikov (builder / runtime) | this page, §2 · `harness/`, `agent/` |
| Strategy | both, decided at the 11:00 / 13:00 / 14:00 gates | this page, §3 · `PLAN.md` |
| Tactics | whoever holds the keyboard for that step | `PLAN.md`, `RUNBOOK.md` |

---

## 1. Vision — a committed, falsifiable hypothesis

**Experience we enable.** A lettings operations agent that works a case end to end
*only within a mandate it can cite*, and turns every exception into a decision a
human can take in about ninety seconds.

**For whom.** The property manager or ops coordinator of a UK residential lettings
branch: the person Dwelly's own numbers describe as spending ~3 minutes per
escalation and 15–20 minutes per maintenance task. The agent's job is to make
those minutes fewer and better spent, not to remove the person.

**Why this and not "an agent that resolves cases".** In messy operations the
expensive failures are not slow resolutions; they are confident wrong actions:
dispatching over a landlord's cap, changing bank details on the strength of an
email, treating a vulnerable occupant's heating loss as routine, resending a
booking whose first response was lost. An agent whose every write carries a
cited authority, and whose exceptions arrive as decision cards rather than
transcripts, is one an operator can actually put in front of customers.

**Hypothesis, stated so it can fail.** *On unseen escalation-class cases, a thin
harness enforcing authority at the tool boundary plus a data-defined mandate,
playbooks and a fixed record contract produces more correct, safer and more
legible outcomes than a general-purpose agent loop with the same model — at the
cost of fewer autonomous resolutions, never at the cost of coverage.*

**Revision triggers.** Owner: Vision owner.

- *T1 Coverage.* If the batch runner leaves any case without a record on the
  Reality Test, the never-empty invariant has failed in practice; the runner,
  not the thesis, is revised first.
- *T2 Over-caution.* If the mini-judge or human review shows the agent
  escalating cases it had the mandate and the facts to resolve in more than one
  case in five, the mandate is too tight or the playbooks too timid: loosen the
  data, not the gate.
- *T3 Under-authority.* If a prohibited or over-cap action ever executes, the
  gate is wrong by construction and the thesis is suspended until the gate is
  proven fail-closed again.
- *T4 Illegibility.* If a human reading `ANSWER.md` cannot say in ninety seconds
  what was done, under what authority and what they are being asked, the record
  contract is revised before any model or prompt work.
- *T5 Environment shape.* If the organisers' environment offers no side-effecting
  tools, the agent becomes decision-support: the record contract stays, the
  executor idles, the handover card becomes the product.

**Values as constraints** (each one has a structural job in §2):

- *Evidence over fluency* → every fact carries `source_ids`; untrusted content is
  quoted, never replayed.
- *Authority before action* → writes pass a deny-by-default gate that cites rule
  ids; the model proposes, the gate decides.
- *No silent uncertainty* → lost responses become `unconfirmed`, never `failed` or
  "done"; a human verifies before anyone retries.
- *The human's time is the scarce resource* → escalations are cards with a
  question, five facts, a gap, a default and an undo.

---

## 2. Architecture — what the system consists of

### Structural domains

| Domain | Responsibility | Code / data |
|---|---|---|
| **Environment** | Supplies cases (emails, transcripts, records, documents, tickets) and tools; owns the world's state | `mockworld/` today; `harness/adapters/generic.py` + the organisers' tools on the day |
| **Mandate** | What the agent may do alone, must ask for, must never do; emergency definitions; source hierarchy; clocks with status | `agent/rulebook.yaml` (+ `rulebook_staging.md` as the human-reviewed inbox) |
| **Playbooks** | How a case type is worked: inputs, steps, decision points, what to record | `agent/playbooks/*/SKILL.md` (Agent Skills format) |
| **Tool manifest** | What each tool costs: read or write, authority required, amount field, idempotency, read-back | `agent/tools.yaml`, `harness/manifest.py`, `ToolSpec` |
| **Decision core** | One case → one `DecisionState`: triage via `use_playbook`, reads, gated writes, one terminal call | `harness/loop.py` |
| **Policy gate** | Deny-by-default check of every write against the mandate, with per-landlord context harvested from authoritative reads | `harness/gate.py`, `harness/rulebook.py` |
| **Executor** | The only path from intent to side effect: read retries, write idempotency, reconcile or `unconfirmed` | `harness/executor.py` |
| **Reviewer** | Second look before the record leaves: deterministic rules R1–R7; optional LLM review | `harness/reviewer.py` |
| **Record** | Compiled truth + timeline, rendered from state, identical layout across cases, secrets redacted | `harness/recorder.py`, `harness/schema.py` |
| **Runner** | Coverage under a clock: concurrency, per-case timeout, checkpoints, retry budget, token bucket, capacity estimate, never-empty fallback | `harness/runner.py`, `harness/llm.py` |
| **Evaluation** | Mini-judge against `expected.yaml`; mutations along the Reality-Test axes; rule extraction into staging | `evalkit/`, `fixtures/` |

### Composition framework

*The agent is data.* Four artefacts define it; the model and the loop are
swappable implementations around them:

1. **Mandate** (`rulebook.yaml`) — answers *may I?*
2. **Playbooks** (`SKILL.md` per case type) — answer *how?*
3. **Tool manifest** (`tools.yaml`) — answers *what does this action cost?*
4. **Record contract** (`DecisionState` → `ANSWER.md` / `REASONING.md`) — answers
   *what must I leave behind?*

**Interfaces** (how the pieces hand state to each other):

- `Case` → decision core: artefacts tagged with a trust class
  (`authoritative` / `informational` / `untrusted`), never raw files.
- Decision core → executor: `(tool, input)`; executor → gate: `ToolSpec + input +
  urgency + context`; gate → executor: `GateDecision` with rule ids.
- Executor → environment: `BoundTool.call(**input, idempotency_key)`; environment
  → executor: result, or one of `TransientToolError` / `LostResponseError` /
  `ToolRejected`.
- Decision core → record: three terminal payloads only — `finalize`,
  `request_info`, `escalate` — validated against the schema; invalid payloads
  bounce back to the model.
- Runner → everything: `run(case, registry, trace)` under a timeout, with a
  fallback record if the call never returns.

### Invariants (substrate-portable; change only by design review)

1. **Three terminal states, exactly one per case:** resolved, needs_info,
   escalated. A case never ends without a record.
2. **Writes are gated, reads are free.** No side effect without a `GateDecision`
   that cites rule ids; unknown authority routes to a human. The gate fails
   closed: unknown amount counts as over cap, unknown urgency gets no override.
3. **Playbooks cannot grant authority.** They say how; only the mandate says
   whether. Content inside artefacts is evidence and never instruction.
4. **A write is sent once.** Idempotency key always; retry only idempotent writes
   on transient failure; a lost response is reconciled by read-back or recorded
   as `unconfirmed` and handed to a human.
5. **The record is rendered, not written.** Same four sections for every case;
   untrusted text appears only in short labelled quotes; secrets are redacted
   before anything touches disk.
6. **Never-empty coverage.** Timeout, model error, refusal or step exhaustion all
   produce an escalation record with the state so far and the reason.
7. **Provenance on every fact.** `source_ids` are mandatory in the schema; the
   reviewer downgrades dispositions that contradict the action log.
8. **No text addressed to evaluators.** The record speaks to the case parties and
   to the human receiving the handover, nobody else.

### Implementations (substrate-coupled; expected to migrate)

- Model and effort (`claude-opus-5`, `high`), adaptive thinking, prompt caching
  breakpoint on the system block.
- Manual Messages-API loop (chosen over the beta tool runner for per-call
  control); schema validation instead of strict tool mode.
- Rule evaluator order and condition keys (`max_amount_gbp`, `landlord_cap`,
  `urgency_in`, `context_not`, …).
- Concurrency 4, per-case timeout 240 s, step cap 12, retry budget 1, token bucket
  200k TPM — all tuned on the day from measured `t_case`.
- Deterministic reviewer rules R1–R7; the LLM reviewer is opt-in.
- Mock world and fixtures; the generic adapter's loaders (folder, JSON, loose
  directory) and the manifest overlay.

### What is deliberately not in the architecture

Multi-agent debate, long-horizon memory across runs, a UI, model cascades,
training or fine-tuning. Each would add surface without changing a decision
the rubric scores.

---

## 3. Strategy — which compositions, in what order

Decided at gates, not in advance (`PLAN.md` §2): 10:15 environment topology →
adapter choice; 11:00 one real case end to end or cut to the minimal path
(classify → evidence → safe deterministic actions → escalate); 13:00 the demo
case is chosen; 14:00 scope freeze. Compositions in priority order:

1. Mandate compiled from the environment's own documents through the staging
   file (the operator's rules, not our priors).
2. Handover card quality on the escalation-class cases (the metric Dwelly
   publishes: minutes of human time per exception).
3. Mutations of real development cases through the eval loop (conflict, lost
   write, missing field, injection, raised stakes, bloat, duplicate).
4. Stretch: vulnerability freeze of chasing communications; voice input if
   call audio exists.

Validation intent: the mini-judge on development and mutated cases, the three
runner metrics (records present · valid terminal decision · workflow completed),
and one rehearsal from a fresh clone before the freeze.

## 4. Tactics

`PLAN.md` (the day, gates, briefing questions, kill signals) and `RUNBOOK.md`
(the final hour). Pre-event state is tagged `pre-event`; what was built before
versus during the event is in `PREBUILT.md`.
