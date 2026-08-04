import matplotlib.pyplot as plt

animales = ["Perros", "Gatos", "Aves", "Peces"]
cantidad = [45, 38, 12, 5]

plt.barh(animales, cantidad, color=["orange", "yellow", "green", "blue"])

plt.grid(True)
plt.legend(["Animales"])

plt.title("Veterinaria", fontsize=17)
plt.xlabel("Animales", fontsize=14)
plt.ylabel("Cantidad", fontsize=14)

# Mostrar valores en cada punto
for x, y in zip(animales, cantidad):
    # Argumento 1: Posición vertical
    # Argumento 2: Posición horizontal
    # Argumento 3: Texto o valor a mostrar
    # Argumento 4: Alineación horizontal
    plt.text(y, x, str(y), va="center")

plt.show()
