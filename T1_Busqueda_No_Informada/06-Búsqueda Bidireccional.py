#¿Qué es la Búsqueda Bidireccional?
# Es un algoritmo que ejecuta dos búsquedas simultáneas: una hacia adelante desde el estado inicial 
# y otra hacia atrás desde el objetivo. El proceso se detiene cuando ambas búsquedas se encuentran 
# en un nodo común.

# Cómo funciona:
# Reduce drásticamente el espacio de búsqueda. En lugar de explorar 
# un árbol de profundidad $d$, explora dos árboles de profundidad $d/2$.
# Utiliza dos estructuras de Cola (como en BFS) para avanzar nivel por nivel.
# Es extremadamente eficiente en grafos grandes, siempre que el grafo permita el movimiento 
# en ambos sentidos (no dirigido o con aristas reversibles).

# Mapa de conexiones de ciudades (Red de transporte de doble sentido)
red_ferroviaria = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J', 'K'],
    'G': ['D', 'L'],
    'H': ['D'],
    'I': ['E', 'M', 'N'],
    'J': ['F'],
    'K': ['F', 'O'],
    'L': ['G', 'P'],
    'M': ['I'],
    'N': ['I', 'Q'],
    'O': ['K'],
    'P': ['L'],
    'Q': ['N', 'R'],
    'R': ['Q']
}

def excavacion_doble_sentido(red, ciudad_a, ciudad_b):
    """
    Coordina dos equipos de excavación para conectar dos puntos geográficos.
    """
    # Equipos de excavación (Colas de exploración)
    equipo_norte = [ciudad_a]
    equipo_sur = [ciudad_b]
    
    # Mapas de rastreo para reconstruir la conexión final
    trazado_norte = {ciudad_a: None}
    trazado_sur = {ciudad_b: None}

    print(f"Iniciando proyecto de conexión: {ciudad_a} <---> {ciudad_b}")

    # Continuamos mientras ambos equipos tengan terreno por explorar
    while equipo_norte and equipo_sur:
        
        # --- FASE 1: AVANCE DESDE EL NORTE ---
        punto_norte = equipo_norte.pop(0)
        print(f"[Excavador Norte] Perforando en: {punto_norte}")
        
        # Comprobamos si el equipo Sur ya pasó por aquí
        if punto_norte in trazado_sur:
            print(f"\n¡CONEXIÓN ESTABLECIDA EN: '{punto_norte}'!")
            return ensamblar_tunel(punto_norte, trazado_norte, trazado_sur)
            
        # El equipo Norte expande sus túneles
        for salida in red.get(punto_norte, []):
            if salida not in trazado_norte:
                trazado_norte[salida] = punto_norte
                equipo_norte.append(salida)

        # --- FASE 2: AVANCE DESDE EL SUR ---
        punto_sur = equipo_sur.pop(0)
        print(f"[Excavador Sur  ] Perforando en: {punto_sur}")
        
        # Comprobamos si el equipo Norte ya pasó por aquí
        if punto_sur in trazado_norte:
            print(f"\n¡CONEXIÓN ESTABLECIDA EN: '{punto_sur}'!")
            return ensamblar_tunel(punto_sur, trazado_norte, trazado_sur)
            
        # El equipo Sur expande sus túneles
        for salida in red.get(punto_sur, []):
            if salida not in trazado_sur:
                trazado_sur[salida] = punto_sur
                equipo_sur.append(salida)

    print("\nError: Las condiciones geológicas no permiten la conexión.")
    return False

def ensamblar_tunel(punto_union, mapa_norte, mapa_sur):
    """
    Une las dos secciones del túnel en una sola ruta continua.
    """
    # 1. Reconstrucción desde el origen hasta el punto de encuentro
    seccion_norte = []
    actual = punto_union
    while actual is not None:
        seccion_norte.append(actual)
        actual = mapa_norte[actual]
    seccion_norte.reverse() 

    # 2. Reconstrucción desde el punto de encuentro hasta el destino
    seccion_sur = []
    # Empezamos desde el siguiente nodo en el mapa sur para evitar duplicar el centro
    actual = mapa_sur[punto_union] 
    while actual is not None:
        seccion_sur.append(actual)
        actual = mapa_sur[actual]
        
    # Fusión de ambos tramos
    vía_completa = seccion_norte + seccion_sur
    
    print(f"Ruta de ingeniería finalizada: {' <-> '.join(vía_completa)}")
    return vía_completa

# --- PRUEBA DE CAMPO ---
excavacion_doble_sentido(red_ferroviaria, ciudad_a='A', ciudad_b='L')