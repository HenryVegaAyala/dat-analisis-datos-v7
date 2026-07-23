import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

filtro_por_cantidad = df["cantidad"] >= 5
filtro_por_precio_unitario = df["precio_unitario"] <= 100

resultado = df[(filtro_por_cantidad) & (filtro_por_precio_unitario)]
print(resultado)