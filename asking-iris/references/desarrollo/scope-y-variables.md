# Scope de variables: `New` y `$NAMESPACE`

## `New $NAMESPACE` dentro de un método no persiste en el llamador

**Síntoma:** Se factoriza el idioma `New $NAMESPACE / Set $NAMESPACE="AGENDA"` en un método compartido (pensado como ayuda estilo Template Method) y se lo invoca con `Do ..CambiarNamespace(...)` como primera línea de otro método — pero el código que sigue después de esa llamada sigue ejecutándose en el namespace original, como si el `Set` nunca hubiera pasado.

**Causa:** `New` guarda el entorno de variables locales actual y lo restaura automáticamente cuando termina la rutina/método/función que ejecutó el `New` (por `QUIT` o `RETURN`). Como `$NAMESPACE` se maneja con la misma semántica de scope que una variable local, un método separado que hace `New $NAMESPACE` restaura el namespace original apenas ese método retorna — el cambio nunca "se ve" en el método que lo llamó.

**Solución / workaround:** El `New $NAMESPACE` (y el `Set` que cambia su valor) debe estar **inline en el mismo método** que necesita operar en el otro namespace — no se puede factorizar a un método/helper separado sin perder el efecto. Si se quiere evitar la duplicación del idioma de todos modos, la alternativa correcta en ObjectScript es una macro de include file (que expande inline en el método que la invoca, ver macro `SwitchNamespace` en `desarrollo/macros-e-include-files.md`), no un método de clase base.

Fuente: docs.intersystems.com, "NEW (ObjectScript)" (ObjectScript Reference: *"the existing local variable environment... is saved and then restored when the subroutine or function terminates"*) — 2026-07-08. Reproducido empíricamente en un proyecto de integración IRIS al intentar extraer el namespace-switch de dos Business Operations a una clase base común.
