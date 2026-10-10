"""Runs board: one self-contained HTML page over everything under `runs/`.

Case runs (`runs/<name>/_run.json`, `_eval.json`, `_cutoffs.yaml`, `<case>/_state.json`)
and simulator runs (`runs/sim/<stamp>/summary.json`, written by `evalkit/simulate.py`)
side by side, newest first. Each run expands into its per-case or per-scenario table
and links into the case browser, the run's report and the raw files. Every source is
optional: a run directory contributes whatever it has, and a directory with none of
them (a cases symlink farm, mutations) is not a run.
"""

from __future__ import annotations

import html
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import yaml

NUM_RE = re.compile(r"(\d{3})$")
DEFAULT_TRACK = "Property Management"
OUTPUT_DIRS = {"cases", "board"}  # pages this module and the case browser write; never runs
NOTE_CHARS = 280
TEXT_CHARS = 160


# --------------------------------------------------------------------------- #
# Reading
# --------------------------------------------------------------------------- #


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    except Exception:  # noqa: BLE001
        return None


def _read_yaml(path: Path) -> Any:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else None
    except Exception:  # noqa: BLE001
        return None


def _parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _mtime(path: Path) -> datetime:
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def _terminal_valid(state: dict[str, Any]) -> bool:
    """Mirror of DecisionState.terminal_valid on the raw JSON: a disposition with the matching payload."""
    disp = state.get("disposition")
    if not disp:
        return False
    if disp == "escalated":
        return bool((state.get("handover") or {}).get("question"))
    if disp == "needs_info":
        return bool(state.get("info_requests"))
    return bool(state.get("decision"))


def _case_row(case_dir: Path, state: dict[str, Any] | None, has_answer: bool) -> dict[str, Any]:
    m = NUM_RE.search(case_dir.name)
    s = state or {}
    dod = [d for d in (s.get("definition_of_done") or []) if isinstance(d, dict)]
    fallback = bool(s.get("fallback"))
    return {
        "id": case_dir.name,
        "number": m.group(1) if m else None,
        "dir": str(case_dir),
        "present": has_answer or state is not None,
        "disposition": s.get("disposition"),
        "stage": s.get("stage") or "",
        "hold_reason": s.get("hold_reason") or "",
        "next_step": s.get("next_step") or "",
        "dod_done": sum(1 for d in dod if d.get("status") == "done"),
        "dod_total": sum(1 for d in dod if d.get("status") != "not_applicable"),
        "steps": s.get("steps"),
        "fallback": fallback,
        "valid": _terminal_valid(s) and not fallback if state is not None else False,
        "model": s.get("model") or "",
        "tokens_in": int(s.get("input_tokens") or 0),
        "tokens_out": int(s.get("output_tokens") or 0),
        "red_flags": len(s.get("red_flags") or []),
        "judge": None,
        "cutoff": None,
        "answer": str(case_dir / "ANSWER.md") if has_answer else None,
        "state_file": str(case_dir / "_state.json") if state is not None else None,
    }


def _judge_row(r: dict[str, Any]) -> dict[str, Any]:
    return {
        "outcome": r.get("outcome"),
        "judgement_safety": r.get("judgement_safety"),
        "disposition": r.get("disposition"),
        "critical_failure": bool(r.get("critical_failure")),
        "prohibited_violated": [str(x) for x in (r.get("prohibited_violated") or [])],
        "notes": str(r.get("notes") or ""),
    }


