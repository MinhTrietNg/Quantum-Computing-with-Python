"""The one-qubit circuit |0> ── RY(θ) ── measure Z and its exact loss."""

import numpy as np
import pennylane as qml

from config import SEED

# Without shots, default.qubit returns exact expectation values from the state
# vector. The seed only matters when gradients.py switches to finite shots.
device = qml.device("default.qubit", wires=1, seed=SEED)


@qml.qnode(device)
def circuit(theta: float):
    # The qubit starts in |0>. RY(θ) = exp(-iθY/2) rotates it around the Y
    # axis of the Bloch sphere:  |0>  ->  cos(θ/2)|0> + sin(θ/2)|1>
    qml.RY(theta, wires=0)
    # <Z> = P(0) - P(1) = cos²(θ/2) - sin²(θ/2) = cos(θ)
    return qml.expval(qml.PauliZ(0))


def quantum_expectation(theta: float) -> float:
    """Return L(θ) = <Z> after RY(θ), computed exactly by the simulator."""
    return float(circuit(theta))


def exact_gradient(theta: float) -> float:
    """Return the analytical derivative of L(θ) = cos(θ). Ground truth only."""
    return -np.sin(theta)
