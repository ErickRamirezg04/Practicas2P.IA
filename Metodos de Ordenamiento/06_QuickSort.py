from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """
    QuickSort (Ordenación rápida).
    Algoritmo complejo basado en la estrategia de división y partición 
    alrededor de un pivote[cite: 58, 70].
    """
    if len(arr) <= 1:
        return arr
    
    pivote = arr[len(arr) // 2]
    izq = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    der = [x for x in arr if x > pivote]
    
    return quick_sort(izq) + centro + quick_sort(der)

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- QUICKSORT ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {quick_sort(datos)}")