#¿Qué es el Truco del Núcleo (Kernel)?
#Imagina que tienes puntos rojos en el centro de un círculo y puntos azules rodeándolos. No puedes 
# cruzarlos con una línea recta.

#El Kernel proyecta esos puntos a una dimensión superior (como convertirlos en una montaña en 3D). 
# De repente, puedes pasar un "cuchillo" (hiperplano) entre la cima de la montaña y la base.

import math

# =====================================================================
# SVM: MÁQUINA DE VECTORES DE SOPORTE (KERNEL RBF)
# =====================================================================

# Datos: [X, Y] y Clase (-1 o 1)
# Imagina un círculo: los puntos cerca del (0,0) son Clase -1, los alejados son 1
entrenamiento = [
    [0, 0, -1], [0.5, 0.2, -1], [0.1, -0.3, -1], # Centro
    [4, 4, 1],   [4, -4, 1],    [-4, 4, 1]       # Periferia
]

def kernel_rbf(p1, p2, gamma=0.1):
    """Calcula la similitud en una dimensión superior (Kernel Gaussiano)."""
    dist_sq = sum((a - b) ** 2 for a, b in zip(p1, p2))
    return math.exp(-gamma * dist_sq)

def svm_predict(punto_nuevo, vectores_soporte, gamma=0.1):
    """
    Simula la decisión de una SVM. 
    Suma la influencia de cada vector de soporte sobre el punto nuevo.
    """
    puntuacion = 0
    for v in vectores_soporte:
        x_v = v[:2]
        y_v = v[2]
        # En una SVM real, cada vector tiene un peso (alpha)
        # Aquí simplificamos asumiendo pesos iguales para ver el efecto del Kernel
        puntuacion += y_v * kernel_rbf(punto_nuevo, x_v, gamma)
    
    return 1 if puntuacion >= 0 else -1

# =====================================================================
# EJECUCIÓN
# =====================================================================

print("--- CLASIFICADOR SVM (KERNEL TRICK) ---")

# Caso 1: Un punto muy cerca del origen
test_1 = [0.2, 0.1]
res_1 = svm_predict(test_1, entrenamiento)
print(f"Punto {test_1}: Clase {res_1} (Zona Interna)")

# Caso 2: Un punto alejado
test_2 = [3.5, 3.5]
res_2 = svm_predict(test_2, entrenamiento)
print(f"Punto {test_2}: Clase {res_2} (Zona Externa)")