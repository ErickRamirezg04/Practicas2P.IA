#¿Qué es una Red Bayesiana?
# Una Red Bayesiana es un modelo gráfico que representa un conjunto de variables y sus dependencias 
# probabilísticas. A diferencia de un simple cálculo de Bayes, la red permite modelar sistemas 
# donde una causa puede tener múltiples efectos, o un efecto puede ser el resultado de varias causas 
# interactuando entre sí.

# Conceptos clave:
# Grafo Acíclico Dirigido (DAG): Las flechas muestran la dirección de la influencia 
# (Causa $\rightarrow$ Efecto). No puede haber ciclos.
# Tablas de Probabilidad Condicional (CPT): Cada nodo tiene una tabla que define su probabilidad 
# basada únicamente en el estado de sus padres.
# Inferencia por Enumeración: Es el proceso de "sumar" todos los escenarios posibles (mundos) para 
# responder a una pregunta específica, como: "¿Cuál es la probabilidad de X si sé que ocurrió Y?".

import itertools

# --- 1. ARQUITECTURA DE LA RED (Conexiones y Probabilidades) ---
# Representamos un sistema de alarma: Robo -> Alarma <- Terremoto
red_seguridad = {
    'Robo': {
        'padres': [],
        'cpt': {(): 0.001}  # P(Robo) es raro
    },
    'Terremoto': {
        'padres': [],
        'cpt': {(): 0.002}  # P(Terremoto) es raro
    },
    'Alarma': {
        'padres': ['Robo', 'Terremoto'],
        'cpt': {
            (True, True): 0.95,   # Suena por ambos
            (True, False): 0.94,  # Suena por robo
            (False, True): 0.29,  # Suena por terremoto
            (False, False): 0.001 # Ruido aleatorio
        }
    }
}

# --- 2. MOTOR DE CÁLCULO DE PROBABILIDAD CONJUNTA ---
def probabilidad_escenario(red, mundo):
    """Calcula P(Variable1, Variable2, ...) multiplicando las CPTs."""
    p_total = 1.0
    for nodo, config in red.items():
        valor_actual = mundo[nodo]
        # Obtenemos estados de los padres para buscar en la tabla
        estados_padres = tuple(mundo[p] for p in config['padres'])
        prob_ser_true = config['cpt'][estados_padres]
        
        # Aplicamos: P(X) si es True, (1-P(X)) si es False
        p_total *= prob_ser_true if valor_actual else (1.0 - prob_ser_true)
    return p_total

# --- 3. MOTOR DE INFERENCIA (Enumeración Exacta) ---
def realizar_consulta(red, consulta, evidencia):
    """Resuelve P(Consulta | Evidencia) analizando todos los mundos posibles."""
    nodos = list(red.keys())
    mundos_posibles = list(itertools.product([True, False], repeat=len(nodos)))
    
    total_evidencia = 0.0
    total_consulta_y_evidencia = 0.0

    for combinacion in mundos_posibles:
        mundo = dict(zip(nodos, combinacion))
        
        # Filtramos mundos que coinciden con lo que sabemos (evidencia)
        if all(mundo[v] == val for v, val in evidencia.items()):
            prob_m = probabilidad_escenario(red, mundo)
            total_evidencia += prob_m
            
            # De esos mundos, ¿cuántos cumplen la consulta?
            if all(mundo[v] == val for v, val in consulta.items()):
                total_consulta_y_evidencia += prob_m
                
    return total_consulta_y_evidencia / total_evidencia if total_evidencia > 0 else 0

# --- 4. PRUEBAS DE DIAGNÓSTICO ---
print("--- SISTEMA DE INFERENCIA BAYESIANA ---")

# Caso A: La alarma sonó. ¿Cuál es la probabilidad de que haya sido un robo?
evid_1 = {'Alarma': True}
cons_1 = {'Robo': True}
res_1 = realizar_consulta(red_seguridad, cons_1, evid_1)
print(f"Prob. de Robo si suena la alarma: {res_1*100:.2f}%")

# Caso B: Explaining Away (Descuento)
# La alarma sonó, PERO el sismógrafo detectó un terremoto. 
# ¿Cómo cambia la sospecha sobre el robo?
evid_2 = {'Alarma': True, 'Terremoto': True}
res_2 = realizar_consulta(red_seguridad, cons_1, evid_2)
print(f"Prob. de Robo si suena la alarma Y hubo terremoto: {res_2*100:.2f}%")