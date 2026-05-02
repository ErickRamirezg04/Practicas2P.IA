#¿Qué es un Mapa de Kohonen?
#Imagina una red de neuronas dispuestas en una cuadrícula. Cada neurona tiene un "vector de pesos" 
# del mismo tamaño que los datos de entrada.

#Cuando entra un dato, ocurre una Competencia:

#Caza de la BMU: Se busca la neurona cuyo peso se parece más al dato de entrada. Esta es la Best 
# Matching Unit (BMU).

#Cooperación: La BMU "gana", pero invita a sus vecinas cercanas en la cuadrícula a parecerse también 
# al dato.

#Adaptación: La BMU y su vecindario ajustan sus pesos para ser más similares al dato observado.

import random
import math

# =====================================================================
# MAPA AUTOORGANIZADO DE KOHONEN (SOM)
# =====================================================================

# Datos de entrada: Colores RGB normalizados [R, G, B]
colores = [
    [1, 0, 0], [0, 1, 0], [0, 0, 1], # Rojo, Verde, Azul puros
    [1, 1, 0], [0, 1, 1], [1, 0, 1], # Amarillo, Cian, Magenta
    [0.5, 0.2, 0.1], [0.1, 0.8, 0.9] # Colores aleatorios
]

# Configuración del mapa (Red de 3x3 neuronas)
FILAS, COLS = 3, 3
red = [[[random.random() for _ in range(3)] for _ in range(COLS)] for _ in range(FILAS)]

def distancia_euclidiana(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

def entrenar_som(datos, epocas=100, tasa_aprendizaje=0.1):
    for ep in range(epocas):
        # 1. Elegir un dato al azar
        dato = random.choice(datos)
        
        # 2. Encontrar la BMU (Best Matching Unit)
        bmu_pos = (0, 0)
        dist_min = float('inf')
        
        for r in range(FILAS):
            for c in range(COLS):
                d = distancia_euclidiana(red[r][c], dato)
                if d < dist_min:
                    dist_min = d
                    bmu_pos = (r, c)
        
        # 3. Actualizar pesos de la BMU y sus vecinos inmediatos (Cruz)
        r_bmu, c_bmu = bmu_pos
        vecinos = [(r_bmu, c_bmu), (r_bmu-1, c_bmu), (r_bmu+1, c_bmu), (r_bmu, c_bmu-1), (r_bmu, c_bmu+1)]
        
        for r, c in vecinos:
            if 0 <= r < FILAS and 0 <= c < COLS:
                for i in range(3):
                    # Acercar el peso de la neurona al dato
                    red[r][c][i] += tasa_aprendizaje * (dato[i] - red[r][c][i])

# --- EJECUCIÓN ---
print("Entrenando Mapa de Kohonen...")
entrenar_som(colores, epocas=1000)

print("\n--- Mapa Resultante (Representación de Colores) ---")
for fila in red:
    # Mostramos los pesos RGB de cada neurona
    print([ [round(canal, 2) for canal in neurona] for neurona in fila])