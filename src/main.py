from pymongo import MongoClient
from modelo import mesa_de_ayuda

Cliente = MongoClient("mongodb://localhost:27017/")
base_de_datos = Cliente["MatriculaApp"]

tickets = list(db.tickets.find())
agente = db.agentes.find_one({"en_turno": True})
mu = agente["tickets_hora"]

Mesa = mesa_de_ayuda(tickets, mu)

lam = mesa.tasa_de_llegadas()
rho, lq, wq = mesa.metricas_mm1(lam)
Esperas = mesa.simular()
_, _, wq_95 = mesa.metricas_mm1(9.5)

print("Lambda:", round(lam, 2))
print("Wq teorico (min):", round(wq * 60, 2))
print("Espera simulada (min):", round(sum(Esperas) / len(Esperas), 2))
print("Wq con 9.5 (min):", round(wq_95 * 60, 2))

Mesa.graficar()