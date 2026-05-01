#¿Qué es el Filtro de Kalman?
# Es un algoritmo matemático que estima el estado de un sistema dinámico (como la posición de un dron) 
# a partir de una serie de mediciones ruidosas. 
# Su magia reside en que es un estimador óptimo: minimiza el error cuadrático promedio combinando 
# dos fuentes de información con incertidumbre.

# El ciclo de vida de Kalman:
# Predicción: Basándose en la física (si el dron iba a 10 m/s, debería estar en X), la IA hace una 
# "suposición" de dónde estará. Al predecir, la incertidumbre ($P$) siempre aumenta.
# Actualización (Corrección): Recibe una señal del sensor ($z$). La IA calcula la Ganancia de Kalman 
# ($K$), que decide cuánto peso darle a la nueva medición frente a su predicción.

# =====================================================================
# SISTEMA DE NAVEGACIÓN: FILTRO DE KALMAN (1D)
# =====================================================================

def ejecutar_rastreo():
    # --- Parámetros del Sistema ---
    x = 0.0      # Estimación inicial de posición
    P = 1.0      # Incertidumbre inicial (qué tanto dudamos al empezar)
    Q = 0.1      # Ruido del proceso (perturbaciones como el viento)
    R = 0.5      # Ruido de medición (margen de error del sensor/GPS)

    # Mediciones recibidas por el sensor (un dron avanzando)
    mediciones = [1.1, 2.0, 2.9, 3.5, 4.2]

    print(f"{'Paso':<6} | {'Medido':<8} | {'Estimado':<10} | {'Incertidumbre':<12} | {'Ganancia K':<10}")
    print("-" * 60)

    for k, z in enumerate(mediciones):
        # 🔹 1. PREDICCIÓN (Predict)
        # Suponemos que el dron mantiene su posición (modelo estático simple)
        x_pred = x
        P_pred = P + Q

        # 🔹 2. ACTUALIZACIÓN / CORRECCIÓN (Update)
        # Calculamos la Ganancia de Kalman: K varía entre 0 y 1
        # Si R es pequeño (sensor confiable), K se acerca a 1 (creemos al sensor)
        # Si R es grande (sensor ruidoso), K se acerca a 0 (creemos a la predicción)
        K = P_pred / (P_pred + R)

        # Fusionamos la predicción con la medición real
        x = x_pred + K * (z - x_pred)
        
        # Actualizamos la incertidumbre (después de medir, siempre dudamos menos)
        P = (1 - K) * P_pred

        print(f"{k+1:<6} | {z:<8.2f} | {x:<10.4f} | {P:<12.4f} | {K:<10.4f}")

# --- Ejecución ---
ejecutar_rastreo()