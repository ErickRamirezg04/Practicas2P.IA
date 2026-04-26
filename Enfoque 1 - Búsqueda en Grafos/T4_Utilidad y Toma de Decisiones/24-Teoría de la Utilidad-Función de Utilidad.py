#¿Qué es la Teoría de la Utilidad?
# En IA, no basta con encontrar un camino; a veces hay que elegir el "mejor" entre varios caminos 
# inciertos. La Teoría de la Utilidad es el marco matemático que permite a un agente racional 
# tomar decisiones bajo incertidumbre.

# Conceptos clave:
# Función de Utilidad ($U$): Asigna un número real a cada estado para indicar qué tan deseable es.
# Incertidumbre: Las acciones tienen resultados probabilísticos (no siempre sale lo que planeas).
# Utilidad Esperada (EU): Es el promedio ponderado de todos los resultados posibles. 

# Se calcula como:$$EU(a) = \sum_{s'} P(s'|a,s) U(s')$$Donde $P$ es la probabilidad de llegar al 
# estado $s'$ realizando la acción $a$.
def simulador_decision_autonoma():
    print("=" * 65)
    print(" 🤖 MÓDULO DE DECISIÓN RACIONAL: VEHÍCULO AUTÓNOMO ")
    print("=" * 65)
    
    print("\n1. DEFINIENDO LA FUNCIÓN DE UTILIDAD U(s)")
    print("   Es la escala de valores del vehículo. Priorizamos la seguridad.")
    print("   - U(Llegar a tiempo y a salvo) = 100")
    print("   - U(Retraso leve) = 50")
    print("   - U(Colisión/Accidente) = -1000 (Catastrófico)")

    print("\n2. EL ESCENARIO DE INCERTIDUMBRE")
    print("   Hay una tormenta. El vehículo debe elegir entre la Autopista o la Ciudad.")

    # --- SIMULACIÓN DE CÁLCULOS INTERNOS ---
    
    # Acción A: Autopista (Rápida pero peligrosa con lluvia)
    # 90% probabilidad de éxito (Llegar a tiempo) -> U=100
    # 10% probabilidad de hidroplaneo (Accidente) -> U=-1000
    p_auto_exito, u_auto_exito = 0.90, 100
    p_auto_fallo, u_auto_fallo = 0.10, -1000

    # Acción B: Ruta Ciudad (Lenta pero muy segura)
    # 100% probabilidad de llegar (aunque con retraso) -> U=50
    p_ciu_exito, u_ciu_exito = 1.0, 50

    # Cálculo de la Utilidad Esperada (EU)
    # EU = (Probabilidad1 * Utilidad1) + (Probabilidad2 * Utilidad2)
    eu_autopista = (p_auto_exito * u_auto_exito) + (p_auto_fallo * u_auto_fallo)
    eu_ciudad = (p_ciu_exito * u_ciu_exito)

    print("\n" + "-" * 65)
    print(" ⚙️  PROCESANDO MAXIMIZACIÓN DE UTILIDAD ESPERADA (MEU) ")
    print("-" * 65)

    print(f"\n[Evaluando Opción A: Autopista]")
    print(f"   -> Riesgo de accidente del 10% detectado.")
    print(f"   -> EU = (0.90 * 100) + (0.10 * -1000)")
    print(f"   -> Utilidad Esperada: {eu_autopista} puntos.")

    print(f"\n[Evaluando Opción B: Ruta Ciudad]")
    print(f"   -> Seguridad garantizada, pero con tráfico.")
    print(f"   -> EU = (1.0 * 50)")
    print(f"   -> Utilidad Esperada: {eu_ciudad} puntos.")

    print("\n3. CONCLUSIÓN DEL AGENTE RACIONAL")
    print("   La IA elige la opción con el valor de utilidad más alto.")
    
    if eu_autopista > eu_ciudad:
        print(f"\n   [DECISIÓN: AUTOPISTA] -> Los beneficios superan los riesgos.")
    else:
        # En este caso, el gran valor negativo del accidente (-1000) arrastra la decisión.
        print(f"\n   [DECISIÓN: CIUDAD] -> El riesgo catastrófico es demasiado alto.")
        print("   Incluso con un 90% de éxito, el 10% de desastre no es racionalmente aceptable.")

    print("\n" + "=" * 65)
    print(" ¡Matemáticamente, la IA ha elegido el camino más 'seguro'! ")
    print("=" * 65)

# Ejecutamos la simulación
simulador_decision_autonoma()