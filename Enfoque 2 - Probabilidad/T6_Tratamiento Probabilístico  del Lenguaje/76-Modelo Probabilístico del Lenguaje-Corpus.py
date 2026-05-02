#1. El Corpus: 
# El ADN del ConocimientoUn Corpus es una colección masiva y estructurada de textos (libros, artículos, 
# conversaciones, código).
# Representatividad: Un modelo entrenado solo con un corpus de leyes hablará como un abogado.
# Pre-procesamiento: Para que la IA entienda el corpus, debemos limpiar el texto:

# Tokenización: Dividir el texto en unidades (palabras o sub-palabras).
# Normalización: Convertir a minúsculas, quitar puntuación o eliminar "stop words" (palabras vacías 
# como "el", "de").

# 2. Modelos de N-gramas
# La forma más sencilla de entender la probabilidad del lenguaje es mirar los N-gramas. Un N-grama es 
# una secuencia de $N$ palabras:
# Unigrama: Probabilidad de una palabra aislada.
# Bigrama: Probabilidad de una palabra dado que la anterior fue $X$.
# Trigrama: Probabilidad de una palabra dadas las dos anteriores.

import random
from collections import defaultdict

# =====================================================================
# MODELO DE LENGUAJE: BIGRAMAS (Markov Chain simplificado)
# =====================================================================

# 1. EL CORPUS (Materia prima)
corpus = """
la inteligencia artificial es asombrosa
la inteligencia es la capacidad de aprender
el aprendizaje profundo es una rama de la inteligencia
artificial significa que no es natural
"""

def entrenar_modelo(texto):
    tokens = texto.lower().split()
    # Diccionario de frecuencias: {palabra_actual: [lista_de_seguidoras]}
    modelo = defaultdict(list)
    
    for i in range(len(tokens) - 1):
        palabra_actual = tokens[i]
        siguiente_palabra = tokens[i+1]
        modelo[palabra_actual].append(siguiente_palabra)
    
    return modelo

def generar_texto(modelo, semilla, longitud=10):
    palabra = semilla.lower()
    resultado = [palabra]
    
    for _ in range(longitud - 1):
        opciones = modelo.get(palabra)
        if not opciones:
            break
        # Elegimos la siguiente palabra según su probabilidad estadística
        palabra = random.choice(opciones)
        resultado.append(palabra)
    
    return " ".join(resultado)

# --- EJECUCIÓN ---
mi_modelo = entrenar_modelo(corpus)

print("--- ESTADÍSTICAS DEL MODELO ---")
print(f"Sucesores de 'inteligencia': {mi_modelo['inteligencia']}")

print("\n--- GENERACIÓN ALEATORIA ---")
# Generamos texto basado en las probabilidades aprendidas del corpus
frase = generar_texto(mi_modelo, semilla="la", longitud=8)
print(f"IA dice: \"{frase}...\"")