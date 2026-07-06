import matplotlib as mpl
import matplotlib.pyplot as plt

NAVY = "#0B2545"
STEEL = "#1B4E8C"
SKY = "#4C8FD4"
AMBER = "#E8A23D"
CORAL = "#D9603B"
TEAL = "#2E8B7C"
SLATE = "#5C6B7A"
FOG = "#F4F6F8"
INK = "#1C2530"

def apply_style():
    mpl.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": SLATE,
        "axes.labelcolor": INK,
        "axes.titlecolor": NAVY,
        "text.color": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.grid": True,
        "grid.color": "#E3E7EC",
        "grid.linewidth": 0.8,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Arial", "DejaVu Sans"],
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 12,
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "savefig.bbox": "tight",
        "savefig.facecolor": "white",
    })
