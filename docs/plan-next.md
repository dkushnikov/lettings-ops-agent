# Plan after the hackathon (v2)

Written 10 October 2026, 15:00, during the event. Version 1 was six workstreams in a fixed order; this version is what
survived a review by a three-model council (deliberative mode: three independent reads, then anonymised cross-critique)
against the constraints below. Milestones are gated on evidence, not dated: two people, part-time.

Constraints the plan is built on: external systems arrive later (ticket system, CRM for landlords, tenants and
properties, vendor management, payments and accounting) and the agent never moves money; the evaluation assets stay
(model judge over the public cases, mutations, the multi-actor simulator, the findings log, the runs board); the demo
emulation (mock world and the browser village) stays as a second environment; UK lettings: tenant data is personal
data and the agency is the controller; the agent's knowledge stays data the agency can edit, never code.

## What the review changed

- **Authority before continuity.** Version 1 built the long-lived ticket session (re-entry, wake-ups, a supervisor
  sweep) before identity and approval binding. Re-entry amplifies whatever is in the record, so a minimal trust
  envelope comes first: who sent this, who is the landlord of record, what exactly was approved, is it still valid at the
  moment of execution.
- **The harness owns its state.** "The ticket system is the memory" was wrong. Execution state (the decision record,
  pending actions, receipts, wake-ups, the event cursor) lives in the harness's own store with a versioned schema; the
  ticket system is transport and a projection (custom fields, an internal note). `_state.json` is a checkpoint of that
  store, not the truth.
- **Memory is hybrid.** Ticket-scoped facts are written continuously and affect only that ticket. Cross-ticket fields
  that the gate reads (standing instructions, caps, always-ask, contractor status) change only through ratified
  proposals, each with a source, an effective date and an expiry. Authoritative facts (a withdrawn approval, a change of
  landlord, an expired certificate) are refreshed from the system that owns them at once, never held until closure.
- **No second model reader yet.** The optional downgrade-only review that exists is the experiment: run it in shadow on
  held-out and adversarial cases and measure incremental serious-error detection, false escalations, latency and cost.
  Adopt it only on that evidence. Bounded sub-calls (document extraction with page references, drafting in the agency's
  voice) are separate and worth doing.
- **The regression gate was too small.** A 25-case subset chosen because it moved today is biased, and a two-point
  band over it is not justified by ±1 per case. The gate is the full public set with a measured paired-run variance,
  critical and prohibited failures failing on their own regardless of averages, plus targeted fixtures.

## Principles

1. A capability is data in the rulebook; a check the gate can make deterministically is never left to the model.
2. Critical checks run before the tool call. A reviewer that downgrades a verdict after execution cannot retract a sent
   message or a dispatched contractor.
3. Every change to rules, prompts or playbooks is measured before it ships; the deterministic layer is replayed for free,
   the model layer is run against the judge.
4. Personal data is minimised, tagged and erasable across every place it lands: state, records, traces, baselines,
   fixtures, git history.

## M0 — Quality gate and layer hygiene

Exit: a change to any artefact cannot reach `main` without the gate; two shipped regressions of the hackathon day could
not recur.

- `make replay-rules`: the gate and reviewer replayed over stored states of past runs (seconds, no model calls). Runs on
  every change to `harness/gate.py`, `harness/reviewer.py`, the rulebook, the schema. It cannot see changed tool
  sequences or model behaviour, so it is necessary, not sufficient.
- `make regress`: the full public set through the model and the judge. Baseline = two runs on the same commit, so the
  per-case variance is measured, not assumed. A drop beyond that variance, or any new critical or prohibited failure,
  fails the gate on its own. Prompt, rule and playbook co-changes always take the full run.
- Targeted fixtures in the simulator and the mutation set: sender spoofing, approval withdrawal after dispatch, duplicate
  and out-of-order events across channels, timeout, crash mid-write, instructions embedded in attachments.
- Evidence, not prose: `_run.json` already carries the commit; add the rulebook and playbook versions, and let the
  changelog be generated from run records. A fresh-context reviewer of the diff stays a review step, not the gate; it
  cannot prove that tests ran.
- Hygiene that the gate depends on: prompt text out of `harness/loop.py` into the data artefacts; tool-argument
  validation against the tool schema before execution (silent type drift is the hackathon's classic failure); the
  case-folder adapter split into parsing and ledger tools; adapter contract tests run against both environments.
- A pre-execution hazard check independent of the model's urgency label: a reported hazard (gas, water on electrics, a
  failed alarm at move-in) blocks `resolved` and `close_request` and forces a human confirmation before any dispatch,
  whatever urgency the model chose. The reviewer's emergency-only escalation stays for the post-hoc verdict.

## M1 — Trust envelope before any live write

Exit: the agent can act on a real ticket in shadow mode without a person being able to spoof an authority.

