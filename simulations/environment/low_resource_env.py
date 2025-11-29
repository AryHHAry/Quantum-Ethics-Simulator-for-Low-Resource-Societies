"""Simple low-resource environment model.

This module provides a minimalist simulation of a small community with
resource nodes, population agents, and simple consequences for decisions.
The goal is to be a didactic starting point for ethics simulations.
"""
from dataclasses import dataclass, field
import random

@dataclass
class CommunityState:
    population: int = 100
    food_units: float = 1000.0
    water_units: float = 1000.0
    infrastructure_score: float = 1.0  # 0..1, 1 = fully functioning
    trust_score: float = 0.5  # 0..1, social trust

def apply_decision(state: CommunityState, decision: dict):
    """Apply an agent decision to the environment and return new state + metrics."""
    # decision is a dict like {"alloc_food": 10, "repair_infra": 0.1}
    s = CommunityState(**vars(state))
    alloc = decision.get("alloc_food", 0.0)
    repair = decision.get("repair_infra", 0.0)
    # simple rules
    s.food_units = max(0.0, s.food_units - alloc)
    s.infrastructure_score = max(0.0, min(1.0, s.infrastructure_score + repair))
    # trust changes with perceived fairness
    fairness = decision.get("fairness", 0.5)
    s.trust_score = max(0.0, min(1.0, s.trust_score + (fairness - 0.5) * 0.1))
    # consequences on population (very simplified)
    if s.food_units < s.population * 2:
        s.population = max(0, int(s.population * 0.99))  # small decline
    return s
