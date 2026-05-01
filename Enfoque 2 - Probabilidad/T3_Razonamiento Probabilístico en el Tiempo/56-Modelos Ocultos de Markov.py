#¿Qué es un Modelo Oculto de Markov (HMM)?
# Un HMM es un modelo estadístico en el que se asume que el sistema es un proceso de Markov con 
# estados no observados (ocultos). Aunque no vemos el estado, este "emite" señales que sí podemos 
# ver (observaciones).

# Se compone de tres pilares:
# Matriz de Transición: La probabilidad de que el clima cambie (ej. de Soleado a Lluvioso).
# Matriz de Emisión: La probabilidad de observar una conducta dado un clima (ej. si llueve, es 
# probable observar "limpiar").
# Probabilidades Iniciales ($\pi$): Cómo creemos que empieza el mundo.

# =====================================================================
# DETECTIVE CLIMÁTICO: MODELO OCULTO DE MARKOV (HMM)
# =====================================================================

ESTADOS = ['Lluvioso', 'Soleado']
# El 'Estado' es lo que no vemos (el clima dentro de una casa sin ventanas)

PI = {'Lluvioso': 0.6, 'Soleado': 0.4}

TRANSICION = {
    'Lluvioso': {'Lluvioso': 0.7, 'Soleado': 0.3},
    'Soleado':  {'Lluvioso': 0.4, 'Soleado': 0.6}
}

EMISION = {
    'Lluvioso': {'caminar': 0.1, 'comprar': 0.4, 'limpiar': 0.5},
    'Soleado':  {'caminar': 0.6, 'comprar': 0.3, 'limpiar': 0.1}
}

def calcular_probabilidad_forward(secuencia):
    """
    Calcula la probabilidad acumulada de una secuencia de observaciones.
    """
    # alpha[t][estado] representa la prob. de estar en 'estado' habiendo 
    # observado la secuencia hasta el tiempo 't'.
    alpha = []

    # 1. INICIALIZACIÓN (Tiempo 0)
    # P(Estado) * P(Observación | Estado)
    alpha_0 = {s: PI[s] * EMISION[s][secuencia[0]] for s in ESTADOS}
    alpha.append(alpha_0)

    # 2. RECURSIÓN (Avanzar en el tiempo)
    for t in range(1, len(secuencia)):
        alpha_t = {}
        for s_actual in ESTADOS:
            # Sumamos las probabilidades de todos los caminos que llegan aquí
            prob_llegada = sum(alpha[t-1][s_prev] * TRANSICION[s_prev][s_actual] for s_prev in ESTADOS)
            # Multiplicamos por la evidencia actual (Emisión)
            alpha_t[s_actual] = prob_llegada * EMISION[s_actual][secuencia[t]]
        alpha.append(alpha_t)

    # 3. TERMINACIÓN
    prob_total = sum(alpha[-1].values())
    
    return alpha, prob_total

# --- SIMULACIÓN ---
observaciones = ['caminar', 'comprar', 'limpiar']
pasos, total = calcular_probabilidad_forward(observaciones)

print(f"--- ANÁLISIS DE SECUENCIA: {observaciones} ---")
for i, p in enumerate(pasos):
    print(f"Tiempo {i}: {p}")

print(f"\n>> PROBABILIDAD TOTAL DE ESTA RUTA: {total:.6f}")