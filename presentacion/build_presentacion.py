"""Fill the XVIII Jornada Científica template with the content of the article."""
import copy, sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE, MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from PIL import Image

SRC, OUT, FIG = sys.argv[1], sys.argv[2], sys.argv[3]
p = Presentation(SRC)
NAVY, YELLOW, WHITE, GRAY, LIGHT = (RGBColor(0x00, 0x38, 0x65), RGBColor(0xF8, 0xA9, 0x00),
                                    RGBColor(0xFF, 0xFF, 0xFF), RGBColor(0x1E, 0x1E, 0x1E), RGBColor(0xE8, 0xEE, 0xF5))
FONT = "DM Sans"


def find(slide, path):
    shapes, sh = slide.shapes, None
    for sid in path:
        sh = next(s for s in shapes if s.shape_id == sid)
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            shapes = sh.shapes
    return sh


def setp(slide, path, pidx, texts):
    par = find(slide, path).text_frame.paragraphs[pidx]
    runs = par.runs
    assert len(texts) <= len(runs), (path, pidx, len(runs), texts)
    for r, t in zip(runs, texts + [""] * (len(runs) - len(texts))):
        r.text = t


def set_lines(slide, path, lines, size=None):
    """Replace a text box's content with one paragraph per line, cloning the first paragraph's format."""
    tf = find(slide, path).text_frame
    first = tf.paragraphs[0]
    for extra in tf.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)
    proto = copy.deepcopy(first._p)
    for i, line in enumerate(lines):
        par = first if i == 0 else None
        if par is None:
            newp = copy.deepcopy(proto)
            tf._txBody.append(newp)
            par = tf.paragraphs[-1]
        runs = par.runs
        runs[0].text = line
        par.alignment = PP_ALIGN.LEFT
        for r in runs[1:]:
            r.text = ""
        if size:
            runs[0].font.size = Pt(size)


def delete(slide, ids):
    for sh in list(slide.shapes):
        if sh.shape_id in ids:
            sh._element.getparent().remove(sh._element)


def pic_fit(slide, img, x, y, w, h):
    iw, ih = Image.open(img).size
    r = min(w / iw, h / ih)
    pw, ph = iw * r, ih * r
    return slide.shapes.add_picture(img, Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))


def textbox(slide, x, y, w, h, text, size=20, color=GRAY, bold=False, align=PP_ALIGN.LEFT, italic=False):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    par = tf.paragraphs[0]
    par.alignment = align
    r = par.add_run()
    r.text = text
    r.font.name = FONT; r.font.size = Pt(size); r.font.bold = bold; r.font.italic = italic
    r.font.color.rgb = color
    return tb


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


S = lambda n: p.slides[n - 1]


def content_slide(n, title, subtitle, title_size=60):
    """Slides built on the 'Introducción' layout (title 33, subtitle 32, boxes 2/5/8/11, texts 34/35)."""
    s = S(n)
    setp(s, (33,), 0, [title])
    find(s, (33,)).text_frame.paragraphs[0].runs[0].font.size = Pt(title_size)
    setp(s, (32,), 0, [subtitle])
    sub = find(s, (32,))
    sub.text_frame.paragraphs[0].runs[0].font.size = Pt(24)
    sub.left, sub.width = Inches(2.5), Inches(15.0)
    sub.top = Inches(3.35)
    return s


def boxes(s, b1, b2, n1="01", n2="02"):
    setp(s, (5, 7), 0, [n1]); setp(s, (11, 13), 0, [n2])
    for sid, txt in ((34, b1), (35, b2)):
        tb = find(s, (sid,))
        tb.top, tb.height = Inches(6.55), Inches(2.5)
        setp(s, (sid,), 0, [txt])
        tb.text_frame.paragraphs[0].runs[0].font.size = Pt(21)
        tb.text_frame.paragraphs[0].alignment = PP_ALIGN.LEFT


def strip_boxes(s):
    delete(s, {2, 5, 8, 11, 34, 35})


