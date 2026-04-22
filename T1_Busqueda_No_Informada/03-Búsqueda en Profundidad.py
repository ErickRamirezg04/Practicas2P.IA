#¿Qué es la Búsqueda en Profundidad (DFS)?
#La Búsqueda en Profundidad (Depth-First Search) es un algoritmo que prioriza ir lo más lejos 
# posible por una rama antes de retroceder (backtracking). En lugar de revisar todos los vecinos 
# inmediatos, elige uno y se sumerge hasta llegar a una "hoja" o nodo sin salida.

#Cómo funciona:
# Utiliza una estructura de Pila (LIFO - Last In, First Out). El último elemento en llegar es el 
# primero en ser procesado.
# Es muy eficiente en memoria si el árbol es muy ancho, pero puede perderse en ramas infinitas si no 
# se tiene cuidado.
# No garantiza encontrar el camino más corto, sino simplemente encontrar el objetivo.

# Estructura de carpetas y subcarpetas (Jerarquía de almacenamiento)
directorio_raiz = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': ['G', 'H'],
    'E': ['I', 'J'],
    'F': ['K', 'L'],
    'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}

def localizar_archivo(sistema_archivos, entrada, objetivo):
    """
    Simula un escaneo profundo en una estructura jerárquica.
    Prioriza la inmersión total en cada rama antes de cambiar de sector.
    """
    # Usamos una estructura de Pila para el comportamiento LIFO
    # Contiene tuplas de: (ubicacion_actual, historial_navegacion)
    almacen_pila = [(entrada, [entrada])]
    
    # Conjunto para rastrear sectores ya escaneados
    sectores_leidos = set()

    while almacen_pila:
        # El método pop() sin argumentos extrae el ÚLTIMO elemento añadido (cima de la pila)
        ubicacion_viva, rastro_carpetas = almacen_pila.pop()
        
        print(f"Escaneando sector: {ubicacion_viva}")

        # Verificación de coincidencia con el archivo buscado
        if ubicacion_viva == objetivo:
            print(f"\n--- ARCHIVO LOCALIZADO ---")
            print(f"Nombre del elemento: '{objetivo}'")
            print(f"Ruta de acceso: {' / '.join(rastro_carpetas)}")
            return True

        # Procesamos el sector si no ha sido escaneado previamente
        if ubicacion_viva not in sectores_leidos:
            sectores_leidos.add(ubicacion_viva)
            
            # Identificamos los subelementos o subcarpetas
            sub_elementos = sistema_archivos.get(ubicacion_viva, [])
            
            # Invertimos el orden para mantener la prioridad de izquierda a derecha en la pila
            for elemento in reversed(sub_elementos):
                if elemento not in sectores_leidos:
                    # Se apila el nuevo elemento con su ruta actualizada
                    ruta_extendida = rastro_carpetas + [elemento]
                    almacen_pila.append((elemento, ruta_extendida))
                    
    print(f"\nError 404: El elemento '{objetivo}' no existe en el volumen.")
    return False

# --- EJECUCIÓN DEL ESCANEO ---
print("Iniciando escaneo profundo del sistema...")
localizar_archivo(directorio_raiz, entrada='A', objetivo='J')