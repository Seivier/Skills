# Productions y el pipeline Business Service → Business Process/Operation

Una **Production** (`Ens.Config.Production`) es el contenedor de configuración que define qué componentes de integración están activos y cómo se conectan entre sí (sus "ítems", cada uno con un `Name` y una `ClassName`). El patrón recomendado por InterSystems para dividir responsabilidades dentro de una Production es:

- **Business Service** (`Ens.BusinessService`): el punto de entrada — recibe datos desde fuera de la Production (HTTP, archivo, TCP, etc.), los envuelve en una clase de mensaje (`Ens.Request`) y los reenvía hacia dentro de la Production. Por diseño debe tener poca o ninguna lógica de negocio: su trabajo es solo *recibir y reenviar*.
- **Business Process** (`Ens.BusinessProcess`, incluyendo los BPL visuales): el lugar recomendado para la lógica de negocio — ramificaciones, orquestación de múltiples llamadas, transformación de datos. InterSystems recomienda explícitamente concentrar la lógica de negocio aquí, no en el Service ni en el Operation.
- **Business Operation** (`Ens.BusinessOperation`): el punto de salida — recibe mensajes desde dentro de la Production (de un Service o Process) y genera la salida hacia un sistema externo (otra API, una base de datos, un archivo). Por convención debe ser una operación extremadamente específica, con poca lógica propia, sin ramificar ni llamar a otras operaciones.

En la práctica, muchas integraciones simples saltan el Business Process cuando la lógica es mínima y ponen todo directamente en el Business Operation (como en proyectos donde una capa REST delgada llama a un BS genérico de pass-through que reenvía síncronamente a un BO que sí concentra la lógica — ver `diseno/rest-y-productions.md`) — esto se aparta un poco de la separación "canónica" de 3 capas, pero es un patrón común y válido cuando no hace falta orquestación entre varias operaciones.

Los componentes se comunican entre sí mediante `SendRequestSync`/`SendRequestAsync`, pasando instancias de clases de mensaje (ver `diseno/mensajes.md`).

Fuente: docs.intersystems.com, "Defining Business Services", "Defining Business Operations", "Business Processes and Business Logic" (Developing Productions / Introducing Interoperability Productions) — 2026-07-08.

## Regla operativa: nunca leer ni crear/modificar el XML de una Production real

No leer el contenido de clases `Ens.Production` reales (XData `ProductionDefinition`) ni de sus exports XML — suelen traer datos sensibles (hosts internos, nombres de credenciales, IPs de producción). Tampoco crear ni modificar una Production directamente: casi siempre ya existe una preexistente en el servidor real que el usuario prefiere ajustar a mano en el Management Portal, no vía archivo generado por el agente.

En su lugar, cuando hace falta comunicar qué config items/Settings necesita una Production (nueva o a modificar), entregar un **documento Markdown aparte** con el listado de configuraciones (nombre de item, clase, Settings clave como `WebServiceURL`/`Credentials`, sin valores sensibles reales si no hace falta) para que el usuario lo aplique manualmente. No generar el `.cls`/XML de la Production como entregable.

Excepción: si el propio usuario pide explícitamente que se lea o genere el archivo de Production en una tarea puntual, se puede hacer solo para esa tarea — la regla por defecto es no hacerlo sin que lo pidan.
