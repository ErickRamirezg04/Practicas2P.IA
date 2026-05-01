#El Algoritmo de Viterbi y el Habla
#En el reconocimiento de voz, el sonido es una señal continua que dividimos en pequeños fragmentos 
# llamados observaciones (fonemas o rasgos acústicos). El problema es que el sonido es ruidoso: una 
# "o" puede sonar como una "a" dependiendo del acento o del ruido de fondo.

#¿Cómo lo resuelve Viterbi?
#A diferencia del algoritmo Forward (que sumaba todas las probabilidades), Viterbi busca el camino 
#máximo. Es un algoritmo de programación dinámica que responde: "¿Cuál es la secuencia de estados 
# más probable que explica este sonido?".

# =====================================================================
# 1. DEFINICIÓN DE LOS MODELOS (DICCIONARIOS)
# =====================================================================

ESTADOS = ['S1', 'S2', 'S3']

# Modelo para la palabra "HOLA"
HMM_HOLA = {
    'PI': {'S1': 1.0, 'S2': 0.0, 'S3': 0.0},
    'TRANSICION': {
        'S1': {'S1': 0.1, 'S2': 0.9, 'S3': 0.0},
        'S2': {'S1': 0.0, 'S2': 0.1, 'S3': 0.9},
        'S3': {'S1': 0.0, 'S2': 0.0, 'S3': 1.0}
    },
    'EMISION': {
        'S1': {'o': 0.8, 'a': 0.1, 'i': 0.1},
        'S2': {'o': 0.2, 'a': 0.7, 'i': 0.1},
        'S3': {'o': 0.1, 'a': 0.2, 'i': 0.7}
    }
}

# Modelo para la palabra "ADIOS"
HMM_ADIOS = {
    'PI': {'S1': 1.0, 'S2': 0.0, 'S3': 0.0},
    'TRANSICION': {
        'S1': {'S1': 0.2, 'S2': 0.8, 'S3': 0.0},
        'S2': {'S1': 0.0, 'S2': 0.2, 'S3': 0.8},
        'S3': {'S1': 0.0, 'S2': 0.0, 'S3': 1.0}
    },
    'EMISION': {
        'S1': {'a': 0.7, 'o': 0.2, 'i': 0.1},
        'S2': {'i': 0.7, 'a': 0.2, 'o': 0.1},
        'S3': {'o': 0.7, 'a': 0.1, 'i': 0.2}
    }
}

# =====================================================================
# 2. EL ALGORITMO DE VITERBI
# =====================================================================

def viterbi(secuencia, modelo):
    V = [{}] 
    camino = {}

    # Inicialización
    for s in ESTADOS:
        V[0][s] = modelo['PI'][s] * modelo['EMISION'][s].get(secuencia[0], 0.0001)
        camino[s] = [s]

    # Recursión
    for t in range(1, len(secuencia)):
        V.append({})
        nuevo_camino = {}
        for s_actual in ESTADOS:
            (prob, s_prev_mejor) = max(
                (V[t-1][s_prev] * modelo['TRANSICION'][s_prev][s_actual] * modelo['EMISION'][s_actual].get(secuencia[t], 0.0001), s_prev)
                for s_prev in ESTADOS
            )
            V[t][s_actual] = prob
            nuevo_camino[s_actual] = camino[s_prev_mejor] + [s_actual]
        camino = nuevo_camino

    prob_final, estado_final = max((V[-1][s], s) for s in ESTADOS)
    return prob_final

# =====================================================================
# 3. MOTOR DE RECONOCIMIENTO
# =====================================================================

def motor_reconocimiento(sonidos):
    # Ahora HMM_HOLA y HMM_ADIOS ya existen arriba, no habrá error
    p_hola = viterbi(sonidos, HMM_HOLA)
    p_adios = viterbi(sonidos, HMM_ADIOS)

    print(f"\nEntrada acústica: {'-'.join(sonidos)}")
    print(f"Confianza 'HOLA':  {p_hola:.8f}")
    print(f"Confianza 'ADIOS': {p_adios:.8f}")
    
    ganador = "HOLA" if p_hola > p_adios else "ADIOS"
    print(f"🧠 Resultado: La IA ha escuchado '{ganador}'")

# --- Ejecución ---
if __name__ == "__main__":
    motor_reconocimiento(['o', 'a', 'i']) # Debería detectar HOLA
    motor_reconocimiento(['a', 'i', 'o']) # Debería detectar ADIOS