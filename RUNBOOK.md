# Runbook — the final hour (16:00–17:00 BST)

Owner of the keyboard: Dmitry K. Owner of the checklist: Dmitry T. Nothing is edited by hand after 16:30 except SUBMISSION.md fields and the posts.

## 16:00 — feature freeze and checks

- [ ] No code changes after this point. Open editors closed.
- [ ] `make check` green.
- [ ] `make secrets-scan` clean (gitleaks over the working tree and history).
- [ ] `.env` not tracked: `git status --ignored` shows it ignored.
- [ ] `LICENSE` present (Apache 2.0), `NOTICE` present.
- [ ] `README.md`: all eight sections, TODO(event) markers resolved except the Reality Test record.
- [ ] `PREBUILT.md` lists what changed since `pre-event`: `git diff --stat pre-event..HEAD`.
- [ ] `SUBMISSION.md` fields filled except hashes and post URLs.
- [ ] Repository switched to **public**: `gh repo edit --visibility public --accept-visibility-change-consequences`; open the URL in a private browser window to confirm.
- [ ] Git LFS working: `git lfs ls-files` lists `video/demo.mp4`.

## 16:15 — video

- [ ] `make video-check` reports duration ≤ 60 s.
- [ ] `video/demo.mp4` committed and pushed; the file downloads from GitHub (not a pointer).

## 16:30 — code freeze and Reality Test start

- [ ] `make freeze` → creates tag `freeze-1630`, prints the commit hash; paste it into `SUBMISSION.md`.
- [ ] `git push --tags`.
- [ ] Reality Test cases copied to the agreed directory (do not edit them).
- [ ] Count the cases. The runner prints the capacity estimate: `T ≈ ⌈N / C⌉ × t_case + margin`. If T exceeds 20 minutes, raise concurrency only if the rate-limit headroom measured at 14:00 allows it.
- [ ] Launch:

```
uv run python -m harness.cli run --cases <reality-test-dir> --out ANSWERS --concurrency 4
```

- [ ] Watch the dashboard. 429s → the runner backs off by itself; do not restart it. A crash → restart the same command; checkpoints skip finished cases.

## 16:50 — stop launching, start verifying

- [ ] Stop launching optional reruns. Running cases finish; the fallback closes anything that cannot.
- [ ] Verify every case folder: `ANSWER.md`, `REASONING.md`, `trace.jsonl` present; `_run.json` written; the runner's summary shows 0 missing.
- [ ] Spot-read one escalated and one resolved record: disposition, authority citations, handover card.
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
