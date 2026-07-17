# Flujo 2 — Estudiando: preguntas, estudio y feedback (sin producir código)

Se activa cuando el usuario quiere **entender**, no que se le haga el trabajo:

- Aprender un concepto: "¿qué es un agregado en DDD?", "explícame la diferencia entre Factory Method y Abstract Factory".
- Comparar autores o enfoques: "¿en qué difieren Fowler y Evans sobre la capa de servicio?".
- Armar un plan de estudio o pedir preguntas de repaso sobre un tema o capítulo.
- **Estudiar sobre el propio código del proyecto**: "¿por qué crees que esto está implementado así?", "¿esto está correcto?", "¿qué principios me sirven para hacer esto?", "¿qué patrón es este?".

## Regla dura: este flujo no escribe ni modifica código

La salida de Estudiando es siempre explicación, diagnóstico o material de estudio — nunca un diff. La regla existe porque quien pregunta para aprender quiere el razonamiento, no que se lo resuelvan: entregar código a medio pedir diluye la explicación y le quita al usuario la oportunidad de hacerlo él mismo con criterio. Si en medio de la conversación el pedido muta a "hazlo" (impleméntalo, refactorízalo, redacta el documento), di explícitamente que cambias de flujo y sigue el que corresponda (Implementando, Refactorizando o Diseñando).

Este es el único flujo que no pregunta por escalado de modelo: es consulta directa a la biblioteca, se responde en la sesión actual.

## Cómo responder

1. **Aplica el protocolo de consulta de la biblioteca** (ver SKILL.md) hasta el nivel que la pregunta exija: una duda puntual suele resolverse con `summary.md` + la sección relevante de `book.md`; una discusión fina de trade-offs puede requerir verificar contra `raw.md` si queda duda de que el resumen realmente diga lo que recuerdas.

2. **Para preguntas sobre el código del proyecto:** lee el código señalado solo para entenderlo y evaluarlo. Responde con el vocabulario de los libros — nombra smells, principios y patrones por su nombre exacto (no "algo tipo factory": "Factory Method" o "Abstract Factory", que son distintos) — y ancla cada observación a una ubicación concreta (archivo, clase, función). Di qué está bien y por qué, no solo qué está mal. La corrección, si corresponde, queda como recomendación: el diff es asunto de Refactorizando.

3. **Para pedidos de estudio, arma material anclado en la biblioteca:**
   - Un plan de estudio son capítulos concretos de libros concretos, en un orden justificado ("primero el cap. 4 de X porque introduce el vocabulario que el cap. 2 de Y da por sabido"), no una lista genérica de temas.
   - Las preguntas de repaso deben poder responderse con los capítulos citados; al corregir las respuestas del usuario, la corrección cita el capítulo que la respalda.
   - Explica progresivamente: primero la idea central, luego los matices y trade-offs, y ofrece profundizar antes de volcar todo de una vez.

4. **Cierra con la línea de fuentes** (regla del protocolo): qué vino de qué libro y capítulo, y qué es criterio general.

## Como flujo de apoyo

Los flujos Implementando, Refactorizando y Diseñando invocan Estudiando cuando surge una duda conceptual a mitad de tarea: se hace la consulta puntual a la biblioteca, se responde (o se incorpora la respuesta a la decisión en curso), y se retoma el flujo original donde iba. No hace falta anunciar ceremonia — basta con que la consulta siga este mismo protocolo y que la referencia quede en la línea de fuentes del entregable final.
