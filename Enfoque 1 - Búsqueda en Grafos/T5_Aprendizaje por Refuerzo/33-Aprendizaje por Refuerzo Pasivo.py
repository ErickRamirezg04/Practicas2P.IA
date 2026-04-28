#¿Qué es el Aprendizaje por Refuerzo Pasivo?
# A diferencia del aprendizaje activo (como Q-Learning), en el Refuerzo Pasivo la política del agente 
# es fija. El agente es un "observador" que simplemente intenta aprender la Función de Valor $V(s)$ de 
# los estados siguiendo un manual de instrucciones que ya le han dado.

# Conceptos clave:
# Estimación Monte Carlo: El agente espera a que el episodio termine para ver cuánta recompensa total 
# acumuló y luego reparte ese éxito entre los estados visitados.

# Retorno ($G$): Es la suma total de recompensas desde un momento dado hasta el final del episodio, 
# aplicando el factor de descuento.

# Promedio Incremental: La IA actualiza su creencia sobre el valor 
# de un estado usando la fórmula:$$V(s) \leftarrow V(s) + \frac{1}{N(s)} (G - V(s))$$Donde $G$ es el 
# retorno actual y $N(s)$ es el número de veces que hemos visto ese estado.
def analista_rutas_montecarlo(historial_viajes, gamma=0.9):
    """
    Estima el valor de cada ubicación observando viajes ya completados.
    """
    V = {}      # Tabla de valores estimados (Utilidad)
    conteo = {} # Frecuencia de visitas para el promedio

    print("--- INICIANDO ANÁLISIS DE RUTAS PASIVO (MONTE CARLO) ---")

    for i, episodio in enumerate(historial_viajes, 1):
        G = 0  # El retorno acumulado (ganancia total)

        # Recorremos el viaje en reversa para calcular el retorno fácilmente
        # El valor de un estado depende de lo que viene DESPUÉS de él.
        for estado, recompensa in reversed(episodio):
            # Ecuación de retorno: G_t = R_t + gamma * G_{t+1}
            G = recompensa + gamma * G

            if estado not in V:
                V[estado] = 0.0
                conteo[estado] = 0

            # Actualización del promedio incremental
            conteo[estado] += 1
            error_estimacion = G - V[estado]
            V[estado] += error_estimacion / conteo[estado]

        print(f" > Procesado Viaje #{i}: Retorno final calculado.")

    return V

# --- ESCENARIO: Rutas de Entrega ---
# Cada tupla es (Ubicación, Recompensa inmediata)
viajes_observados = [
    [("Almacén", -1), ("Centro_Ciudad", 2), ("Puerto", 50)],
    [("Almacén", -1), ("Periferia", 5), ("Puerto", 45)],
    [("Almacén", -2), ("Centro_Ciudad", 1), ("Puerto", 55)]
]

# --- EJECUCIÓN ---
utilidades_estimadas = analista_rutas_montecarlo(viajes_observados)

print("\n" + "="*50)
print(" RESULTADOS DEL APRENDIZAJE PASIVO ")
print("="*50)
for loc, val in sorted(utilidades_estimadas.items(), key=lambda x: x[1], reverse=True):
    print(f" Destino: {loc.ljust(15)} | Valor Esperado: {val:6.2f} pts")