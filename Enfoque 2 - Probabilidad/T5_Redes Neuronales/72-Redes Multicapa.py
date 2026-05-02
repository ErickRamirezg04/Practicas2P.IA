#Las Redes Multicapa (o Multilayer Perceptrons - MLP) son la respuesta definitiva al problema de la 
# separabilidad lineal. Si un solo Perceptrón era una línea recta, una Red Multicapa es una estructura 
# capaz de moldearse a cualquier forma, convirtiéndose en un Aproximador Universal de Funciones.

#Al añadir una o más Capas Ocultas, la red deja de ver los datos crudos y empieza a crear sus propias 
# representaciones intermedias.

#La Anatomía de la Complejidad
#En una red multicapa, el flujo de información sigue este orden:

#Capa de Entrada: Recibe los estímulos (sensores, píxeles, etc.).

#Capas Ocultas: Aquí es donde se "dobla" el espacio. Las neuronas en estas capas combinan las entradas 
# para detectar patrones que no son evidentes a simple vista.

#Capa de Salida: Entrega la decisión final.

import math
import random

# =====================================================================
# RED MULTICAPA: RESOLVIENDO EL PROBLEMA XOR
# =====================================================================

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    return x * (1 - x)

# 1. DATOS XOR (No separables linealmente)
entradas = [[0,0], [0,1], [1,0], [1,1]]
objetivos = [[0], [1], [1], [0]]

# 2. ARQUITECTURA: 2 Entradas -> 2 Neuronas Ocultas -> 1 Salida
# Inicialización de pesos aleatorios
w_ocultos = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
w_salida = [random.uniform(-1, 1) for _ in range(2)]
bias_oculto = [random.uniform(-1, 1) for _ in range(2)]
bias_salida = random.uniform(-1, 1)

# 3. ENTRENAMIENTO (Backpropagation simplificado)
tasa = 0.5
for epoca in range(20000):
    for i in range(len(entradas)):
        # --- FORWARD PASS ---
        # Capa Oculta
        h = [sigmoide(sum(entradas[i][j] * w_ocultos[j][k] for j in range(2)) + bias_oculto[k]) for k in range(2)]
        # Capa Salida
        o = sigmoide(sum(h[j] * w_salida[j] for j in range(2)) + bias_salida)

        # --- BACKPROPAGATION ---
        error_salida = objetivos[i][0] - o
        delta_salida = error_salida * derivada_sigmoide(o)

        # Ajuste Pesos Salida
        for j in range(2):
            w_salida[j] += tasa * delta_salida * h[j]
        bias_salida += tasa * delta_salida

        # Ajuste Pesos Ocultos
        for k in range(2):
            error_oculto = delta_salida * w_salida[k]
            delta_oculto = error_oculto * derivada_sigmoide(h[k])
            for j in range(2):
                w_ocultos[j][k] += tasa * delta_oculto * entradas[i][j]
            bias_oculto[k] += tasa * delta_oculto

# 4. RESULTADOS
print("--- PRUEBA DE RED MULTICAPA (XOR) ---")
for i in range(len(entradas)):
    h = [sigmoide(sum(entradas[i][j] * w_ocultos[j][k] for j in range(2)) + bias_oculto[k]) for k in range(2)]
    o = sigmoide(sum(h[j] * w_salida[j] for j in range(2)) + bias_salida)
    print(f"Entrada: {entradas[i]} -> Predicción: {round(o, 4)}")