"""
Parameter-Shift Rule: a minimal visual demo
===========================================

Circuit:   |0> ── RY(θ) ── measure Z
Loss:      L(θ) = <Z> = cos(θ)
Exact:     dL/dθ = -sin(θ)            (used only as ground truth)

The Parameter-Shift Rule runs the SAME circuit at two shifted angles and
combines the two expectation values:

    dL/dθ = 1/2 * [ L(θ + π/2) - L(θ - π/2) ]

Run:
    python parameter_shift_demo.py               # θ0 = π/3
    python parameter_shift_demo.py --theta 0.5   # any other angle
"""

import argparse
import sys
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pennylane as qml

SHIFT = np.pi / 2
SHOT_COUNTS = [100, 1000, 10000]
REPETITIONS = 500
FIGURE_DIR = Path(__file__).parent / "figures"

# Chart colours. Curve / θ+π/2 / θ-π/2 were checked for colour-blind separation;
# every point also gets its own marker shape and a text label.
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
SURFACE = "#fcfcfb"
CURVE_COLOR = "#2a78d6"
PLUS_COLOR = "#eb6834"
MINUS_COLOR = "#1baf7a"
SHOT_COLORS = ["#86b6ef", "#2a78d6", "#104281"]  # light -> dark = few -> many shots


# ─────────────────────────────────────────────────────────────────────────────
# 1. Quantum circuit
# ─────────────────────────────────────────────────────────────────────────────

# Without shots, default.qubit returns exact expectation values from the state
# vector. The seed only matters later, when section 5 switches to finite shots.
device = qml.device("default.qubit", wires=1, seed=42)


@qml.qnode(device)
def circuit(theta):
    # The qubit starts in |0>. RY(θ) = exp(-iθY/2) rotates it around the Y axis
    # of the Bloch sphere:  |0>  ->  cos(θ/2)|0> + sin(θ/2)|1>
    qml.RY(theta, wires=0)
    # <Z> = P(0) - P(1) = cos²(θ/2) - sin²(θ/2) = cos(θ)
    return qml.expval(qml.PauliZ(0))


def quantum_expectation(theta):
    """L(θ) = <Z> after RY(θ), computed exactly by the simulator."""
    return float(circuit(theta))


def exact_gradient(theta):
    """Analytical derivative of L(θ) = cos(θ). Ground truth only."""
    return -np.sin(theta)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Parameter-shift gradient (manual, no autodiff)
# ─────────────────────────────────────────────────────────────────────────────

def parameter_shift_gradient(theta):
    """Return L(θ+π/2), L(θ-π/2) and the parameter-shift gradient at θ."""
    # Run the same circuit twice; only the rotation angle changes.
    L_plus = quantum_expectation(theta + SHIFT)
    L_minus = quantum_expectation(theta - SHIFT)

    # RY's generator Y/2 has eigenvalues ±1/2, so L(θ) is a pure sinusoid:
    # L(θ) = A cos θ + B sin θ + C. For any such function this combination
    # equals L'(θ) exactly. It is not a finite-difference approximation.
    gradient = 0.5 * (L_plus - L_minus)
    return L_plus, L_minus, gradient


# ─────────────────────────────────────────────────────────────────────────────
# 3. Visualization: L(θ), the two shifted evaluations, and the tangent
# ─────────────────────────────────────────────────────────────────────────────

def style_axes(ax):
    ax.set_facecolor(SURFACE)
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=INK_SECONDARY)


