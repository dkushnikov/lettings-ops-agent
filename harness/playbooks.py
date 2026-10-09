"""Playbooks: Agent-Skills-style procedures, one per case type.

A playbook says *how* a case type is worked; the rulebook says *whether* an
action is allowed. The model picks one playbook per case through the
`use_playbook` harness tool, which keeps the context small (progressive
disclosure) and records the choice.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class Playbook:
    name: str
    description: str
    case_types: list[str]
    body: str
    version: str = "0.1"
    source: str = ""
    path: Path | None = None


def _split_frontmatter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            return meta, parts[2].lstrip("\n")
    return {}, text


def load_playbooks(root: str | Path) -> list[Playbook]:
    root = Path(root)
    books: list[Playbook] = []
    if not root.exists():
        return books
    for skill in sorted(root.glob("*/SKILL.md")):
        meta, body = _split_frontmatter(skill.read_text(encoding="utf-8"))
        books.append(
            Playbook(
                name=str(meta.get("name") or skill.parent.name),
                description=str(meta.get("description", "")).strip(),
                case_types=[str(c) for c in (meta.get("case_types") or [])],
                body=body.strip(),
                version=str(meta.get("version", "0.1")),
                source=str(meta.get("source", "")),
                path=skill,
            )
        )
    return books


@dataclass
class PlaybookLibrary:
    books: list[Playbook] = field(default_factory=list)

    @classmethod
    def load(cls, root: str | Path) -> "PlaybookLibrary":
        return cls(load_playbooks(root))

    def get(self, name: str) -> Playbook | None:
        for b in self.books:
            if b.name == name:
                return b
        return None

    def for_case_type(self, case_type: str) -> Playbook | None:
        ct = case_type.strip().lower()
        for b in self.books:
            if ct in [c.lower() for c in b.case_types]:
                return b
        return None

    def catalog(self) -> str:
        if not self.books:
            return "(no playbooks installed)"
        lines = []
        for b in self.books:
            types = ", ".join(b.case_types) or "-"
            lines.append(f"- {b.name}: {b.description} [case types: {types}]")
        return "\n".join(lines)
