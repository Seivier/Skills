# The Architecture of Open Source Applications, Vol. 1

## Progreso
- [x] Configuración inicial y copia de raw.md
- [x] Detección de capítulos
- [x] Procesar Table of Contents — modelo: claude-haiku-4-5-20251001
- [x] Procesar Introduction — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 1. Asterisk — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 2. Audacity — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 3. The Bourne-Again Shell — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 4. Berkeley DB — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 5. CMake — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 6. Continuous Integration — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 7. Eclipse — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 8. Graphite — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 9. The Hadoop Distributed File System — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 10. Jitsi — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 11. LLVM — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 12. Mercurial — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 13. The NoSQL Ecosystem — modelo: claude-haiku-4-5-20251001 (rango unido: la cabecera del capítulo quedó separada de su cuerpo por un artefacto de pandoc — ver Historial)
- [x] Procesar Chapter 14. Python Packaging — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 15. Riak and Erlang/OTP — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 16. Selenium WebDriver — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 17. Sendmail — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 18. SnowFlock — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 19. SocialCalc — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 20. Telepathy — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 21. Thousand Parsec — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 22. Violet — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 23. VisTrails — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 24. VTK — modelo: claude-haiku-4-5-20251001
- [x] Procesar Chapter 25. Battle For Wesnoth — modelo: claude-haiku-4-5-20251001
- [x] Procesar Bibliography — modelo: claude-haiku-4-5-20251001
- [x] Ensamblado de book.md, summary.md y examples.md
- [x] Actualización de catalog.md

## Historial
- 2026-07-17 — Ingesta inicial: EPUB descargado de Anna's Archive con ISBN de metadata `9781105571817` (el mismo que Vol. II según nota previa), pero el contenido convertido con pandoc resultó ser íntegramente el Vol. I (25 capítulos: Asterisk → Battle For Wesnoth, coincide con el índice oficial del Vol. I) — error de metadata de la fuente, no una mezcla de volúmenes. 29 secciones detectadas por `split_chapters.py` (H1); el Capítulo 13 (The NoSQL Ecosystem) quedó separado en dos entradas por un artefacto de pandoc (un `<a>` con el nombre del autor mal renderizado como encabezado H1 inmediatamente después del título real del capítulo) y se procesó como un único rango unido (líneas 14260-15856). 28 ítems resumidos en paralelo con Haiku vía Workflow — modelo: claude-sonnet-5.
