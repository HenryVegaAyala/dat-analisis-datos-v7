class Cliente:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo_inicial = saldo_inicial

    def comprar(self, monto):
        if self.saldo_inicial >= monto:
            self.saldo_inicial = self.saldo_inicial - monto
            print(f"{self.nombre} ha comprado por {monto}. Saldo restante: {self.saldo_inicial}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para comprar por {monto}. Saldo actual: {self.saldo_inicial}")


# Instanciar la clase
c1 = Cliente("Juan", 1200)
c1.comprar(500) # Se ha comprado un celular
c1.comprar(700) # Se ha comprado una laptop
c1.comprar(100) # Se ha comprado un case