#La Separabilidad Lineal es el concepto geométrico fundamental que dictó el éxito y el fracaso de la 
# inteligencia artificial durante décadas. Es la prueba de fuego para cualquier modelo de clasificación 
# simple como el Perceptrón.

#Un conjunto de datos es linealmente separable si existe un hiperplano (una línea en 2D, un plano en 3
# D) capaz de dividir perfectamente las clases sin cometer un solo error.

# =====================================================================
# TEST DE SEPARABILIDAD LINEAL: AND vs XOR
# =====================================================================

def perceptron_test(datos, etiquetas, nombre):
    w = [0.0, 0.0] # Pesos
    b = 0.0        # Bias
    tasa = 0.1
    
    # Intentamos entrenar por 50 épocas
    for _ in range(50):
        for x, y in zip(datos, etiquetas):
            # Predicción: paso(w*x + b)
            z = x[0]*w[0] + x[1]*w[1] + b
            pred = 1 if z >= 0 else 0
            
            # Regla de aprendizaje
            error = y - pred
            w[0] += tasa * error * x[0]
            w[1] += tasa * error * x[1]
            b += tasa * error

    # Verificación final
    aciertos = 0
    for x, y in zip(datos, etiquetas):
        z = x[0]*w[0] + x[1]*w[1] + b
        pred = 1 if z >= 0 else 0
        if pred == y: aciertos += 1
    
    print(f"Problema {nombre}: {aciertos}/{len(etiquetas)} aciertos.")
    return aciertos == len(etiquetas)

# --- DATOS ---
# AND: Linealmente Separable
entradas_and = [[0,0], [0,1], [1,0], [1,1]]
salidas_and = [0, 0, 0, 1]

# XOR: NO Linealmente Separable
entradas_xor = [[0,0], [0,1], [1,0], [1,1]]
salidas_xor = [0, 1, 1, 0]

print("--- RESULTADOS DE SEPARABILIDAD ---")
res_and = perceptron_test(entradas_and, salidas_and, "AND")
res_xor = perceptron_test(entradas_xor, salidas_xor, "XOR")

if not res_xor:
    print("\nConclusión: XOR requiere capas ocultas o Kernels porque no es linealmente separable.")