#¿Qué es la Búsqueda en Profundidad Iterativa (IDDFS)?
#Es un algoritmo híbrido que combina lo mejor de dos mundos: la eficiencia en memoria de la 
# Búsqueda en Profundidad (DFS) y la garantía de encontrar el camino más corto de la Búsqueda 
# en Anchura (BFS).

#Cómo funciona:
# Realiza múltiples búsquedas en profundidad limitada (DLS) de forma sucesiva.
# En la primera iteración busca con límite 0, en la segunda con límite 1, luego límite 2, y así 
# sucesivamente.
# Aunque parece ineficiente repetir los niveles superiores, el costo computacional es mínimo 
# comparado con el beneficio de no saturar la memoria RAM.
# Se detiene cuando encuentra el objetivo o cuando una búsqueda completa (sin cortes) confirma 
# que el nodo no existe.

# Mapeo de coordenadas planetarias (Nodos y sus conexiones)
red_coordenadas = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': ['G', 'H'], 'E': ['I'], 'F': ['J', 'K'],
    'G': ['L'], 'I': ['M', 'N'], 'K': ['O'],
    'L': ['P'], 'N': ['Q'], 'Q': ['R'],
    'H': [], 'J': [], 'M': [], 'O': [], 'P': [], 'R': []
}

# --- MOTOR DE ESCANEO LOCAL (Búsqueda Limitada) ---
def escaneo_por_capas(red, punto_focal, señal_meta, umbral, rastro_gps=[]):
    """
    Función interna que procesa una sola capa de profundidad.
    """
    # Actualizamos el rastro de la señal
    historial_señal = rastro_gps + [punto_focal]
    nivel_actual = len(rastro_gps)
    
    # Verificamos si la señal captada coincide con la meta
    if punto_focal == señal_meta:
        return "SEÑAL_LOCALIZADA", historial_señal

    # Verificamos si el sensor alcanzó su umbral de potencia actual
    if nivel_actual >= umbral:
        # Si hay más profundidad pero el sensor no llega, marcamos un bloqueo
        if red.get(punto_focal, []):
            return "BLOQUEO_POTENCIA", None 
        else:
            return "FIN_DE_RAMA", None 

    # Propagación de la búsqueda a nodos adyacentes
    conexiones = red.get(punto_focal, [])
    hubo_bloqueo_en_capas_bajas = False
    
    for siguiente in conexiones:
        estado, ruta_detectada = escaneo_por_capas(red, siguiente, señal_meta, umbral, historial_señal)
        
        if estado == "SEÑAL_LOCALIZADA":
            return "SEÑAL_LOCALIZADA", ruta_detectada
        if estado == "BLOQUEO_POTENCIA":
            hubo_bloqueo_en_capas_bajas = True 

    # Determinamos el tipo de respuesta si no se halló la meta
    if hubo_bloqueo_en_capas_bajas:
        return "BLOQUEO_POTENCIA", None
    else:
        return "FIN_DE_RAMA", None


# --- CONTROLADOR CENTRAL (Búsqueda Iterativa) ---
def controlador_id_dfs(mapa_astral, origen, objetivo, potencia_max=10):
    """
    Gestiona el aumento progresivo de la potencia del escáner.
    """
    print(f"Iniciando rastreo satelital. Objetivo: '{objetivo}'")
    
    # Bucle de iteración: Incrementa la resolución del escáner en cada ciclo
    for potencia_paso in range(potencia_max + 1):
        print(f"\n[Ajustando Potencia del Sensor: Nivel {potencia_paso}]")
        
        # Ejecutamos el motor de escaneo con el límite de potencia actual
        status, trayectoria = escaneo_por_capas(mapa_astral, origen, objetivo, potencia_paso)
        
        if status == "SEÑAL_LOCALIZADA":
            print(f">>> ¡CONFIRMADO! Señal '{objetivo}' detectada en Nivel {potencia_paso}.")
            print(f">>> Coordenadas de acceso: {' -> '.join(trayectoria)}")
            return True
            
        elif status == "FIN_DE_RAMA":
            # Si el escaneo termina sin bloqueos, la señal no existe en ninguna profundidad
            print(">>> AVISO: El área ha sido mapeada por completo. Objetivo inexistente.")
            return False
            
        # Si el resultado es BLOQUEO_POTENCIA, el bucle for subirá la potencia en el siguiente paso
        else:
            print(">>> Alerta: Resolución insuficiente. Incrementando potencia para el siguiente barrido...")

    print(f"\nSe agotó el rango de potencia máximo ({potencia_max}) sin resultados.")
    return False


# --- PRUEBA DEL SISTEMA SATELITAL ---
controlador_id_dfs(red_coordenadas, origen='A', objetivo='M', potencia_max=8)