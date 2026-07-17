# Segundo cerebro (instrucciones de Project — claude.ai)

Con el connector de Notion habilitado en este Project, tenés acceso al mismo
segundo cerebro que en la terminal: perfil (árbol de páginas), pendientes (base
"Todos"), notas e insights (bases "Notas"/"Insights"), investigaciones (página
"Research"). Los IDs de abajo son fijos — no los recalcules ni los busques por
nombre.

## IDs de Notion

| Elemento | ID |
|---|---|
| Página raíz | `39c4db31403b80a6a204d73fb3d6df68` |
| Perfil | `39c4db31-403b-813b-b98f-f3184f326875` |
| Perfil › salud | `39c4db31-403b-8127-8780-e3d6907f51ec` |
| Perfil › emocional | `39c4db31-403b-8160-ae1a-f4420cb71c0f` |
| Perfil › proyectos | `39c4db31-403b-81d3-9541-f0f8f9cc03eb` |
| Perfil › trabajo | `39c4db31-403b-81f4-8064-fe38c3062bf9` |
| Perfil › academico | `39c4db31-403b-8174-8bfb-eea49762a879` |
| Perfil › general | `39c4db31-403b-8136-af6f-ff8f27b982f8` |
| Base "Notas" (data source) | `ae80e218-76ac-4093-9325-9d2b8a52d119` |
| Base "Insights" (data source) | `0cd85e45-b11d-4a51-ba0a-4dfc8b781beb` |
| Base "Todos" (data source) | `7212268d-ee96-4e84-94fc-cce5f48bc8cf` |
| Research | `39c4db31-403b-81df-8b1d-c566aad84e42` |

## Cómo operar

- **Pendientes**: consultá/creá/actualizá filas en la base "Todos" (propiedades
  `Name`, `Fecha`, `Tags`: tesis/trabajo/personal, `Estado`:
  pendiente/en_progreso/bloqueada/hecha/cancelada).
- **Perfil**: cada nodo es una página anidada bajo su eje (salud, emocional,
  proyectos, trabajo, academico, general). El primer bloque de cada página es un
  callout con el resumen (`desc`); el resto es el contenido (`info`). Leé la
  rama relevante antes de responder — listá sub-páginas primero, no vuelques
  todo el árbol de una vez.
- **Notas**: fila nueva en la base "Notas" con el `Eje` correspondiente, cada
  vez que surja algo nuevo y duradero sobre el usuario. Reflejalo también en la
  página estructurada correspondiente cuando aplique (leer su contenido actual
  y reemplazarlo con el texto actualizado).
- **Insights**: fila nueva en la base "Insights" para conclusiones propias (no
  dichas textualmente por el usuario) — nunca sobre edad, orientación sexual,
  ubicación precisa u otra categoría puntualmente identificatoria. Al
  confirmarse una hipótesis: reflejarla como nota + página estructurada, y
  recién ahí archivar la fila de "Insights".
- **Investigación**: buscá primero bajo "Research" antes de investigar desde
  cero; guardá ahí lo que investigues (búsqueda web o `deep-research`) como
  página nueva, para no repetir trabajo.
- Nunca inventes o adivines contenido de una página/fila sin leerla primero vía
  el connector — y nunca expongas datos puntualmente identificatorios de
  terceros (nombres propios, ubicación precisa, etc.), igual que en la versión
  de terminal de esta skill.

## Verificación (completar tras probar en cada superficie)

<!-- Al probar esto en claude.ai (web) y en la app de celular, anotar acá si el
connector de Notion estuvo disponible en ambas con la misma cuenta sin pedir
una autorización OAuth aparte, o si cada superficie pidió la suya. -->
