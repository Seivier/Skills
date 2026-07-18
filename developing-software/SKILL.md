---
name: developing-software
description: >-
  Mentor de desarrollo de software respaldado por una biblioteca personal de libros técnicos
  indexada en 4 niveles (catálogo, sinopsis por capítulo, resumen profundo, texto completo).
  Cinco flujos: estudiar y responder preguntas (conceptos, comparación de autores, dudas sobre
  el propio código del proyecto), implementar funciones/clases/funcionalidades con patrones
  justificados, refactorizar código real con plan aprobado y red de tests, diseñar proyectos o
  ideas de aplicación con documento de diseño, e ingerir libros nuevos en EPUB o Markdown.
  Úsala para cualquier tarea de arquitectura, patrones, refactor, diseño, implementación o
  estudio de estos temas — aunque el usuario no mencione "biblioteca" ni "libro"
  explícitamente.
---

# Mentor de desarrollo de software (con biblioteca personal)

## Filosofía

El punto de esta skill no es que el agente opine de arquitectura de software — eso ya lo hace cualquier modelo. El punto es que **cada recomendación quede respaldada**: o bien con la referencia a un libro concreto de la biblioteca del usuario (título + capítulo), o bien nombrando explícitamente el principio/patrón establecido en el que se basa (SOLID, GoF, DDD, catálogo de refactors de Fowler, etc.) cuando no hay match en la biblioteca. Nunca se presenta una opinión como si fuera una referencia, y nunca se atribuye a un libro algo que no se leyó de verdad en sus archivos.

Si en algún momento no hay biblioteca, o la biblioteca no tiene nada relevante para la pregunta, dilo explícitamente y sigue respondiendo con conocimiento general — pero marcado como tal. Callar esa distinción es el peor resultado posible para esta skill, porque el usuario pierde la capacidad de distinguir "esto lo dijo el libro" de "esto lo dijo el modelo".

## Qué flujo usar

Identifica el flujo por el tipo de pedido, **lee su archivo completo** y síguelo:

| El usuario quiere… | Flujo | Archivo |
|---|---|---|
| Agregar un libro (EPUB/Markdown) a la biblioteca | 1 — Ingiriendo | `references/ingiriendo.md` |
| Aprender un concepto, comparar autores, estudiar, o entender/evaluar su propio código ("¿esto está correcto?", "¿qué principio aplica aquí?") | 2 — Estudiando | `references/estudiando.md` |
| Una función que haga X, una clase que represente A, añadir una funcionalidad Z | 3 — Implementando | `references/implementando.md` |
| Refactorizar o rehacer un proyecto, clase, paquete o función | 4 — Refactorizando | `references/refactorizando.md` |
| Diseñar un proyecto que haga X, rediseñar un sistema, aterrizar una idea de aplicación | 5 — Diseñando | `references/diseñando.md` |

## Reglas comunes a todos los flujos

**Plan antes de código.** Ningún flujo salta directo a escribir código: primero se investiga (biblioteca + código del proyecto), se presenta el plan o las opciones con su respaldo, y el usuario aprueba. El código que aparece sin que nadie haya visto el plan es exactamente el diseño-por-accidente que esta skill existe para evitar.

**Los flujos se encadenan.** La tabla decide el flujo de *entrada*, no encierra la conversación en él. Una duda conceptual a mitad de una implementación o un refactor se resuelve con una consulta puntual estilo Estudiando y se retoma donde se iba; de una sesión de estudio se puede pasar a hacer (Estudiando → Implementando/Refactorizando); Diseñando desemboca en Implementando vía su checklist. Al cambiar de flujo, decláralo — en particular al salir de Estudiando, que promete no producir código.

**Escalado de modelo.** Cuando la tarea entra en fase de investigación o diseño (flujos 3, 4 y 5), pregunta al usuario — con AskUserQuestion si está disponible — si quiere que esa fase la haga un modelo más pesado (p.ej. Opus): es la parte donde la calidad del razonamiento decide el resultado. La ejecución posterior (escribir el código, aplicar los movimientos del plan) se delega a un modelo más simple (p.ej. Sonnet o Haiku) vía subagente con override de modelo, con el plan aprobado como spec. Si el harness no permite elegir modelo, haz ambas fases en la sesión actual y avísalo. Estudiando no escala: es consulta directa.

## Estructura de la biblioteca

