#¿Qué es un POMDP?
# Un POMDP es la evolución del MDP para el mundo real. En un MDP normal, el robot siempre sabe en qué 
# casilla está. En un POMDP, el robot está "ciego": solo tiene un Estado de Creencia (Belief State), 
# que es una distribución de probabilidad sobre dónde podría estar.

# Los componentes clave son:
# Estado de Creencia ($b$): Una lista de probabilidades que suman 100%. Representa la "fe" del robot 
# en su ubicación.Modelo de Observación ($Z$ o $O$): Describe qué tan ruidosos son los sensores. 
# Por ejemplo: "Si estoy en la meta, mi sensor pita el 80% de las veces".
# Ciclo de Actualización:Predicción: Si me muevo a la derecha, mi creencia se desplaza a la derecha.
# Corrección (Actualización Bayesiana): Si mi sensor detecta algo, aumento la probabilidad de los 
# estados que coinciden con esa señal y disminuyo el resto.

# --- CONFIGURACIÓN DEL SECTOR SUBMARINO ---
# El objetivo (el náufrago) está en el Sector_2
sectores = ['Sector_1', 'Sector_2', 'Sector_3']

def modelo_fisico_helice(origen, maniobra):
    """P(s' | s, a): Los motores no son perfectos (corrientes marinas)."""
    if maniobra == 'Avanzar':
        if origen == 'Sector_1': return {'Sector_2': 0.85, 'Sector_1': 0.15}
        if origen == 'Sector_2': return {'Sector_3': 0.85, 'Sector_2': 0.15}
        if origen == 'Sector_3': return {'Sector_3': 1.0}
    return {origen: 1.0}

def sonar_probabilidad(lectura, sector_real):
    """O(o | s): El sonar puede confundir rocas con el objetivo."""
    if sector_real == 'Sector_2':
        # En el sector del objetivo, el sonar es 75% preciso
        return 0.75 if lectura == 'Eco_Objetivo' else 0.25
    else:
        # En otros sectores, suele dar 'Eco_Vacio' (90% precisión)
        return 0.90 if lectura == 'Eco_Vacio' else 0.10

# 1. ESTADO DE CREENCIA INICIAL (Incertidumbre Total)
# El submarino no tiene idea de dónde lo soltaron.
creencia = {s: 1.0/len(sectores) for s in sectores}

def filtro_bayesiando_creencia(creencia_actual, accion, señal_sonar):
    """Actualiza el mapa mental del submarino usando Bayes."""
    nueva_b = {s: 0.0 for s in sectores}
    
    for s_post in sectores:
        # A) PASO DE PREDICCIÓN: ¿A dónde me llevó mi hélice?
        prob_transito = 0
        for s_pre in sectores:
            p_movimiento = modelo_fisico_helice(s_pre, accion).get(s_post, 0.0)
            prob_transito += p_movimiento * creencia_actual[s_pre]
            
        # B) PASO DE EVIDENCIA: ¿Qué dice el sonar sobre estar en s_post?
        prob_evidencia = sonar_probabilidad(señal_sonar, s_post)
        
        # C) COMBINACIÓN: Creencia = Prob_Movimiento * Prob_Sensor
        nueva_b[s_post] = prob_evidencia * prob_transito
        
    # NORMALIZACIÓN: Asegurar que todas las probabilidades sumen 1
    total = sum(nueva_b.values())
    return {s: p/total for s, p in nueva_b.items()}

# --- SIMULACIÓN DE NAVEGACIÓN ---

def mostrar_radar(paso, b):
    print(f"\n[PASO {paso}] Probabilidades de ubicación:")
    for s, p in b.items():
        visual = "▒" * int(p * 30)
        print(f"  {s.ljust(10)}: {p*100:6.2f}% {visual}")

# Estado inicial: Ciego
mostrar_radar(0, creencia)

# El submarino avanza y el sonar dice que no hay nada
accion_1 = 'Avanzar'
sonar_1 = 'Eco_Vacio'
print(f"\n[*] Ejecutando: {accion_1} | Sonar reporta: {sonar_1}")
creencia = filtro_bayesiando_creencia(creencia, accion_1, sonar_1)
mostrar_radar(1, creencia)

# El submarino avanza de nuevo y ¡BING! Detecta algo
accion_2 = 'Avanzar'
sonar_2 = 'Eco_Objetivo'
print(f"\n[*] Ejecutando: {accion_2} | Sonar reporta: {sonar_2}")
creencia = filtro_bayesiando_creencia(creencia, accion_2, sonar_2)
mostrar_radar(2, creencia)