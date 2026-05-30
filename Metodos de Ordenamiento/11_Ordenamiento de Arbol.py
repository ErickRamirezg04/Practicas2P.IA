from typing import List, Optional

class Nodo:
    def __init__(self, clave: int):
        self.val: int = clave
        self.izq: Optional[Nodo] = None
        self.der: Optional[Nodo] = None

def insertar(raiz: Optional[Nodo], clave: int) -> Nodo:
    if raiz is None:
        return Nodo(clave)
    if clave < raiz.val:
        raiz.izq = insertar(raiz.izq, clave)
    else:
        raiz.der = insertar(raiz.der, clave)
    return raiz

def recorrer_inorder(raiz: Optional[Nodo], resultado: List[int]) -> None:
    if raiz:
        recorrer_inorder(raiz.izq, resultado)
        resultado.append(raiz.val)
        recorrer_inorder(raiz.der, resultado)

def tree_sort(arr: List[int]) -> List[int]:
    """
    Ordenamiento de Árbol (TreeSort).
    Construye un árbol binario de búsqueda y recupera los datos
    de forma secuencial mediante un recorrido In-Order.
    """
    if not arr:
        return []
        
    raiz = None
    for elemento in arr:
        raiz = insertar(raiz, elemento)
        
    resultado: List[int] = []
    recorrer_inorder(raiz, resultado)
    return resultado

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- ORDENAMIENTO DE ÁRBOL ---")
    print(f"Original: {datos}")
    print(f"Ordenado: {tree_sort(datos)}")