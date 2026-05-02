#Las Gramáticas Probabilísticas Lexicalizadas (LPCFG) son la respuesta al mayor defecto de las PCFG 
# estándar: la falta de "memoria" sobre las palabras específicas.
# En una gramática normal, la regla de una Frase Verbal ($VP \rightarrow V \dots$) tiene la misma 
# probabilidad sin importar qué verbo sea. Pero en la realidad, el verbo "comer" tiene mucha más 
# probabilidad de ir seguido por un objeto (comida), mientras que el verbo "dormir" casi nunca lo hace. 
# Las LPCFG solucionan esto asociando cada regla con una palabra clave llamada "Cabeza" (Head).

# El Concepto de "Head" (Cabeza)En una gramática lexicalizada, cada nodo del árbol sintáctico hereda 
# una palabra de sus hijos.En una Frase Nominal ($NP$), la cabeza suele ser el Sustantivo.
# En una Frase Verbal ($VP$), la cabeza es el Verbo.Esto permite que la IA calcule probabilidades 
# basadas en dependencias reales: ¿Qué tan probable es que el sujeto "Chef" realice la acción "cocinar"?
#  Esto es mucho más preciso que simplemente preguntar: ¿Qué tan probable es que un Sustantivo realice 
# un Verbo?

# =====================================================================
# GRAMÁTICAS LEXICALIZADAS: DEPEDENCIA DE PALABRAS (HEADS)
# =====================================================================

# Simulamos probabilidades de dependencia léxica
# P(Objeto Directo | Verbo)
dependencias_lexicas = {
    ("comer", "NP"): 0.85,  # Es muy probable que 'comer' tenga un objeto
    ("dormir", "NP"): 0.05, # Es muy raro que 'dormir' tenga un objeto directo
}

def calcular_probabilidad_lexicalizada(verbo, estructura_hijo):
    """
    Calcula la probabilidad de una estructura gramatical 
    condicionada a la palabra 'cabeza'.
    """
    print(f"Analizando Verbo Cabeza: '{verbo}'")
    
    # Probabilidad base de la gramática (VP -> V NP)
    prob_gramatical = 0.5 
    
    # Probabilidad léxica (La 'magia' de la lexicalización)
    prob_lexica = dependencias_lexicas.get((verbo, estructura_hijo), 0.01)
    
    # La probabilidad final depende de ambos factores
    return prob_gramatical * prob_lexica

# --- PRUEBA ---
p1 = calcular_probabilidad_lexicalizada("comer", "NP")
p2 = calcular_probabilidad_lexicalizada("dormir", "NP")

print(f"Prob. de 'comer algo': {p1:.4f}")
print(f"Prob. de 'dormir algo': {p2:.4f}")