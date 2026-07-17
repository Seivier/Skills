# Domain-Driven Design: Tackling Complexity in the Heart of Software

## Progreso

- [x] Configuración inicial y copia de raw/raw.md (con corrección de rutas de `media/`, ver nota abajo)
- [x] Detección de capítulos (H2 → 29 secciones detectadas)
- [x] Procesar Foreword — modelo: haiku
- [x] Procesar Preface — modelo: haiku
- [x] Procesar Capítulo One. Crunching Knowledge — modelo: haiku
- [x] Procesar Capítulo Two. Communication and the Use of Language — modelo: haiku
- [x] Procesar Capítulo Three. Binding Model and Implementation — modelo: haiku
- [x] Procesar Capítulo Four. Isolating the Domain — modelo: haiku
- [x] Procesar Capítulo Five. A Model Expressed in Software — modelo: haiku
- [x] Procesar Capítulo Six. The Life Cycle of a Domain Object — modelo: haiku
- [x] Procesar Capítulo Seven. Using the Language: An Extended Example — modelo: haiku
- [x] Procesar Capítulo Eight. Breakthrough — modelo: haiku
- [x] Procesar Capítulo Nine. Making Implicit Concepts Explicit — modelo: haiku
- [x] Procesar Capítulo Ten. Supple Design — modelo: haiku
- [x] Procesar Capítulo Eleven. Applying Analysis Patterns — modelo: haiku
- [x] Procesar Capítulo Twelve. Relating Design Patterns to the Model — modelo: haiku
- [x] Procesar Capítulo Thirteen. Refactoring Toward Deeper Insight — modelo: haiku
- [x] Procesar Capítulo Fourteen. Maintaining Model Integrity — modelo: haiku
- [x] Procesar Capítulo Fifteen. Distillation — modelo: haiku
- [x] Procesar Capítulo Sixteen. Large-Scale Structure — modelo: haiku (reintentado: el primer intento falló por un límite de tokens de la herramienta Read al leer el rango de 1714 líneas; el reintento con instrucciones más explícitas sobre offset/limit tuvo éxito)
- [x] Procesar Capítulo Seventeen. Bringing the Strategy Together — modelo: haiku
- [x] Procesar Conclusion — modelo: haiku
- [x] Procesar Appendix. The Use of Patterns in This Book — modelo: haiku
- [x] Procesar Glossary — modelo: haiku
- [x] Ensamblado de book.md, summary.md y examples.md
- [x] Actualización de catalog.md

## Historial

- 2026-07-09 — Ingesta inicial: 29 secciones procesadas — modelo: haiku (capítulos), claude-sonnet-5 (orquestación)
- 2026-07-09 — Backfill de summary.md (nivel intermedio de sinopsis corta, hoy renombrado desde chapters.md) — modelo: claude-sonnet-5
- 2026-07-09 — Backfill del resumen de catalog.md a 5-10 líneas — modelo: claude-sonnet-5
- 2026-07-10 — Renombrado de archivos de la biblioteca: summary.md→book.md, chapters.md→summary.md, todo.md→history.md; history.md reestructurado en secciones Progreso + Historial — modelo: claude-sonnet-5

### Detalle de la ingesta inicial (2026-07-09)

**Secciones detectadas sin contenido sustantivo de diseño (omitidas deliberadamente, sin gastar `agent()`):** Praise for *Domain-Driven Design*, Contents (índice/TOC), Acknowledgments, References (bibliografía), Photo Credits, Index, Footnotes — son portada/agradecimientos/material de referencia sin prosa de diseño. Se documentan en `summary.md` y `examples.md` con una línea explícita de "sin contenido sustantivo" en vez de resumirlas con un agente.

**Nota técnica sobre `raw/`:** esta versión de pandoc (3.7.0.2) referencia las imágenes con el prefijo `media/` incluido (ej. `media/graphics/9780132181273.jpg`), a diferencia del caso general documentado en el skill. Por eso `raw/media/` se mantiene como subcarpeta (no aplanada) — se verificó con `test -f` que las rutas resuelven así.

**Verificación final:**
- `raw/raw.md` (23,546 líneas) + `raw/media/graphics/` (222 imágenes) — rutas de imagen verificadas con `test -f`.
- `book.md` y `examples.md` (nombres actuales; en ese momento `summary.md` y `examples.md`): 29 encabezados `##` cada uno, coincidiendo con las 29 secciones H2 detectadas.
- Capítulo 16 verificado manualmente tras el reintento (ratio de densidad ~7.5 caracteres/línea, en línea con el resto de capítulos; el resto de capítulos dio entre 4 y 30 caracteres/línea, todos dentro de rango razonable salvo el fallo puntual ya corregido).
- `catalog.md` reescrito completo con la nueva entrada, releído desde disco para confirmar.
