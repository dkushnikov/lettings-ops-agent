"""Case loading: a folder with `case.yaml` and artefact files, a JSON array, or a
loose directory of files when the environment comes without a manifest.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from .schema import Artefact, ArtefactKind, Case

_KIND_HINTS = {
    "email": ArtefactKind.email,
    "mail": ArtefactKind.email,
    "transcript": ArtefactKind.call_transcript,
    "call": ArtefactKind.call_transcript,
    "ticket": ArtefactKind.ticket,
    "record": ArtefactKind.record,
    "crm": ArtefactKind.record,
    "tenancy": ArtefactKind.record,
    "note": ArtefactKind.note,
    "doc": ArtefactKind.document,
    "agreement": ArtefactKind.document,
    "certificate": ArtefactKind.document,
}

_DEFAULT_TRUST = {
    ArtefactKind.email: "untrusted",
    ArtefactKind.call_transcript: "untrusted",
    ArtefactKind.ticket: "untrusted",
    ArtefactKind.record: "authoritative",
    ArtefactKind.document: "authoritative",
    ArtefactKind.note: "informational",
    ArtefactKind.other: "informational",
}


def guess_kind(filename: str) -> ArtefactKind:
    low = filename.lower()
    for hint, kind in _KIND_HINTS.items():
        if hint in low:
            return kind
    if low.endswith((".json", ".csv")):
        return ArtefactKind.record
    if low.endswith(".pdf"):
        return ArtefactKind.document
    return ArtefactKind.other


def read_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader  # optional dependency

            reader = PdfReader(str(path))
            return "\n".join((page.extract_text() or "") for page in reader.pages)
        except Exception as e:  # noqa: BLE001
            return f"[PDF could not be read: {e}]"
    if suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return json.dumps(data, indent=2, ensure_ascii=False)
        except Exception:  # noqa: BLE001
            return path.read_text(encoding="utf-8", errors="replace")
    return path.read_text(encoding="utf-8", errors="replace")


def load_case_dir(case_dir: Path) -> Case:
    """A case directory: `case.yaml` listing artefacts, plus the artefact files."""
    manifest_path = case_dir / "case.yaml"
    if not manifest_path.exists():
        return load_loose_dir(case_dir)
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    artefacts: list[Artefact] = []
    for item in manifest.get("artefacts", []):
        file = case_dir / item["file"]
        kind = ArtefactKind(item.get("kind") or guess_kind(file.name).value)
        artefacts.append(
            Artefact(
                id=item.get("id") or file.stem,
                kind=kind,
                title=item.get("title", file.name),
                source=str(file.relative_to(case_dir)),
                content=read_text(file),
                metadata=item.get("metadata", {}) or {},
                trust=item.get("trust") or _DEFAULT_TRUST[kind],
            )
        )
    expected = case_dir / "expected.yaml"
    received = manifest.get("received_at")
    return Case(
        id=str(manifest.get("id") or case_dir.name),
        title=str(manifest.get("title", "") or ""),
        received_at=str(received) if received is not None else None,
        artefacts=artefacts,
        metadata=manifest.get("metadata", {}) or {},
        env=manifest.get("env", {}) or {},
        expected_path=str(expected) if expected.exists() else None,
    )


def load_loose_dir(case_dir: Path) -> Case:
    """No manifest: every file is an artefact; kind and trust are guessed."""
    artefacts: list[Artefact] = []
    for file in sorted(p for p in case_dir.iterdir() if p.is_file() and not p.name.startswith(".")):
        if file.name in {"expected.yaml", "expected.json"}:
            continue
        kind = guess_kind(file.name)
        artefacts.append(
            Artefact(
                id=file.stem,
                kind=kind,
                title=file.name,
                source=file.name,
                content=read_text(file),
                trust=_DEFAULT_TRUST[kind],
            )
        )
    expected = case_dir / "expected.yaml"
    return Case(id=case_dir.name, title=case_dir.name, artefacts=artefacts, expected_path=str(expected) if expected.exists() else None)


def load_cases_json(path: Path) -> list[Case]:
    """A JSON array of cases: [{id, title, artefacts: [{id, kind, trust, title, content}]}]."""
    data = json.loads(path.read_text(encoding="utf-8"))
    cases: list[Case] = []
    for item in data:
        arts = []
        for j, a in enumerate(item.get("artefacts", []), start=1):
            kind = ArtefactKind(a.get("kind", "other"))
            content = a.get("content")
            if not isinstance(content, str):
                content = json.dumps(content, indent=2, ensure_ascii=False)
            arts.append(Artefact(id=a.get("id") or f"a{j}", kind=kind, title=a.get("title", ""), source=a.get("source", ""), content=content, trust=a.get("trust") or _DEFAULT_TRUST[kind], metadata=a.get("metadata", {}) or {}))
        received = item.get("received_at")
        cases.append(Case(id=str(item["id"]), title=str(item.get("title", "") or ""), received_at=str(received) if received is not None else None, artefacts=arts, metadata=item.get("metadata", {}) or {}, env=item.get("env", {}) or {}))
    return cases


def load_cases(path: str | Path) -> list[Case]:
    p = Path(path)
    if p.is_file() and p.suffix == ".json":
        return load_cases_json(p)
    if (p / "case.yaml").exists():
        return [load_case_dir(p)]
    cases: list[Case] = []
    for sub in sorted(x for x in p.iterdir() if x.is_dir() and not x.name.startswith((".", "_"))):
        cases.append(load_case_dir(sub))
    return cases


def case_summary(case: Case) -> dict[str, Any]:
    return {
        "id": case.id,
        "title": case.title,
        "artefacts": [{"id": a.id, "kind": a.kind.value, "trust": a.trust, "chars": len(a.content)} for a in case.artefacts],
    }
