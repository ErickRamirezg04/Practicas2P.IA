#¿Qué es la Iteración de Valores?
# Es un algoritmo de Aprendizaje por Refuerzo que permite a una IA calcular la utilidad a largo 
# plazo de estar en un estado específico. A diferencia de las búsquedas simples, aquí la IA asume 
# que el mundo es estocástico (aleatorio): tus acciones pueden fallar.

# Los pilares del algoritmo:
# Ecuación de Bellman: Es la fórmula mágica que dice: "El valor de este sitio es la recompensa 
# inmediata más el valor descontado del mejor sitio al que puedo ir después".
# $$U(s) = R(s) + \gamma \max_{a \in A} \sum_{s'} P(s' | s, a) U(s')$$
# Factor de Descuento ($\gamma$): Un número entre 0 y 1 que define qué tan "paciente" es la IA. 
# Si es 0.9, prefiere recompensas pronto; si es 0.1, es extremadamente cortoplacista.
# Convergencia: El algoritmo repite los cálculos hasta que los valores de los estados dejan de 
# cambiar significativamente.

import copy

# --- CONFIGURACIÓN DEL ENTORNO MDP ---
estados = ['Entrada', 'Plataforma_Hielo', 'Cámara_Tesoro', 'Abismo']

# Recompensas R(s): El costo de moverse vs el premio final
recompensas = {
    'Entrada': -1.0,
    'Plataforma_Hielo': -2.0, # El frío drena energía
    'Cámara_Tesoro': 100.0,
    'Abismo': -100.0
}

estados_finales = ['Cámara_Tesoro', 'Abismo']
acciones = ['Avanzar', 'Retroceder']

# Modelo de Transición P(s' | s, a): Probabilidades de éxito/fallo
transiciones = {
    'Entrada': {
        'Avanzar': [(0.9, 'Plataforma_Hielo'), (0.1, 'Entrada')],
        'Retroceder': [(1.0, 'Entrada')]
    },
    'Plataforma_Hielo': {
        # El hielo es resbaladizo: 70% éxito, 30% caída fatal
        'Avanzar': [(0.7, 'Cámara_Tesoro'), (0.3, 'Abismo')],
        'Retroceder': [(1.0, 'Entrada')]
    }
}

# Parámetros de Aprendizaje
gamma = 0.9    # Importancia del futuro
epsilon = 0.01 # Precisión deseada

def simulador_aprendizaje_bellman():
    """Calcula la utilidad de la cueva mediante iteración de valores."""
    # Inicializamos utilidades en 0
    U = {s: 0.0 for s in estados}
    paso = 0

    print("--- Iniciando Mapeo de Utilidad de la Cueva ---")

    while True:
        U_nueva = copy.deepcopy(U)
        delta = 0

        for s in estados:
            if s in estados_finales:
                U_nueva[s] = recompensas[s]
                continue

            # Buscamos la acción que maximiza la utilidad esperada
            mejor_valor_accion = float('-inf')
            for a in acciones:
                # Sumatoria de Bellman: Σ P(s'|s,a) * U(s')
                valor_esperado = sum(prob * U[dest] for prob, dest in transiciones[s][a])
                mejor_valor_accion = max(mejor_valor_accion, valor_esperado)

            # Aplicamos actualización: U(s) = R(s) + γ * Max(EU)
            U_nueva[s] = recompensas[s] + gamma * mejor_valor_accion
            delta = max(delta, abs(U_nueva[s] - U[s]))

        U = U_nueva
        paso += 1
        
        if delta < epsilon:
            print(f"[*] Mapa mental completado en {paso} ciclos evolutivos.")
            break

    return U

# --- EJECUCIÓN Y POLÍTICA ---
utilidades_finales = simulador_aprendizaje_bellman()

print("\n" + "="*55)
print(" MAPA DE UTILIDAD FINAL (VALORES DE ESTADO) ")
print("="*55)
for s, v in utilidades_finales.items():
    print(f" {s.ljust(18)} : {v:8.2f} pts")

print("\n--- GENERANDO POLÍTICA ÓPTIMA (Estrategia de Vuelo) ---")
for s in estados:
    if s in estados_finales: continue
    
    # La IA elige la acción que apunta al vecino con mayor utilidad
    mejor_a = max(acciones, key=lambda a: sum(p * utilidades_finales[d] for p, d in transiciones[s][a]))
    print(f" En '{s}': La recomendación racional es {mejor_a.upper()}")