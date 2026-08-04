import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
from openpyxl.chart import marker

semanas = [1, 2, 3, 4]
kilometros = [2, 5, 4, 8]

# Tamaño de la figura
plt.figure(figsize=(8, 6))

plt.plot(
    semanas,
    kilometros,
    color="green",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8
)
plt.title("Progreso de Juan", fontsize=17)
plt.xlabel("Semanas", fontsize=14)
plt.ylabel("Kilometros recorridos", fontsize=14)

# Cuadricula
plt.grid(True, linestyle="--", alpha=0.6)

# Leyenda
plt.legend(["Semanas"])

# Mostrar valores en cada punto
for x, y in zip(semanas, kilometros):
    # Argumento 1: Posición horizontal
    # Argumento 2: Posición vertical
    # Argumento 3: Texto o valor a mostrar
    # Argumento 4: Alineación horizontal
    plt.text(x, y + .15, str(y), ha="center")

# Se encarga de encajar el contenido en la figura
plt.tight_layout()

plt.show()
