from typing import List

def radix_sort(arr: List[int]) -> List[int]:
    """
    RadixSort.
    Ordena los elementos procesando sus dígitos individuales de forma 
    posicional (unidades, decenas, centenas)[cite: 39].
    """
    if not arr:
        return arr
    a = arr.copy()
    max_num = max(a)
    exp = 1  # Representa la posición del dígito analizado (1, 10, 100...)
    
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in a:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        
        # Reagrupa los elementos según el orden posicional actual
        a = [num for bucket in buckets for num in bucket]
        exp *= 10
        
    return a

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- RADIXSORT ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {radix_sort(datos)}")