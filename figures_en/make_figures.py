"""Regenerate the article figures with English text.

Data for Figures 4 and 9 were recovered from the original (Spanish) figures;
the values of Figures 6, 7 and 8 are those reported in the article.
Run:  python make_figures.py   (writes PNG + PDF next to this script)
"""
import json
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SANS = "Liberation Sans"   # Arial-compatible (as in the original figures)
plt.rcParams.update({"mathtext.fontset": "custom", "mathtext.bf": "Liberation Sans:bold",
                     "font.family": SANS})


def save(fig, name, dpi):
    fig.savefig(os.path.join(HERE, name + ".png"), dpi=dpi)
    fig.savefig(os.path.join(HERE, name + ".pdf"))
    plt.close(fig)


# ---------------------------------------------------------------- helpers
def box(ax, x, y, w, h, fc, ec, lw=1.2, r=0.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw))


def arrow(ax, p0, p1, color="#333", lw=1.0, cs="arc3", ms=10, style="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=style, mutation_scale=ms,
                                 color=color, lw=lw, connectionstyle=cs,
                                 shrinkA=0, shrinkB=0))


# ================================================================ Figure 1
def fig1():
    W, H = 14.7, 10.255
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    plt.rcParams["font.family"] = SANS
    phases = [
        ("Data\nunderstanding", "#dbe8fb", "#6d8fd6"),
        ("Data\npreparation", "#e3f1dc", "#7cb36a"),
        ("Modeling", "#fdf0d0", "#e0b44f"),
        ("Evaluation", "#f7d6d6", "#d26464"),
        ("Deployment", "#e9e0f3", "#9a7cc0"),
    ]
    rows = [
        [("Data source and relational integration",
          "ENDES 2007–2025 (INEI): modules RECH0, RECH1, RECH6, RECH23 and REC41 (via REC21), joined by\n"
          "HHID / CASEID → N = 304,271 children under 5 years of age")],
        [("Target variable and data leakage prevention",
          "Y = 1 if HAZ < −2 SD (WHO); prevalence 15.8% (1 : 5.3). Height (HC3), weight (HC2) and variables\n"
          "recorded after the measurement are excluded")],
        [("Preprocessing",
          "Harmonization of codes across years · missing values · categorical encoding · child–mother consistency > 99.9%")],
        [("Four-stage feature selection",
          "189 columns → S1: missing > 60% · S2: |r| > 0.80 and VIF > 5 · S3: χ² and Kruskal–Wallis (p < 0.05) → 74 →\n"
          "S4: gradient boosting importance → $\\bf{45\\ variables}$ (+ sufficiency check)")],
        [("Class imbalance handling",
          "Class weights (balanced / scale_pos_weight) · INEI expansion factor (HV005) for representativeness ·\n"
          "triage-oriented decision threshold τ")],
        [("Model training and comparison",
          "Logistic regression (L2), CART, XGBoost, CatBoost, MLP 3×200 and LightGBM · stratified 5-fold cross-validation")],
        [("Performance evaluation",
          "AUC-ROC, AUC-PR, sensitivity, precision, specificity and F1 ·\n95% bootstrap CI (1,000) · DeLong test"),
         ("SHAP explainability",
          "TreeExplainer · local explanation and aggregated by\ndepartment and natural region")],
        [("Implementation and reproducibility",
          "Streamlit web application (3 layers) · Docker, Makefile and Zenodo"),
         ("Relevance assessment",
          "Panel of 4 health professionals · TAM2-based instrument")],
    ]
    phase_of_row = [0, 0, 1, 1, 2, 2, 3, 4]
    x0, x1 = 3.0, 14.25
    rh, gap = 0.82, 0.40
    y = 0.70
    ys = []
    for i in range(len(rows)):
        ys.append(y)
        y += rh + gap
    # phase panels
    for p, (name, fc, ec) in enumerate(phases):
        idx = [i for i, q in enumerate(phase_of_row) if q == p]
        top, bot = ys[idx[0]] - 0.12, ys[idx[-1]] + rh + 0.12
        box(ax, 0.55, top, 2.15, bot - top, fc, ec)
        ax.text(1.625, (top + bot) / 2, name, ha="center", va="center", fontsize=12.5,
                fontweight="bold", color="#222")
    for i, row in enumerate(rows):
        ec = phases[phase_of_row[i]][2]
        n = len(row)
        bw = (x1 - x0 - 0.3 * (n - 1)) / n
        for j, (t, s) in enumerate(row):
            bx = x0 + j * (bw + 0.3)
            box(ax, bx, ys[i], bw, rh, "white", ec)
            ax.text(bx + bw / 2, ys[i] + 0.24, t, ha="center", va="center",
                    fontsize=11, fontweight="bold", color="#111")
            ax.text(bx + bw / 2, ys[i] + 0.56, s, ha="center", va="center",
                    fontsize=8.6, color="#222", linespacing=1.35)
            if i + 1 < len(rows):
                n2 = len(rows[i + 1])
                if n2 == n:
                    cx = bx + bw / 2
                    arrow(ax, (cx, ys[i] + rh + 0.04), (cx, ys[i + 1] - 0.04), ms=9)
                else:  # 1 -> 2 split
                    bw2 = (x1 - x0 - 0.3) / 2
                    for k in range(2):
                        cx = x0 + k * (bw2 + 0.3) + bw2 / 2
                        arrow(ax, (cx, ys[i] + rh + 0.04), (cx, ys[i + 1] - 0.04), ms=9)
    save(fig, "fig01_crisp_dm_workflow", 200)


