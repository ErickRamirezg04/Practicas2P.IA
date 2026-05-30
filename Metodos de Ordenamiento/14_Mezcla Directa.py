from typing import List

def straight_merging(arr: List[int]) -> List[int]:
    """
    Simulación de Mezcla Directa (Straight Merging - Ordenamiento Externo).
    Ordena combinando subtramos de datos de tamaño fijo de forma iterativa.
    """
    a = arr.copy()
    n = len(a)
    tamano_tramo = 1
    
    while tamano_tramo < n:
        # Simulamos la lectura externa por bloques
        for izq in range(0, n, 2 * tamano_tramo):
            medio = min(izq + tamano_tramo, n)
            der = min(izq + 2 * tamano_tramo, n)
            
            # Mezcla local simulando flujos de archivos temporales
            i, j = izq, medio
            mezclado = []
            while i < medio and j < der:
                if a[i] <= a[j]:
                    mezclado.append(a[i]); i += 1
                else:
                    mezclado.append(a[j]); j += 1
            mezclado.extend(a[i:medio])
            mezclado.extend(a[j:der])
            
            a[izq:der] = mezclado
            
        tamano_tramo *= 2
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- MEZCLA DIRECTA (EXTERNO) ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {straight_merging(datos)}")