# ================================================================== 1 Carátula
s = S(1)
t = find(s, (12,))
t.top, t.height, t.width = Inches(3.55), Inches(4.6), Inches(10.6)
set_lines(s, (12,), ["MODELO DE MACHINE LEARNING PARA PREDECIR EL RIESGO DE DESNUTRICIÓN CRÓNICA INFANTIL EN EL PERÚ"], size=40)
setp(s, (11,), 0, ["ENDES · LightGBM · SHAP"])
find(s, (11,)).text_frame.paragraphs[0].runs[0].font.size = Pt(22)
textbox(s, 1.16, 9.45, 9.5, 0.9,
        "Guevara Huasco, A. · Vergara Rojas, V. · Vallejos Cotrina, Z. · Pineda Ancco, F. · Saboya Rios, N.",
        size=16, color=NAVY)
notes(s, "Buenos días. Presentamos nuestro artículo: un modelo de machine learning que predice el riesgo de desnutrición "
         "crónica en niños menores de cinco años en el Perú, explica qué factores pesan más en cada departamento y se "
         "implementó en una herramienta web.")

# ================================================================== 2 Equipo
s = S(2)
team = [((14,), "Abel Is-Boset Guevara Huasco", 16, "AG", 17),
        ((29,), "Verónica Lisseth Vergara Rojas", 20, "VV", 21),
        ((30,), "Zulin Pamela Vallejos Cotrina", 24, "ZV", 25)]
for path, name, photo, ini, ring in team:
    tf = find(s, path).text_frame
    tf.paragraphs[0].runs[0].text = name
    for r in tf.paragraphs[0].runs[1:]:
        r.text = ""
    tf.paragraphs[1].runs[0].text = "5.° año – Ciclo X"
    for r in tf.paragraphs[1].runs[1:]:
        r.text = ""
    ph = find(s, (photo,))
    x, y, w, h = ph.left, ph.top, ph.width, ph.height
    ph._element.getparent().remove(ph._element)
    rg = find(s, (ring,))
    rg._element.getparent().remove(rg._element)
    c = s.shapes.add_shape(MSO_SHAPE.OVAL, x, y, w, h)
    c.fill.solid(); c.fill.fore_color.rgb = NAVY; c.line.fill.background()
    tf2 = c.text_frame
    tf2.paragraphs[0].alignment = PP_ALIGN.CENTER
    r = tf2.paragraphs[0].add_run(); r.text = ini
    r.font.name = FONT; r.font.size = Pt(54); r.font.bold = True; r.font.color.rgb = WHITE
    tf2.vertical_anchor = MSO_ANCHOR.MIDDLE
textbox(s, 1.12, 9.35, 13.0, 0.6, "Coautor: Ferdinand Pineda Ancco · Asesor: Mg. Nemias Saboya Rios",
        size=20, color=NAVY)
notes(s, "Somos estudiantes de quinto año de Ingeniería de Sistemas. El artículo tiene como coautor a Ferdinand Pineda "
         "Ancco y como asesor al Mg. Nemias Saboya Rios.")

# ================================================================== 3 Índice
s = S(3)
setp(s, (6,), 0, ["Introducción y trabajos relacionados"])
setp(s, (22,), 0, ["Metodología y resultados"])
setp(s, (23,), 0, ["Conclusiones y sometimiento del artículo"])
notes(s, "La presentación tiene tres partes: el problema y lo que ya se ha hecho; cómo construimos el modelo y qué "
         "encontramos; y las conclusiones junto con el envío del artículo a la revista Nutrition.")

# ================================================================== 4 Introducción
s = content_slide(4, "INTRODUCCIÓN", "En el Perú, la desnutrición crónica infantil se estancó en torno al 12% desde 2018", 72)
boxes(s,
      "Problema: la prevalencia se mantiene entre 11.3% y 12.4% y llega al 21.5% en zonas rurales. Los recursos no alcanzan para llegar a todos los hogares.",
      "Objetivo: desarrollar un modelo de machine learning que prediga el riesgo, analice los factores por departamento y se implemente en una herramienta.")
notes(s, "La desnutrición crónica, talla baja para la edad, afecta el desarrollo físico y cognitivo. En el Perú bajó con "
         "fuerza hasta 2017, pero desde 2018 se mantiene alrededor del 12%, con una brecha rural persistente. Por eso "
         "planteamos priorizar a los niños y territorios con mayor riesgo.")

