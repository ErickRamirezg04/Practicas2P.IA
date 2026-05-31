from typing import List

def distribution_of_initial_runs(arr: List[int]) -> List[List[int]]:
    """
    Simulación de Distribución de Tramos Iniciales (Distribution of initial runs).
    Rompe una colección masiva de datos en bloques pequeños (runs),
    los ordena de manera interna y los prepara en vías independientes.
    """
    a = arr.copy()
    tamano_bloque_ram = 3  # Tamaño máximo simulado que tolera la memoria principal
    tramos_escriptura_disco: List[List[int]] = []
    
    # Fase de lectura y pre-ordenamiento interno por bloques
    for i in range(0, len(a), tamano_bloque_ram):
        bloque_en_ram = a[i : i + tamano_bloque_ram]
        # Se ordena en memoria RAM (usando método interno estándar)
        bloque_en_ram.sort()
        # Se escribe de vuelta en el almacenamiento secundario (lista externa)
        tramos_escriptura_disco.append(bloque_en_ram)
        
    return tramos_escriptura_disco

if __name__ == "__main__":
    datos = [54, 26, 93, 17, 77, 31, 44, 55, 20, 17]
    print("--- DISTRIBUCIÓN DE TRAMOS INICIALES (EXTERNO) ---")
    print(f"Original: {datos}")
    print("Bloques pre-ordenados escritos en disco:")
    bloques_disco = distribution_of_initial_runs(datos)
    for idx, bloque in enumerate(bloques_disco):
        print(f"  Archivo_Temporal_{idx}: {bloque}")