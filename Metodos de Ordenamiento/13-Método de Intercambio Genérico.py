from typing import List

def exchange_sort(arr: List[int]) -> List[int]:
    """
    Método de Intercambio Directo Genérico.
    Compara de forma consecutiva un elemento base contra el resto
    del arreglo, intercambiando valores de dos en dos en caso necesario.
    """
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- METODO DE INTERCAMBIO ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {exchange_sort(datos)}")