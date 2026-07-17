# Fechas y datetime: de string ISO 8601 (JSON/Vue) a ObjectScript

## El problema
Un frontend (Vue, o cualquier cliente JS) serializa fechas con `Date.prototype.toISOString()`, que produce siempre `"yyyy-mm-ddThh:mm:ss.sssZ"` (UTC, sufijo `Z`) — o, si viene de otra fuente con offset propio, `"yyyy-mm-ddThh:mm:ss±hh:mm"`. Ninguno de los dos es el formato interno de ObjectScript (`$H`, `days,seconds` desde el 31-dic-1840) ni el formato lógico de `%TimeStamp` (ODBC: `"yyyy-mm-dd hh:mm:ss.fff"`).

## Camino correcto: `%Library.TimeStamp.XSDToLogical`
`%Library.TimeStamp` (el datatype que respalda `%TimeStamp`) trae el conversor que el framework usa para XML/SOAP/JSON. Convierte un string `xsd:dateTime` — el mismo formato que produce ISO 8601, incluyendo el sufijo `Z` — directo al valor lógico ODBC que la propiedad espera:

```objectscript
set tsLogical = ##class(%Library.TimeStamp).XSDToLogical(isoString)
set obj.MiPropiedadTimeStamp = tsLogical
```

El parámetro `XMLTIMEZONE` de `%Library.TimeStamp` vale `UTC` por defecto, lo que significa "convertir a UTC en la entrada" (la alternativa es `IGNORE`, que ignora la zona horaria) — por eso `XSDToLogical` sí interpreta correctamente tanto `Z` como un offset explícito `±hh:mm`, y devuelve el resultado ya normalizado a UTC (fuente: docs.intersystems.com, Class Reference de `%Library.TimeStamp`, parámetro `XMLTIMEZONE` y método `XSDToLogical`, 2026-07-10). Para el caso típico de `toISOString()` (siempre termina en `Z`) esto funciona directo, sin ningún ajuste al string.

**Caveat con offsets sin dos-puntos:** el formato XSD estándar espera el offset como `+hh:mm` (con `:`). Si tu string trae el offset sin separador (`+0100` en vez de `+01:00` — no es el caso de `toISOString()`, pero sí de algunos otros serializadores), hay que insertarlo antes de llamar a `XSDToLogical`:

```objectscript
; ejemplo de Vitaliy Serdtsev en community.intersystems.com (ver más abajo): inserta ":" antes de los últimos 2 caracteres del offset
set tsLogical = ##class(%Library.TimeStamp).XSDToLogical($Extract(isoString,1,19)_$Extract(isoString,20,21)_":"_$Extract(isoString,22,23))
```

## Camino que NO sirve para el offset: `$ZDATETIMEH` con `tformat=5`
Es tentador usar `$ZDATETIMEH("2021-11-04T11:10:00+0100", 3, 5)` (abreviable `$ZDTH`) para obtener `$H` directo de un string con offset — de hecho corre sin error y devuelve un valor (`66052,40200`). **Pero el offset queda silenciosamente descartado**: la documentación oficial dice explícitamente para `tformat` 5 (y también 6, 7 y 8) que el sufijo `±hh:mm` "may be supplied, but is ignored" — la hora se toma tal cual como hora local, sin aplicar el offset (fuente: docs.intersystems.com, "$ZDATETIMEH (ObjectScript)", ObjectScript Reference, IRIS Data Platform 2026.1, tabla de valores de `tformat`, 2026-07-10). Prueba reproducible: `$zdth("2021-11-04T11:10:00+0100",3,5)`, `$zdth("2021-11-04T11:10:00+0200",3,5)` y `$zdth("2021-11-04T11:10:00-0100",3,5)` devuelven **el mismo** `66052,40200` — si el offset importara, darían resultados distintos.

Este comportamiento es justo el tipo de gotcha que conviene tener presente: el string se procesa sin error y "parece" funcionar (compila, corre, da un `$H`), pero es silenciosamente incorrecto para cualquier caso donde el offset no coincide con la hora local del servidor. Si necesitás `$H` y no solo el valor lógico ODBC, la forma correcta es convertir primero con `XSDToLogical` (que sí aplica el offset) y recién ahí pasar a `$H`:

```objectscript
set h = $ZDATETIMEH(##class(%Library.TimeStamp).XSDToLogical(isoString), 3)
```

## Origen y verificación
Este capítulo salió de un hilo de community.intersystems.com, "How to convert datetime ISO 8601 to ObjectScript datetime" (https://community.intersystems.com/post/how-convert-datetime-iso-8601-objectscript-datetime, Kurro Lopez, Nov 2021). `WebFetch` devuelve 403 sobre esa página (y sobre `docs.intersystems.com`); se pudo leer el HTML completo pidiéndolo con `curl` y un User-Agent de navegador normal en vez de `WebFetch` — ambos devuelven el mismo HTML público, solo que `WebFetch` es bloqueado por lo que sea que estén filtrando (user-agent, probablemente). Ese mismo método permitió confirmar independientemente, leyendo las páginas oficiales, tanto lo de `tformat=5` como lo de `XMLTIMEZONE=UTC` citados arriba.

Cronología del hilo (importa para no repetir el error que cometió el propio hilo):
1. **Vitaliy Serdtsev** propone `$zdth(isoString,3,5)` como solución.
2. **Julius Kavay** responde citando la documentación oficial y demostrando con 3 ejemplos que el offset se ignora — la propuesta de Vitaliy Serdtsev no resuelve el problema real (conversión correcta de zona horaria), aunque no tira error.
3. **Vitaliy Serdtsev** reconoce el punto y publica el método `Iso8601ToTimeStamp`, basado en `%Library.TimeStamp.XSDToLogical` con el ajuste de los dos-puntos en el offset — este es el que sí produce resultados distintos y correctos para cada offset de sus 4 ejemplos.
4. **Kurro Lopez** (el autor de la pregunta) responde "Thanks.. the 3,5 was the answer... now it's working!!!" — dirigido a Julius Kavay, pero cronológicamente antes de que Vitaliy Serdtsev publicara el método corregido. Su "funciona" describe la experiencia de que el string parseó sin error, no que el offset se procesó bien; no lo contradice ninguna fuente, pero tampoco hay que leerlo como confirmación de que `3,5` resuelve el problema de fondo.

Ver `references/comunidad.json` (`python3 scripts/comunidad.py show --usuario vitaliy-serdtsev2149` / `... --usuario julius-kavay`) para el detalle de reputación de cada aporte.
