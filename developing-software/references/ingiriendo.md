# Flujo 1 — Ingiriendo: agregar un libro nuevo a la biblioteca

Se activa cuando el usuario entrega un EPUB, o un markdown ya generado con pandoc a partir de un EPUB (o pega el contenido), y pide agregarlo a la biblioteca.

**Si lo único disponible es un PDF, no lo conviertas ni extraigas texto de él sin más.** Un PDF pierde estructura de capítulos/encabezados frente a un EPUB (pandoc convierte EPUB con mucha más fidelidad; un PDF requiere heurísticas de extracción — `pdftotext`, `pdfplumber`, OCR — que degradan la detección de capítulos en el paso 3/4). Antes de proceder con un PDF, advierte esto al usuario explícitamente y pide confirmación (con `AskUserQuestion` si está disponible): ¿tiene o puede conseguir el EPUB del mismo libro?, ¿confirma igual seguir con el PDF a pesar de la menor fidelidad? Busca también con cuidado si el EPUB ya existe en el mismo directorio antes de asumir que solo hay PDF — un filtro de búsqueda limitado a `*.pdf` puede ocultar un EPUB presente.

Las rutas de este documento son relativas a la raíz de la skill: `~/.claude/skills/developing-software/`. Sigue los pasos en orden y no improvises de memoria: varios de los avisos marcados como CRÍTICO codifican errores que ya ocurrieron en ingestas reales.

Este documento también incluye, al final, el **Subflujo: Auditoría de fidelidad** — no es parte de la secuencia numerada de ingesta de un libro nuevo, sino una herramienta invocable en cualquier momento (incluso sobre libros ya guardados de sesiones anteriores) para contrastar un capítulo ya ensamblado contra su `raw.md` y detectar alucinaciones u omisiones. Si el usuario pide auditar, verificar o "revisar contra el raw" algo ya en la biblioteca, es ese subflujo el que aplica, no los pasos 1-11.

**Por qué las imágenes nunca entran a la skill:** ninguno de los tres archivos de consulta (`book.md`, `summary.md`, `examples.md`) referencia imágenes — no se usan en los flujos 2-5, son solo peso muerto para la biblioteca (una ingesta real dejó ~180 imágenes y 59 MB en un solo libro). Por eso la conversión (Paso 1) corre dentro de una carpeta `<slug>/` creada junto al `.epub` original, y ahí se quedan tanto el markdown crudo como las imágenes extraídas — el Paso 5 solo copia ese markdown a la skill, renombrado a `raw.md` y suelto directamente en la carpeta del libro (sin subcarpeta `raw/`). El archivo fuente, su carpeta `<slug>/` y las imágenes son responsabilidad del usuario (dónde guardarlos, si respaldarlos en alguna nube, etc.); esta skill nunca los toca ni opina sobre eso.

## Pasos

1. **Si el archivo que te dieron es un `.epub`, conviértelo tú mismo antes de seguir, en una carpeta `<slug>` dentro del mismo directorio donde está el `.epub`.** Determina el slug primero si no es obvio (ver criterio en el paso 2) — lo necesitas para nombrar la carpeta antes de convertir. No hace falta que el usuario corra pandoc a mano. Comprueba primero que esté disponible (`which pandoc`); si no está instalado, avísale y sugiérele instalarlo (`apt-get install pandoc` en la mayoría de los entornos Linux) o que te pase el markdown ya convertido. Si está disponible, ubícate en el directorio del `.epub`, crea la carpeta `<slug>` ahí mismo, y corre pandoc apuntando toda su salida dentro de ella:
   ```bash
   cd "$(dirname <archivo.epub>)"
   mkdir -p <slug>
   pandoc "$(basename <archivo.epub>)" -t gfm --extract-media=<slug>/media -o <slug>/<slug>.md
   ```
   Usa específicamente `-t gfm` (GitHub-Flavored Markdown) y no el escritor "markdown" por defecto de pandoc. El resultado — el markdown y la carpeta `media/` con las imágenes embebidas — debe quedar **todo dentro de `<slug>/`**, nunca suelto en el directorio del `.epub` ni en ninguna ruta de la skill: esa carpeta es lo único que identifica de un vistazo, entre varios libros convertidos en el mismo directorio, cuál `media/` pertenece a cuál markdown. Esas imágenes no se vuelven a tocar en el resto del flujo.

