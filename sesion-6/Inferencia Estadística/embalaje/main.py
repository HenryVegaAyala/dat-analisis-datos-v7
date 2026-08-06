import pandas as pd
import scipy.stats as st

df = pd.read_csv("embalaje_puntaje.csv")

# Agrupar las 2 modalidades
embalaje_tradicional = df[df["embalaje"] == "A"]["puntuacion"] # Filtro avanzado por embalaje del tipo A
embalaje_ecologico = df[df["embalaje"] == "B"]["puntuacion"] # Filtro avanzado por embalaje del tipo B

# Realizamos el test A/B
resultado = st.ttest_ind(embalaje_tradicional, embalaje_ecologico)

# Mostrar resultados
print(f"Valor P: {resultado.pvalue:.4f}")

# Interpretacion
if resultado.pvalue < 0.05:
    print("Rechazamos la hipotesis nula, hay diferencia significativa entre los embalajes")
else:
    print("No hay diferencias significativas entre los embalajes. No rechazamos la hipotesis nula")