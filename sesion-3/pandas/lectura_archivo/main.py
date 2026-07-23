import pandas as pd

data = pd.read_csv("data_ventas_enero.csv")
print(data)

data_xlsx = pd.read_excel("data_ventas_enero_xlsx.xlsx")
print(data_xlsx)