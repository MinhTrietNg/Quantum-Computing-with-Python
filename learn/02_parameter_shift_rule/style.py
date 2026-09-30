"""Shared chart colours, axes theme and figure saving."""

from matplotlib.axes import Axes
from matplotlib.figure import Figure

from config import FIGURE_DIR, FIGURE_DPI

# Curve / θ+π/2 / θ-π/2 were checked for colour-blind separation; every
# point also gets its own marker shape and a text label.
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
SURFACE = "#fcfcfb"
CURVE_COLOR = "#2a78d6"
PLUS_COLOR = "#eb6834"
MINUS_COLOR = "#1baf7a"
SHOT_COLORS = ("#86b6ef", "#2a78d6", "#104281")  # light -> dark = few -> many


def style_axes(ax: Axes) -> None:
    """Apply the shared light theme to one set of axes."""
    ax.set_facecolor(SURFACE)
    ax.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
    ax.tick_params(colors=INK_SECONDARY)


def save_figure(fig: Figure, filename: str) -> None:
    """Save a figure into FIGURE_DIR and report its path."""
    FIGURE_DIR.mkdir(exist_ok=True)
    path = FIGURE_DIR / filename
    fig.savefig(path, dpi=FIGURE_DPI, facecolor=SURFACE)
    print(f"\nSaved figure: {path}")
