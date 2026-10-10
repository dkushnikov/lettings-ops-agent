# Runbook — the final hour (16:00–17:00 BST)

Owner of the keyboard: Dmitry K. Owner of the checklist: Dmitry T. Nothing is edited by hand after 16:30 except SUBMISSION.md fields and the posts.

## 16:00 — feature freeze and checks

- [ ] No code changes after this point. Open editors closed.
- [ ] `make check` green; `make rehearse` green (fresh clone → setup → run → verify).
- [ ] `git status` clean before `make freeze` (it stages everything).
- [ ] `make secrets-scan` clean (gitleaks over the working tree and history).
- [ ] `.env` not tracked: `git status --ignored` shows it ignored.
- [ ] `LICENSE` present (Apache 2.0), `NOTICE` present.
- [ ] `README.md`: all eight sections, TODO(event) markers resolved except the Reality Test record.
- [ ] `PREBUILT.md` lists what changed since `pre-event`: `git diff --stat pre-event..HEAD`.
- [ ] `SUBMISSION.md` fields filled except hashes and post URLs.
- [ ] Repository switched to **public**: `gh repo edit --visibility public --accept-visibility-change-consequences`; open the URL in a private browser window to confirm.
- [ ] `video/demo.mp4` is a plain git blob (42 MB, under GitHub's limit); `git lfs ls-files` is empty and that is expected.

## 16:15 — video

- [ ] `make video-check` reports duration ≤ 60 s.
- [ ] `video/demo.mp4` committed and pushed; the raw URL returns the binary (`curl -sL -o /dev/null -w '%{http_code} %{content_type}' https://raw.githubusercontent.com/dkushnikov/lettings-ops-agent/main/video/demo.mp4`).

## 16:30 — code freeze and Reality Test start

- [ ] `make freeze` → creates tag `freeze-1630`, prints the commit hash; paste it into `SUBMISSION.md`.
- [ ] `git push --tags`.
- [ ] Reality Test cases received: the organisers' README says results are submitted only for the cases in `HackatonChallendges/` (the public examples under `Property Management/` must not be submitted). `git -C ../HackatonPublicCases pull`, then check the layout: `NNN/` folders with `index.md` and `history.md`; if the folder name differs from `HackatonChallendges/Property Management`, change only `CASES=`.
- [ ] Count the cases. The runner prints the capacity estimate: `T ≈ ⌈N / C⌉ × t_case + margin`. Measured today: 50 cases at concurrency 6 take about 16 minutes with no 429s; 100 cases would take about 32, so raise concurrency to 8 only if the count is above 60.
- [ ] No runner alive before launching: `pgrep -fl "harness.cli run"` prints nothing (the 15:20 rehearsal reused one case from a runner that was still writing when the folder was removed).
- [ ] Launch (the exact form tested all day; `--id-style number` → `ANSWERS/<case number>/`):

```
git -C ../HackatonPublicCases pull                     # the Reality Test cases arrive at 16:30
ls "../HackatonPublicCases/HackatonChallendges/Property Management"   # expect NNN/ folders with index.md + history.md
make run ARGS="--adapter dwelly --id-style number --concurrency 6 --deadline 16:52" \
  CASES="../HackatonPublicCases/HackatonChallendges/Property Management" OUT=ANSWERS
```

- [ ] Watch the dashboard. 429s → the runner backs off by itself; do not restart it. A crash → restart the same command; checkpoints skip finished cases.
- [ ] `--deadline 16:52`: a case not started by then gets a fallback record instead of holding the run past the freeze; running cases finish on their own budget (540 s).
- [ ] `ANSWERS/` holds only Reality Test results (the form: unseen cases received at 16:30, committed by 17:00). The 15:20 rehearsal on the public cases lives in `runs/answers-rehearsal/`, not in the repository. Before launching, `ANSWERS/` must be absent: the runner reuses finished case folders (checkpoint) and would not regenerate them.

## 16:50 — stop launching, start verifying

- [ ] Stop launching optional reruns. Running cases finish; the fallback closes anything that cannot.
- [ ] Verify every case folder: `ANSWER.md`, `REASONING.md`, `trace.jsonl` present; `_run.json` written; the runner's summary shows 0 missing.
- [ ] Spot-read one escalated and one resolved record: disposition, authority citations, handover card.
- [ ] Pre-push integrity check (read-only): `uv run --directory /Users/dkushnikov/Claude/source-judge python tools/check_answers.py ANSWERS --cases "<the Reality Test cases dir>"` → "OK — nothing blocking"; a warning that `_run.json` commit ≠ HEAD is expected once docs commits followed the freeze.
- [ ] `make secrets-scan` green (`.gitleaks.toml` allowlists the records' idempotency keys and action ids; anything else it finds is real).
- [ ] `git add ANSWERS && git commit -m "Reality Test results"` and `git push`.
- [ ] Open the repository on GitHub and confirm `ANSWERS/` is visible; note the commit hash into `SUBMISSION.md`.

## 16:55 — submit

- [ ] Publish the LinkedIn and X posts (`posts/`), paste URLs into `SUBMISSION.md`; commit and push.
- [ ] Submit the form: repo URL, team, track, members, freeze hash, results commit hash, results path, video path, post URLs.
- [ ] Screenshot the form confirmation.

## Rules that do not bend

- Never edit a file inside `ANSWERS/` by hand. A wrong answer stays wrong; a fabricated one is disqualifying.
- Never re-run a single case to "fix" it after 16:50.
- Never force-push.
