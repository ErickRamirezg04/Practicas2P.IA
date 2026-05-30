from typing import List

def heap_sort(arr: List[int]) -> List[int]:
    """
    HeapSort (Ordenamiento por Montículos).
    Algoritmo complejo que utiliza una estructura de árbol binario 
    (Max-Heap) para ordenar la información de forma eficiente[cite: 36, 70].
    """
    a = arr.copy()
    n = len(a)

    def heapify(lista, tamano, indice_raiz):
        mayor = indice_raiz
        izq = 2 * indice_raiz + 1
        der = 2 * indice_raiz + 2
        
        if izq < tamano and lista[izq] > lista[mayor]:
            mayor = izq
        if der < tamano and lista[der] > lista[mayor]:
            mayor = der
            
        if mayor != indice_raiz:
            lista[indice_raiz], lista[mayor] = lista[mayor], lista[indice_raiz]
            heapify(lista, tamano, mayor)

    # Paso 1: Construir el árbol montículo (Max-Heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
        
    # Paso 2: Extraer elementos del montículo uno a uno
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)
        
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- HEAPSORT ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {heap_sort(datos)}")