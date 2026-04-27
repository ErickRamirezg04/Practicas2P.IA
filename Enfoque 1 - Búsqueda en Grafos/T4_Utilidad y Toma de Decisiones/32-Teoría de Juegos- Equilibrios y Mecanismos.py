#¿Qué es el Equilibrio de Nash?
#El Equilibrio de Nash es un concepto fundamental donde ningún jugador tiene incentivos para cambiar 
# su estrategia unilateralmente. En otras palabras, dada la jugada del oponente, tú estás haciendo 
# lo mejor que puedes, y viceversa. Es el punto de "estancamiento" o tregua matemática.

#Conceptos clave:

#Mejor Respuesta (Best Response): La estrategia que maximiza tu beneficio asumiendo que el otro 
# jugador ha elegido una acción específica.

#Estrategia Dominante: Una jugada que es mejor que todas las demás, sin importar lo que haga el 
# oponente.

#Óptimo de Pareto: Un estado donde es imposible mejorar la situación de un jugador sin empeorar 
# la de otro. Curiosamente, ¡el Equilibrio de Nash no siempre es un Óptimo de Pareto!

# --- CONFIGURACIÓN DE LA COMPETENCIA ---
competidores = ['SkyJet', 'OceanicAir']
estrategias = ['Precio_Premium', 'Precio_Descuento']

# Matriz de Pagos: (Estrategia_SkyJet, Estrategia_Oceanic) -> (Millones SkyJet, Millones Oceanic)
# Basado en el Dilema del Prisionero
matriz_competencia = {
    ('Precio_Premium',   'Precio_Premium'):   (50, 50), # Cooperación implícita
    ('Precio_Premium',   'Precio_Descuento'): (0, 80),  # SkyJet pierde mercado
    ('Precio_Descuento', 'Precio_Premium'):   (80, 0),  # SkyJet captura el mercado
    ('Precio_Descuento', 'Precio_Descuento'): (20, 20)  # Guerra de precios (Desgaste)
}

def motor_analisis_nash():
    print("--- INICIANDO ANALIZADOR DE EQUILIBRIO DE MERCADO ---")
    
    # Conjuntos para almacenar las mejores respuestas (BR)
    br_skyjet = set()
    br_oceanic = set()

    # 1. Analizando la perspectiva de SkyJet
    print("\n[Paso 1] Buscando Mejor Respuesta para SkyJet:")
    for est_o in estrategias:
        # Buscamos cuál de nuestras estrategias da más dinero contra la jugada est_o de Oceanic
        mejor_opcion = max(estrategias, key=lambda est_s: matriz_competencia[(est_s, est_o)][0])
        ganancia = matriz_competencia[(mejor_opcion, est_o)][0]
        
        br_skyjet.add((mejor_opcion, est_o))
        print(f"  > Si Oceanic elige {est_o}, SkyJet debe elegir {mejor_opcion} (+{ganancia}M)")

    # 2. Analizando la perspectiva de OceanicAir
    print("\n[Paso 2] Buscando Mejor Respuesta para OceanicAir:")
    for est_s in estrategias:
        # Buscamos cuál de nuestras estrategias da más dinero contra la jugada est_s de SkyJet
        mejor_opcion = max(estrategias, key=lambda est_o: matriz_competencia[(est_s, est_o)][1])
        ganancia = matriz_competencia[(est_s, mejor_opcion)][1]
        
        br_oceanic.add((est_s, mejor_opcion))
        print(f"  > Si SkyJet elige {est_s}, Oceanic debe elegir {mejor_opcion} (+{ganancia}M)")

    # 3. Identificar la intersección (Donde ambos coinciden en su mejor respuesta)
    equilibrios = br_skyjet.intersection(br_oceanic)
    return equilibrios

# --- EJECUCIÓN ---
puntos_de_equilibrio = motor_analisis_nash()

print("\n" + "="*60)
print(" VERDICTO DE LA TEORÍA DE JUEGOS ")
print("="*60)

if puntos_de_equilibrio:
    for eq in puntos_de_equilibrio:
        s1, s2 = eq
        p1, p2 = matriz_competencia[eq]
        print(f"[*] EQUILIBRIO DETECTADO: {s1} vs {s2}")
        print(f"    Resultado: Ambos ganan {p1}M y {p2}M respectivamente.")
        print(f"    Nota: Ninguno cambiará de táctica porque perdería dinero.")
else:
    print("[!] No hay equilibrio estable en estrategias puras.")