2. **Detectar o pedir el título y el slug.** El slug es el nombre de carpeta (kebab-case, ej. `clean-architecture`). Si no es obvio del contenido, pregúntalo.

3. **Decidir si conviene dividir por capítulos.**
   Cuenta el número total de líneas del archivo markdown (o el tamaño en KB).
   - **Libro corto (< 2,000 líneas):** puedes no dividirlo y tratarlo como un único ítem en el paso 6.
   - **Libro largo (≥ 2,000 líneas):** divídelo por capítulos con `split_chapters.py` (paso 4) — cada capítulo se resume como un ítem independiente en el paso 6.
   El modelo a usar para resumir ya no depende de este tamaño: el paso 6 usa un modelo económico por defecto para todos los casos.

4. **Detectar los capítulos con el script (si se decide dividir).** Ejecuta:
   ```bash
   python3 ~/.claude/skills/developing-software/scripts/split_chapters.py <archivo.md>
   ```
   Esto no escribe nada a disco — solo imprime un manifiesto (JSON) con el título de cada capítulo detectado y el rango de líneas que ocupa en el archivo original. Intenta encabezados H1 primero; si eso da menos de 2 capítulos, prueba H2. Si aun así falla (algunos PDFs o EPUBs mal estructurados no dejan encabezados limpios ni con `-t gfm`), avisa al usuario y ofrece dividir el manifiesto a mano revisando el archivo.

5. **Copia solo el markdown a la carpeta del libro, renombrado a `raw.md` — la carpeta `<slug>/` con sus imágenes se queda donde está, junto al `.epub` fuente.**
   ```bash
   mkdir -p ~/.claude/skills/developing-software/references/library/<slug>
   cp <slug>/<slug>.md ~/.claude/skills/developing-software/references/library/<slug>/raw.md
   ```
   No copies `media/` ni ninguna imagen — quedan en `<slug>/` junto al `.epub` (paso 1), fuera de la skill. Los links de imagen que haya dentro de `raw.md` pueden quedar rotos si alguien lo abre suelto de esa carpeta; no importa, porque ningún flujo de consulta renderiza esas imágenes ni depende de que el link resuelva.

5b. **Crear el archivo de seguimiento `history.md`, y espejarlo como tasks del agente.**
    Crea un archivo de seguimiento llamado `history.md` en la carpeta del libro (`references/library/<slug>/history.md`) con dos secciones fijas — mismo esquema para todos los libros:
    ```markdown
    # <Título del Libro>

    ## Progreso
    - [ ] Configuración inicial y copia de raw.md
    - [ ] Detección de capítulos
    - [ ] Procesar Capítulo 1 — modelo: —
    - [ ] Procesar Capítulo 2 — modelo: —
    ... (listar todos los capítulos, cada uno con su propio `— modelo: —`)
    - [ ] Ensamblado de book.md, summary.md y examples.md
    - [ ] Actualización de catalog.md

    ## Historial
    ```
    **Progreso** es la checklist operativa de la ingesta en curso — sirve para reanudar sin perder el hilo si algo se interrumpe a mitad de camino (falla un `agent()`, se corta la sesión). **Historial** arranca vacío y es el log append-only de cambios hechos a este libro a lo largo del tiempo (ingesta inicial, backfills, correcciones, re-ingestas de un capítulo): cada línea nueva se agrega, nunca se edita ni se borra una anterior, con el formato `- <fecha> — <descripción> — modelo: <modelo>` (ver paso 11 para la primera entrada).

    Además, si tienes disponible un tool de tasks (`TaskCreate`/`TaskUpdate`/`TaskList`), crea con `TaskCreate` una task por cada línea de la lista de Progreso (una por la configuración inicial, una por la detección de capítulos, una por cada capítulo, una por el ensamblado, una por la actualización del catálogo). El archivo `history.md` es el registro durable — sobrevive a esta sesión y es lo que se audita después si hay que reconstruir algo puntual; las tasks son el reflejo en vivo de esa misma checklist mientras dura la ingesta, para que el progreso se vea en el harness sin tener que reabrir el archivo.

    A medida que se completen los subagentes y los pasos del flujo, mantén ambos en sincronía: cambia `[ ]` por `[x]` en la sección Progreso del archivo, y usa `TaskUpdate` (`status: in_progress` al empezar cada paso, `status: completed` al terminarlo) en la task correspondiente. En cada capítulo, reemplaza el `—` de `modelo:` en el archivo por el identificador del modelo real que efectivamente lo resumió en el paso 6 en el entorno en ejecución (por ejemplo, `gemini-3.5-flash` para entornos Gemini, o `haiku`/`sonnet` si se está usando una suite Claude real), y anota lo mismo en la task con `TaskUpdate` (`metadata: {"modelo": "<modelo_real>"}`) al marcarla completed — así queda un registro auditable (en el archivo y en vivo en las tasks) del modelo real ejecutado y en qué se gastó más presupuesto, útil si después hay que reconstruir solo los capítulos que salieron con un modelo más caro.