- Identity at ingress: email authentication results, known numbers, the landlord of record per property. Trust classes
  are assigned by verified identity, not by where a file sits.
- A small authoritative table with provenance (landlord of record, spend cap, always-ask, standing instructions, each
  with who/when/source): a controlled import from the agency's records or a hand-kept table. The full CRM integration
  comes later; this table is enough for the gate.
- An approval object bound to a quote: amount, scope, the event it came from, withdrawal. Re-checked immediately before
  execution, not only when the plan was made.
- Operational controls: a kill switch, shadow mode (the agent writes to its own ledger only), a per-environment write
  allowlist, explicit human ownership of escalations with delivery confirmation, an acknowledgement deadline and an
  out-of-hours fallback. Evaluation distinguishes escalation recorded, handoff delivered, responsibility accepted.
- Untrusted-content controls at live ingress: tool authority bound to the verified channel, instructions inside
  attachments quarantined, adversarial cases in the judge and mutation suite.

## M2 — Continuity

Exit: a ticket survives days of silence and new events without the agent re-reading it from scratch or acting twice.

- The harness's ticket store: state, pending actions, receipts, wake-ups, event cursor; schema versioned with
  migrations.
- Re-entry: the previous state is loaded as the agent's own prior claims, not as evidence; per-ticket serialisation;
  deduplicated and ordered ingestion when an email, an SMS and a call summary arrive within minutes.
- Wake-ups from the clocks and promises already in the record; a supervisor sweep with a rate and cost budget and a
  risk-ordered queue (escalated, then resolved with money, then holds past their date); a morning board.
- The ticket-system adapter (Zammad or FreeScout): read-only first (thread = event stream), then writes behind the
  allowlist; custom fields and the internal note are projections of the store.

## M3 — Memory and documents

Exit: the gate reads cross-ticket fields only through ratified, dated, attributed entries; long documents enter the
loop as cited facts.

- Hybrid entity memory as described above, with a deliberately small schema; proposals accumulate during a case and are
  ratified at closure or on demand; consent and sensitivity tags on tenant fields with field-level access; a
  rectification and erasure path that reaches every copy.
- Bounded extraction: check-out reports, quotes and invoices read by a sub-call that returns facts with page references;
  citations verified against the document before they enter the record.
- Drafting sub-call: the agency's voice and lexicon as data; every outbound message in a ledger with the draft and the
  sent text, so an operator's edits become a signal.
- Model tiering: the decision step on the strongest model; extraction, drafting and classification on cheaper ones.
  A maintenance desk's margin does not pay for Opus on every sub-call.

## M4 — Integrations, in this order

Each one an adapter with contract tests in both environments and a shadow pilot before writes.

1. CRM (full): canonical identities and relationships replace the M1 table; the table's provenance rules carry over.
2. Vendor management: compliance documents with expiry (insurance, gas-safety registration), trade match, blacklist,
   SLAs, track record from tickets. They become gate preconditions on data (`CAP-DISPATCH` requires compliance valid on
   the date), not prompt text.
3. Payments and accounting: invoice capture into structure, the three-way match of quote, invoice and completion
   evidence, a `resolution` proposal object (invoice to landlord, deduct from rent, without payment). A person posts.
   "No ledger writes" also excludes indirect posting or payment tools.

## Cross-cutting: data protection and the public repository

A DPIA with the agency; retention and deletion agreed with the controller; no personal data in public fixtures, traces
or git history; the boundary between the public repository (harness, evaluation, the example agent) and the agency's
own assets (its rulebook, lexicon, schemas, endpoints) drawn before the first real ticket.

## Deferred or rejected, with reasons

- An in-runtime second model reader: deferred to the shadow measurement above. Dissent recorded: one review would drop
  it outright and spend the budget on deterministic rules and the offline judge.
- Specialist agents for steps of the loop: rejected; five or six steps gain nothing from hand-offs.
- CRM integration before any ticket work: rejected in favour of the M1 table; the full CRM is M4.
- A changelog line written by hand per commit: replaced by generated run records.

## Practices borrowed from the author's personal agent system

See [plan-atlas-practices.md](plan-atlas-practices.md) for the first four. Added after today: raw communication is
immutable and a call summary is an index, not a source (the reviewer may treat a summary as weaker evidence than the
verbatim message it summarises); a supervisor's stall heuristics (a step several times the median duration is flagged;
no progress plus a hard multiple is killed); shadow mode for any new threshold before it can fail a gate; a decision log
whose entries are typed and attributed, which is what the approval object is; a comms ledger with the draft and the
sent text; a multi-model council as a release gate, never at runtime.

## Decisions for the team

1. Shadow pilot on real tickets: which agency desk, how many tickets, who owns escalations out of hours.
2. The ticket system (Zammad or FreeScout) and whether the agency's current tools can export the M1 table.
3. The open-source boundary: which of today's artefacts stay public as the example agent.
