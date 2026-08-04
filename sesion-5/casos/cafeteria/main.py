import matplotlib.pyplot as plt

horas_dia = [1, 2, 3, 4]
cantidad = [10, 20, 25, 30]

plt.plot(horas_dia, cantidad)
plt.title("Ventas de la cafeteria")
plt.xlabel("Horas del dia")
plt.ylabel("Cantidad de café vendido")

plt.show()