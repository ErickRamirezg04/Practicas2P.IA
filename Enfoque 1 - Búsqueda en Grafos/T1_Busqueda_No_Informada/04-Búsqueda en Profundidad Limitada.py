#¿Qué es la Búsqueda en Profundidad Limitada (DLS)?
#Es una variante de la búsqueda en profundidad (DFS) que impone un tope máximo a la exploración. 
# Evita que el algoritmo se pierda en ramas infinitas o demasiado profundas al establecer un umbral 
# de "profundidad máxima".

#Cómo funciona:
# Funciona igual que DFS, pero cada nodo tiene asociada una profundidad.
# Si el algoritmo llega al nivel de profundidad especificado como límite, deja de expandir a los hijos 
# de ese nodo, incluso si existen.
# Introduce el concepto de "Corte" (Cutoff): una señal que indica que el objetivo no se encontró en 
# ese nivel, pero que existen más nodos más abajo que no pudimos ver por la restricción.

# Mapa de las cámaras de la pirámide (Conexiones entre salas)
complejo_piramidal = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J', 'K'],
    'G': ['L'],
    'I': ['M', 'N'],
    'K': ['O'],
    'L': ['P'],
    'N': ['Q'],
    'Q': ['R'],
    'H': [], 'J': [], 'M': [], 'O': [], 'P': [], 'R': []
}

def sondear_camara_recursivo(red_salas, sala_actual, reliquia, oxigeno_limite, ruta_recorrida=[]):
    """
    Algoritmo DLS: Explora hasta un nivel de profundidad determinado.
    """
    # Registramos la sala actual en nuestro mapa de expedición
    trayectoria_nueva = ruta_recorrida + [sala_actual]
    nivel_descenso = len(ruta_recorrida)
    
    # Reporte de telemetría de la exploración
    print(f"Sondeando: {sala_actual} (Nivel de descenso: {nivel_descenso} | Límite de Oxígeno: {oxigeno_limite})")

    # 1. Verificamos si la sala actual contiene la reliquia buscada
    if sala_actual == reliquia:
        return "HALLADO", trayectoria_nueva

    # 2. Verificamos si nos hemos quedado sin suministro (límite alcanzado)
    if nivel_descenso >= oxigeno_limite:
        # Si la cámara tiene túneles que bajan más, notificamos un corte
        if red_salas.get(sala_actual, []):
            return "LIMITE_ALCANZADO", None 
        else:
            return "VACIO", None 

    # 3. Exploración de túneles adyacentes (Paso Recursivo)
    pasadizos = red_salas.get(sala_actual, [])
    quedaron_zonas_sin_ver = False
    
    for proxima_sala in pasadizos:
        # Iniciamos el descenso recursivo a la siguiente cámara
        estado, ruta_final = sondear_camara_recursivo(
            red_salas, proxima_sala, reliquia, oxigeno_limite, trayectoria_nueva
        )
        
        if estado == "HALLADO":
            return "HALLADO", ruta_final
        
        if estado == "LIMITE_ALCANZADO":
            # Marcamos que la expedición se detuvo por falta de oxígeno en niveles inferiores
            quedaron_zonas_sin_ver = True 

    # Si terminamos los túneles sin éxito, reportamos el tipo de fallo
    if quedaron_zonas_sin_ver:
        return "LIMITE_ALCANZADO", None
    else:
        return "VACIO", None

def gestor_de_expedicion(mapa, inicio, objetivo, rango_max):
    """
    Función envolvente para organizar los resultados de la misión.
    """
    print(f"\n--- INICIANDO PROTOCOLO DE BÚSQUEDA (Objetivo: '{objetivo}', Alcance: {rango_max}) ---")
    estatus, rastro = sondear_camara_recursivo(mapa, inicio, objetivo, rango_max)
    
    if estatus == "HALLADO":
        print(f"ESTADO FINAL: ¡RELIQUIA ENCONTRADA!")
        print(f"Ruta de extracción: {' -> '.join(rastro)}")
    elif estatus == "LIMITE_ALCANZADO":
        print(f"ESTADO FINAL: ALCANCE INSUFICIENTE. El objetivo está a mayor profundidad que {rango_max}.")
    else:
        print(f"ESTADO FINAL: ÁREA DESPEJADA. El objetivo no está en los sectores explorables.")

# --- PRUEBAS DE LA MISIÓN ---

# Prueba A: Exploración superficial Objetivo:L
gestor_de_expedicion(complejo_piramidal, 'A', 'L', rango_max=3)

# Prueba B: Exploración profunda Objetivo: F
gestor_de_expedicion(complejo_piramidal, 'A', 'F', rango_max=5)