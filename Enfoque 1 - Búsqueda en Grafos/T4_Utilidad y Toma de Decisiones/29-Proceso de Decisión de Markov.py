#¿Qué es un Proceso de Decisión de Markov (MDP) y Q-Learning?
# Un MDP describe un entorno donde los resultados son parcialmente aleatorios y parcialmente 
# controlados por un agente. El Q-Learning es un algoritmo que permite a la IA resolver este 
# proceso sin que nadie le explique las reglas; ella las descubre "sufriendo" las consecuencias.

# Los pilares del aprendizaje:
# Exploración vs. Explotación ($\epsilon$-greedy): La IA debe decidir entre probar algo nuevo 
# (explorar) o usar lo que ya sabe que funciona (explotar).
# La Tabla Q: Es la "memoria" del agente. En lugar de guardar valores de estados, guarda el valor 
# de paralelos estado-acción.
# Diferencia Temporal (TD): Es el mecanismo de actualización. La IA ajusta sus expectativas 
# comparando lo que creía que pasaría con la recompensa real obtenida más el potencial futuro.

import random

# --- CONFIGURACIÓN DEL UNIVERSO ---
zonas = ['Base', 'Ruta_Nevada', 'Punto_Extracción', 'Grieta']
maniobras = ['Avanzar', 'Esperar']
zonas_finales = ['Punto_Extracción', 'Grieta']

def motor_fisico_entorno(ubicacion, maniobra):
    """El mundo real: tiene viento y azar que la IA no conoce."""
    if ubicacion == 'Base':
        if maniobra == 'Avanzar':
            # 90% llega a la ruta, 10% el viento lo mantiene en la base
            return ('Ruta_Nevada', -1) if random.random() < 0.9 else ('Base', -1)
        return 'Base', -1
            
    elif ubicacion == 'Ruta_Nevada':
        if maniobra == 'Avanzar':
            # Riesgo extremo: 70% rescate exitoso, 30% caída en grieta
            return ('Punto_Extracción', 100) if random.random() < 0.7 else ('Grieta', -100)
        return 'Base', -1 # Volver a la base por seguridad
    
    return ubicacion, 0

# --- INICIALIZACIÓN DEL CEREBRO (TABLA Q) ---
# Al principio, el dron no sabe que el Punto_Extracción es bueno ni que la Grieta es mala.
Q_Table = {z: {m: 0.0 for m in maniobras} for z in zonas}

# HIPERPARÁMETROS
tasa_aprendizaje = 0.1 # Alfa (α)
descuento_futuro = 0.9 # Gamma (γ)
prob_exploracion = 0.2 # Epsilon (ε)
simulaciones = 2000

print("--- Entrenando Sistema de Navegación Autónoma ---")

for vida in range(1, simulaciones + 1):
    zona_actual = 'Base'
    
    while zona_actual not in zonas_finales:
        # 1. TOMA DE DECISIÓN (Epsilon-Greedy)
        if random.random() < prob_exploracion:
            accion = random.choice(maniobras) # Prueba algo nuevo
        else:
            # Usa el conocimiento más alto de su tabla Q
            accion = max(Q_Table[zona_actual], key=Q_Table[zona_actual].get)
            
        # 2. INTERACCIÓN CON EL MUNDO
        proxima_zona, premio = motor_fisico_entorno(zona_actual, accion)
        
        # 3. ACTUALIZACIÓN DE CONOCIMIENTO (Ecuación de Q-Learning)
        # Estimamos el valor máximo del siguiente estado
        max_futuro = max(Q_Table[proxima_zona].values()) if proxima_zona not in zonas_finales else 0.0
        
        # Ajustamos el valor Q actual basándonos en la experiencia
        v_viejo = Q_Table[zona_actual][accion]
        objetivo = premio + (descuento_futuro * max_futuro)
        Q_Table[zona_actual][accion] = v_viejo + tasa_aprendizaje * (objetivo - v_viejo)
        
        zona_actual = proxima_zona

    if vida % 500 == 0:
        print(f" > Simulación {vida} finalizada. El dron está refinando su instinto...")

# --- RESULTADOS ---
print("\n" + "="*55)
print(" MAPA DE CONOCIMIENTO ADQUIRIDO (TABLA Q) ")
print("="*55)
for z in ['Base', 'Ruta_Nevada']:
    print(f"En {z}:")
    for m, val in Q_Table[z].items():
        print(f"  - Acción {m.upper()}: Calidad Estimada = {val:.2f}")

print("\n--- PROTOCOLO DE VUELO APRENDIDO ---")
for z in ['Base', 'Ruta_Nevada']:
    mejor_m = max(Q_Table[z], key=Q_Table[z].get)
    print(f"Si el dron está en '{z}' -> Ejecutará: {mejor_m.upper()}")