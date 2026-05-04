#1. ¿Cómo funciona un Filtro? 
# (La Convolución)Imagina una pequeña matriz de números llamada Kernel o Máscara (por ejemplo, de $3 
# \times 3$). Deslizamos esta máscara sobre cada píxel de la imagen original. El nuevo valor del píxel 
# es el resultado de multiplicar los números de la máscara por los valores de los píxeles vecinos y 
# sumarlos.

# 2. Tipos de Filtros Fundamentales

# Filtros de Suavizado (Smoothing): Como el Filtro Gaussiano o de Media. Borran el ruido "difuminando" 
# la imagen. Son los que usa tu teléfono en el "modo belleza" para suavizar la piel.

# Filtros de Realce (Edge Detection): Como los filtros Sobel o Prewitt. Resaltan los cambios bruscos 
# de intensidad (bordes). Son vitales para que un coche autónomo detecte las líneas del carril.

# Filtros de Ruido Sal y Pimienta: Filtros como el de Mediana, que son excelentes para eliminar 
# píxeles blancos o negros aislados sin perder nitidez en los bordes.

# =====================================================================
# PREPROCESADO: FILTRO DE CONVOLUCIÓN (SOBEL VERTICAL)
# =====================================================================

# Una "imagen" simple de 5x5 (una pared oscura a la izquierda, clara a la derecha)
imagen = [
    [10, 10, 90, 90, 90],
    [10, 10, 90, 90, 90],
    [10, 10, 90, 90, 90],
    [10, 10, 90, 90, 90],
    [10, 10, 90, 90, 90]
]

# Kernel Sobel Vertical: Resalta cambios de izquierda a derecha
# Los negativos a la izquierda y positivos a la derecha detectan la diferencia
kernel = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

def aplicar_filtro(img, kern):
    res = [[0]*3 for _ in range(3)] # Salida más pequeña por los bordes
    for i in range(1, 4):
        for j in range(1, 4):
            # Operación de Convolución
            suma = 0
            for ki in range(3):
                for kj in range(3):
                    suma += img[i-1+ki][j-1+kj] * kern[ki][kj]
            res[i-1][j-1] = suma
    return res

# --- EJECUCIÓN ---
resultado = aplicar_filtro(imagen, kernel)

print("--- IMAGEN FILTRADA (Bordes Verticales) ---")
for fila in resultado:
    print([val for val in fila])

# Nota: Los valores altos (320) indican que se encontró un borde muy claro en el centro.