# ================================================================ Figure 2
def fig2():
    W, H = 18.75, 8.225
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    navy, grey = "#1d3557", "#444"
    ax.text(0.45, 0.32, "HOUSEHOLD MODULES (ENDES 2007–2025)", fontsize=11, fontweight="bold",
            color=navy, va="center")
    ax.text(15.25, 0.32, "MOTHER MODULES", fontsize=11, fontweight="bold", color=navy, va="center")
    mods = [("RECH0", "Household interview\nmetadata"),
            ("RECH1", "Household roster:\ndemographic characteristics\nof members"),
            ("RECH6", "Anthropometry and child health\n(HAZ = HC70/100)"),
            ("RECH23", "Housing, water, sanitation\nand geographic altitude"),
            ("REC41", "Obstetric history, prenatal\ncare, birth weight")]
    bw, bh, y0 = 3.2, 1.55, 0.65
    xs = [0.6, 4.3, 8.0, 11.7, 15.4]
    for x, (t, s) in zip(xs, mods):
        box(ax, x, y0, bw, bh, "white", grey, lw=1.3, r=0.12)
        ax.text(x + bw / 2, y0 + 0.35, t, ha="center", va="center", fontsize=14,
                fontweight="bold", color=navy)
        ax.text(x + bw / 2, y0 + 0.95, s, ha="center", va="center", fontsize=9.5,
                color="#222", linespacing=1.3)
    # REC21 bridge
    rx, ry, rw, rh = 15.4, 3.15, 3.2, 1.35
    box(ax, rx, ry, rw, rh, "#fdf1dd", "#e3a54a", lw=1.3, r=0.12)
    ax.text(rx + rw / 2, ry + 0.3, "REC21", ha="center", va="center", fontsize=14,
            fontweight="bold", color=navy)
    ax.text(rx + rw / 2, ry + 0.85, "Bridge table: links each\nchild to their mother\none-to-one",
            ha="center", va="center", fontsize=9.5, color="#222", linespacing=1.3)
    cx = 15.4 + bw / 2
    arrow(ax, (cx, y0 + bh), (cx, ry - 0.02), color=navy, lw=2, ms=18)
    ax.text(cx + 0.12, 2.95, "CASEID", fontsize=9, fontweight="bold", color=navy, va="center")
    # join lines: every module feeds one horizontal bus that drops into the merge
    yj = 5.0
    for x in xs[:4]:
        ax.plot([x + bw / 2] * 2, [y0 + bh, yj], color=navy, lw=2)
    ax.plot([cx, cx], [ry + rh, yj], color=navy, lw=2)
    ax.plot([xs[0] + bw / 2, cx], [yj, yj], color=navy, lw=2, solid_capstyle="round")
    ax.text(4.05, yj - 0.12, "join by HHID (household)", fontsize=9.5, fontweight="bold",
            color=navy, ha="center", va="bottom")
    ax.text(15.15, yj - 0.12, "join by CASEID (mother)", fontsize=9.5, fontweight="bold",
            color=navy, ha="center", va="bottom")
    mx, my, mw, mh = 5.9, 5.6, 5.7, 1.05
    arrow(ax, (mx + mw / 2, yj), (mx + mw / 2, my - 0.01), color=navy, lw=2, ms=22)
    box(ax, mx, my, mw, mh, "#eaf0f8", grey, lw=1.3, r=0.12)
    ax.text(mx + mw / 2, my + 0.3, "Relational merge", ha="center", va="center",
            fontsize=13, fontweight="bold", color=navy)
    ax.text(mx + mw / 2, my + 0.72,
            "Composite keys HHID / CASEID · child–mother consistency\naudit (> 99.9% in sex and year of birth)",
            ha="center", va="center", fontsize=9.3, color="#222", linespacing=1.3)
    arrow(ax, (mx + mw / 2, my + mh), (mx + mw / 2, 7.0), color=navy, lw=2, ms=22)
    dx, dy, dw, dh = 6.65, 7.0, 4.2, 1.0
    box(ax, dx, dy, dw, dh, navy, navy, r=0.12)
    ax.text(dx + dw / 2, dy + 0.3, "Consolidated dataset", ha="center", va="center",
            fontsize=13, fontweight="bold", color="white")
    ax.text(dx + dw / 2, dy + 0.7, "N = 304,271 children under 5 with valid\nanthropometry",
            ha="center", va="center", fontsize=9.3, color="white", linespacing=1.3)
    save(fig, "fig02_endes_integration", 200)


