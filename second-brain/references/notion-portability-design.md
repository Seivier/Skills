# Diseño: portabilidad de second-brain vía Notion

Fecha: 2026-07-13
Estado: aprobado por el usuario, pendiente de implementación (ver `writing-plans`)

## Problema

`second-brain` vive hoy como archivos locales bajo `~/.claude/second-brain/`
(`profile.json`, `todos.json`, `todos-archive.json`, `research/*.md`) manipulados
por scripts Python (`todo.py`, `profile.py`) que solo Claude Code puede ejecutar.
Esto funciona en la terminal de esta máquina, pero no es usable desde:

- Otro PC con Claude Code (ej. PC de la pega) — sin sync de datos hoy (el backup
  a iCloud actual ni siquiera incluye `second-brain/` en lo que respalda).
- claude.ai en navegador — no tiene acceso al filesystem local ni ejecuta scripts.
- La app móvil de Claude — mismo problema que el navegador.

Objetivo: una sola fuente de verdad accesible, con lectura y escritura completas,
desde las 4 superficies (terminal, PC de la pega, navegador, celular), sin pagar
ni mantener un servidor propio.

## Opciones descartadas (y por qué)

- **Servidor MCP propio (Cloudflare Workers + KV/D1)**: técnicamente la opción
  más "limpia" (fuente única, validación de esquema propia), pero implica
  hostear y mantener infraestructura — descartada porque el usuario prefiere no
  operar un servidor propio aunque sea gratuito.
- **Sync bidireccional local↔remoto (estilo backup actual)**: mismo problema que
  ya tiene el backup a iCloud hoy — "gana el último guardado, no fusiona" — dos
  copias que se pueden pisar. Descartada por introducir el mismo riesgo que se
  busca eliminar.
- **Artifact de Claude como backend**: sin hosting, pero (a) la CSP de los
  artifacts bloquea cualquier `fetch`/`XHR`, así que no hay escritura real desde
  JS del navegador — la única escritura posible es que Claude reescriba y
  republique el artifact completo en cada cambio; (b) eso implica traer y
  reenviar el contenido entero por cada edición chica (costoso en tokens); (c) no
  hay ninguna validación de esquema — Claude edita la estructura a mano en cada
  actualización; (d) incertidumbre sobre si la app móvil soporta leer/actualizar
  artifacts igual que web/desktop. Descartada por el costo en tokens y la
  pérdida total de validación.
- **`localStorage`/`IndexedDB` dentro de un artifact-webapp**: descartada de
  entrada — es almacenamiento por dispositivo/navegador, no sincroniza entre
  superficies, que es justo el objetivo. Además no hay garantía de que persista
  ni siquiera entre recargas en un mismo dispositivo (origen del iframe
  sandboxeado potencialmente inestable entre renders).

## Decisión: Notion + su MCP oficial remoto

