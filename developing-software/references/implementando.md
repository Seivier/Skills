# Flujo 3 — Implementando: función, clase o funcionalidad nueva

Se activa cuando hay que escribir código nuevo: "necesito una función que haga X", "una clase que represente A", "añadir la funcionalidad Z a la app". El valor de este flujo sobre implementar directo es que la decisión de diseño se toma con la biblioteca sobre la mesa y el usuario elige entre opciones justificadas — no descubre el diseño cuando ya está escrito.

## Pasos

1. **Pregunta si usar un modelo más pesado para la fase de diseño** (regla común de escalado, ver SKILL.md). La investigación en la biblioteca y la generación de opciones es la parte que más se beneficia de un modelo fuerte; la escritura del código, no tanto.

2. **Revisa las fuentes con el protocolo de consulta.** Identifica la decisión de diseño que el código va a encarnar (¿qué patrón de creación? ¿dónde vive la lógica de dominio? ¿cómo se desacopla la integración?) y busca qué dicen los libros sobre ella. `examples.md` es especialmente útil aquí: si hay un ejemplo del patrón, úsalo como referencia de forma — no lo copies, adáptalo al lenguaje y las convenciones del proyecto.

3. **Si faltan variables que cambian la decisión, resuélvelas antes de proponer**: escala esperada, restricciones de consistencia/latencia, vida útil del código, quién más lo va a tocar. Pregunta las que importen o declara el supuesto que estás tomando — recomendar sin ellas produce diseño genérico.

4. **Presenta una o más opciones de cómo proceder** (plan antes de código, regla común). Cada opción trae: el patrón o estructura propuesta, sus trade-offs, y su respaldo (libro + capítulo, o "criterio general" marcado como tal). Si hay una opción claramente superior puede ser una sola, pero cuando el trade-off es real (simplicidad hoy vs. extensibilidad mañana, por ejemplo) presenta las alternativas y **deja que el usuario decida** — usa AskUserQuestion con las opciones si está disponible. No escribas código hasta que haya elegido.

5. **Delega la implementación a un modelo más simple** (regla común de escalado): lanza un subagente con la opción elegida como spec — qué construir, qué patrón seguir, qué archivos tocar, y las convenciones de estilo del proyecto. El código debe leerse como el resto del codebase: mismo idioma de nombres y comentarios, misma densidad de comentarios. Nombra las piezas según el patrón solo cuando sea idiomático en ese entorno (una clase `OrderFactory`, sí; un sufijo `Strategy` en cada archivo, no necesariamente). Si el harness no permite delegar con otro modelo, implementa en la sesión actual y avísalo.

6. **Al entregar**, di qué patrón/estructura se aplicó, por qué ese y no la alternativa más cercana, y qué trade-off se aceptó. Cierra con la línea de fuentes.

## Encadenamientos frecuentes

- Una duda conceptual a mitad de implementación → consulta puntual vía Estudiando y se retoma.
- Si al abrir el código resulta que lo que hace falta no es agregar sino rehacer lo que hay → decláralo y cambia a Refactorizando.
- Si el pedido es más grande que una funcionalidad (un proyecto o módulo completo desde cero) → eso es Diseñando primero; este flujo ejecuta después su checklist ítem por ítem.
