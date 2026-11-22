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
Según el modelo M/M/1, con una tasa de llegada de ocho boletos por hora y una tasa de servicio de diez boletos por hora, el tiempo promedio de espera (Wq) es de 0,42 horas (25,2 minutos). Sin embargo, en la simulación del lunes con ocho boletos, el tiempo promedio de espera (Wq) es de 0,42 horas (25,2 minutos), mientras que el boleto T3, como se muestra en `graficas/resultado.png`.  se muestra este tiempo. Esta discrepancia surge del hecho de que la simulación supone que el sistema permanece en el mismo estado durante un período prolongado, mientras que la solución analítica representa un único equilibrio a corto plazo. Tan pronto como la tasa de demanda aumenta a 9 boletos por hora, el sistema se acerca a la saturación y Wq (tiempo de espera) aumenta sustancialmente a 1,90 horas (114 minutos). Se recomienda que Huilasoft, con la ayuda de Andrea Perdomo, evite la sobrecarga en Huilasoft durante los períodos de mayor afluencia.