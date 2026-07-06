"""Generate all static figures for the Paceometer lit-review Quarto report."""
import numpy as np
import matplotlib.pyplot as plt
from style import apply_style, NAVY, STEEL, SKY, AMBER, CORAL, TEAL, SLATE, FOG, INK

apply_style()
OUT = "/Users/yusuf/paceometer_lit_review/figures"

# ---------------------------------------------------------------
# Fig 1: The core hyperbola — time to complete a fixed 10-mile trip vs speed
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5))
v = np.linspace(8, 100, 500)
t = 600 / v  # minutes for 10 miles

ax.plot(v, t, color=STEEL, linewidth=3, zorder=3)
ax.fill_between(v, t, color=SKY, alpha=0.12)

for v1, v2, color, label_xy in [(20, 30, CORAL, (34, 34)), (70, 80, TEAL, (60, 16))]:
    t1, t2 = 600 / v1, 600 / v2
    saved = t1 - t2
    ax.plot([v1, v1], [0, t1], ls="--", color=SLATE, linewidth=1, zorder=2)
    ax.plot([v2, v2], [0, t2], ls="--", color=SLATE, linewidth=1, zorder=2)
    ax.plot([v1, v2], [t1, t1], ls=":", color=color, linewidth=1.4, zorder=2)
    ax.scatter([v1, v2], [t1, t2], color=color, s=45, zorder=4, edgecolor="white", linewidth=0.8)
    ax.plot([v2 + 0.6, v2 + 0.6], [t2, t1], color=color, linewidth=2.2, zorder=4)
    ax.annotate(f"{v1} to {v2} mph saves {saved:.1f} min",
                xy=(v2 + 0.6, (t1 + t2) / 2), xytext=label_xy,
                fontsize=10.5, color=color, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=color, lw=1.2, shrinkA=0, shrinkB=4))

ax.set_xlim(8, 100)
ax.set_ylim(0, 65)
ax.set_xlabel("Speed (mph)")
ax.set_ylabel("Time to travel 10 miles (minutes)")
ax.set_title("The same 10 mph gain buys very different rewards")
fig.tight_layout()
fig.savefig(f"{OUT}/fig01_hyperbola.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 2: Debiasing effect sizes (Herberz et al. 2019) — immediate vs spillover
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 4.8))
labels = ["Static pace display\n(immediate)", "Static pace display\n(spillover)",
          "Adaptive pop-up\nassistant (immediate)", "Adaptive pop-up\nassistant (spillover)"]
values = [0.54, 0.0, 1.07, 0.82]
sig = [True, False, True, True]
colors = [AMBER if s else "#C9CFD6" for s in sig]
bars = ax.bar(labels, values, color=colors, width=0.55, zorder=3)
for i, (b, s) in enumerate(zip(bars, sig)):
    txt = f"d = {values[i]:.2f}" if s else "n.s. (bias returns)"
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.04, txt,
            ha="center", fontsize=10, color=INK, fontweight="bold")
