"""Charts for deck v4. Every number is from a source cited in Peter & Devlin (2025); source on the slide.
Run: ../.venv/Scripts/python charts.py  -> charts/*.png (300 dpi, deck colours)"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path("charts"); OUT.mkdir(exist_ok=True)
BG, INK, MUTED, ACCENT, SOFT, LINE = "#F2F5F3", "#17231F", "#5E6B66", "#2C6E5F", "#BCCFC8", "#D3DED9"
FONT = "Segoe UI" if any("Segoe UI" in f.name for f in font_manager.fontManager.ttflist) else "DejaVu Sans"
plt.rcParams.update({"font.family": FONT, "font.size": 17, "axes.edgecolor": LINE, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "figure.facecolor": BG, "axes.facecolor": BG,
                     "savefig.facecolor": BG, "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


# 1. Kirk et al. 2024 (ICLR), Table 11: per-input diversity (EAD), OPT models, summarisation
sizes = ["125M", "350M", "1.3B", "2.7B", "6.7B"]
sft = [0.81, 0.80, 0.81, 0.80, 0.79]
rlhf = [0.15, 0.15, 0.13, 0.16, 0.07]
fig, ax = plt.subplots(figsize=(8.6, 4.8))
x = range(len(sizes)); w = 0.38
b1 = ax.bar([i - w / 2 for i in x], sft, w, color=SOFT, label="Before RLHF")
b2 = ax.bar([i + w / 2 for i in x], rlhf, w, color=ACCENT, label="After RLHF")
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.015, f"{b.get_height():.2f}", ha="center",
                va="bottom", fontsize=15, color=INK)
ax.set_xticks(list(x)); ax.set_xticklabels(sizes)
ax.set_xlabel("Model size (OPT, parameters)")
ax.set_ylabel("Answer variety (EAD)")
ax.set_ylim(0, 1.05); ax.yaxis.grid(True, color=LINE, lw=0.8); ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper right", ncol=2, fontsize=16)
save(fig, "rlhf_diversity")

# 2. Our proposed metric (illustrative example, not data): Overton coverage of a voter-bot answer
parties = ["A", "B", "C", "D", "E", "F"]
covered = [1, 1, 1, 0, 1, 0]
fig, ax = plt.subplots(figsize=(7.8, 2.6)); ax.axis("off")
for i, (p, c) in enumerate(zip(parties, covered)):
    ax.add_patch(plt.Rectangle((i * 1.15, 0), 1.0, 1.0, color=ACCENT if c else "white", ec=ACCENT, lw=2))
    ax.text(i * 1.15 + 0.5, 0.5, "yes" if c else "no", ha="center", va="center", fontsize=19,
            color="white" if c else ACCENT)
    ax.text(i * 1.15 + 0.5, -0.32, "Party " + p, ha="center", va="center", fontsize=13, color=MUTED)
ax.text(7.2, 0.5, "4 / 6 = 67%", ha="left", va="center", fontsize=27, color=INK, weight="bold")
ax.set_xlim(-0.1, 10.2); ax.set_ylim(-0.7, 1.2)
save(fig, "overton_metric")
print("charts:", sorted(p.name for p in OUT.iterdir()))
