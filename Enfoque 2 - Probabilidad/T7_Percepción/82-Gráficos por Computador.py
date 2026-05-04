#1. El Pipeline Gráfico (La línea de montaje)
#Para que una idea matemática se convierta en un píxel en tu pantalla, debe pasar por una serie de 
# etapas. Este proceso es lo que permite que los videojuegos y las películas en 3D se vean tan reales.

#Modelado: Definir la forma de los objetos mediante vértices, aristas y caras (polígonos).

#Transformación: Ubicar los objetos en un espacio 3D (rotar, escalar, mover).

#Iluminación: Calcular cómo interactúa la luz con las superficies.

#Rasterización: El paso crítico donde los objetos 3D se convierten en una rejilla de píxeles 2D.

#2. Rasterización vs. Ray Tracing (Trazado de Rayos)
#Existen dos filosofías principales para dibujar imágenes:

#Rasterización: Es rápida (usada en videojuegos). Dibuja los objetos polígono por polígono. Es 
# eficiente pero le cuesta manejar reflejos y sombras complejas.

#Ray Tracing: Es realista (usada en cine). Simula el camino físico de los rayos de luz desde la cámara 
# hasta los objetos. Calcula rebotes, refracciones en cristal y sombras suaves.

# =====================================================================
# GRÁFICOS POR COMPUTADOR: RASTERIZADOR BÁSICO
# =====================================================================

def crear_lienzo(ancho, alto):
    # Creamos una "pantalla" vacía (espacios)
    return [[" " for _ in range(ancho)] for _ in range(alto)]

def dibujar_rectangulo(lienzo, x, y, w, h, caracter="#"):
    """Dibuja un rectángulo rellenando la rejilla de píxeles."""
    alto_l = len(lienzo)
    ancho_l = len(lienzo[0])
    
    for fila in range(y, y + h):
        for col in range(x, x + w):
            if 0 <= fila < alto_l and 0 <= col < ancho_l:
                lienzo[fila][col] = caracter

def mostrar_pantalla(lienzo):
    print("+" + "-" * len(lienzo[0]) + "+")
    for fila in lienzo:
        print("|" + "".join(fila) + "|")
    print("+" + "-" * len(lienzo[0]) + "+")

# --- EJECUCIÓN ---
ancho, alto = 40, 15
pantalla = crear_lienzo(ancho, alto)

# Dibujamos "objetos" en nuestro espacio
dibujar_rectangulo(pantalla, 5, 2, 10, 5, "X")  # Un cuadrado
dibujar_rectangulo(pantalla, 20, 5, 15, 8, "O") # Un rectángulo largo

print("RENDERIZADO FINAL:")
mostrar_pantalla(pantalla)