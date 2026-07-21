# 1. Crear una lista de productos: Ejemplo de una lista de cadenas
panaderia = ["pan", "croissant", "baguette", "donut", "muffin"]
print(panaderia)

# 2. Ejemplo de una lista de números: Ventas por hora
ventas_hora = [10, 20, 15, 30]
print(ventas_hora)

# 3. Ejemplo de valores mixtos
valores_mixtos = [10, 20, 20.50, "Hola", True]
print(valores_mixtos)

# 4. Acceder a un elemento de una lista basada en indice
primer_elemento = panaderia[3]
print(f"Primer producto de la lista: {primer_elemento}")

# 5. Acceder al último elemento de una lista
ultimo_elemento = panaderia[-1]
print(f"Último producto de la lista: {ultimo_elemento}")

# 6. Agregar un nuevo producto a la lista
panaderia.append("aceite")
print(f"Lista de productos y agregados: {panaderia}")

# 7. Cambiar o actualizar producto de la lista
panaderia[5] = "aceite de oliva"
print(f"Lista de productos y actualizados: {panaderia}")

# 8. Eliminar un producto de la lista
panaderia.remove("baguette")
print(f"Lista de productos y eliminados: {panaderia}")

# 9. Eliminar un producto basado en el índice de una lista
del panaderia[2]
print(f"Lista de productos y eliminados por índice: {panaderia}")

# 10. Obtener la cantidad de registros de una lista
total_de_elementos = len(panaderia)
print(f"Total de productos en la lista: {total_de_elementos}")