import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

df.rename(columns={"id_venta": "codigo_venta"}, inplace=True)

print(df)