# ================================================================ Figure 3
def fig3():
    W, H = 10.16, 5.77
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    plt.rcParams["font.family"] = SANS
    lay_ec, lay_fc = "#b9c6d6", "#ffffff"
    bfc, bec = "#e8f0fb", "#4a6fa5"
    fs = 7.6

    def layer(x, y, w, h, t):
        ax.add_patch(Rectangle((x, y), w, h, fc=lay_fc, ec=lay_ec, lw=1))
        ax.text(x + 0.08, y + 0.13, t, ha="left", va="center", fontsize=8.5,
                fontweight="bold", color="#33475b")

    def b(cx, cy, w, h, t):
        ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, fc=bfc, ec=bec, lw=1))
        ax.text(cx, cy, t, ha="center", va="center", fontsize=fs, color="#111", linespacing=1.25)
        return cx, cy, w, h

    layer(1.0, 0.07, 8.1, 1.03, "Presentation layer")
    layer(0.55, 1.68, 6.3, 2.0, "Logic layer")
    layer(0.45, 4.42, 9.25, 1.03, "Data layer")
    c1 = b(2.65, 0.6, 2.0, 0.52, "Single-child assessment\nand score explanation")
    c2 = b(5.2, 0.6, 2.3, 0.52, "Group assessment (CSV or\nExcel) and prioritized list")
    c3 = b(7.7, 0.6, 1.95, 0.52, "Territorial risk map\n(25 departments)")
    e = b(2.4, 2.2, 1.55, 0.52, "LightGBM\ninference engine")
    s = b(4.6, 2.2, 2.2, 0.52, "Contribution of each variable\n(SHAP values)")
    t = b(3.95, 3.15, 2.0, 0.52, "Priority threshold based\non the chosen coverage")
    d1 = b(1.6, 4.95, 1.6, 0.52, "Model and metadata\n(.pkl, .json)")
    d2 = b(3.95, 4.95, 1.9, 0.52, "Coverage–threshold curve\n(.json)")
    d3 = b(7.75, 4.95, 2.4, 0.52, "SHAP by department (.csv)\nand geometries (GeoJSON)")
    col = "#5b7fb4"
    bot = lambda q, dx=0: (q[0] + dx, q[1] + q[3] / 2)
    top = lambda q, dx=0: (q[0] + dx, q[1] - q[3] / 2)
    arrow(ax, bot(c1, -0.3), top(e, -0.15), col, cs="arc3,rad=0.25", ms=9)
    arrow(ax, bot(c1, 0.3), top(s, -0.3), col, cs="arc3,rad=0.2", ms=9)
    arrow(ax, bot(c2, -0.4), top(e, 0.2), col, cs="arc3,rad=-0.2", ms=9)
    arrow(ax, bot(c2, 0.7), top(s, 0.3), col, cs="arc3,rad=-0.3", ms=9)
    arrow(ax, bot(c3), top(d3), col, ms=9)
    arrow(ax, bot(e, -0.45), top(d1), col, cs="arc3,rad=0.25", ms=9)
    arrow(ax, bot(e, 0.5), top(t), col, cs="arc3,rad=-0.25", ms=9)
    arrow(ax, bot(t), top(d2), col, ms=9)
    save(fig, "fig03_architecture", 200)


