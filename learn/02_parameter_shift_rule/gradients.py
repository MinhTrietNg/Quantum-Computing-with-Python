"""Parameter-shift gradient: exact, shot-based, and its theoretical spread."""

from typing import NamedTuple

import numpy as np
import pennylane as qml

from circuit import circuit, quantum_expectation
from config import SHIFT


class ShiftResult(NamedTuple):
    """The two shifted expectation values and the gradient built from them."""

    loss_plus: float
    loss_minus: float
    gradient: float


def parameter_shift_gradient(theta: float) -> ShiftResult:
    """
    Compute dL/dθ with the two-term parameter-shift rule (no autodiff).

    Parameters
    ----------
    theta : float
        Point θ at which the gradient is evaluated.

    Returns
    -------
    ShiftResult
        L(θ + π/2), L(θ - π/2) and the gradient 1/2 * (L+ - L-).
    """
    # Run the same circuit twice; only the rotation angle changes.
    loss_plus = quantum_expectation(theta + SHIFT)
    loss_minus = quantum_expectation(theta - SHIFT)

    # RY's generator Y/2 has eigenvalues ±1/2, so L(θ) is a pure sinusoid:
    # L(θ) = A cos θ + B sin θ + C. For any such function this combination
    # equals L'(θ) exactly. It is not a finite-difference approximation.
    gradient = 0.5 * (loss_plus - loss_minus)
    return ShiftResult(loss_plus, loss_minus, gradient)


def shot_based_parameter_shift(
    theta: float, shots: int, repetitions: int
) -> np.ndarray:
    """
    Repeat the parameter-shift estimate with a finite number of shots.

    Parameters
    ----------
    theta : float
        Point θ at which the gradient is evaluated.
    shots : int
        Measurements per circuit evaluation.
    repetitions : int
        Number of independent gradient estimates.

    Returns
    -------
    np.ndarray
        Array of shape ``(repetitions,)`` with one gradient estimate each.
    """
    # Real hardware cannot return <Z> exactly. Each shot measures the qubit
    # once and gives +1 or -1; <Z> is estimated by averaging `shots` of them.
    # This is the same circuit as above, now sampled instead of computed.
    sampled_circuit = qml.set_shots(circuit, shots=shots)

    estimates = np.empty(repetitions)
    for i in range(repetitions):
        loss_plus = float(sampled_circuit(theta + SHIFT))
        loss_minus = float(sampled_circuit(theta - SHIFT))
        estimates[i] = 0.5 * (loss_plus - loss_minus)
    return estimates


def theoretical_std(theta: float, shots: int) -> float:
    """
    Return the standard deviation of the shot-based parameter-shift gradient.

    Each shot is ±1, so one shot estimates <Z> with variance 1 - <Z>².
    Averaging N shots divides that by N. The two circuits are independent
    and the factor 1/2 squares to 1/4, so

        Var[g] = [ (1 - L+²) + (1 - L-²) ] / (4N)
    """
    loss_plus, loss_minus, _ = parameter_shift_gradient(theta)
    variance = ((1 - loss_plus**2) + (1 - loss_minus**2)) / (4 * shots)
    return np.sqrt(variance)
