#1. El Problema de la Apertura y la Incertidumbre
#Cuando observamos una línea a través de un agujero pequeño (apertura), no podemos saber su dirección 
# real de movimiento, solo la componente perpendicular a la línea. El cerebro y la IA resuelven esta 
# ambigüedad combinando múltiples probabilidades locales para obtener una velocidad global coherente.

#2. Estimación de Movimiento: Flujo Óptico
#Existen dos métodos principales bajo el enfoque probabilístico:

#Lucas-Kanade: Asume que el movimiento es constante en una pequeña vecindad de píxeles y resuelve el 
# desplazamiento mediante mínimos cuadrados (una forma de estimación de máxima verosimilitud).

#Horn-Schunck: Introduce una restricción de "suavizado global", asumiendo que es más probable que los 
# objetos se muevan de forma fluida y no errática.

# =====================================================================
# PERCEPCIÓN DE MOVIMIENTO: FILTRO DE KALMAN (ESTIMACIÓN PROBABILÍSTICA)
# =====================================================================

class PercepcionMovimiento:
    def __init__(self, pos_inicial):
        self.estimacion = pos_inicial  # Creencia actual
        self.velocidad = 2.0           # Velocidad asumida (píxeles/frame)
        self.incertidumbre = 1.0       # Qué tan seguros estamos (varianza)
        
    def predecir(self):
        # Predicción basada en el modelo físico: pos = pos + vel
        self.estimacion += self.velocidad
        self.incertidumbre += 0.5 # La incertidumbre crece al predecir el futuro
        print(f"[Predicción] Posición probable: {self.estimacion:.2f} (Incertidumbre: {self.incertidumbre:.2f})")

    def corregir(self, observacion_ruidosa):
        # Ganancia de Kalman: ¿Cuánto caso le hacemos al sensor?
        # Si el sensor es ruidoso (incertidumbre alta), confiamos más en la predicción.
        error_sensor = 2.0
        ganancia = self.incertidumbre / (self.incertidumbre + error_sensor)
        
        # Actualizamos nuestra creencia mezclando predicción y observación
        self.estimacion = self.estimacion + ganancia * (observacion_ruidosa - self.estimacion)
        self.incertidumbre = (1 - ganancia) * self.incertidumbre
        
        print(f"[Corrección] Observado: {observacion_ruidosa} -> Nueva Creencia: {self.estimacion:.2f}")

# --- SIMULACIÓN DE SEGUIMIENTO ---
tracker = PercepcionMovimiento(pos_inicial=0)

# El objeto se mueve realmente a +2 por frame, pero el sensor tiene ruido
lecturas_sensor = [2.1, 4.5, 5.8, 8.2, 11.5]

for i, obs in enumerate(lecturas_sensor):
    print(f"\n--- Frame {i+1} ---")
    tracker.predecir()
    tracker.corregir(obs)