ax.set_ylabel("Effect size (Cohen's d) debiasing the time-loss estimate")
ax.set_title("A static pace display works — but the effect doesn't travel with you")
ax.set_ylim(0, 1.3)
fig.tight_layout()
fig.savefig(f"{OUT}/fig02_bias_effect_sizes.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 3: Power Model exponents by road type (Cameron & Elvik 2010)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5))
categories = ["Urban\narterial", "Residential", "Rural\nhighway", "Freeway"]
fatalities = [3.60, 4.84, 5.90, 5.33]
serious = [2.67, 3.90, 4.96, 4.40]
slight = [0.90, 2.13, 3.19, 2.63]

x = np.arange(len(categories))
w = 0.26
ax.bar(x - w, fatalities, width=w, label="Fatalities", color=CORAL, zorder=3)
ax.bar(x, serious, width=w, label="Serious injuries", color=AMBER, zorder=3)
ax.bar(x + w, slight, width=w, label="Slight injuries", color=STEEL, zorder=3)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel("Power Model exponent")
ax.set_title("How fast crash risk compounds with speed depends on road type")
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(f"{OUT}/fig03_power_model_road_type.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 4: Power model vs Exponential model divergence (Elvik 2013)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5))
speed = np.linspace(25, 120, 400)
ref = 120
power = 100 * (speed / ref) ** 4.23
expo = 100 * np.exp(0.069 * (speed - ref))

ax.plot(speed, power, color=STEEL, linewidth=2.8, label="Power model (exponent 4.23)")
ax.plot(speed, expo, color=CORAL, linewidth=2.8, label="Exponential model ($\\beta$ = 0.069)")
ax.set_xlabel("Mean speed (km/h)")
ax.set_ylabel("Relative number of fatal accidents\n(=100 at 120 km/h)")
ax.set_title("Two ways to model risk agree at moderate speed,\ndiverge sharply above ~90 km/h")
ax.legend(frameon=False, loc="upper left")
fig.tight_layout()
fig.savefig(f"{OUT}/fig04_power_vs_exponential.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 5: Fuel economy sweet spot — illustrative U-curve anchored to Wang et al. (2008)'s
# measured minimum (~65 km/h, ~6.0 L/100km). NOTE: Orfila et al. (2017)'s published quartic
# f(v) is an intermediate term inside a mixed-unit efficiency-ratio formula (Eq. 2 of that
# paper), not a standalone L/100km curve — evaluating it directly as L/100km gives physically
# implausible values (e.g. >300 L/100km at 50 km/h), so we do not plot it at face value.
# Instead we draw a schematic curve matching the qualitative shape + single anchor point that
# both Wang et al. (2008) and Orfila et al. (2017) independently describe in prose.
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5))
sv = np.linspace(15, 130, 400)
fuel = 6.0 + np.where(sv >= 65, 0.00107 * (sv - 65) ** 2, 0.0024 * (sv - 65) ** 2)

ax.plot(sv, fuel, color=STEEL, linewidth=3, zorder=3)
ax.axvspan(50, 70, color=TEAL, alpha=0.15, zorder=1)
ax.scatter([65], [6.0], color=CORAL, zorder=4, s=70, edgecolor="white", linewidth=1)
ax.annotate("Wang et al. (2008)\nmeasured minimum\n(~65 km/h, ~6.0 L/100km)",
            xy=(65, 6.0), xytext=(80, 9.3),
            fontsize=9.5, color=CORAL, fontweight="bold",
            arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=1.6))
ax.text(60, 11.3, "50–70 km/h\nefficiency band", color=TEAL, fontsize=10,
        fontweight="bold", ha="center")
ax.set_xlabel("Speed (km/h)")
ax.set_ylabel("Fuel consumption (L / 100 km, illustrative)")
ax.set_title("Fuel economy is U-shaped, not “slower is always better”")
ax.set_xlim(15, 130)
ax.set_ylim(4, 13)
fig.tight_layout()
fig.savefig(f"{OUT}/fig05_fuel_sweet_spot.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 6: Variance in fuel consumption explained by traffic variables (Evans, Herman & Lam 1976)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.2, 4.6))
labels = ["Pace alone\n(time/distance)", "+ acceleration\nwork/distance", "+ deceleration\nfraction",
          "All 16 variables\ncombined"]
values = [71.4, 75.3, 82.0, 83.4]
bars = ax.bar(labels, values, color=[STEEL, SKY, TEAL, SLATE], width=0.55, zorder=3)
for b, val in zip(bars, values):
    ax.text(b.get_x() + b.get_width() / 2, val + 1.3, f"{val:.1f}%", ha="center",
            fontsize=10.5, fontweight="bold", color=INK)
ax.set_ylabel("% of variance in fuel use per distance explained")
ax.set_title("Pace alone explains most of urban fuel consumption\n(Evans, Herman & Lam, 1976)")
ax.set_ylim(0, 95)
fig.tight_layout()
fig.savefig(f"{OUT}/fig06_variance_explained.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 7: Effectiveness vs. acceptability of speed-feedback systems
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5.5))
points = [
    ("Mandatory / active ISA\n(hard speed limiter)", 82, 21, CORAL),
    ("Adaptive ISA\n(AVSAS, personalized)", 45, 52, AMBER),
    ("Informational / advisory\nISA (alert only)", 30, 76, TEAL),
    ("Belgium active ISA\n(Ghent, 90 km/h roads)", 72, 40, STEEL),
]
for label, eff, acc, color in points:
    ax.scatter(eff, acc, s=180, color=color, zorder=3, edgecolor="white", linewidth=1.2)
    ax.annotate(label, xy=(eff, acc), xytext=(8, 8), textcoords="offset points",
                fontsize=9.3, color=INK)