# ================================================================== 5 Contexto (figura 4)
s = content_slide(5, "CONTEXTO", "Prevalencia ponderada de desnutrición crónica en menores de 5 años, ENDES 2007–2025", 72)
strip_boxes(s)
pic_fit(s, f"{FIG}/f4.png", 2.0, 4.35, 15.8, 5.95)
notes(s, "Con el factor de expansión del INEI, la prevalencia nacional bajó de 29.2% en 2007 a 13.0% en 2017 y desde "
         "entonces está entre 11.3% y 12.4%. En 2025 fue 21.5% en la zona rural y 7.9% en la urbana.")

# ================================================================== 6 Trabajos relacionados
s = content_slide(6, "TRABAJOS RELACIONADOS", "Machine learning aplicado a la desnutrición infantil con encuestas DHS", 52)
boxes(s,
      "Antecedentes: ensambles de árboles en Bangladesh y Etiopía; red neuronal con AUC-ROC de 0.84 en Ruanda; en Nutrition, estudios en África, Egipto, India y Filipinas.",
      "Brechas: exactitud combinada de 68.9%, una sola ronda de encuesta, métricas centradas en la exactitud y sin herramienta. En el Perú, sin explicación territorial.")
notes(s, "Varios estudios con datos DHS encontraron que los ensambles de árboles predicen mejor. Pero un metaanálisis "
         "reportó una exactitud combinada de 68.9% con alta heterogeneidad; la mayoría usa una sola ronda, reporta solo "
         "exactitud y no ofrece una herramienta. En el Perú no se había aplicado un enfoque predictivo con explicación "
         "territorial a toda la serie de la ENDES.")

# ================================================================== 7 Metodología
s = S(7)
setp(s, (7, 9), 0, ["Comprensión"])
setp(s, (10, 12), 0, ["Preparación"])
setp(s, (16, 18), 0, ["Modelado"])
setp(s, (13, 15), 0, ["Evaluación y despliegue"])
textbox(s, 2.12, 9.15, 13.5, 1.0,
        "Marco CRISP-DM · ENDES 2007–2025 · 189 columnas → 45 predictores · 6 algoritmos · validación cruzada estratificada de 5 pliegues",
        size=19, color=NAVY)
notes(s, "Seguimos el marco CRISP-DM. Integramos cinco módulos de la ENDES; armonizamos códigos y seleccionamos variables en "
         "cuatro etapas, de 189 columnas a 45 predictores; comparamos seis algoritmos con validación cruzada estratificada "
         "de cinco pliegues, pesos de clase y el factor de expansión; evaluamos con bootstrap y SHAP, y desplegamos una "
         "aplicación web.")

# ================================================================== 8 Datos y variables
s = content_slide(8, "DATOS Y VARIABLES", "ENDES 2007–2025 (INEI): 304,271 niños menores de 5 años; 15.8% con desnutrición crónica", 52)
boxes(s,
      "Variable objetivo: talla para la edad < −2 DE (OMS). Se excluyeron el peso, la talla y lo registrado después de la medición para evitar fuga de información.",
      "45 predictores en 5 dominios: niño (7), madre y embarazo (11), hogar y territorio (8), agua y saneamiento (10) y vivienda (9).")
notes(s, "La variable objetivo sigue el estándar de la OMS. Para no dar al modelo la respuesta, excluimos la talla, el peso "
         "y todo lo registrado después de la medición. Los 45 predictores cubren las causas inmediatas, subyacentes y "
         "básicas de la desnutrición.")

# ================================================================== 9 Resultados (portada)
s = S(9)
tb = find(s, (11,))
tb.width, tb.height = Inches(7.4), Inches(3.4)
set_lines(s, (11,), ["• LightGBM: AUC-ROC de 0.83",
                     "• Detecta el 80.5% de los casos con el umbral de 0.45",
                     "• Factores clave: pobreza, peso al nacer y altitud",
                     "• Valoración de expertos: 9 de 10"], size=22)
notes(s, "En resumen: LightGBM fue el mejor modelo, detecta cuatro de cada cinco casos con el umbral de triaje, los "
         "factores principales son la pobreza, el peso al nacer y la altitud, y los expertos valoraron la herramienta "
         "con 9 de 10.")

