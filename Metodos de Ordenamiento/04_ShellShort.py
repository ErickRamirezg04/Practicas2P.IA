from typing import List

def shell_sort(arr: List[int]) -> List[int]:
    """
    ShellSort.
    Extensión del método de inserción directa que permite realizar 
    comparaciones entre elementos distantes usando un intervalo (gap)[cite: 69].
    """
    a = arr.copy()
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- SHELLSORT ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {shell_sort(datos)}")