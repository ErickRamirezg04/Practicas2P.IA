from typing import List

def hashing_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento por Hashing (Bucket Sort conceptual).
    Distribuye los elementos en un mapa indexado proporcional a sus valores
    para recuperar la información sin realizar comparaciones directas de dos en dos.
    """
    if not arr:
        return arr
        
    min_val, max_val = min(arr), max(arr)
    rango = max_val - min_val + 1
    
    # Crear una tabla Hash / Cubetas vacías
    tabla_hash: List[List[int]] = [[] for _ in range(rango)]
    
    # Función Hash de mapeo directo
    for num in arr:
        indice = num - min_val
        tabla_hash[indice].append(num)
        
    # Recolectar de forma secuencial los elementos de la tabla
    resultado = []
    for cubeta in tabla_hash:
        resultado.extend(cubeta)
        
    return resultado

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- ORDENAMIENTO POR HASHING ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {hashing_sort(datos)}")