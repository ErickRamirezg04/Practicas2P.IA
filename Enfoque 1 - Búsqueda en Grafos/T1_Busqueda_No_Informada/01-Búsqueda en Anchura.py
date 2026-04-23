#¿Qué es la Búsqueda en Anchura (BFS)?
#La Búsqueda en Anchura (Breadth-First Search) es un algoritmo de exploración para grafos y árboles. 
#Su funcionamiento se basa en expandirse por "niveles": primero visita el nodo raíz, luego todos los
# #vecinos directos de ese nodo, después los vecinos de esos vecinos, y así sucesivamente.

#Cómo funciona:
#Utiliza una estructura de Cola. El primer nodo en entrar es el primero en ser explorado.
#Garantiza encontrar el camino más corto (en número de pasos) en grafos sin pesos.
#Es ideal cuando sabemos que el objetivo está cerca de la raíz.

# Definición de la estructura de datos (Red de conexiones)
mapa_nodos = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': ['G', 'H'],
    'E': ['I', 'J'],
    'F': ['K', 'L'],
    'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}

def rastrear_objetivo(red, punto_inicio, objetivo):
    """
    Realiza una exploración por niveles para localizar un elemento específico.
    """
    # Lista de espera para procesar los nodos (Estructura FIFO)
    pendientes = []
    
    # Registro de elementos ya procesados para evitar ciclos infinitos
    explorados = set()
    
    # Inicializamos la exploración con el punto de partida
    pendientes.append(punto_inicio)
    
    # Procesamos mientras existan elementos en la lista de espera
    while pendientes:
        # Extraemos el elemento más antiguo de la lista (el primero en llegar)
        actual = pendientes.pop(0)
        print(f"Analizando posición: {actual}")
        
        # Verificamos si hemos llegado al destino
        if actual == objetivo:
            print(f"\nLocalización exitosa: '{objetivo}' ha sido hallado.")
            return True
            
        # Si el nodo actual no ha sido procesado previamente, expandimos sus ramas
        if actual not in explorados:
            explorados.add(actual)
            
            # Obtenemos las conexiones (vecinos) del nodo actual
            conexiones = red.get(actual, [])
            
            # Añadimos cada conexión al final de la lista de pendientes
            for proximo in conexiones:
                pendientes.append(proximo)
                
    # Si la lista se vacía sin éxito, el objetivo no existe en esta red
    print(f"\nResultado: '{objetivo}' es inaccesible desde el origen.")
    return False

# EJECUCIÓN DEL PROCESO
print("Ejecutando protocolo de búsqueda por niveles...")
rastrear_objetivo(mapa_nodos, punto_inicio='A', objetivo='J')