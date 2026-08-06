import pandas as pd
import scipy.stats as st
import numpy as np

#  1. Leer y cargar los datos en memoria
df = pd.read_csv("heladeria_gastos.csv")

datos_de_gasto = df["gasto"]

# 2. Calcular el intervalo de confianza al 95%
intervalo = st.t.interval(
    confidence=0.95, # porcentaje de intervalo de confianza
    df=len(datos_de_gasto) -1, # Ajuste de cantida de registros
    loc= np.mean(datos_de_gasto), # Media de los datos -> promedio
    scale=st.sem(datos_de_gasto), # error estandar de la media
)

print(f"El cliente en promedio gasta entre S/.{intervalo[0]:.2f} y S/.{intervalo[1]:.2f}")

# Punto medio
promedio = np.mean(intervalo)
print(f"EL promedio de gasto es: S/.{promedio:.2f}")

# Margenes de errores.
print(promedio - intervalo[0])
print(intervalo[1] - promedio)