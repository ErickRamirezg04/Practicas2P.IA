#Las Funciones de Activación son el "interruptor" o la "válvula" de una neurona. Sin ellas, una red 
# neuronal sería simplemente una serie de multiplicaciones matemáticas aburridas que solo podrían 
# resolver problemas lineales (líneas rectas).

#Su función principal es introducir no-linealidad. Esto permite que la red aprenda patrones 
# complejos, curvas, formas y relaciones caóticas en los datos.

#ReLU (Rectified Linear Unit): Es la más usada hoy. ¿Por qué? Porque es computacionalmente barata 
# (solo un max(0, x)) y soluciona en gran parte el problema del Desvanecimiento del Gradiente, 
# permitiendo que las redes sean realmente profundas.

#Sigmoide: Ha caído en desuso para capas ocultas porque "satura" (si el valor es muy alto o muy bajo, 
# la pendiente es casi cero y la red deja de aprender). Sin embargo, es obligatoria al final si 
# necesitas una probabilidad.

#Softmax: (Mención especial) Se usa en la última capa cuando tienes múltiples clases (ej. clasificar 
# si una foto es Perro, Gato o Loro). Hace que la suma de todas las salidas sea exactamente 1.0 (100%).

import math

# Entrada: Suma ponderada de la neurona (z = x*w + b)
z_input = [-5, -2, 0, 2, 5]

# 1. SIGMOIDE: Aplasta todo al rango [0, 1]
def sigmoide(z):
    return 1 / (1 + math.exp(-z))

# 2. TANH (Tangente Hiperbólica): Aplasta todo al rango [-1, 1]
def tanh(z):
    return math.tanh(z)

# 3. ReLU (Rectified Linear Unit): Elimina los negativos
def relu(z):
    return max(0, z)

# 4. Leaky ReLU: Deja pasar un poco de los negativos (evita neuronas muertas)
def leaky_relu(z):
    return z if z > 0 else 0.01 * z

print(f"{'Z':<5} | {'Sigmoide':<10} | {'Tanh':<10} | {'ReLU':<10}")
print("-" * 45)
for z in z_input:
    print(f"{z:<5} | {sigmoide(z):<10.4f} | {tanh(z):<10.4f} | {relu(z):<10.4f}")