#1. El Perceptrón (1958)
#Es el abuelo de las redes neuronales. Utiliza una función de activación de paso (escalón). Su 
# aprendizaje es binario: si se equivoca, ajusta los pesos; si acierta, no hace nada. Solo funciona 
# si los datos se pueden separar con una línea recta perfecta.

#2. ADALINE (Adaptive Linear Neuron)
#La evolución lógica. A diferencia del Perceptrón, ADALINE utiliza una función de activación lineal 
# durante el entrenamiento. Esto permite usar el Descenso de Gradiente, minimizando el error 
# cuadrático. Es mucho más estable porque aprende "qué tan lejos" estuvo de la respuesta correcta, 
# no solo si falló.

#3. MADALINE (Many ADALINES)
#Como su nombre indica, es una arquitectura de múltiples ADALINEs conectadas. Es la primera red 
# neuronal multicapa. Al combinar varios ADALINEs, MADALINE puede resolver problemas que no son 
# linealmente separables (como la compuerta XOR).

# =====================================================================
# EVOLUCIÓN NEURONAL: PERCEPTRÓN vs ADALINE
# =====================================================================

class NeuronaEvolutiva:
    def __init__(self, n_entradas, tipo="Perceptron"):
        self.w = [0.0] * (n_entradas + 1) # Pesos + Bias
        self.tipo = tipo
        self.tasa = 0.1

    def activacion_lineal(self, x):
        # Suma ponderada: z = sum(w*x) + b
        return sum(xi * wi for xi, wi in zip(x, self.w[:-1])) + self.w[-1]

    def predecir(self, x):
        # Función Escalón: Salida binaria -1 o 1
        return 1 if self.activacion_lineal(x) >= 0 else -1

    def entrenar(self, x, objetivo):
        prediccion = self.predecir(x)
        z = self.activacion_lineal(x)
        
        if self.tipo == "Perceptron":
            # Regla del Perceptrón: Solo actúa si hay error
            error = objetivo - prediccion
            for i in range(len(x)):
                self.w[i] += self.tasa * error * x[i]
            self.w[-1] += self.tasa * error
            
        else: # ADALINE
            # Regla Delta: Aprende del error continuo (z), no solo de la clase
            error = objetivo - z
            for i in range(len(x)):
                self.w[i] += self.tasa * error * x[i]
            self.w[-1] += self.tasa * error
        return error**2

# --- DATOS: [Acidez, Cuerpo] -> Clase (1: Premium, -1: Estándar) ---
datos = [[1, 1], [2, 1], [0, 0], [1, 0]]
labels = [1, 1, -1, -1]

# Ejecución
p = NeuronaEvolutiva(2, "Perceptron")
a = NeuronaEvolutiva(2, "ADALINE")

print(f"{'Modelo':<12} | {'Error Final':<15}")
print("-" * 30)

for _ in range(100): # 100 Épocas
    error_p = sum(p.entrenar(xi, yi) for xi, yi in zip(datos, labels))
    error_a = sum(a.entrenar(xi, yi) for xi, yi in zip(datos, labels))

print(f"{'Perceptrón':<12} | {error_p:<15.4f}")
print(f"{'ADALINE':<12} | {error_a:<15.4f}")