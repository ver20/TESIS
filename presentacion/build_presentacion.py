import copy, sys
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from PIL import Image

SRC, OUT, FIG = sys.argv[1], sys.argv[2], sys.argv[3]
p = Presentation(SRC)
E = 914400


def find(slide, path):
    shapes = slide.shapes
    sh = None
    for sid in path:
        sh = next(s for s in shapes if s.shape_id == sid)
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            shapes = sh.shapes
    return sh


def setp(slide, path, pidx, texts):
    """Write texts into the existing runs of a paragraph (keeps formatting)."""
    par = find(slide, path).text_frame.paragraphs[pidx]
    runs = par.runs
    assert len(texts) <= len(runs), (path, pidx, len(runs), texts)
    for r, t in zip(runs, texts + [""] * (len(runs) - len(texts))):
        r.text = t


def drop_par(slide, path, pidx):
    par = find(slide, path).text_frame.paragraphs[pidx]
    par._p.getparent().remove(par._p)


def delete(slide, ids):
    for sh in list(slide.shapes):
        if sh.shape_id in ids:
            sh._element.getparent().remove(sh._element)


def pic_fit(slide, img, x, y, w, h):
    iw, ih = Image.open(img).size
    r = min(w / iw, h / ih)
    pw, ph = iw * r, ih * r
    pic = slide.shapes.add_picture(img, Inches(x + (w - pw) / 2), Inches(y + (h - ph) / 2), Inches(pw), Inches(ph))
    return pic


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


S = lambda n: p.slides[n - 1]
LBL = (2, 4)
TTL = (5, 7)

# ---------------------------------------------------------------- 1 Portada
s = S(1)
setp(s, (4, 6), 0, ["Jornada de investigación"])
setp(s, (8,), 0, ["Modelo de machine learning para predecir el riesgo de desnutrición crónica infantil en el Perú"])
find(s, (8,)).text_frame.paragraphs[0].runs[0].font.size = Pt(46)
find(s, (9,)).top = Inches(6.45)
find(s, (10,)).top = Inches(8.2)
setp(s, (9,), 0, ["Datos de la ENDES 2007–2025, LightGBM y SHAP para priorizar a quién llegar primero"])
setp(s, (10,), 0, ["Abel Guevara Huasco · Verónica Vergara Rojas · Pamela Vallejos Cotrina"])
setp(s, (10,), 1, ["Ferdinand Pineda Ancco · Asesor: Mg. Nemias Saboya Rios"])
setp(s, (10,), 2, ["Universidad Peruana Unión — EP Ingeniería de Sistemas"])
setp(s, (10,), 3, ["Noviembre de 2026"])
notes(s, "Buenos días. Presentamos nuestro artículo: un modelo de machine learning que estima el riesgo de "
         "desnutrición crónica en niños menores de cinco años en el Perú, explica qué factores pesan más en cada "
         "departamento y se implementó en una herramienta web para priorizar a quién llegar primero.")

# ---------------------------------------------------------------- 2 Problema
s = S(2)
setp(s, LBL, 0, ["1 · El problema"])
setp(s, TTL, 0, ["Entre 2007 y 2025, 1 de cada 6 niños tuvo desnutrición crónica"])
setp(s, (11,), 0, ["Hoy afecta al 12% y no está repartida por igual. Se concentra:"])
notes(s, "La desnutrición crónica es talla baja para la edad. En las 19 rondas de la ENDES afectó en promedio "
         "a uno de cada seis niños menores de cinco años (16.2%). Hoy está en 12% y se concentra en la sierra "
         "(26.2%), las zonas rurales (30.7%) y los hogares más pobres.")

