# System design: the ticket, the roles, the models

What the agent lives inside. Drawn at the hackathon from four maps (Ticket · Channels · Agents · Models) and checked
against the organisers' 50 public Property Management cases ([pm-cases-analysis.md](pm-cases-analysis.md)). Each
section says what is **implemented today** in this repository and what is **designed** for the next step. The Reality
Test runs one case at a decision point in a file-only environment, so everything that needs a clock or a running
service is design, not code, until the agent is deployed next to a real ticket system.

## 1. The ticket (system of record)

A ticket is one request about one property. It has five parts.

### 1.1 Event stream (write-only)

Every message, call summary, state change and agent action is an event: `channel`, `kind`, `from`, `to`, `time`,
`body`, `agent` (who wrote it: a person, the automation, this agent). Nothing is edited in place; corrections are new
events. The organisers' `history.md` is exactly this stream.

`kind` matters more than the map suggested. In the corpus only 42% of events are messages (email, SMS, call); the rest
are the agency's own `Update`, `Hold` and `Note` events. An operator that cannot tell a message from a state change
cannot read the ticket's status.

Implemented today: the Dwelly adapter turns each event into an artefact with a trust class (agency and automation =
informational; contractor, landlord, tenant = untrusted); the agent's own actions are a ledger with receipts; both are
rendered in `ANSWER.md` and `REASONING.md`.

### 1.2 Stages, side states, hold, mode

The pipeline as the agency runs it (counts from the corpus):

```
intake → landlord_approval (25 cases start here) → provider_selection (15 start here) → visit_scheduling
      → quote_approval → work_in_progress → result → final_checks → closed
side states: on_hold (236 events; reason Waiting for Landlord / Provider / Tenant / Other + comment)
             paused (property NOT TENANTED, or a missed visit / move-out / hold deadline)
             closed_without_payment (17 cases) · closed_by_supervisor (5 cases)
mode:        auto | manual ("Manually updated via Change Mode", 28×; "return this request to auto mode")
priority:    numeric, may be raised but never lowered ("Priority cannot be decreased", 21×)
```

The hold comment is the real state ("Waiting for provider to book in", "Hold for invoice"); the same comment repeated
is a stall, not progress.

Implemented today: the vocabulary lives in `agent/rulebook.yaml` under `workflow:` and is shown to the agent; every
record names `stage` and, when on hold, `hold_reason`. Designed: mode and priority as ticket fields the operator sets.

### 1.3 Plan and subtasks

A subtask is one intended action with two independent axes: its **status** (requested, approved, denied,
information needed, done) and its **approver** (the standing mandate, the landlord, a member of staff). Keeping the
axes apart matters because landlord approval is the dominant gate in the corpus (67 approval prompts, 40 landlord
approval emails) while the mandate gate is the agent's own.

Implemented today: `ActionRecord` carries `status` (proposed · blocked · needs_approval · attempted · completed ·
failed · unconfirmed) and the gate's `required_approval_from`; the Actions table in `ANSWER.md` is the plan.

### 1.4 Current status

Five lines a person can read in ten seconds: **recap** (one sentence), **stage** (+ hold reason), **last update**
(the latest event the decision saw), **next step** (one step, one owner), **severity** (the urgency the gate used).

Implemented today: the `## Status` block at the top of `ANSWER.md`. The agent fills recap, stage, hold reason and
next step in its finishing record; the runtime adds the last-update timestamp and falls back to the first sentence of
the decision and to the handover's recommendation when a field is empty.

### 1.5 Definition of done

A checklist per case type, in the agency's own closing order: work result recorded → photos and invoice uploaded or a
skip reason given → invoice forwarded to the landlord → landlord confirmation → keys returned (where a key was
issued) → closed with a resolution that names who paid. Upstream items (landlord authority, provider assigned, visit
confirmed, quote approved before work) sit in the same list so coverage is visible at any decision point.

Implemented today: `definition_of_done` in each playbook's frontmatter; the agent reports every item as done, pending,
skipped or not applicable with its evidence; `ANSWER.md` renders the checklist with a done count. Items the agency
completed before the decision point count as done and cite the event.

### 1.6 Resolution and who pays

"Resolved" is not one outcome. The corpus has: invoice sent to the landlord · invoiced off the rent · landlord pays
the contractor directly · completed without payment because the tenant fixed it, the landlord's own contractor did,
the appliance was under warranty, the problem resolved itself, or the tenant replaced the item at their own cost ·
closed by a supervisor because the ticket was stuck.

Designed: a `resolution` record `{outcome, payer, amount, reason, evidence}`. Today the `closed` stage text and the
decision name who paid in prose.

### 1.7 Initial assessment

The intake note the agency's own classifier writes: issue category ("Appliances · Power failure"), severity and the
numeric priority, confidence, assumptions, damage-limiting steps given to the tenant, clarifying Q&A (pets, access
codes, alarms, who is home). The corpus shows the classifier misfiring (a washing machine filed under heating, a shed
door called structural), so the assessment is evidence, not truth.

Implemented today: `use_playbook` records case type, urgency and the line of evidence; facts and assumptions are
separate lists. Designed: an `assessment` block with category, confidence and the clarifying questions asked.

