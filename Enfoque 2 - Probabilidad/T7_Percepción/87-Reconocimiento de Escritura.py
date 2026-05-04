#1. El Enfoque de Probabilidad en el Trazo
# A diferencia de los objetos rígidos, la escritura varía por la presión, el ángulo y el estilo. Por 
# ello, el reconocimiento se modela como un proceso estocástico. Se utilizan herramientas como los 
# Modelos Ocultos de Márkov (HMM) o las Redes Recurrentes (LSTM) para entender la secuencia de los 
# trazos a través del tiempo.

# 2. Clasificación de Caracteres (MNIST Style)
# El estándar de oro para entender este tema es el dataset MNIST. Cada dígito es una matriz de $28 
# \times 28$ píxeles. El modelo calcula un vector de probabilidad donde cada posición representa un 
# dígito (0-9).
# Incertidumbre: Si un "4" está mal escrito y se parece a un "9", el modelo reportará 
# algo como $P(4) = 0.45$ y $P(9) = 0.40$. Aquí es donde el contexto probabilístico salva el día.

# =====================================================================
# PERCEPCIÓN: RECONOCIMIENTO DE ESCRITURA PROBABILÍSTICO
# =====================================================================

def reconocer_trazo(altura, tiene_hueco):
    """
    Infiere el carácter basado en rasgos físicos.
    altura: 0.0 (bajo) a 1.0 (alto)
    tiene_hueco: 1 (sí, como en 'o' o '0'), 0 (no)
    """
    
    # Perfiles estadísticos (Priors y Verosimilitud)
    # Formato: {'caracter': (prob_altura_esperada, prob_hueco_esperado)}
    modelos = {
        '1': (0.9, 0.0), # Alto, sin hueco
        '0': (0.8, 1.0), # Alto, con hueco
        'i': (0.4, 0.0), # Bajo, sin hueco
        'o': (0.3, 1.0)  # Bajo, con hueco
    }
    
    probabilidades = {}
    
    for char, (m_alt, m_hueco) in modelos.items():
        # Verosimilitud: qué tanto se parece el trazo al modelo
        # Usamos una función de similitud inversa a la distancia
        dist_alt = abs(altura - m_alt)
        dist_hueco = abs(tiene_hueco - m_hueco)
        
        # Probabilidad de observación P(Rasgos | Caracter)
        verosimilitud = (1 - dist_alt) * (1 - dist_hueco)
        probabilidades[char] = max(verosimilitud, 0.01)

    # Normalización para obtener la distribución de probabilidad
    total = sum(probabilidades.values())
    resultado = {k: (v / total) * 100 for k, v in probabilidades.items()}
    
    # Ordenar por mayor probabilidad
    final = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
    
    print(f"Entrada: Altura {altura}, Hueco {tiene_hueco}")
    for char, prob in final:
        print(f"  P('{char}'): {prob:>5.2f}%")
    
    return final[0][0]

# --- CASOS DE PERCEPCIÓN ---
print("--- TEST 1: Trazo corto con hueco ---")
reconocer_trazo(0.35, 1)

print("\n--- TEST 2: Trazo largo y recto ---")
reconocer_trazo(0.95, 0)