# ---------------------------------------------------------------- 3 Pregunta y objetivo
s = S(3)
setp(s, LBL, 0, ["1 · El problema"])
setp(s, (15,), 0, ["Hoy ", "esa decisión se toma con criterios generales del territorio (por ejemplo, toda una zona)."])
setp(s, (16,), 0, ["Objetivo: ", "desarrollar un modelo que prediga el riesgo, explique sus factores por departamento y se use para priorizar."])
notes(s, "El personal de salud sabe diagnosticar; el problema es que no puede llegar a todos a la vez. Hoy se "
         "prioriza por zonas completas. Nuestro objetivo fue desarrollar un modelo de machine learning que prediga "
         "el riesgo, explique los factores predominantes por departamento y se implemente en una herramienta.")

# ---------------------------------------------------------------- 4 Datos
s = S(4)
setp(s, LBL, 0, ["2 · Métodos"])
setp(s, TTL, 0, ["¿Con qué datos trabajamos?"])
setp(s, (26,), 0, ["seleccionados entre 189 columnas en cuatro etapas"])
notes(s, "Usamos los microdatos públicos de la ENDES del INEI, de 2007 a 2025: 304,271 niños con antropometría "
         "válida, de los cuales el 15.8% tenía desnutrición crónica. Integramos cinco módulos de la encuesta con "
         "las llaves HHID y CASEID. La definición es la de la OMS: talla para la edad menor a −2 desviaciones estándar.")

# ---------------------------------------------------------------- 5 Tendencia
s = S(5)
setp(s, LBL, 0, ["2 · Métodos"])
setp(s, TTL, 0, ["La desnutrición crónica se estancó en torno al 12%"])
setp(s, (8, 10), 0, ["Prevalencia ponderada en menores de 5 años, ENDES 2007–2025: nacional, urbana y rural"])
setp(s, (23, 25), 0, ["29.2%"])
setp(s, (26, 28), 0, ["en 2007"])
setp(s, (26, 28), 1, ["Casi 1 de cada 3 niños tenía talla baja para su edad."])
setp(s, (31, 33), 0, ["~12%"])
setp(s, (34, 36), 0, ["desde 2018 (12.0% en 2025)"])
setp(s, (34, 36), 1, ["Estancada entre 11.3% y 12.4%: ocho años sin bajar."])
setp(s, (39, 41), 0, ["21.5%"])
setp(s, (42, 44), 0, ["en la zona rural (2025)"])
setp(s, (42, 44), 1, ["Casi el triple que en la zona urbana (7.9%)."])
delete(s, {11, 13, 16, 18, 45})
pic_fit(s, f"{FIG}/f4.png", 0.75, 3.45, 12.2, 6.6)
notes(s, "Con el factor de expansión del INEI, la prevalencia nacional bajó de 29.2% en 2007 a 13.0% en 2017, "
         "pero desde 2018 se mantiene entre 11.3% y 12.4%. La brecha persiste: en 2025 fue 21.5% en la zona rural "
         "y 7.9% en la urbana. Ese estancamiento justifica dirigir los recursos a quienes tienen más riesgo.")

# ---------------------------------------------------------------- 6 CRISP-DM (copia de la diapositiva del mapa de calor)
s = S(6)
setp(s, LBL, 0, ["2 · Métodos"])
setp(s, TTL, 0, ["Seguimos las fases de CRISP-DM"])
setp(s, (12, 14), 0, ["189 columnas → 74 factores significativos → 45 predictores."])
setp(s, (17, 19), 0, ["6 algoritmos, validación cruzada estratificada de 5 pliegues."])
setp(s, (22, 24), 0, ["Pesos de clase y factor de expansión del INEI."])
delete(s, {8})
pic_fit(s, f"{FIG}/f1.png", 0.75, 2.95, 13.35, 7.35)
notes(s, "Seguimos el marco CRISP-DM. Seleccionamos variables en cuatro etapas: ausentes, correlación y VIF, "
         "pruebas chi-cuadrado y Kruskal-Wallis, e importancia en gradient boosting, hasta llegar a 45 predictores. "
         "Comparamos regresión logística, árbol de decisión, XGBoost, CatBoost, red neuronal y LightGBM, con pesos "
         "de clase para el desbalance y el factor de expansión para que los resultados representen al país.")

