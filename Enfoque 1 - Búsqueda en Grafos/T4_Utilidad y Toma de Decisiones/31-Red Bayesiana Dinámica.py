#¿Qué es una Red Bayesiana Dinámica (DBN)?
# Una DBN es una red bayesiana que representa secuencias de variables aleatorias. Es la evolución 
# de los Modelos Ocultos de Márkov (HMM), permitiendo representar estados complejos con múltiples 
# variables que interactúan entre sí.

# Conceptos fundamentales:
# Estado Oculto ($X_t$): La realidad que no podemos ver directamente (ej. si llueve o hace viento en 
# el exterior).Modelo de Transición: Describe cómo cambia el mundo de un paso al siguiente. Se basa 
# en la Propiedad de Márkov: el futuro solo depende del presente, no del pasado remoto.
# Modelo de Sensor (Observación): Describe la probabilidad de ver una evidencia (ej. el paraguas) 
# dado el estado real.
# Filtrado: El proceso de actualizar nuestra creencia sobre el estado actual a medida que llega 
# nueva información cada día.

print("--- SISTEMA DE INFERENCIA CLIMÁTICA DINÁMICA ---")

# 1. MODELO DE TRANSICIÓN: ¿Cómo evoluciona el clima de ayer a hoy?
def modelo_evolucion(lluvia_hoy, viento_hoy, lluvia_ayer, viento_ayer):
    # La lluvia tiene inercia: si ayer llovió, es probable que hoy también.
    p_lluvia = 0.7 if lluvia_ayer == lluvia_hoy else 0.3
    # El viento es más persistente:
    p_viento = 0.8 if viento_ayer == viento_hoy else 0.2
    
    return p_lluvia * p_viento

# 2. MODELO DE OBSERVACIÓN: Probabilidad de ver el paraguas según el clima
def verosimilitud_evidencia(paraguas, lluvia, viento):
    if lluvia and viento:      p = 0.50 # Difícil de usar con viento fuerte
    elif lluvia and not viento: p = 0.90 # Caso ideal para paraguas
    elif not lluvia and viento: p = 0.05 # Solo por protección del viento (raro)
    else:                       p = 0.01 # Olvido o error
    
    return p if paraguas else (1.0 - p)

# 3. CREENCIAS INICIALES (Día 0)
# Distribución uniforme: no sabemos nada.
creencia = {(ll, vi): 0.25 for ll in [True, False] for vi in [True, False]}

def paso_de_tiempo_dbn(creencia_pasada, evidencia_hoy):
    """Realiza la actualización Bayesiana Dinámica: Predicción + Corrección."""
    nueva_creencia = {}
    
    for ll_h in [True, False]:
        for vi_h in [True, False]:
            # --- PASO 1: PREDICCIÓN (Inferencia hacia adelante) ---
            # Sumamos las probabilidades de todos los caminos que llegan a este estado
            prob_predicha = sum(
                modelo_evolucion(ll_h, vi_h, ll_a, vi_a) * creencia_pasada[(ll_a, vi_a)]
                for ll_a in [True, False] for vi_a in [True, False]
            )
            
            # --- PASO 2: CORRECCIÓN (Incorporar la evidencia actual) ---
            prob_evidencia = verosimilitud_evidencia(evidencia_hoy, ll_h, vi_h)
            nueva_creencia[(ll_h, vi_h)] = prob_evidencia * prob_predicha
            
    # --- PASO 3: NORMALIZACIÓN ---
    total = sum(nueva_creencia.values())
    return {estado: p / total for estado, p in nueva_creencia.items()}

# --- SIMULACIÓN MULTI-DÍA ---
observaciones = [True, True, False] # Paraguas, Paraguas, No paraguas

for i, obs in enumerate(observaciones, 1):
    creencia = paso_de_tiempo_dbn(creencia, obs)
    
    print(f"\n[Día {i}] Reporte: {'Paraguas detectado' if obs else 'Sin paraguas'}")
    # Ordenar por probabilidad para mostrar lo más creíble
    for (ll, vi), prob in sorted(creencia.items(), key=lambda x: x[1], reverse=True):
        txt = f"{'Lluvia' if ll else 'Seco'} & {'Viento' if vi else 'Calma'}"
        print(f"  {txt.ljust(15)}: {prob*100:5.2f}% {'█' * int(prob*20)}")