# Desarrollo

Este eje cubre el lenguaje y la plataforma en el día a día: sintaxis, macros/includes, scope, carga/compilación de código, errores de compilación y runtime, y comportamientos que difieren de lo que uno asumiría leyendo la documentación superficialmente. Si la pregunta trae un mensaje de error concreto (`ERROR #NNNN`, `MPPnnnn`, o un error de runtime entre `<...>`), casi siempre cae aquí.

## Conceptos clave

- **`Include` va antes de `Class`, no dentro del cuerpo** — colocarlo como si fuera un keyword de clase produce `ERROR #5559`/`ERROR #5030`. Ver `macros-e-include-files.md`.
- **Un include (`.inc`) que nunca se cargó** produce `MPP5635`/`MPP5610` y cascadas de `#1026` en cada uso de la macro — la causa raíz suele ser la herramienta de carga usada, no la clase. Ver `macros-e-include-files.md`.
- **Las macros son sustitución de texto pura**, expandida inline en el scope de quien la usa — por eso una macro sí sirve para compartir un idioma como `New $NAMESPACE`, pero un método de clase base no. Ver `macros-e-include-files.md`.
- **`$SYSTEM.OBJ.LoadDir` no tiene parámetro `filespec`** y, por diseño, solo carga `.cls`/`.xml` — nunca `.inc`/`.mac`, sin importar qué argumentos se le pasen. Ver `carga-y-compilacion.md`.
- **`ERROR #5373` (clase referenciada no existe)** suele significar que un paquete opcional (`HS.*`, un stub de sandbox) no está instalado, no un bug del código propio. Ver `carga-y-compilacion.md`.
- **`New $NAMESPACE` no persiste fuera del método que lo ejecuta** — el cambio de namespace se revierte automáticamente al retornar, por la misma semántica de scope de cualquier variable local. Ver `scope-y-variables.md`.
- **`%Save()` puede no ser visible en SQL hasta `%BuildIndices()`** — el acceso por `ID` funciona pero `COUNT(*)`/filtros por columna no indexada pueden devolver 0 filas justo después de un seed automatizado. Ver `persistencia-y-sql.md`.
- **DTL: el `<assign>` que se ejecuta último gana**, los paths de campos repetibles de HL7 (`{PID:3.1}` vs `{PID:3(1).1}` vs `{PID:3().1}`) no son intercambiables, y un mismatch de Message Schema Category entre el Test y la Production real puede desalinear campos sin dar error. Ver `dtl-y-hl7.md`.
- **Un string ISO 8601 (el que produce `Date.toISOString()` en JS/Vue) se convierte con `##class(%Library.TimeStamp).XSDToLogical(isoString)`**, que sí interpreta el offset y el sufijo `Z` (confirmado en la documentación oficial). **`$ZDATETIMEH(isoString,3,5)` NO sirve para esto** — la documentación dice explícitamente que el offset de `tformat=5` (y 6/7/8) "may be supplied, but is ignored": corre sin error pero descarta la zona horaria en silencio. Ver `fechas-y-datetime.md`.

## Capítulos

- `macros-e-include-files.md`
- `carga-y-compilacion.md`
- `scope-y-variables.md`
- `persistencia-y-sql.md`
- `dtl-y-hl7.md`
- `fechas-y-datetime.md`
