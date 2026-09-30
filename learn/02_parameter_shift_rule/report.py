"""Console output: one function per section of the demo."""

import numpy as np
import pennylane as qml

from circuit import circuit, exact_gradient, quantum_expectation
from config import LEARNING_RATE, REPETITIONS, SHIFT, SHOT_COUNTS
from gradients import (
    ShiftResult,
    parameter_shift_gradient,
    shot_based_parameter_shift,
    theoretical_std,
)

KEY_IDEA = """\
Parameter-Shift Rule does NOT choose between θ + π/2 and θ - π/2.
Those two shifted points are measurements used to estimate the
derivative at the ORIGINAL point θ.

The optimizer then uses that gradient to update the circuit parameter:

    θ_new = θ - η * gradient

Parameter Shift:
    two shifted circuit evaluations
            ↓
    expectation values
            ↓
    difference
            ↓
    gradient at θ
            ↓
    optimizer
            ↓
    new θ"""


def header(title: str) -> None:
    """Print a section header."""
    print()
    print("=" * 64)
    print(title)
    print("=" * 64)


def report_circuit(theta: float) -> None:
    """Section 1: draw the circuit template and its instance at θ0."""
    header("1. Quantum circuit")
    print("Template:   0: ──RY(θ)──┤ <Z>")
    print(f"At θ0:      {qml.draw(circuit, decimals=3)(theta)}")


def report_exact_gradient(theta: float, shift: ShiftResult) -> None:
    """Section 2: compare the parameter-shift gradient with -sin(θ)."""
    header("2. Parameter-shift gradient (exact simulator)")
    loss_0 = quantum_expectation(theta)
    gradient_exact = exact_gradient(theta)
    error = abs(shift.gradient - gradient_exact)

    print(f"theta = {theta:.6f}")
    print(f"L(theta) = {loss_0:.6f}")
    print()
    print(f"L(theta + pi/2) = {shift.loss_plus:.6f}")
    print(f"L(theta - pi/2) = {shift.loss_minus:.6f}")
    print()
    print(
        f"Parameter Shift Gradient = 0.5 * ({shift.loss_plus:.6f} - "
        f"({shift.loss_minus:.6f})) = {shift.gradient:.6f}"
    )
    print(
        f"Exact Gradient           = -sin(theta)"
        f"                        = {gradient_exact:.6f}"
    )
    print(f"Absolute Error           = {error:.2e}")

    # The rule is exact everywhere, not only at θ0.
    test_angles = np.linspace(-np.pi, np.pi, 13)
    worst = max(
        abs(parameter_shift_gradient(t).gradient - exact_gradient(t))
        for t in test_angles
    )
    print(f"\nChecked {len(test_angles)} angles in [-π, π]: max |error| = {worst:.2e}")


def report_shifted_circuits(theta: float, shift: ShiftResult) -> None:
    """Section 3: show that both evaluations use the same circuit."""
    header("3. Parameter shift evaluates the SAME circuit twice")
    draw = qml.draw(circuit, decimals=3)
    print("Circuit A:  0: ──RY(θ + π/2)──┤ <Z>")
    print(f"            {draw(theta + SHIFT)}    ->  L_plus  = {shift.loss_plus:+.6f}")
    print()
    print("Circuit B:  0: ──RY(θ - π/2)──┤ <Z>")
    print(f"            {draw(theta - SHIFT)}    ->  L_minus = {shift.loss_minus:+.6f}")
    print()
    print(f"Combine:    gradient = 0.5 * (L_plus - L_minus) = {shift.gradient:+.6f}")


def run_shot_experiment(theta: float) -> dict[int, np.ndarray]:
    """Section 4: estimate the gradient with finite shots and tabulate it."""
    header(f"4. Shot-based parameter shift ({REPETITIONS} repetitions per shot count)")
    print(f"exact gradient = {exact_gradient(theta):.6f}\n")
    print(
        f"{'shots':>7} | {'mean gradient':>13} | {'variance':>10} | "
        f"{'std':>8} | {'theory std':>10}"
    )
    print("-" * 61)

    estimates_by_shots = {}
    for shots in SHOT_COUNTS:
        estimates = shot_based_parameter_shift(theta, shots, REPETITIONS)
        estimates_by_shots[shots] = estimates
        print(
            f"{shots:>7,} | {estimates.mean():>13.6f} | "
            f"{estimates.var(ddof=1):>10.2e} | {estimates.std(ddof=1):>8.5f} | "
            f"{theoretical_std(theta, shots):>10.5f}"
        )
    print("\n10x more shots -> variance about 10x smaller -> std about 3.16x smaller.")
    return estimates_by_shots


def report_key_idea(theta: float, gradient: float) -> None:
    """Section 5: explain how the gradient feeds one optimizer step."""
    header("5. Key idea")
    print(KEY_IDEA)
    theta_new = theta - LEARNING_RATE * gradient
    print(
        f"\nExample with η = {LEARNING_RATE}:  "
        f"θ_new = {theta:.4f} - {LEARNING_RATE} * ({gradient:.4f}) = {theta_new:.4f}"
    )
