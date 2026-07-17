# Testing de Productions: `EnsLib.Testing.Service` y extracción de lógica

Para TDD sobre Business Services/Processes/Operations sin pasar por el transporte real (HTTP/archivo/TCP), IRIS expone `EnsLib.Testing.Service` — la misma clase que usa la página **Interoperability → Test → Business Hosts** del Management Portal por debajo. Su método clave:

```objectscript
classmethod SendTestRequest(pTarget As %String, pRequest As Ens.Request,
    ByRef pResponse As Ens.Response, Output pSessionId As %String,
    pGetReply As %Boolean = 0) As %Status
```

`pTarget` es el nombre de ítem de un Business Process **o** Business Operation — a diferencia de `Ens.Director.CreateBusinessService`, que solo instancia Business Services, `SendTestRequest` invoca un BO directamente, con traza completa en el Message Viewer vía `pSessionId`. Requiere que la Production tenga `TestingEnabled="true"` (atributo del `XData ProductionDefinition`) y esté corriendo.

Para el loop de TDD más rápido (sin producción corriendo), la alternativa es extraer la lógica que no dependa del ciclo de vida de `Ens.BusinessOperation` (sin Adapter, sin `$$$TRACE`) a una clase plana que no extienda `Ens.BusinessOperation`, testeable con `%UnitTest.TestCase` y `%New()` sin restricción (ver más abajo el gotcha de `%New()` directo sobre BS/BO). Para flujos con dependencias externas (HTTP, otro sistema), el patrón que documenta la comunidad es el "substitute operation": un BO alternativo con el mismo contrato de mensajes que hace trabajo local determinista, apuntado vía el `TargetConfigName`/settings de un ítem de Production de test — sin tocar código de producción ni el BO real (propuesto por un autor por identificar en community.intersystems.com; ver `references/comunidad.json` (`scripts/comunidad.py show`), veredicto sin verificar — el patrón es razonable y coherente con el diseño de Productions, pero no se validó armando un caso propio).

Si se necesita sembrar datos de prueba con una clase `%Persistent` como parte del setup, tener presente el gotcha de `%BuildIndices()` en `desarrollo/persistencia-y-sql.md` — es el escenario típico donde aparece.

Fuente: Documatic de `EnsLib.Testing.Service` (ENSLIB, IRIS Data Platform / Health Connect 2024.3–2026.1) — método `SendTestRequest`; [Testing and Debugging Productions](https://docs.intersystems.com/irislatest/csp/docbook/DocBook.UI.Page.cls?KEY=EGDV_testing) (docs.intersystems.com) — `TestingEnabled` en el `XData ProductionDefinition` y la página Interoperability → Test → Business Hosts del Management Portal — 2026-07-10. Patrón "substitute operation": [How do you approach integration testing of a full BS > BP > BO flow in IRIS?](https://community.intersystems.com/post/how-do-you-approach-integration-testing-full-bs-bp-bo-flow-iris), InterSystems Developer Community — 2026-07-10.

## `Ens.BusinessOperation`/`Ens.BusinessService` no están pensadas para `%New()` directo fuera de una Production

**Síntoma:** Se intenta instanciar una Business Operation con `##class(Mi.BO).%New()` y llamar directamente a uno de sus métodos de mensaje (fuera del framework de producción, por ejemplo desde una sesión interactiva de prueba) — falla con `<INVALID OREF>` o comportamiento inconsistente (el objeto no está correctamente inicializado como lo estaría un ítem real de producción).

**Causa:** Las Business Operations/Services están diseñadas para ser instanciadas y gestionadas por el framework de Productions de Ensemble/IRIS (pooling, configuración de adapter, `Ens.Director`), no para instanciación manual.

**Solución / workaround:** Para pruebas ad-hoc de la lógica de una Business Operation sin levantar la Production completa, extraer la lógica de negocio a un método privado que no dependa del ciclo de vida de `Ens.BusinessOperation` y probar ese método por separado (con `%UnitTest.TestCase`, ver arriba), o usar `##class(Ens.Director).CreateBusinessService(...)`/`EnsLib.Testing.Service.SendTestRequest` en vez de `%New()` directo.

Fuente: verificado empíricamente — intento de invocar una Business Operation propia vía `%New()` desde una sesión IRIS interactiva — 2026-07-08.
