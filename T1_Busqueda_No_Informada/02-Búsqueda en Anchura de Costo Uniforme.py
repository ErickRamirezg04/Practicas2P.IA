#¿Qué es la Búsqueda de Costo Uniforme (UCS)?
#Es un algoritmo de búsqueda no informada que se utiliza para encontrar el camino con el costo 
# total mínimo desde un nodo origen hasta un nodo destino. Es una variante de la búsqueda en anchura, 
# pero optimizada para grafos donde las aristas tienen diferentes pesos o valores.

#Cómo funciona:

#En lugar de una cola simple, utiliza idealmente una Cola de Prioridad.
#Siempre expande el nodo que tiene el menor costo acumulado desde la raíz.
#Garantiza la solución óptima (el camino más barato) siempre que los costos de los pasos sean positivos.
#Funciona de manera muy similar al algoritmo de Dijkstra, pero se detiene en cuanto encuentra el 
# objetivo.

# Estructura de conexiones con sus respectivos pesos (Costo de envío/distancia)
logistica_rutas = {
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 2)],
    'C': [('E', 8), ('F', 3)],
    'D': [('G', 1), ('H', 4)],
    'E': [('I', 2), ('J', 1)],
    'F': [('K', 6), ('L', 2)],
    'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}

def calcular_trayecto_economico(red_vial, inicio, destino):
    """
    Algoritmo UCS: Encuentra la ruta más barata basándose en el acumulado de pesos.
    Estructura de la lista: (costo_acumulado, punto_actual, historial_ruta)
    """
    # Inicializamos la frontera con el punto de partida, costo cero y su ruta inicial
    frontera_busqueda = [(0, inicio, [inicio])]
    
    # Historial para no repetir puntos y evitar bucles
    puntos_procesados = set()

    while frontera_busqueda:
        # Reordenamos la frontera para priorizar el trayecto con menor gasto acumulado
        # Usamos sort para simular el comportamiento de una cola de prioridad
        frontera_busqueda.sort(key=lambda item: item[0])
        
        # Extraemos el elemento con el valor de costo más bajo (el primero de la lista)
        gasto_total, punto_focal, rastro = frontera_busqueda.pop(0)
        
        print(f"Evaluando ubicación: {punto_focal} | Inversión acumulada: {gasto_total}")

        # Comprobamos si el punto actual es nuestro destino final
        if punto_focal == destino:
            print(f"\n--- OBJETIVO LOCALIZADO ---")
            print(f"Punto de llegada: '{destino}'")
            print(f"Secuencia de viaje: {' -> '.join(rastro)}")
            print(f"Costo final del trayecto: {gasto_total}")
            return True

        # Solo exploramos si no hemos analizado este punto con un costo menor anteriormente
        if punto_focal not in puntos_procesados:
            puntos_procesados.add(punto_focal)
            
            # Revisamos las ramificaciones (vecinos) del punto actual
            ramales = red_vial.get(punto_focal, [])
            
            for siguiente_punto, costo_tramo in ramales:
                if siguiente_punto not in puntos_procesados:
                    # Sumamos el costo del tramo actual al acumulado que traíamos
                    acumulado_actualizado = gasto_total + costo_tramo
                    
                    # Registramos el nuevo rastro del camino para este ramal
                    nuevo_rastro = rastro + [siguiente_punto]
                    
                    # Añadimos los datos a la frontera para ser evaluados en el próximo ciclo
                    frontera_busqueda.append((acumulado_actualizado, siguiente_punto, nuevo_rastro))
                    
    print(f"\nError: No existe una ruta disponible hacia '{destino}'.")
    return False

# --- PRUEBA DEL SISTEMA DE COSTOS ---
print("Iniciando motor de optimización de rutas...")
calcular_trayecto_economico(logistica_rutas, inicio='A', destino='L')