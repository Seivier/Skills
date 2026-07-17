# Flujo 5 — Diseñando: proyectos, rediseños e ideas de aplicación

Se activa cuando el entregable es una decisión de diseño documentada, no código: "quiero diseñar un proyecto que haga X", "quiero rediseñar este sistema", "tengo una idea de aplicación", o cuando el equipo necesita un documento de diseño o ADR para discutir. Es el flujo que más conversación requiere: la mayor parte del valor está en las preguntas, porque una idea sin aterrizar produce una arquitectura genérica que no le sirve a nadie.

## Pasos

1. **Pregunta si usar un modelo más pesado para el diseño** (regla común de escalado, ver SKILL.md). Es la fase de mayor apalancamiento de toda la skill — una decisión de arquitectura equivocada cuesta meses; aquí es donde más se justifica el modelo fuerte.

2. **Revisa los libros según el dominio del problema** con el protocolo de consulta: si la idea es una integración entre sistemas, los patrones de integración; si es un dominio de negocio rico, DDD; si la duda es de estructura y dependencias, arquitectura. No esperes a tener todas las respuestas del usuario — lo que leas aquí alimenta las preguntas del paso siguiente.

   **Referencia recomendada para la decisión de estilo arquitectónico:** *Fundamentals of Software Architecture* (Ford & Richards), cap. 18 ("Decision Criteria") trae el framework más directo de la biblioteca para esta decisión — 6 áreas a resolver antes (dominio, characteristics, datos, factores organizacionales, madurez de proceso/equipo, isomorfismo dominio-arquitectura) y 3 decisiones que se derivan (¿monolito o distribuido?, ¿dónde viven los datos?, ¿comunicación síncrona o asíncrona?). Útil como checklist de las preguntas del paso 3 cuando el proyecto involucra elegir o justificar un estilo.

3. **Haz bastantes preguntas, informadas por lo que leíste.** El objetivo es entender la naturaleza de la idea y aterrizar el proyecto, y las buenas preguntas salen del conocimiento: si el libro dice que la decisión entre consistencia fuerte y eventual define la arquitectura, pregunta por la tolerancia a datos desactualizados; si el dominio parece tener subdominios, pregunta dónde están los límites naturales del negocio. Cubre al menos: qué problema resuelve y para quién, escala esperada (usuarios, datos, equipo), restricciones duras (plataforma, integraciones existentes, presupuesto, plazos), vida útil esperada, y qué es lo mínimo que tendría que existir para que el usuario lo considere vivo. Pregunta en tandas cortas (AskUserQuestion si está disponible), no las veinte de una vez.

4. **Presenta el documento de diseño** (plan antes de código, regla común) y guárdalo en el proyecto — `.claude/design/<slug>.md` por defecto, o donde el usuario indique. Estructura (usa esta plantilla salvo que el equipo del usuario ya tenga una propia):

   ```markdown
   # [Nombre del proyecto o decisión]
   ## Contexto
   El problema, los usuarios, las restricciones y los supuestos declarados.
   ## Decisión
   La arquitectura o diseño propuesto, con sus componentes y responsabilidades.
   ## Alternativas consideradas
   Cada una con sus trade-offs y su respaldo (libro + capítulo, o criterio general).
   ## Consecuencias
   Lo que se gana, lo que se paga, y qué señal obligaría a revisar la decisión.
   ## Fuentes
   ```

   Un documento de diseño es tan bueno como la honestidad con la que trata a las alternativas descartadas: consulta la biblioteca por *cada* alternativa relevante, no solo por la ganadora, y pon las citas junto a lo que respaldan (en cada alternativa y trade-off) — la sección Fuentes solo recapitula.

5. **Ofrece la implementación vía Implementando.** Si el usuario acepta: deriva del documento un checklist/todo — un archivo en `.claude/plans/<slug>-todo.md` con una línea `- [ ]` por ítem implementable en orden de dependencias, más tasks espejo del harness si están disponibles (misma lógica de seguimiento que la ingesta y el refactor) — y ejecuta el flujo Implementando por cada ítem, marcando el progreso a medida que se completa. El documento de diseño es la fuente de verdad del checklist: si durante la implementación una decisión cambia, se actualiza primero el documento.

## Encadenamientos frecuentes

- Dudas conceptuales durante el diseño → consulta puntual vía Estudiando y se retoma.
- Si el "rediseño" resulta ser un sistema existente que hay que transformar gradualmente (no rehacer desde cero) → el documento de diseño define el destino, y la ejecución pasa por Refactorizando en lugar de Implementando.
