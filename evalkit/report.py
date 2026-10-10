"""Self-contained HTML report for a run: one page the operator can scan in a minute.

No dependencies beyond the standard library. Reads a run directory
(`ANSWERS/` or `runs/<name>/`), the optional `_eval.json` from the judge, and
the fixtures' `expected.yaml` when a cases directory is given.
"""

from __future__ import annotations

import html
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from harness.recorder import read_state

STYLE = """
:root{color-scheme:light dark;--bg:#faf7f0;--fg:#2a2622;--muted:#6b6259;--line:#e6dfd2;--card:#fffdf8;--ok:#2e7d32;--warn:#b26a00;--bad:#b3261e;--info:#1f5fa8}
@media (prefers-color-scheme:dark){:root{--bg:#1e1b17;--fg:#ebe5da;--muted:#a79d90;--line:#3a342d;--card:#26221d;--ok:#7bc47f;--warn:#e0a84a;--bad:#f28b82;--info:#8ab4f8}}
body{margin:0;padding:24px;background:var(--bg);color:var(--fg);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}
h1{font-size:24px;margin:0 0 6px}h2{font-size:17px;margin:0 0 8px}
.sub{color:var(--muted);margin-bottom:18px}
.metrics{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px}
.metric{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 14px;min-width:150px}
.metric b{display:block;font-size:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:4px 0}
.tag{display:inline-block;padding:1px 8px;border-radius:999px;font-size:12px;border:1px solid var(--line)}
.resolved{color:var(--ok)}.needs_info{color:var(--info)}.escalated{color:var(--warn)}.bad{color:var(--bad)}
.k{color:var(--muted);font-size:12px}
details{margin-top:8px}summary{cursor:pointer;color:var(--info)}
pre{white-space:pre-wrap;word-break:break-word;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:10px;font-size:12.5px;max-height:60vh;overflow:auto}
.note{font-size:13px;color:var(--muted)}
table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}
"""


def _expected_map(cases_dir: Path | None) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not cases_dir or not cases_dir.exists():
        return out
    for case_yaml in sorted(cases_dir.glob("*/case.yaml")):
        manifest = yaml.safe_load(case_yaml.read_text(encoding="utf-8")) or {}
        cid = str(manifest.get("id") or case_yaml.parent.name)
        exp = case_yaml.parent / "expected.yaml"
        if exp.exists():
            out[cid] = yaml.safe_load(exp.read_text(encoding="utf-8")) or {}
    return out


def _eval_map(run_dir: Path) -> dict[str, dict[str, Any]]:
    p = run_dir / "_eval.json"
    if not p.exists():
        return {}
    try:
        return {r["case"]: r for r in json.loads(p.read_text(encoding="utf-8"))}
    except Exception:  # noqa: BLE001
        return {}


def _esc(s: Any) -> str:
    return html.escape(str(s) if s is not None else "")


