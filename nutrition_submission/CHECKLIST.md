# Envío a *Nutrition* (Elsevier) – lista de verificación

Basada en la *Guide for Authors* de la revista (consultada el 11/11/2026).

## Archivos a subir
- [ ] `main.tex` + `references.bib` + figuras (el PDF **no** sirve como archivo fuente)
- [ ] `highlights.txt` como archivo aparte, con "highlights" en el nombre (3–5 viñetas, ≤ 85 caracteres)
- [ ] Cada figura como archivo aparte: `Figure_1.pdf` … `Figure_10.png`
- [ ] Documento de la herramienta de declaraciones (conflicto de intereses), en .docx
- [ ] Resumen gráfico (opcional, recomendado)

## Requisitos y estado del manuscrito actual
| Requisito de la guía | Manuscrito actual |
|---|---|
| Investigación original: **3000–5000 palabras incluyendo tablas, figuras y referencias** | ⚠️ ~6100 palabras de texto + ~1600 de referencias ≈ 7700. Hay que recortar |
| Resumen ≤ 250 palabras, estructurado (Objective / Methods / Results / Conclusions) | ✅ 202 palabras |
| 1–7 palabras clave | ✅ 6 |
| Highlights obligatorios | ➕ borrador en `highlights.txt` |
| Página de título con correo del autor de correspondencia y dirección postal completa | ⚠️ falta el correo y la dirección |
| Figuras: no combinar varias imágenes en un archivo | ⚠️ la Fig. 10 junta 4 capturas; justificarla o dividirla |
| Figuras: vectoriales (PDF/EPS) o ≥ 300 dpi | ✅ PDF vectorial para Figs. 1–4 y 6–9 en `figures_en/` |
| Tablas editables, sin líneas verticales | ✅ (booktabs) |
| Referencias numeradas [n] por orden de aparición, estilo consistente | ✅ — corregir errores del .bib (ver abajo) |
| CRediT, Funding, Competing interests, Data availability | ➕ secciones en `main.tex` |
| Declaración de IA generativa antes de las referencias | ✅ (usar el título exacto de la guía) |
| Revisión simple anónima | ✅ no hace falta anonimizar |

## Errores concretos a corregir antes de enviar
- Sección 2.6: el código del comité de ética dice **"code XXXX"**.
- Refs. [6], [46], [50] (y [25]): aparece `amp;` y `<scp>w</scp>`. En el `.bib` escribir `\&` y quitar las etiquetas `<scp>`.
- Ref. [15]: falta el espacio antes de `doi`: "1–12doi:10.1017/…".
