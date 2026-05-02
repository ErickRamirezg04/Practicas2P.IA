#Llegamos al motor que hace posible el aprendizaje en las redes neuronales modernas: la Retropropagación
#  del Error (Backpropagation). Si la red fuera un estudiante, el "Forward Pass" es cuando hace el 
# examen y el "Backpropagation" es cuando el profesor le entrega la corrección y el estudiante analiza 
# exactamente en qué paso de cada ejercicio se equivocó para no repetirlo.

#En términos matemáticos, es una aplicación magistral de la Regla de la Cadena del cálculo para 
# encontrar el gradiente de la función de pérdida con respecto a cada peso de la red.

#¿Cómo funciona el flujo de aprendizaje?
#Propagación hacia adelante (Forward): Los datos entran, se multiplican por los pesos, pasan por las 
# activaciones y generan una predicción.

#Cálculo del Error: Comparamos la predicción con el valor real usando una función de pérdida (como el 
# Error Cuadrático Medio).

#Propagación hacia atrás (Backward): El error viaja desde la salida hacia la entrada.

#Calculamos cuánto contribuyó cada neurona al error total.

#Ajustamos los pesos en la dirección opuesta al gradiente (Descenso de Gradiente) para reducir el 
# error.

import math

# =====================================================================
# EL ALGORITMO DE BACKPROPAGATION (PASO A PASO)
# =====================================================================

def sigmoide(x):
    return 1 / (1 + math.exp(-x))

def derivada_sigmoide(x):
    # La derivada de la sigmoide en términos de su salida
    return x * (1 - x)

# --- Configuración Inicial ---
x = [0.5, 0.1]       # Entrada
y_real = 0.7         # Lo que queremos obtener
w_oculto = [0.2, -0.4] # Pesos capa oculta
w_salida = 0.6       # Peso capa salida
tasa_aprendizaje = 0.1

# 1. FORWARD PASS
# Neurona oculta
z1 = x[0]*w_oculto[0] + x[1]*w_oculto[1]
a1 = sigmoide(z1)

# Neurona salida
z2 = a1 * w_salida
prediccion = sigmoide(z2)

print(f"Predicción inicial: {prediccion:.4f} (Objetivo: {y_real})")

# 2. BACKPROPAGATION
# A. Error en la salida
error_total = y_real - prediccion

# B. Gradiente en la salida (Delta Salida)
# Error * Derivada de la activación
delta_salida = error_total * derivada_sigmoide(prediccion)

# C. Error en la capa oculta (Repartiendo la culpa)
# Propagamos el delta de salida a través del peso hacia atrás
error_oculto = delta_salida * w_salida
delta_oculto = error_oculto * derivada_sigmoide(a1)

# 3. ACTUALIZACIÓN DE PESOS
# Nuevo peso = peso anterior + (tasa * delta * entrada_a_ese_peso)
w_salida += tasa_aprendizaje * delta_salida * a1
w_oculto[0] += tasa_aprendizaje * delta_oculto * x[0]
w_oculto[1] += tasa_aprendizaje * delta_oculto * x[1]

print(f"Pesos ajustados. Nueva predicción tras 1 paso: {sigmoide(sigmoide(x[0]*w_oculto[0] + x[1]*w_oculto[1]) * w_salida):.4f}")