# ---------------------------------------------------------------- 7 Los 45 predictores
s = S(7)
setp(s, LBL, 0, ["2 · Métodos"])
setp(s, TTL, 0, ["Los 45 predictores, en 5 dimensiones"])
setp(s, (12, 14), 0, ["7"])
setp(s, (16,), 0, ["Edad, sexo, peso y tamaño al nacer, hemoglobina, intervalo entre partos"])
setp(s, (21, 23), 0, ["11"])
setp(s, (24,), 0, ["Madre, embarazo y lactancia"])
setp(s, (25,), 0, ["Educación de la madre, controles prenatales, hierro, parto, lactancia"])
setp(s, (30, 32), 0, ["8"])
setp(s, (33,), 0, ["Hogar y territorio"])
setp(s, (34,), 0, ["Índice de riqueza, zona urbana o rural, altitud, tamaño del hogar"])
setp(s, (39, 41), 0, ["10"])
setp(s, (42,), 0, ["Agua y saneamiento"])
setp(s, (48, 50), 0, ["9"])
setp(s, (51,), 0, ["Vivienda"])
setp(s, (52,), 0, ["Habitaciones, alumbrado, humo en la cocina, combustible, ventanas"])
setp(s, (55, 57), 0, ["✔  Casi todo se obtiene por entrevista o carné de control. ",
                      "Solo la hemoglobina requiere laboratorio (tamizaje de anemia)."])
notes(s, "Los 45 predictores se agrupan en cinco dominios: 7 del niño, 11 de la madre con su embarazo y lactancia, "
         "8 del hogar y el territorio, 10 de agua y saneamiento y 9 de la vivienda. Corresponden a las causas "
         "inmediatas, subyacentes y básicas de la desnutrición. La lista completa está en la Tabla suplementaria S1.")

# ---------------------------------------------------------------- 8 Sin peso ni talla
s = S(8)
setp(s, LBL, 0, ["2 · Métodos"])
setp(s, TTL, 0, ["¿Por qué no se usan el peso ni la talla actuales?"])
setp(s, (22,), 1, ["13 casos menos por cada 10 000 niños con desnutrición"])
notes(s, "Para evitar la fuga de información excluimos la talla, el peso y todo lo registrado después de la "
         "medición: son el diagnóstico mismo. La hemoglobina es el único dato que requiere una punción; al quitarla, "
         "el AUC-ROC baja de 0.8294 a 0.8281 y la sensibilidad de 76.43% a 76.30%.")

# ---------------------------------------------------------------- 9 Comparación de algoritmos (copia de referencias)
s = S(9)
setp(s, LBL, 0, ["3 · Resultados"])
setp(s, TTL, 0, ["LightGBM fue el mejor de 6 algoritmos"])
delete(s, {8, 10, 12, 15, 17, 19, 22, 24, 26, 29, 31, 33, 36, 38, 40})
rows = [
    ["Modelo", "AUC-ROC", "AUC-PR", "Sensibilidad", "Precisión", "Especificidad", "F1"],
    ["LightGBM", "0.830", "0.499", "76.4%", "36.4%", "74.3%", "49.3%"],
    ["CatBoost", "0.828", "0.507", "29.1%", "61.0%", "96.4%", "39.4%"],
    ["Red neuronal", "0.823", "0.487", "24.5%", "61.3%", "97.0%", "35.0%"],
    ["XGBoost", "0.794", "0.425", "75.9%", "32.4%", "69.5%", "45.4%"],
    ["Regresión logística", "0.793", "0.417", "71.4%", "33.8%", "73.0%", "45.9%"],
    ["Árbol de decisión", "0.780", "0.391", "71.7%", "32.5%", "71.3%", "44.8%"],
]
DARK, TEAL, LIGHT, ROWALT, GRAY = RGBColor(0x17, 0x40, 0x4A), RGBColor(0x1F, 0x8A, 0x8A), RGBColor(0xE6, 0xF4, 0xF1), RGBColor(0xF6, 0xF8, 0xF8), RGBColor(0x5B, 0x6E, 0x74)
tbl = s.shapes.add_table(len(rows), 7, Inches(0.9), Inches(2.95), Inches(18.2), Inches(0.9 * len(rows))).table
widths = [3.8, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4]
for j, w in enumerate(widths):
    tbl.columns[j].width = Inches(w)
