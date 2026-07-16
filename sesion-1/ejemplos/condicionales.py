# if: "si pasa esto..."
# elseif: "si no paso lo anterior, prueba esto..."
# else: "Si nada cumple"

# If else
edad = 15
if edad >= 18:
    print("El edad es mayor a 18")
else:
    print("El edad es menor a 18")

# If elseif else
nota = 15
if nota >= 18: # primera condición
    print("Nota excelente")
elif nota >= 14: # segunda condición
    print("Nota buena")
else: # ninguna se cumple las condiciones.
    print("Nota insuficiente")