6. **Genera resúmenes profundos y ejemplos de cada capítulo en paralelo, usando el tool `Workflow`.**
   Llama a `Workflow` con un script que recorra el manifiesto de capítulos (o el libro completo como único ítem, si no se dividió en el paso 3) y lance un `agent()` por capítulo dentro de `parallel()` — no hay dependencia entre capítulos, así que no hace falta `pipeline()`:
   ```js
   export const meta = {
     name: 'summarize-book-chapters',
     description: 'Resumen profundo + ejemplos por capítulo de un libro de la biblioteca',
     phases: [{ title: 'Summarize' }],
   }
   const results = await parallel(chapters.map(ch => () =>
     agent(promptFor(ch), { schema: CHAPTER_SCHEMA, model: 'haiku', phase: 'Summarize', label: ch.title })
   ))
   return results
   ```
   **`chapters` debe ser un array literal incrustado directamente en el script, no pasado vía el parámetro `args` del tool `Workflow`.** En la práctica, `args` puede llegar al script serializado como string en vez de array y romper `chapters.map is not a function` — ya pasó en una ingesta real. Escribe el manifiesto completo (el JSON que imprimió `split_chapters.py`) como un `const chapters = [ ... ]` dentro del cuerpo del script.

   **Si el entorno no ofrece el tool `Workflow`,** procesa los capítulos con los subagentes que sí tenga disponibles el harness (en paralelo si es posible, secuencial si no) — el resto del procedimiento no cambia: mismo esquema `CHAPTER_SCHEMA`, mismo modelo económico por defecto, mismas verificaciones de rango.

   `CHAPTER_SCHEMA` pide un objeto `{ synopsis: string, summary: string, examples: string }` — evita depender de que el subagente respete un formato de texto plano con marcadores.

   **Modelo por defecto: `haiku`.** Prioriza el consumo de tokens sobre el matiz técnico — todos los capítulos se resumen con Haiku salvo excepción puntual. Solo escala un capítulo puntual a `model: 'sonnet'` (reintentando solo ese `agent()`, nunca el libro entero) si el usuario lo pide explícitamente, o si el resumen que devolvió Haiku queda claramente por debajo de la densidad pedida.

   **CRÍTICO - Profundidad del resumen:**
   El `summary` de cada capítulo debe ser **muy detallado e instructivo (ocupando entre el 30% y el 50% de las líneas del capítulo original)**. No debe ser una simple descripción ejecutiva de un párrafo. Debe retener:
   - Explicaciones minuciosas de la lógica del diseño.
   - Trade-offs detallados y decisiones arquitectónicas.
   - Explicaciones de diagramas en prosa y flujo de datos.
   - Nombres específicos de todas las clases y funciones involucradas.

   Esta densidad es la que permite que los flujos de consulta citen capítulo, patrón y trade-off exactos sin tener que recargar `raw.md` completo — un resumen ejecutivo de un párrafo no sostiene esa precisión.

   **CRÍTICO - El `synopsis` es el nivel corto, no un resumen ejecutivo del `summary`.**
   Debe ocupar **entre 3 y 10 líneas**, sin importar cuán largo sea el capítulo — ni una línea menos (perdería utilidad como resumen) ni una línea más (dejaría de ser distinguible del `summary` profundo, y perdería su propósito de lectura rápida). Debe alcanzar para que alguien decida, sin leer más, si ese capítulo es relevante para su pregunta: de qué trata, qué patrón/principio/problema central aborda, y qué conclusión o postura central sostiene el autor — sin entrar en el detalle de trade-offs o nombres de clases que sí van en `summary`. Igual que en `summary`, si el capítulo no tiene contenido de autor (portada, índice, divisor de parte), dilo explícitamente en 1-2 líneas en vez de forzar 3-10 líneas de relleno.

   **CRÍTICO - No te salgas del rango de líneas.** El `promptFor(ch)` debe instruir explícitamente al `agent()` a leer *solo* `ch.start_line`–`ch.end_line` y a no leer más allá aunque el contenido parezca insuficiente. Los divisores de parte/sección (capítulos de pocas líneas que son solo marcado de pandoc sin prosa) son comunes, y un subagente puede "compensar" leyendo el capítulo siguiente y resumiendo ese en su lugar — ya ocurrió en una ingesta real con un divisor de 8 líneas que terminó duplicando el capítulo contiguo. Si el rango no tiene contenido sustantivo, el `agent()` debe decirlo explícitamente en `synopsis` y en `summary` (2-4 líneas basta en cada uno) en vez de rellenar con contenido ajeno al rango.

   **CRÍTICO - Sin encabezados markdown propios.** Instruye al `agent()` a no incluir sus propios `#`/`##`/`###` en `synopsis`, `summary` ni en `examples` — el título del capítulo ya se agrega una sola vez al ensamblar (paso 7), y un encabezado adicional por dentro del texto genera duplicados que ensucian la búsqueda por título que hace el protocolo de consulta.

   El campo `examples` debe traer fragmentos de código completos, casos de estudio, o diagramas de patrones descritos en prosa, preservando la sintaxis exacta. Si un capítulo no tiene ejemplos, que el propio `agent()` lo diga explícitamente en `examples` en vez de dejarlo vacío sin explicación.

   **CRÍTICO - Mantener el idioma original.** Si el libro está en español, el resumen y los ejemplos deben estar en español; si está en inglés, deben estar en inglés. No traduzcas ni adaptes el contenido a otro idioma. Los idiomas oficiales son inglés y español, si es necesario traducir debes pedir permiso al usuario, y preguntarle si lo quiere en español o inglés antes de hacerlo. Todos los prompts de `agent()` deben instruir explícitamente a mantener el idioma original o la traducción autorizada por el usuario.

    **Actualiza `history.md` (y su task espejo, si la creaste en el paso 5b) con el modelo real de cada capítulo** a medida que cada `agent()` resuelve: marca `[x]` y completa `— modelo: <modelo_real>` (indicando el identificador del modelo real ejecutado por la plataforma en el entorno actual, por ejemplo `gemini-3.5-flash`, y no los placeholders 'haiku' o 'sonnet' literalmente si el agente está corriendo en otra suite de LLMs) en el archivo, y en paralelo marca la task de ese capítulo como `completed` con `TaskUpdate` (`metadata: {"modelo": "<modelo_real>"}`). No lo dejes para el final ni lo infieras de memoria — si un capítulo se reintentó con otro modelo, el que quede anotado (en el archivo y en la task) debe ser el que realmente produjo el contenido final de ese capítulo.

   **CRÍTICO - Si un capítulo falla por bloqueo del filtro de contenido de la API** (el `agent()` devuelve un error tipo "Output blocked by content filtering policy" en vez de completar), el rango de líneas en sí casi nunca es problemático — en la práctica ha ocurrido con contenido técnico completamente benigno (ej. un capítulo sobre patrones de distribución con ejemplos de código Java/C#). No lo interpretes como una señal de que hay que censurar o resumir el capítulo de forma más vaga. En vez de eso:
   - Reintenta ese capítulo puntual dividiéndolo en 2 mitades por línea, y si vuelve a fallar, en 4 cuartos — nunca renuncies a resumir el capítulo completo ni lo saltees en silencio.
   - Cada fragmento adicional necesita su propio prompt con el rango de líneas exacto, igual de estricto que el prompt original (mismo idioma, mismo rango, misma prohibición de salirse de rango).
   - **No dejes que el reintento se convierta en una excusa para omitir código real en `examples`.** Un subagente que fue bloqueado una vez puede "sobrecorregir" y devolver solo descripciones en prosa de los ejemplos en vez de los fragmentos de código literal, para evitar disparar el filtro de nuevo — esto ya ocurrió en una ingesta real y dejó un capítulo entero sin una sola línea de código en `examples.md`, rompiendo la paridad con el resto del libro. Si eso pasa, extrae el código directamente de `raw.md` tú mismo (no vía el `agent()`) usando un script que localice los bloques de código en el rango del capítulo (busca patrones como "Click here to view code" seguido del bloque, delimitado por líneas en blanco) y limpia los artefactos de pandoc (backslashes de continuación de línea al final de cada línea, anchors `<span id="...">...</span>` incrustados a mitad de línea, escapes `\[`/`\]`/`\<`/`\>`) antes de insertarlo.
   - Al ensamblar los fragmentos de un mismo capítulo (paso 7), la numeración de los ejemplos debe quedar **continua a través de los fragmentos** (1, 2, 3... sin reiniciar a 1 en cada fragmento) — reiniciar la numeración a mitad de una lista, sin ningún separador que avise el cambio, es confuso para quien lea `examples.md` después y ya ocurrió en una ingesta real. Agrega también una nota breve al inicio de la sección del capítulo en `examples.md` explicando que se procesó en fragmentos (referenciando `history.md`), para que quien lo lea entienda por qué el capítulo tiene esa estructura.

7. **Ensambla `book.md`, `summary.md` y `examples.md` tú mismo.** Antepón un índice de capítulos —una lista con los mismos títulos y en el mismo orden del manifiesto de `split_chapters.py`— justo debajo del título del libro, antes del primer capítulo:
   ```markdown
   ## Índice de capítulos
   - [Título del capítulo 1](#título-del-capítulo-1)
   - [Título del capítulo 2](#título-del-capítulo-2)
   ...
   ```
   No hace falta que los anchors resuelvan perfectamente en todos los visores de markdown — el índice sirve igual como mapa de lectura. Debajo de él, concatena `results[i].summary` / `results[i].examples` bajo el título de cada capítulo (mismo título que en `raw.md`, para que después puedas cruzar de uno a otro) para armar `book.md` y `examples.md` respectivamente. Ensambla `summary.md` con el mismo esquema de índice + secciones por título de capítulo, pero usando `results[i].synopsis` en vez de `results[i].summary` — es el archivo que el protocolo de consulta lee primero, completo, para decidir en qué capítulo profundizar antes de tocar `book.md`. Escribe los tres archivos completos (no un fragmento) en:
   ```
   ~/.claude/skills/developing-software/references/library/<slug>/book.md
   ~/.claude/skills/developing-software/references/library/<slug>/summary.md
   ~/.claude/skills/developing-software/references/library/<slug>/examples.md
   ```

   **Antes de dar el ensamblado por bueno, revisa el largo de cada `summary` contra el tamaño de su rango de líneas.** Un capítulo de pocas líneas (p.ej. un divisor de parte de 8-20 líneas) con un `summary` desproporcionadamente largo es la señal de que el `agent()` se salió del rango y resumió el capítulo contiguo (ver nota del paso 6). Compáralo contra capítulos de tamaño similar: si dos divisores de 8 líneas dieron 500 y 14,000 caracteres respectivamente, el segundo probablemente esté mal — relanza solo ese capítulo con el prompt reforzado antes de continuar. Aplica la misma revisión a `summary.md`: cada `synopsis` debe caer dentro de 3-10 líneas — si un capítulo cortito quedó con 15+ líneas o un capítulo largo quedó en 1 línea, relanza ese capítulo puntual con el prompt reforzado.

8. **Sintetiza y agrega la entrada del catálogo — reescribiendo el archivo completo, no editando un fragmento.** Este paso es el que hace al libro consultable: el protocolo de consulta (SKILL.md) arranca leyendo `catalog.md`, así que hasta que esta escritura no ocurre, todo lo generado en los pasos 1-7 vive en `references/library/<slug>/` pero es invisible para Estudiando/Implementando/Refactorizando/Diseñando — por diseño, para poder ingerir sin bloquear ni ensuciar la consulta de otra sesión que esté usando la biblioteca en paralelo. Lee el `book.md` completo (ya lo tienes fresco) y escribe: un resumen de 5 a 10 líneas del libro completo, y de 4 a 8 tags seleccionados de la taxonomía estandarizada en inglés definida en la cabecera de `catalog.md` (como `software-architecture`, `design-patterns`, `code-quality-and-refactoring`, etc.). Lee el `catalog.md` actual, arma su contenido completo con la entrada nueva agregada al final, y escribe el archivo entero de una vez, sobrescribiéndolo por completo (no en modo append). El formato de cada entrada:

   ```markdown
   ## [Título del libro](<slug>/)
   **Resumen:** <cinco a diez líneas>
   **Tags:** tag1, tag2, tag3, tag4
   ```

9. **Vuelve a leer `catalog.md` (y de paso `book.md`) desde disco antes de decirle al usuario que terminaste — con una lectura nueva y separada, no reutilices el contenido que ya tenías en memoria.** Si la entrada no aparece completa en esa relectura nueva, no lo reportes como éxito: reintenta la escritura (si la escritura directa no está tomando el cambio, ejecutar un comando de shell o un script de Python que reescriba el archivo es una alternativa robusta) y vuelve a verificar antes de decir que terminaste.

9b. **Si algún capítulo de esta ingesta se fragmentó o reintentó** (ver nota del paso 6), ejecuta sobre él el **Subflujo: Auditoría de fidelidad** descrito al final de este documento antes de continuar al paso 10 — no lo dejes para después ni lo saltees porque "probablemente esté bien".

10. Confirma al usuario cuántos capítulos se detectaron y muéstrale la entrada del catálogo para que la valide — los tags y el resumen de 5 a 10 líneas son juicio del modelo, vale la pena que el usuario les eche un ojo.

11. **Cierra agregando una entrada a la sección Historial de `history.md`.** Nunca reemplaces ni edites una entrada previa — agrega una línea nueva al final con el formato `- <fecha> — <descripción> — modelo: <modelo>`: la fecha de hoy, una descripción breve (título del libro, cantidad de capítulos procesados) y el modelo que ejecutó *esta sesión* — el que detectó capítulos, lanzó el `Workflow`, ensambló `book.md`/`summary.md`/`examples.md` y actualizó el catálogo. Es distinto del `modelo:` anotado por capítulo en la sección Progreso (paso 6): aquel registra quién resumió cada texto, este registra quién orquestó el flujo completo, y cuándo.

## Subflujo: Auditoría de fidelidad

Este subflujo contrasta lo ya ensamblado (`book.md`/`summary.md`/`examples.md`) contra el texto fuente (`raw.md`) de un capítulo, buscando alucinaciones, omisiones y código no fiel al original. Nace del paso 9b, pero **no depende de estar en medio de una ingesta**: es invocable de forma independiente, en cualquier sesión futura, sobre cualquier libro ya guardado en la biblioteca — el usuario puede pedirlo directamente ("auditá el capítulo X de \<libro\>", "revisá si el capítulo fragmentado de \<libro\> sigue teniendo sentido", "contrastá esto con el raw") sin que haya una ingesta activa ni que el capítulo se haya tocado en la sesión actual.

**Cuándo se activa:**
- **Automático:** paso 9b de este documento, para todo capítulo recién fragmentado o reintentado en la ingesta en curso.
- **Bajo demanda:** el usuario lo pide sobre un libro/capítulo que ya está en `catalog.md`, sin importar cuándo se ingirió ni si fue en esta sesión u otra. Es el caso típico de un capítulo marcado en `history.md` como fragmentado (busca en la sección Progreso o Historial del libro anotaciones tipo "dividido en N fragmentos", "reintentado", "bloqueado por filtro de contenido") que nunca llegó a auditarse, o de cualquier capítulo sobre el que el usuario quiera una segunda verificación aunque no haya tenido problemas conocidos.

**Cómo ubicar lo que hay que auditar** (si no viene ya identificado en el pedido del usuario):
1. Localiza el libro en `catalog.md` y su `slug`.
2. Lee `references/library/<slug>/history.md` — la sección Historial suele decir qué capítulo se fragmentó o reintentó y por qué.
3. Ubica el rango de líneas del capítulo en `raw.md` buscando su título con grep (mismo título que usan `book.md`/`summary.md`/`examples.md`).

**Pasos:**
1. Lee el texto fuente completo del capítulo en `raw.md` (rango de líneas ubicado arriba). Si es muy largo (varios cientos de líneas), está bien leerlo en 2-3 tandas con `Read`/offset-limit.
2. Lee las secciones ya ensambladas de ese mismo capítulo en `book.md`, `summary.md` y `examples.md` (búscalas por el título del capítulo).
3. Lanza un `agent()` (puede correr en background mientras seguís con otra cosa) con ambos textos — fuente y ensamblado — y pídele explícitamente que reporte:
   - **Alucinaciones:** afirmaciones, citas, nombres de clases/patrones o conclusiones atribuidas al autor que no están respaldadas por el rango fuente dado — presta especial atención a contenido que suene plausible pero en realidad pertenezca a *otro* capítulo del mismo libro (contaminación por conocimiento general del subagente que resumió).
   - **Omisiones relevantes:** contenido sustantivo del original que falta en el resumen, en particular cerca de los puntos de corte si el capítulo fue fragmentado (ahí es donde más se pierden frases de cierre o conclusiones).
   - **Tergiversaciones:** simplificaciones que cambian el sentido original, no solo que sean imprecisas.
   - **Fidelidad de citas textuales:** toda frase entre comillas presentada como cita debe coincidir literal o casi literalmente con el original, no ser una paráfrasis disfrazada de cita.
   - **Fidelidad del código** en `examples.md`: los fragmentos deben ser código real extraído de `raw.md`, nunca código "reconstruido de memoria" por un subagente — y el capítulo debe tener código en absoluto si el original lo tiene (un capítulo reducido a solo descripciones en prosa, sin un solo bloque de código, es en sí mismo un hallazgo que reportar).
4. Aplica las correcciones que encuentre editando directamente `book.md`/`summary.md`/`examples.md` — no reinicies el capítulo completo desde cero salvo que el problema sea extenso. Si falta código real en `examples.md`, extráelo tú mismo de `raw.md` (no vía `agent()`) localizando los bloques de código en el rango del capítulo y limpiando artefactos de pandoc (backslashes de continuación de línea, anchors `<span id="...">...</span>` incrustados a mitad de línea, escapes `\[`/`\]`/`\<`/`\>`).
5. Deja constancia en la sección Historial de `history.md` del libro: qué capítulo se auditó, qué se encontró y qué se corrigió (formato `- <fecha> — <descripción> — modelo: <modelo>`, igual que cualquier otra entrada de Historial) — aunque la auditoría no encuentre nada que corregir, vale la pena registrar que se hizo y cuándo.
6. Reporta al usuario un resumen de los hallazgos (o su ausencia) con el mismo nivel de detalle que pediría una auditoría seria: qué se revisó, qué problemas había, qué se corrigió — no lo resumas en una frase genérica tipo "todo bien".
