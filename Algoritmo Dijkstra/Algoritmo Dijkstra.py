"""
Simulador en Consola del Algoritmo de Dijkstra.
Muestra de forma interactiva el gráfico general, solicita origen/destino
y explica la toma de decisiones paso a paso.
"""
from typing import Dict, List, Set

# --- DEFINICIÓN DEL GRAFO (MAPA DE CIUDADES) ---
# Un diccionario de diccionarios que representa las conexiones y sus costos
mapa_ejemplo = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'C': 1},
    'C': {'B': 1, 'D': 6, 'E': 8},
    'D': {'F': 3, 'E': 2},
    'E': {'F': 5},
    'F': {}
}

def mostrar_grafico_general():
    """Imprime una representación visual en ASCII del mapa de nodos."""
    print("\n" + "=" * 60)
    print("      MAPA GENERAL DE CONEXIONES (GRAFO DE PRUEBA)      ")
    print("=" * 60)
    print("""
          (5)           (4)
       [B] ---------> [D] ---------\\\\
      ^   |          ^   |          \\\\ (3)
     /     |        /     |          \\\\
 (5)/     (1)   (6)/     (2)          v
   /       v      /       v          [F]
 [A] <---> [C] --/       [E] --------^
   \\\\       ^              |        /
 (2)\\\\     /               |       / (5)
     v----/                \\\\-----/
          (2)                (5)
    """)
    print("Nodos disponibles en la red: A, B, C, D, E, F")
    print("=" * 60 + "\n")


def simulador_dijkstra_interactivo():
    # 1. Mostrar el gráfico al inicio
    mostrar_grafico_general()
    
    # 2. Solicitar datos al usuario de forma dinámica
    while True:
        origen = input("Introduzca el NODO DE ORIGEN (Partida): ").upper().strip()
        if origen in mapa_ejemplo:
            break
        print("❌ Error: El nodo no existe en el mapa. Intente de nuevo.")
        
    while True:
        destino = input("Introduzca el NODO DE DESTINO (Llegada): ").upper().strip()
        if destino in mapa_ejemplo:
            if destino != origen:
                break
            print("❌ El destino no puede ser igual al origen. Elija otro punto.")
        else:
            print("❌ Error: El nodo no existe en el mapa. Intente de nuevo.")

    print("\n" + "•" * 70)
    print(f"  📍 INICIO DE TRAYECTO SELECCIONADO: De '[{origen}]' hacia '[{destino}]'")
    print("•" * 70)
    input("\nPresione ENTER para arrancar los cálculos del algoritmo paso a paso...")

    # Inicialización de estructuras de Dijkstra
    distancias = {nodo: float('inf') for nodo in mapa_ejemplo}
    distancias[origen] = 0
    predecesores = {nodo: None for nodo in mapa_ejemplo}
    nodos_no_visitados: Set[str] = set(mapa_ejemplo.keys())
    
    paso = 1
    
    while nodos_no_visitados:
        print(f"\n⚡ PASO {paso} ⚡")
        print(f"Estado de la memoria - Nodos pendientes por visitar: {sorted(list(nodos_no_visitados))}")
        print(f"Tabla de costos acumulados actuales: {distancias}")
        
        # Seleccionar el nodo con la distancia mínima acumulada que no haya sido visitado
        nodo_actual = min(nodos_no_visitados, key=lambda n: distancias[n])
        distancia_actual = distancias[nodo_actual]
        
        print(f"\n--> DECISIÓN: Analizaremos el nodo '{nodo_actual}'.")
        print(f"    ¿Por qué?: De los pendientes, es el que tiene la menor distancia acumulada descubierta ({distancia_actual}).")
        
        if nodo_actual == destino:
            print(f"\n🎯 ¡LLEGAMOS AL DESTINO SOLICITADO! Hemos alcanzado '{destino}' evaluando su ruta óptima.")
            break
            
        if distancia_actual == float('inf'):
            print(f"⚠️ Alerta: Los nodos restantes son inalcanzables desde el origen '{origen}'.")
            break
            
        # Evaluar vecinos del nodo seleccionado
        print(f"--> Inspeccionando las aristas salientes de '{nodo_actual}':")
        if not mapa_ejemplo[nodo_actual]:
            print(f"    (El nodo '{nodo_actual}' no tiene vecinos hacia donde avanzar, es un callejón sin salida).")
            
        for vecino, peso in mapa_ejemplo[nodo_actual].items():
            if vecino in nodos_no_visitados:
                nueva_distancia = distancia_actual + peso
                print(f"    * Evaluando camino a '{vecino}':")
                print(f"      Costo actual registrado = {distancias[vecino]}")
                print(f"      Nueva propuesta si pasamos por '{nodo_actual}' = {distancia_actual} + {peso} = {nueva_distancia}")
                
                if nueva_distancia < distancias[vecino]:
                    print(f"      ✅ [¡CAMINO MEJORADO!] Como {nueva_distancia} < {distancias[vecino]}, actualizamos la tabla.")
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                else:
                    print(f"      ❌ [RECHAZADO] No mejora la ruta que ya conocíamos ({distancias[vecino]}).")
            else:
                print(f"    * El vecino '{vecino}' ya fue cerrado y visitado previamente. Se ignora.")
                
        # Eliminar el nodo actual de la lista de pendientes
        nodos_no_visitados.remove(nodo_actual)
        print(f"\n🏁 Fin del Paso {paso}: El nodo '{nodo_actual}' queda marcado como VISITADO y su costo mínimo está asegurado.")
        paso += 1
        print("-" * 70)
        input("Presione ENTER para avanzar al siguiente paso...")

    # --- RECONSTRUCCIÓN DE LA RUTA ÓPTIMA FINAL ---
    print("\n" + "=" * 70)
    print("           SIMULACIÓN CONCLUIDA - REPORTE DE VIAJE           ")
    print("=" * 70)
    
    if distancias[destino] == float('inf'):
        print(f"❌ No existe ninguna combinación de caminos para ir desde '{origen}' hasta '{destino}'.")
    else:
        # Reconstruir la ruta hacia atrás usando los predecesores
        camino = []
        actual = destino
        while actual is not None:
            camino.insert(0, actual)
            actual = predecesores[actual]
            
        print(f"📍 PUNTO DE PARTIDA : {origen}")
        print(f"🏁 PUNTO DE LLEGADA : {destino}")
        print(f"🚀 RUTA ÓPTIMA      : {' ➔ '.join(camino)}")
        print(f"💰 COSTO TOTAL MIN. : {distancias[destino]} unidades de distancia/tiempo.")
    print("=" * 70)

if __name__ == "__main__":
    simulador_dijkstra_interactivo()