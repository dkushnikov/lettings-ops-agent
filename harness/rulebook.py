"""Rulebook: the mandate as data.

Loads `agent/rulebook.yaml` and answers one question for the gate: given a
write tool's authority, its input and the current urgency, is the action
allowed on the agent's own authority, does it need someone's approval, or is it
prohibited? Every answer cites rule ids.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .schema import GateDecision, GateVerdict


@dataclass
class Rulebook:
    raw: dict[str, Any]
    path: Path | None = None

    # ---- loading -------------------------------------------------------- #

    @classmethod
    def load(cls, path: str | Path) -> "Rulebook":
        p = Path(path)
        with p.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        return cls(raw=data, path=p)

    # ---- accessors ------------------------------------------------------ #

    @property
    def role(self) -> str:
        return str(self.raw.get("role", "")).strip()

    @property
    def capabilities(self) -> list[dict[str, Any]]:
        return list(self.raw.get("capabilities", []))

    @property
    def approvals(self) -> list[dict[str, Any]]:
        return list(self.raw.get("approvals", []))

    @property
    def prohibited(self) -> list[dict[str, Any]]:
        return list(self.raw.get("prohibited", []))

    @property
    def escalation_triggers(self) -> list[dict[str, Any]]:
        return list(self.raw.get("escalation_triggers", []))

    @property
    def emergency(self) -> dict[str, Any]:
        return dict(self.raw.get("emergency", {}))

    @property
    def source_hierarchy(self) -> list[str]:
        return list(self.raw.get("source_hierarchy", []))

    @property
    def clocks(self) -> list[dict[str, Any]]:
        return list(self.raw.get("clocks", []))

    @property
    def sources(self) -> dict[str, dict[str, Any]]:
        return {s["id"]: s for s in self.raw.get("sources", [])}

    @property
    def context_keys(self) -> list[str]:
        """Keys harvested from authoritative read results and fed to the gate."""
        return [str(k) for k in self.raw.get("context_keys", [])]

    def rule(self, rule_id: str) -> dict[str, Any] | None:
        for section in ("capabilities", "approvals", "prohibited", "escalation_triggers", "clocks"):
            for r in self.raw.get(section, []):
                if r.get("id") == rule_id:
                    return r
        return None

    # ---- gate logic ----------------------------------------------------- #

    def evaluate(
        self,
        authority: str | None,
        tool_input: dict[str, Any],
        *,
        amount_gbp: float | None,
        urgency: str,
        context: dict[str, Any] | None = None,
    ) -> GateDecision:
        """Decide whether a write with this authority may proceed.

        Order: prohibited → capability with override → approval required →
        capability → no mandate (needs_approval from a human). `context` carries
        facts harvested from authoritative reads (the landlord's own spend cap,
        an always-ask instruction) so the mandate can be per landlord.
        """
        context = context or {}
        if amount_gbp is not None and (not math.isfinite(amount_gbp) or amount_gbp < 0):
            return GateDecision(verdict=GateVerdict.deny, reason="Invalid amount: a finite, non-negative number of pounds is required.")
        if authority is None:
            # A write tool without a declared authority is outside the mandate.
            return GateDecision(
                verdict=GateVerdict.needs_approval,
                reason="Write tool carries no authority name; no capability can match it.",
                required_approval_from="property_manager",
            )

        # 1. Prohibited always wins.
        for pro in self.prohibited:
            if pro.get("authority") == authority:
                verdict = GateVerdict.escalate if pro.get("on_request") == "escalate" else GateVerdict.deny
                return GateDecision(
                    verdict=verdict,
                    rule_ids=[pro["id"]],
                    reason=pro.get("reason") or pro.get("description", "Prohibited action"),
                )

        matching = [c for c in self.capabilities if c.get("authority") == authority]
        if not matching:
            return GateDecision(
                verdict=GateVerdict.needs_approval,
                reason=f"No capability grants '{authority}'.",
                required_approval_from="property_manager",
            )

        # 2. A capability whose conditions hold and which overrides approvals
        #    (the emergency override) is checked first.
        for cap in matching:
            if cap.get("overrides") and self._conditions_hold(cap.get("conditions", {}), tool_input, amount_gbp, urgency, context):
                return GateDecision(verdict=GateVerdict.allow, rule_ids=[cap["id"]], reason=cap.get("note", "Override capability"))

        # 3. Approval rules.
        for apr in self.approvals:
            if apr.get("authority") != authority:
                continue
            if self._approval_triggers(apr.get("when", {}), amount_gbp, urgency, context):
                return GateDecision(
                    verdict=GateVerdict.needs_approval,
                    rule_ids=[apr["id"]],
                    reason=apr.get("note", "Approval required"),
                    required_approval_from=apr.get("from", "property_manager"),
                )

        # 4. Ordinary capabilities.
        for cap in matching:
            if cap.get("overrides"):
                continue
            if self._conditions_hold(cap.get("conditions", {}), tool_input, amount_gbp, urgency, context):
                return GateDecision(verdict=GateVerdict.allow, rule_ids=[cap["id"]], reason=cap.get("note", "Within mandate"))

        # 5. Capability exists but its conditions do not hold.
        ids = [c["id"] for c in matching]
        return GateDecision(
            verdict=GateVerdict.needs_approval,
            rule_ids=ids,
            reason="Conditions of the matching capability are not met (amount, urgency or consent).",
            required_approval_from="property_manager",
        )

    # ---- helpers -------------------------------------------------------- #

    @staticmethod
    def _limit(value: Any, rule: dict[str, Any], context: dict[str, Any]) -> float:
        """A numeric limit, or the landlord's own cap from context when the rule says `landlord_cap`."""
        if isinstance(value, str) and value == "landlord_cap":
            cap = context.get("spend_cap_gbp")
            if cap is None:
                cap = rule.get("default_cap_gbp", 0)  # a prior is not a mandate: no limit on file, no standing spend
            return float(cap)
        return float(value)

    @classmethod
    def _conditions_hold(cls, cond: dict[str, Any], tool_input: dict[str, Any], amount: float | None, urgency: str, context: dict[str, Any]) -> bool:
        if "urgency_in" in cond and urgency not in cond["urgency_in"]:
            return False
        if "max_amount_gbp" in cond:
            if amount is None:
                # Unknown amount: be conservative, treat as exceeding.
                return False
            limit = cls._limit(cond["max_amount_gbp"], cond, context)
            if limit <= 0 or amount > limit:
                return False
        if "requires_consent_field" in cond:
            if not str(tool_input.get(cond["requires_consent_field"]) or "").strip():
                return False
        for k, v in (cond.get("context_not") or {}).items():
            if context.get(k) == v:
                return False
        for k, v in (cond.get("context") or {}).items():
            if context.get(k) != v:
                return False
        return True

    @classmethod
    def _approval_triggers(cls, when: dict[str, Any], amount: float | None, urgency: str, context: dict[str, Any]) -> bool:
        if "urgency_not" in when and urgency == when["urgency_not"]:
            return False
        if "urgency_in" in when and urgency not in when["urgency_in"]:
            return False
        for k, v in (when.get("context") or {}).items():
            if context.get(k) != v:
                return False
        if "amount_gbp_over" in when:
            if amount is None:
                return True  # unknown spend above a cap rule: ask
            limit = cls._limit(when["amount_gbp_over"], when, context)
            if limit <= 0:
                return True  # no limit on file: any spend, even £0, is the landlord's decision
            return amount > limit
        return True

    # ---- prompt rendering ----------------------------------------------- #

    def render_for_prompt(self) -> str:
        """Compact, stable text of the mandate for the system prompt."""
        lines: list[str] = []
        lines.append("MANDATE (rule ids are citable; cite them in authority_citations)")
        lines.append("Capabilities (you may do these yourself):")
        for c in self.capabilities:
            cond = c.get("conditions") or {}
            cond_txt = f" when {cond}" if cond else ""
            ov = " [overrides spend cap]" if c.get("overrides") else ""
            lines.append(f"- {c['id']}: {c.get('authority')}{cond_txt}{ov}. {c.get('note', '')}".rstrip())
        lines.append("Approvals (ask first):")
        for a in self.approvals:
            lines.append(f"- {a['id']}: {a.get('authority')} when {a.get('when')} → approval from {a.get('from')}. {a.get('note', '')}".rstrip())
        lines.append("Prohibited (never on your own authority):")
        for p in self.prohibited:
            txt = p.get("reason") or p.get("description", "")
            lines.append(f"- {p['id']}: {txt}")
        lines.append("Escalation triggers:")
        for e in self.escalation_triggers:
            first = f" First: {e['first']}" if e.get("first") else ""
            lines.append(f"- {e['id']}: {e.get('description', '')}{first}")
        routing = self.raw.get("decision_routing") or []
        if routing:
            lines.append("Decision routing (who owns the decision decides how the case ends):")
            for r in routing:
                lines.append(f"- {r['id']} [{r.get('owner')}]: {r.get('decisions', '')} → {r.get('how', '')}")
        em = self.emergency
        if em:
            lines.append("Emergency definitions: " + "; ".join(em.get("definitions", [])))
            lines.append(f"Cold months: {em.get('cold_months', [])}")
            for k, v in (em.get("first_actions") or {}).items():
                lines.append(f"- first action [{k}]: {v}")
        lines.append("Source hierarchy (earlier wins on conflict): " + " > ".join(self.source_hierarchy))
        lines.append("Clocks (status tells you how firm the deadline is):")
        for ck in self.clocks:
            lines.append(f"- {ck['id']} [{ck.get('status')}]: {ck.get('name')} — {ck.get('basis', '')}")
        for d in self.raw.get("data_handling", []) or []:
            lines.append(f"Data handling: {d}")
        sp = self.raw.get("safety_pass") or {}
        if sp:
            lines.append("SAFETY PASS (the reviewer blocks `resolved` when a document or message carries one of these and the record does not address it): " + ", ".join(str(k) for k in sp.get("keywords", [])))
            for n in sp.get("notes", []) or []:
                lines.append(f"- {n}")
        wf = self.raw.get("workflow") or {}
        if wf:
            stages = []
            for st in wf.get("stages", []) or []:
                if isinstance(st, dict):
                    stages.append(f"{st.get('id')} ({st.get('text', '')})" if st.get("text") else str(st.get("id")))
                else:
                    stages.append(str(st))
            lines.append("WORKFLOW STAGES (name the one the ticket is at in `stage`, in this order): " + " → ".join(stages))
            if wf.get("side_states"):
                lines.append("Side states: " + ", ".join(str(x) for x in wf["side_states"]))
            if wf.get("hold_reasons"):
                lines.append("Hold reasons (use in hold_reason, with a comment): " + ", ".join(str(x) for x in wf["hold_reasons"]))
            for t in wf.get("manual_triggers", []) or []:
                lines.append(f"Manual-mode trigger — where the agency's automation stops and a person decides; here you decide: {t}")
            if wf.get("priority_rule"):
                lines.append(f"Priority rule: {wf['priority_rule']}")
        return "\n".join(lines)