# ================================================================ Figure 4
def fig4():
    d = json.load(open(os.path.join(HERE, "data_fig4.json")))
    yrs = np.arange(2007, 2026)
    plt.rcParams["font.family"] = SANS
    fig = plt.figure(figsize=(13, 6.6))
    ax = fig.add_axes([0.058, 0.13, 0.91, 0.72])
    ax.axvspan(2017.5, 2025.4, color="#f1f0ec", zorder=0)
    ax.text(2021.45, 47.3, "2018–2025: stagnation at around 12%", ha="center", va="center",
            fontsize=13, color="#6b6b6b")
    spec = [("rural", "#eb6834", 2.2, "Rural 21.5%", False),
            ("nac", "#2a78d6", 4.5, "National 12.0%", True),
            ("urb", "#1baf7a", 2.2, "Urban 7.9%", False)]
    for key, c, lw, lab, bold in spec:
        v = d[key]
        ax.plot(yrs, v, color=c, lw=lw, zorder=3, solid_capstyle="round")
        ax.scatter([2007], [v[0]], s=40, color=c, zorder=4)
        ax.scatter([2025], [v[-1]], s=70, color=c, edgecolor="white", lw=2, zorder=4)
        ax.text(2006.6, v[0], f"{v[0]:.1f}%", ha="right", va="center", fontsize=13)
        ax.text(2025.5, v[-1], lab, ha="left", va="center", fontsize=15,
                fontweight="bold" if bold else "normal", color="#111")
    ax.set_xlim(2005.6, 2027.9); ax.set_ylim(0, 50)
    ax.set_yticks(range(0, 51, 10)); ax.set_yticklabels([f"{t}%" for t in range(0, 51, 10)])
    ax.set_xticks(range(2007, 2026, 2))
    ax.tick_params(length=0, labelsize=14, colors="#666", pad=8)
    ax.grid(axis="y", color="#e2e2e2", lw=1)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_axisbelow(True)
    fig.text(0.058, 0.965, "Childhood stunting in children under 5, Peru 2007–2025",
             fontsize=21, fontweight="bold", color="#222", va="top")
    fig.text(0.058, 0.905, "Weighted prevalence (height-for-age < −2 SD, WHO standard). "
             "It fell to less than half by 2017 and has remained stable since then.",
             fontsize=13, color="#6b6b6b", va="top")
    fig.text(0.058, 0.04, "Source: ENDES 2007–2025 (INEI), 304,271 children with valid anthropometry; "
             "own elaboration using the HV005 expansion factor.", fontsize=10.5, color="#6b6b6b")
    save(fig, "fig04_prevalence_trend", 200)


# ================================================================ Figure 6
def fig6():
    plt.rcParams["font.family"] = "DejaVu Sans"
    m = np.array([[73.8, 26.2], [24.7, 75.3]])
    fig = plt.figure(figsize=(4.217, 3.31))
    ax = fig.add_axes([0.335, 0.155, 0.645, 0.82])
    ax.imshow(m, cmap="Blues", vmin=0, vmax=100)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{m[i, j]:.1f} %", ha="center", va="center", fontsize=12,
                    color="white" if m[i, j] > 50 else "black")
    labs = ["No stunting", "Stunting"]
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9.5)
    ax.set_yticks([0, 1]); ax.set_yticklabels(labs, fontsize=9.5)
    ax.set_xlabel("Predicted class", fontsize=11)
    ax.set_ylabel("True class", fontsize=11)
    save(fig, "fig06_confusion_matrix", 300)


# ================================================================ Figure 7
def fig7():
    plt.rcParams["font.family"] = SANS
    labs = ["Household poverty", "Low birth weight", "Altitude of residence", "Size at birth",
            "Child's age", "Birth interval", "Child's sex", "Anemia (hemoglobin)",
            "Household members", "Breastfeeding duration", "Kitchen smoke outlet",
            "Mother's education", "Formula in the first days", "Glass windows", "Rural residence"]
    vals = [0.4234, 0.4109, 0.2611, 0.2482, 0.1941, 0.1937, 0.1556, 0.1408, 0.1286, 0.1206,
            0.0901, 0.0878, 0.0790, 0.0672, 0.0630]
    fig = plt.figure(figsize=(9, 6.2))
    ax = fig.add_axes([0.287, 0.10, 0.69, 0.87])
    y = np.arange(len(vals))
    ax.barh(y, vals, height=0.68, color="#2a78d6", zorder=3)
    for yi, v in zip(y, vals):
        ax.text(v + 0.004, yi, f"{v:.2f}", va="center", fontsize=12.5, color="#222")
    ax.set_yticks(y); ax.set_yticklabels(labs, fontsize=15.5, color="#222")
    ax.invert_yaxis(); ax.set_xlim(0, 0.475); ax.set_ylim(len(vals) - 0.3, -0.85)
    ax.set_xticks(np.arange(0, 0.41, 0.1)); ax.tick_params(length=0, labelsize=14.5)
    ax.grid(axis="x", color="#e0e0e0", lw=1, zorder=0)
    for k in ("top", "right", "left"):
        ax.spines[k].set_visible(False)
    ax.set_xlabel("Mean absolute SHAP value (10,000 children)", fontsize=15.5, color="#777")
    save(fig, "fig07_shap_global_importance", 200)


