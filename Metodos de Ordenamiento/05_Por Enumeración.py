from typing import List

def enumeration_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento por Enumeración.
    Compara cada elemento contra los demás y cuenta cuántos son 
    más pequeños para determinar su posición final exacta[cite: 64, 65, 66].
    """
    a = arr.copy()
    n = len(a)
    resultado = [0] * n
    for i in range(n):
        count = 0
        for j in range(n):
            # La condición 'j < i' garantiza la estabilidad con elementos duplicados
            if a[j] < a[i] or (a[j] == a[i] and j < i):
                count += 1
        resultado[count] = a[i]
    return resultado

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- ORDENAMIENTO POR ENUMERACIÓN ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {enumeration_sort(datos)}")