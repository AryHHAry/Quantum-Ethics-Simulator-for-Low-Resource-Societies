from simulations.environment.low_resource_env import CommunityState, apply_decision

def test_apply_decision_reduces_food():
    s = CommunityState(food_units=100.0, population=10)
    s2 = apply_decision(s, {"alloc_food": 5})
    assert s2.food_units <= s.food_units
