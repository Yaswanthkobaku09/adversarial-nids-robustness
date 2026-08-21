"""Explicit, disclosed threat model definitions.

Every attack run must declare: adversary knowledge (black-box/grey-box/white-box),
query budget, and perturbation constraints — this is the reproducibility
requirement the field-level survey flags as commonly missing.
"""

from dataclasses import dataclass


@dataclass
class ThreatModel:
    knowledge: str  # "black-box" | "grey-box" | "white-box"
    query_budget: int
    max_perturbation_norm: float