- **Almacenamiento**: un workspace de Notion (plan free). Para un workspace de
  un solo miembro, Notion no limita bloques/páginas (el límite de 1000 bloques
  solo aplica con 2+ miembros) — ver
  [Understanding block usage](https://www.notion.com/help/understanding-block-usage).
  Otros límites del free tier no son relevantes acá: 10 guests solo-lectura,
  archivos de hasta 5MB, historial de versiones de 7 días (única pérdida real
  frente a git, que da historial ilimitado).
- **API**: ~3 requests/segundo promedio, tope de 1000 requests/5min por
  workspace, payloads de hasta 500KB/1000 bloques por request — ver
  [Notion API request limits](https://developers.notion.com/reference/request-limits).
  Muy por encima del volumen de uso de esta skill.
- **Acceso**: el MCP oficial y remoto de Notion, hosteado por ellos en
  `https://mcp.notion.com/mcp` — ver
  [Notion MCP Server](https://github.com/makenotion/notion-mcp-server) y
  [Connecting to Notion MCP](https://developers.notion.com/guides/mcp/get-started-with-mcp).
  Auth es OAuth por cliente (no soporta bearer token fijo); se autoriza una vez
  por instalación/dispositivo, costo aceptado por el usuario.
- **La skill `second-brain`** deja de invocar `todo.py`/`profile.py` sobre JSON
  local, y en su lugar instruye a Claude para operar directamente sobre el
  workspace de Notion vía las tools del MCP (buscar, leer página/bloques, crear
  página, actualizar propiedades, agregar bloques, consultar base de datos).

## Esquema en Notion

### Perfil (árbol de nodos) → jerarquía nativa de páginas

El modelo actual `{name, desc, info, childs}` se traduce directo a la jerarquía
de páginas de Notion, sin base de datos intermedia:

- Página raíz "Perfil" con 6 sub-páginas fijas: `salud`, `emocional`,
  `proyectos`, `trabajo`, `academico`, `general`.
- **Cada nodo del árbol = una página de Notion**, anidada bajo su nodo padre
  (misma profundidad libre que hoy).
  - `name` → título de la página.
  - `desc` → primer bloque de la página (*callout* en itálica, "Resumen: ...")
    — así las operaciones tipo `tree`/`list` (que hoy no cargan `info`) piden
    solo título + ese primer bloque, no la página completa.
  - `info` → resto del contenido (párrafos de texto plano). Misma disciplina de
    hoy: ramificar en sub-páginas cuando el contenido crece o mezcla temas, en
    vez de estructurarlo dentro de un solo bloque.
  - `childs` → sub-páginas anidadas, mismo shape recursivo.
- Equivalencias de comandos: `tree`/`list` → listar sub-páginas; `show` → leer
  bloques de una página puntual; `set` → crear/actualizar página y su
  contenido; `append` → agregar bloque al final; `rm` → archivar página.

### Notas e insights → bases de datos

- Base **"Notas"**: propiedades `Eje` (select), `Fecha` (created time), `Texto`
  (rich text), e **`ID` nativo de Notion** (propiedad tipo ID, autoincremental,
  con prefijo — ej. `NOTE-7`) — reemplaza el contador manual que hoy vive en
  `profile.py`. Las citas tipo "ver nota salud#5" pasan a citar este ID nativo.
- Base **"Insights"**: mismo shape, sin `Eje` (transversal al perfil, como hoy).

### Todos → base de datos

Base **"Todos"**: propiedades `Fecha` (date), `Tags` (multi-select:
tesis/trabajo/personal), `Estado` (select: pendiente/en_progreso/bloqueada/
hecha/cancelada). Sin base de datos separada para archivo — al no haber límite
de bloques, hecha/cancelada quedan filtradas en una vista en vez de migrar a
otro storage (`todos-archive.json` deja de ser necesario).

### Investigación → páginas

Página padre "Research" con una sub-página por tema (reemplaza cada
`research/*.md`). El `index.md` manual deja de ser necesario — Notion ya lista
las sub-páginas y tiene buscador de texto completo nativo.

## Migración (script único, se descarta después de usarse)

Script Python con un *integration token* interno de Notion (se crea gratis en
`notion.so/my-integrations`, se comparte una vez con el workspace destino):

1. Crea la página raíz "Perfil" y sus 6 sub-páginas de eje.
2. Recorre `profile.json` recursivamente, creando una sub-página de Notion por
   nodo (título, callout de `desc`, contenido `info`).
3. Crea las bases "Notas", "Insights", "Todos" con su schema (incluida la
   propiedad `ID` nativa).
4. Migra notas/insights/todos (+archive) a filas de esas bases.
5. Crea "Research" con una sub-página por archivo `.md` existente.
6. Anota los IDs de páginas/bases raíz (permanentes) para referenciarlos desde
   la skill sin tener que buscarlos por nombre en cada operación.

Los JSON/MD locales **no se borran** — quedan como respaldo congelado dentro de
`~/.claude/second-brain/` (marcados como obsoletos, ya no la fuente de verdad).

## Despliegue por superficie

- **Terminal / PC de la pega (Claude Code)**: `SKILL.md` se reescribe
  reemplazando la tabla de comandos CLI por instrucciones de tools MCP de
  Notion, e incluye la tabla de IDs de páginas/bases fijos (capturados en la
  migración). Se instala/sincroniza igual que hoy (vía la skill `backup`).
  Requiere una vez por instalación: `claude mcp add --transport http notion
  https://mcp.notion.com/mcp` + autorizar OAuth en el navegador.
- **claude.ai web/celular**: no existe "instalar skill" ahí. Se crea un
  **Project** en claude.ai (ej. "Segundo cerebro") con el connector de Notion
  habilitado, y como instrucciones del proyecto una versión condensada del
  `SKILL.md` (sin rutas locales, con la misma tabla de IDs). A confirmar en la
  práctica si la app móvil hereda el connector con la misma cuenta o pide una
  autorización propia ahí también.

## Alcance de esta migración (fuera de este spec)

- No se resuelve en este documento el detalle exacto de qué tools del MCP de
  Notion mapean a cada operación (`tree`/`list`/`show`/`set`/`append`/`rm`,
  `note`/`notas`/`rm-nota`, `insight`/`insights`/`rm-insight`, `todo add/list/
  done/set/rm/delays`) — eso se define en el plan de implementación.
- No se resuelve el texto final del `SKILL.md` reescrito ni el de las
  instrucciones condensadas para el Project de claude.ai — también parte del
  plan de implementación.
- No se resuelve si `todos-archive.json` y `research/index.md` se eliminan del
  repo de la skill tras confirmar la migración, o quedan indefinidamente como
  respaldo — decisión a tomar una vez migrado y verificado en Notion.
