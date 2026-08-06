import pandas as pd

df = pd.read_csv("tienda_de_mascotas.csv")

categoria = df["categoria"]
precio = df["precio"]

moda = categoria.mode()
promedio = precio.mean()

print(moda)

print(f"La moda de la categoría es: {moda[0]}")
print(f"El promedio del precio es: {promedio}")