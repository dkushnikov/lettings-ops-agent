"""Claude client, settings and a client-side throttle.

Everything substrate-specific lives here: model id, effort, thinking mode,
cache breakpoints, retry/timeout, and the token bucket that keeps a batch of
concurrent cases under the key's tokens-per-minute budget.
"""

from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass, field
from typing import Any

import anthropic

TERMINAL_MAX_TOKENS = 8000


@dataclass
class Settings:
    model: str = "claude-opus-5"
    effort: str = "high"
    reviewer: str = "rules"  # rules | llm
    concurrency: int = 4
    case_timeout_s: float = 540.0
    max_steps: int = 12
    retry_budget: int = 1
    tpm_budget: int = 200_000
    max_tokens: int = 8000
    request_timeout_s: float = 120.0
    max_retries: int = 3
    rulebook_path: str = "agent/rulebook.yaml"
    playbooks_dir: str = "agent/playbooks"
    extra: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_env(cls, **overrides: Any) -> "Settings":
        def env(name: str, default: Any, cast=str):
            raw = os.environ.get(name)
            if raw is None or raw == "":
                return default
            try:
                return cast(raw)
            except (TypeError, ValueError):
                return default

        s = cls(
            model=env("LOA_MODEL", "claude-opus-5"),
            effort=env("LOA_EFFORT", "high"),
            reviewer=env("LOA_REVIEWER", "rules"),
            concurrency=env("LOA_CONCURRENCY", 4, int),
            case_timeout_s=env("LOA_CASE_TIMEOUT_S", 540.0, float),
            max_steps=env("LOA_MAX_STEPS", 12, int),
            retry_budget=env("LOA_RETRY_BUDGET", 1, int),
            tpm_budget=env("LOA_TPM_BUDGET", 200_000, int),
            rulebook_path=env("LOA_RULEBOOK", "agent/rulebook.yaml"),
            playbooks_dir=env("LOA_PLAYBOOKS", "agent/playbooks"),
        )
        for k, v in overrides.items():
            if v is not None and hasattr(s, k):
                setattr(s, k, v)
        return s


def load_dotenv(path: str = ".env") -> None:
    """Tiny .env loader: KEY=VALUE lines, no expansion, never overrides the environment."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and k not in os.environ and v:
                    os.environ[k] = v
    except FileNotFoundError:
        return


def make_client(settings: Settings) -> anthropic.AsyncAnthropic:
    return anthropic.AsyncAnthropic(timeout=settings.request_timeout_s, max_retries=settings.max_retries)


def estimate_tokens(text: str) -> int:
    return len(text) // 4 + 1


class TokenBucket:
    """Approximate tokens-per-minute limiter shared by all concurrent cases."""

    def __init__(self, tokens_per_minute: int):
        self.capacity = max(1, tokens_per_minute)
        self.tokens = float(self.capacity)
        self.rate = self.capacity / 60.0
        self.updated = time.monotonic()
        self._lock = asyncio.Lock()

    def _refill(self) -> None:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
        self.updated = now

    async def acquire(self, n: int) -> None:
        n = min(n, self.capacity)
        while True:
            async with self._lock:
                self._refill()
                if self.tokens >= n:
                    self.tokens -= n
                    return
                wait = (n - self.tokens) / self.rate
            await asyncio.sleep(min(max(wait, 0.05), 5.0))


def thinking_params(model: str) -> dict[str, Any]:
    """Adaptive thinking on current models; older models get no thinking block."""
    if "haiku" in model or "sonnet-4-5" in model or "opus-4-5" in model:
        return {}
    return {"thinking": {"type": "adaptive"}}


async def create_message(
    client: anthropic.AsyncAnthropic,
    settings: Settings,
    *,
    system: list[dict[str, Any]],
    messages: list[Any],
    tools: list[dict[str, Any]] | None,
    bucket: TokenBucket | None = None,
    max_tokens: int | None = None,
    output_config: dict[str, Any] | None = None,
) -> Any:
    """One Messages API call with the harness's standard parameters."""
    if bucket is not None:
        approx = sum(estimate_tokens(b.get("text", "")) for b in system)
        approx += sum(estimate_tokens(str(m)) for m in messages)
        approx += sum(estimate_tokens(str(t)) for t in (tools or []))
        await bucket.acquire(approx)
    params: dict[str, Any] = {
        "model": settings.model,
        "max_tokens": max_tokens or settings.max_tokens,
        "system": system,
        "messages": messages,
        **thinking_params(settings.model),
    }
    cfg: dict[str, Any] = {"effort": settings.effort}
    if output_config:
        cfg.update(output_config)
    if "haiku" not in settings.model:
        params["output_config"] = cfg
    if tools:
        params["tools"] = tools
    return await client.messages.create(**params)


def usage_of(response: Any) -> dict[str, int]:
    u = getattr(response, "usage", None)
    if u is None:
        return {"input": 0, "output": 0, "cache_read": 0}
    return {
        "input": int(getattr(u, "input_tokens", 0) or 0),
        "output": int(getattr(u, "output_tokens", 0) or 0),
        "cache_read": int(getattr(u, "cache_read_input_tokens", 0) or 0),
    }


def is_transient_error(e: BaseException) -> bool:
    if isinstance(e, (anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.APITimeoutError)):
        return True
    if isinstance(e, anthropic.APIStatusError):
        return e.status_code >= 500 or getattr(e, "type", "") in {"overloaded_error", "rate_limit_error"}
    return isinstance(e, (asyncio.TimeoutError, TimeoutError))
