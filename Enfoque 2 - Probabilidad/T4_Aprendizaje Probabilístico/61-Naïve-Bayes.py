#¿Por qué es "Ingenuo"?
#Se le llama Naïve (ingenuo) porque asume que todas las características (clima, temperatura, etc.) 
# son totalmente independientes entre sí para una clase dada.

#En el mundo real, sabemos que el clima y la temperatura suelen estar relacionados (si está nevando, 
# probablemente hace frío), pero Naïve Bayes ignora esa conexión. Sorprendentemente, a pesar de esta 
# "mentira" matemática, el algoritmo funciona increíblemente bien para clasificar texto, correos y 
# diagnósticos médicos.

# =====================================================================
# CLASIFICADOR NAÏVE BAYES: ¿Saldré a correr hoy?
# =====================================================================

# Dataset de entrenamiento: (Clima, Temperatura) -> ¿Hizo actividad?
historial_entrenamiento = [
    ('soleado', 'calor', 'no'),
    ('soleado', 'calor', 'no'),
    ('nublado', 'calor', 'si'),
    ('lluvia', 'templado', 'si'),
    ('lluvia', 'frio', 'si'),
    ('lluvia', 'frio', 'no'),
    ('nublado', 'frio', 'si'),
    ('soleado', 'templado', 'no'),
    ('soleado', 'frio', 'si'),
    ('lluvia', 'templado', 'si')
]

def entrenar_modelo(datos):
    """Calcula las frecuencias de cada característica por clase."""
    modelo = {'si': {'total': 0, 'clima': {}, 'temp': {}}, 
              'no': {'total': 0, 'clima': {}, 'temp': {}}}
    
    for clima, temp, clase in datos:
        modelo[clase]['total'] += 1
        modelo[clase]['clima'][clima] = modelo[clase]['clima'].get(clima, 0) + 1
        modelo[clase]['temp'][temp] = modelo[clase]['temp'].get(temp, 0) + 1
        
    return modelo, len(datos)

def predecir_actividad(modelo, total_muestras, clima_hoy, temp_hoy):
    """Aplica la regla de Bayes para clasificar."""
    evidencias = {}
    
    for clase, stats in modelo.items():
        # 1. Probabilidad a priori: P(Clase)
        p_clase = stats['total'] / total_muestras
        
        # 2. Verosimilitud: P(Característica | Clase)
        # Usamos 0.0001 como un suavizado simple para evitar multiplicar por cero
        p_clima = stats['clima'].get(clima_hoy, 0.0001) / stats['total']
        p_temp = stats['temp'].get(temp_hoy, 0.0001) / stats['total']
        
        # 3. Naive Bayes: P(Clase | Evidencia) ∝ P(Clase) * P(Clima|Clase) * P(Temp|Clase)
        evidencias[clase] = p_clase * p_clima * p_temp
        
    return evidencias

# --- EJECUCIÓN ---
conocimiento, n_total = entrenar_modelo(historial_entrenamiento)

# Caso de prueba: Un día soleado pero frío
hoy = ('soleado', 'frio')
scores = predecir_actividad(conocimiento, n_total, hoy[0], hoy[1])

print(f"--- PREDICCIÓN NAÏVE BAYES ---")
print(f"Condiciones: {hoy[0]} y {hoy[1]}")
for c, s in scores.items():
    print(f" > Score para '{c}': {s:.6f}")

ganador = max(scores, key=scores.get)
print(f"\nResultado: La IA predice que '{ganador.upper()}' harás actividad.")