import os
import simpy
import matplotlib.pyplot as plt

class mesa_de_ayuda:
    def __init__(self, tickets, mu):
        if not isinstance(tickets, list):
            raise TypeError("los Tickets Debe Ser Una Lista De Diccionarios")
        if mu is None or mu <= 0:
            raise ValueError("La Capacidad Del Agente (mu) Debe Ser Mayor A 0")
        self.tks_MatriculaApp = sorted(tickets, key=lambda x: x.get('llegada_minutos', 0))
        self.mu = float(mu)

    def tasa_de_llegadas(self):
        total = len(self.tks_MatriculaApp)
        if total < 2:
            return 0.0
        primer_turno = self.tks_MatriculaApp[0]['llegada_minutos']
        ultimo_turno = self.tks_MatriculaApp[-1]['llegada_minutos']
        diferencia_de_horas = (ultimo_turno - primer_turno) / 60.0
        if diferencia_de_horas == 0:
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
        return rho, lq, wq

    def simular(self):
        env = simpy.Environment()
        agente = simpy.Resource(env, capacity=1)
        esperas = []

        def ticket(env, ag, lleg, aten):
            yield env.timeout(lleg)
            with ag.request() as turno:
                yield turno
                esperas.append(env.now - lleg)
                yield env.timeout(aten)

        for t in self.tks_MatriculaApp:
            env.process(ticket(env, agente, t['llegada_minutos'], t['atencion_minutos']))

        env.run()
        return esperas

    def graficar(self, ruta="graficas/resultado.png"):
        esperas = self.simular()
        cods = []
        for t in self.tks_MatriculaApp:
            cods.append(t['codigo'])

        carpeta = os.path.dirname(ruta)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)

        prom = sum(esperas) / len(esperas) if esperas else 0

        fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
        barras = ax.bar(cods, esperas, color="#2563EB", edgecolor="#1E3A8A", width=0.55, zorder=3, label="Tiempo en cola")

        ax.axhline(prom, color="#DC2626", linestyle="--", linewidth=1.5, zorder=4, label=f"Promedio: {prom:.2f} min")

        for b in barras:
            h = b.get_height()
            ax.annotate(f"{h:.1f} min",
                        xy=(b.get_x() + b.get_width() / 2, h),
                        xytext=(0, 4),
                        textcoords="offset points",
                        ha="center", va="bottom",
                        fontsize=9, fontweight="bold", color="#1F2937")

        ax.set_title("Tiempo de Espera por Ticket en Cola - MatriculaApp (HuilaSoft)", fontsize=12, fontweight="bold", pad=15)
        ax.set_xlabel("Código del Ticket", fontsize=10, fontweight="bold", labelpad=8)
        ax.set_ylabel("Tiempo de Espera (minutos)", fontsize=10, fontweight="bold")
        ax.set_ylim(0, max(esperas) + 1.5 if esperas else 5)
        ax.grid(axis="y", linestyle=":", alpha=0.6, zorder=0)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.legend(frameon=True, facecolor="#F9FAFB", edgecolor="#D1D5DB")

        plt.tight_layout()
        plt.savefig(ruta, dpi=150)
        plt.close()