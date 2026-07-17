# REST y Productions: el acoplamiento por nombre de ítem

## El nombre del ítem BS en una Production y el `Parameter SERVICENAME` de la clase REST se acoplan solo por string, sin verificación en tiempo de compilación

**Síntoma:** Una clase `%CSP.REST` invoca un Business Service por nombre (`Parameter SERVICENAME = "Mi.BS.Item"` + `##class(Ens.Director).CreateBusinessService(pServiceName, ...)`), y el nombre debe coincidir *exactamente* con el `Name` del ítem correspondiente en `Ens.Config.Production` — si no coincide (typo, rename sin actualizar ambos lados), el error solo aparece en runtime (`"No se pudo iniciar el servicio"`), nunca en tiempo de compilación.

**Causa:** El acoplamiento entre la clase REST y la Production es por string libre, no por referencia de clase — es un patrón común en integraciones IRIS/Ensemble (varios ítems de producción con distinto `Name` pueden apuntar a la misma clase BS reutilizable, diferenciados solo por `TargetConfigName`/nombre de ítem). Este es precisamente el tipo de acoplamiento que aparece en la variante simplificada del pipeline BS→BP→BO descrita en `diseno/productions-bs-bp-bo.md`, donde una capa REST delgada llama directo a un BS de pass-through.

**Solución / workaround:** Mantener el nombre del ítem documentado explícitamente (comentario de cabecera en la clase REST y en `Production.cls`) y, si es posible, agregar una prueba de humo que confirme en cada build que la Production tiene todos los ítems que las clases REST esperan.

Fuente: verificado empíricamente — patrón de una clase REST y un Business Service reutilizable, diferenciados por `TargetConfigName` — 2026-07-08.
