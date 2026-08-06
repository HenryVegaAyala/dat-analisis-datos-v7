import pandas as pd

df = pd.read_csv("venta_casas.csv")

cantidad_nulos = df["precios"].isnull().sum()

print(f"Cantida de registros nullos {cantidad_nulos}")

descripcion = df.describe()

print(descripcion)