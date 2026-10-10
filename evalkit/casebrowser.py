"""Static case browser for the organisers' case format.

One self-contained `index.html` (no CDN, no external assets, vanilla JS) with a
searchable, filterable list of cases on the left and the selected case on the
right: Case · History (with a "cut here" decision point and a cutoff copier) ·
Attachments · Agent (optional overlay of one or more run directories).
"""

from __future__ import annotations

import html
import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from harness.adapters.dwelly import AGENCY_MARKERS, auto_cutoff, iter_case_dirs, parse_history, parse_index
from harness.loader import read_text

MONEY_RE = re.compile(r"£\s?\d[\d,]*(?:\.\d{2})?")
ATTACH_EXCERPT = 4000
NUM_RE = re.compile(r"(\d{3})$")


def party_of(sender: str) -> str:
    s = (sender or "").lower()
    if any(m in s for m in AGENCY_MARKERS):
        return "agency"
    if "contractor" in s or "provider" in s or "supplier" in s or "engineer" in s:
        return "contractor"
    if "landlord" in s:
        return "landlord"
    if "tenant" in s or "occupant" in s:
        return "tenant"
    return "other" if s else "agency"


def collect_case(case_dir: Path, out_dir: Path) -> dict[str, Any]:
    track = case_dir.parent.name
    parsed = parse_index((case_dir / "index.md").read_text(encoding="utf-8", errors="replace"))
    history_md = (case_dir / "history.md").read_text(encoding="utf-8", errors="replace") if (case_dir / "history.md").exists() else ""
    events = parse_history(history_md)
    ev_rows = []
    channels: dict[str, int] = {}
    parties: dict[str, int] = {}
    for e in events:
        party = party_of(e.sender)
        channels[e.channel] = channels.get(e.channel, 0) + 1
        parties[party] = parties.get(party, 0) + 1
        ev_rows.append({"number": e.number, "timestamp": e.timestamp, "channel": e.channel, "from": e.sender, "to": e.recipient, "party": party, "body": e.body})
    attachments = []
    att_dir = case_dir / "attachments"
    if att_dir.exists():
        for f in sorted(p for p in att_dir.iterdir() if p.is_file()):
            if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif"):
                text = f"[image: {f.name}]"
            else:
                try:
                    text = read_text(f)
                except Exception as e:  # noqa: BLE001
                    text = f"[could not read: {e}]"
            attachments.append({"name": f.name, "size": f.stat().st_size, "href": os.path.relpath(f, out_dir), "excerpt": text[:ATTACH_EXCERPT], "truncated": len(text) > ATTACH_EXCERPT})
    all_text = "\n".join([parsed.initial_request, parsed.overview, parsed.outcome, history_md])
    money = sorted(set(m.replace(" ", "") for m in MONEY_RE.findall(all_text)))
    return {
        "track": track,
        "number": case_dir.name,
        "id": f"{track}/{case_dir.name}",
        "title": parsed.title,
        "source_role": parsed.details.get("source_role", ""),
        "status": parsed.details.get("status", ""),
        "created": parsed.details.get("created", ""),
        "updated": parsed.details.get("updated", ""),
        "completed": parsed.details.get("completed", ""),
        "property": parsed.details.get("property", ""),
        "initial_request": parsed.initial_request,
        "overview": parsed.overview,
        "outcome": parsed.outcome,
        "attachments": attachments,
        "events": ev_rows,
        "n_events": len(ev_rows),
        "channels": channels,
        "parties": parties,
        "has_attachments": bool(attachments),
        "money": money,
        "first_external": auto_cutoff(events, "first-external"),
        "dir": os.path.relpath(case_dir, out_dir),
    }


def collect_cases(root: Path, out_dir: Path) -> list[dict[str, Any]]:
    return [collect_case(d, out_dir) for d in iter_case_dirs(root)]


def _short(value: Any, n: int) -> str:
    text = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, default=str)
    return text if len(text) <= n else text[: n - 1] + "…"


def _compact_action(a: dict[str, Any]) -> dict[str, Any]:
    gate = a.get("gate") or {}
    return {
        "seq": a.get("seq"),
        "tool": a.get("tool"),
        "cls": a.get("tool_class"),
        "status": a.get("status"),
        "verdict": gate.get("verdict"),
        "rules": gate.get("rule_ids") or [],
        "reason": gate.get("reason") or "",
        "input": _short(a.get("input") or {}, 420),
        "receipt": _short(a.get("receipt") or a.get("error") or "", 300),
    }


