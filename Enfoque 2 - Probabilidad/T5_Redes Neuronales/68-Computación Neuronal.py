#Se basa en el principio de Procesamiento Distribuido en Paralelo (PDP): la información no se guarda 
# en un solo lugar, sino que reside en la fuerza de las conexiones (sinapsis) entre las neuronas.

# El Átomo de la Computación: El Perceptrón
# El modelo fundamental es el Perceptrón. Es una abstracción matemática de una neurona biológica que 
# recibe señales, las pondera y decide si "disparar" una señal de salida.Entradas ($x_i$): Los datos 
# que recibe.
# Pesos ($w_i$): La importancia que la red le da a cada dato (aquí es donde reside el 
# aprendizaje).
# Sesgo ($b$): El umbral de sensibilidad.
# Función de Activación: El "gatillo" que decide si la neurona se activa.

# =====================================================================
# COMPUTACIÓN NEURONAL: REGLA DE HEBB (MEMORIA ASOCIATIVA)
# =====================================================================

class NeuronaHebbiana:
    def __init__(self, num_entradas):
        # Empezamos con pesos en cero (mente vacía)
        self.pesos = [0.0] * num_entradas
        print("Neurona creada: Sin asociaciones previas.")

    def clasificar(self, entradas):
        # Suma ponderada (Potencial de membrana)
        suma = sum(x * w for x, w in zip(entradas, self.pesos))
        # Función de activación escalón ( bipolar: -1 o 1 )
        return 1 if suma >= 0 else -1

    def entrenar(self, entradas, salida_esperada):
        # Regla de Hebb: w_i = w_i + (x_i * y)
        # Si la entrada y la salida son iguales, el peso aumenta.
        for i in range(len(self.pesos)):
            self.pesos[i] += entradas[i] * salida_esperada

# --- SIMULACIÓN: Aprendiendo a reconocer un patrón ---
# Entradas: [Forma Circular, Color Rojo] (1 = Sí, -1 = No)
# Queremos que asocie [1, 1] con 'Manzana' (1)
manzana = [1, 1]
label_manzana = 1

brain = NeuronaHebbiana(2)

print("\n--- Fase de Entrenamiento ---")
for _ in range(3):
    brain.entrenar(manzana, label_manzana)
    print(f"Pesos actualizados: {brain.pesos}")

print("\n--- Fase de Prueba ---")
test = [1, 1]
resultado = brain.clasificar(test)
print(f"Entrada {test} -> Identificado como: {'Manzana' if resultado == 1 else 'Desconocido'}")