for i, row in enumerate(rows):
    tbl.rows[i].height = Inches(0.9)
    for j, val in enumerate(row):
        c = tbl.cell(i, j)
        c.text = val
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        c.margin_left = c.margin_right = Inches(0.15)
        para = c.text_frame.paragraphs[0]
        para.alignment = PP_ALIGN.LEFT if j == 0 else PP_ALIGN.CENTER
        r = para.runs[0]
        r.font.name = "Calibri (MS)"
        r.font.size = Pt(22)
        r.font.bold = (i == 0 or i == 1)
        c.fill.solid()
        if i == 0:
            c.fill.fore_color.rgb = DARK
            r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        elif i == 1:
            c.fill.fore_color.rgb = LIGHT
            r.font.color.rgb = TEAL
        else:
            c.fill.fore_color.rgb = ROWALT if i % 2 == 0 else RGBColor(0xFF, 0xFF, 0xFF)
            r.font.color.rgb = DARK
tb = s.shapes.add_textbox(Inches(0.9), Inches(9.45), Inches(18.2), Inches(0.8))
tb.text_frame.word_wrap = True
r = tb.text_frame.paragraphs[0].add_run()
r.text = ("Media de los 5 pliegues con el umbral de 0.5. CatBoost y la red neuronal tienen alta precisión, "
          "pero detectan menos del 30% de los casos.")
r.font.name = "Calibri (MS)"; r.font.size = Pt(20); r.font.color.rgb = GRAY
notes(s, "En los cinco pliegues, LightGBM tuvo el mayor AUC-ROC (0.83), la mayor sensibilidad (76.4%) y el mayor F1 "
         "(49.3%). CatBoost tuvo un AUC-PR algo mayor, pero detectó solo el 29.1% de los casos, y la red neuronal, "
         "entrenada sin pesos, el 24.5%. La prueba de DeLong confirmó la superioridad de LightGBM sobre XGBoost "
         "y la regresión logística.")

# ---------------------------------------------------------------- 10-12 Resultados
setp(S(10), LBL, 0, ["3 · Resultados"])
notes(S(10), "Con 1,000 réplicas bootstrap, LightGBM alcanzó un AUC-ROC de 0.829 (IC 95%: 0.827–0.832): entre un niño "
             "con desnutrición y otro sin ella, da más riesgo al correcto 83 de cada 100 veces. Detecta al 76% de los "
             "casos y, de cada 100 niños que marca, 36 tienen desnutrición crónica.")
setp(S(11), LBL, 0, ["3 · Resultados"])
setp(S(11), (26,), 0, ["Cobertura 8", "0%", " · ", "Acierto", " 34% con el umbral de 0.45."])
setp(S(12), LBL, 0, ["3 · Resultados"])
setp(S(12), (22,), 0, ["✔  Resultados comprobados con 1,000 réplicas bootstrap: el margen de error es de alrededor de medio punto."])
notes(S(12), "El umbral se puede ajustar. Con 0.45, el que usa la aplicación, la sensibilidad sube a 80.5% y la "
             "precisión baja a 34.0%. En triaje lo preferimos: un falso positivo cuesta una evaluación adicional, "
             "mientras que un falso negativo deja a un niño en riesgo sin atención.")

