#1. El Modelo de Espacio Vectorial (VSM)
#En IR, no buscamos coincidencias exactas de letras. Convertimos cada documento y cada consulta en un 
# vector en un espacio multidimensional.

#Si el documento trata sobre "IA" y "Robots", su vector apuntará en esa dirección.

#Si tu búsqueda es "IA", el sistema busca el documento cuyo vector tenga el ángulo más pequeño 
# (Similitud de Coseno) con el tuyo.

#2. El Algoritmo TF-IDF
#Es la métrica reina para decidir qué tan importante es una palabra en un documento:

#TF (Term Frequency): Cuántas veces aparece la palabra en este documento. (Si aparece mucho, es 
# importante).

#IDF (Inverse Document Frequency): Qué tan rara es la palabra en toda la colección. (Si aparece en 
# todos los documentos, como "el" o "que", no sirve para distinguir y su valor baja).

import math
from collections import Counter

# =====================================================================
# RECUPERACIÓN DE DATOS: MOTOR DE BÚSQUEDA TF-IDF
# =====================================================================

# 1. COLECCIÓN DE DOCUMENTOS (Nuestro pequeño internet)
docs = [
    "la inteligencia artificial es el futuro",
    "el aprendizaje profundo es una rama de la inteligencia",
    "mañana va a llover en la ciudad",
    "el futuro de la computación es la inteligencia"
]

def buscar(consulta, documentos):
    # Tokenización simple
    query_terms = consulta.lower().split()
    resultados = []

    for i, doc in enumerate(documentos):
        doc_terms = doc.lower().split()
        cuenta = Counter(doc_terms)
        
        # Calculamos una puntuación simple (TF simplificado)
        score = 0
        for term in query_terms:
            if term in cuenta:
                # TF: frecuencia en el doc / IDF: peso por rareza (aquí 1 para simplificar)
                score += cuenta[term]
        
        if score > 0:
            resultados.append((score, documentos[i]))

    # Ordenar por relevancia (puntuación más alta primero)
    return sorted(resultados, reverse=True)

# --- PRUEBA ---
query = "inteligencia futuro"
print(f"Resultados para: '{query}'")
for score, texto in buscar(query, docs):
    print(f"  [Score: {score}] {texto}")