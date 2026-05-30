from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento Burbuja (BubbleSort).
    Revisa cada elemento de la lista con el siguiente, intercambiándolos 
    si están en el orden equivocado[cite: 80].
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        # El límite n - 1 evita desbordamiento de índice al evaluar j + 1 [cite: 180, 182]
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- ORDENAMIENTO BURBUJA ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {bubble_sort(datos)}")