import numpy as np

temperaturas = [22, 21, 23, 90, 22, 20, 105, 21]
temperaturas_array = np.array(temperaturas)

# Filtrado de temperaturas con error
encontrar_error =  temperaturas_array > 50

resultado = temperaturas_array[encontrar_error]
print(f"Temperaturas con error: {resultado}")

cantidad_errores = len(resultado)
print(f"Cantidad de errores: {cantidad_errores}")