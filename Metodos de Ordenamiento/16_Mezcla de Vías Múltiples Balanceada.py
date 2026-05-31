from typing import List

def balanced_multiway_merging(arr: List[int]) -> List[int]:
    """
    Simulación de Mezcla de Vías Múltiples Balanceada (Ordenamiento Externo).
    Simula una distribución balanceada usando 3 vías simultáneas de mezcla.
    """
    if len(arr) <= 1:
        return arr
        
    a = arr.copy()
    # Distribución en 3 vías independientes (N-vías)
    vias: List[List[int]] = [[], [], []]
    for idx, elemento in enumerate(a):
        vias[idx % 3].append(elemento)
        
    # Ordenar las vías localmente antes de la fusión balanceada
    vias = [sorted(via) for via in vias]
    
    # Proceso de mezcla balanceada combinando los punteros de las N vías
    resultado = []
    punteros = [0, 0, 0]
    
    while True:
        valor_minimo = float('inf')
        via_elegida = -1
        
        for k in range(3):
            if punteros[k] < len(vias[k]):
                if vias[k][punteros[k]] < valor_minimo:
                    valor_minimo = vias[k][punteros[k]]
                    via_elegida = k
                    
        if via_elegida == -1:
            break
            
        resultado.append(int(valor_minimo))
        punteros[via_elegida] += 1
        
    return resultado

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- MEZCLA DE VÍAS MÚLTIPLES BALANCEADA (EXTERNO) ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {balanced_multiway_merging(datos)}")