"""Sanitisation: secrets never reach a log, untrusted text never becomes prose.

Two jobs:
1. `redact_secrets` scrubs anything that looks like a credential before it is
   written to a trace or a record.
2. `quote_untrusted` turns a span of untrusted content (an email, a transcript)
   into a short, labelled, escaped quotation. Records cite evidence; they do not
   replay it, so an injected instruction cannot ride into the judge's context.
"""

from __future__ import annotations

import json
import re
from typing import Any

_SECRET_PATTERNS = [
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{8,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._\-]{16,}"),
    re.compile(r"(?i)(api[_\-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9._\-]{12,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9\-]{10,}"),
]

_CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_WS = re.compile(r"\s+")
# Tool-call pseudo-markup the model sometimes writes into free text (observed in two of fifty
# PM records: `<parameter name="case_type">`). It is never content; a judge reading the record
# must not see it.
_TOOL_MARKUP = re.compile(r"</?(?:antml:)?(?:invoke|parameter|function_calls|function_results)\b[^>]*>")


def strip_tool_markup(text: str) -> str:
    out = _TOOL_MARKUP.sub("", text)
    return re.sub(r"[ \t]+\n", "\n", out)


def first_sentence(text: str, max_chars: int = 160) -> str:
    """The first sentence of a free-text field, markup-free, capped — used as a recap when none was given."""
    t = _WS.sub(" ", strip_tool_markup(text or "")).strip()
    if not t:
        return ""
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    out = m.group(1) if m else t
    return out if len(out) <= max_chars else out[: max_chars - 1].rstrip() + "…"


def redact_secrets(text: str) -> str:
    out = strip_tool_markup(text)
    for pat in _SECRET_PATTERNS:
        out = pat.sub("[REDACTED]", out)
    return out


def quote_untrusted(text: str, max_chars: int = 240) -> str:
    """Short, labelled quotation of untrusted content."""
    cleaned = _WS.sub(" ", _CONTROL.sub("", text)).strip()
    if len(cleaned) > max_chars:
        cleaned = cleaned[: max_chars - 1].rstrip() + "…"
    cleaned = cleaned.replace("`", "'")
    return f"`[quoted, untrusted] {cleaned}`"


def truncate(text: str, max_chars: int = 600) -> str:
    text = text if isinstance(text, str) else str(text)
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def jsonable(obj: Any) -> Any:
    """Best-effort conversion of tool results and SDK objects to JSON-safe data."""
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [jsonable(v) for v in obj]
    if hasattr(obj, "model_dump"):
        try:
            return jsonable(obj.model_dump(mode="json"))
        except Exception:  # pragma: no cover - defensive
            pass
    if hasattr(obj, "to_dict"):
        try:
            return jsonable(obj.to_dict())
        except Exception:  # pragma: no cover - defensive
            pass
    return str(obj)


def to_json(obj: Any, **kwargs: Any) -> str:
    return redact_secrets(json.dumps(jsonable(obj), ensure_ascii=False, default=str, **kwargs))
