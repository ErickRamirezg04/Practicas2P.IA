"""
Simulador en Consola del Algoritmo de Kruskal (Mínimo y Máximo Coste).
Incluye estructura Union-Find explicada paso a paso.
"""
from typing import Dict, List, Tuple

# --- DEFINICIÓN DE LAS ARISTAS DEL GRAFO NO DIRIGIDO ---
# Formato: (Nodo1, Nodo2, Peso/Costo)
aristas_grafo: List[Tuple[str, str, int]] = [
    ('A', 'B', 4), ('A', 'C', 2),
    ('B', 'C', 1), ('B', 'D', 5),
    ('C', 'D', 6), ('C', 'E', 8),
    ('D', 'E', 3), ('D', 'F', 4),
    ('E', 'F', 7)
]
nodos_disponibles = ['A', 'B', 'C', 'D', 'E', 'F']

def mostrar_mapa_kruskal():
    print("\n" + "=" * 60)
    print("      MAPA DE CONEXIONES PARA EL ALGORITMO DE KRUSKAL   ")
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
    print("Nodos en la red: A, B, C, D, E, F")
    print("=" * 60 + "\n")

# --- ESTRUCTURA DISJOINT-SET (UNION-FIND) PARA DETECTAR CICLOS ---
class UnionFind:
    def __init__(self, nodos: List[str]):
        # Inicialmente cada nodo es su propio jefe/padre (conjuntos aislados)
        self.padre: Dict[str, str] = {nodo: nodo for nodo in nodos}

    def encontrar(self, nodo: str) -> str:
        # Busca la raíz o "representante" del conjunto al que pertenece el nodo
        if self.padre[nodo] == nodo:
            return nodo
        # Optimización por compresión de caminos
        self.padre[nodo] = self.encontrar(self.padre[nodo])
        return self.padre[nodo]

    def union(self, nodo_u: str, nodo_v: str) -> bool:
        raiz_u = self.encontrar(nodo_u)
        raiz_v = self.encontrar(nodo_v)
        
        # Si tienen la misma raíz, pertenecen al mismo conjunto (¡Alerta de Ciclo!)
        if raiz_u == raiz_v:
            return False
            
        # Si son diferentes, se fusionan los árboles colocando a uno como padre del otro
        self.padre[raiz_u] = raiz_v
        return True


def simulador_kruskal():
    mostrar_mapa_kruskal()
    
    # Menú interactivo de selección de criterio
    print("Seleccione el tipo de simulación que desea ejecutar:")
    print("  [1] Árbol de MÍNIMO coste (Presupuesto óptimo)")
    print("  [2] Árbol de MÁXIMO coste (Fiabilidad / Capacidad máxima)")
    
    while True:
        opcion = input("Elija una opción (1 o 2): ").strip()
        if opcion in ['1', '2']:
            break
        print("❌ Opción inválida. Digite 1 o 2.")
        
    es_minimo = (opcion == '1')
    criterio_txt = "MÍNIMO" if es_minimo else "MÁXIMO"
    
    # CRITERIO DE ORDENAMIENTO (Paso fundamental de Kruskal)
    # Ordena las aristas de menor a mayor para mínimo, y de mayor a menor para máximo
    aristas_ordenadas = sorted(aristas_grafo, key=lambda x: x[2], reverse=not es_minimo)
    
    print("\n" + "•" * 75)
    print(f" 📍 INICIANDO KRUSKAL - GENERANDO ÁRBOL DE COMPONENTES DE {criterio_txt} COSTE")
    print("•" * 75)
    print("\n--> PASO 1: Lista de aristas ordenadas según la prioridad del criterio:")
    for u, v, peso in aristas_ordenadas:
        print(f"    • Enlace [{u}] <---> [{v}] (Costo: {peso})")
        
    input("\nPresione ENTER para comenzar a evaluar las aristas una por una...")
    
    # Inicializar la memoria de conjuntos de Kruskal
    uf = UnionFind(nodos_disponibles)
    aristas_mst: List[Tuple[str, str, int]] = []
    costo_total = 0
    paso = 1
    
    for u, v, peso in aristas_ordenadas:
        print(f"\n⚡ EVALUANDO ARISTA {paso}: [{u}] <───({peso})───> [{v}] ⚡")
        
        raiz_u = uf.encontrar(u)
        raiz_v = uf.encontrar(v)
        
        print(f"    - Estado de control: '{u}' pertenece al conjunto raíz '{raiz_u}'")
        print(f"    - Estado de control: '{v}' pertenece al conjunto raíz '{raiz_v}'")
        
        # Intentar unir los conjuntos
        se_pudo_unir = uf.union(u, v)
        
        if se_pudo_unir:
            print(f"\n    ✅ [ARISTA ACEPTADA]")
            print(f"    ¿Por qué?: Como '{raiz_u}' y '{raiz_v}' son diferentes, unirlos NO genera un ciclo cerrado.")
            print(f"    Acción: El subárbol de '{u}' y el de '{v}' ahora forman un solo componente conectado.")
            aristas_mst.append((u, v, peso))
            costo_total += peso
        else:
            print(f"\n    ❌ [ARISTA RECHAZADA - IGNORADA]")
            print(f"    ¿Por qué?: Ambos nodos ya están conectados indirectamente a través del conjunto '{raiz_u}'.")
            print(f"    Si pusiéramos este cable, provocaríamos un ciclo redundante (bucle eléctrico/lógico).")
            
        print(f"\n    --> Árbol actual: {[(a, b) for a, b, _ in aristas_mst]}")
        print(f"    --> Costo acumulado de la red: {costo_total}")
        paso += 1
        print("-" * 75)
        
        # Parada anticipada optimizada: un árbol de expansión completo tiene exactamente (V - 1) aristas
        if len(aristas_mst) == len(nodos_disponibles) - 1:
            print("\n🎯 ¡ÁRBOL COMPLETADO CON ÉXITO! Todos los nodos han quedado amarrados de forma óptima.")
            break
            
    # --- REPORTE DE INFRAESTRUCTURA FINAL ---
    print("\n" + "=" * 70)
    print(f"      REPORTE FINAL: ÁRBOL DE EXPANSION DE {criterio_txt} COSTE     ")
    print("=" * 70)
    print("🛠️ Conexiones definitivas de la infraestructura:")
    for inicio, fin, costo in aristas_mst:
        print(f"   • Enlace: [{inicio}] ───(Costo: {costo})─── [{fin}]")
    print(f"\n💰 INVERSIÓN TOTAL DE LA OPTIMIZACIÓN: {costo_total} unidades.")
    print("=" * 70)

if __name__ == "__main__":
    simulador_kruskal()