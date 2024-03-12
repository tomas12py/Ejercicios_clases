class Cuenta():
    def __init__(self,valor_agregar = 0,valor_retirar = 0,monto = 1000,saldo = 0,valor_actual = 0):
        self.saldo = saldo
        self.valor_agregar = valor_agregar
        self.valor_retirar = valor_retirar
        self.monto = monto
        self.valor_actual = valor_actual
        if self.saldo >= 0:
            self.saldo = self.saldo
        elif self.saldo < 0:
            self.saldo = 0
            print("Digite un saldo valido")
    def credit(self):
        self.valor_agregar = int(input("Digite el valor a agregar a la cuenta"))
        self.saldo = self.saldo + self.valor_agregar
        return self.valor_agregar
    def cargar(self):
        self.valor_retirar = int(input("Digite el valor a retirar"))
        if self.valor_retirar == self.monto:
            self.saldo = self.saldo
            return (f"El saldo a retirar excede el monto de dinero que se puede retirar")
        else:
            self.saldo = self.saldo - self.valor_retirar
            return self.valor_retirar
    def obtener_saldo(self):
            return self.saldo

Cuenta_2  = Cuenta()
print(f"El valor agregado a su cuenta es {Cuenta_2.credit()} el valor retirado es {Cuenta_2.cargar()} y su saldo actual es {Cuenta_2.obtener_saldo()}")