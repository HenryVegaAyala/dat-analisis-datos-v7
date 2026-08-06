import pandas as pd

edades = [10, 12, 10, 11, None, 85, 11]

df = pd.Series(edades)

# calcular la media de las edades, aplicando el filtro
median = df.median()

print(f"El valor de la mediana es {median}")

# reemplazar valores nan
edades_corregidas = df.fillna(median)

resultado_final = edades_corregidas[edades_corregidas <= 18]

print(resultado_final)