def plot_loss_and_gradient(theta):
    L_0 = quantum_expectation(theta)
    L_plus, L_minus, gradient = parameter_shift_gradient(theta)

    # One full period of L(θ), centred on θ0, evaluated point by point.
    thetas = np.linspace(theta - np.pi, theta + np.pi, 400)
    losses = [quantum_expectation(t) for t in thetas]

    fig, ax = plt.subplots(figsize=(9, 5.5), facecolor=SURFACE)
    style_axes(ax)
    ax.plot(thetas, losses, color=CURVE_COLOR, linewidth=2, label=r"$L(\theta) = \langle Z \rangle = \cos\theta$")

    # Tangent at θ0 whose slope is the parameter-shift gradient.
    t = np.linspace(theta - 0.9, theta + 0.9, 2)
    ax.plot(t, L_0 + gradient * (t - theta), color=INK, linewidth=2,
            label=rf"tangent at $\theta_0$, slope = $g_{{PS}}$ = {gradient:.3f}")

    # The straight line between the two shifted points is NOT the gradient:
    # its slope is (L+ - L-)/π, while the rule divides by 2.
    secant_slope = (L_plus - L_minus) / (2 * SHIFT)
    ax.plot([theta - SHIFT, theta + SHIFT], [L_minus, L_plus], color=MUTED, linewidth=1.5,
            linestyle="--", label=f"line through shifted points, slope = {secant_slope:.3f} (not the gradient)")

    points = [
        (theta - SHIFT, L_minus, MINUS_COLOR, "^", r"$L(\theta_0-\pi/2)$", (-12, 14), "right"),
        (theta, L_0, INK, "o", r"$L(\theta_0)$", (12, 10), "left"),
        (theta + SHIFT, L_plus, PLUS_COLOR, "s", r"$L(\theta_0+\pi/2)$", (-12, -18), "right"),
    ]
    for x, y, color, marker, name, offset, align in points:
        ax.vlines(x, -1.3, y, color=MUTED, linewidth=1, linestyle=":")
        ax.plot(x, y, marker=marker, markersize=10, color=color, markeredgecolor=SURFACE, markeredgewidth=2, zorder=5)
        ax.annotate(f"{name} = {y:.3f}", (x, y), xytext=offset, textcoords="offset points",
                    ha=align, va="center", color=INK, fontsize=10)

    ax.text(0.98, 0.97,
            r"$g_{PS} = \frac{1}{2}\,[\,L(\theta_0+\pi/2) - L(\theta_0-\pi/2)\,]$" "\n"
            rf"$\quad\;\; = \frac{{1}}{{2}}\,[\,({L_plus:.3f}) - ({L_minus:.3f})\,] = {gradient:.3f}$" "\n"
            rf"exact $-\sin\theta_0$ = {exact_gradient(theta):.3f}",
            transform=ax.transAxes, ha="right", va="top", fontsize=10, color=INK,
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor=AXIS))

    ax.set_xticks([theta - SHIFT, theta, theta + SHIFT])
    ax.set_xticklabels([rf"$\theta_0-\pi/2$" f"\n{theta - SHIFT:.2f}",
                        rf"$\theta_0$" f"\n{theta:.2f}",
                        rf"$\theta_0+\pi/2$" f"\n{theta + SHIFT:.2f}"])
    ax.set_xlim(thetas[0], thetas[-1])
    ax.set_ylim(-1.3, 1.45)
    ax.set_xlabel(r"$\theta$ (radians)", color=INK_SECONDARY)
    ax.set_ylabel(r"$L(\theta)$", color=INK_SECONDARY)
    ax.set_title(r"Parameter-shift rule: two shifted circuits give the slope at $\theta_0$",
                 color=INK, loc="left", fontsize=12)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=1, frameon=False, fontsize=9)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# 4. Shot-based parameter shift
# ─────────────────────────────────────────────────────────────────────────────

def shot_based_parameter_shift(theta, shots, repetitions):
    """Repeat the parameter-shift estimate with a finite number of shots."""
    # Real hardware cannot return <Z> exactly. Each shot measures the qubit
    # once and gives +1 or -1; <Z> is estimated by averaging `shots` of them.
    # This is the same circuit as above, now sampled instead of computed exactly.
    sampled_circuit = qml.set_shots(circuit, shots=shots)

    estimates = np.empty(repetitions)
    for i in range(repetitions):
        L_plus = float(sampled_circuit(theta + SHIFT))
        L_minus = float(sampled_circuit(theta - SHIFT))
        estimates[i] = 0.5 * (L_plus - L_minus)
    return estimates


