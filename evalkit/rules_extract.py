"""Rules extraction: environment documents → candidate rules in the staging file.

Never writes to `agent/rulebook.yaml`. A human reads the staging rows, keeps
the ones that are real rules, and merges them with source ids.
"""

from __future__ import annotations

import asyncio
from datetime import datetime
from pathlib import Path

from harness.llm import Settings, create_message, load_dotenv, make_client
from harness.loader import read_text

ROOT = Path(__file__).resolve().parent.parent

DEFAULT_PROMPT = """You extract operating rules from a lettings agency's documents for a policy rulebook.
For every rule you find, output one markdown table row:
| proposed_id | rule (one sentence, operational) | source document | verbatim quote (short) | status (sop/in_force/prior) | rulebook section (capabilities/approvals/prohibited/escalation_triggers/emergency/clocks/source_hierarchy) | condition keys (max_amount_gbp, amount_gbp_over, urgency_in, urgency_not, requires_consent_field, from) |
Only rules that change what an agent may do, must ask, must never do, or by when. Quote the document; never invent. If a document contains no rules, say so in one line."""


def _collect(docs: Path) -> list[tuple[str, str]]:
    files = [docs] if docs.is_file() else sorted(p for p in docs.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt", ".pdf", ".json", ".yaml", ".yml", ".csv"})
    return [(str(p.relative_to(docs) if docs.is_dir() else p.name), read_text(p)) for p in files]


async def _extract(settings: Settings, docs: Path) -> str:
    prompt_path = ROOT / "docs" / "rules-extraction-prompt.md"
    system = prompt_path.read_text(encoding="utf-8") if prompt_path.exists() else DEFAULT_PROMPT
    client = make_client(settings)
    chunks = _collect(docs)
    body = "\n\n".join(f"<document name=\"{name}\">\n{text[:60000]}\n</document>" for name, text in chunks)
    response = await create_message(
        client,
        settings,
        system=[{"type": "text", "text": system}],
        messages=[{"role": "user", "content": f"Documents follow. Extract candidate rules.\n\n{body}"}],
        tools=None,
        max_tokens=8000,
    )
    return "\n".join(b.text for b in response.content if getattr(b, "type", None) == "text")


def main(docs: Path, out: Path, model: str | None = None) -> int:
    load_dotenv(str(ROOT / ".env"))
    settings = Settings.from_env(model=model)
    text = asyncio.run(_extract(settings, docs))
    stamp = datetime.now().astimezone().isoformat(timespec="minutes")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("a", encoding="utf-8") as fh:
        fh.write(f"\n\n## Extraction {stamp} from `{docs}` (model {settings.model}) — REVIEW BEFORE MERGING\n\n{text}\n")
    print(f"appended candidate rules to {out}")
    return 0