def _judge_totals(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    rows = [r for r in rows if isinstance(r, dict)]
    if not rows:
        return None
    outcome = [r.get("outcome") for r in rows if isinstance(r.get("outcome"), (int, float))]
    js = [r.get("judgement_safety") for r in rows if isinstance(r.get("judgement_safety"), (int, float))]
    return {
        "rows": len(rows),
        "outcome_sum": int(sum(outcome)),
        "outcome_max": 2 * len(outcome),
        "js_sum": int(sum(js)),
        "js_max": 2 * len(js),
        "critical": sum(1 for r in rows if r.get("critical_failure")),
        "prohibited": sum(1 for r in rows if r.get("prohibited_violated")),
    }


def collect_case_run(run_dir: Path, name: str | None = None) -> dict[str, Any] | None:
    """A case run from whatever the directory holds; None when it holds nothing a run would."""
    run_dir = Path(run_dir)
    meta = _read_json(run_dir / "_run.json")
    meta = meta if isinstance(meta, dict) else {}
    eval_rows = _read_json(run_dir / "_eval.json")
    eval_rows = [r for r in eval_rows if isinstance(r, dict)] if isinstance(eval_rows, list) else []
    raw_cutoffs = _read_yaml(run_dir / "_cutoffs.yaml")
    cutoffs: dict[str, int] = {}
    if isinstance(raw_cutoffs, dict):
        for k, v in raw_cutoffs.items():
            try:
                cutoffs[str(k).zfill(3)] = int(v)
            except (TypeError, ValueError):
                continue
    cases: list[dict[str, Any]] = []
    for cd in sorted(p for p in run_dir.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
        state = _read_json(cd / "_state.json")
        state = state if isinstance(state, dict) else None
        has_answer = (cd / "ANSWER.md").exists()
        if state is None and not has_answer:
            continue
        cases.append(_case_row(cd, state, has_answer))
    if not meta and not eval_rows and not cases:
        return None
    by_case: dict[str, dict[str, Any]] = {}
    for r in eval_rows:
        key = str(r.get("case", ""))
        by_case[key] = r
        m = NUM_RE.search(key)
        if m:
            by_case.setdefault(m.group(1), r)
    for row in cases:
        r = by_case.get(row["id"]) or (by_case.get(row["number"]) if row["number"] else None)
        if r:
            row["judge"] = _judge_row(r)
        if row["number"] and row["number"] in cutoffs:
            row["cutoff"] = cutoffs[row["number"]]
    with_state = [c for c in cases if c["state_file"]]
    dispositions = {"needs_info": 0, "escalated": 0, "resolved": 0}
    for c in with_state:
        if c["disposition"] in dispositions:
            dispositions[c["disposition"]] += 1
    if not with_state and meta:
        dispositions = {k: int(meta.get(k) or 0) for k in dispositions}
    time = _parse_time(meta.get("started_at")) or _parse_time(meta.get("finished_at")) or _mtime(run_dir)
    raw = [(f, str(run_dir / f)) for f in ("_run.json", "_eval.json", "_cutoffs.yaml") if (run_dir / f).exists()]
    model = str(meta.get("model") or (with_state[0]["model"] if with_state else "") or "")
    return {
        "name": name or run_dir.name,
        "kind": "cases",
        "dir": str(run_dir),
        "time": time,
        "time_iso": time.isoformat(timespec="seconds"),
        "finished": (_parse_time(meta.get("finished_at")) or time).isoformat(timespec="seconds"),
        "commit": str(meta.get("commit") or "") or None,
        "dirty": bool(meta.get("dirty")),
        "run_id": str(meta.get("run_id") or ""),
        "model": (model + (f" ({meta['effort']})" if meta.get("effort") else "")).strip(),
        "cases_total": int(meta.get("cases_total") or len(cases)),
        "present": sum(1 for c in cases if c["present"]),
        "valid": sum(1 for c in cases if c["valid"]),
        "fallbacks": sum(1 for c in with_state if c["fallback"]) if with_state else int(meta.get("fallback_count") or 0),
        "dispositions": dispositions,
        "judge": _judge_totals(eval_rows),
        "wall_s": float(meta["actual_wall_s"]) if isinstance(meta.get("actual_wall_s"), (int, float)) else None,
        "tokens_in": int(meta.get("input_tokens") or sum(c["tokens_in"] for c in cases)),
        "tokens_out": int(meta.get("output_tokens") or sum(c["tokens_out"] for c in cases)),
        "failures": [str(f) for f in (meta.get("failures") or [])],
        "notes": [str(n) for n in (meta.get("notes") or [])],
        "report": str(run_dir / "report.html") if (run_dir / "report.html").exists() else None,
        "raw": raw,
        "cases": cases,
    }


def collect_sim_run(run_dir: Path, name: str | None = None) -> dict[str, Any] | None:
    """A simulator run from `summary.json` as `evalkit.simulate.write_run` writes it."""
    run_dir = Path(run_dir)
    s = _read_json(run_dir / "summary.json")
    if not isinstance(s, dict) or not isinstance(s.get("scenarios"), list):
        return None
    scenarios = []
    verdicts: dict[str, int] = {}
    for row in s["scenarios"]:
        if not isinstance(row, dict):
            continue
        v = str(row.get("verdict") or "UNGRADED")
        verdicts[v] = verdicts.get(v, 0) + 1
        file = str(row.get("file") or "")
        scenarios.append({**row, "verdict": v, "file": str(run_dir / file) if file and (run_dir / file).exists() else None})
    time = _parse_time(s.get("timestamp")) or _mtime(run_dir)
    agent = s.get("agent") if isinstance(s.get("agent"), dict) else {}
    director = s.get("director") if isinstance(s.get("director"), dict) else {}
    model = str(agent.get("model") or "")
    if agent.get("effort"):
        model += f" ({agent['effort']})"
    if director.get("model"):
        model += f" · director {director['model']}" + (f" ({director['effort']})" if director.get("effort") else "")
    return {
        "name": name or run_dir.name,
        "kind": "sim",
        "dir": str(run_dir),
        "time": time,
        "time_iso": time.isoformat(timespec="seconds"),
        "commit": str(s.get("commit") or "") or None,
        "dirty": bool(s.get("dirty")),
        "model": model.strip(),
        "max_ticks": s.get("max_ticks"),
        "judge_on": bool(s.get("judge", True)),
        "verdicts": dict(sorted(verdicts.items())),
        "wall_s": float(s["wall_s"]) if isinstance(s.get("wall_s"), (int, float)) else None,
        "tokens_in": int(s.get("tokens_in") or 0),
        "tokens_out": int(s.get("tokens_out") or 0),
        "report": None,
        "raw": [("summary.json", str(run_dir / "summary.json"))],
        "scenarios": scenarios,
    }


def collect_runs(runs_dir: Path) -> list[dict[str, Any]]:
    """Every run under `runs_dir`, newest first. `runs_dir/sim/<stamp>/` holds simulator runs; any other
    directory with a `summary.json` of kind `sim` counts as one too; the rest are case runs."""
    runs_dir = Path(runs_dir)
    entries: list[dict[str, Any]] = []
    if not runs_dir.is_dir():
        return entries
    for d in sorted(p for p in runs_dir.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))):
        if d.name in OUTPUT_DIRS:
            continue
        if d.name == "sim":
            for s in sorted(p for p in d.iterdir() if p.is_dir() and not p.name.startswith(".")):
                e = collect_sim_run(s, name=f"sim/{s.name}")
                if e:
                    entries.append(e)
            continue
        e = collect_sim_run(d) if (d / "summary.json").exists() else None
        e = e or collect_case_run(d)
        if e:
            entries.append(e)
    entries.sort(key=lambda e: e["time"], reverse=True)
    return entries


