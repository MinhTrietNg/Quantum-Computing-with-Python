"""Figures: L(θ) with its tangent, and the spread of shot-based gradients."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from circuit import exact_gradient, quantum_expectation
from config import SHIFT
from gradients import ShiftResult, parameter_shift_gradient, theoretical_std
from style import (
    AXIS,
    CURVE_COLOR,
    INK,
    INK_SECONDARY,
    MINUS_COLOR,
    MUTED,
    PLUS_COLOR,
    SHOT_COLORS,
    SURFACE,
    style_axes,
)

# ─────────────────────────────────────────────────────────────────────────────
# Figure 1: L(θ), the two shifted evaluations and the tangent at θ0
# ─────────────────────────────────────────────────────────────────────────────


def _draw_shift_points(
    ax: Axes, theta: float, loss_0: float, shift: ShiftResult
) -> None:
    """Mark L(θ0) and the two shifted evaluations, each with a label."""
    points = [
        # x, y, colour, marker, label, text offset, alignment
        (theta - SHIFT, shift.loss_minus, MINUS_COLOR, "^",
         r"$L(\theta_0-\pi/2)$", (-12, 14), "right"),
        (theta, loss_0, INK, "o",
         r"$L(\theta_0)$", (12, 10), "left"),
        (theta + SHIFT, shift.loss_plus, PLUS_COLOR, "s",
         r"$L(\theta_0+\pi/2)$", (-12, -18), "right"),
    ]  # fmt: skip
    for x, y, color, marker, name, offset, align in points:
        ax.vlines(x, -1.3, y, color=MUTED, linewidth=1, linestyle=":")
        ax.plot(
            x, y,
            marker=marker, markersize=10, color=color,
            markeredgecolor=SURFACE, markeredgewidth=2, zorder=5,
        )  # fmt: skip
        ax.annotate(
            f"{name} = {y:.3f}", (x, y),
            xytext=offset, textcoords="offset points",
            ha=align, va="center", color=INK, fontsize=10,
        )  # fmt: skip


def _draw_formula_box(ax: Axes, theta: float, shift: ShiftResult) -> None:
    """Write the rule with the numbers plugged in, top right of the axes."""
    text = (
        r"$g_{PS} = \frac{1}{2}\,[\,L(\theta_0+\pi/2) - L(\theta_0-\pi/2)\,]$"
        "\n"
        rf"$\quad\;\; = \frac{{1}}{{2}}\,[\,({shift.loss_plus:.3f})"
        rf" - ({shift.loss_minus:.3f})\,] = {shift.gradient:.3f}$"
        "\n"
        rf"exact $-\sin\theta_0$ = {exact_gradient(theta):.3f}"
    )
    ax.text(
        0.98, 0.97, text,
        transform=ax.transAxes, ha="right", va="top", fontsize=10, color=INK,
        bbox=dict(boxstyle="round,pad=0.5", facecolor="white", edgecolor=AXIS),
    )  # fmt: skip


def plot_loss_and_gradient(theta: float) -> Figure:
    """Plot L(θ), the two shifted evaluations and the tangent at θ0."""
    loss_0 = quantum_expectation(theta)
    shift = parameter_shift_gradient(theta)

    # One full period of L(θ), centred on θ0, evaluated point by point.
    thetas = np.linspace(theta - np.pi, theta + np.pi, 400)
    losses = [quantum_expectation(t) for t in thetas]

    fig, ax = plt.subplots(figsize=(9, 5.5), facecolor=SURFACE)
    style_axes(ax)
    ax.plot(
        thetas, losses, color=CURVE_COLOR, linewidth=2,
        label=r"$L(\theta) = \langle Z \rangle = \cos\theta$",
    )  # fmt: skip

    # Tangent at θ0 whose slope is the parameter-shift gradient.
    t = np.linspace(theta - 0.9, theta + 0.9, 2)
    ax.plot(
        t, loss_0 + shift.gradient * (t - theta), color=INK, linewidth=2,
        label=rf"tangent at $\theta_0$, slope = $g_{{PS}}$ = {shift.gradient:.3f}",
    )  # fmt: skip

    # The straight line between the two shifted points is NOT the gradient:
    # its slope is (L+ - L-)/π, while the rule divides by 2.
    secant_slope = (shift.loss_plus - shift.loss_minus) / (2 * SHIFT)
    ax.plot(
        [theta - SHIFT, theta + SHIFT], [shift.loss_minus, shift.loss_plus],
        color=MUTED, linewidth=1.5, linestyle="--",
        label=(
            f"line through shifted points, slope = {secant_slope:.3f} "
            "(not the gradient)"
        ),
    )  # fmt: skip

    _draw_shift_points(ax, theta, loss_0, shift)
    _draw_formula_box(ax, theta, shift)

    ax.set_xticks([theta - SHIFT, theta, theta + SHIFT])
    ax.set_xticklabels([
        rf"$\theta_0-\pi/2$" f"\n{theta - SHIFT:.2f}",
        rf"$\theta_0$" f"\n{theta:.2f}",
        rf"$\theta_0+\pi/2$" f"\n{theta + SHIFT:.2f}",
    ])  # fmt: skip
    ax.set_xlim(thetas[0], thetas[-1])
    ax.set_ylim(-1.3, 1.45)
    ax.set_xlabel(r"$\theta$ (radians)", color=INK_SECONDARY)
    ax.set_ylabel(r"$L(\theta)$", color=INK_SECONDARY)
    ax.set_title(
        r"Parameter-shift rule: two shifted circuits give the slope at $\theta_0$",
        color=INK, loc="left", fontsize=12,
    )  # fmt: skip
    ax.legend(
        loc="upper center", bbox_to_anchor=(0.5, -0.16),
        ncol=1, frameon=False, fontsize=9,
    )  # fmt: skip
    fig.tight_layout()
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# Figure 2: distribution of shot-based gradient estimates
# ─────────────────────────────────────────────────────────────────────────────


def _histogram_bins(
    estimates: np.ndarray, shots: int, target_width: float
) -> np.ndarray:
    """
    Return bin edges aligned with the values a shot-based gradient can take.

    With N shots, g = (count0_plus - count0_minus) / N can only take values
    k/N. Bins are a whole number of those steps wide and centred on them,
    otherwise the histogram shows gaps between the allowed values.
    """
    step = 1 / shots
    width = max(1, round(target_width / step)) * step
    first = (np.floor(estimates.min() * shots) - 0.5) * step
    return np.arange(first, estimates.max() + width, width)


def plot_gradient_distributions(
    theta: float, estimates_by_shots: dict[int, np.ndarray]
) -> Figure:
    """Plot one histogram of shot-based gradient estimates per shot count."""
    exact = exact_gradient(theta)
    all_estimates = np.concatenate(list(estimates_by_shots.values()))
    target_width = np.ptp(all_estimates) / 60
    repetitions = len(next(iter(estimates_by_shots.values())))

    # Same x-axis for every panel, so the spreads compare directly.
    fig, axes = plt.subplots(
        len(estimates_by_shots), 1, sharex=True, figsize=(9, 7), facecolor=SURFACE
    )
    panels = zip(axes, SHOT_COLORS, estimates_by_shots.items())
    for ax, color, (shots, estimates) in panels:
        style_axes(ax)
        bins = _histogram_bins(estimates, shots, target_width)
        ax.hist(estimates, bins=bins, color=color, edgecolor=SURFACE, linewidth=1)
        ax.axvline(
            exact, color=INK, linestyle="--", linewidth=1.5,
            label=r"exact gradient $-\sin\theta_0$",
        )  # fmt: skip

        stats = (
            f"mean = {estimates.mean():.4f}\n"
            f"std  = {estimates.std(ddof=1):.4f}  "
            f"(theory {theoretical_std(theta, shots):.4f})"
        )
        ax.text(
            0.01, 0.92, f"{shots:,} shots", transform=ax.transAxes,
            ha="left", va="top", fontsize=11, fontweight="bold", color=INK,
        )  # fmt: skip
        ax.text(
            0.01, 0.72, stats, transform=ax.transAxes,
            ha="left", va="top", fontsize=10, color=INK_SECONDARY,
            family="monospace",
        )  # fmt: skip
        ax.set_ylabel("count", color=INK_SECONDARY)

    axes[0].legend(loc="upper right", frameon=False)
    axes[-1].set_xlabel(r"estimated gradient $g_{PS}$", color=INK_SECONDARY)
    axes[0].set_title(
        rf"Parameter-shift gradient with finite shots at $\theta_0$ = {theta:.3f} "
        f"({repetitions} repetitions each)",
        color=INK, loc="left", fontsize=12,
    )  # fmt: skip
    fig.tight_layout()
    return fig
