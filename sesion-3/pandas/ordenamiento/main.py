import pandas as pd

df = pd.read_csv("data_ventas_enero.csv")

resultado = df.sort_values("producto")
print(resultado)

print("*" * 100)

resultado = df.sort_values("vendedor", ascending=False)
print(resultado)

print("*" * 100)

resultado = df.sort_values(["cantidad", "vendedor"], ascending=[False, True])
print(resultado)