from typing import List

def polyphase_sort(arr: List[int]) -> List[int]:
    """
    Simulación conceptual de Ordenamiento Polifásico (Polyphase Sort).
    Distribuye y mezcla bloques bajo una estrategia asimétrica de archivos
    para minimizar las operaciones de intercambio.
    """
    if len(arr) <= 1:
        return arr
        
    # El ordenamiento polifásico divide los tramos iniciales usando proporciones fijas
    # Simulamos el comportamiento procesando particiones dinámicas desiguales
    a = arr.copy()
    mitad = int(len(a) * 0.618)  # Aproximación basada en la proporción Áurea/Fibonacci
    
    archivo_f1 = sorted(a[:mitad])
    archivo_f2 = sorted(a[mitad:])
    
    # Combinación directa asimétrica de ambos flujos de datos
    resultado = []
    i = j = 0
    while i < len(archivo_f1) and j < len(archivo_f2):
        if archivo_f1[i] <= archivo_f2[j]:
            resultado.append(archivo_f1[i]); i += 1
        else:
            resultado.append(archivo_f2[j]); j += 1
            
    resultado.extend(archivo_f1[i:])
    resultado.extend(archivo_f2[j:])
    return resultado

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- ORDENAMIENTO POLIFÁSICO (EXTERNO) ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {polyphase_sort(datos)}")