def theoretical_std(theta, shots):
    """Standard deviation of the shot-based parameter-shift gradient."""
    # Each shot is ±1, so one shot estimates <Z> with variance 1 - <Z>².
    # Averaging N shots divides that by N. The two circuits are independent and
    # the factor 1/2 squares to 1/4, so:
    #     Var[g] = [ (1 - L_plus²) + (1 - L_minus²) ] / (4N)
    L_plus, L_minus, _ = parameter_shift_gradient(theta)
    return np.sqrt(((1 - L_plus**2) + (1 - L_minus**2)) / (4 * shots))


# ─────────────────────────────────────────────────────────────────────────────
# 5. Visualization: distribution of shot-based gradients
# ─────────────────────────────────────────────────────────────────────────────

def plot_gradient_distributions(theta, estimates_by_shots):
    exact = exact_gradient(theta)
    all_estimates = np.concatenate(list(estimates_by_shots.values()))
    target_width = np.ptp(all_estimates) / 60

    # Same x-axis for every panel, so the spreads compare directly.
    fig, axes = plt.subplots(len(estimates_by_shots), 1, sharex=True, figsize=(9, 7), facecolor=SURFACE)
    for ax, color, (shots, estimates) in zip(axes, SHOT_COLORS, estimates_by_shots.items()):
        style_axes(ax)
        # With N shots, g = (count0_plus - count0_minus) / N can only take values
        # k/N. Bins are a whole number of those steps wide and centred on them,
        # otherwise the histogram shows gaps between the allowed values.
        step = 1 / shots
        width = max(1, round(target_width / step)) * step
        first = (np.floor(estimates.min() * shots) - 0.5) * step
        bins = np.arange(first, estimates.max() + width, width)
        ax.hist(estimates, bins=bins, color=color, edgecolor=SURFACE, linewidth=1)
        ax.axvline(exact, color=INK, linestyle="--", linewidth=1.5, label=r"exact gradient $-\sin\theta_0$")
        ax.text(0.01, 0.92, f"{shots:,} shots", transform=ax.transAxes, ha="left", va="top",
                fontsize=11, fontweight="bold", color=INK)
        ax.text(0.01, 0.72,
                f"mean = {estimates.mean():.4f}\n"
                f"std  = {estimates.std(ddof=1):.4f}  (theory {theoretical_std(theta, shots):.4f})",
                transform=ax.transAxes, ha="left", va="top", fontsize=10, color=INK_SECONDARY, family="monospace")
        ax.set_ylabel("count", color=INK_SECONDARY)

    axes[0].legend(loc="upper right", frameon=False)
    axes[-1].set_xlabel(r"estimated gradient $g_{PS}$", color=INK_SECONDARY)
    axes[0].set_title(rf"Parameter-shift gradient with finite shots at $\theta_0$ = {theta:.3f} "
                      f"({len(next(iter(estimates_by_shots.values())))} repetitions each)",
                      color=INK, loc="left", fontsize=12)
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def header(title):
    print()
    print("=" * 64)
    print(title)
    print("=" * 64)


