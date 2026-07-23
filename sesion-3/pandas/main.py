import pandas as pd

datos = {
    "nombres": ["Pepito", "Juan", "Maria", "Ana"],
    "edades": [15, 18, 16, 17]
}

resultado = pd.DataFrame(datos)
print(resultado)
