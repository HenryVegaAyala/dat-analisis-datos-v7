import pandas as pd

data = pd.read_csv("facturacion.csv")

data["id_cliente"] = data["id_cliente"].fillna("Desconocido")
print(data)

data_sin_nan = data.dropna()
print(data_sin_nan)

data_corregida_duplicados = data.drop_duplicates()
print(data_corregida_duplicados)

data_corregida_duplicados = data.drop_duplicates(subset=["id_factura", "id_cliente"])
print(data_corregida_duplicados)