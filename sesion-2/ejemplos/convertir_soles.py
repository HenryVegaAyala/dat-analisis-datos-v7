def convertir_a_soles(monto):
    tipo_de_cambio = 3.8
    conversion = monto * tipo_de_cambio
    return conversion

resultado = convertir_a_soles(100)
print(f"El resultado de la conversión es: {resultado} soles")