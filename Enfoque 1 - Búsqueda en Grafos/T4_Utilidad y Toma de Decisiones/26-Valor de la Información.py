#¿Qué es el Valor de la Información Perfecta (VPI)?
# El VPI (o VPI por sus siglas en inglés) cuantifica cuánto ganaría una IA si pudiera eliminar toda 
# la incertidumbre antes de actuar. Es una herramienta crítica porque le dice a la IA: "¿Vale la pena 
# gastar energía o dinero en obtener más datos?".

# Los tres pasos del cálculo:
# Utilidad Esperada Actual ($EU$): Lo que ganamos hoy con los datos que tenemos (eligiendo la mejor 
# acción posible a ciegas).
# Utilidad con Información Perfecta ($EU_{PI}$): Lo que ganaríamos si un "oráculo" nos dijera qué 
# va a pasar y nosotros pudiéramos adaptar nuestra acción a cada escenario.
# VPI: La diferencia entre ambos. Si el VPI es 0, no compres el sensor; si el VPI es alto, la 
# información es valiosa.

# --- 1. CONFIGURACIÓN DEL ENTORNO DE NEGOCIO ---
proyectos = ['Invertir en Oro', 'Mantener Efectivo']
escenarios_mercado = ['Subida', 'Caída']

# El mercado tiene un 70% de probabilidad de subir
p_mercado = {'Subida': 0.70, 'Caída': 0.30}

# Matriz de Utilidad (Decisión, Escenario) -> Ganancia en miles de USD
ganancias = {
    ('Invertir en Oro', 'Subida'): 50,    # Ganancia alta
    ('Invertir en Oro', 'Caída'): -100,   # Pérdida catastrófica
    ('Mantener Efectivo', 'Subida'): 0,   # Costo de oportunidad
    ('Mantener Efectivo', 'Caída'): 10    # El efectivo mantiene valor relativo
}

def simulador_valor_informacion():
    print("=" * 65)
    print(" 📊 LABORATORIO DE VPI: VALOR DE LA INFORMACIÓN PERFECTA ")
    print("=" * 65)

    # --- FASE 1: UTILIDAD ESPERADA SIN INFORMACIÓN ---
    print("\n[FASE 1] Calculando rendimiento actual (a ciegas):")
    eu_max_actual = float('-inf')
    mejor_accion_ciega = ""

    for accion in proyectos:
        # EU = Suma de (Probabilidad * Utilidad)
        eu_accion = sum(p_mercado[s] * ganancias[(accion, s)] for s in escenarios_mercado)
        print(f"  > Acción '{accion}': EU = {eu_accion:.2f}k")
        
        if eu_accion > eu_max_actual:
            eu_max_actual = eu_accion
            mejor_accion_ciega = accion

    print(f"Resultado: Sin más datos, la IA elige '{mejor_accion_ciega}' con {eu_max_actual:.2f}k.")

    # --- FASE 2: UTILIDAD CON ORÁCULO (INFORMACIÓN PERFECTA) ---
    print("\n[FASE 2] Calculando rendimiento con un Oráculo Perfecto:")
    eu_con_oraculo = 0

    for escenario in escenarios_mercado:
        # Si supiéramos de antemano el escenario, elegiríamos la MAX ganancia para ese caso
        mejor_ganancia_posible = max(ganancias[(a, escenario)] for a in proyectos)
        
        # Ponderamos esa ganancia óptima por la probabilidad de que ocurra ese escenario
        aporte = p_mercado[escenario] * mejor_ganancia_posible
        eu_con_oraculo += aporte
        
        print(f"  > Si el oráculo dice '{escenario}': Ganamos {mejor_ganancia_posible}k. (Pesa {aporte:.2f}k)")

    print(f"Resultado: Con información perfecta, la IA ganaría {eu_con_oraculo:.2f}k.")

    # --- FASE 3: EL VALOR DE LA INFORMACIÓN ---
    vpi = eu_con_oraculo - eu_max_actual
    
    print("\n" + "-" * 65)
    print(f" 💡 CONCLUSIÓN: VPI = {vpi:.2f}k USD ")
    print("-" * 65)
    print(f"La IA no debería pagar más de {vpi:.2f}k por un reporte de mercado.")
    
    if vpi > 0:
        print("La información es valiosa porque permite cambiar de opinión según el caso.")
    else:
        print("La información no tiene valor: harías lo mismo de todas formas.")

    return vpi

# --- EJECUCIÓN ---
simulador_valor_informacion()