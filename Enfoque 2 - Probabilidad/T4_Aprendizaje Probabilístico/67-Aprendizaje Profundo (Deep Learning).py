#¿Qué hace que el aprendizaje sea "Profundo"?
# Un modelo se considera "profundo" cuando tiene múltiples capas ocultas entre la entrada y la salida. 
# Cada capa actúa como un filtro que transforma los datos en una representación más abstracta.
# Neurona (Perceptrón): La unidad básica que suma entradas con pesos ($w$), añade un sesgo ($b$) y 
# aplica una función de activación (como ReLU o Sigmoide).
# Capas Ocultas: Donde ocurre la "magia". Cuantas más capas, más complejos son los patrones que puede 
# captar.
# Retropropagación (Backpropagation): Es el mecanismo de aprendizaje. La red comete un error, 
# calcula qué tan lejos está de la verdad y ajusta los pesos de todas las neuronas hacia atrás para 
# no fallar la próxima vez.

import math
import random

# =====================================================================
# DEEP LEARNING: RED NEURONAL MANUAL (SIN LIBRERÍAS)
# =====================================================================

def sigmoide(x):
    """Función de activación para introducir no-linealidad."""
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    """Necesaria para el ajuste de pesos (Backpropagation)."""
    return x * (1 - x)

# 1. DATOS (Lógica XOR: diferentes dan 1, iguales dan 0)
entradas = [[0,0], [0,1], [1,0], [1,1]]
salidas_esperadas = [[0], [1], [1], [0]]

# 2. INICIALIZACIÓN DE PESOS (Capa Oculta y Capa Salida)
# 2 entradas -> 3 neuronas ocultas -> 1 salida
random.seed(42)
w_ocultos = [[random.uniform(-1, 1) for _ in range(3)] for _ in range(2)]
w_salida = [[random.uniform(-1, 1)] for _ in range(3)]

# 3. ENTRENAMIENTO (Mil iteraciones de aprendizaje)
print("Entrenando red neuronal profunda...")
for epoca in range(10000):
    for i in range(len(entradas)):
        # --- PASO 1: Forward (Propagación hacia adelante) ---
        capa_entrada = entradas[i]
        
        # Capa Oculta
        suma_oculta = [sum(capa_entrada[j] * w_ocultos[j][k] for j in range(2)) for k in range(3)]
        activacion_oculta = [sigmoide(s) for s in suma_oculta]
        
        # Capa Salida
        suma_final = sum(activacion_oculta[j] * w_salida[j][0] for j in range(3))
        prediccion = sigmoide(suma_final)
        
        # --- PASO 2: Backpropagation (Aprendizaje) ---
        error = salidas_esperadas[i][0] - prediccion
        
        # Ajuste pesos salida
        delta_salida = error * derivada_sigmoide(prediccion)
        for j in range(3):
            w_salida[j][0] += activacion_oculta[j] * delta_salida * 0.1 # 0.1 = Tasa de aprendizaje
            
        # Ajuste pesos ocultos
        for j in range(2):
            for k in range(3):
                delta_oculto = delta_salida * w_salida[k][0] * derivada_sigmoide(activacion_oculta[k])
                w_ocultos[j][k] += capa_entrada[j] * delta_oculto * 0.1

# 4. PRUEBA FINAL
print("\n--- RESULTADOS TRAS EL APRENDIZAJE ---")
for x in entradas:
    s_oc = [sigmoide(sum(x[j] * w_ocultos[j][k] for j in range(2))) for k in range(3)]
    pred = sigmoide(sum(s_oc[j] * w_salida[j][0] for j in range(3)))
    print(f"Entrada: {x} -> Predicción: {round(pred, 2)}")