def _compact_trace(path: Path) -> list[dict[str, Any]]:
    """The run's trace.jsonl reduced to what the replay needs: model turns, playbook, gate verdicts, tool results, finish."""
    out: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            ev = json.loads(line)
        except Exception:  # noqa: BLE001
            continue
        kind = ev.get("event")
        if kind == "model_turn":
            u = ev.get("usage") or {}
            out.append({"k": "turn", "step": ev.get("step"), "stop": ev.get("stop_reason"), "in": u.get("input"), "out": u.get("output"), "cache": u.get("cache_read")})
        elif kind == "playbook":
            out.append({"k": "playbook", "name": ev.get("name"), "urgency": ev.get("urgency"), "case_type": ev.get("case_type")})
        elif kind == "gate":
            out.append({"k": "gate", "tool": ev.get("tool"), "verdict": ev.get("verdict"), "rules": ev.get("rules") or [], "reason": ev.get("reason") or ""})
        elif kind == "tool_result":
            out.append({"k": "result", "tool": ev.get("tool"), "status": ev.get("status"), "attempts": ev.get("attempts"), "receipt": _short(ev.get("receipt") or ev.get("error") or "", 300)})
        elif kind:
            out.append({"k": kind, **{key: _short(v, 200) for key, v in ev.items() if key not in ("event", "ts")}})
    return out


