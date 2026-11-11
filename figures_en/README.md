# Figures in English

| File | Figure |
|---|---|
| fig01_crisp_dm_workflow | Fig. 1 – CRISP-DM methodological workflow |
| fig02_endes_integration | Fig. 2 – Relational integration of ENDES modules |
| fig03_architecture | Fig. 3 – Three-layer architecture |
| fig04_prevalence_trend | Fig. 4 – Weighted stunting prevalence 2007–2025 |
| fig05_roc_curves | Fig. 5 – ROC curves (fifth fold) |
| fig06_confusion_matrix | Fig. 6 – LightGBM confusion matrix |
| fig07_shap_global_importance | Fig. 7 – Global SHAP importance |
| fig08_shap_local_explanation | Fig. 8 – Local explanation, high-risk profile |
| fig09_factor_weight_by_department | Fig. 9 – Factor weight by department |
| fig10_application_screens | Fig. 10 – Application screens (panel titles translated) |

Each PNG has the same pixel size as the original, so it can replace the Spanish
file in LaTeX without changing `\includegraphics` options. Figs. 1–4 and 6–9 also
have a vector PDF version.

- `make_figures.py` – redraws Figs. 1–4 and 6–9 (data in `data_fig4.json`, `data_fig9.json`, recovered from the original images).
- `edit_raster_figures.py` – translates the text of Figs. 5 and 10 over the original images (`src_fig05_es.png`, `src_fig10_es.png`).
- `replace_in_pdf.py input.pdf output.pdf` – swaps the figures inside the compiled article.
- `main-en_figures-en.pdf` – the article with all figures in English.
