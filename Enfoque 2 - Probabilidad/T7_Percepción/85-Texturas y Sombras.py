#1. La Textura como Probabilidad (Campos Aleatorios)
#En computación, una textura no es solo un dibujo; es una distribución espacial de variaciones. Para la 
# percepción probabilística, modelamos la textura como un Campo Aleatorio de Markov (MRF). Si conocemos
#  los píxeles vecinos, podemos predecir con cierta probabilidad el valor del píxel actual.

#Gradientes de Textura: La densidad de la textura nos da una pista probabilística de la distancia. Si 
# los elementos de la textura están más juntos, la probabilidad de que el objeto esté lejos aumenta.

#2. Sombras e Inferencia de Forma
#Las sombras son fundamentales para la percepción de la tercera dimensión.

#Sombra Propia: Nos dice la curvatura del objeto (probabilidad de orientación de la cara respecto a la 
# luz).

#Sombra Proyectada: Nos dice la distancia entre el objeto y el suelo.

#El cerebro asume por defecto una prior probabilística: "la luz viene de arriba". Si inviertes las 
# sombras de un cráter, ¡lo percibirás como una montaña!

import random

# =====================================================================
# PERCEPCIÓN PROBABILÍSTICA: TEXTURA vs. SOMBRA
# =====================================================================

# Simulamos una superficie con textura (ruido) y una zona de sombra (fosa)
# Valores de 0 a 100 (Brillo)
superficie = [80, 82, 79, 81, 78, 83] + [30, 25, 20, 25, 30] + [80, 79, 81]
#             --- Textura Clara ---   --- Zona de Sombra ---   --- Textura ---

def analizar_percepcion(datos):
    print(f"{'Píxel':<7} | {'Brillo':<8} | {'Inferencia de Percepción'}")
    print("-" * 50)
    
    # Parámetros probabilísticos (Prioris)
    media_superficie = 80
    umbral_sombra = 40 
    
    for i, brillo in enumerate(datos):
        # Estimación probabilística simple:
        # Si el brillo se aleja mucho de la media esperada de la superficie,
        # la probabilidad de que sea una 'Sombra' (estructura) supera a la de 'Textura' (ruido).
        
        diff = abs(brillo - media_superficie)
        
        if brillo < umbral_sombra:
            tag = "SOMBRA (Estructura 3D detectada)"
        elif diff < 5:
            tag = "TEXTURA (Variación aleatoria superficial)"
        else:
            tag = "ANOMALÍA / CAMBIO DE MATERIAL"
            
        print(f"{i:<7} | {brillo:<8} | {tag}")

# --- EJECUCIÓN ---
analizar_percepcion(superficie)