"""Cover letter for Nutrition in English (to submit) and Spanish (reference only), as .docx and .tex."""
import docx
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

DATE = {"en": "Lima, 13 November 2026", "es": "Lima, 13 de noviembre de 2026"}
T = {
"en": dict(
 heading="Cover Letter", salute="Dear Editor,",
 paras=[
  "We are pleased to submit our manuscript entitled \u201cMachine Learning Model for Predicting the Risk of Childhood Stunting in Peru\u201d for consideration as an original research article in Nutrition. The authors are Abel Is-Boset Guevara-Huasco, Zulin Pamela Vallejos-Cotrina, Ver\u00f3nica Lisseth Vergara-Rojas, Ferdinand Edgardo Pineda-Ancco and Nemias Saboya-Rios.",
  "The study develops and internally validates a model to predict stunting in 304,271 children under five, using the Peruvian Demographic and Family Health Survey (ENDES) 2007\u20132025 and 45 predictors from five domains: the child, the mother, the household and territory, water and sanitation, and housing. Six supervised algorithms were compared under stratified five-fold cross-validation with survey weights. LightGBM was selected, with an out-of-fold AUC-ROC of 0.829 (95% CI 0.827\u20130.832) and a sensitivity of 76.4%. SHAP values identified household poverty, birth weight and altitude as the leading predictors and showed how their weight differs across Peru\u2019s 25 departments.",
  "The model was implemented as a web-based decision-support application, which a panel of four health professionals rated favorably (median overall score of 9 out of 10). The code, the processed dataset and the trained model are openly available in Zenodo to support reproducibility.",
  "We believe the manuscript will interest the readers of Nutrition, which has published several machine learning studies on child undernutrition in Bangladesh, Egypt, India, the Philippines and sub-Saharan Africa. Our work extends this line of research to Latin America, where it remains scarce, and adds a territorial interpretation and a practical tool aimed at public health institutions.",
  "We confirm that this manuscript has not been published elsewhere and is not under consideration by any other journal. All authors have approved the manuscript and agree with its submission to Nutrition. The study was approved by the Ethics Committee of the School of Systems Engineering, Universidad Peruana Uni\u00f3n (No. CEI-UPEU-FIA-2026-24), and the authors declare no competing interests.",
  "Thank you for your time and consideration."],
 close="Sincerely,",
 sign=["Nemias Saboya-Rios, MSc", "Corresponding author",
       "School of Systems Engineering, Faculty of Engineering and Architecture",
       "Universidad Peruana Uni\u00f3n, Carretera Central Km 19.5, \u00d1a\u00f1a, Lurigancho-Chosica, Lima, Peru",
       "saboya@upeu.edu.pe \u00b7 ORCID 0000-0002-7166-2197"]),
"es": dict(
 heading="Carta de presentaci\u00f3n", salute="Estimado editor:",
 paras=[
  "Nos complace presentar nuestro manuscrito titulado \u201cMachine Learning Model for Predicting the Risk of Childhood Stunting in Peru\u201d (Modelo de machine learning para predecir el riesgo de desnutrici\u00f3n cr\u00f3nica infantil en el Per\u00fa) para su consideraci\u00f3n como art\u00edculo de investigaci\u00f3n original en Nutrition. Los autores son Abel Is-Boset Guevara-Huasco, Zulin Pamela Vallejos-Cotrina, Ver\u00f3nica Lisseth Vergara-Rojas, Ferdinand Edgardo Pineda-Ancco y Nemias Saboya-Rios.",
  "El estudio desarrolla y valida internamente un modelo para predecir la desnutrici\u00f3n cr\u00f3nica en 304,271 ni\u00f1os menores de cinco a\u00f1os, a partir de la Encuesta Demogr\u00e1fica y de Salud Familiar (ENDES) 2007\u20132025 y de 45 predictores de cinco dominios: el ni\u00f1o, la madre, el hogar y el territorio, el agua y el saneamiento, y la vivienda. Se compararon seis algoritmos supervisados mediante validaci\u00f3n cruzada estratificada de cinco pliegues con ponderaci\u00f3n de la encuesta. Se seleccion\u00f3 LightGBM, con un AUC-ROC fuera de pliegue de 0.829 (IC 95%: 0.827\u20130.832) y una sensibilidad del 76.4%. Los valores SHAP identificaron la pobreza del hogar, el peso al nacer y la altitud como los principales predictores y mostraron c\u00f3mo su peso var\u00eda entre los 25 departamentos del Per\u00fa.",
  "El modelo se implement\u00f3 en una aplicaci\u00f3n web de apoyo a la decisi\u00f3n, que un panel de cuatro profesionales de salud valor\u00f3 favorablemente (mediana de la valoraci\u00f3n global: 9 sobre 10). El c\u00f3digo, el conjunto de datos procesado y el modelo entrenado est\u00e1n disponibles en Zenodo para favorecer la reproducibilidad.",
  "Consideramos que el manuscrito interesar\u00e1 a los lectores de Nutrition, que ha publicado varios estudios de machine learning sobre desnutrici\u00f3n infantil en Bangladesh, Egipto, India, Filipinas y \u00c1frica subsahariana. Nuestro trabajo extiende esta l\u00ednea de investigaci\u00f3n a Am\u00e9rica Latina, donde a\u00fan es escasa, y aporta una interpretaci\u00f3n territorial y una herramienta pr\u00e1ctica dirigida a las instituciones de salud p\u00fablica.",
  "Confirmamos que este manuscrito no ha sido publicado en otro lugar y no est\u00e1 en evaluaci\u00f3n en ninguna otra revista. Todos los autores han aprobado el manuscrito y est\u00e1n de acuerdo con su env\u00edo a Nutrition. El estudio fue aprobado por el Comit\u00e9 de \u00c9tica de la Escuela Profesional de Ingenier\u00eda de Sistemas de la Universidad Peruana Uni\u00f3n (N.\u00b0 CEI-UPEU-FIA-2026-24), y los autores declaran no tener conflictos de intereses.",
  "Agradecemos su tiempo y consideraci\u00f3n."],
 close="Atentamente,",
 sign=["Mg. Nemias Saboya-Rios", "Autor de correspondencia",
       "Escuela Profesional de Ingenier\u00eda de Sistemas, Facultad de Ingenier\u00eda y Arquitectura",
       "Universidad Peruana Uni\u00f3n, Carretera Central Km 19.5, \u00d1a\u00f1a, Lurigancho-Chosica, Lima, Per\u00fa",
       "saboya@upeu.edu.pe \u00b7 ORCID 0000-0002-7166-2197"]),
}