# ================================================================== 10 Comparación de modelos
s = content_slide(10, "COMPARACIÓN DE MODELOS", "Media de 5 pliegues de validación cruzada, umbral de 0.5", 52)
strip_boxes(s)
rows = [["Modelo", "AUC-ROC", "AUC-PR", "Sensibilidad", "Precisión", "Especificidad", "F1"],
        ["LightGBM", "0.830", "0.499", "76.4%", "36.4%", "74.3%", "49.3%"],
        ["CatBoost", "0.828", "0.507", "29.1%", "61.0%", "96.4%", "39.4%"],
        ["Red neuronal", "0.823", "0.487", "24.5%", "61.3%", "97.0%", "35.0%"],
        ["XGBoost", "0.794", "0.425", "75.9%", "32.4%", "69.5%", "45.4%"],
        ["Regresión logística", "0.793", "0.417", "71.4%", "33.8%", "73.0%", "45.9%"],
        ["Árbol de decisión", "0.780", "0.391", "71.7%", "32.5%", "71.3%", "44.8%"]]
tbl = s.shapes.add_table(7, 7, Inches(2.0), Inches(4.35), Inches(15.8), Inches(5.6)).table
for j, w in enumerate([3.8, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]):
    tbl.columns[j].width = Inches(w)
for i, row in enumerate(rows):
    tbl.rows[i].height = Inches(0.8)
    for j, val in enumerate(row):
        c = tbl.cell(i, j); c.text = val; c.vertical_anchor = MSO_ANCHOR.MIDDLE
        par = c.text_frame.paragraphs[0]; par.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.CENTER
        r = par.runs[0]; r.font.name = FONT; r.font.size = Pt(17 if i == 0 else 20); r.font.bold = i <= 1
        c.fill.solid()
        if i == 0:
            c.fill.fore_color.rgb = NAVY; r.font.color.rgb = WHITE
        elif i == 1:
            c.fill.fore_color.rgb = YELLOW; r.font.color.rgb = NAVY
        else:
            c.fill.fore_color.rgb = LIGHT if i % 2 == 0 else WHITE; r.font.color.rgb = GRAY
notes(s, "LightGBM tuvo el mayor AUC-ROC, la mayor sensibilidad y el mayor F1. CatBoost y la red neuronal tienen alta "
         "precisión, pero detectan menos del 30% de los casos, porque marcan muy pocos niños. La prueba de DeLong "
         "confirmó la superioridad de LightGBM sobre XGBoost y la regresión logística.")

# ================================================================== 11 Desempeño de LightGBM
s = content_slide(11, "DESEMPEÑO DE LIGHTGBM", "1,000 réplicas bootstrap sobre las probabilidades fuera de pliegue", 52)
boxes(s,
      "Umbral 0.5: AUC-ROC 0.829 (IC 95%: 0.827–0.832), sensibilidad 76.4%, precisión 36.4% y F1 49.3%.",
      "Umbral 0.45 (triaje): detecta el 80.5% de los casos con una precisión de 34.0%. Se prioriza no dejar pasar a un niño en riesgo.")
notes(s, "Con bootstrap, el AUC-ROC fue 0.829. Una precisión de 36% significa que uno de cada tres niños marcados tiene "
         "desnutrición crónica. Para triaje es aceptable: un falso positivo cuesta una evaluación adicional, mientras que "
         "un falso negativo deja a un niño sin atención. Por eso la aplicación usa el umbral de 0.45.")

# ================================================================== 12 SHAP global
s = content_slide(12, "FACTORES ASOCIADOS", "Importancia global con valores SHAP (10,000 niños)", 52)
strip_boxes(s)
pic_fit(s, f"{FIG}/f7.png", 2.0, 4.2, 15.8, 6.15)
notes(s, "La importancia se concentra en pocos factores: la pobreza del hogar y el bajo peso al nacer, ambos con 0.41, "
         "seguidos de la altitud y el tamaño al nacer. Las diez primeras variables suman el 68.5% del total. Son "
         "asociaciones aprendidas de la encuesta, no efectos causales.")

# ================================================================== 13 Por departamento
s = content_slide(13, "FACTORES POR DEPARTAMENTO", "Peso relativo de los 10 factores principales (0 = menor; 1 = mayor)", 52)
strip_boxes(s)
pic_fit(s, f"{FIG}/f9.png", 2.0, 4.2, 15.8, 6.15)
notes(s, "El peso de cada factor cambia por departamento. En Puno destacan la altitud, la pobreza y el bajo peso al nacer; "
         "en Huancavelica, el bajo peso al nacer, el intervalo entre partos y la edad del jefe de hogar. Esto sugiere "
         "priorizar según el perfil de cada territorio y no solo según la prevalencia.")

