"""
Simulador en Consola del Algoritmo de Prim.
Muestra el mapa inicial, permite elegir el origen (con 'A' por defecto)
y explica detalladamente la construcción del árbol paso a paso.
"""
from typing import Dict, List, Set, Tuple

# --- DEFINICIÓN DEL GRAFO NO DIRIGIDO (MAPA DE PRUEBA) ---
# Al ser no dirigido, si A se conecta con B, B también se conecta con A.
mapa_prim = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 6, 'E': 8},
    'D': {'B': 5, 'C': 6, 'E': 3, 'F': 4},
    'E': {'C': 8, 'D': 3, 'F': 7},
    'F': {'D': 4, 'E': 7}
}

def mostrar_mapa_ascii():
    print("\n" + "=" * 60)
    print("       MAPA DE CONEXIONES PARA EL ALGORITMO DE PRIM     ")
    print("=" * 60)
    print("""
          (4)           (5)
       [B] --------- [D] ---------\\
      /   |         /   |          \\ (4)
     /     |       /     |          \\
 (4)/     (1)   (6)/     (3)          \\
   /       |      /       |           v
 [A] ----- [C] --/       [E] -------- [F]
   \\       /              |          /
 (2)\\     /               |         / (7)
     \\---/                \\--------/
          (2)                (7)
    """)
    print("Nodos disponibles en la red: A, B, C, D, E, F")
    print("Objetivo: Conectar todos los nodos al menor costo total.")
    print("=" * 60 + "\n")


def simulador_prim_consola():
    mostrar_mapa_ascii()
    
    # Solicitar nodo de origen interactivo con blindaje por defecto en 'A'
    while True:
        origen = input("Introduzca el NODO DE ORIGEN (Presione ENTER para usar 'A' por defecto): ").upper().strip()
        if origen == "":
            origen = 'A'
            print("-> Seleccionado automáticamente el nodo 'A' de la clase.")
            break
        if origen in mapa_prim:
            break
        print("❌ Error: El nodo no existe en el mapa. Intente de nuevo.")

    print("\n" + "•" * 70)
    print(f"  📍 INICIANDO CONSTRUCCIÓN DEL MST DESDE EL NODO: '[{origen}]'")
    print("•" * 70)
    input("\nPresione ENTER para comenzar a conectar la red paso a paso...")

    # Estructuras lógicas de Prim
    nodos_visitados: Set[str] = {origen}
    nodos_pendientes: Set[str] = set(mapa_prim.keys()) - nodos_visitados
    aristas_mst: List[Tuple[str, str, int]] = []
    costo_total = 0
    paso = 1

    while nodos_pendientes:
        print(f"\n⚡ PASO {paso} ⚡")
        print(f"Nodos ya conectados al árbol : {sorted(list(nodos_visitados))}")
        print(f"Nodos aislados (pendientes)  : {sorted(list(nodos_pendientes))}")
        
        print("\n--> Buscando todas las aristas posibles que salen de nuestra red conectada hacia los nodos aislados:")
        aristas_candidatas = []
        
        # Evaluar aristas desde cualquier nodo ya conectado hacia los no conectados
        for nodo_u in nodos_visitados:
            for nodo_v, peso in mapa_prim[nodo_u].items():
                if nodo_v in nodos_pendientes:
                    aristas_candidatas.append((nodo_u, nodo_v, peso))
                    print(f"    * Opción: [{nodo_u}] ---({peso})---> [{nodo_v}]")
                    
        if not aristas_candidatas:
            print("⚠️ Error: El grafo está desconectado. No se pueden alcanzar más nodos.")
            break
            
        # CRITERIO GREEN/CODICIOSO: Elegir la arista con el menor peso
        arista_elegida = min(aristas_candidatas, key=lambda x: x[2])
        u, v, peso_elegido = arista_elegida
        
        print(f"\n--> DECISIÓN DEL ALGORITMO:")
        print(f"    ¡Seleccionamos la arista [{u}] ---({peso_elegido})---> [{v}]!")
        print(f"    ¿Por qué?: Es la conexión más barata disponible que extiende nuestra red sin crear bucles.")
        
        # Agregar al árbol y actualizar conjuntos
        aristas_mst.append(arista_elegida)
        costo_total += peso_elegido
        nodos_visitados.add(v)
        nodos_pendientes.remove(v)
        
        print(f"\n🏁 Fin del Paso {paso}: El nodo '{v}' ahora forma parte de la red.")
        print(f"    Costo acumulado de la infraestructura: {costo_total}")
        paso += 1
        print("-" * 70)
        input("Presione ENTER para buscar la siguiente conexión...")

    # --- REPORTE FINAL ---
    print("\n" + "=" * 70)
    print("      SIMULACIÓN CONCLUIDA - ÁRBOL DE EXPANSIÓN MÍNIMA (MST)     ")
    print("=" * 70)
    print(f"📍 Nodo Raíz de Inicio : {origen}")
    print("🛠️ Conexiones de infraestructura óptimas a construir:")
    for inicio, fin, costo in aristas_mst:
        print(f"   • Tramo: [{inicio}] ───(Costo: {costo})─── [{fin}]")
    print(f"\n💰 COSTO MÍNIMO TOTAL DE LA RED: {costo_total} unidades de recursos.")
    print("=" * 70)

if __name__ == "__main__":
    simulador_prim_consola()