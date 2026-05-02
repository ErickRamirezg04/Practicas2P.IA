#Los 4 Pilares de la Extracción
#NER (Named Entity Recognition): Identificar nombres de personas, organizaciones, lugares, cantidades 
# o fechas.

#Extracción de Relaciones: Determinar cómo se conectan las entidades (ej. "Steve Jobs" [Fundador] de 
# "Apple").

#Extracción de Eventos: Identificar "qué pasó", "quién", "cuándo" y "dónde" (ej. un anuncio de 
# adquisición de una empresa).

#Resolución de Correferencia: Saber que "él", "el director" y "Juan" se refieren a la misma entidad 
# en un texto.

# =====================================================================
# EXTRACCIÓN DE INFORMACIÓN (NER + RELACIONES SIMPLIFICADO)
# =====================================================================

texto = "Elon Musk es el CEO de Tesla y fundó SpaceX en California"

# Diccionarios de conocimiento (Simulando un modelo entrenado)
entidades_conocidas = {
    "Elon Musk": "PERSONA",
    "Tesla": "ORGANIZACIÓN",
    "SpaceX": "ORGANIZACIÓN",
    "California": "LUGAR"
}

indicadores_relacion = ["CEO de", "fundó"]

def extraer_info(frase):
    print(f"Texto original: '{frase}'\n")
    
    # 1. Reconocimiento de Entidades (NER)
    entidades_encontradas = []
    for entidad, tipo in entidades_conocidas.items():
        if entidad in frase:
            entidades_encontradas.append((entidad, tipo))
            print(f"[NER] Encontrado: {entidad} ({tipo})")

    # 2. Extracción de Relaciones (Basada en patrones)
    print("\n--- Relaciones Detectadas ---")
    if "CEO de" in frase:
        # Lógica simple: Persona antes de 'CEO de', Org después.
        print("RELACIÓN: [Elon Musk] -> CARGO -> [Tesla]")
    
    if "fundó" in frase:
        print("RELACIÓN: [Elon Musk] -> FUNDADOR -> [SpaceX]")

# --- EJECUCIÓN ---
extraer_info(texto)