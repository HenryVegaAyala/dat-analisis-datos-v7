import matplotlib.pyplot as plt

horas_dia = [1, 2, 3, 4]
cantidad = [10, 20, 25, 30]

# Tamaño de la figura
plt.figure(figsize=(8, 5))

plt.plot(horas_dia, cantidad)
plt.title("Ventas de la cafeteria")
plt.xlabel("Horas del dia")
plt.ylabel("Cantidad de café vendido")

# Cuadricula
plt.grid(True, linestyle="--", alpha=0.6)

# Leyenda
plt.legend(["Horas del dia"])

# Mostrar valores en cada punto
for x, y in zip(horas_dia, cantidad):
    # Argumento 1: Posición horizontal
    # Argumento 2: Posición vertical
    # Argumento 3: Texto o valor a mostrar
    # Argumento 4: Alineación horizontal
    plt.text(x, y + 1, str(y), ha="center")

# Se encarga de encajar el contenido en la figura
plt.tight_layout()

plt.show()