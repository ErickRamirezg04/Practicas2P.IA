#1. La Red de Hopfield (Memoria Auto-asociativa)
#Es una red recurrente que funciona como una memoria direccionable por contenido. Si le das un patrón 
# borroso, la red "cae" en un estado de mínima energía que corresponde al recuerdo original.

#2. La Regla de Hebb (Aprendizaje Sináptico)
#Como vimos anteriormente: "Neurons that fire together, wire together". Es la base para entrenar los 
# pesos en Hopfield y otros modelos asociativos.

#3. Red de Hamming
#A diferencia de Hopfield, la red de Hamming es una red de clasificación. Mide la distancia de Hamming 
# (cuántos bits son diferentes) entre la entrada y los patrones almacenados para decidir cuál es el más 
# parecido.

#4. Máquina de Boltzmann
#Es la versión estocástica (con azar) de la red de Hopfield. Utiliza conceptos de termodinámica para 
# evitar quedarse atrapada en "mínimos locales" (recuerdos falsos), permitiendo que la red explore 
# mejores soluciones.

# =====================================================================
# MEMORIA ASOCIATIVA: MODELO SIMPLIFICADO (HEBB + HOPFIELD)
# =====================================================================

class RedAsociativa:
    def __init__(self, n_neuronas):
        self.n = n_neuronas
        # Matriz de pesos (Conexiones entre neuronas)
        self.W = [[0.0 for _ in range(n_neuronas)] for _ in range(n_neuronas)]

    def memorizar_hebb(self, patron):
        """Regla de Hebb: Fortalece conexiones entre neuronas activas juntas."""
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    self.W[i][j] += patron[i] * patron[j]

    def recuperar(self, entrada_ruidosa, iteraciones=2):
        """Proceso tipo Hopfield: Converger al recuerdo más cercano."""
        estado = list(entrada_ruidosa)
        for _ in range(iteraciones):
            for i in range(self.n):
                # Suma ponderada de influencias de otras neuronas
                activacion = sum(self.W[i][j] * estado[j] for j in range(self.n))
                estado[i] = 1 if activacion >= 0 else -1
        return estado

# --- SIMULACIÓN ---
# Patrón: Una cara muy simple 3x1 (OJO, NARIZ, BOCA) -> [1, -1, 1]
patron_original = [1, -1, 1] 

memoria = RedAsociativa(3)
memoria.memorizar_hebb(patron_original)

# Entrada dañada: El ojo está cerrado/ruidoso [-1, -1, 1]
ruido = [-1, -1, 1]
recuerdo = memoria.recuperar(ruido)

print(f"Patrón Original: {patron_original}")
print(f"Entrada Ruidosa: {ruido}")
print(f"Recuerdo Recuperado: {recuerdo}")