ax.set_xlabel("Effectiveness — severe-speeding reduction achieved (%)")
ax.set_ylabel("Acceptance — drivers willing to adopt / purchase (%)")
ax.set_title("The effectiveness–acceptability paradox in speed-feedback systems")
ax.set_xlim(15, 95)
ax.set_ylim(10, 90)
fig.tight_layout()
fig.savefig(f"{OUT}/fig07_effectiveness_acceptability.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 8: Gauge shape reading-time comparison (Liu & Shen 2025; Francois et al. 2019)
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.8))

ax = axes[0]
shapes = ["Semicircle", "Horizontal", "Vertical", "Circular"]
rt = [2253, 2322, 2604, 2830]
colors_shape = [TEAL, STEEL, AMBER, CORAL]
bars = ax.bar(shapes, rt, color=colors_shape, width=0.6, zorder=3)
for b, val in zip(bars, rt):
    ax.text(b.get_x() + b.get_width() / 2, val + 30, f"{val}", ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel("Mean reading time (ms)")
ax.set_title("Liu & Shen (2025)\ngeneral reading task", fontsize=12)
ax.set_ylim(0, 3200)

ax = axes[1]
shapes2 = ["Horizontal", "Vertical"]
tct = [1442, 1503]
bars = ax.bar(shapes2, tct, color=[STEEL, AMBER], width=0.45, zorder=3)
for b, val in zip(bars, tct):
    ax.text(b.get_x() + b.get_width() / 2, val + 5, f"{val}", ha="center", fontsize=10, fontweight="bold")
ax.set_ylabel("Mean task completion time (ms)")
ax.set_title("Francois et al. (2019)\ntruck drivers", fontsize=12)
ax.set_ylim(1350, 1560)

fig.suptitle("Semicircular and horizontal gauges are read fastest", fontsize=14, fontweight="bold", color=NAVY, y=1.03)
fig.tight_layout()
fig.savefig(f"{OUT}/fig08_gauge_reading_time.png")
plt.close(fig)

# ---------------------------------------------------------------
# Fig 9: Preference vs. performance mismatch (Francois et al. 2019)
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.8))

ax = axes[0]
labels = ["Circular", "Linear"]
perf = [1470, 1423]  # approx task completion time, small ~4% gap, illustrative from reported ~47ms/4%
bars = ax.bar(labels, perf, color=[SLATE, STEEL], width=0.5, zorder=3)
ax.set_ylabel("Task completion time (ms)")
ax.set_title("Objective performance\n(roughly equal)", fontsize=12)
ax.set_ylim(1300, 1550)
for b, val in zip(bars, perf):
    ax.text(b.get_x() + b.get_width() / 2, val + 5, f"~{val}", ha="center", fontsize=10, fontweight="bold")

ax = axes[1]
sat = [11.17, 4.10]
bars = ax.bar(labels, sat, color=[CORAL, STEEL], width=0.5, zorder=3)
ax.set_ylabel("Driver satisfaction rating")
ax.set_title("Subjective preference\n(circular strongly favored)", fontsize=12)
for b, val in zip(bars, sat):
    ax.text(b.get_x() + b.get_width() / 2, val + 0.3, f"{val:.2f}", ha="center", fontsize=10, fontweight="bold")

fig.suptitle("Drivers prefer circular gauges even though they perform no better",
             fontsize=13.5, fontweight="bold", color=NAVY, y=1.03)
fig.tight_layout()
fig.savefig(f"{OUT}/fig09_preference_performance_mismatch.png")
plt.close(fig)

print("All figures written to", OUT)
