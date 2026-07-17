# Flujo 4 — Refactorizando: mejorar o rehacer código existente

Se activa cuando hay código existente que mejorar o rehacer: "refactoriza este proyecto/clase/paquete/función", "este módulo quedó inmanejable", "quiero hacer esto de nuevo pero bien", "aplica tal patrón aquí". Es el flujo más riesgoso de la skill — se modifica código que ya funciona — así que es también el más ceremonioso: análisis, advertencia de tests, preguntas, plan guardado, y recién entonces ejecución.

## Pasos

1. **Pregunta si usar un modelo más pesado para el análisis** (regla común de escalado, ver SKILL.md). Detectar los smells reales y elegir los refactors correctos es la parte que decide si el resultado mejora o solo cambia; la ejecución mecánica de los movimientos no necesita el modelo fuerte.

2. **Lee el código señalado y consulta los libros.** Nombra los smells con la nomenclatura de Fowler (Long Method, Feature Envy, Shotgun Surgery, Divergent Change…) — nombrarlos exactos permite ir a buscar el refactor correspondiente en la biblioteca en vez de improvisar. Con el protocolo de consulta, busca el refactor o patrón destino: qué movimiento resuelve cada smell, qué precauciones señala el autor, y si `examples.md` trae un caso análogo.

3. **Advierte sobre los tests antes de comprometerte con el plan.** Un refactoring correcto exige una red de tests que garantice que el comportamiento no cambia — es la advertencia central de Fowler: sin tests no hay forma de distinguir "refactoricé" de "rompí y no me di cuenta". Verifica si el código afectado tiene tests y díselo al usuario explícitamente:
   - **Hay tests:** se corren antes de empezar (línea base) y tras cada movimiento.
   - **No hay tests:** propón escribir primero el mínimo de tests de caracterización (los que fijan el comportamiento actual, correcto o no, para detectar cualquier cambio), o que el usuario acepte explícitamente proceder bajo su riesgo. No avances al paso siguiente sin una de las dos.

4. **Haz preguntas al usuario para afinar el enfoque**, basadas en lo que extrajiste de los libros — no genéricas. Si el análisis abrió alternativas reales (¿extraer una clase o mover los métodos?, ¿refactor incremental o rehacer el módulo?), pregunta por las restricciones que las deciden: qué partes no se pueden tocar, cuánto puede cambiar la interfaz pública, si hay deadline que favorezca lo incremental.

5. **Entrega el plan completo y guárdalo en `.claude/plans/` del proyecto** (plan antes de código, regla común). Crea la carpeta si no existe; nombra el archivo con un slug descriptivo y la fecha (`2026-07-10-extraer-servicio-pagos.md`). El plan lista los movimientos en orden, con el porqué de cada uno (qué smell resuelve, qué dice la fuente), e incluye un **checklist de progreso** con la misma lógica de la ingesta: una línea `- [ ]` por movimiento en el archivo, más tasks espejo del harness (`TaskCreate`/`TaskUpdate`) si están disponibles. El archivo es el registro durable que sobrevive a la sesión; las tasks son el reflejo en vivo. El usuario aprueba el plan antes de tocar código.

6. **Delega el refactoring a un modelo más simple** (regla común de escalado): un subagente con el plan como spec, ejecutando en pasos pequeños — un movimiento, correr los tests, marcar `[x]` en el checklist y actualizar la task, siguiente movimiento. Si un test falla, se detiene y se revisa ese movimiento antes de seguir; no se acumulan movimientos sin verificar. Si el harness no permite delegar con otro modelo, ejecuta en la sesión actual con la misma disciplina y avísalo.

7. **Al entregar**, resume qué smells se resolvieron y con qué movimientos, el estado final de los tests, y cierra con la línea de fuentes.

## Encadenamientos frecuentes

- Una duda conceptual durante el análisis o la ejecución → consulta puntual vía Estudiando y se retoma.
- Si el diagnóstico revela que el problema no es el código sino el diseño del sistema (la estructura de módulos, los límites entre contextos) → decláralo y propón pasar a Diseñando antes de mover código.
- Si el pedido nació como pregunta en Estudiando ("¿esto está bien?") y el usuario pide arreglarlo → confirma el alcance antes de entrar aquí: feedback sobre tres archivos no autoriza refactorizar el paquete entero.
