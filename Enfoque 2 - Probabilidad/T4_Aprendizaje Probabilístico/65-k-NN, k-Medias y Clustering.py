#k-Nearest Neighbors (k-NN)
# El k-NN es un algoritmo supervisado. Su lema es: "Dime con quién andas y te diré quién eres". 
# Para clasificar un punto nuevo, busca los $k$ vecinos más cercanos y votan para decidir la clase.

#k-Medias (k-Means)
# Es un algoritmo no supervisado. Aquí no hay etiquetas; la IA debe encontrar los centros de masa 
# ($k$ centroides) para agrupar los datos por su cuenta.

#Clustering (Concepto General)
#El Clustering no es un código aparte, sino la técnica de organizar objetos en grupos (clusters) 
# cuya similitud sea máxima entre miembros del mismo grupo y mínima entre grupos distintos.

import math
import random

# =====================================================================
# EL LABORATORIO: Datos de Flores (Altura, Ancho)
# =====================================================================
# Dataset etiquetado para k-NN (Supervisado)
# [Altura, Ancho, Clase] -> 0: Girasol, 1: Lavanda
flores_conocidas = [
    [10, 5, 0], [12, 6, 0], [11, 4, 0],  # Girasoles (Grandes)
    [2, 1, 1],  [3, 2, 1],  [2.5, 1.5, 1] # Lavandas (Pequeñas)
]

# Dataset sin etiquetas para k-Means (No Supervisado)
flores_sin_nombre = [
    [9, 5], [11, 5], [3, 1], [2, 2], [10, 6], [2.8, 1.2]
]

# =====================================================================
# MOTOR DE DISTANCIA (Corazón de ambos algoritmos)
# =====================================================================
def calcular_distancia(p1, p2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

# =====================================================================
# ALGORITMO 1: k-Nearest Neighbors (k-NN) - Clasificador
# =====================================================================
def knn(punto_nuevo, datos, k=3):
    distancias = []
    for p in datos:
        dist = calcular_distancia(punto_nuevo, p[:2])
        distancias.append((dist, p[2]))
    
    # Ordenar por cercanía y votar
    vecinos = sorted(distancias)[:k]
    votos = [v[1] for v in vecinos]
    prediccion = max(set(votos), key=votos.count)
    return "Girasol" if prediccion == 0 else "Lavanda"

# =====================================================================
# ALGORITMO 2: k-Means - Agrupador (Clustering)
# =====================================================================
def kmeans(puntos, k_clusters=2, iteraciones=3):
    # Inicializar centroides al azar
    centroides = random.sample(puntos, k_clusters)
    
    for _ in range(iteraciones):
        clusters = {i: [] for i in range(k_clusters)}
        
        # Paso de Asignación
        for p in puntos:
            dist = [calcular_distancia(p, c) for c in centroides]
            idx_centroide = dist.index(min(dist))
            clusters[idx_centroide].append(p)
            
        # Paso de Actualización (Mover el centroide al promedio)
        for i in range(k_clusters):
            if clusters[i]:
                centroides[i] = [sum(p[j] for p in clusters[i]) / len(clusters[i]) for j in range(2)]
    return centroides, clusters

# =====================================================================
# EJECUCIÓN DEL LABORATORIO
# =====================================================================

print("--- FASE 1: k-NN (Supervisado) ---")
misterio = [10.5, 5.5]
resultado_knn = knn(misterio, flores_conocidas)
print(f"El punto {misterio} se parece a sus vecinos. Es un: {resultado_knn}")

print("\n--- FASE 2: k-Means (No Supervisado) ---")
centros, grupos = kmeans(flores_sin_nombre)
for i, c in enumerate(centros):
    print(f"Cluster {i+1} centrado en { [round(x,2) for x in c] } con {len(grupos[i])} flores.")