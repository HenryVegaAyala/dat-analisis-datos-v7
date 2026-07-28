import pandas as pd
import glob

# Buscar todos los registros en csv automaticamente
buscar_archivos = glob.glob("data/ventas_*.csv")

print(f"Cantidad de archivos encontrados {len(buscar_archivos)}")

dataframes = [] # Variable global

# Leer y concatenar todos los archivos encontrados
for archivo in buscar_archivos:
    df = pd.read_csv(archivo)
    dataframes.append(df)

consolidado = pd.concat(dataframes, ignore_index=True)

consolidado.to_csv("resultado/consolidado.csv", index=False)