# ================================================================ Figure 8
def fig8():
    plt.rcParams["font.family"] = SANS
    labs = ["Birth weight (kg): 2.4", "Wealth index: Quintile 1 (poorest)",
            "Age (months): 18", "Size at birth: Small", "Birth interval (months): 18",
            "Child's sex: Male", "Hemoglobin (g/dL): 9.6", "Household members: 7",
            "Place of delivery: Home", "Glass windows: No"]
    vals = [0.6636, 0.5004, 0.4158, 0.3893, 0.2393, 0.1849, 0.1129, 0.1026, 0.1018, 0.0842]
    fig = plt.figure(figsize=(9, 5.6))
    ax = fig.add_axes([0.388, 0.105, 0.592, 0.865])
    y = np.arange(len(vals))
    ax.barh(y, vals, height=0.65, color="#eb6834", zorder=3)
    for yi, v in zip(y, vals):
        ax.text(v + 0.012, yi - 0.02, f"+{v:.2f}", va="center", fontsize=13.5, color="#111")
    ax.set_yticks(y); ax.set_yticklabels(labs, fontsize=15.5, color="#111")
    ax.invert_yaxis(); ax.set_xlim(0, 0.78); ax.set_ylim(len(vals) - 0.5, -0.75)
    ax.set_xticks(np.arange(0, 0.71, 0.1)); ax.tick_params(length=0, labelsize=15)
    ax.grid(axis="x", color="#e0e0e0", lw=1, zorder=0)
    for k in ("top", "right", "left"):
        ax.spines[k].set_visible(False)
    ax.set_xlabel("Contribution to model output (log-odds scale)", fontsize=14.5, color="#777")
    save(fig, "fig08_shap_local_explanation", 200)


# ================================================================ Figure 9
def fig9():
    plt.rcParams["font.family"] = "DejaVu Sans"
    vals = np.array(json.load(open(os.path.join(HERE, "data_fig9.json"))))
    deps = ["Ancash", "Arequipa", "Callao", "Ica", "La Libertad", "Lambayeque", "Lima",
            "Moquegua", "Tumbes", "Tacna", "Piura", "Cajamarca", "Junin", "Cusco", "Ayacucho",
            "Apurimac", "Puno", "Pasco", "Huanuco", "Huancavelica", "Loreto", "Amazonas",
            "Madre de Dios", "San Martin", "Ucayali"]
    facs = ["Household poverty", "Low birth weight", "Altitude of residence", "Child's age",
            "Anemia (hemoglobin)", "Birth interval", "Breastfeeding duration",
            "Iron during pregnancy", "Age of household head", "Size at birth"]
    fig = plt.figure(figsize=(12.885, 7.17))
    ax = fig.add_axes([0.096, 0.275, 0.795, 0.662])
    im = ax.pcolormesh(vals, cmap="YlOrRd", vmin=0, vmax=1, edgecolors="white", linewidth=0.6)
    ax.set_xlim(0, 10); ax.set_ylim(25, 0)
    ax.set_xticks(np.arange(10) + 0.5)
    ax.set_xticklabels(facs, rotation=40, ha="right", rotation_mode="anchor", fontsize=12)
    ax.set_yticks(np.arange(25) + 0.5); ax.set_yticklabels(deps, fontsize=10.5)
    for sp in ax.spines.values():
        sp.set_visible(False)
    for yb in (11, 20):
        ax.axhline(yb, color="#1d3557", lw=2.5)
    cax = fig.add_axes([0.913, 0.355, 0.012, 0.48])
    cb = fig.colorbar(im, cax=cax)
    cb.set_label("Relative intensity of the factor", fontsize=10.5)
    cb.outline.set_visible(False)
    fig.text(0.5, 0.975, "Which factor weighs most in each department", ha="center",
             va="top", fontsize=17, fontweight="bold")
    fig.text(0.5, 0.018, "The more intense the color, the greater the weight of that factor in "
             "that department.  Bands separated by natural region: coast, highlands and rainforest.",
             ha="center", fontsize=11, color="#555")
    save(fig, "fig09_factor_weight_by_department", 200)


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig6, fig7, fig8, fig9):
        f()
    print("done")
