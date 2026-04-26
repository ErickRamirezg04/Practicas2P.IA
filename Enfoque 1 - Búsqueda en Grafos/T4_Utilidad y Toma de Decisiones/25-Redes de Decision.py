#¿Qué es una Red de Decisión?
#Una Red de Decisión es una extensión de las Redes Bayesianas que integra la capacidad de razonar 
# sobre acciones y valores. Es una herramienta gráfica que permite a la IA visualizar cómo las 
# decisiones interactúan con el azar y el beneficio final.

#Se compone de tres tipos de nodos:

#Nodos de Decisión (Rectángulos): Acciones que el agente puede elegir.

#Nodos de Azar (Óvalos): Variables aleatorias del entorno que el agente no controla.

#Nodos de Utilidad (Diamantes): Representan la función de recompensa del agente basándose en el 
# resultado final.

# 1. NODOS DE DECISIÓN: Las opciones del Director de Vuelo
protocolos = ['Lanzar Cohete', 'Abortar Misión']

# 2. NODOS DE AZAR: Variables climáticas fuera de nuestro control
clima_orbital = ['Estable', 'Tormenta Eléctrica']

# Evidencia de telemetría: El radar indica un 70% de riesgo de tormenta.
probabilidad_radar = {
    'Tormenta Eléctrica': 0.70,
    'Estable': 0.30
}

# 3. NODO DE UTILIDAD (DIAMANTE): Impacto en el éxito de la agencia
# Mapea (Protocolo, Clima) -> Valor de éxito/pérdida
matriz_utilidad = {
    ('Lanzar Cohete', 'Estable'): 100,      # ÉXITO TOTAL: Satélite en órbita
    ('Lanzar Cohete', 'Tormenta Eléctrica'): -500, # DESASTRE: Pérdida del equipo
    ('Abortar Misión', 'Estable'): -10,     # PÉRDIDA LEVE: Retraso y costos de combustible
    ('Abortar Misión', 'Tormenta Eléctrica'): 20    # PRUDENCIA: Se salvó el equipo de un rayo
}

def motor_inferencia_decision(datos_entorno):
    print("--- PROCESANDO RED DE DECISIÓN AEROESPACIAL ---")
    print(f"Telemetría actual: Riesgo de Tormenta al {datos_entorno['Tormenta Eléctrica']*100}%")
    print("-" * 50)
    
    max_eu = float('-inf')
    decision_optima = None
    
    # 4. Evaluación de la Utilidad Esperada (EU)
    for opcion in protocolos:
        eu_actual = 0
        print(f"\n[Analizando Nodo de Decisión: '{opcion}']")
        
        for estado in clima_orbital:
            p = datos_entorno[estado]
            u = matriz_utilidad[(opcion, estado)]
            
            # Cálculo: EU = Σ P(resultado|accion) * U(resultado)
            aporte = p * u
            eu_actual += aporte
            
            print(f"  -> Escenario '{estado}' (P={p}): U={u} | Ponderación: {aporte:.2f}")
            
        print(f"  [*] Utilidad Esperada (EU) para '{opcion}': {eu_actual:.2f}")
        
        # 5. Maximización de la Utilidad Esperada (MEU)
        if eu_actual > max_eu:
            max_eu = eu_actual
            decision_optima = opcion
            
    return decision_optima, max_eu

# --- EJECUCIÓN DE CONTROL DE MISIÓN ---
mision_final, valor_esperado = motor_inferencia_decision(probabilidad_radar)

print("\n" + "=" * 50)
print(" 🚀 PROTOCOLO FINAL DE INTELIGENCIA RACIONAL ")
print("=" * 50)
print(f"RECOMENDACIÓN: {mision_final.upper()}")
print(f"UTILIDAD ESPERADA PROYECTADA: {valor_esperado:.2f} unidades.")