def load_runs(runs: list[Path] | None) -> dict[str, dict[str, Any]]:
    """Overlay data from run directories, keyed by run name then case number."""
    out: dict[str, dict[str, Any]] = {}
    for run in runs or []:
        run = Path(run)
        if not run.exists():
            continue
        entry: dict[str, Any] = {"cutoffs": {}, "evals": {}, "cases": {}}
        cut = run / "_cutoffs.yaml"
        if cut.exists():
            try:
                entry["cutoffs"] = {str(k).zfill(3): int(v) for k, v in (yaml.safe_load(cut.read_text(encoding="utf-8")) or {}).items()}
            except Exception:  # noqa: BLE001
                entry["cutoffs"] = {}
        ev = run / "_eval.json"
        if ev.exists():
            try:
                for row in json.loads(ev.read_text(encoding="utf-8")):
                    m = NUM_RE.search(str(row.get("case", "")))
                    if m:
                        entry["evals"][m.group(1)] = {"outcome": row.get("outcome"), "judgement_safety": row.get("judgement_safety"), "critical_failure": row.get("critical_failure"), "notes": row.get("notes", "")}
            except Exception:  # noqa: BLE001
                pass
        for d in sorted(p for p in run.iterdir() if p.is_dir() and not p.name.startswith("_")):
            m = NUM_RE.search(d.name)
            if not m or not (d / "ANSWER.md").exists():
                continue
            rec: dict[str, Any] = {"dir": d.name, "answer": (d / "ANSWER.md").read_text(encoding="utf-8", errors="replace")}
            st = d / "_state.json"
            if st.exists():
                try:
                    s = json.loads(st.read_text(encoding="utf-8"))
                    rec.update({"disposition": s.get("disposition"), "fallback": s.get("fallback"), "steps": s.get("steps"), "urgency": s.get("urgency"), "flags": [f.get("kind") for f in s.get("red_flags", [])]})
                    rec["status"] = {k: s.get(k, "") for k in ("recap", "stage", "hold_reason", "next_step")}
                    rec["notes"] = list(s.get("reviewer_notes", [])) + list(s.get("system_notes", []))
                    rec["actions"] = [_compact_action(a) for a in s.get("actions", [])]
                except Exception:  # noqa: BLE001
                    pass
            tr = d / "trace.jsonl"
            if tr.exists():
                rec["trace"] = _compact_trace(tr)
            entry["cases"][m.group(1)] = rec
        out[run.name] = entry
    return out


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Case browser — __TITLE__</title>
<style>
:root{color-scheme:light dark;--bg:#faf7f0;--fg:#2a2622;--muted:#6b6259;--line:#e6dfd2;--card:#fffdf8;--accent:#8a5a2b;--agency:#e9f0f7;--contractor:#fff1dc;--landlord:#eaf5e6;--tenant:#f6e8f3;--other:#efece6;--dim:.38}
@media (prefers-color-scheme:dark){:root{--bg:#1e1b17;--fg:#ebe5da;--muted:#a79d90;--line:#3a342d;--card:#26221d;--accent:#d9a06a;--agency:#23313f;--contractor:#3d2f1d;--landlord:#1f3320;--tenant:#3a2537;--other:#2d2925}}
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;display:grid;grid-template-columns:380px 1fr;grid-template-rows:100vh}
aside{border-right:1px solid var(--line);display:flex;flex-direction:column;min-height:0}
main{min-height:0;overflow:auto;padding:18px 24px}
.toolbar{padding:10px 12px;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:6px}
.toolbar input[type=search],.toolbar input[type=text]{width:100%;padding:7px 9px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg);font:inherit}
.frow{display:flex;gap:6px;flex-wrap:wrap}
.frow select,.frow input[type=number]{flex:1;min-width:90px;padding:4px 6px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg);font:12px/1.3 inherit}
.frow label{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:4px}
.count{font-size:12px;color:var(--muted)}
ul.cases{list-style:none;margin:0;padding:0;overflow:auto;flex:1}
ul.cases li{padding:8px 12px;border-bottom:1px solid var(--line);cursor:pointer}
ul.cases li:hover{background:var(--card)}ul.cases li.sel{background:var(--card);box-shadow:inset 3px 0 0 var(--accent)}
.num{font-weight:600;font-variant-numeric:tabular-nums}.ttl{display:block;font-size:13px}
.badges{display:flex;gap:4px;flex-wrap:wrap;margin-top:3px}
.b{font-size:11px;padding:0 6px;border-radius:999px;border:1px solid var(--line);color:var(--muted);white-space:nowrap}
.b.run{color:var(--fg);border-color:var(--accent)}
.b.resolved{border-color:#2e7d32}.b.needs_info{border-color:#1f5fa8}.b.escalated{border-color:#b26a00}.b.crit{border-color:#b3261e;color:#b3261e}
h1{font-size:20px;margin:0 0 4px}.sub{color:var(--muted);margin-bottom:12px;font-size:13px}
.tabs{display:flex;gap:4px;border-bottom:1px solid var(--line);margin-bottom:14px}
.tabs button{background:none;border:none;border-bottom:2px solid transparent;padding:8px 12px;font:inherit;color:var(--muted);cursor:pointer}
.tabs button.on{color:var(--fg);border-bottom-color:var(--accent)}
.pane{display:none}.pane.on{display:block}
table.kv{border-collapse:collapse;margin-bottom:14px}table.kv td{padding:3px 10px 3px 0;vertical-align:top}table.kv td:first-child{color:var(--muted);white-space:nowrap}
.box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin-bottom:12px;white-space:pre-wrap;word-break:break-word}
.hidden-note{color:var(--muted);font-style:italic}
.ctl{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:12px;font-size:13px}
.ctl input[type=number]{width:70px;padding:4px 6px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg)}
.ctl button{padding:4px 10px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg);cursor:pointer;font:inherit}
.ev{border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:8px;background:var(--other)}
.ev.agency{background:var(--agency)}.ev.contractor{background:var(--contractor)}.ev.landlord{background:var(--landlord)}.ev.tenant{background:var(--tenant)}
.ev.dim{opacity:var(--dim)}
.evh{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:12px;color:var(--muted);margin-bottom:4px}
.evh .n{font-weight:700;color:var(--fg)}.evh .ch{border:1px solid var(--line);border-radius:999px;padding:0 6px}
.evh .cut{margin-left:auto;font-size:11px;padding:1px 7px;border:1px solid var(--line);border-radius:6px;background:var(--card);cursor:pointer;color:var(--fg)}
.evb{white-space:pre-wrap;word-break:break-word}
.evb.long{max-height:7.5em;overflow:hidden;position:relative}.evb.long::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2.5em;background:linear-gradient(transparent,var(--card))}
.more{font-size:12px;color:var(--accent);cursor:pointer;background:none;border:none;padding:0;margin-top:4px}
pre{white-space:pre-wrap;word-break:break-word;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px;font-size:12.5px}
.att h3{margin:8px 0 4px;font-size:14px}.att a{color:var(--accent)}
.empty{color:var(--muted);padding:40px 0;text-align:center}
kbd{border:1px solid var(--line);border-radius:4px;padding:0 4px;font-size:11px}
@media (max-width:900px){body{grid-template-columns:1fr;grid-template-rows:45vh 55vh}aside{border-right:none;border-bottom:1px solid var(--line)}}
.replay{margin:8px 0 12px;border:1px solid var(--line);border-radius:8px;padding:8px;background:var(--panel)}
.replay .steps{list-style:none;margin:6px 0 0;padding:0}
.replay li.st{display:none;border-top:1px dashed var(--line);padding:6px 0}
.replay li.st.show{display:block}
.replay .sth{margin-bottom:3px}
.replay .act{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;margin:3px 0 3px 10px;padding:3px 6px;border-left:3px solid var(--line);white-space:pre-wrap}
.replay .act.write{border-left-color:var(--accent)}
.replay .act.playbook{border-left-color:#8a6d3b}
.replay .act.finish{border-left-color:#2a7;font-weight:600}
.replay .act .tag{font-size:10px;letter-spacing:.04em;opacity:.7}
.replay .gate.deny,.replay .gate.escalate,.replay .act.deny{color:#b03a2e}
.replay .gate.needs_approval{color:#b26a00}
.replay .inp{opacity:.85;margin:2px 0}
.replay .res{opacity:.75}
.kv.status td:first-child{width:90px;font-weight:600}
details.rec summary{cursor:pointer;color:var(--accent);margin:6px 0}
</style></head><body>
<aside>
  <div class="toolbar">
    <input id="q" type="search" placeholder="Search title, request, overview, history…  (press / to focus)">
    <div class="frow">
      <select id="fTrack"><option value="">track: any</option></select>
      <select id="fChannel"><option value="">channel: any</option></select>
      <select id="fParty"><option value="">party: any</option></select>
    </div>
    <div class="frow">
      <select id="fRole"><option value="">source role: any</option></select>
      <select id="fStatus"><option value="">status: any</option></select>
      <select id="fSort"><option value="number">sort: number</option><option value="events">sort: events</option><option value="created">sort: created</option></select>
    </div>
    <div class="frow">
      <input id="fMin" type="number" placeholder="events ≥" min="0"><input id="fMax" type="number" placeholder="events ≤" min="0">
      <label><input id="fAtt" type="checkbox"> attachments</label>
      <label><input id="fRun" type="checkbox"> has run</label>
    </div>
    <input id="fHist" type="text" placeholder="text in history only (e.g. 'invoice', 'hold')">
    <div class="count" id="count"></div>
  </div>
  <ul class="cases" id="list"></ul>
</aside>
<main>
  <div id="detail"><div class="empty">Select a case. <kbd>↑</kbd> <kbd>↓</kbd> to move, <kbd>/</kbd> to search.</div></div>
</main>
<script id="data" type="application/json">__DATA__</script>
<script id="runs" type="application/json">__RUNS__</script>
<script>
const CASES = JSON.parse(document.getElementById('data').textContent);
const RUNS = JSON.parse(document.getElementById('runs').textContent);
const RUN_NAMES = Object.keys(RUNS);
const state = { q:'', track:'', channel:'', party:'', role:'', status:'', sort:'number', min:null, max:null, att:false, run:false, hist:'', sel:null, tab:'case', hideOutcome:true, cutoffs:{}, expanded:{} };
const $ = id => document.getElementById(id);
const esc = s => String(s==null?'':s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function uniq(arr){ return [...new Set(arr.filter(Boolean))].sort(); }
function fillSelect(id, values, prefix){ const s=$(id); values.forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;s.appendChild(o);}); }
fillSelect('fTrack', uniq(CASES.map(c=>c.track)));
fillSelect('fChannel', uniq(CASES.flatMap(c=>Object.keys(c.channels))));
fillSelect('fParty', uniq(CASES.flatMap(c=>Object.keys(c.parties))));
fillSelect('fRole', uniq(CASES.map(c=>c.source_role)));
fillSelect('fStatus', uniq(CASES.map(c=>c.status)));
function statusHtml(x){
  const st=x.rec.status; if(!st) return '';
  return `<table class="kv status"><tr><td>Recap</td><td>${esc(st.recap||'-')}</td></tr><tr><td>Stage</td><td>${esc(st.stage||'-')}${st.hold_reason?' · <b>hold:</b> '+esc(st.hold_reason):''}</td></tr><tr><td>Next step</td><td>${esc(st.next_step||'-')}</td></tr></table>`;
}
function replayHtml(x,xi){
  const tr=x.rec.trace||[]; const acts=x.rec.actions||[]; if(!tr.length&&!acts.length) return '';
  const steps=[]; let cur=null; let k=0;
  for(const ev of tr){
    if(ev.k==='turn'){ cur={title:`Step ${ev.step} · model turn`, meta:`in ${fmtK(ev.in)} · out ${fmtK(ev.out)}${ev.cache?' · cache '+fmtK(ev.cache):''}`, acts:[]}; steps.push(cur); continue; }
    if(!cur){ cur={title:'Before the first turn', meta:'', acts:[]}; steps.push(cur); }
    if(ev.k==='playbook'){ cur.acts.push({cls:'playbook', html:`<b>use_playbook</b> ${esc(ev.name)} · case type ${esc(ev.case_type||'-')} · urgency <b>${esc(ev.urgency||'-')}</b> → the gate now uses this urgency`}); }
    else if(ev.k==='gate'){
      // every action passes the gate once, in ledger order; a denied or approval-needing write never reaches a tool_result
      const a=acts[k]||{}; k++; const write=(a.cls||'')==='write'; const v=ev.verdict||a.verdict||''; const rules=(ev.rules&&ev.rules.length?ev.rules:(a.rules||[])).join(', ');
      const head=`<span class="tag">${write?'WRITE':'read'}</span> <b>${esc(ev.tool)}</b> <span class="gate ${esc(v)}">gate: ${esc(v||'-')}${rules?' · '+esc(rules):''}${ev.reason&&ev.reason!=='read'?' · '+esc(ev.reason):''}</span>${a.input&&a.input!=='{}'?`<div class="inp">${esc(a.input)}</div>`:''}`;
      if(v==='allow'){ cur.pending={head, write, v}; }
      else { cur.pending=null; cur.acts.push({cls:(write?'write ':'read ')+esc(v), html:head+`<div class="res">→ ${esc(a.status||'blocked')} · not executed</div>`}); }
    }
    else if(ev.k==='result'){
      const g=cur.pending||{head:`<b>${esc(ev.tool)}</b>`, write:false, v:''}; cur.pending=null;
      cur.acts.push({cls:(g.write?'write ':'read ')+esc(g.v), html:g.head+`<div class="res">→ ${esc(ev.status)}${ev.attempts>1?' after '+ev.attempts+' attempts':''}${ev.receipt?' · '+esc(ev.receipt):''}</div>`});
    }
    else if(ev.k==='terminal'){ cur.acts.push({cls:'finish', html:`<b>finish</b> ${esc(Object.entries(ev).filter(([kk])=>kk!=='k').map(([kk,vv])=>kk+': '+vv).join(' · '))}`}); }
    else { cur.acts.push({cls:'other', html:`<b>${esc(ev.k)}</b> ${esc(Object.entries(ev).filter(([kk])=>kk!=='k').map(([kk,vv])=>kk+': '+vv).join(' · '))}`}); }
  }
  // blocked / needs_approval actions never produce a tool_result event: show them from the ledger
  for(const a of acts.slice(k)){ const tgt=steps[steps.length-1]||(steps.push({title:'Ledger',meta:'',acts:[]}),steps[steps.length-1]); tgt.acts.push({cls:'write '+esc(a.verdict||''), html:`<span class="tag">WRITE</span> <b>${esc(a.tool)}</b> <span class="gate ${esc(a.verdict||'')}">gate: ${esc(a.verdict||'-')}${(a.rules||[]).length?' · '+esc(a.rules.join(', ')):''}${a.reason?' · '+esc(a.reason):''}</span>${a.input&&a.input!=='{}'?`<div class="inp">${esc(a.input)}</div>`:''}<div class="res">→ ${esc(a.status)}</div>`}); }
  const fin={title:`Finish · ${(x.rec.disposition||'?').toUpperCase()}`, meta:(x.rec.notes||[]).join(' · '), acts:[]};
  steps.push(fin);
  const lis=steps.map(st=>`<li class="st"><div class="sth"><b>${esc(st.title)}</b> <span class="count">${esc(st.meta)}</span></div>${st.acts.map(a=>`<div class="act ${a.cls}">${a.html}</div>`).join('')}</li>`).join('');
  return `<div class="replay" id="replay-${xi}"><div class="ctl"><button class="rplay">▶ replay</button><button class="rnext">next step</button><button class="rall">show all</button><span class="count rcount"></span><span class="count">what the agent read, what the gate allowed, what was written, how it finished</span></div><ol class="steps">${lis}</ol></div>`;
}
function fmtK(n){ return n==null?'-':(n>=1000?(n/1000).toFixed(1)+'k':String(n)); }
function runInfo(c){ const out=[]; for (const r of RUN_NAMES){ const rec=RUNS[r].cases[c.number]; if(rec) out.push({run:r, rec, eval:RUNS[r].evals[c.number]||null, cutoff:RUNS[r].cutoffs[c.number]}); } return out; }
function haystack(c){ return (c.title+'\n'+c.initial_request+'\n'+c.overview+'\n'+c.events.map(e=>e.body).join('\n')).toLowerCase(); }
function filtered(){
  const q=state.q.toLowerCase(), h=state.hist.toLowerCase();
  let rows = CASES.filter(c => {
    if (state.track && c.track!==state.track) return false;
    if (state.channel && !c.channels[state.channel]) return false;
    if (state.party && !c.parties[state.party]) return false;
    if (state.role && c.source_role!==state.role) return false;
    if (state.status && c.status!==state.status) return false;
    if (state.min!=null && c.n_events<state.min) return false;
    if (state.max!=null && c.n_events>state.max) return false;
    if (state.att && !c.has_attachments) return false;
    if (state.run && runInfo(c).length===0) return false;
    if (q && !haystack(c).includes(q)) return false;
    if (h && !c.events.some(e=>e.body.toLowerCase().includes(h))) return false;
    return true;
  });
  const key = state.sort;
  rows.sort((a,b)=> key==='events' ? b.n_events-a.n_events : key==='created' ? (a.created||'').localeCompare(b.created||'') : a.id.localeCompare(b.id));
  return rows;
}
let VISIBLE = [];
function renderList(){
  VISIBLE = filtered();
  $('count').textContent = `${VISIBLE.length} of ${CASES.length} cases`;
  const ul=$('list'); ul.innerHTML='';
  for (const c of VISIBLE){
    const li=document.createElement('li'); li.dataset.id=c.id; if (state.sel===c.id) li.classList.add('sel');
    const runs = runInfo(c).map(ri => { const d=ri.rec.disposition||'?'; const ev=ri.eval? ` · judge ${ri.eval.outcome??'-'}/${ri.eval.judgement_safety??'-'}`:''; const crit = ri.eval&&ri.eval.critical_failure ? ' crit' : ''; return `<span class="b run ${esc(d)}${crit}">${esc(ri.run)}: ${esc(d)}${esc(ev)}</span>`; }).join('');
    li.innerHTML = `<span class="num">${esc(c.number)}</span> <span class="ttl">${esc(c.title.replace(/^Case \d+:\s*/,''))}</span>
      <div class="badges"><span class="b">${c.n_events} events</span>${c.has_attachments?'<span class="b">📎 '+c.attachments.length+'</span>':''}${c.first_external?'<span class="b">first external: '+c.first_external+'</span>':''}${c.money.length?'<span class="b">'+esc(c.money.slice(0,3).join(' '))+'</span>':''}${runs}</div>`;
    li.onclick=()=>select(c.id);
    ul.appendChild(li);
  }
}
function select(id){ state.sel=id; location.hash='#'+encodeURIComponent(id); renderList(); renderDetail(); const li=document.querySelector(`li[data-id="${CSS.escape(id)}"]`); if(li) li.scrollIntoView({block:'nearest'}); }
function caseById(id){ return CASES.find(c=>c.id===id); }
function currentCutoff(c){ if (state.cutoffs[c.id]!=null) return state.cutoffs[c.id]; for (const ri of runInfo(c)) if (ri.cutoff!=null) return ri.cutoff; return c.n_events; }
function renderDetail(){
  const c=caseById(state.sel); const box=$('detail');
  if(!c){ box.innerHTML='<div class="empty">Select a case.</div>'; return; }
  const tabs=[['case','Case'],['history','History'],['attachments','Attachments ('+c.attachments.length+')']];
  const ri=runInfo(c); if (ri.length) tabs.push(['agent','Agent ('+ri.length+')']);
  let h=`<h1>${esc(c.title)}</h1><div class="sub">${esc(c.track)} · ${esc(c.number)} · ${esc(c.property)} · created ${esc(c.created)} · source role: ${esc(c.source_role)} · <a href="${esc(c.dir)}" style="color:var(--accent)">folder</a></div>`;
  h+='<div class="tabs">'+tabs.map(([k,l])=>`<button data-tab="${k}" class="${state.tab===k?'on':''}">${esc(l)}</button>`).join('')+'</div>';
  // Case
  h+=`<div class="pane ${state.tab==='case'?'on':''}" id="pane-case">
    <table class="kv"><tr><td>Property</td><td>${esc(c.property)}</td></tr><tr><td>Source role</td><td>${esc(c.source_role)}</td></tr><tr><td>Created</td><td>${esc(c.created)}</td></tr>
    <tr><td>Status / completed</td><td>${state.hideOutcome?'<span class="hidden-note">hidden</span>':esc(c.status)+' · '+esc(c.completed)}</td></tr>
    <tr><td>Events</td><td>${c.n_events} · channels: ${esc(Object.entries(c.channels).map(([k,v])=>k+' '+v).join(', '))} · parties: ${esc(Object.entries(c.parties).map(([k,v])=>k+' '+v).join(', '))}</td></tr>
    ${c.money.length?`<tr><td>Amounts</td><td>${esc(c.money.join(', '))}</td></tr>`:''}</table>
    <h3>Initial request</h3><div class="box">${esc(c.initial_request)}</div>
    <div class="ctl"><label><input type="checkbox" id="hideOutcome" ${state.hideOutcome?'checked':''}> hide overview and outcome (practice decision points honestly)</label></div>
    <h3>Overview</h3><div class="box">${state.hideOutcome?'<span class="hidden-note">hidden — untick above to reveal</span>':esc(c.overview)}</div>
    <h3>Outcome</h3><div class="box">${state.hideOutcome?'<span class="hidden-note">hidden — untick above to reveal</span>':esc(c.outcome)}</div>
  </div>`;
  // History
  const cut=currentCutoff(c); const vis=c.events.filter(e=>e.number<=cut).length;
  h+=`<div class="pane ${state.tab==='history'?'on':''}" id="pane-history">
    <div class="ctl">cut after event <input type="number" id="cutN" min="0" max="${c.n_events}" value="${cut}"> <span>visible: <b id="visN">${vis}</b> of ${c.n_events}</span>
    <button id="cutFirst" title="first message from an outside party">first external (${c.first_external??'-'})</button>
    <button id="cutAll">show all</button>
    <button id="copyCut">copy "${esc(c.number)}": ${cut} for cutoffs.yaml</button><span id="copied" class="count"></span></div>`;
  for (const e of c.events){
    const long = e.body.length>600 && !state.expanded[c.id+'#'+e.number];
    h+=`<div class="ev ${esc(e.party)} ${e.number>cut?'dim':''}" id="ev-${e.number}"><div class="evh"><span class="n">#${String(e.number).padStart(3,'0')}</span><span>${esc(e.timestamp)}</span><span class="ch">${esc(e.channel)}</span><span>${esc(e.from||'-')} → ${esc(e.to||'-')}</span><button class="cut" data-n="${e.number}">cut here</button></div>
      <div class="evb ${long?'long':''}">${esc(e.body)}</div>${e.body.length>600?`<button class="more" data-k="${esc(c.id+'#'+e.number)}">${long?'show more':'show less'}</button>`:''}</div>`;
  }
  h+='</div>';
  // Attachments
  h+=`<div class="pane ${state.tab==='attachments'?'on':''}" id="pane-attachments">`+(c.attachments.length?c.attachments.map(a=>`<div class="att"><h3><a href="${esc(a.href)}">${esc(a.name)}</a> <span class="count">${(a.size/1024).toFixed(0)} KB${a.truncated?' · excerpt':''}</span></h3><pre>${esc(a.excerpt)}</pre></div>`).join(''):'<div class="empty">No attachments.</div>')+'</div>';
  // Agent
  if (ri.length){
    h+=`<div class="pane ${state.tab==='agent'?'on':''}" id="pane-agent">`+ri.map((x,xi)=>`<h3>${esc(x.run)} · <span class="b run ${esc(x.rec.disposition||'')}">${esc(x.rec.disposition||'?')}</span> ${x.rec.fallback?'<span class="b crit">fallback</span>':''} · urgency ${esc(x.rec.urgency||'-')} · steps ${esc(x.rec.steps??'-')} · cutoff ${x.cutoff??'-'} · flags: ${esc((x.rec.flags||[]).join(', ')||'none')}</h3>${statusHtml(x)}${replayHtml(x,xi)}${x.eval?`<div class="box">judge: outcome ${esc(x.eval.outcome)}/2 · judgement&safety ${esc(x.eval.judgement_safety)}/2${x.eval.critical_failure?' · <b>CRITICAL FAILURE</b>':''}\n${esc(x.eval.notes||'')}</div>`:''}<details class="rec"><summary>ANSWER.md</summary><pre>${esc(x.rec.answer)}</pre></details>`).join('')+'</div>';
  }
  box.innerHTML=h;
  box.querySelectorAll('.tabs button').forEach(b=>b.onclick=()=>{state.tab=b.dataset.tab; renderDetail();});
  box.querySelectorAll('.replay').forEach(rp=>{
    const items=[...rp.querySelectorAll('li.st')]; let i=0, timer=null; const cnt=rp.querySelector('.rcount');
    const show=n=>{ items.slice(0,n).forEach(li=>li.classList.add('show')); i=Math.min(n,items.length); cnt.textContent=i+' / '+items.length; if(items[i-1]) items[i-1].scrollIntoView({block:'nearest'}); if(i>=items.length&&timer){clearInterval(timer); timer=null;} };
    rp.querySelector('.rplay').onclick=()=>{ if(timer){clearInterval(timer); timer=null; return;} if(i>=items.length){ items.forEach(li=>li.classList.remove('show')); i=0; } show(i+1); timer=setInterval(()=>show(i+1), 1100); };
    rp.querySelector('.rnext').onclick=()=>show(i+1);
    rp.querySelector('.rall').onclick=()=>show(items.length);
    show(0);
  });
  const ho=$('hideOutcome'); if(ho) ho.onchange=()=>{state.hideOutcome=ho.checked; renderDetail();};
  const cn=$('cutN'); if(cn) cn.onchange=()=>{state.cutoffs[c.id]=Math.max(0,Math.min(c.n_events,parseInt(cn.value||'0',10))); renderDetail();};
  const cf=$('cutFirst'); if(cf) cf.onclick=()=>{state.cutoffs[c.id]=c.first_external||c.n_events; renderDetail();};
  const ca=$('cutAll'); if(ca) ca.onclick=()=>{state.cutoffs[c.id]=c.n_events; renderDetail();};
  const cc=$('copyCut'); if(cc) cc.onclick=()=>{const t=`"${c.number}": ${currentCutoff(c)}`; navigator.clipboard.writeText(t).then(()=>{$('copied').textContent='copied '+t;}).catch(()=>{$('copied').textContent=t;});};
  box.querySelectorAll('button.cut').forEach(b=>b.onclick=()=>{state.cutoffs[c.id]=parseInt(b.dataset.n,10); renderDetail(); const el=document.getElementById('ev-'+b.dataset.n); if(el) el.scrollIntoView({block:'center'});});
  box.querySelectorAll('button.more').forEach(b=>b.onclick=()=>{state.expanded[b.dataset.k]=!state.expanded[b.dataset.k]; renderDetail();});
}
function bind(id, key, parse){ $(id).addEventListener('input', ev=>{ state[key]=parse?parse(ev.target.value):ev.target.value; renderList(); }); }
bind('q','q'); bind('fTrack','track'); bind('fChannel','channel'); bind('fParty','party'); bind('fRole','role'); bind('fStatus','status'); bind('fSort','sort'); bind('fHist','hist');
bind('fMin','min',v=>v===''?null:parseInt(v,10)); bind('fMax','max',v=>v===''?null:parseInt(v,10));
$('fAtt').addEventListener('change', ev=>{state.att=ev.target.checked; renderList();});
$('fRun').addEventListener('change', ev=>{state.run=ev.target.checked; renderList();});
document.addEventListener('keydown', ev=>{
  const tag=(document.activeElement&&document.activeElement.tagName)||'';
  if (ev.key==='/' && tag!=='INPUT' && tag!=='SELECT'){ ev.preventDefault(); $('q').focus(); return; }
  if ((ev.key==='ArrowDown'||ev.key==='ArrowUp') && tag!=='INPUT' && tag!=='SELECT' && tag!=='TEXTAREA'){
    ev.preventDefault(); if(!VISIBLE.length) return; let i=VISIBLE.findIndex(c=>c.id===state.sel); i = ev.key==='ArrowDown' ? Math.min(VISIBLE.length-1, i+1) : Math.max(0, i-1); select(VISIBLE[i].id);
  }
});
renderList();
(function(){ const h=decodeURIComponent(location.hash.slice(1)); if (h && caseById(h)) { state.sel=h; renderList(); renderDetail(); } })();
</script>
</body></html>
"""


def build_page(cases: list[dict[str, Any]], runs: dict[str, dict[str, Any]], out: Path, title: str = "") -> Path:
    out.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(cases, ensure_ascii=False).replace("</", "<\\/")
    runs_json = json.dumps(runs, ensure_ascii=False).replace("</", "<\\/")
    stamp = datetime.now().astimezone().isoformat(timespec="minutes")
    page = PAGE.replace("__DATA__", data).replace("__RUNS__", runs_json).replace("__TITLE__", html.escape(title or f"{len(cases)} cases · {stamp}"))
    out.write_text(page, encoding="utf-8")
    return out


def main(cases: Path, out: Path, runs: list[Path] | None = None, open_browser: bool = False) -> int:
    out = Path(out)
    collected = collect_cases(Path(cases), out.parent)
    overlay = load_runs([Path(r) for r in (runs or [])])
    build_page(collected, overlay, out, title=f"{Path(cases).name} · {len(collected)} cases")
    size_mb = out.stat().st_size / 1e6
    print(f"{out} ({size_mb:.1f} MB, {len(collected)} cases, runs: {', '.join(overlay) or 'none'})")
    if open_browser:
        subprocess.run(["open", str(out)], check=False)
    return 0
