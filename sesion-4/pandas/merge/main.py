import pandas as pd

clientes = pd.read_csv("clientes.csv")
facturacion = pd.read_csv("facturacion.csv")

# unir tablas

df_final = pd.merge(
    facturacion,
    clientes,
    on="id_cliente",
    how="left"
)

print(df_final)