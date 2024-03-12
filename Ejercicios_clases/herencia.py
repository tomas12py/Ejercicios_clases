class persona():
    def __init__(self,nombre = "",edad = 0):
        self.nombre = input("Digite su nombre")
        self.edad = int(input("Digite su edad"))
    def datos(self):
        return f"el nombre del empleado es{self.nombre} y la edad del empleado es {self.edad}"

class empleado(persona):
    def __init__(self,nombre = "",edad = 0,sueldo = 0):
        self.sueldo = sueldo
        super().__init__(nombre, edad)
    def impuestos(self):
        self.sueldo = int(input("Digite su sueldo"))
        if self.sueldo > 3000000:
            return f"pagas impuestos"
        else:
            return f"no pagas impuestos"
    
persona_1 = empleado()
print(f"Estos son los datos de la persona {persona_1.datos()} y el estado de impuestos de la persona es {persona_1.impuestos()}")