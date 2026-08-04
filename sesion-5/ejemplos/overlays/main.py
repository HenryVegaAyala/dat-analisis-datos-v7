import matplotlib.pyplot as plt
from openpyxl.chart import marker

# datos del mes
mes = ["Enero", "Febrero", "Marzo", "Abril"]

# Gastos mensuales de cada servicio en soles
luz = [40, 50, 56, 60]
agua = [25, 30, 31, 35]

# Crear gráfico de gastos de luz
plt.plot(
    mes,
    luz,
    label="servicios de luz",
    marker="o",
    linewidth=3,
    color="blue",
)

# Crear gráfico de gastos de agua
plt.plot(
    mes,
    agua,
    label="servicios de agua",
    marker="s",
    linewidth=3,
    color="red",
)

# Títulos y nombres de los ejes
plt.title("Gastos de la casa", fontsize=14)
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Gastos S/.", fontsize=12)

# Cuadricula
plt.grid(True, linestyle="-", linewidth=0.3, color="black")

# Leyenda
plt.legend()

# mostrar valores encima de cada punto
for index, valor in enumerate(luz):
    plt.text(
        mes[index], # El indice se colocar en cada mes
        valor + 1,
        str(valor),
        ha="center",
    )

# mostrar valores encima de cada punto
for index, valor in enumerate(agua):
    plt.text(
        mes[index], # El indice se colocar en cada mes
        valor + 1,
        str(valor),
        ha="center",
    )

# plt.show()
plt.savefig("consolidado_gastos.png")