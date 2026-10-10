"""Command line: run · demo · eval · sim · mutate · rehearse · freeze · capacity · video-check · rules-extract."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from .adapters.generic import GenericAdapter
from .llm import Settings, TokenBucket, load_dotenv, make_client
from .loop import CaseAgent
from .playbooks import PlaybookLibrary
from .rulebook import Rulebook
from .runner import estimate_wall_seconds, previous_t_case, run_batch
from .schema import Case
from .tools import EnvironmentAdapter

ROOT = Path(__file__).resolve().parent.parent


def build_adapter(name: str, tools_module: str | None, args: argparse.Namespace | None = None) -> EnvironmentAdapter:
    if name == "mock":
        from mockworld.adapter import MockAdapter  # local package

        return MockAdapter()
    if name == "dwelly":
        from .adapters.dwelly import DwellyCasesAdapter, load_cutoffs

        return DwellyCasesAdapter(
            hide_outcome=not bool(getattr(args, "show_outcome", False)),
            cutoff=getattr(args, "cutoff", None),
            cutoffs=load_cutoffs(getattr(args, "cutoffs", None)),
            auto_cutoff=getattr(args, "auto_cutoff", None),
            id_style=getattr(args, "id_style", "track") or "track",
            with_attachments=not bool(getattr(args, "no_attachments", False)),
        )
    return GenericAdapter(tools_module)


def build_agent(settings: Settings) -> CaseAgent:
    rulebook = Rulebook.load(ROOT / settings.rulebook_path if not Path(settings.rulebook_path).is_absolute() else settings.rulebook_path)
    playbooks = PlaybookLibrary.load(ROOT / settings.playbooks_dir if not Path(settings.playbooks_dir).is_absolute() else settings.playbooks_dir)
    client = make_client(settings)
    bucket = TokenBucket(settings.tpm_budget)
    return CaseAgent(settings, client, rulebook, playbooks, bucket=bucket)


def _select(cases: list[Case], only: list[str] | None, limit: int | None) -> list[Case]:
    if only:
        wanted = set(only)
        cases = [c for c in cases if c.id in wanted]
    if limit:
        cases = cases[:limit]
    return cases


def _parse_deadline(text: str | None) -> datetime | None:
    if not text:
        return None
    now = datetime.now().astimezone()
    hh, mm = text.split(":")
    return now.replace(hour=int(hh), minute=int(mm), second=0, microsecond=0)


def cmd_run(args: argparse.Namespace) -> int:
    settings = Settings.from_env(model=args.model, effort=args.effort, concurrency=args.concurrency, case_timeout_s=args.timeout, max_steps=args.max_steps, reviewer=args.reviewer)
    adapter = build_adapter(args.adapter, args.tools_module, args)
    cases = _select(adapter.load_cases(Path(args.cases)), args.case, args.limit)
    if not cases:
        print("No cases found.", file=sys.stderr)
        return 2
    if args.adapter == "dwelly":
        import yaml as _yaml

        from .adapters.dwelly import write_expected

        eff = dict(getattr(adapter, "effective_cutoffs", {}) or {})
        Path(args.out).mkdir(parents=True, exist_ok=True)
        if eff:
            (Path(args.out) / "_cutoffs.yaml").write_text(_yaml.safe_dump(eff, sort_keys=True), encoding="utf-8")
            print(f"decision points for {len(eff)} case(s) written to {Path(args.out) / '_cutoffs.yaml'}")
        if getattr(args, "emit_expected", False):
            n_exp = write_expected(Path(args.cases), Path(args.out) / "_expected", cutoff=args.cutoff, cutoffs=eff, id_style=args.id_style or "track")
            print(f"wrote {n_exp} hidden-outcome expectation file(s) to {Path(args.out) / '_expected'} (judge only)")
    agent = build_agent(settings)
    meta = asyncio.run(run_batch(cases, adapter, agent, settings, Path(args.out), force=args.force, deadline=_parse_deadline(args.deadline), progress=not args.no_progress))
    return 0 if meta.completed == meta.cases_total else 1


def cmd_demo(args: argparse.Namespace) -> int:
    args.out = args.out or "runs/demo"
    args.limit = 1 if not args.case else None
    args.force = True
    rc = cmd_run(args)
    out = Path(args.out)
    for d in sorted(out.iterdir()):
        if (d / "ANSWER.md").exists():
            print((d / "ANSWER.md").read_text(encoding="utf-8"))
            break
    return rc


def cmd_capacity(args: argparse.Namespace) -> int:
    t_case = args.t_case or previous_t_case(Path(args.out))
    est = estimate_wall_seconds(args.cases, args.concurrency, t_case)
    print(f"{args.cases} cases · concurrency {args.concurrency} · t_case {t_case:.0f}s → ~{est/60:.1f} min (with 25% margin)")
    return 0


def cmd_eval(args: argparse.Namespace) -> int:
    try:
        from evalkit.judge import main as judge_main
    except ImportError:
        print("evalkit.judge not available yet.", file=sys.stderr)
        return 2
    return judge_main(answers=Path(args.answers), cases=Path(args.cases), model=args.model)


def cmd_sim(args: argparse.Namespace) -> int:
    from evalkit.simulate import main as sim_main
    from evalkit.simulate import sim_settings_from

    ids = [s for raw in (args.scenario or []) for s in raw.split(",") if s.strip()]
    agent = None
    sim_settings = None
    if not args.list:
        settings = Settings.from_env(model=args.model, effort=args.effort, case_timeout_s=args.timeout, max_steps=args.max_steps, reviewer=args.reviewer)
        agent = build_agent(settings)
        sim_settings = sim_settings_from(settings, args.sim_model, args.sim_effort)
    return sim_main(
        scenario_ids=ids,
        run_all=args.all,
        list_only=args.list,
        scenarios_path=Path(args.scenarios),
        agent=agent,
        sim_settings=sim_settings,
        max_ticks=args.max_ticks,
        concurrency=args.concurrency,
        judge=not args.no_judge,
        verbose=args.verbose,
    )


def cmd_mutate(args: argparse.Namespace) -> int:
    try:
        from evalkit.mutate import main as mutate_main
    except ImportError:
        print("evalkit.mutate not available yet.", file=sys.stderr)
        return 2
    return mutate_main(case=Path(args.case), out=Path(args.out), axes=args.axes)


def cmd_rules_extract(args: argparse.Namespace) -> int:
    try:
        from evalkit.rules_extract import main as rx_main
    except ImportError:
        print("evalkit.rules_extract not available yet.", file=sys.stderr)
        return 2
    return rx_main(docs=Path(args.docs), out=Path(args.out), model=args.model)


def cmd_report(args: argparse.Namespace) -> int:
    from evalkit.report import main as report_main

    return report_main(run=Path(args.run), cases=Path(args.cases) if args.cases else None, open_browser=args.open)


def cmd_cases_browser(args: argparse.Namespace) -> int:
    from evalkit.casebrowser import main as browser_main

    return browser_main(cases=Path(args.cases), out=Path(args.out), runs=[Path(r) for r in (args.runs or [])], open_browser=args.open)


def cmd_rehearse(args: argparse.Namespace) -> int:
    """Fresh clone → sync → run two fixtures → check outputs. What a judge would do."""
    tmp = Path(tempfile.mkdtemp(prefix="loa-rehearse-"))
    try:
        subprocess.run(["git", "clone", "-q", str(ROOT), str(tmp / "repo")], check=True)
        repo = tmp / "repo"
        subprocess.run(["uv", "sync", "-q"], cwd=repo, check=True)
        env = dict(os.environ)
        cmd = [
            "uv", "run", "python", "-m", "harness.cli", "run", "--cases", str(ROOT / args.cases), "--out", str(tmp / "out"),
            "--adapter", "mock", "--limit", str(args.limit), "--force", "--no-progress",
        ]
        subprocess.run(cmd, cwd=repo, check=True, env=env)
        produced = sorted(p.parent.name for p in (tmp / "out").glob("*/ANSWER.md"))
        print(f"rehearsal OK: {len(produced)} record(s) from a fresh clone: {', '.join(produced)}")
        return 0 if produced else 1
    finally:
        if not args.keep:
            shutil.rmtree(tmp, ignore_errors=True)
        else:
            print(f"kept {tmp}")


def cmd_freeze(args: argparse.Namespace) -> int:
    subprocess.run(["git", "add", "-A"], cwd=ROOT, check=False)
    subprocess.run(["git", "commit", "-q", "-m", f"freeze: {args.tag}"], cwd=ROOT, check=False)
    subprocess.run(["git", "tag", "-f", args.tag], cwd=ROOT, check=True)
    sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    line = f"{stamp} tag={args.tag} commit={sha}\n"
    (ROOT / "FREEZE.txt").open("a", encoding="utf-8").write(line)
    print(line.strip())
    return 0


def cmd_video_check(args: argparse.Namespace) -> int:
    p = Path(args.path)
    if not p.exists():
        print(f"missing: {p}", file=sys.stderr)
        return 2
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration,size", "-of", "json", str(p)], capture_output=True, text=True)
    if out.returncode != 0:
        print(out.stderr, file=sys.stderr)
        return 2
    info = json.loads(out.stdout)["format"]
    dur = float(info["duration"])
    size_mb = int(info["size"]) / 1e6
    ok = dur <= 60.5
    print(f"{p}: {dur:.1f}s, {size_mb:.1f} MB → {'OK' if ok else 'TOO LONG (max 60s)'}")
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="lettings-ops-agent")
    sub = p.add_subparsers(dest="cmd", required=True)

    def add_run_args(sp: argparse.ArgumentParser, demo: bool = False) -> None:
        sp.add_argument("--cases", default="fixtures")
        sp.add_argument("--out", default=None if demo else "runs/latest")
        sp.add_argument("--adapter", choices=["mock", "generic", "dwelly"], default="mock")
        sp.add_argument("--tools-module", default=None, help="pkg.module:build_registry for the generic adapter")
        sp.add_argument("--cutoff", type=int, default=None, help="dwelly: show only history events up to this number (decision point)")
        sp.add_argument("--cutoffs", default=None, help="dwelly: YAML file mapping case number → last visible event (per-case decision points)")
        sp.add_argument("--auto-cutoff", default=None, help="dwelly: pick decision points automatically: first-external | fraction:0.4")
        sp.add_argument("--id-style", choices=["track", "number"], default="track", help="dwelly: record directory names — 'number' gives ANSWERS/<case number>/ for submission")
        sp.add_argument("--show-outcome", action="store_true", help="dwelly: keep overview/outcome visible (never for evaluation)")
        sp.add_argument("--no-attachments", action="store_true", help="dwelly: skip attachment text")
        sp.add_argument("--emit-expected", action="store_true", help="dwelly: write hidden outcome + later events to <out>/_expected for the judge")
        sp.add_argument("--concurrency", type=int, default=None)
        sp.add_argument("--model", default=None)
        sp.add_argument("--effort", default=None)
        sp.add_argument("--timeout", type=float, default=None, help="per-case seconds")
        sp.add_argument("--max-steps", type=int, default=None)
        sp.add_argument("--reviewer", choices=["rules", "llm"], default=None)
        sp.add_argument("--case", action="append", help="run only these case ids")
        sp.add_argument("--limit", type=int, default=None)
        sp.add_argument("--force", action="store_true", help="ignore checkpoints")
        sp.add_argument("--deadline", default=None, help="HH:MM local; cases not started by then get fallback records")
        sp.add_argument("--no-progress", action="store_true")

    sp = sub.add_parser("run", help="process a batch of cases")
    add_run_args(sp)
    sp.set_defaults(fn=cmd_run)

    sp = sub.add_parser("demo", help="run one case and print its ANSWER.md")
    add_run_args(sp, demo=True)
    sp.set_defaults(fn=cmd_demo)

    sp = sub.add_parser("capacity", help="estimate wall time for a batch")
    sp.add_argument("--cases", type=int, required=True)
    sp.add_argument("--concurrency", type=int, default=4)
    sp.add_argument("--t-case", type=float, default=None)
    sp.add_argument("--out", default="runs/latest")
    sp.set_defaults(fn=cmd_capacity)

    sp = sub.add_parser("eval", help="judge answers against expected.yaml files")
    sp.add_argument("--answers", default="runs/latest")
    sp.add_argument("--cases", default="fixtures")
    sp.add_argument("--model", default=None)
    sp.set_defaults(fn=cmd_eval)

    sp = sub.add_parser("sim", help="play multi-actor scenarios (tenant, landlord, contractor) against the agent and grade them")
    sp.add_argument("--scenario", "-s", action="append", help="scenario id, e.g. SC-01 or 1; repeatable or comma-separated")
    sp.add_argument("--all", action="store_true", help="run every scenario")
    sp.add_argument("--list", action="store_true", help="list scenarios and exit")
    sp.add_argument("--scenarios", default=str(ROOT / "evalkit" / "actors" / "scenarios.yaml"))
    sp.add_argument("--max-ticks", type=int, default=10, help="agent runs per scenario")
    sp.add_argument("--concurrency", type=int, default=2, help="scenarios in parallel")
    sp.add_argument("--model", default=None, help="agent model")
    sp.add_argument("--effort", default=None, help="agent effort")
    sp.add_argument("--sim-model", default=None, help="director and judge model (default: agent model)")
    sp.add_argument("--sim-effort", default=None, help="director and judge effort (default: medium)")
    sp.add_argument("--timeout", type=float, default=None, help="per-tick agent seconds")
    sp.add_argument("--max-steps", type=int, default=None)
    sp.add_argument("--reviewer", choices=["rules", "llm"], default=None)
    sp.add_argument("--no-judge", action="store_true", help="play the episodes without grading")
    sp.add_argument("--verbose", "-v", action="store_true", help="full message bodies and director notes")
    sp.set_defaults(fn=cmd_sim)

    sp = sub.add_parser("mutate", help="derive adversarial variants of a case")
    sp.add_argument("--case", required=True)
    sp.add_argument("--out", default="runs/mutations")
    sp.add_argument("--axes", nargs="*", default=None)
    sp.set_defaults(fn=cmd_mutate)

    sp = sub.add_parser("rules-extract", help="extract candidate rules from environment documents into staging")
    sp.add_argument("--docs", required=True)
    sp.add_argument("--out", default="agent/rulebook_staging.md")
    sp.add_argument("--model", default=None)
    sp.set_defaults(fn=cmd_rules_extract)

    sp = sub.add_parser("report", help="self-contained HTML report for a run directory")
    sp.add_argument("--run", default="runs/latest")
    sp.add_argument("--cases", default="fixtures")
    sp.add_argument("--open", action="store_true")
    sp.set_defaults(fn=cmd_report)

    sp = sub.add_parser("cases-browser", help="static HTML browser over the organisers' cases (search, filters, history cut points, run overlay)")
    sp.add_argument("--cases", required=True, help="track directory, e.g. ../HackatonPublicCases/Property Management")
    sp.add_argument("--out", default="runs/cases/index.html")
    sp.add_argument("--runs", action="append", default=None, help="run directory to overlay (repeatable)")
    sp.add_argument("--open", action="store_true")
    sp.set_defaults(fn=cmd_cases_browser)

    sp = sub.add_parser("rehearse", help="fresh clone → sync → run → verify")
    sp.add_argument("--cases", default="fixtures")
    sp.add_argument("--limit", type=int, default=2)
    sp.add_argument("--keep", action="store_true")
    sp.set_defaults(fn=cmd_rehearse)

    sp = sub.add_parser("freeze", help="commit, tag and record the hash")
    sp.add_argument("--tag", required=True)
    sp.set_defaults(fn=cmd_freeze)

    sp = sub.add_parser("video-check", help="check the demo video length")
    sp.add_argument("path", nargs="?", default="video/demo.mp4")
    sp.set_defaults(fn=cmd_video_check)
    return p


def main(argv: list[str] | None = None) -> int:
    load_dotenv(str(ROOT / ".env"))
    args = build_parser().parse_args(argv)
    return int(args.fn(args) or 0)


if __name__ == "__main__":
    sys.exit(main())
