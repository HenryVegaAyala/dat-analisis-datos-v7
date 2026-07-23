import pandas as pd

data = pd.read_csv("data_ventas_enero.csv")
print(data)

print("*" * 60)

data_xlsx = pd.read_excel("data_ventas_enero_xlsx.xlsx")
print(data_xlsx)

print("*" * 60)

data_hoja1 = pd.read_excel("data_ventas_enero_xlsx.xlsx", sheet_name="Hoja1")
print(data_hoja1)
