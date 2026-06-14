"""
CETI Mecatrónica - Proyecto de Inteligencia Artificial
Demostración de Machine Learning: Regresión Lineal para Predicción de Precios
Librería Base: Scikit-Learn
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("--- INICIANDO SISTEMA DE MACHINE LEARNING ---")

# 1. GENERACIÓN DE DATOS SIMULADOS (Plusvalía de Terrenos / Antigüedad vs Precio)
# Imaginemos que medimos el tamaño del terreno (en metros cuadrados) y su precio final.
np.random.seed(42)
metros_cuadrados = np.random.rand(100, 1) * 150 + 50  # Terrenos entre 50 y 200 m2
# El precio depende del tamaño, más un factor de ruido aleatorio del mercado
precios = metros_cuadrados * 1200 + np.random.randn(100, 1) * 15000 + 30000

# Crear un DataFrame de Pandas (Estructura de datos vista en el tutorial)
df = pd.DataFrame(data=np.hstack((metros_cuadrados, precios)), columns=['Tamaño_m2', 'Precio_MXN'])

# 2. PREPARACIÓN DE LOS DATOS (Features 'X' y Labels 'y')
X = df[['Tamaño_m2']] # Características para predecir
y = df['Precio_MXN']  # Lo que queremos predecir


# Separar datos en Entrenamiento (80%) y Pruebas (20%) como dicta el tutorial
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. ENTRENAMIENTO DEL MODELO DE MACHINE LEARNING
print("-> Entrenando el modelo de Regresión Lineal en la CPU...")
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. EVALUACIÓN Y PRUEBA DEL EXPERIMENTO
eficiencia = modelo.score(X_test, y_test)
print(f"✅ ¡Entrenamiento Concluido! Precisión del modelo (R² Score): {eficiencia:.4f}")

# 5. GENERAR UNA PREDICCIÓN CON UN DATO NUEVO
terreno_nuevo = [[110]] # Queremos cotizar un terreno de 120 metros cuadrados
precio_predicho = modelo.predict(terreno_nuevo)
print(f"🔮 PREDICCIÓN: Un terreno de {terreno_nuevo} m² debería costar aproximadamente: ${precio_predicho[0]:,.2f} MXN")

# 6. GRÁFICA VISUAL (Para demostrar el experimento en tu video y documento)
plt.scatter(X_test, y_test, color='blue', label='Datos Reales de Prueba')
plt.plot(X_test, modelo.predict(X_test), color='red', linewidth=2, label='Línea de Predicción del Modelo')
plt.title('Machine Learning - Predicción de Bienes Raíces (CETI)')
plt.xlabel('Tamaño del Terreno (m²)')
plt.ylabel('Precio (MXN)')
plt.legend()
plt.grid(True)
print("-> Generando ventana gráfica del experimento...")
plt.show()