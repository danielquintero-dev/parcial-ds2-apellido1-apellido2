import os
import simpy
import matplotlib.pyplot as plt
class mesa_de_ayuda:
    def init(self, tickets, mu):
        if not isinstance(tickets, list):
            raise TypeError("los Tickets Debe Ser Una Lista De Diccionarios")
        if mu is None or mu <= 0:
            raise ValueError("La Capacidad Del Agente (mu) Debe Ser Mayor A 0")
        self.tks_MatriculaApp = sorted(tickets, key=lambda x: x.get('llegada_min', 0))
        self.mu = float(mu)
    def tasa_de_llegadas(self):
        total = len(self.tks_MatriculaApp)
        if total < 2:
            return 0.0
        primer_turno = self.tks_MatriculApp[0]['llegada_minutos']
        ultimo_turno = self.tks_MatriculaApp[-1]['llegada_minutos']
        diff_hrs = (ultimo_turno - primer_turno) / 60.0
        if diferencia_de_horasv== 0:
            return 0.0
        return (total - 1) / diferencia_de_horas
    def metricas_mm1(self, lam):
        if lam < 0:
            raise ValueError("Lambda No Puede Ser Negativo")
        if lam >= self.mu:
            raise ValueError(f"Sistema Colapsado: Demanda ({lam}) >= Capacidad ({self.mu})")
        rho = lam / self.mu
        lq = (rho**2) / (1 - rho)
        wq = rho / (self.mu - lam)
        return rho