#¿Qué hace el Algoritmo Forward-Backward?
# Este algoritmo combina dos flujos de información:
# Paso Hacia Adelante (Forward): Calcula la probabilidad de estar en un estado en el tiempo $t$ 
# basado en la evidencia pasada (Filtrado).
# Paso Hacia Atrás (Backward): Calcula la probabilidad de que ocurran las evidencias futuras dado 
# que estamos en un estado en el tiempo $t$.
# Al multiplicar ambos, obtenemos el Suavizado: una estimación mucho más precisa de lo que ocurrió en 
# el pasado, porque ahora sabemos cómo terminó la historia.

# --- MOTOR FORWARD-BACKWARD (SUAVIZADO) ---

def forward_backward(observaciones, estados, p_inicial, transicion, emision):
    """
    Calcula la probabilidad suavizada de cada estado en cada momento del tiempo.
    """
    T = len(observaciones)
    N = len(estados)
    
    # 1. PASO FORWARD (Hacia adelante)
    # fw[t][s] = P(estado s en t | obs 0:t)
    fw = [{}] * T
    for s in estados:
        fw[0][s] = p_inicial[s] * emision[s][observaciones[0]]
        
    for t in range(1, T):
        fw[t] = {}
        for s_actual in estados:
            prob_venida = sum(fw[t-1][s_prev] * transicion[s_prev][s_actual] for s_prev in estados)
            fw[t][s_actual] = prob_venida * emision[s_actual][observaciones[t]]
        # Normalización para evitar números infinitesimales
        norm = sum(fw[t].values())
        for s in estados: fw[t][s] /= norm

    # 2. PASO BACKWARD (Hacia atrás)
    # bw[t][s] = P(obs t+1:T | estado s en t)
    bw = [{}] * T
    for s in estados:
        bw[T-1][s] = 1.0 # Caso base: el futuro después del final es 100%
        
    for t in range(T-2, -1, -1):
        bw[t] = {}
        for s_actual in estados:
            bw[t][s_actual] = sum(transicion[s_actual][s_siguiente] * emision[s_siguiente][observaciones[t+1]] * bw[t+1][s_siguiente] for s_siguiente in estados)
        # Normalización
        norm = sum(bw[t].values())
        for s in estados: bw[t][s] /= norm

    # 3. COMBINACIÓN (SUAVIZADO)
    suavizado = []
    for t in range(T):
        prob_t = {s: fw[t][s] * bw[t][s] for s in estados}
        norm = sum(prob_t.values())
        suavizado.append({s: p / norm for s, p in prob_t.items()})
        
    return suavizado

# --- CONFIGURACIÓN DEL ESCENARIO ---
# Estados: 'Compras' o 'Paseo' | Observaciones: 'Bolsa', 'Vacio'
estados = ['Compras', 'Paseo']
p_ini = {'Compras': 0.5, 'Paseo': 0.5}

trans = {
    'Compras': {'Compras': 0.7, 'Paseo': 0.3},
    'Paseo':   {'Compras': 0.2, 'Paseo': 0.8}
}

emis = {
    'Compras': {'Bolsa': 0.8, 'Vacio': 0.2},
    'Paseo':   {'Bolsa': 0.1, 'Vacio': 0.9}
}

# Secuencia observada: El usuario empezó con manos vacías, pero luego tuvo bolsas
secuencia = ['Vacio', 'Vacio', 'Bolsa', 'Bolsa']

# Ejecución
print("--- ANALIZANDO HISTORIAL CON FORWARD-BACKWARD ---")
resultados = forward_backward(secuencia, estados, p_ini, trans, emis)

for t, prob in enumerate(resultados):
    estado_top = max(prob, key=prob.get)
    print(f"Tiempo {t} (Obs: {secuencia[t]}): IA concluye que estaba en '{estado_top}' (Prob: {prob[estado_top]:.2%})")