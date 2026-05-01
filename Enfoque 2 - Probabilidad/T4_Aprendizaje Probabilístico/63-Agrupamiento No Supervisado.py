#¿Qué es el Agrupamiento No Supervisado (K-means)?
#A diferencia de Naïve Bayes, aquí no hay etiquetas. La IA no sabe qué es "bueno" o "malo", "perro" o 
# "gato". Su único objetivo es encontrar patrones geométricos en los datos: agrupar cosas que se 
# parecen y separar cosas que son distintas.

#El proceso cíclico de K-means:

#Asignación: Cada dato mira a los centroides actuales y se "casa" con el que tenga más cerca 
# (distancia mínima).

#Actualización: Una vez formados los grupos, cada centroide se muda al centro real (el promedio) 
# de sus nuevos miembros.

#Repetición: El baile continúa hasta que los centroides dejan de moverse.

import random

# =====================================================================
# K-MEANS: AGRUPAMIENTO AUTOMÁTICO DE PAQUETES
# =====================================================================

# Ubicaciones de los paquetes en un pasillo (coordenadas 1D)
ubicaciones = [1.0, 2.0, 1.5, 8.0, 9.0, 8.5]
K = 2  # Queremos crear 2 zonas de recolección

def ejecutar_logistica_kmeans(datos, k_clusters, iteraciones=5):
    # INICIALIZACIÓN: Elegimos K paquetes al azar para que sean los "jefes" iniciales
    centroides = random.sample(datos, k_clusters)
    
    print(f"Iniciando K-means con K={k_clusters}")
    print(f"Ubicaciones iniciales de los centros: {centroides}")

    for it in range(iteraciones):
        # Diccionario para guardar qué paquetes van a qué centro
        zonas = {i: [] for i in range(k_clusters)}

        # 🔹 1. FASE DE ASIGNACIÓN (¿A quién le queda más cerca?)
        for paquete in datos:
            # Calculamos distancia absoluta en 1D
            distancias = [abs(paquete - c) for c in centroides]
            centro_mas_cercano = distancias.index(min(distancias))
            zonas[centro_mas_cercano].append(paquete)

        # 🔹 2. FASE DE ACTUALIZACIÓN (Mover el centro al medio del grupo)
        nuevos_centroides = []
        for i in range(k_clusters):
            if zonas[i]:
                # El nuevo centroide es el promedio de su zona
                centro_nuevo = sum(zonas[i]) / len(zonas[i])
                nuevos_centroides.append(round(centro_nuevo, 2))
            else:
                # Si un centro se quedó solo, no se mueve
                nuevos_centroides.append(centroides[i])

        # Verificamos si hubo cambios (Criterio de parada)
        if nuevos_centroides == centroides:
            print(f"\n[!] Convergencia alcanzada en la iteración {it+1}")
            break
            
        centroides = nuevos_centroides

        print(f"\nIteración {it+1}:")
        for idx, centro in enumerate(centroides):
            print(f" > Centro {idx} en {centro}: contiene paquetes {zonas[idx]}")

    return centroides

# --- EJECUCIÓN ---
centros_finales = ejecutar_logistica_kmeans(ubicaciones, K)