# ---------------------------------------------------------------- 13 SHAP global (copia del mapa de calor)
s = S(13)
setp(s, LBL, 0, ["3 · Resultados"])
setp(s, TTL, 0, ["Los factores que más pesan en el riesgo"])
setp(s, (12, 14), 0, ["Pobreza del hogar y bajo peso al nacer: 0.41 cada uno."])
setp(s, (17, 19), 0, ["Les siguen la altitud (0.26) y el tamaño al nacer (0.25)."])
setp(s, (22, 24), 0, ["Las 10 primeras variables suman el 68.5% del total."])
delete(s, {8})
pic_fit(s, f"{FIG}/f7.png", 0.75, 2.95, 13.35, 7.35)
notes(s, "Con valores SHAP, calculados sobre 10,000 niños, la importancia se concentra en pocos factores: la pobreza "
         "del hogar, el peso al nacer, la altitud y el tamaño al nacer. Coinciden con el marco de causas de la "
         "desnutrición materno-infantil. Son asociaciones aprendidas de la encuesta, no efectos causales.")

# ---------------------------------------------------------------- 14-15 Territorio
setp(S(14), LBL, 0, ["3 · Resultados"])
setp(S(14), (18,), 0, ["Amazonas"])
notes(S(14), "El peso de cada factor cambia por departamento. En Puno destaca la altitud; en Amazonas y Madre de Dios, "
             "la pobreza; en Huancavelica, el bajo peso al nacer, el intervalo entre partos y la edad del jefe de hogar. "
             "Esto sugiere priorizar las intervenciones según el perfil de cada territorio y no solo según la prevalencia.")
s = S(15)
setp(s, LBL, 0, ["3 · Resultados"])
delete(s, {8})
pic_fit(s, f"{FIG}/f9.png", 0.75, 2.95, 13.35, 7.35)
notes(s, "Este es el mapa completo: cada fila es un departamento y cada columna uno de los diez factores principales. "
             "Mientras más oscuro, más pesa ese factor en ese departamento. Las líneas separan costa, sierra y selva.")

# ---------------------------------------------------------------- 16-17 Aplicación
s = S(16)
setp(s, LBL, 0, ["4 · La aplicación"])
setp(s, TTL, 0, ["¿Qué hace la aplicación?"])
notes(s, "Implementamos el modelo en una aplicación web en Streamlit con tres capas: presentación, lógica y datos. "
         "Con los datos del hogar y de la madre, estima el riesgo del niño sin necesidad de pesarlo ni tallarlo.")
s = S(17)
setp(s, LBL, 0, ["4 · La aplicación"])
setp(s, TTL, 0, ["La aplicación en acción"])
notes(s, "La aplicación está disponible en stunting-risk-peru.streamlit.app. Permite ver el mapa de riesgo por "
         "departamento, evaluar a un niño con la explicación de su puntaje y evaluar a un grupo desde un archivo. "
         "En 300 niños de la ENDES 2025 reconoció las 45 columnas y marcó 100 como prioridad alta.")

# ---------------------------------------------------------------- 18 Panel (copia de la diapositiva de datos)
s = S(18)
setp(s, LBL, 0, ["5 · Evaluación"])
setp(s, TTL, 0, ["¿Qué opinaron los profesionales de salud?"])
setp(s, (10,), 0, ["TAM2", ": 19 ítems Likert de 1 a 5, una valoración global de 1 a 10 y 4 preguntas abiertas."])
setp(s, (13,), 0, ["4 expertos"])
setp(s, (14,), 0, ["3 nutricionistas y 1 enfermero, con 10 años o más de experiencia"])
setp(s, (17,), 0, ["≥ 4 de 5"])
setp(s, (18,), 0, ["mediana en los 8 constructos evaluados"])
setp(s, (21,), 0, ["9 de 10"])
setp(s, (22,), 0, ["mediana de la valoración global"])
setp(s, (25,), 0, ["75%"])
setp(s, (26,), 0, ["menor acuerdo: confianza en el riesgo y datos disponibles"])
setp(s, (27,), 0, ["Sugerencias: ", "datos más actuales, extender a sobrepeso y micronutrientes, y más detalle territorial."])
notes(s, "Con la aprobación del Comité de Ética de la Escuela, cuatro especialistas evaluaron la aplicación con un "
         "instrumento basado en TAM2. Todos los constructos alcanzaron una mediana de 4 o más, y la valoración global "
         "tuvo una mediana de 9 sobre 10. El menor acuerdo, 75%, fue en la confianza en los niveles de riesgo y en "
         "la disponibilidad de los datos y de la hemoglobina.")