# --------------------------------------------------------------------------- #
# Rendering
# --------------------------------------------------------------------------- #


def _esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def _short(text: Any, n: int) -> str:
    s = "" if text is None else str(text)
    return s if len(s) <= n else s[: n - 1] + "…"


def _fmt_time(dt: datetime) -> str:
    return dt.astimezone().strftime("%Y-%m-%d %H:%M")


def _fmt_dur(seconds: float | None) -> str:
    if seconds is None:
        return "-"
    return f"{seconds:.0f} s" if seconds < 60 else f"{seconds / 60:.1f} min"


def _fmt_k(n: int | None) -> str:
    if n is None:
        return "-"
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Runs board — __TITLE__</title>
<style>
:root{color-scheme:light dark;--bg:#faf7f0;--fg:#2a2622;--muted:#6b6259;--line:#e6dfd2;--card:#fffdf8;--accent:#8a5a2b;--agency:#e9f0f7;--contractor:#fff1dc;--landlord:#eaf5e6;--tenant:#f6e8f3;--other:#efece6;--ok:#2e7d32;--info:#1f5fa8;--warn:#b26a00;--bad:#b3261e}
@media (prefers-color-scheme:dark){:root{--bg:#1e1b17;--fg:#ebe5da;--muted:#a79d90;--line:#3a342d;--card:#26221d;--accent:#d9a06a;--agency:#23313f;--contractor:#3d2f1d;--landlord:#1f3320;--tenant:#3a2537;--other:#2d2925;--ok:#6fbf73;--info:#7fb0e8;--warn:#e0a24a;--bad:#e8706a}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}
main{max-width:1280px;margin:0 auto;padding:18px 16px 60px}
h1{font-size:20px;margin:0 0 4px}.sub{color:var(--muted);font-size:13px;margin-bottom:12px}
a{color:var(--accent)}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:14px}
.toolbar input[type=search]{flex:1;min-width:180px;padding:7px 9px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);font:inherit}
.toolbar select,.toolbar button{padding:5px 8px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg);font:12px/1.3 inherit;cursor:pointer}
.count{font-size:12px;color:var(--muted)}
.totals{display:flex;gap:6px 18px;flex-wrap:wrap;font-size:13px;color:var(--muted);margin-bottom:14px}.totals b{color:var(--fg);font-variant-numeric:tabular-nums}
details.run{background:var(--card);border:1px solid var(--line);border-radius:10px;margin-bottom:10px}
details.run>summary{list-style:none;cursor:pointer;padding:10px 14px;display:flex;flex-wrap:wrap;gap:5px 14px;align-items:baseline}
details.run>summary::-webkit-details-marker{display:none}
details.run>summary::before{content:"▸";color:var(--muted);font-size:12px}
details.run[open]>summary::before{content:"▾"}
details.run[open]>summary{border-bottom:1px solid var(--line)}
.name{font-weight:700;font-size:15px}
.kv{color:var(--muted);font-size:12.5px;white-space:nowrap}.kv b{color:var(--fg);font-weight:600;font-variant-numeric:tabular-nums}
.b{font-size:11px;padding:0 6px;border-radius:999px;border:1px solid var(--line);color:var(--muted);white-space:nowrap}
.b.cases{color:var(--fg);border-color:var(--accent)}.b.sim{color:var(--fg);border-color:var(--info)}
.b.resolved{border-color:var(--ok);color:var(--ok)}.b.needs_info{border-color:var(--info);color:var(--info)}.b.escalated{border-color:var(--warn);color:var(--warn)}
.b.crit,.b.FAIL,.b.ERROR{border-color:var(--bad);color:var(--bad)}.b.PASS{border-color:var(--ok);color:var(--ok)}.b.PARTIAL{border-color:var(--warn);color:var(--warn)}.b.UNGRADED{color:var(--muted)}
.group{display:inline-flex;gap:4px;flex-wrap:wrap}
.links{margin-left:auto;display:flex;gap:10px;flex-wrap:wrap;font-size:12.5px}
.clamp{display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.body{padding:8px 14px 12px}
.meta{font-size:12.5px;color:var(--muted);margin-bottom:8px}
.tbl{overflow:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:12.5px}
th,td{text-align:left;padding:5px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font-weight:600;white-space:nowrap;position:sticky;top:0;background:var(--card)}
tr:last-child td{border-bottom:none}
td.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
td.txt{min-width:200px;max-width:380px}
td.nw{white-space:nowrap}
.muted{color:var(--muted)}
.empty{color:var(--muted);padding:40px 0;text-align:center}
@media (max-width:640px){main{padding:12px 16px 40px}details.run>summary{gap:4px 10px;padding:10px 12px}.links{margin-left:0}.body{padding:8px 10px 12px}}
</style></head><body>
<main>
<h1>Runs board</h1>
<div class="sub">__SUB__</div>
<div class="toolbar"><input id="q" type="search" placeholder="filter runs by name, model, commit…"><select id="kind"><option value="">kind: any</option><option value="cases">cases</option><option value="sim">sim</option></select><button id="expand">expand all</button><button id="collapse">collapse all</button><span class="count" id="shown"></span></div>
<div class="totals">__TOTALS__</div>
__RUNS__
</main>
<script>
const TOTAL=document.querySelectorAll('details.run').length;
const q=document.getElementById('q'), k=document.getElementById('kind');
function apply(){const t=q.value.toLowerCase(), kind=k.value; let n=0; document.querySelectorAll('details.run').forEach(d=>{const ok=(!kind||d.dataset.kind===kind)&&(!t||d.dataset.hay.includes(t)); d.style.display=ok?'':'none'; if(ok)n++;}); document.getElementById('shown').textContent=n+' of '+TOTAL+' runs';}
q.addEventListener('input',apply); k.addEventListener('input',apply);
document.getElementById('expand').onclick=()=>document.querySelectorAll('details.run').forEach(d=>{if(d.style.display!=='none')d.open=true;});
document.getElementById('collapse').onclick=()=>document.querySelectorAll('details.run').forEach(d=>d.open=false);
apply();
(function(){const h=decodeURIComponent(location.hash.slice(1)); if(!h) return; const d=document.getElementById('run-'+h); if(d){d.open=true; d.scrollIntoView({block:'start'});}})();
</script>
</body></html>
"""


def _case_browser_link(cases_href: str | None, track: str, number: str | None) -> str | None:
    if not cases_href or not number:
        return None
    return f"{cases_href}#{quote(track)}/{number}"


def _case_table(e: dict[str, Any], href: Any, cases_href: str | None, track: str) -> str:
    if not e["cases"]:
        return '<div class="muted">No case records in this directory.</div>'
    head = ["Case", "Disposition", "Stage", "Judge O", "J&amp;S", "Crit", "Fallback", "Steps", "DoD", "Flags", "Tokens in/out", "Cutoff", "Next step", "Judge notes", "Files"]
    rows = []
    for c in e["cases"]:
        link = _case_browser_link(cases_href, track, c["number"])
        name = f'<a href="{_esc(link)}" title="open in the case browser">{_esc(c["id"])}</a>' if link else _esc(c["id"])
        j = c["judge"] or {}
        disp = c["disposition"] or "-"
        crit = []
        if j.get("critical_failure"):
            crit.append('<span class="b crit">critical</span>')
        if j.get("prohibited_violated"):
            crit.append(f'<span class="b crit" title="{_esc("; ".join(j["prohibited_violated"]))}">prohibited {len(j["prohibited_violated"])}</span>')
        stage = _esc(c["stage"] or "-") + (f' <span class="muted">· hold: {_esc(_short(c["hold_reason"], 120))}</span>' if c["hold_reason"] else "")
        files = []
        if c["answer"]:
            files.append(f'<a href="{href(c["answer"])}">ANSWER.md</a>')
        if c["state_file"]:
            files.append(f'<a href="{href(c["state_file"])}">_state.json</a>')
        files.append(f'<a href="{href(c["dir"])}">folder</a>')
        notes = j.get("notes") or ""
        rows.append(
            "<tr>"
            f'<td class="nw">{name}</td>'
            f'<td class="nw"><span class="b {_esc(disp)}">{_esc(disp)}</span>{"" if c["valid"] or not c["state_file"] else " <span class=\"b crit\" title=\"no valid terminal decision\">invalid</span>"}</td>'
            f'<td class="txt" title="{_esc(c["hold_reason"])}"><div class="clamp">{stage}</div></td>'
            f'<td class="num">{_esc(j.get("outcome", "-") if j else "-")}</td>'
            f'<td class="num">{_esc(j.get("judgement_safety", "-") if j else "-")}</td>'
            f'<td class="nw">{" ".join(crit) or "-"}</td>'
            f'<td class="nw">{"<span class=\"b crit\">fallback</span>" if c["fallback"] else "-"}</td>'
            f'<td class="num">{_esc(c["steps"] if c["steps"] is not None else "-")}</td>'
            f'<td class="num">{c["dod_done"]}/{c["dod_total"]}</td>'
            f'<td class="num">{c["red_flags"]}</td>'
            f'<td class="num">{_fmt_k(c["tokens_in"])}/{_fmt_k(c["tokens_out"])}</td>'
            f'<td class="num">{_esc(c["cutoff"] if c["cutoff"] is not None else "-")}</td>'
            f'<td class="txt" title="{_esc(c["next_step"])}"><div class="clamp">{_esc(_short(c["next_step"], TEXT_CHARS)) or "-"}</div></td>'
            f'<td class="txt" title="{_esc(notes)}"><div class="clamp">{_esc(_short(notes, NOTE_CHARS)) or "-"}</div></td>'
            f'<td class="nw">{" · ".join(files)}</td>'
            "</tr>"
        )
    return '<div class="tbl"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"


def _sim_table(e: dict[str, Any], href: Any) -> str:
    if not e["scenarios"]:
        return '<div class="muted">No scenarios in this run.</div>'
    head = ["Scenario", "Title", "Ticks", "Final", "Expected", "Should", "Must-not", "End state", "Verdict", "Ended", "Tokens in/out", "File"]
    rows = []
    for s in e["scenarios"]:
        final = f'{s.get("final_disposition") or "none"}/{s.get("final_stage") or "-"}' + (" (fallback)" if s.get("fallback") else "")
        expected = s.get("expected") or f'{s.get("expected_disposition") or ""}/{s.get("expected_stage") or ""}'
        should = f'{s.get("should_passed", 0)}/{s.get("should_total", 0)}' if s.get("should_total") else "-"
        must_not = f'{s.get("must_not_violated", 0)} of {s.get("must_not_total", 0)}' if s.get("must_not_total") else "-"
        crit = ' <span class="b crit">critical</span>' if s.get("critical_failure") else ""
        file = f'<a href="{href(s["file"])}">{_esc(Path(s["file"]).name)}</a>' if s.get("file") else "-"
        rows.append(
            "<tr>"
            f'<td class="nw">{_esc(s.get("id"))}</td>'
            f'<td class="txt">{_esc(s.get("title"))}</td>'
            f'<td class="num">{_esc(s.get("ticks", "-"))}</td>'
            f'<td class="nw">{_esc(final)}</td>'
            f'<td class="nw">{_esc(expected)}</td>'
            f'<td class="num">{should}</td>'
            f'<td class="num">{must_not}</td>'
            f'<td class="nw">{_esc(s.get("end_state_match") or "-")}</td>'
            f'<td class="nw"><span class="b {_esc(s["verdict"])}">{_esc(s["verdict"])}</span>{crit}</td>'
            f'<td class="txt" title="{_esc(s.get("end_reason"))}"><div class="clamp">{_esc(_short(s.get("end_reason"), TEXT_CHARS)) or "-"}</div></td>'
            f'<td class="num">{_fmt_k(s.get("tokens_in"))}/{_fmt_k(s.get("tokens_out"))}</td>'
            f'<td class="nw">{file}</td>'
            "</tr>"
        )
    return '<div class="tbl"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"


def _summary_line(e: dict[str, Any], href: Any) -> str:
    parts = [f'<span class="name">{_esc(e["name"])}</span>', f'<span class="b {e["kind"]}">{e["kind"]}</span>', f'<span class="kv">{_esc(_fmt_time(e["time"]))}</span>']
    if e.get("commit"):
        parts.append(f'<span class="kv">commit <b>{_esc(e["commit"])}{"*" if e.get("dirty") else ""}</b></span>')
    if e["kind"] == "cases":
        parts.append(f'<span class="kv">cases <b>{e["cases_total"]}</b> · present <b>{e["present"]}</b> · valid <b>{e["valid"]}</b> · fallbacks <b>{e["fallbacks"]}</b></span>')
        parts.append('<span class="group">' + "".join(f'<span class="b {k}">{k} {v}</span>' for k, v in e["dispositions"].items()) + "</span>")
        j = e["judge"]
        if j:
            parts.append(f'<span class="kv">judge outcome <b>{j["outcome_sum"]}/{j["outcome_max"]}</b> · J&amp;S <b>{j["js_sum"]}/{j["js_max"]}</b> · critical <b>{j["critical"]}</b></span>')
        else:
            parts.append('<span class="kv">no judge file</span>')
    else:
        parts.append(f'<span class="kv">scenarios <b>{len(e["scenarios"])}</b></span>')
        parts.append('<span class="group">' + "".join(f'<span class="b {_esc(k)}">{_esc(k)} {n}</span>' for k, n in e["verdicts"].items()) + "</span>")
    parts.append(f'<span class="kv">wall <b>{_fmt_dur(e.get("wall_s"))}</b></span>')
    if e.get("model"):
        parts.append(f'<span class="kv">{_esc(e["model"])}</span>')
    links = []
    if e.get("report"):
        links.append(f'<a href="{href(e["report"])}">report</a>')
    for label, p in e["raw"]:
        links.append(f'<a href="{href(p)}">{_esc(label)}</a>')
    links.append(f'<a href="{href(e["dir"])}">folder</a>')
    parts.append('<span class="links">' + " ".join(links) + "</span>")
    return "".join(parts)


def _run_block(e: dict[str, Any], href: Any, cases_href: str | None, track: str) -> str:
    hay = " ".join(str(x) for x in (e["name"], e["kind"], e.get("model"), e.get("commit"), e.get("run_id", ""))).lower()
    meta = []
    if e["kind"] == "cases":
        meta.append(f'tokens in/out {_fmt_k(e["tokens_in"])}/{_fmt_k(e["tokens_out"])}')
        if e.get("run_id"):
            meta.append(f'run id {_esc(e["run_id"])}')
        if e.get("failures"):
            meta.append(f'failures: {_esc("; ".join(e["failures"][:5]))}')
        if e.get("notes"):
            meta.append(_esc("; ".join(e["notes"])))
        body = _case_table(e, href, cases_href, track)
    else:
        meta.append(f'tokens in/out {_fmt_k(e["tokens_in"])}/{_fmt_k(e["tokens_out"])}')
        if e.get("max_ticks") is not None:
            meta.append(f'max ticks {_esc(e["max_ticks"])}')
        if not e.get("judge_on", True):
            meta.append("played without the judge")
        body = _sim_table(e, href)
    return (
        f'<details class="run" id="run-{_esc(e["name"])}" data-kind="{e["kind"]}" data-hay="{_esc(hay)}">'
        f"<summary>{_summary_line(e, href)}</summary>"
        f'<div class="body"><div class="meta">{" · ".join(meta)}</div>{body}</div></details>'
    )


def _totals(entries: list[dict[str, Any]]) -> str:
    cases = [e for e in entries if e["kind"] == "cases"]
    sims = [e for e in entries if e["kind"] == "sim"]
    parts = [f"<span>runs <b>{len(entries)}</b></span>", f"<span>case runs <b>{len(cases)}</b></span>", f"<span>sim runs <b>{len(sims)}</b></span>"]
    if cases:
        parts.append(f"<span>case records <b>{sum(e['present'] for e in cases)}</b></span>")
        judged = [e for e in cases if e["judge"]]
        if judged:
            parts.append(f"<span>judged <b>{sum(e['judge']['rows'] for e in judged)}</b> · critical <b>{sum(e['judge']['critical'] for e in judged)}</b></span>")
    if sims:
        v: dict[str, int] = {}
        for e in sims:
            for k, n in e["verdicts"].items():
                v[k] = v.get(k, 0) + n
        parts.append("<span>episodes " + " · ".join(f"{_esc(k)} <b>{n}</b>" for k, n in sorted(v.items())) + "</span>")
    return "".join(parts)


def build_page(entries: list[dict[str, Any]], out: Path, *, track: str = DEFAULT_TRACK, cases_index: Path | None = None) -> Path:
    """Write the board to `out`. Case links point at the case browser next to the board (`../cases/index.html`)
    when it exists, or at `cases_index` when given."""
    out = Path(out)
    base = out.parent
    base.mkdir(parents=True, exist_ok=True)
    cases_index = Path(cases_index) if cases_index else base.parent / "cases" / "index.html"
    cases_href = quote(os.path.relpath(cases_index, base).replace(os.sep, "/")) if cases_index.exists() else None

    def href(path: str) -> str:
        return quote(os.path.relpath(path, base).replace(os.sep, "/"))

    stamp = datetime.now().astimezone().isoformat(timespec="minutes")
    runs_html = "".join(_run_block(e, href, cases_href, track) for e in entries) or '<div class="empty">No runs found.</div>'
    sub = f"{len(entries)} runs, newest first · generated {stamp}" + (f' · <a href="{_esc(cases_href)}">case browser</a>' if cases_href else " · no case browser yet (make cases-browser)")
    page = PAGE.replace("__TITLE__", _esc(f"{len(entries)} runs · {stamp}")).replace("__SUB__", sub).replace("__TOTALS__", _totals(entries)).replace("__RUNS__", runs_html)
    out.write_text(page, encoding="utf-8")
    return out


def main(runs: Path, out: Path, open_browser: bool = False) -> int:
    entries = collect_runs(Path(runs))
    out = build_page(entries, Path(out))
    n_cases = sum(1 for e in entries if e["kind"] == "cases")
    n_sim = len(entries) - n_cases
    print(f"{out} ({out.stat().st_size / 1e3:.0f} KB, {len(entries)} runs: {n_cases} case runs, {n_sim} sim runs)")
    if open_browser:
        subprocess.run(["open", str(out)], check=False)
    return 0
