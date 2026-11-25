"""Charts for deck v3. Every number is from a source cited in Peter & Devlin (2025); source under each chart.
Run: python charts.py  -> charts/*.png (300 dpi, deck colours)"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path("charts"); OUT.mkdir(exist_ok=True)
BG, INK, MUTED, ACCENT, SOFT, LINE = "#F2F5F3", "#17231F", "#5E6B66", "#2C6E5F", "#BCCFC8", "#D3DED9"
FONT = "Segoe UI" if any("Segoe UI" in f.name for f in font_manager.fontManager.ttflist) else "DejaVu Sans"
plt.rcParams.update({"font.family": FONT, "font.size": 15, "axes.edgecolor": LINE, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": MUTED, "figure.facecolor": BG, "axes.facecolor": BG,
                     "savefig.facecolor": BG, "axes.spines.top": False, "axes.spines.right": False})


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


# 1. Kirk et al. 2024 (ICLR), Table 11: per-input diversity (EAD), OPT models, summarisation
sizes = ["125M", "350M", "1.3B", "2.7B", "6.7B"]
sft = [0.81, 0.80, 0.81, 0.80, 0.79]
rlhf = [0.15, 0.15, 0.13, 0.16, 0.07]
fig, ax = plt.subplots(figsize=(8.6, 4.6))
x = range(len(sizes)); w = 0.36
b1 = ax.bar([i - w / 2 for i in x], sft, w, color=SOFT, label="Before RLHF (SFT only)")
b2 = ax.bar([i + w / 2 for i in x], rlhf, w, color=ACCENT, label="After RLHF")
for bars in (b1, b2):
    for b in bars:
        ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.015, f"{b.get_height():.2f}", ha="center",
                va="bottom", fontsize=12, color=INK)
ax.set_xticks(list(x)); ax.set_xticklabels([f"OPT {s}" for s in sizes])
ax.set_ylabel("Output diversity (EAD, higher = more varied)")
ax.set_ylim(0, 1.0); ax.yaxis.grid(True, color=LINE, lw=0.8); ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper right", ncol=2, fontsize=13)
save(fig, "rlhf_diversity")

# 2. Prior inclusive efforts: participants (as reported in Peter & Devlin 2025, Prior work)
names = ["STELA", "Collective\nConstitutional AI", "PRISM", "Rose et al."]
vals = [44, 1000, 1500, 15000]
labels = ["44", "~1,000", "1,500", "~15,000"]
fig, ax = plt.subplots(figsize=(6.2, 4.2))
ax.barh(names, vals, color=[SOFT, ACCENT, SOFT, SOFT], height=0.55)
for i, (v, l) in enumerate(zip(vals, labels)):
    ax.text(v * 1.15, i, l, va="center", fontsize=17, color=INK)
ax.set_xscale("log"); ax.set_xlim(20, 60000)
ax.set_xticks([100, 1000, 10000]); ax.set_xticklabels(["100", "1,000", "10,000"]); ax.minorticks_off()
ax.set_xlabel("Participants (log scale)")
ax.spines["left"].set_visible(False); ax.tick_params(axis="y", length=0, labelsize=17, labelcolor=INK)
ax.invert_yaxis()
save(fig, "prior_participants")

# 3. CCAI funnel: Anthropic 2023 blog + Peter & Devlin 2025 (adopted 1 principle, citing Anthropic 2024)
steps = [("38,252", "votes by ~1,000\nAmericans"), ("1,127", "statements written"),
         ("75", "principles in the\npublic constitution"), ("1", "adopted in later\nClaude models")]
fig, ax = plt.subplots(figsize=(7.2, 4.8)); ax.axis("off")
widths = [1.0, 0.74, 0.48, 0.16]
for i, ((num, lab), wd) in enumerate(zip(steps, widths)):
    y = 3 - i
    col = ACCENT if i == 3 else SOFT
    ax.add_patch(plt.Rectangle((0.5 - wd / 2, y - 0.38), wd, 0.76, color=col, lw=0))
    ax.text(0.5, y, num, ha="center", va="center", fontsize=24, color="white" if i == 3 else INK, weight="bold")
    ax.text(1.06, y, lab, ha="left", va="center", fontsize=18, color=INK)
ax.set_xlim(0, 2.25); ax.set_ylim(-0.6, 3.6)
save(fig, "ccai_funnel")

# 4. Our proposed metric (illustrative example, not data): Overton coverage of a voter-bot answer
parties = ["Party A", "Party B", "Party C", "Party D", "Party E", "Party F"]
covered = [1, 1, 1, 0, 1, 0]
fig, ax = plt.subplots(figsize=(7.8, 2.6)); ax.axis("off")
for i, (p, c) in enumerate(zip(parties, covered)):
    ax.add_patch(plt.Rectangle((i * 1.15, 0), 1.0, 1.0, color=ACCENT if c else "white", ec=ACCENT, lw=2))
    ax.text(i * 1.15 + 0.5, 0.5, "yes" if c else "no", ha="center", va="center", fontsize=18,
            color="white" if c else ACCENT)
    ax.text(i * 1.15 + 0.5, -0.32, p, ha="center", va="center", fontsize=13, color=MUTED)
ax.text(7.2, 0.5, "4 / 6 = 67%", ha="left", va="center", fontsize=26, color=INK, weight="bold")
ax.set_xlim(-0.1, 10.2); ax.set_ylim(-0.7, 1.2)
save(fig, "overton_metric")
# 5. Atari et al. 2023 "Which Humans?": GPT closest vs farthest cultures (order from their cluster analysis)
close = ["United States", "Uruguay", "Canada", "Great Britain", "Australia", "Germany", "Netherlands"]
far = ["Kyrgyzstan", "Pakistan", "Ethiopia"]
fig, ax = plt.subplots(figsize=(11, 2.4)); ax.axis("off")
ax.annotate("", xy=(10.9, 0), xytext=(-0.3, 0), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.5))
ax.plot([-0.6], [0], "o", ms=22, color=INK); ax.text(-0.6, 0, "GPT", color="white", ha="center", va="center", fontsize=11, weight="bold")
for i, c in enumerate(close):
    xx = 0.55 + i * 0.62
    ax.plot([xx], [0], "o", ms=11, color=ACCENT)
    ax.text(xx, 0.32 if i % 2 == 0 else -0.36, c, ha="center", va="center", fontsize=12, color=INK)
for i, c in enumerate(far):
    xx = 8.0 + i * 0.95
    ax.plot([xx], [0], "o", ms=11, color=SOFT)
    ax.text(xx, 0.32 if i % 2 == 0 else -0.36, c, ha="center", va="center", fontsize=12, color=INK)
ax.text(2.4, -0.85, "most similar to GPT", ha="center", fontsize=12, color=ACCENT)
ax.text(8.95, -0.85, "least similar", ha="center", fontsize=12, color=MUTED)
ax.set_xlim(-1.1, 11.1); ax.set_ylim(-1.1, 0.7)
save(fig, "weird_strip")
print("charts:", sorted(p.name for p in OUT.iterdir()))
