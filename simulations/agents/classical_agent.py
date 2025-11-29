"""A simple classical decision-making agent for the simulation."""
import random

class ClassicalAgent:
    def __init__(self, policy=None):
        # policy: callable(state) -> decision dict
        self.policy = policy or self.random_policy

    def random_policy(self, state):
        # make naive choices
        return {
            "alloc_food": max(0, int(state.food_units * 0.01)),
            "repair_infra": 0.01,
            "fairness": random.random()
        }

    def act(self, state):
        return self.policy(state)
