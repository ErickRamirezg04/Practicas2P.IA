# =====================================================================
# HMM: ALGORITMO DE VITERBI (EL DECODIFICADOR)
# =====================================================================

def viterbi_decodificador():
    # 1. DEFINICIÓN DEL MUNDO
    estados = ['Pasillo', 'Oficina']
    observaciones = ['Luz', 'Sombra']
    
    prob_inicial = {'Pasillo': 0.5, 'Oficina': 0.5}
    
    # Probabilidad de moverse entre habitaciones
    transicion = {
        'Pasillo': {'Pasillo': 0.7, 'Oficina': 0.3},
        'Oficina': {'Pasillo': 0.4, 'Oficina': 0.6}
    }
    
    # Probabilidad de lo que el sensor ve en cada sitio
    emision = {
        'Pasillo': {'Luz': 0.8, 'Sombra': 0.2}, # El pasillo es iluminado
        'Oficina': {'Luz': 0.3, 'Sombra': 0.7}  # La oficina es oscura
    }

    # 2. SECUENCIA OBSERVADA (Lo que el robot reporta)
    secuencia_sensor = ['Luz', 'Sombra', 'Sombra']
    
    # 3. EL ALGORITMO
    T = len(secuencia_sensor)
    V = [{}] # Tabla de probabilidades de Viterbi
    camino = {} # Para reconstruir la ruta óptima

    # Paso Inicial (t=0)
    for s in estados:
        V[0][s] = prob_inicial[s] * emision[s][secuencia_sensor[0]]
        camino[s] = [s]

    # Pasos Siguientes (t=1 a T-1)
    for t in range(1, T):
        V.append({})
        nuevo_camino = {}

        for s_actual in estados:
            # Seleccionamos el camino previo que MAXIMIZA la probabilidad actual
            (prob, s_prev_mejor) = max(
                (V[t-1][s_prev] * transicion[s_prev][s_actual] * emision[s_actual][secuencia_sensor[t]], s_prev)
                for s_prev in estados
            )
            V[t][s_actual] = prob
            nuevo_camino[s_actual] = camino[s_prev_mejor] + [s_actual]
        
        camino = nuevo_camino

    # 4. RESULTADO FINAL
    (prob_final, mejor_estado_final) = max((V[T-1][s], s) for s in estados)
    ruta_optima = camino[mejor_estado_final]

    print(f"--- RECONSTRUCCIÓN DE TRAYECTORIA ---")
    print(f"Observaciones del sensor: {secuencia_sensor}")
    print(f"Ruta más probable: {' -> '.join(ruta_optima)}")
    print(f"Confianza de la ruta: {prob_final:.4f}")

# Ejecutar
viterbi_decodificador()