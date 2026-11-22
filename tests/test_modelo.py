import sys
sys.path.append("src")
from modelo import mesa_de_ayuda

M1 = mesa_de_ayuda([], 10)
_, _, wq = M1.metricas_mm1(8)
assert round(wq, 2) == 0.4

datos = [
    {"codigo": "Turno1", "llegada_minutos": 0, "atencion_minutos": 5},
    {"codigo": "Turno2", "llegada_minutos": 3, "atencion_minutos": 7}
]
M2 = mesa_de_ayuda(datos, 10)
assert M2.simular() == [0, 2]

print("Pruebas Estan Ok...")