#¿Cómo funciona una PCFG?
# Una PCFG extiende una gramática independiente del contexto asignando una probabilidad a cada regla 
# de producción. La suma de las probabilidades de todas las reglas para un mismo símbolo no terminal 
# debe ser siempre 1.0.
# Símbolos No Terminales: Como NP (Frase Nominal), VP (Frase Verbal).
# Reglas con Peso: $NP \rightarrow \text{Det } N$ (Prob: 0.7) o $NP \rightarrow \text{Pronoun}$ 
# (Prob: 0.3).
# Probabilidad del Árbol: Se calcula multiplicando las probabilidades de todas las reglas utilizadas 
# para construirlo.

# =====================================================================
# PCFG: GRAMÁTICA PROBABILÍSTICA INDEPENDIENTE DEL CONTEXTO
# =====================================================================

# Definición de la Gramática: Símbolo -> [(Producción, Probabilidad)]
gramatica_pcfg = {
    'S':  [(['NP', 'VP'], 1.0)],
    'NP': [(['Det', 'N'], 0.7), (['Pron'], 0.3)],
    'VP': [(['V', 'NP'], 0.6), (['V'], 0.4)],
    # Léxico (Palabras terminales)
    'Det': [(['el'], 1.0)],
    'N':   [(['gato'], 0.5), (['perro'], 0.5)],
    'V':   [(['come'], 1.0)],
    'Pron':[(['él'], 1.0)]
}

def calcular_probabilidad_arbol(estructura):
    """
    Simula el cálculo de probabilidad de una frase: 'el gato come'
    Estructura: S -> NP(Det, N) + VP(V)
    """
    # 1. S -> NP VP (p=1.0)
    p1 = 1.0 
    # 2. NP -> Det N (p=0.7)
    p2 = 0.7
    # 3. VP -> V (p=0.4)
    p3 = 0.4
    # 4. Det -> 'el' (p=1.0), N -> 'gato' (p=0.5), V -> 'come' (p=1.0)
    p_lexico = 1.0 * 0.5 * 1.0
    
    prob_total = p1 * p2 * p3 * p_lexico
    return prob_total

# --- EJECUCIÓN ---
frase = "el gato come"
probabilidad = calcular_probabilidad_arbol(frase)

print(f"Análisis de la frase: '{frase}'")
print(f"Probabilidad de la estructura gramatical: {probabilidad:.4f}")