def make_docx(lang, path):
    t = T[lang]; d = docx.Document()
    s = d.sections[0]; s.left_margin = s.right_margin = Cm(2.5); s.top_margin = s.bottom_margin = Cm(2.5)
    st = d.styles["Normal"]; st.font.name = "Times New Roman"; st.font.size = Pt(12)
    st.paragraph_format.space_after = Pt(8); st.paragraph_format.line_spacing = 1.15
    p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.RIGHT; p.add_run(DATE[lang])
    p = d.add_paragraph(); r = p.add_run(t["heading"]); r.bold = True; r.font.size = Pt(14)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    d.add_paragraph(t["salute"])
    for para in t["paras"]:
        p = d.add_paragraph(para); p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for name in ("Nutrition",):
            pass
    d.add_paragraph(t["close"])
    d.add_paragraph().add_run("\n\n")
    for i, line in enumerate(t["sign"]):
        p = d.add_paragraph(); p.paragraph_format.space_after = Pt(0)
        r = p.add_run(line); r.bold = (i == 0)
    d.save(path)

def tex_escape(s):
    return s.replace("%", r"\%").replace("&", r"\&").replace("#", r"\#")

def make_tex(lang, path):
    t = T[lang]
    body = "\n\n".join(tex_escape(x).replace("Nutrition", r"\emph{Nutrition}") for x in t["paras"])
    sign = r"\\".join(([r"\textbf{%s}" % tex_escape(t["sign"][0])] + [tex_escape(x) for x in t["sign"][1:]]))
    babel = "english"
    open(path, "w").write(rf"""\documentclass[11pt]{{article}}
\usepackage[utf8]{{inputenc}}\usepackage[T1]{{fontenc}}\usepackage{{mathptmx}}
\usepackage[{babel}]{{babel}}
\usepackage[a4paper,margin=2.2cm]{{geometry}}
\setlength{{\parindent}}{{0pt}}\setlength{{\parskip}}{{7pt}}\linespread{{1.05}}
\pagestyle{{empty}}
\begin{{document}}
\hfill {tex_escape(DATE[lang])}

\begin{{center}}\large\bfseries {t["heading"]}\end{{center}}

{t["salute"]}

{body}

{t["close"]}

\vspace{{1.2cm}}
{{\setlength{{\parskip}}{{0pt}}\small {sign}\par}}
\end{{document}}
""")

for lang, name in (("en", "Cover_Letter_EN"), ("es", "Carta_presentacion_ES_referencia")):
    make_docx(lang, name + ".docx"); make_tex(lang, name + ".tex")
print("ok")