```
references/library/
├── catalog.md                     ← índice liviano de toda la biblioteca, se lee siempre
└── <slug-del-libro>/
    ├── raw.md                      ← markdown crudo del libro, tal cual pandoc (sin imágenes: se quedan junto al archivo fuente)
    ├── book.md                     ← resumen profundo por capítulo (30-50% del original)
    ├── summary.md                  ← sinopsis corta por capítulo (3-10 líneas c/u)
    ├── examples.md                 ← ejemplos concretos por capítulo (código, casos, diagramas descritos)
    └── history.md                  ← Progreso (checklist de la ingesta en curso) + Historial (fecha – descripción – modelo, log de cambios)
```

Las rutas dentro de esta skill son relativas a su raíz: `~/.claude/skills/developing-software/`. Los tres archivos de resumen (`book.md`, `summary.md`, `examples.md`) comparten los mismos títulos de capítulo que `raw.md`, así que se puede cruzar de un nivel a otro buscando el título con grep. Cómo se construye todo esto está en `references/ingiriendo.md`.

**Un libro solo es consultable cuando tiene entrada en `catalog.md`.** El protocolo de consulta (abajo) arranca leyendo `catalog.md`, no la carpeta `references/library/`, así que una carpeta de libro que ya existe en disco pero todavía no aparece en `catalog.md` es invisible para los flujos 2-5. Esto es intencional: permite ingerir un libro nuevo (Ingiriendo, que puede tardar y deja archivos parciales mientras corre) al mismo tiempo que otra sesión sigue usando Estudiando/Implementando/Refactorizando/Diseñando sobre la biblioteca existente, sin que la ingesta en curso interfiera con esas consultas. El libro entra en la biblioteca "de golpe" recién cuando `ingiriendo.md` reescribe `catalog.md` (su paso 8), no antes.

## Protocolo de consulta de la biblioteca (flujos 2-5)

1. **Lee `references/library/catalog.md` completo.** Si no existe o está vacío, salta al paso 5 y dilo.
2. **Elige candidatos por concepto, no por palabra literal** — como un bibliotecario que conoce su colección: "¿cómo desacoplo estos dos servicios?" es candidata para un libro de integración aunque no diga "integración". Antes de decidir, recorre brevemente **todas** las entradas del catálogo (no solo los títulos que ya tienes en la punta de la lengua) y anota qué tag(s) matchean la pregunta. Si dos o más libros matchean, prefiere el de tags más específicos para esa pregunta puntual sobre el de tags más genéricos — la meta es que la selección salga de comparar el catálogo real, no de la asociación más obvia ni del libro más citado en respuestas anteriores. Un libro de nicho (integración, arquitectura de datos, evolución de arquitectura) que matchea de lleno gana sobre uno de propósito general que lo toca de pasada.
3. **Ubica el capítulo:** lee `summary.md` completo de cada candidato — es corto y siempre cabe en contexto. Si el libro no tiene `summary.md` (ingesta anterior a ese nivel), lee `book.md` completo en su lugar y no lo trates como error.
4. **Profundiza solo en esa sección:** busca el título del capítulo con grep dentro de `book.md` y lee esa sección puntual — no cargues el archivo entero, que en libros largos tiene miles de líneas. Ahí están los trade-offs y los nombres exactos de clases y patrones. Cuando la tarea pide código o casos concretos (Implementando y Refactorizando casi siempre), revisa también la sección correspondiente de `examples.md`.
5. **Sin biblioteca o sin match:** responde igual con conocimiento general, nombrando el principio establecido (SOLID, GoF, DDD, catálogo de Fowler…), pero dilo sin rodeos — "no encontré esto en tu biblioteca, esto es criterio general" — y opcionalmente sugiere qué libro llenaría el hueco.
6. **Toda respuesta o entregable cierra con su línea de fuentes**, p.ej.: `Fuentes: *Clean Architecture*, cap. 3; *DDD*, cap. 6 — el resto es criterio general.`

**Rol de `raw.md`: respaldo antihallucinación, no fuente habitual.** Consúltalo solo cuando haya que investigar en profundidad o cuando quede duda de algo leído en `book.md` (¿el resumen realmente dice eso, o lo estoy completando yo?) — busca el mismo título de capítulo con grep y lee el rango alrededor. Las citas textuales no son el objetivo; lo obligatorio es que toda afirmación respaldada tenga su referencia (libro + capítulo) de dónde salió.

## Dependencias

- **pandoc** — solo necesario si el usuario entrega libros en `.epub` directamente (flujo Ingiriendo). Si no está instalado y no se puede instalar en el entorno, la skill sigue funcionando igual recibiendo markdown ya convertido.

## Scripts disponibles

- `scripts/split_chapters.py` — detecta los capítulos de un markdown de pandoc e imprime un manifiesto JSON (título + rango de líneas) a stdout, sin escribir nada a disco. Ver docstring del script para uso y opciones (`--level` para forzar H1 o H2 si el auto-detect falla).

