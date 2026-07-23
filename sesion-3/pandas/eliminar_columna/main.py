import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

df.drop([0, 4], axis=0, inplace=True)
df.drop(["vendedor", "id_venta"], axis=1, inplace=True)

resultado = df["producto"] != "Mouse"
print(df[resultado])
