## Daniel Esteban Quintero Buendia 20211195403 
## Faiber Martin Tovar Rubiano 20202192246 

## Opción escogida Teoría de colas

## Modelo de datos (MongoDB)
* **Base de datos:** `MatriculaApp`
* **Colecciones y campos:**
  * `agentes`:
    * `_id` (String)
    * `nombre` (String)
    * `nivel` (String)
    * `tickets_hora` (Int)
    * `en_turno` (Boolean)
  * `tickets`:
    * `codigo` (String)
    * `llegada_minutos` (Int)
    * `atencion_minutos` (Int)
    * `prioridad` (String)
    * `agente` (String)
  * `pruebas`:
    * `semana` (Int)
    * `numero_defectos` (Int)
* **Relación:** La colección `tickets` se relaciona con `agentes` mediante el campo de referencia `agente`, el cual apunta al `_id` del agente encargado de atender el ticket.

## Interpretación
Según el modelo teórico M/M/1, con una tasa de llegadas de 8.08 tickets/hora y la capacidad de Laura Cerquera de 10 tickets/hora, el tiempo promedio de espera (Wq) es de 0.42 horas (25.2 minutos). Sin embargo, la simulación de los 8 tickets del lunes muestra una espera promedio de solo 1.63 minutos, con un pico máximo de 6 minutos en el ticket T3, como se observa en `graficas/resultado.png`. Esta diferencia se debe a que el modelo teórico asume un sistema en estado estacionario a largo plazo con variabilidad exponencial, mientras que la simulación evalúa una muestra corta y puntual. Si la demanda sube a 9.5 tickets/hora, Wq se dispara a 1.90 horas (114 minutos) por acercarse a la saturación. Se recomienda a HuilaSoft asignar a Andrés Perdomo como apoyo en horarios pico para evitar cuellos de botella.