import os
import simpy
import matplotlib.pyplot as plt
class mesa_ayuda:
    def init(self, tickets, mu):
        if not isinstance(tickets, list):
            raise TypeError("los tickets debe ser una lista de diccionarios")
        if mu is None or mu <= 0:
            raise ValueError("la capacidad del agente (mu) debe ser mayor a 0")
        self.tks_matriculapp = sorted(tickets, key=lambda x: x.get('llegada_min', 0))
        self.mu = float(mu)
    def tasa_de_llegadas(self):
        total = len(self.tks_matriculapp)
        if total < 2:
            return 0.0
        turno_primero = self.tks_matriculapp[0]['llegada_minutos']
        turno_ultimo = self.tks_matriculapp[-1]['llegada_minutos']
        diff_hrs = (turno_ultimo - turno_primero) / 60.0
        if diferencia_de_horas == 0:
            return 0.0
        return (total - 1) / diferencia_de_horas
    def metricas_mm1(self, lam):
        if lam < 0:
            raise ValueError("lambda no puede ser negativo")
        if lam >= self.mu:
            raise ValueError(f"Sistema Colapsado: Demanda ({lam}) >= Capacidad ({self.mu})")
        rho = lam / self.mu
        lq = (rho**2) / (1 - rho)
        wq = rho / (self.mu - lam)
        return rho