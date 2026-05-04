#1. El Alfabeto de las Líneas
# Para que una máquina "perciba" profundidad en un dibujo plano, etiqueta las aristas con tres 
# símbolos:
# Convexa (+): La arista sobresale hacia el observador (como el borde exterior de una caja).
# Cóncava (-): La arista se aleja del observador (como el rincón interior de una habitación).
# Oclusiva o de Contorno ($\rightarrow$): La arista marca el límite del objeto; lo que hay a un lado 
# de la flecha oculta lo que hay al otro.

# 2. Consistencia Local y Probabilidad
# La percepción utiliza la consistencia de vértices. Un vértice donde se unen tres líneas tiene un 
#  limitado de configuraciones físicamente posibles. Si una arista se etiqueta como "+" en un extremo, 
# la probabilidad de que sea "-" en el otro es cero (restricción física). El proceso de etiquetado es 
# una propagación de estas probabilidades y restricciones a través de todo el grafo del objeto.

# =====================================================================
# PERCEPCIÓN: ETIQUETADO DE LÍNEAS (INFERENCIA DE ESTRUCTURA)
# =====================================================================

def inferir_etiqueta_arista(angulo_vertice, es_borde_externo):
    """
    Infiere la probabilidad del tipo de arista en un vértice.
    angulo_vertice: grados entre las líneas.
    es_borde_externo: Booleano, indica si la línea toca el fondo.
    """
    
    # Modelos de etiquetas posibles
    # + : Convexo, - : Cóncavo, > : Oclusivo
    
    probabilidades = {'+': 0.0, '-': 0.0, '>': 0.0}
    
    if es_borde_externo:
        # Si es el límite del objeto, la probabilidad de ser oclusiva es máxima
        probabilidades['>'] = 0.95
        probabilidades['+'] = 0.05
    else:
        # Si es interna, depende de la geometría detectada
        if angulo_vertice < 180:
            # Probabilidad bayesiana: en un dibujo 2D, ángulos agudos 
            # internos suelen ser esquinas convexas (+) en 3D.
            probabilidades['+'] = 0.80
            probabilidades['-'] = 0.20
        else:
            probabilidades['-'] = 0.70
            probabilidades['+'] = 0.30

    print(f"Análisis de Vértice: Ángulo {angulo_vertice}°, Externo: {es_borde_externo}")
    for etiqueta, prob in probabilidades.items():
        if prob > 0:
            print(f"  P(Etiqueta '{etiqueta}'): {prob*100:>5.1f}%")
            
    return max(probabilidades, key=probabilidades.get)

# --- SIMULACIÓN DE PERCEPCIÓN 3D ---
print("--- TEST 1: Arista del contorno de un cubo ---")
inferir_etiqueta_arista(90, True)

print("\n--- TEST 2: Arista interna (unión de paredes) ---")
inferir_etiqueta_arista(120, False)