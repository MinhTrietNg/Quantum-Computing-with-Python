"""
Parameter-shift rule: a minimal visual demo.

Circuit:   |0> ── RY(θ) ── measure Z
Loss:      L(θ) = <Z> = cos(θ)
Exact:     dL/dθ = -sin(θ)            (used only as ground truth)

The parameter-shift rule runs the SAME circuit at two shifted angles and
combines the two expectation values:

    dL/dθ = 1/2 * [ L(θ + π/2) - L(θ - π/2) ]

Run:
    python parameter_shift_demo.py               # θ0 = π/3
    python parameter_shift_demo.py --theta 0.5   # any other angle
    python parameter_shift_demo.py --no-show     # save figures only

References:
    K. Mitarai et al., "Quantum circuit learning", Phys. Rev. A 98, 032309 (2018).
    M. Schuld et al., "Evaluating analytic gradients on quantum hardware",
    Phys. Rev. A 99, 032331 (2019).
"""

import argparse
import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from gradients import parameter_shift_gradient
from plotting import plot_gradient_distributions, plot_loss_and_gradient
from report import (
    report_circuit,
    report_exact_gradient,
    report_key_idea,
    report_shifted_circuits,
    run_shot_experiment,
)
from style import save_figure


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parameter-Shift Rule demo")
    parser.add_argument(
        "--theta", type=float, default=np.pi / 3,
        help="angle θ0 in radians (default: π/3)",
    )  # fmt: skip
    parser.add_argument(
        "--no-show", action="store_true",
        help="save figures without opening windows",
    )  # fmt: skip
    return parser.parse_args()


def main() -> None:
    # Windows terminals can default to a legacy code page; θ, π and the
    # circuit-drawing characters need UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args()
    theta = args.theta
    shift = parameter_shift_gradient(theta)

    report_circuit(theta)
    report_exact_gradient(theta, shift)
    report_shifted_circuits(theta, shift)
    save_figure(plot_loss_and_gradient(theta), "parameter_shift_tangent.png")

    estimates_by_shots = run_shot_experiment(theta)
    save_figure(
        plot_gradient_distributions(theta, estimates_by_shots),
        "shot_gradient_distributions.png",
    )

    report_key_idea(theta, shift.gradient)

    if not args.no_show and matplotlib.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    main()
