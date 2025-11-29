"""QuantumAgent stub: demonstrates how a quantum-enhanced decision
component *could* be integrated. This file intentionally uses a soft
dependency on Qiskit; if Qiskit is unavailable the agent falls back to
a stochastic classical policy.
"""
try:
    from qiskit import QuantumCircuit, Aer, execute
    _qiskit_available = True
except Exception:
    _qiskit_available = False

import random

class QuantumAgent:
    def __init__(self, shots=1024):
        self.shots = shots

    def _quantum_choice(self):
        if not _qiskit_available:
            # fallback: random choice simulating a quantum outcome distribution
            return random.random()
        # Simple quantum circuit producing a biased measurement
        qc = QuantumCircuit(1,1)
        qc.h(0)
        qc.measure(0,0)
        backend = Aer.get_backend('aer_simulator')
        job = execute(qc, backend=backend, shots=min(1024, self.shots))
        result = job.result().get_counts()
        # produce a pseudo-probability between 0 and 1
        zeros = result.get('0', 0)
        return zeros / sum(result.values())

    def act(self, state):
        prob = self._quantum_choice()
        # map prob to a decision
        return {
            "alloc_food": max(0, int(state.food_units * prob * 0.02)),
            "repair_infra": prob * 0.05,
            "fairness": prob
        }
