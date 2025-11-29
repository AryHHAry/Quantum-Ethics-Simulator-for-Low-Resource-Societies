"""Run a simple simulation with one agent and a small community."""
from simulations.environment.low_resource_env import CommunityState, apply_decision
from simulations.agents.classical_agent import ClassicalAgent
import json

def run(steps=10):
    state = CommunityState()
    agent = ClassicalAgent()
    history = []
    for t in range(steps):
        decision = agent.act(state)
        state = apply_decision(state, decision)
        history.append({"t": t, "state": vars(state), "decision": decision})
    return history

if __name__ == '__main__':
    hist = run(steps=20)
    print(json.dumps(hist, indent=2))