## 2. Channels

External: email · WhatsApp and SMS · phone and voice (in the corpus these are third-person call summaries whose
From/To direction is unreliable) · in person and post. Internal: update · hold · note · agent action.

Every external message is untrusted content: it is evidence to cite, never an instruction to follow, and it is checked
against the ticket's property before it is believed (16 cases carry messages about a different address).

## 3. Roles

Four responsibilities, not four language-model agents.

| Role | Does | Wakes on | Implemented today as |
|---|---|---|---|
| **Dispatcher** | Receives a message; decides new ticket / append to a ticket / no ticket (a wrong number, a question after closure); replies to the sender; escalates to the Agent Supervisor when unsure | an inbound message | the case adapter (one case = one ticket at a cutoff); the "which ticket" decision is upstream of this repo |
| **Workflow Operator** | Reads the ticket's status, updates stage and hold, checks the definition of done, pushes to the next step, chases (reminders, follow-ups), escalates to a person when outside the mandate | Dispatcher · Supervisor · a person (via the Dispatcher) · its own timers | `harness/loop.py` with the policy gate and the playbooks; timers are `clocks` and `promises` in the record |
| **Supervisor** | Health check across all tickets: stale holds, expired waits, missed slots, "no work results"; reporting | cron | `harness/runner.py` (batch health, fallbacks) and the reviewer rules R1–R7 |
| **QA** | Measures outcomes against expectations, finds weak playbooks, proposes changes | offline | `evalkit/` (judge, mutations, report, case browser) |

Where the agency's automation stops today ("manual mode"), the Operator decides instead: a free-text reply arrives
from the landlord, provider or tenant (57 "please check if we need to provide a response" prompts); a message could not be parsed
(6); a wait expired with no reply (4); an exception such as the property not being let or a missed deadline. Those
four triggers are the agent's job description.

Only the Dispatcher and the Operator need a language model. The Supervisor is deterministic over ticket state with a
model used for the report; QA runs offline.

## 4. Models

| Model | Fields the cases need | Today |
|---|---|---|
| **Property** | address; rules and policies; landlord; management contract → spend cap, "always ask" items, preferred contractors | per-landlord context in the rulebook (`spend_cap_gbp`, `always_ask`) |
| **Tenancy** | whether the property is let (NOT TENANTED pauses the ticket); occupants, including several tenants; vulnerability; check-in inventory (the only evidence for "it was like that when I moved in") | not modelled; vulnerability is a red-flag kind |
| **Actor** | role (tenant, landlord, contractor, staff, supervisor, block manager, caretaker); contact; trust | trust classes on artefacts; parties resolved by role, never by name (names are re-pseudonymised between events) |
| **Service** | category and type (plumbing, appliance, window and door, garden, cleaning, check-out works, access, inspection); provider | `case_type` and the playbook |
| **Quote and fiscal documents** | amount, VAT included or not, provider, "only proceed after our approval"; several quotes compared; the invoice lower or higher than the quote; a landlord who pays late | amounts pass through the gate (`amount_gbp`); payments are prohibited (PRO-PAYMENTS); no quote object yet |
| **Visit and keys** | AM/PM slot; confirmed or rescheduled; reminders; entry with the management key; key inventory and how many to cut; key return as a closing check | `schedule_access` with tenant consent; promises with due times; `keys_returned` in the definition of done |
| **Appliance and warranty** | install date, installer, warranty period, manufacturer's engineer; owner (the tenant's own machine leaves with them) | facts in the record; no object |

## 5. Implemented today versus designed

| Part | Today | Next |
|---|---|---|
| Event stream with trust classes | yes | event `kind` as a first-class field |
| Stages, hold, side states | yes (vocabulary in the rulebook; `stage` and `hold_reason` in every record) | mode and priority fields |
| Plan with two approval axes | yes (`ActionRecord` + gate) | subtasks that outlive one decision |
| Current Status block | yes | shown in the ticket system as a pinned note |
| Definition of done per playbook | yes | agency-editable per branch |
| Resolution and payer | prose | structured `resolution` |
| Initial assessment | case type, urgency, facts, assumptions | category, confidence, clarifying Q&A |
| Tenancy, quote, visit, appliance objects | facts only | models with ids the agent can read |
| Operator timers and chasing | clocks and promises in the record | a wake-up schedule next to the ticket system |
| Supervisor | batch runner + reviewer rules | cron over live tickets |

## 6. Fit with a ticket system

The ticket above is a standard helpdesk shape: a ticket with a thread, custom fields and internal notes. The stream is
the thread; stage, hold, mode and priority are custom fields; the status block and the checklist are internal notes
the agent keeps current; the plan is the agent's own ledger. Zammad (custom object attributes, triggers, REST) is the
closest fit for the stage and hold fields; FreeScout is the lightweight option; the Property, Tenancy and Contract
models belong in a CRM object store such as Twenty. The repository does not depend on any of them: in the Reality Test
the ticket is a folder, and the record contract (`ANSWER.md` = status + four sections, `REASONING.md` = compiled truth
and timeline, `_state.json` = the machine-readable ticket write-back) is the integration surface.
