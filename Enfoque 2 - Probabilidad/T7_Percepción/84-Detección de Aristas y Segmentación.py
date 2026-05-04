#1. Detección de Aristas (Edge Detection)
# Una arista es una discontinuidad local en la intensidad de la imagen. Es el "esqueleto" de los 
# objetos.Detector de Canny: Es el algoritmo más popular. No solo detecta bordes, sino que los limpia 
# usando cuatro pasos:
# Reducción de ruido (Gaussiano).
# Cálculo de gradientes (¿Dónde cambia el brillo?).
# Supresión de no-máximos (Hace que los bordes sean 
# finos, de 1 píxel).
# Umbralización con histéresis (Conecta bordes débiles si están junto a uno fuerte).

# 2. Segmentación de Imágenes
# Segmentar es agrupar píxeles que pertenecen a la misma entidad. Es pasar de "píxeles sueltos" a 
# "regiones con significado".Umbralización (Thresholding): La forma más simple. Si el píxel es más 
# oscuro que $X$, es fondo; si es más claro, es objeto.

# Crecimiento de regiones (Region Growing): Empieza en un píxel "semilla" y se expande a los vecinos 
# si tienen un color similar.

# Segmentación Semántica: Usando Deep Learning, clasificamos cada píxel (ej: "este píxel es carretera", 
# "este es peatón").

# =====================================================================
# PERCEPCIÓN: SEGMENTACIÓN POR UMBRAL (THRESHOLDING)
# =====================================================================

# Imagen de 6x6 con un objeto brillante en el centro
imagen_gris = [
    [20, 22, 25, 20, 21, 20],
    [22, 85, 90, 88, 25, 22],
    [20, 92, 98, 95, 30, 20],
    [25, 88, 95, 85, 28, 21],
    [21, 25, 30, 22, 25, 20],
    [20, 20, 22, 21, 20, 25]
]

def segmentar(imagen, umbral):
    # Si el valor > umbral, ponemos 1 (Objeto), si no 0 (Fondo)
    return [[1 if pixel > umbral else 0 for pixel in fila] for fila in imagen]

# --- EJECUCIÓN ---
limite = 50
resultado = segmentar(imagen_gris, limite)

print(f"--- SEGMENTACIÓN (Umbral: {limite}) ---")
for fila in resultado:
    print(" ".join(["█" if p == 1 else "." for p in fila]))

# El resultado mostrará el "núcleo" brillante separado del fondo.