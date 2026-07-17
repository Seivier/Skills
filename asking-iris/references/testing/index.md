# Testing

Este eje cubre cómo probar correctamente código IRIS/Ensemble: unit testing de lógica, testing de Productions (BS/BP/BO), dobles de prueba, seeds de datos, y qué se puede y no se puede instanciar fuera del framework.

## Conceptos clave

- **`EnsLib.Testing.Service.SendTestRequest`** permite invocar un Business Process o Business Operation directamente (sin transporte real), a diferencia de `Ens.Director.CreateBusinessService` que solo crea Business Services; requiere `TestingEnabled="true"` en la Production. Ver `testing-de-productions.md`.
- **Extraer la lógica a una clase plana** (sin extender `Ens.BusinessOperation`) permite testear con `%UnitTest.TestCase` y `%New()` sin restricción, para el loop de TDD más rápido sin producción corriendo. Ver `testing-de-productions.md`.
- **Patrón "substitute operation"**: un BO alternativo con el mismo contrato de mensajes, para testear flujos con dependencias externas sin tocar el BO real ni el código de producción. Ver `testing-de-productions.md`.
- **`%New()` directo sobre una Business Operation/Service falla** (`<INVALID OREF>` o inicialización inconsistente) — no están pensadas para instanciación manual fuera del framework de Productions. Ver `testing-de-productions.md`.
- **Seeds de datos de prueba con `%Persistent`**: recordar `%BuildIndices()` después de sembrar (gotcha detallado en `desarrollo/persistencia-y-sql.md`, referenciado aquí porque el contexto típico donde aparece es justamente un script de seed de testing).

## Capítulos

- `testing-de-productions.md`