# ---------------------------------------------------------------- 19 Alcance
setp(S(19), LBL, 0, ["6 · Alcance"])
notes(S(19), "Es importante aclarar el alcance. La herramienta estima una probabilidad y apoya la focalización y el "
             "triaje; no diagnostica ni reemplaza al profesional. Además, el estudio tiene límites: la ENDES es "
             "transversal, así que el modelo identifica asociaciones y no causas, no se validó con datos externos ni "
             "por periodos, y cuatro especialistas no permiten generalizar la evaluación.")

# ---------------------------------------------------------------- 20 Conclusiones (copia de la diapositiva de la pregunta)
s = S(20)
setp(s, LBL, 0, ["7 · Conclusiones"])
setp(s, TTL, 0, ["Conclusiones"])
setp(s, (12, 14), 0, ["“Los datos de rutina de la encuesta permiten priorizar a los niños con mayor riesgo y explicar cada resultado.”"])
setp(s, (15,), 0, ["Resultado: ", "LightGBM logró un AUC-ROC de 0.83 y detectó el 80.5% de los casos con el umbral de triaje."])
setp(s, (16,), 0, ["Trabajo futuro: ", "validar por periodos, sumar datos locales y extender a sobrepeso y micronutrientes."])
notes(s, "En conclusión, LightGBM logró el mejor equilibrio entre discriminación y detección de casos. La pobreza del "
         "hogar, el peso y el tamaño al nacer y la altitud fueron los factores más asociados al riesgo, con perfiles "
         "que varían por departamento. La aplicación explica cada resultado y fue valorada favorablemente como apoyo "
         "a la focalización, no al diagnóstico. Como trabajo futuro: validar por periodos, corregir la escala del "
         "índice de riqueza, incorporar datos locales y extender el enfoque al sobrepeso y a los micronutrientes.")

# ---------------------------------------------------------------- 21 Referencias
s = S(21)
refs = [
    ["Black, R. E., Victora, C. G., Walker, S. P., et al. (2013). ",
     "Maternal and child undernutrition and overweight in low-income and middle-income countries. ",
     "The Lancet, 382(9890), 427–451."],
    ["Victora, C. G., Christian, P., Vidaletti, L. P., et al. (2021). ",
     "Revisiting maternal and child undernutrition in low-income and middle-income countries. ",
     "The Lancet, 397(10282), 1388–1399."],
    ["Ke, G., Meng, Q., Finley, T., et al. (2017). ",
     "LightGBM: A highly efficient gradient boosting decision tree. ",
     "Advances in Neural Information Processing Systems 30, 3146–3154."],
    ["Lundberg, S. M., & Lee, S.-I. (2017). ",
     "A unified approach to interpreting model predictions. ",
     "Advances in Neural Information Processing Systems 30."],
    ["Venkatesh, V., & Davis, F. D. (2000). ",
     "A theoretical extension of the technology acceptance model: four longitudinal field studies. ",
     "Management Science, 46(2), 186–204."],
]
for path, ref in zip([(12, 14), (19, 21), (26, 28), (33, 35), (40, 42)], refs):
    setp(s, path, 0, ref)
notes(s, "Estas son las referencias principales. La lista completa está en el artículo.")

# ---------------------------------------------------------------- 22 Gracias
s = S(22)
setp(s, (5,), 0, ["Agradecemos su atención. Quedamos atentos a sus preguntas."])
setp(s, (8,), 0, ["EP Ingeniería de Sistemas — Universidad Peruana Unión · Coautor: Ferdinand Pineda Ancco · Asesor: Mg. Nemias Saboya Rios"])
notes(s, "Muchas gracias por su atención. Quedamos atentos a sus preguntas.")

p.save(OUT)
print("saved", OUT)
