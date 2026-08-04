import matplotlib.pyplot as plt

edades = [18, 19, 21, 25, 26, 30, 34, 38, 40, 50]

plt.hist(edades, bins=5, color="skyblue", edgecolor="black")
plt.title("Histograma de edades", fontsize=14)

plt.show()