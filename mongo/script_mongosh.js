"Insertar Agentes"
db.agentes.insertMany([{_id: "Agente1", nombre: "Laura Cerquera", nivel: "senior", ticket_hora: 10, en_turno: true},{_id: "Agente2", nombre: "Andrés Perdomo", nivel: "junior", ticket_hora: 6, en_turno: false}])
"Insertar Tickets"
db.tickets.insertMany([{codigo: "Turno1", llegada_minutos: 0, atencion_minutos: 5, prioridad: "Alta", agente_id: "Agente1"},{codigo: "Turno2", llegada_minutos: 3, atencion_minutos: 7, prioridad: "Alta", agente: "Agente1"}])
db.tickets.insertMany([{codigo: "Turno3", llegada_minutos: 6, atencion_minutos: 4, prioridad: "Media", agente_id: "Agente1"},{codigo: "Turno4", llegada_minutos: 14, atencion_minutos: 8, prioridad: "Baja", agente: "Agente1"}])
db.tickets.insertMany([{codigo: "Turno5", llegada_minutos: 25, atencion_minutos: 6, prioridad: "Alta", agente_id: "Agente1"},{codigo: "Turno6", llegada_minutos: 28, atencion_minutos: 5, prioridad: "Media", agente: "Agente1"}])
db.tickets.insertMany([{codigo: "Turno7", llegada_minutos: 40, atencion_minutos: 9, prioridad: "Baja", agente_id: "Agente1"},{codigo: "Turno8", llegada_minutos: 52, atencion_minutos: 4, prioridad: "Alta", agente: "Agente1"}])
"Insertar Pruebas"
db.pruebas.insertMany([{semana: 1, numero_defectos: 28,},{semana: 2, numero_defectos: 23}])
db.pruebas.insertMany([{semana: 3, numero_defectos: 22,},{semana: 4, numero_defectos: 17}])
db.pruebas.insertMany([{semana: 5, numero_defectos: 16,},{semana: 6, numero_defectos: 12}])
db.pruebas.insertMany([{semana: 7, numero_defectos: 12,},{semana: 8, numero_defectos: 9}])
"Impirmir Tickets de Alta Prioridad"
print("Tickets De Alta Prioridad"); printjson(db.tickets.find({ prioridad: "Alta" }).toArray())
"Impirmir Tickets de Atencion Mayor A 6 Minutos"
print("Tickets De Atencion Mayor A 6 Minutos"); printjson(db.tickets.find({ atencion_minutos: { $gt: 6 } }).toArray())
"Impirmir Semanas Con Menos De 15 Defectos"
print("Semanas Con Menos De 15 Defectos"); printjson(db.pruebas.find({ numero_defectos: { $lt: 15 } }).toArray())
"Actualizar Prioridad de Ticket"
db.tickets.updateOne({codigo: "Turno7"}, {$set: {prioridad: "Media"}})
"Insertar Ticket de Prueba"
db.tickets.insertOne({codigo: "Turno Prueba", llegada_minutos: 40, atencion_minutos: 2, prioridad: "Alta", agente: "Agente1"})
"Eliminar Ticket de Prueba"
db.tickets.deleteOne({codigo: "Turno Prueba",})
