"""Tool registry and the environment adapter contract.

The environment (mock world today, the organisers' tools on the day) supplies
*bound tools*: a ToolSpec the gate can reason about plus a callable. The loop
adds its own terminal tools; the adapter never sees them.
"""

from __future__ import annotations

import inspect
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Awaitable, Callable, Protocol

from .schema import Case, ToolClass, ToolSpec


class ToolError(Exception):
    """Base class for tool failures the executor understands."""


class TransientToolError(ToolError):
    """Timeouts, 5xx, flaky transport: safe to retry for reads."""


class LostResponseError(ToolError):
    """The call may have succeeded but the response was lost.

    For a write this is the dangerous case: retrying can duplicate the effect.
    """


class ToolRejected(ToolError):
    """Deterministic rejection (validation, not found, not permitted by the env)."""


ToolFn = Callable[..., Awaitable[Any] | Any]
ReconcileFn = Callable[[dict[str, Any]], Awaitable[Any] | Any]


@dataclass
class BoundTool:
    spec: ToolSpec
    fn: ToolFn
    # Given the original input, returns the existing effect (e.g. a work order
    # already created) or None. Used after a lost response on a write.
    reconcile: ReconcileFn | None = None

    async def call(self, **kwargs: Any) -> Any:
        result = self.fn(**kwargs)
        if inspect.isawaitable(result):
            result = await result
        return result

    async def reconcile_call(self, original_input: dict[str, Any]) -> Any:
        if self.reconcile is None:
            return None
        result = self.reconcile(original_input)
        if inspect.isawaitable(result):
            result = await result
        return result


@dataclass
class ToolRegistry:
    tools: dict[str, BoundTool] = field(default_factory=dict)

    def add(self, tool: BoundTool) -> None:
        self.tools[tool.spec.name] = tool

    def get(self, name: str) -> BoundTool | None:
        return self.tools.get(name)

    def specs(self) -> list[ToolSpec]:
        return [t.spec for t in self.tools.values()]

    def names(self) -> list[str]:
        return list(self.tools.keys())

    def api_definitions(self) -> list[dict[str, Any]]:
        """Tool definitions in the Anthropic Messages API shape.

        The description is annotated with the gate-relevant facts so the model
        knows the cost of each tool before calling it.
        """
        defs = []
        for spec in self.specs():
            tags = [spec.tool_class.value]
            if spec.authority:
                tags.append(f"authority: {spec.authority}")
            if spec.side_effect:
                tags.append(f"effect: {spec.side_effect}")
            if not spec.reversible:
                tags.append("irreversible")
            desc = f"{spec.description} [{'; '.join(tags)}]"
            defs.append({
                "name": spec.name,
                "description": desc,
                "input_schema": spec.input_schema,
            })
        return defs


class EnvironmentAdapter(Protocol):
    """What the harness needs from an environment.

    Implementations: ``mockworld.adapter.MockAdapter`` today; a thin adapter to
    the organisers' data and tools on the day.
    """

    name: str

    def load_cases(self, path: Path) -> list[Case]: ...

    def tools_for(self, case: Case) -> ToolRegistry: ...

    def reset(self, case: Case) -> None: ...


def make_spec(
    name: str,
    description: str,
    input_schema: dict[str, Any],
    *,
    tool_class: ToolClass = ToolClass.read,
    authority: str | None = None,
    amount_field: str | None = None,
    idempotent: bool = False,
    reversible: bool = True,
    side_effect: str = "",
    reconcile_with: str | None = None,
) -> ToolSpec:
    """Small helper so adapters can declare specs without repeating field names."""
    return ToolSpec(
        name=name,
        description=description,
        input_schema=input_schema,
        tool_class=tool_class,
        authority=authority,
        amount_field=amount_field,
        idempotent=idempotent,
        reversible=reversible,
        side_effect=side_effect,
        reconcile_with=reconcile_with,
    )