def main():
    # Windows terminals can default to a legacy code page; θ, π and the
    # circuit-drawing characters need UTF-8.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Parameter-Shift Rule demo")
    parser.add_argument("--theta", type=float, default=np.pi / 3, help="angle θ0 in radians (default: π/3)")
    parser.add_argument("--no-show", action="store_true", help="save figures without opening windows")
    args = parser.parse_args()
    theta = args.theta
    FIGURE_DIR.mkdir(exist_ok=True)

    # ── 1. The circuit ──────────────────────────────────────────────────────
    header("1. Quantum circuit")
    print("Template:   0: ──RY(θ)──┤ <Z>")
    print(f"At θ0:      {qml.draw(circuit, decimals=3)(theta)}")

    # ── 2. Parameter-shift gradient ─────────────────────────────────────────
    header("2. Parameter-shift gradient (exact simulator)")
    L_0 = quantum_expectation(theta)
    L_plus, L_minus, gradient = parameter_shift_gradient(theta)
    gradient_exact = exact_gradient(theta)

    print(f"theta = {theta:.6f}")
    print(f"L(theta) = {L_0:.6f}")
    print()
    print(f"L(theta + pi/2) = {L_plus:.6f}")
    print(f"L(theta - pi/2) = {L_minus:.6f}")
    print()
    print(f"Parameter Shift Gradient = 0.5 * ({L_plus:.6f} - ({L_minus:.6f})) = {gradient:.6f}")
    print(f"Exact Gradient           = -sin(theta)                        = {gradient_exact:.6f}")
    print(f"Absolute Error           = {abs(gradient - gradient_exact):.2e}")

    # The rule is exact everywhere, not only at θ0.
    test_angles = np.linspace(-np.pi, np.pi, 13)
    worst = max(abs(parameter_shift_gradient(t)[2] - exact_gradient(t)) for t in test_angles)
    print(f"\nChecked {len(test_angles)} angles in [-π, π]: max |error| = {worst:.2e}")

    # ── 3. The same circuit, evaluated twice ────────────────────────────────
    header("3. Parameter shift evaluates the SAME circuit twice")
    print("Circuit A:  0: ──RY(θ + π/2)──┤ <Z>")
    print(f"            {qml.draw(circuit, decimals=3)(theta + SHIFT)}    ->  L_plus  = {L_plus:+.6f}")
    print()
    print("Circuit B:  0: ──RY(θ - π/2)──┤ <Z>")
    print(f"            {qml.draw(circuit, decimals=3)(theta - SHIFT)}    ->  L_minus = {L_minus:+.6f}")
    print()
    print(f"Combine:    gradient = 0.5 * (L_plus - L_minus) = {gradient:+.6f}")

    # Figure 1: L(θ), the two shifted evaluations and the tangent at θ0
    fig_1 = plot_loss_and_gradient(theta)
    path_1 = FIGURE_DIR / "parameter_shift_tangent.png"
    fig_1.savefig(path_1, dpi=150, facecolor=SURFACE)
    print(f"\nSaved figure: {path_1}")

    # ── 4. Shot-based experiment (separate from the exact demo above) ───────
    header(f"4. Shot-based parameter shift ({REPETITIONS} repetitions per shot count)")
    print(f"exact gradient = {gradient_exact:.6f}\n")
    print(f"{'shots':>7} | {'mean gradient':>13} | {'variance':>10} | {'std':>8} | {'theory std':>10}")
    print("-" * 61)
    estimates_by_shots = {}
    for shots in SHOT_COUNTS:
        estimates = shot_based_parameter_shift(theta, shots, REPETITIONS)
        estimates_by_shots[shots] = estimates
        print(f"{shots:>7,} | {estimates.mean():>13.6f} | {estimates.var(ddof=1):>10.2e} | "
              f"{estimates.std(ddof=1):>8.5f} | {theoretical_std(theta, shots):>10.5f}")
    print("\n10x more shots -> variance about 10x smaller -> std about 3.16x smaller.")

    # Figure 2: distribution of the shot-based estimates
    fig_2 = plot_gradient_distributions(theta, estimates_by_shots)
    path_2 = FIGURE_DIR / "shot_gradient_distributions.png"
    fig_2.savefig(path_2, dpi=150, facecolor=SURFACE)
    print(f"\nSaved figure: {path_2}")

    # ── 5. What the rule is, and what it is not ─────────────────────────────
    header("5. Key idea")
    print(
        "Parameter-Shift Rule does NOT choose between θ + π/2 and θ - π/2.\n"
        "Those two shifted points are measurements used to estimate the\n"
        "derivative at the ORIGINAL point θ.\n"
        "\n"
        "The optimizer then uses that gradient to update the circuit parameter:\n"
        "\n"
        "    θ_new = θ - η * gradient\n"
        "\n"
        "Parameter Shift:\n"
        "    two shifted circuit evaluations\n"
        "            ↓\n"
        "    expectation values\n"
        "            ↓\n"
        "    difference\n"
        "            ↓\n"
        "    gradient at θ\n"
        "            ↓\n"
        "    optimizer\n"
        "            ↓\n"
        "    new θ"
    )
    eta = 0.1
    print(f"\nExample with η = {eta}:  θ_new = {theta:.4f} - {eta} * ({gradient:.4f}) = {theta - eta * gradient:.4f}")

    if not args.no_show and matplotlib.get_backend().lower() != "agg":
        plt.show()


if __name__ == "__main__":
    main()
