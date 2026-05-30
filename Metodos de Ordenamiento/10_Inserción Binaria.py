from typing import List

def binary_insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento por Inserción Binaria.
    Optimiza la inserción directa utilizando búsqueda binaria para encontrar
    la posición correcta del elemento a insertar.
    """
    a = arr.copy()
    for i in range(1, len(a)):
        val = a[i]
        izq = 0
        der = i - 1
        
        # Búsqueda binaria del punto de inserción
        while izq <= der:
            medio = (izq + der) // 2
            if val < a[medio]:
                der = medio - 1
            else:
                izq = medio + 1
        
        # Desplazar elementos a la derecha
        for j in range(i - 1, izq - 1, -1):
            a[j + 1] = a[j]
            
        a[izq] = val
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- INSERCIÓN BINARIA ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {binary_insertion_sort(datos)}")