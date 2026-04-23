#¿Qué es la Búsqueda en Grafos?
#A diferencia de la búsqueda en árboles, la Búsqueda en Grafos está diseñada para manejar 
# estructuras donde existen múltiples caminos para llegar a un mismo punto y, lo más importante, 
# donde existen ciclos (caminos cerrados).

#Cómo funciona:
# Utiliza una estructura de datos (generalmente un Set o Conjunto) llamada Memoria de Visitados o 
# Explored Set.
# Antes de agregar un nodo a la cola de exploración, el algoritmo consulta su memoria: si el nodo 
# ya fue procesado, lo descarta.
# Esta verificación es lo que evita que el programa entre en un bucle infinito 
# (quedarse saltando entre A y B para siempre).
#Garantiza la terminación del algoritmo incluso en redes altamente interconectadas.

# Base de datos de amistades (Grafo con conexiones recíprocas/ciclos)
red_social = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J', 'K'],
    'G': ['D', 'L'],
    'H': ['D'],
    'I': ['E', 'M', 'N'],
    'J': ['F'],
    'K': ['F', 'O'],
    'L': ['G', 'P'],
    'M': ['I'],
    'N': ['I', 'Q'],
    'O': ['K'],
    'P': ['L'],
    'Q': ['N', 'R'],
    'R': ['Q']
}

def vincular_usuarios(plataforma, perfil_inicio, perfil_destino):
    """
    Busca una cadena de contactos entre dos perfiles evitando redundancias.
    """
    print(f"--- Buscando vínculo entre {perfil_inicio} y {perfil_destino} ---")
    
    # Lista de perfiles por analizar (Perfil actual, cadena de amigos)
    fila_analisis = [(perfil_inicio, [perfil_inicio])]
    
    # Registro histórico para evitar procesar al mismo usuario dos veces
    bitacora_usuarios = set()

    while fila_analisis:
        # Extraemos el siguiente perfil en la fila
        perfil_focal, cadena_contactos = fila_analisis.pop(0)

        # Si el perfil analizado es el que buscamos, devolvemos la ruta
        if perfil_focal == perfil_destino:
            print(f"\n¡CONEXIÓN ESTABLECIDA! Usuario '{perfil_destino}' localizado.")
            print(f"Grados de separación: {len(cadena_contactos) - 1}")
            print(f"Ruta de contacto: {' -> '.join(cadena_contactos)}")
            return True

        # Verificamos si este perfil ya pasó por nuestra auditoría
        if perfil_focal not in bitacora_usuarios:
            # Marcamos al usuario para no volver a él en el futuro
            bitacora_usuarios.add(perfil_focal)
            print(f"\n[*] Auditando perfil: {perfil_focal}")
            
            # Revisamos la lista de amigos del perfil actual
            contactos_directos = plataforma.get(perfil_focal, [])
            
            for conocido in contactos_directos:
                # Si el amigo ya fue auditado, lo omitimos para no crear un ciclo
                if conocido in bitacora_usuarios:
                    print(f"    - Omitiendo '{conocido}': Ya registrado en bitácora.")
                else:
                    # Si es un contacto nuevo, lo ponemos en la fila de espera
                    print(f"    - Agregando '{conocido}' a la fila de espera")
                    nueva_cadena = cadena_contactos + [conocido]
                    fila_analisis.append((conocido, nueva_cadena))
                    
    print(f"\nNo existe ninguna cadena de conexión hacia '{perfil_destino}'.")
    return False

# --- PRUEBA DE LA RED SOCIAL ---
# Buscamos conectar a 'A' con su contacto indirecto 'K'
vincular_usuarios(red_social, perfil_inicio='A', perfil_destino='K')