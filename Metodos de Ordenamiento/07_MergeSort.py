from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    MergeSort (Ordenamiento por Mezcla).
    Divide recursivamente el arreglo en mitades y luego las combina 
    de manera ordenada en memoria principal[cite: 28, 38].
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])
    
    # Proceso de combinación (Merge)
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
            
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- MERGESORT ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {merge_sort(datos)}")