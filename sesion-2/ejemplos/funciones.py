def saludar_analista(nombre, apellido):
    mensaje = f"Hola soy {nombre} {apellido}, un gusto en saludarte."
    return mensaje

saludo = saludar_analista("Juan", "Perez")
print(saludo)

saludo_2 = saludar_analista("Pepito", "Perez")
print(saludo_2)