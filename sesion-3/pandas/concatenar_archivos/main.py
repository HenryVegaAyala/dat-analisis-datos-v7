import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

enero = pd.read_csv("ventas_enero_2026.csv")
febrero = pd.read_csv("ventas_febrero_2026.csv")
marzo = pd.read_csv("ventas_marzo_2026.csv")

consolidado = pd.concat([enero, febrero, marzo])
print(consolidado)

