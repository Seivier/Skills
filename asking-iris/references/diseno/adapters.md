# Adapters

Un **Adapter** (`EnsLib.HTTP.OutboundAdapter`, `EnsLib.TCP.OutboundAdapter`, etc.) encapsula el detalle de transporte (HTTP, TCP, archivo, FTP...) que un Business Service o Business Operation necesita para hablar con el mundo exterior. Se configura como `Property Adapter As <Clase de Adapter>` más `Parameter ADAPTER = "<Clase de Adapter>"` en la clase del Service/Operation, y sus parámetros de conexión (host, puerto, credencial) se configuran a nivel de la Production, no hardcodeados en el código — separar el adapter de la lógica de negocio es lo que permite cambiar de HTTP a otro transporte sin tocar la lógica.

Ejemplo mínimo de un Business Operation que usa el adapter HTTP saliente:

```objectscript
Class Mi.Paquete.BO.MiOperacionHTTP Extends Ens.BusinessOperation
{
Parameter ADAPTER = "EnsLib.HTTP.OutboundAdapter";
Property Adapter As EnsLib.HTTP.OutboundAdapter;

XData MessageMap
{
<MapItems>
  <MapItem MessageType="Mi.Paquete.Messages.HacerAlgoRequest">
    <Method>HacerAlgo</Method>
  </MapItem>
</MapItems>
}

Method HacerAlgo(pRequest As Mi.Paquete.Messages.HacerAlgoRequest, Output pResponse As Mi.Paquete.Messages.HacerAlgoResponse) As %Status
{
    Set tSC = ..Adapter.SendFormDataArray(.tHttpResponse, "POST", .tHeaders, .tFormData)
    Quit tSC
}
}
```

Los valores de `Server`/`Port`/`URL`/`SSLConfig` del adapter se configuran como *settings* del ítem en la Production (no en el código), y ahí es donde también se asocia una credencial (`Ens.Config.Credentials`) si el destino requiere autenticación.

Fuente: docs.intersystems.com, "About the HTTP Adapters" y "Using the HTTP Outbound Adapter" (Using HTTP Adapters in Productions, KEY=EHTTP_INTRO / EHTTP_outbound), "Settings for the HTTP Outbound Adapter" (KEY=EHTTP_settings_outbound) — 2026-07-08.
