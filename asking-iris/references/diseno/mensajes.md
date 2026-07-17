# Clases de mensaje: `Ens.Request` / `Ens.Response`

Toda comunicación dentro de una Production viaja como instancias de subclases de `Ens.Request` (petición) y `Ens.Response` (respuesta) — clases de datos simples (propiedades tipadas), sin lógica de negocio propia. Un Business Operation declara un `XData MessageMap` que asocia cada tipo de `Ens.Request` que puede recibir con el método que debe manejarlo:

```objectscript
XData MessageMap
{
<MapItems>
  <MapItem MessageType="Mi.Paquete.Messages.HacerAlgoRequest">
    <Method>HacerAlgo</Method>
  </MapItem>
</MapItems>
}
```

Diseñar un tipo de Request/Response distinto por operación (en vez de una única clase "genérica" con un campo discriminador tipo `Operation` que cambia de significado según su valor) es más alineado con tipado fuerte y más fácil de mantener — un antipatrón común en código legado de integraciones es exactamente ese "God Request" con un campo `Operation` que hace de switch.

Toda clase de mensaje debe ser persistente (los mensajes que pasan por una Production se guardan en la base de datos hasta que un administrador los purga). Hay dos formas de construir una: extender `Ens.Request`/`Ens.Response` directamente, o extender `%Persistent` + `Ens.Util.RequestBodyMethods`/`ResponseBodyMethods` — esta segunda forma evita que el mensaje se guarde en la tabla compartida de todos los requests/responses del sistema, lo que puede afectar el rendimiento de las consultas sobre esa tabla a medida que crece.

Fuente: docs.intersystems.com, "Defining Messages" (Developing Productions, KEY=EGDV_messages) — 2026-07-08. Patrón de migración observado en proyectos de integración IRIS (de una clase Request genérica con campo `Operation` hacia clases de Request separadas por operación) — verificado empíricamente.

## Serialización de Mensajes y %JSON.Adaptor
**Causa:** Por defecto, las clases persistentes de ObjectScript no se serializan a JSON/XML a menos que hereden de los adaptadores correspondientes. Además, si un mensaje contiene objetos anidados, estas subclases deben ser serializables en la base de datos (heredar de `%SerialObject`) para poder almacenarse dentro de la tabla del mensaje persistentemente.
**Solución / workaround:**
1. Heredar la clase del mensaje de `(Ens.Request, %JSON.Adaptor, %XML.Adaptor)` o `(Ens.Response, %JSON.Adaptor, %XML.Adaptor)`.
2. Para cualquier objeto complejo anidado (propiedad del mensaje), la clase del objeto anidado debe heredar de `(%SerialObject, %JSON.Adaptor, %XML.Adaptor)`. Esto asegura que sea almacenable en base de datos de manera embebida y serializable a JSON/XML recursivamente.
3. Si los campos del JSON entrante no son identificadores válidos en ObjectScript (por ejemplo, contienen guiones como `order-id`), usar el parámetro de propiedad `%JSONFIELDNAME` (ej. `Property orderId As %String(%JSONFIELDNAME = "order-id");`).
4. Para campos con valores discretos (uniones de literals en TS), usar el parámetro `VALUELIST` (ej. `VALUELIST = ",A,B"`) para asegurar la validación automática durante el `%JSONImport()`.
Fuente: verificado empíricamente contra IRIS Community 2026.1 (2026-07-10).
