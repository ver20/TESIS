# Envío a *Nutrition* (Elsevier): revisión completa de la guía para autores

Revisión punto por punto de la *Guide for Authors* (descargada el 11/11/2026) frente a la versión `main-en_1.pdf`.
✅ cumple · ⚠️ hay que corregir · ⓘ recomendable (no obligatorio) · ➖ no aplica

## 1. Tipo de artículo y extensión
| Requisito | Estado |
|---|---|
| Investigación original: 3000–5000 palabras incluyendo tablas, figuras y referencias | ✅ ~4,940 |
| Revisión anónima simple (no hace falta anonimizar) | ✅ |

## 2. Ética y políticas
| Requisito | Estado |
|---|---|
| Trabajo no publicado antes (una tesis o un preprint no cuentan) | ✅ |
| Un solo autor de correspondencia con datos completos | ✅ Nemias Saboya |
| Criterios de autoría (aporte, redacción o revisión, aprobación final) | ✅ según CRediT |
| Nombres escritos igual que en el sistema de envío; no se pueden cambiar después | ⚠️ unificar "Saboya-Rios" / "Saboya Ríos" (tilde) y los guiones de los apellidos |
| Conflicto de intereses en el artículo y en la herramienta de declaraciones (.docx) | ✅ en el artículo; ⚠️ falta generar el .docx al enviar |
| Financiamiento | ✅ |
| Declaración de IA generativa antes de las referencias | ⚠️ actualizarla: también se usó IA para figuras, traducción y material suplementario |
| Lenguaje inclusivo | ✅ ⓘ se puede preferir "children with stunting" a "stunted children" |
| Sexo y género definidos (SAGER) | ✅ |
| Manipulación de imágenes / IA en figuras | ⚠️ ver sección 6 |
| Mapas: solo el área de estudio, con nota sobre fronteras | ✅ nota presente; ⓘ el mapa base muestra el nombre "ECUADOR" |
| Afiliación con el nombre oficial completo de la institución | ✅ |
| Registro de ensayo clínico | ➖ estudio observacional |

## 3. Formato de archivo y página de título
| Requisito | Estado |
|---|---|
| Fuente editable (.tex); el PDF no sirve como fuente | ⚠️ subir .tex, .bib y figuras |
| Dos columnas permitidas en LaTeX; sin tachados ni subrayados | ✅ |
| Título conciso y sin abreviaturas | ✅ |
| Afiliaciones con letra en superíndice, dirección postal y país | ✅ |
| Correo del autor de correspondencia | ✅ |

## 4. Resumen, palabras clave, highlights
| Requisito | Estado |
|---|---|
| ≤ 250 palabras, estructurado y sin referencias | ✅ 205 |
| Abreviaturas poco comunes definidas en el resumen | ⚠️ definir CRISP-DM, SHAP y TAM2 |
| Methods & Procedures: diseño y duración del estudio | ⚠️ agregar el diseño ("observational/cross-sectional"); la duración 2007–2025 ✅ |
| Resultados con significancia estadística | ✅ IC 95% |
| 1–7 palabras clave en inglés, sin "and/of" | ✅ ⓘ SHAP y LightGBM son abreviaturas; se pueden mantener |
| Highlights: archivo aparte, 3–5 viñetas de ≤ 85 caracteres | ⚠️ subir `highlights.txt` |
| Resumen gráfico | ⓘ opcional (≥ 1328 px de ancho) |

## 5. Unidades, fórmulas y tablas
| Requisito | Estado |
|---|---|
| Unidades SI, con equivalencia si se usa otra | ⚠️ Fig. 8: "Hemoglobin: 9.6 g/dL (96 g/L)"; agregar "(months)" a "Birth interval" |
| Ecuaciones como texto editable, numeradas y con variables en cursiva | ✅ ⓘ definir M en la Ec. 2 (M = 45) |
| Tablas editables, citadas en orden y con notas debajo | ✅ |
| Tablas sin líneas verticales ni sombreado | ✅ |
| Tablas que no dupliquen el texto | ⓘ la sección 3.3 repite cifras de la Tabla 2 (recortar también ahorra palabras) |

## 6. Figuras
| Requisito | Estado |
|---|---|
| Cada figura en su propio archivo (Figure_1…Figure_13), citadas en orden | ⚠️ preparar los archivos |
| Pie de figura = título breve + descripción, explicando símbolos y abreviaturas | ⚠️ explicar abreviaturas: Fig. 1 (HAZ, SD, WHO, VIF, CI, CART, MLP, TAM2), Fig. 2 (HHID, CASEID, HAZ), Fig. 3 y 7 (SHAP), Fig. 5 (AUC), Fig. 8 (log-odds) |
| Título fuera de la imagen | ✅ |
| Vectorial con fuentes incrustadas, o ≥ 300 dpi | ✅ |
| Texto no desproporcionadamente pequeño | ⚠️ capturas 10–13 y texto pequeño en Figs. 1–2 |
| Colores accesibles para daltonismo | ⓘ Fig. 5: rojo y verde; agregar estilos de línea |
| IA en figuras: permitida para diagramas y gráficos derivados de los datos de forma reproducible; si se usó IA, declararlo en cada pie y en la declaración | ⚠️ las Figs. 1–4 y 6–9 se rehicieron con Claude. Las Figs. 4 y 9 usaron valores **recuperados de las imágenes** (aprox. ±0.1): regenerarlas con los datos originales. Declarar el uso de IA en los pies y en la declaración |
| Permiso para material de terceros | ⓘ Fig. 13: mapa base de OpenStreetMap/CARTO, con atribución visible |

## 7. Material suplementario y datos
| Requisito | Estado |
|---|---|
| Citado en el texto, subido junto con el artículo y con una breve descripción | ✅ `Supplementary_material.pdf` (S1–S3, Texto S1) |
| Datos en un repositorio y citados (Opción B) | ✅ Zenodo ⓘ se pueden agregar como referencias `[dataset]` (suma ~75 palabras) |

## 8. Estructura y referencias
| Requisito | Estado |
|---|---|
| Secciones con encabezados | ✅ |
| CRediT con los roles oficiales | ✅ |
| Agradecimientos: incluir a quien ayudó con idioma, redacción o revisión | ⚠️ si un traductor revisó el texto, agregar *Acknowledgments* antes de las referencias |
| Referencias reales, completas, con DOI y numeradas por orden de aparición | ✅ 44 |
| Primeros 6 autores y luego "et al." | ✅ |
| Referencias web con URL y fecha de consulta | ⚠️ ref. [25] (INEI): agregar URL y "[accessed …]" |
| Preprints marcados como tales | ➖ ya no hay |

## 9. Lista de verificación del envío
| Requisito | Estado |
|---|---|
| Todos los archivos subidos (figuras, suplementario, pies de figura) | ⚠️ al enviar |
| Revisión de ortografía y gramática | ⚠️ pendiente final |
| Citas en el texto y referencias coinciden | ✅ |
| Permisos para material con copyright | ⓘ mapa base (ver sección 6) |
| Acceso abierto: los autores pagan el APC si eligen esa opción | ⓘ decidir entre suscripción (gratis) o acceso abierto (con APC) |

## Pendiente fuera de la guía
- Confirmación por escrito del comité de ética sobre el consentimiento implícito del formulario.
- Las cinco mejoras de redacción (0.41/0.42, AUC frente a exactitud, CatBoost, DeLong, "importance of birth weight").
