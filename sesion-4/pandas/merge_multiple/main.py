import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

clientes = pd.read_csv("clientes.csv")
ventas = pd.read_csv("ventas.csv")
productos = pd.read_csv("productos.csv")

# Ejemplo con inner
resultado_inner = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="inner"
)
print(resultado_inner)
print("-" * 100)

resultado_left = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="left"
)
print(resultado_left)
print("-" * 100)

# Ejemplo con right
resultado_right = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="right"
)
print(resultado_right)
print("-" * 100)

# Ejemplo con outer
resultado_outer = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="outer"
)
print(resultado_outer)
print("-" * 100)

# Relación de 3 datasets
data_ventas_clientes = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="left"
)

data_ventas_clientes_productos = pd.merge(
    data_ventas_clientes,
    productos,
    on="id_producto",
    how="right"
)

print(data_ventas_clientes_productos)
