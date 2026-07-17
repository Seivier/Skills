# Carga y compilación de código: `$SYSTEM.OBJ` y dependencias faltantes

`$SYSTEM.OBJ` es la API para cargar y compilar clases/rutinas desde archivos, usada típicamente en scripts de build/deploy (`iris.script` corridos con `iris session IRIS < script`). Tiene varios métodos con capacidades distintas — no intercambiables sin revisar qué tipos de archivo soporta cada uno:

- `LoadDir(dir, qspec, .errorlog, recurse, .loadedlist)` — deprecado; solo carga `.cls` y `.xml`.
- `ImportDir(dir, wildcards, qspec, .errorlog, recurse, .imported, listonly, .selectedlist)` — soporta múltiples tipos vía el parámetro `wildcards` (p. ej. `"*.cls;*.mac;*.int;*.inc;*.dfi"`).
- A partir de 2025.1, hay un nuevo método `Import()` que reemplaza a `LoadDir`/`ImportDir`/`Load` para importar uno o varios archivos — revisar la versión de IRIS en uso antes de asumir cuál está disponible.

El flag `"ck"` usado como `qspec` en estos métodos significa, en términos generales, "compile + keep source" — pero el flag por sí solo no determina qué *tipos de archivo* se procesan; eso lo determina el método elegido (`LoadDir` vs `ImportDir`) y, en `ImportDir`, el parámetro `wildcards`.

Fuente: docs.intersystems.com, Documatic de `%SYSTEM.OBJ` — 2026-07-08.

## `$SYSTEM.OBJ.LoadDir` no carga archivos `.inc`/`.mac` — no tiene parámetro `filespec`

**Síntoma:** Una clase con `Include MiArchivo` compila con `MPP5635`/`MPP5610` (ver `desarrollo/macros-e-include-files.md`) al cargar un directorio completo vía `$SYSTEM.OBJ.LoadDir(dir, qspec, , recurse)`, incluso intentando "arreglarlo" pasando un tercer argumento con un patrón de wildcards tipo `"*.cls,*.inc"`.

**Causa:** La firma real y actual de `LoadDir` es `LoadDir(dir As %String, qspec As %String, ByRef errorlog As %String, recurse As %Boolean, ByRef loadedlist As %String)` — **no existe un parámetro `filespec`**. El tercer parámetro posicional es `errorlog` (`ByRef`), así que pasarle un string tipo `"*.cls,*.inc"` no filtra nada — simplemente se ignora como valor de un parámetro de salida. Además, `LoadDir` está **deprecado** y, por diseño, solo carga definiciones de clase (`.cls`) y archivos `.xml`; no soporta rutinas `.mac`/`.int`/`.inc` en absoluto, sin importar qué se le pase.

**Solución / workaround:** Para cargar un directorio que incluya `.inc`/`.mac`, usar `$SYSTEM.OBJ.ImportDir(dir, wildcards, qspec, .errorlog, recurse, .imported, listonly, .selectedlist)` con `wildcards` explícito, p. ej. `"*.cls;*.mac;*.int;*.inc;*.dfi"` — este sí soporta múltiples tipos de rutina. Alternativa moderna (2025.1+): el nuevo método `Import()` que reemplaza a `LoadDir`/`ImportDir`/`Load` (revisar la versión de IRIS en uso antes de asumir cuál está disponible).

Fuente: docs.intersystems.com, Documatic de `%SYSTEM.OBJ` (firma de `LoadDir` e `ImportDir`) — 2026-07-08. Reproducido empíricamente: 3 rebuilds de imagen Docker con distintos argumentos de `LoadDir` en IRIS Community 2026.1, ninguno cargó el `.inc`, hasta cambiar a inlinear el código sin macros.

## ERROR #5373 — "Class 'X', used by 'Y:campo', does not exist"

**Síntoma:** `ERROR #5373: Class 'HS.Message.XMLMessage', used by 'MiClase:MiMetodo:FormalSpec', does not exist` (o similar con cualquier clase referenciada en una firma de método, tipo de propiedad, o `dependson`).

**Causa:** La clase compila contra una dependencia (parámetro de método, tipo de propiedad, clase base) que no está presente en el namespace — típicamente porque el paquete que la provee (ej. `HS.*` de IRIS for Health, o un paquete propietario de terceros) no está instalado en esa instancia/edición, o es un stub de sandbox incompleto que no replica el 100% del sistema real.

**Solución / workaround:** No siempre es un bug del código propio — confirmar primero si la clase faltante pertenece a un componente opcional (ej. módulos de IRIS for Health) o a un sistema externo que el sandbox solo mockea parcialmente. Si es así, el error es esperado y limitado a esa clase (no bloquea la compilación de clases no relacionadas).

Fuente: verificado empíricamente — un proyecto de integración IRIS, clases stub que referencian paquetes opcionales (ej. `HS.Message.XMLMessage` de IRIS for Health) sin esos paquetes instalados en IRIS Community — 2026-07-08.
