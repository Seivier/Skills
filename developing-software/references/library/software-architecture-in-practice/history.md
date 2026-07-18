# Software Architecture in Practice (4th ed.)

## Progreso
- [x] Configuración inicial y copia de raw.md
- [x] Detección de capítulos
- [x] Procesar Preface — modelo: claude-haiku-4-5
- [x] Procesar Acknowledgments — modelo: claude-haiku-4-5
- [x] Procesar Chapter 1. What Is Software Architecture? — modelo: claude-haiku-4-5
- [x] Procesar Chapter 2. Why Is Software Architecture Important? — modelo: claude-haiku-4-5
- [x] Procesar Chapter 3. Understanding Quality Attributes — modelo: claude-haiku-4-5
- [x] Procesar Chapter 4. Availability — modelo: claude-haiku-4-5
- [x] Procesar Chapter 5. Deployability — modelo: claude-haiku-4-5
- [x] Procesar Chapter 6. Energy Efficiency — modelo: claude-haiku-4-5
- [x] Procesar Chapter 7. Integrability — modelo: claude-haiku-4-5
- [x] Procesar Chapter 8. Modifiability — modelo: claude-haiku-4-5
- [x] Procesar Chapter 9. Performance — modelo: claude-haiku-4-5
- [x] Procesar Chapter 10. Safety — modelo: claude-haiku-4-5
- [x] Procesar Chapter 11. Security — modelo: claude-haiku-4-5
- [x] Procesar Chapter 12. Testability — modelo: claude-haiku-4-5
- [x] Procesar Chapter 13. Usability — modelo: claude-haiku-4-5
- [x] Procesar Chapter 14. Working with Other Quality Attributes — modelo: claude-haiku-4-5
- [x] Procesar Chapter 15. Software Interfaces — modelo: claude-haiku-4-5
- [x] Procesar Chapter 16. Virtualization — modelo: claude-haiku-4-5
- [x] Procesar Chapter 17. The Cloud and Distributed Computing — modelo: claude-haiku-4-5
- [x] Procesar Chapter 18. Mobile Systems — modelo: claude-haiku-4-5
- [x] Procesar Chapter 19. Architecturally Significant Requirements — modelo: claude-haiku-4-5
- [x] Procesar Chapter 20. Designing an Architecture — modelo: claude-haiku-4-5
- [x] Procesar Chapter 21. Evaluating an Architecture — modelo: claude-haiku-4-5
- [x] Procesar Chapter 22. Documenting an Architecture — modelo: claude-haiku-4-5
- [x] Procesar Chapter 23. Managing Architecture Debt — modelo: claude-haiku-4-5
- [x] Procesar Chapter 24. The Role of Architects in Projects — modelo: claude-haiku-4-5
- [x] Procesar Chapter 25. Architecture Competence — modelo: claude-haiku-4-5
- [x] Procesar Chapter 26. A Glimpse of the Future: Quantum Computing — modelo: claude-haiku-4-5
- [x] Procesar References — modelo: claude-haiku-4-5
- [x] Ensamblado de book.md, summary.md y examples.md
- [x] Actualización de catalog.md

## Historial
- 2026-07-17 — Ingesta inicial completa: 29 ítems (Preface, Acknowledgments, 26 capítulos numerados, References; se excluyeron About this eBook, Contents, About the Authors e Index del manifiesto por ser puramente estructurales). La detección automática por H1 de `split_chapters.py` falló (agrupaba varios capítulos reales bajo un mismo divisor de Parte, y el último bloque "Part VI: Conclusions" mezclaba el capítulo 26 con References/About the Authors/Index en un solo rango de 5778 líneas) porque el EPUB marca el número de capítulo como H2 y el título real como H1 o texto plano suelto varias líneas después — se reconstruyó el manifiesto a mano localizando cada header `## N` y tomando el primer párrafo no vacío siguiente como título real, verificado contra el índice del libro. Todos los 29 ítems se resumieron en paralelo con Haiku sin bloqueos de filtro de contenido ni errores. — modelo orquestador: claude-sonnet-5
