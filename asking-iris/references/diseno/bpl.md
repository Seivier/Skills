# Cómo explicar una clase BPL (Business Process visual)

Un `Ens.BusinessProcessBPL` no tiene lógica ObjectScript escrita a mano: toda su lógica vive en el `XData BPL` como un flujo visual (el mismo que se ve al abrir la clase en el editor gráfico del Management Portal / Studio). Explicarlo bien significa reconstruir en prosa lo que ese editor muestra gráficamente — no listar el XML tal cual. Usar siempre esta estructura, en este orden:

## 1. Identificación

- Tipo (`Ens.BusinessProcessBPL`) y de qué se compone la clase (solo `XData BPL`, sin métodos manuales, salvo que los haya — si los hay, mencionarlos aparte).
- `request`/`response` del `<process>`: qué clase de mensaje entra y cuál sale, con sus campos si son pocos (si son muchos, resumir por tipo de dato que representan, no listar los 26 uno por uno salvo que el usuario lo pida).

## 2. Contexto (`<context>`)

Listar cada `<property>` del contexto y, para cada una, dos cosas:
- Qué guarda (con su `initialexpression` si es relevante — sobre todo si es un literal hardcodeado tipo credenciales).
- **Para qué se usa después** — si una variable de contexto se llena en un paso y nunca se lee en ninguno de los siguientes (`response.X` no le hace referencia ni ningún `<call>` posterior la usa como `callrequest.Y`), decirlo explícitamente como hallazgo ("dato curioso: se llena pero no se vuelve a usar" — puede ser resto de una versión anterior del proceso). No asumir que toda variable de contexto tiene un propósito activo solo por estar declarada.

## 3. Secuencia de actividades

Recorrer el `<sequence>` (o las ramas si hay `<branch>`/`<if>`) en orden y, por cada `<call>` (o `<code>`, `<transform>`, etc.), reportar:

- **Nombre** de la actividad y **target** (el `Name` del config item de la Production que recibe la llamada — no la clase BO/BP en sí, ya que el mismo target puede reutilizar una clase BO genérica con distinto Setting).
- **Tipo de request/response** de esa llamada puntual.
- **Mapeo de entrada**: qué campos de `request`/`context`/un `<call>` anterior alimentan el `callrequest` de esta llamada.
- **Mapeo de salida**: qué campos de `callresponse` terminan en `response` (la salida final del proceso) y cuáles terminan en `context` (para alimentar un `<call>` posterior).
- **Dependencias entre pasos**: señalar explícitamente cuando un paso depende del resultado de uno anterior (ej. "usa `context.IDPaciente`, llenado en el paso 1") — es la parte que en el editor visual se ve como una flecha entre cajas y que en prosa hay que hacer explícita.
- Si es `async='0'` (síncrono) vs `async='1'` — decirlo, porque cambia si el proceso espera la respuesta antes de seguir.

## 4. Puntos a marcar (siempre revisar, no solo si se ven a simple vista)

- **Credenciales o secretos hardcodeados** en el BPL (`initialexpression` con contraseñas/usuarios) en vez de vivir en Settings de la Production — marcarlo como hallazgo de seguridad.
- **Config items de Production de los que depende** (todos los `target` usados) — recordar que documentarlos va en un `.md` aparte, nunca leyendo/creando la Production real (ver regla en `productions-bs-bp-bo.md`).
- **Manejo de errores/compensación**: si el BPL no tiene `<catch>`/`<compensate>` visible, decir explícitamente que no hay lógica de manejo de fallos definida — importa para migración porque si cualquier `<call>` síncrono falla, no hay compensación.
- **Reescritura de valores**: cuando dos pasos escriben a la misma variable de contexto o folder de respuesta con datos distintos (ej. un `<call>` llena `context.DescLocal` y otro llena `response.CTLOCDesc` con información similar pero de otra fuente) — aclarar si es una colisión real o solo una coincidencia de nombres sin conflicto.

## 5. Diagrama (cuando el usuario lo pide o ayuda a la claridad)

El editor visual de BPL en el Management Portal muestra el `<sequence>` como una columna vertical de cajas redondeadas (una por actividad), conectadas por flechas de arriba hacia abajo, con ramas (`<branch>`) abriéndose en columnas paralelas. Para reproducir esa lectura en un artifact, usar un flowchart de Mermaid (`flowchart TD`) con:

- Una caja de inicio (`Start`) y una de fin (`End`).
- Un `subgraph` por cada `<call>`, con el nombre de la actividad y el target como título, y dentro dos nodos: el mapeo de request (qué entra) y el de response (qué sale) — así se ve, igual que en el inspector del editor real al hacer clic en una actividad, sin tener que abrir cada una por separado.
- Conectores entre los `subgraph` en el mismo orden que el `<sequence>`.
- Si hay contexto relevante para el flujo (credenciales, IDs que viajan de un paso a otro), un nodo o nota aparte conectado con línea punteada al paso donde se usa, en vez de mezclarlo dentro de las cajas de actividad.

No hace falta un diagrama para cada explicación de BPL — solo cuando el usuario lo pide explícitamente o cuando el proceso tiene ramas/loops que son más claras en dibujo que en prosa (un `<sequence>` lineal de 2-3 pasos casi siempre alcanza con la lista de la sección 3).

Fuente: patrón de documentación derivado empíricamente al explicar `Custom.CERO.BP.NuevoDetalleCita` (proyecto de migración HOSMIL, 2026-07-15) — no es un formato dictado por InterSystems, es una convención de este proyecto para hacer legible en texto lo que el editor BPL muestra gráficamente.
