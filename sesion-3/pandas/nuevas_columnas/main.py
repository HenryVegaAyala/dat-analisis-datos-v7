import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

df["total"] = df["cantidad"] * df["precio_unitario"]

df.to_csv("data_ventas_enero_v2.csv", index=False)