#1. El Marco Bayesiano del Reconocimiento
# El reconocimiento moderno se basa en la Regla de Bayes:
# 
# ¿Qué tan probable es ver estas características si el objeto fuera realmente un "Coche"?
# Prior ($P(C)$): ¿Qué tan común es ver ese objeto en este contexto? (Si estás en medio del océano, 
# la probabilidad a priori de ver un "Coche" es casi cero, lo que ayuda a corregir errores de visión).

# 2. Extracción de Características (Features)
# Para que la probabilidad sea manejable, no usamos todos los píxeles. Usamos descriptores 
# como:SIFT/SURF: Puntos clave que no cambian aunque el objeto rote o cambie de tamaño.
# HOG (Histogram of Oriented Gradients): Captura la "silueta" basándose en la dirección de los bordes.

# =====================================================================
# PERCEPCIÓN: RECONOCIMIENTO DE OBJETOS (MODELO PROBABILÍSTICO)
# =====================================================================

def reconocer_objeto(redondez, grosor):
    """
    Simula un reconocimiento basado en verosimilitud estadística.
    redondez: 0 (cuadrado) a 1 (círculo perfecto)
    grosor: 0 (delgado) a 1 (voluminoso)
    """
    
    # Modelos Estadísticos (Media de características por objeto)
    # Formato: [media_redondez, media_grosor]
    modelo_pelota = [0.95, 0.80]
    modelo_libro  = [0.10, 0.20]
    
    # Priors (Probabilidad de encontrar el objeto en la escena)
    prior_pelota = 0.4
    prior_libro  = 0.6
    
    def calcular_verosimilitud(obs, modelo):
        # Distancia euclidiana como inversa de la verosimilitud
        dist = sum((o - m)**2 for o, m in zip(obs, modelo))
        return 1 / (1 + dist) # A menor distancia, mayor probabilidad

    # Cálculo de verosimilitudes P(Características | Objeto)
    v_pelota = calcular_verosimilitud([redondez, grosor], modelo_pelota)
    v_libro  = calcular_verosimilitud([redondez, grosor], modelo_libro)
    
    # Probabilidad Posterior (Numerador de Bayes: Verosimilitud * Prior)
    post_pelota = v_pelota * prior_pelota
    post_libro  = v_libro * prior_libro
    
    # Normalización para obtener porcentajes
    total = post_pelota + post_libro
    prob_p = (post_pelota / total) * 100
    prob_l = (post_libro / total) * 100
    
    print(f"Observación: Redondez={redondez}, Grosor={grosor}")
    print(f"-> Probabilidad Pelota: {prob_p:.2f}%")
    print(f"-> Probabilidad Libro:  {prob_l:.2f}%")
    
    return "PELOTA" if prob_p > prob_l else "LIBRO"

# --- SIMULACIÓN DE PERCEPCIÓN ---
# Caso 1: Un objeto casi circular y con volumen
print("--- TEST 1 ---")
reconocer_objeto(0.88, 0.75)

# Caso 2: Un objeto plano y rectangular (baja redondez)
print("\n--- TEST 2 ---")
reconocer_objeto(0.15, 0.25)