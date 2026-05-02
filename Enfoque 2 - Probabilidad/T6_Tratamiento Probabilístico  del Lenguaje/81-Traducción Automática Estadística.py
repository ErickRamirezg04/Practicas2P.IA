#La Traducción Automática Estadística (SMT) fue el paradigma dominante antes de la llegada de las 
# redes neuronales. A diferencia de los sistemas antiguos basados en reglas gramaticales rígidas, 
# la SMT trata la traducción como un problema de probabilidad y estadística.

# Su filosofía es: "No intento entender el significado de la frase, intento calcular cuál es la 
# secuencia de palabras en el idioma destino que tiene más probabilidades de ser la traducción 
# correcta".

# Los Dos Pilares de la SMT (Modelo de Canal Ruidoso)Para traducir una frase, la SMT combina dos 
# modelos matemáticos distintos:
# Modelo de Traducción ($P(f|e)$): Mide qué tan bien se traducen las palabras individualmente. 
# Se entrena con Corpus Paralelos (textos que son traducciones exactas uno del otro).
# Modelo de Lenguaje ($P(e)$): Mide qué tan natural suena la frase en el idioma destino. Asegura que
#  el resultado sea gramaticalmente correcto, aunque el modelo no sepa gramática.

# =====================================================================
# TRADUCCIÓN ESTADÍSTICA SIMPLIFICADA (Modelos de Probabilidad)
# =====================================================================

# 1. Modelo de Traducción (Probabilidad de palabra origen dado destino)
prob_traduccion = {
    "the": {"el": 0.8, "la": 0.2},
    "cat": {"gato": 0.9, "felino": 0.1},
    "eats": {"come": 0.95, "ingiere": 0.05}
}

# 2. Modelo de Lenguaje (Probabilidad de bigramas en español)
# Nos dice que 'el gato' es más común que 'la gato'
prob_lenguaje = {
    ("el", "gato"): 0.9,
    ("la", "gato"): 0.01,
    ("gato", "come"): 0.8
}

def traducir_frase(frase_en):
    palabras = frase_en.lower().split()
    posibles_traducciones = [prob_traduccion[p].keys() for p in palabras]
    
    # En un sistema real, usaríamos el algoritmo de Viterbi para buscar
    # Aquí probamos dos combinaciones posibles:
    candidata_1 = ["el", "gato", "come"]
    candidata_2 = ["la", "gato", "come"]
    
    def evaluar(frase):
        # Simplificación: P(traducción) * P(lenguaje)
        p_trad = 1.0
        for i, p_en in enumerate(palabras):
            p_trad *= prob_traduccion[p_en].get(frase[i], 0.01)
        
        # Probabilidad de lenguaje (bigramas)
        p_lang = prob_lenguaje.get((frase[0], frase[1]), 0.01) * \
                 prob_lenguaje.get((frase[1], frase[2]), 0.01)
        
        return p_trad * p_lang

    s1 = evaluar(candidata_1)
    s2 = evaluar(candidata_2)
    
    return candidata_1 if s1 > s2 else candidata_2

# --- EJECUCIÓN ---
entrada = "the cat eats"
resultado = traducir_frase(entrada)
print(f"Inglés: {entrada} -> Español: {' '.join(resultado)}")