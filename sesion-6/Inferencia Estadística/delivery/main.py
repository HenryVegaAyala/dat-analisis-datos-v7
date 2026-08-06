import pprint

import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv("tiempos_de_entrega_delivery.csv")

# Paso 1: Filtrado de datos en grupos
vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]

# Paso 2: Calculo de la desviación estandar para vehiculos tradicionales
promedio_tradicional = np.mean(vehiculo_tradicional)

ic_tradicional = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_tradicional) - 1,
    loc=promedio_tradicional,
    scale=st.sem(vehiculo_tradicional)
)

print(f"Rangos del intervalo de confianza con vehiculo tradicional")
print(f"Rango del vehiculo tradiconal {ic_tradicional[0]:.2f} y {ic_tradicional[1]:.2f}")
print(f"Promedio del vehiculo tradicional {np.mean(ic_tradicional):.2f}")

print("--" * 100)

promedio_electrico = np.mean(vehiculo_electrico)

ic_electrico = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_electrico) - 1,
    loc=promedio_electrico,
    scale=st.sem(vehiculo_electrico)
)

print(f"Rangos del intervalo de confianza con vehiculo electrico")
print(f"Rango del vehiculo electrico {ic_electrico[0]:.2f} y {ic_electrico[1]:.2f}")
print(f"Promedio del vehiculo electrico {np.mean(ic_electrico):.2f}")

print("--" * 100)

# Paso 3: Pruebas Test A/B
resultado = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)
print(f"Valor P: {resultado.pvalue:.4f}")

# Paso 4: Interpretación del resultado
if resultado.pvalue < 0.05:
    print("Existe una diferencia significativa entre ambos vehiculos")
else:
    print("No existe una diferencia significativa entre ambos vehiculos")