def build_report(run_dir: Path, cases_dir: Path | None = None) -> Path:
    expected = _expected_map(cases_dir)
    evals = _eval_map(run_dir)
    meta: dict[str, Any] = {}
    if (run_dir / "_run.json").exists():
        try:
            meta = json.loads((run_dir / "_run.json").read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            meta = {}

    cards: list[str] = []
    n = valid = workflow = fallbacks = unconf_total = 0
    disp_counts = {"resolved": 0, "needs_info": 0, "escalated": 0}
    judge_out = judge_js = judged = 0
    for case_dir in sorted(p for p in run_dir.iterdir() if p.is_dir() and (p / "ANSWER.md").exists()):
        cid = case_dir.name
        state = read_state(case_dir)
        answer = (case_dir / "ANSWER.md").read_text(encoding="utf-8")
        reasoning = (case_dir / "REASONING.md").read_text(encoding="utf-8") if (case_dir / "REASONING.md").exists() else ""
        n += 1
        disp = state.disposition.value if state and state.disposition else "unknown"
        disp_counts[disp] = disp_counts.get(disp, 0) + 1
        fb = bool(state and state.fallback)
        fallbacks += int(fb)
        unconf = sum(1 for a in (state.actions if state else []) if a.status.value == "unconfirmed")
        unconf_total += unconf
        if state and state.terminal_valid() and not fb:
            valid += 1
        exp = expected.get(cid, {})
        ev = evals.get(cid, {})
        if isinstance(ev.get("outcome"), int):
            judged += 1
            judge_out += ev["outcome"]
            judge_js += int(ev.get("judgement_safety") or 0)
        exp_disp = exp.get("expected_disposition")
        match = "" if not exp_disp else ("match" if exp_disp == disp else "differs")
        writes_ok = state.completed_writes if state else 0
        if state and ((disp == "resolved" and writes_ok) or (disp == "escalated" and state.handover) or (disp == "needs_info" and state.info_requests)):
            workflow += 1
        flags = ", ".join(f"{f.kind}" for f in (state.red_flags if state else []))
        title = _esc(answer.splitlines()[0].replace("# ANSWER — ", "")) if answer else cid
        judge_html = ""
        if ev:
            crit = ev.get("critical_failure")
            judge_html = (
                f'<div class="row"><span class="tag">judge outcome {ev.get("outcome")}/2</span>'
                f'<span class="tag">judgement&safety {ev.get("judgement_safety")}/2</span>'
                f'<span class="tag {"bad" if crit else ""}">{"CRITICAL FAILURE" if crit else "no critical failure"}</span>'
                f'<span class="tag {"bad" if ev.get("prohibited_violated") else ""}">prohibited: {len(ev.get("prohibited_violated") or [])}</span></div>'
                f'<div class="note">{_esc(ev.get("notes", ""))}</div>'
            )
        exp_html = ""
        if exp:
            req = "".join(f"<li>{_esc(r)}</li>" for r in (exp.get("required_outcomes") or [])[:6])
            crit_l = "".join(f"<li>{_esc(r)}</li>" for r in (exp.get("critical_failures") or [])[:4])
            exp_html = f"<details><summary>Expected ({_esc(exp.get('axis', ''))})</summary><div class='k'>required</div><ul>{req}</ul><div class='k'>critical failures</div><ul>{crit_l}</ul></details>"
        cards.append(
            f'<div class="card"><h2>{title}</h2>'
            f'<div class="row"><span class="tag {disp}">{disp}</span>'
            + (f'<span class="tag {"bad" if match == "differs" else ""}">expected {_esc(exp_disp)} · {match}</span>' if exp_disp else "")
            + f'<span class="tag">urgency {_esc(state.urgency if state else "?")}</span>'
            f'<span class="tag">steps {state.steps if state else "?"}</span>'
            f'<span class="tag">writes ok {writes_ok}</span>'
            + (f'<span class="tag bad">unconfirmed {unconf}</span>' if unconf else "")
            + ('<span class="tag bad">FALLBACK</span>' if fb else "")
            + (f'<span class="tag">flags: {_esc(flags)}</span>' if flags else "")
            + "</div>"
            + judge_html
            + exp_html
            + f"<details><summary>ANSWER.md</summary><pre>{_esc(answer)}</pre></details>"
            + f"<details><summary>REASONING.md</summary><pre>{_esc(reasoning)}</pre></details>"
            + "</div>"
        )

    stamp = datetime.now().astimezone().isoformat(timespec="minutes")
    metrics = [
        ("records present", f"{n}/{n}"),
        ("valid terminal decision", f"{valid}/{n}"),
        ("workflow completed", f"{workflow}/{n}"),
        ("fallbacks", str(fallbacks)),
        ("unconfirmed writes", str(unconf_total)),
        ("resolved / needs_info / escalated", f"{disp_counts.get('resolved',0)} / {disp_counts.get('needs_info',0)} / {disp_counts.get('escalated',0)}"),
    ]
    if judged:
        metrics.append(("judge: outcome · judgement&safety", f"{judge_out}/{2*judged} · {judge_js}/{2*judged}"))
    if meta:
        metrics.append(("wall / model", f"{(meta.get('actual_wall_s') or 0):.0f}s · {_esc(meta.get('model',''))} · c={meta.get('concurrency')}"))
    metrics_html = "".join(f'<div class="metric"><span class="k">{_esc(k)}</span><b>{_esc(v)}</b></div>' for k, v in metrics)
    page = (
        "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>Run report — {_esc(run_dir.name)}</title><style>{STYLE}</style></head><body>"
        f"<h1>Run report — {_esc(run_dir)}</h1><div class='sub'>generated {stamp}"
        + (" · judge file present" if evals else " · no _eval.json (run <code>make eval</code>)")
        + "</div>"
        f"<div class='metrics'>{metrics_html}</div><div class='grid'>{''.join(cards)}</div></body></html>"
    )
    out = run_dir / "report.html"
    out.write_text(page, encoding="utf-8")
    return out


def main(run: Path, cases: Path | None = None, open_browser: bool = False) -> int:
    out = build_report(run, cases)
    print(out)
    if open_browser:
        import subprocess

        subprocess.run(["open", str(out)], check=False)
    return 0
