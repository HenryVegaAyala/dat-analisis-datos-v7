import matplotlib.pyplot as plt

# Crear una figurar con 4 espacios para gráficos
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# titulo general de toda la figura
fig.suptitle("Ejemplo de visualización de datos con matplotlib", fontsize=14)

# Grafico de lineas
meses = ["Enero", "Febrero", "Marzo", "Abril"]
ventas_mensuales = [1000, 2000, 3000, 5000]

axs[0, 0].plot(meses, ventas_mensuales, label="Mensual", marker="o")
axs[0, 0].set_title("Mensual", fontsize=14)
axs[0, 0].set_xlabel("Mes")
axs[0, 0].set_ylabel("Ventas")

# Grafico de barras
meses = ["Enero", "Febrero", "Marzo", "Abril"]
ventas_mensuales = [1000, 2000, 3000, 5000]

axs[0, 1].bar(meses, ventas_mensuales, label="Mensual")
axs[0, 1].set_title("Mensual", fontsize=14)
axs[0, 1].set_xlabel("Mes")
axs[0, 1].set_ylabel("Ventas")

fig.show()
# fig.savefig(
#     "Histograma de ventas.png",
#     bbox_inches="tight", )