"""Tool manifest overlay (`agent/tools.yaml`).

On the day the environment hands us tools with a name, a description and an
input schema and nothing else. The gate needs more: is it a read or a write,
which mandate capability it needs, where the £ amount lives, is it idempotent,
can a read confirm it. This file is the place to say so without touching code.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .schema import ToolClass, ToolSpec
from .tools import ToolRegistry

_FIELDS = ("tool_class", "authority", "amount_field", "idempotent", "reversible", "side_effect", "reconcile_with", "description")


def load_manifest(path: str | Path) -> dict[str, dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        return {}
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    tools = data.get("tools", data)
    return {str(name): dict(cfg or {}) for name, cfg in tools.items()}


def annotate(spec: ToolSpec, overlay: dict[str, Any]) -> ToolSpec:
    update: dict[str, Any] = {}
    for f in _FIELDS:
        if f in overlay and overlay[f] is not None:
            update[f] = ToolClass(overlay[f]) if f == "tool_class" else overlay[f]
    return spec.model_copy(update=update) if update else spec


def apply_manifest(registry: ToolRegistry, manifest: dict[str, dict[str, Any]]) -> ToolRegistry:
    """Return the same registry with specs annotated from the manifest.

    Tools present in the manifest but missing from the registry are ignored;
    tools missing from the manifest keep their declared spec. A write tool that
    the manifest does not know stays a write without authority, which the gate
    routes to a human.
    """
    for name, tool in registry.tools.items():
        if name in manifest:
            tool.spec = annotate(tool.spec, manifest[name])
    return registry
