#¿Qué es el Algoritmo EM?
#El Algoritmo EM es un método iterativo para encontrar estimaciones de máxima verosimilitud de 
# parámetros en modelos probabilísticos donde hay variables latentes (variables que no vemos, como 
# a qué grupo pertenece cada dato).

#Funciona en un ciclo infinito de dos pasos:

#Paso E (Expectation): La IA "estima" a qué grupo pertenece cada dato basándose en los parámetros 
# actuales. No asigna un grupo fijo, sino una responsabilidad (ej. "tienes un 90% de probabilidad 
# de ser del Grupo A").

#Paso M (Maximization): La IA actualiza las medias y pesos de los grupos usando los datos, pero 
# dándole más importancia a los datos que "prometieron" pertenecer a ese grupo en el paso anterior.

import math

# =====================================================================
# ALGORITMO EM: SEGMENTACIÓN PROBABILÍSTICA (Mezcla de Gaussianas)
# =====================================================================

# Montos de compras de 6 clientes (notamos dos grupos naturales)
datos_compras = [1.2, 2.5, 1.8, 8.2, 9.5, 8.8]

def gaussiana(x, mu, sigma=1.0):
    """Calcula la probabilidad de x en una campana de Gauss."""
    exponente = math.exp(-((x - mu)**2) / (2 * sigma**2))
    return (1 / (math.sqrt(2 * math.pi) * sigma)) * exponente

def ejecutar_em(datos, iteraciones=5):
    # PARÁMETROS INICIALES (Adivinanzas iniciales)
    mu_pobre = 2.0      # Media del Grupo 1
    mu_rico = 5.0       # Media del Grupo 2
    pi_pobre = 0.5      # Probabilidad inicial del Grupo 1
    pi_rico = 0.5       # Probabilidad inicial del Grupo 2
    sigma = 1.0         # Dispersión fija para simplificar

    print(f"Iniciando segmentación de {len(datos)} clientes...")

    for i in range(iteraciones):
        # --- 🔹 PASO E: EXPECTACIÓN (Calcular Responsabilidades) ---
        responsabilidades = []
        for x in datos:
            # ¿Qué tan probable es que x venga de cada campana?
            prob1 = pi_pobre * gaussiana(x, mu_pobre, sigma)
            prob2 = pi_rico * gaussiana(x, mu_rico, sigma)
            
            total = prob1 + prob2
            # Responsabilidad: Probabilidad relativa de pertenecer a cada grupo
            r1 = prob1 / total
            r2 = prob2 / total
            responsabilidades.append((r1, r2))

        # --- 🔹 PASO M: MAXIMIZACIÓN (Actualizar Parámetros) ---
        n_pobre = sum(r[0] for r in responsabilidades)
        n_rico = sum(r[1] for r in responsabilidades)

        # Actualizamos las medias (promedio ponderado por la responsabilidad)
        mu_pobre = sum(r[0] * x for r, x in zip(responsabilidades, datos)) / n_pobre
        mu_rico = sum(r[1] * x for r, x in zip(responsabilidades, datos)) / n_rico

        # Actualizamos los pesos de los grupos (pi)
        pi_pobre = n_pobre / len(datos)
        pi_rico = n_rico / len(datos)

        print(f"\nIteración {i+1}:")
        print(f" > Centro Grupo 1: {mu_pobre:.2f} (Peso: {pi_pobre:.1%})")
        print(f" > Centro Grupo 2: {mu_rico:.2f} (Peso: {pi_rico:.1%})")

# --- EJECUCIÓN ---
ejecutar_em(datos_compras)