import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

filtro_por_cantidad = df["cantidad"] >= 10

resultado = df[filtro_por_cantidad]

print(resultado)