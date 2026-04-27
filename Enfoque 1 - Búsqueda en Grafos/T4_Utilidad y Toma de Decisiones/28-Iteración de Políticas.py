#¿Qué es la Iteración de Políticas?
#A diferencia de la Iteración de Valores (que actualiza los números hasta que estos convergen), 
# la Iteración de Políticas se enfoca en el comportamiento. Es un proceso cíclico más parecido a 
# cómo aprendemos los humanos: tomamos una decisión, vemos qué tan bien nos va, y ajustamos nuestra 
# estrategia.

#El algoritmo se divide en dos fases críticas:

#Evaluación de la Política: Dado un manual de instrucciones actual (política), calculamos qué tan 
# valioso es cada estado si seguimos ese manual a rajatabla.

#Mejora de la Política: Una vez que sabemos el valor de los estados, revisamos si existe alguna 
# acción distinta que nos dé un mejor resultado. Si la hay, actualizamos el manual.

# --- CONFIGURACIÓN DEL SIMULADOR ---
puntos = ['Hangar', 'Pista_Hielo', 'Meta', 'Colisión']
premios = {'Hangar': -1, 'Pista_Hielo': -1, 'Meta': 100, 'Colisión': -100}
terminales = ['Meta', 'Colisión']
maniobras = ['Avanzar', 'Esperar']

# Modelo de Transición: La física del entorno
fisica_vuelo = {
    'Hangar': {
        'Avanzar': [(0.9, 'Pista_Hielo'), (0.1, 'Hangar')],
        'Esperar': [(1.0, 'Hangar')]
    },
    'Pista_Hielo': {
        'Avanzar': [(0.7, 'Meta'), (0.3, 'Colisión')],
        'Esperar': [(1.0, 'Hangar')]
    }
}

gamma = 0.9 # Factor de importancia del futuro

def evaluar_manual(manual, valores):
    """FASE 1: Estima el valor de supervivencia siguiendo el manual actual."""
    for _ in range(15): # Estabilización rápida de valores
        nuevos_valores = valores.copy()
        for s in puntos:
            if s in terminales:
                nuevos_valores[s] = premios[s]
                continue
            
            accion = manual[s]
            # Utilidad = R(s) + γ * Σ P(s'|s,a) * U(s')
            eu = sum(p * valores[dest] for p, dest in fisica_vuelo[s][accion])
            nuevos_valores[s] = premios[s] + (gamma * eu)
        valores = nuevos_valores
    return valores

def optimizar_navegacion():
    """FASE 2: Mejora el manual de maniobras iterativamente."""
    print("--- INICIANDO ENTRENAMIENTO DE PILOTO AUTOMÁTICO ---")
    
    # Iniciamos con una política conservadora (y errónea): 'Esperar' en todo
    manual = {s: 'Esperar' for s in puntos if s not in terminales}
    valores = {s: 0.0 for s in puntos}
    
    ciclo = 1
    while True:
        print(f"\n[Ciclo de Entrenamiento {ciclo}]")
        print(f"  Estrategia actual: Hangar->{manual['Hangar']}, Pista->{manual['Pista_Hielo']}")
        
        # 1. EVALUACIÓN: ¿Cuánto vale cada sitio con este manual?
        valores = evaluar_manual(manual, valores)
        
        # 2. MEJORA: ¿Podemos hacerlo mejor?
        estrategia_estable = True
        for s in puntos:
            if s in terminales: continue
            
            maniobra_vieja = manual[s]
            # Buscamos la maniobra que maximiza el valor futuro
            mejor_maniobra = max(maniobras, key=lambda m: sum(p * valores[d] for p, d in fisica_vuelo[s][m]))
            
            if mejor_maniobra != maniobra_vieja:
                manual[s] = mejor_maniobra
                estrategia_estable = False
                print(f"  [*] ¡Ajuste de mando! En '{s}': {maniobra_vieja} -> {mejor_maniobra}")
        
        if estrategia_estable:
            print("\n[✔] Entrenamiento completado: La política es óptima.")
            break
        ciclo += 1
        
    return manual, valores

# --- EJECUCIÓN ---
estrategia_final, valores_finales = optimizar_navegacion()

print("\n" + "="*50)
print(" MANUAL DE VUELO DEFINITIVO ")
print("="*50)
for s in ['Hangar', 'Pista_Hielo']:
    print(f" Ubicación: {s.ljust(12)} -> Acción: {estrategia_final[s].upper()}")