# ================================================================== 14 Aplicación web
s = content_slide(14, "APLICACIÓN WEB", "Streamlit, tres capas · stunting-risk-peru.streamlit.app", 52)
strip_boxes(s)
pic_fit(s, f"{FIG}/f10.png", 1.9, 4.2, 7.9, 6.0)
pic_fit(s, f"{FIG}/f13.png", 10.1, 4.2, 7.9, 6.0)
notes(s, "La aplicación permite evaluar a un niño y explicar su puntaje, evaluar a un grupo desde un archivo y ver el mapa "
         "de riesgo por departamento. En 300 niños de la ENDES 2025 reconoció las 45 columnas y marcó 100 como prioridad "
         "alta.")

# ================================================================== 15 Evaluación por expertos
s = content_slide(15, "EVALUACIÓN POR EXPERTOS", "4 especialistas (3 nutricionistas y 1 enfermero) · instrumento basado en TAM2", 52)
boxes(s,
      "Todos los constructos alcanzaron una mediana de 4 o más sobre 5, y la valoración global tuvo una mediana de 9 sobre 10.",
      "Menor acuerdo (75%): confianza en el riesgo y disponibilidad de datos. Sugirieron datos más actuales y extender a sobrepeso y micronutrientes.")
notes(s, "Con la aprobación del Comité de Ética de la Escuela, cuatro especialistas evaluaron la aplicación con 19 ítems "
         "Likert, una valoración global y cuatro preguntas abiertas. Ninguno objetó los factores mostrados.")

# ================================================================== 16 Conclusiones
s = S(16)
find(s, (10,)).text_frame.paragraphs[0].runs[0].font.size = Pt(78)
tb = find(s, (11,))
tb.width, tb.height = Inches(7.4), Inches(4.4)
set_lines(s, (11,), ["• LightGBM logró el mejor equilibrio entre discriminación y detección de casos.",
                     "• Pobreza, peso y tamaño al nacer y altitud fueron los factores más asociados al riesgo.",
                     "• El peso de cada factor varía por departamento.",
                     "• La herramienta apoya la focalización y el triaje, no el diagnóstico."], size=20)
notes(s, "Como trabajo futuro: validar el modelo por periodos, corregir la escala del índice de riqueza entre años, "
         "incorporar datos locales de establecimientos de salud y extender el enfoque al sobrepeso y a los micronutrientes.")

# ================================================================== 17 Sometimiento
s = S(17)
tb = find(s, (11,))
tb.top, tb.width, tb.height = Inches(5.4), Inches(8.0), Inches(4.2)
set_lines(s, (11,), ["Revista: Nutrition (Elsevier), ISSN 0899-9007",
                     "Tipo: artículo de investigación original",
                     "Título: Machine Learning Model for Predicting the Risk of Childhood Stunting in Peru",
                     "Fecha de envío: 13 de noviembre de 2026",
                     "Estado: enviado"], size=20)
notes(s, "El artículo se envió a la revista Nutrition de Elsevier como investigación original. La evidencia del envío "
         "está en los anexos.")

# ================================================================== 18 Referencias
s = S(18)
tb = find(s, (7,))
tb.top, tb.height, tb.width = Inches(4.4), Inches(5.4), Inches(10.0)
set_lines(s, (7,), [
    "Black RE, Victora CG, Walker SP, et al. Maternal and child undernutrition and overweight in low-income and middle-income countries. Lancet. 2013;382:427–51.",
    "Ke G, Meng Q, Finley T, et al. LightGBM: a highly efficient gradient boosting decision tree. NeurIPS. 2017;30:3146–54.",
    "Lundberg SM, Lee S-I. A unified approach to interpreting model predictions. NeurIPS. 2017;30.",
    "Rao B, Rashid M, Hasan MG, Thunga G. Machine learning in predicting child malnutrition: a meta-analysis of DHS data. Int J Environ Res Public Health. 2025;22:449.",
    "Venkatesh V, Davis FD. A theoretical extension of the technology acceptance model. Manage Sci. 2000;46:186–204."], size=16)
notes(s, "Estas son las referencias principales. La lista completa está en el artículo.")

p.save(OUT)
print("saved", OUT)
