from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento por Selección Directa (SelectionSort).
    Busca el elemento más pequeño de todo el conjunto y lo coloca 
    en su posición adecuada[cite: 60].
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Intercambia el mínimo encontrado con el elemento de la posición i
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- SELECCIÓN DIRECTA ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {selection_sort(datos)}")