# Arquitectura

Este eje cubre cómo funciona la plataforma por dentro: namespaces vs databases, globals y mapeos, ediciones/licencias, instalación/Docker, y habilitación de Interoperability.

## Conceptos clave

- **Namespace vs Database**: el namespace es el espacio lógico de código y datos; la database es el almacenamiento físico. Clases y globals pueden mapearse a databases distintas dentro del mismo namespace, sin relación 1:1. Ver `namespaces-y-databases.md`.
- **Interoperability en Community Edition**: el paquete `Ens.*`/`EnsLib.*` está disponible en Community Edition, pero el namespace debe habilitarse explícitamente (`%EnsembleMgr.EnableNamespace`) — el flag del manifiesto del Installer no siempre alcanza en builds automatizados de Docker. Ver `instalacion-y-ediciones.md`.

## Capítulos

- `namespaces-y-databases.md`
- `instalacion-y-ediciones.md`
