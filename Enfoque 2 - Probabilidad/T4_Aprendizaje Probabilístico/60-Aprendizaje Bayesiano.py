#¿Qué es el Aprendizaje Bayesiano (Beta-Bernoulli)?
# En el aprendizaje clásico, calculas un promedio y listo. En el Aprendizaje Bayesiano, tratas la 
# probabilidad como una variable viva que tiene su propia distribución.
# Prior (Beta): Es lo que crees antes de ver los datos. Un $\alpha=1, \beta=1$ (Distribución Uniforme) 
# significa que no tienes ni idea y que cualquier probabilidad es posible.
# Likelihood (Bernoulli): Es el evento binario (clic/no clic, éxito/fracaso).
# Posterior: Es tu nueva creencia después de ver el dato. La magia de la distribución Beta es que 
# es el conjugado previo de la Bernoulli: para aprender, solo tienes que sumar los éxitos a $\alpha$ 
# y los fracasos a $\beta$.

# =====================================================================
# APRENDIZAJE BAYESIANO: ESTIMACIÓN DE TASA DE ÉXITO
# =====================================================================

def simulacion_aprendizaje():
    # 1. ESTADO INICIAL (Prior)
    # Alpha=1, Beta=1 representa una mente "en blanco" (distribución plana)
    a = 1
    b = 1

    # Datos que llegan en tiempo real: 1 (Usuario compró), 0 (Usuario salió)
    flujo_datos = [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]

    print(f"{'Dato':<8} | {'Éxitos (α)':<12} | {'Fallos (β)':<12} | {'Confianza (Media)':<10}")
    print("-" * 60)

    for i, dato in enumerate(flujo_datos):
        # ACTUALIZACIÓN BAYESIANA: El aprendizaje más simple del mundo
        if dato == 1:
            a += 1  # Reforzamos la creencia de éxito
        else:
            b += 1  # Reforzamos la creencia de fracaso

        # La media de la distribución Beta es α / (α + β)
        # Representa nuestra mejor estimación de la probabilidad real
        probabilidad_estimada = a / (a + b)

        # La varianza (incertidumbre) disminuye a medida que α + β crece
        print(f"{i+1:<8} | {a:<12} | {b:<12} | {probabilidad_estimada:<10.4f}")

# --- Ejecución ---
simulacion_aprendizaje()