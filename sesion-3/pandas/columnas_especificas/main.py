import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

# print(df.head(2))

columnas_a_mostrar = df[["producto", "precio_unitario", "cantidad"]]

print(columnas_a_mostrar)