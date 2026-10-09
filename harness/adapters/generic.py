"""Generic adapter: cases from files, tools from a module, annotated by the manifest.

This is the adapter to fill on the day. Cases come from a folder of case
directories, a loose directory, or a JSON array (see `harness.loader`). Tools
come from a Python module exposing `build_registry(case) -> ToolRegistry`
(wrapping whatever the environment provides: REST calls, an MCP client, local
functions), and `agent/tools.yaml` annotates them for the gate.
"""

from __future__ import annotations

import importlib
from pathlib import Path
from typing import Callable

from ..loader import load_cases
from ..manifest import apply_manifest, load_manifest
from ..schema import Case
from ..tools import ToolRegistry

ROOT = Path(__file__).resolve().parent.parent.parent


class GenericAdapter:
    name = "generic"

    def __init__(self, tools_module: str | None = None, manifest_path: str | Path | None = None):
        self._builder: Callable[[Case], ToolRegistry] | None = None
        if tools_module:
            mod_name, _, fn_name = tools_module.partition(":")
            mod = importlib.import_module(mod_name)
            self._builder = getattr(mod, fn_name or "build_registry")
        self.manifest = load_manifest(manifest_path or ROOT / "agent" / "tools.yaml")

    def load_cases(self, path: Path) -> list[Case]:
        return load_cases(path)

    def tools_for(self, case: Case) -> ToolRegistry:
        registry = self._builder(case) if self._builder else ToolRegistry()
        return apply_manifest(registry, self.manifest)

    def reset(self, case: Case) -> None:
        return None
