from simulations.agents.classical_agent import ClassicalAgent
from simulations.environment.low_resource_env import CommunityState

def test_classical_agent_action():
    s = CommunityState()
    agent = ClassicalAgent()
    decision = agent.act(s)
    assert 'alloc_food' in decision and 'repair_infra' in decision
