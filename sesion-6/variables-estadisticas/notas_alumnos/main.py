import pandas as pd

df = pd.read_csv("notas_alumnos.csv")

media = df["notas"].mean()
mediana = df["notas"].median()

print(f"El valor de media: {media}")
print(f"El valor de mediana: {mediana}")