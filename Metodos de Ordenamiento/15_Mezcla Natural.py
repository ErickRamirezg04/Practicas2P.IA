from typing import List

def obtener_tramos_naturales(a: List[int]) -> List[int]:
    # Encuentra los índices donde terminan las secuencias ordenadas de forma natural
    puntos = [0]
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            puntos.append(i)
    puntos.append(len(a))
    return puntos

def natural_merging(arr: List[int]) -> List[int]:
    """
    Simulación de Mezcla Natural (Natural Merging - Ordenamiento Externo).
    Detecta secuencias que ya vienen ordenadas por azar y las fusiona.
    """
    a = arr.copy()
    
    while True:
        tramos = obtener_tramos_naturales(a)
        if len(tramos) <= 2:  # Ya solo queda un único tramo completo ordenado
            break
            
        nueva_lista = []
        i = 0
        while i < len(tramos) - 1:
            if i + 2 < len(tramos):
                # Mezclar tramo i con tramo i+1
                izq, medio, der = tramos[i], tramos[i+1], tramos[i+2]
                idx_i, idx_j = izq, medio
                while idx_i < medio and idx_j < der:
                    if a[idx_i] <= a[idx_j]:
                        nueva_lista.append(a[idx_i]); idx_i += 1
                    else:
                        nueva_lista.append(a[idx_j]); idx_j += 1
                nueva_lista.extend(a[idx_i:medio])
                nueva_lista.extend(a[idx_j:der])
                i += 2
            else:
                # Si queda un tramo huérfano al final, solo se copia
                nueva_lista.extend(a[tramos[i]:tramos[i+1]])
                i += 1
        a = nueva_lista
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- MEZCLA NATURAL (EXTERNO) ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {natural_merging(datos)}")