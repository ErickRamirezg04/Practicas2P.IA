#¿Qué es el Filtro de Partículas?
#Es un algoritmo de Monte Carlo Secuencial. A diferencia de Kalman, que representa la incertidumbre 
# como una campana perfecta, el Filtro de Partículas la representa como una "nube" de puntos.

#Funciona mediante una "Selección Natural" de datos:

#Predicción: Cada partícula se mueve según lo que cree que el robot hizo (añadiendo un poco de azar).

#Ponderación: Comparamos cada partícula con la medición real del sensor. Las partículas que 
# "predijeron" bien la medición reciben un peso alto; las que están en lugares imposibles reciben 
# un peso bajo.

#Resampling (Supervivencia): Las partículas con pesos bajos mueren. Las partículas con pesos altos 
# se clonan. La nube de puntos se concentra donde está la verdad.

import random

# --- CONFIGURACIÓN DEL SISTEMA ---
NUM_PARTICULAS = 150
# El robot empieza en algún lugar entre 0 y 10 (incertidumbre total)
nube_particulas = [random.uniform(0, 10) for _ in range(NUM_PARTICULAS)]

def modelo_fisico(x):
    """Predicción: El robot intenta avanzar 1 metro, pero hay viento/fricción."""
    return x + 1.0 + random.gauss(0, 0.3)

def medir_verosimilitud(z, x):
    """Evaluación: ¿Qué tan coherente es que el sensor diga 'z' si la partícula está en 'x'?"""
    distancia = abs(z - x)
    # Una gaussiana manual: a menor distancia, mayor peso (verosimilitud)
    return (2.718 ** (-(distancia**2) / 0.5))

def motor_particulas(mediciones):
    global nube_particulas
    
    print(f"{'Paso':<6} | {'Sensor':<8} | {'Estimación':<12} | {'Estado de la Nube'}")
    print("-" * 65)

    for t, z in enumerate(mediciones):
        # 1. PREDICCIÓN (Mutación)
        nube_particulas = [modelo_fisico(p) for p in nube_particulas]

        # 2. PESOS (Selección Natural)
        pesos = [medir_verosimilitud(z, p) for p in nube_particulas]
        total_pesos = sum(pesos)
        
        # Evitar división por cero si todas las partículas mueren
        if total_pesos == 0: 
            pesos = [1.0/NUM_PARTICULAS] * NUM_PARTICULAS
        else:
            pesos = [p / total_pesos for p in pesos]

        # 3. RESAMPLING (Clonación de los mejores)
        # Aquí es donde las partículas 'buenas' se multiplican
        nube_particulas = random.choices(nube_particulas, weights=pesos, k=NUM_PARTICULAS)

        # 4. ESTIMACIÓN (Promedio de la nube)
        pos_estimada = sum(nube_particulas) / NUM_PARTICULAS
        
        # Visualización simple de la concentración de la nube
        min_p, max_p = min(nube_particulas), max(nube_particulas)
        print(f"{t:<6} | {z:<8.2f} | {pos_estimada:<12.3f} | Rango: [{min_p:.1f} - {max_p:.1f}]")

# --- EJECUCIÓN ---
# El robot se mueve, y el sensor nos da estas lecturas con ruido
sensor_gps = [1.2, 2.1, 3.0, 3.8, 4.9]
motor_particulas(sensor_gps)