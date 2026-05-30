from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento por Inserción Directa (InsertionSort).
    Toma los elementos uno a uno y los inserta en la posición 
    apropiada respecto a los ya ordenados[cite: 52, 53].
    """
    a = arr.copy()
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        # Desplaza los elementos mayores una posición a la derecha [cite: 309, 322]
        while j >= 0 and a[j] > temp:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- INSERCIÓN DIRECTA ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {insertion_sort(datos)}")