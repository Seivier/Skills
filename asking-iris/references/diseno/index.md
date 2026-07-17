# Diseño

Este eje cubre el diseño/implementación sugerida de integraciones IRIS/Ensemble: responsabilidades de Business Service/Process/Operation, clases de mensaje, adapters, DTL, y patrones y antipatrones de integración.

## Conceptos clave

- **Pipeline BS → BP → BO**: el Service recibe y reenvía (poca lógica), el Process concentra la lógica de negocio, el Operation es una salida específica sin ramificar. En integraciones simples es válido saltar el BP. Ver `productions-bs-bp-bo.md`.
- **`Ens.Request`/`Ens.Response`**: clases de datos simples, un tipo por operación (evitar el antipatrón "God Request" con campo `Operation` discriminador); pueden persistir en la tabla compartida o, con `%Persistent` + `RequestBodyMethods`/`ResponseBodyMethods`, en su propia tabla. Soporte para serialización JSON/XML recursiva con `%JSON.Adaptor` y `%SerialObject`. Ver `mensajes.md`.
- **Adapter**: encapsula el transporte (HTTP, TCP, archivo...) separado de la lógica de negocio; sus parámetros de conexión van en settings de la Production, no hardcodeados. Ver `adapters.md`.
- **Acoplamiento REST ↔ Production solo por string**: el `Parameter SERVICENAME` de una clase `%CSP.REST` debe coincidir exactamente con el `Name` del ítem BS en la Production; un desajuste solo falla en runtime, nunca en compilación. Ver `rest-y-productions.md`.
- **Explicar una clase BPL (`Ens.BusinessProcessBPL`)**: estructura estándar — identificación (request/response), contexto (qué guarda cada variable y si de verdad se reutiliza), secuencia de actividades (`target`, mapeo de entrada/salida, dependencias entre pasos), hallazgos a marcar siempre (credenciales hardcodeadas, falta de manejo de errores, config items de Production usados), y cuándo/cómo armar un diagrama Mermaid que imite el editor visual del Management Portal. Ver `bpl.md`.

## Capítulos

- `productions-bs-bp-bo.md`
- `mensajes.md`
- `adapters.md`
- `rest-y-productions.md`
- `bpl.md`
