# Building Evolutionary Architectures

## Progreso
- [x] Configuración inicial y copia de raw.md
- [x] Detección de capítulos (H1 detectó 79 subsecciones; consolidado manualmente en 9 capítulos + front matter, ver Historial)
- [x] Procesar Front Matter (portada, prefacios, agradecimientos) — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 1 — Evolving Software Architecture — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 2 — Fitness Functions — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 3 — Engineering Incremental Change — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 4 — Automating Architectural Governance — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 5 — Evolutionary Architecture Topologies — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 6 — Evolutionary Data — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 7 — Building Evolvable Architectures — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 8 — Evolutionary Architecture Pitfalls and Antipatterns — modelo: claude-haiku-4-5-20251001
- [x] Procesar Capítulo 9 — Putting Evolutionary Architecture into Practice — modelo: claude-haiku-4-5-20251001
- [x] Ensamblado de book.md, summary.md y examples.md
- [x] Actualización de catalog.md

## Historial
- 2026-07-17 — Ingesta inicial de *Building Evolutionary Architectures* (2ª ed.) vía EPUB+pandoc. El split_chapters.py por H1 detectó 79 secciones (muchas eran subsecciones internas de un mismo capítulo, no capítulos reales), así que se consolidaron manualmente en 9 capítulos + Front Matter según los encabezados "Chapter N." del libro. Se omitieron Index, About the Authors y Colophon (sin contenido de autor sustantivo para resumir). Los 10 ítems se resumieron en paralelo vía Workflow con Haiku, sin errores ni bloqueos de filtro de contenido — no hubo fragmentación ni reintentos, por lo que no aplica el subflujo de auditoría de fidelidad (paso 9b). — modelo: claude-sonnet-5
