import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

clientes = pd.read_csv("clientes.csv")
ventas = pd.read_csv("ventas.csv")

consolidado = pd.merge(
    clientes,
    ventas,
    on="id_cliente",
    how="inner",
)

consolidado["total"] = consolidado["cantidad"] * consolidado["precio"]

resultado = consolidado[["pais", "total", "nivel"]]

agrupar = resultado.groupby(["pais", "nivel"])["total"].sum().reset_index()

print(agrupar)