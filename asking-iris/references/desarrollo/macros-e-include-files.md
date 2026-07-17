# Macros e Include Files

Un **include file** en ObjectScript no es un archivo suelto del sistema operativo — es, igual que una clase o una rutina, una unidad de código guardada dentro de una database de IRIS (de tipo `.inc`). Sirve para definir **macros** (`#define`) que se puedan compartir entre varias clases/rutinas sin duplicar el texto. Una clase incluye un archivo así con la directiva `Include NombreDelInclude` (sin la extensión `.inc`, sin `#` inicial), colocada **antes** de la declaración `Class ... { }`.

Las macros son sustitución de texto pura: el compilador reemplaza cada uso de la macro por su definición al compilar (visible en el código `.INT` generado), así que el resultado de la sustitución debe ser sintácticamente válido por sí solo. Esto tiene una consecuencia importante para patrones como "factorizar un `New $NAMESPACE` compartido": una macro definida en un include file y usada dentro de un método se expande *inline*, dentro del scope de ese método — a diferencia de llamar a un método de una clase base, que crea un nuevo stack frame y por lo tanto no sirve para este propósito (ver `desarrollo/scope-y-variables.md`, entrada de `New $NAMESPACE`).

Fuente: docs.intersystems.com, "Macros and Include Files" (Using ObjectScript) — 2026-07-08.

## ERROR #5559 / ERROR #5030 — "could not be parsed correctly" al usar `Include`

**Síntoma:** `ERROR #5559: The class definition for class 'X' could not be parsed correctly...` seguido de `ERROR #5030: An error occurred while compiling class 'X'`, en una clase que usa la palabra clave `Include`.

**Causa:** La directiva `Include NombreArchivo` debe ir **antes** de la declaración `Class ... { }`, no dentro del cuerpo de la clase. Si se coloca dentro de las llaves (como si fuera un keyword de clase más, al lado de `Parameter`/`Property`), el parser de definición de clase falla.

**Solución / workaround:**
```objectscript
/// comentarios de cabecera de la clase
Include MiArchivoDeIncludes

Class Mi.Paquete.MiClase Extends %RegisteredObject
{
    ...
}
```
Cuando una clase incluye un include file, cualquier subclase de esa clase lo incluye automáticamente (no hace falta repetir el `Include` en subclases).

Fuente: docs.intersystems.com, "Macros and Include Files" (Using ObjectScript) — 2026-07-08.

## MPP5635 "No include file 'X'" / MPP5610 "Referenced macro not defined" — el include nunca se cargó

**Síntoma:** `ERROR: MiClase.cls(1) : MPP5635 : No include file 'X'` y/o `MPP5610 : Referenced macro not defined: 'NombreMacro'`, seguido de `#1026: Invalid command` en cada línea que usa la macro (`$$$NombreMacro(...)` se interpreta como comando inválido porque nunca se sustituyó).

**Causa:** El archivo `.inc` que define las macros nunca llegó a compilarse/cargarse en la base de datos de rutinas — el `Include` en la clase referencia un include file que no existe todavía en ese namespace. Esto pasa fácilmente en scripts de build automatizados que cargan un directorio completo si la herramienta de carga usada no soporta `.inc` (ver `desarrollo/carga-y-compilacion.md`, entrada de `$SYSTEM.OBJ.LoadDir`).

**Solución / workaround:** Confirmar que el `.inc` se cargó como rutina antes de compilar las clases que lo usan (ver `desarrollo/carga-y-compilacion.md` para la causa raíz más común). Si la carga masiva no soporta `.inc`, usar `$SYSTEM.OBJ.ImportDir` con `wildcards` explícito, o cargar el `.inc` individualmente con `$SYSTEM.OBJ.Load`.

Fuente: verificado empíricamente contra IRIS Community 2026.1 (sandbox Docker) — 2026-07-08.
