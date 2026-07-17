# Patterns of Enterprise Application Architecture

## Progreso
- [x] Configuración inicial y copia de raw.md
- [x] Detección de capítulos
- [x] Procesar Preface — modelo: claude-haiku-4-5
- [x] Procesar Introduction — modelo: claude-haiku-4-5
- [x] Procesar Chapter 1. Layering — modelo: claude-haiku-4-5
- [x] Procesar Chapter 2. Organizing Domain Logic — modelo: claude-haiku-4-5
- [x] Procesar Chapter 3. Mapping to Relational Databases — modelo: claude-haiku-4-5
- [x] Procesar Chapter 4. Web Presentation — modelo: claude-haiku-4-5
- [x] Procesar Chapter 5. Concurrency — modelo: claude-haiku-4-5
- [x] Procesar Chapter 6. Session State — modelo: claude-haiku-4-5
- [x] Procesar Chapter 7. Distribution Strategies — modelo: claude-haiku-4-5
- [x] Procesar Chapter 8. Putting It All Together — modelo: claude-haiku-4-5
- [x] Procesar Chapter 9. Domain Logic Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 10. Data Source Architectural Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 11. Object-Relational Behavioral Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 12. Object-Relational Structural Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 13. Object-Relational Metadata Mapping Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 14. Web Presentation Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 15. Distribution Patterns — modelo: claude-sonnet-5 (haiku bloqueado por filtro de contenido de la API; dividido en 4 fragmentos y reintentado con sonnet)
- [x] Procesar Chapter 16. Offline Concurrency Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 17. Session State Patterns — modelo: claude-haiku-4-5
- [x] Procesar Chapter 18. Base Patterns — modelo: claude-haiku-4-5
- [x] Procesar References — modelo: claude-haiku-4-5
- [x] Ensamblado de book.md, summary.md y examples.md
- [x] Actualización de catalog.md

## Historial
- 2026-07-16 — Ingesta inicial completa: 21 capítulos (Preface, Introduction, 18 capítulos, References; se excluyeron Contents e Index del manifiesto por ser puramente estructurales). El Capítulo 15 (Distribution Patterns) falló repetidamente con Haiku por un bloqueo del filtro de contenido de la API y se reintentó dividido en 4 fragmentos con Sonnet. — modelo orquestador: claude-sonnet-5
- 2026-07-16 — Revisión de coherencia del Capítulo 15 tras la fragmentación: verificados los 3 puntos de corte en `raw.md` contra el texto original (todos caen en transiciones limpias, sin pérdida ni duplicación de contenido). Se corrigió un defecto real en `examples.md`: la lista de ejemplos reiniciaba su numeración a mitad de capítulo (1-9 seguido de otro 1-6) sin ningún separador que indicara el cambio de fragmento — se renumeró de forma continua (1-17) y se agregaron subtítulos de sección más una nota explicando la fragmentación. `book.md` y `summary.md` ya tenían marcadores `[Remote Facade — part N de 3]` legibles y no requirieron cambios. — modelo orquestador: claude-sonnet-5
- 2026-07-16 — Auditoría profunda del Capítulo 15 contrastando contra `raw.md` línea por línea (subagente dedicado). Encontró y se corrigieron dos defectos reales: (1) `summary.md` atribuía al Capítulo 15 la cita "First Law of Distributed Object Design" que en realidad pertenece al Capítulo 7 (línea 5643 de raw.md) — alucinación de atribución, eliminada; (2) `book.md` omitía la moraleja de cierre del ejemplo Web Service ("The important thing to remember... isn't the cool gyrations with SOAP and .NET but the fundamental layering approach") — agregada. Además, `examples.md` para este capítulo no contenía ningún fragmento de código real (solo descripciones en prosa, a diferencia de todos los demás capítulos del libro) — se extrajeron programáticamente los 17 bloques de código literal desde `raw.md` (líneas 20801-21824) limpiando artefactos de pandoc (escapes, anchors `<span>`, saltos de línea de maquetación) y se reemplazó la sección completa. Todas las citas textuales entre comillas en `book.md` se verificaron como literales contra raw.md. — modelo orquestador: claude-sonnet-5
