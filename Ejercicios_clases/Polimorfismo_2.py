"""
Se pretende desarrollar un conjunto de clases que representen, de forma simplificada, a una 
hipotética empresa dedicada a vender un producto. A continuación, se describen las 
características básicas de estas clases:
1. Empleado. Clase básica que describe a un empleado. Incluye sus datos personales (nombre, 
apellidos, DNI, dirección) y algunos datos tales como los años de antigüedad, teléfono de contacto 
y su salario. Incluye también información de quién es el empleado que lo supervisa (Empleado *). 
Tendrá, al menos, las siguientes funciones miembro: • Constructores para definir correctamente 
un empleado, a partir de su nombre, apellidos, DNI, dirección, teléfono y salario. • Imprimir (A 
través de los operadores de E/S redefinidos) • Cambiar supervisor • Incrementar salario 
2. secretario. Tiene despacho, número de fax e incrementa su salario un 5% anual. Tendrá, al 
menos, las siguientes funciones miembro: • Constructores (debe rellenar la información personal 
y los datos principales) • Imprimir (debe imprimir sus datos personales y su puesto en la empresa). 
3. Vendedor. Tiene coche de la empresa (identificado por la matricula, marca y modelo), teléfono 
móvil, área de venta, lista de clientes y porcentaje que se lleva de las ventas en concepto de 
comisiones. Incrementa su salario un 10% anual. Tendrá, al menos, las siguientes funciones 
miembro: • Constructores (debe rellenar la información personal y los datos principales) • 
Imprimir (debe imprimir sus datos personales y su puesto en la empresa). • Dar de alta un nuevo 
cliente. • Dar de baja un cliente. • Cambiar de coche. 
4. Jefe de zona. Tiene despacho, tiene un secretario a su cargo, una lista de vendedores a su cargo 
y tiene coche de la empresa (identificado por la matrícula, marca y modelo). Incrementa su salario 
un 20% anual. Tendrá, al menos, las siguientes funciones miembro: • Constructores (debe rellenar 
la información personal y los datos principales) • Imprimir (debe imprimir sus datos personales y 
su puesto en la empresa). • Cambiar de secretario. • Cambiar de coche. • Dar de alta y de baja un 
nuevo vendedor en su zona. Todos los empleados son vendedores, jefes de zona o secretarios. 
Hacer un programa de prueba que muestre cómo funciona. Probar, especialmente, que el método 
incrementar salario se comparta bien, según el empleado

"""

class Empleado():
    def __init__(self,nombre = "",apellidos = "",dni = 0,direccion = "",antiguedad = 0,telefono = 0,salario = 0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.telefono = telefono
        self.salario = salario
    def informacion(self):
        self.nombre = input("Digite su nombre")
        self.apellidos = input("Digite sus apellidos")
        self.dni = int(input("Digite su dni"))
        self.direccion = input("Digite su direccion")
        self.antiguedad = int(input("Digite sus años de antiguedad"))
        self.telefono = int(input("Digite su numero de telefono"))
        self.salario = float(input("Digite su salario"))
        return f"El nombre del empleado es {self.nombre}\nsus apellido son {self.apellidos}\nsu dni es {self.direccion}\nsu direccion es {self.direccion}\nsu antiguedad es {self.antiguedad}\nsu telefono es {self.telefono}\ny su salario es {self.salario}"
    def cambiar_supervisor(self):
        print("El supervisor a cambiado digite la informacion del nuevo supervisor")
        return f"{self.informacion()}"
    def incrementar_salario(self):
        porcentaje = 50/self.salario*100
        self.salario = self.salario + porcentaje
        return f"su salario con el incremento es de {self.salario}"
class Secretario():
    def __init__(self,despacho = "Despacho en uso",numero_fax = 0):
        self.despacho = despacho
        self.numero_fax = numero_fax
    def informacion(self):
        self.nombre = input("Digite su nombre")
        self.apellidos = input("Digite sus apellidos")
        self.dni = int(input("Digite su dni"))
        self.direccion = input("Digite su direccion")
        self.antiguedad = int(input("Digite sus años de antiguedad"))
        self.telefono = int(input("Digite su numero de telefono"))
        self.salario = float(input("Digite su salario"))
        self.despacho = input("Digite el estado de su despacho")
        self.numero_fax = int(input("Digite el numero de fax"))
        i = 0
        for i in range(1,11):
            if self.antiguedad > i:
                i += 1
            elif self.antiguedad == i:
                porcentaje = 5/self.salario*100
                self.salario = self.salario + porcentaje * i
                return "Se a aplicado el porcentaje anual"
            else:
                return "Digite un valor correcto"

        return "La informacion fue ingresada correctamente"
    def mostrar(self):
        return f"El nombre del empleado {self.nombre}\nsus apellidos son {self.apellidos}\nsu dni es {self.direccion}\nsu direccion es {self.direccion}\nsu antiguedad es {self.antiguedad}\nsu telefono es {self.telefono}\nsu salario es {self.salario}\ny su puesto en la empresa es secretario"

class Vendedor():
    def __init__(self,matricula = 0,marca = "",modelo = "",telefono = 0,area_venta = "",lista_clientes = [],porcentaje_comisiones = 0,nombre = "",apellidos = "",dni = 0,direccion = "",
                 antiguedad = 0,salario = 0,):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.telefono = telefono
        self.area_venta = area_venta
        self.lista_clientes = lista_clientes
        self.porcentaje_comisiones = porcentaje_comisiones
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.salario = salario
    def informacion(self):
        self.nombre = input("Digite su nombre")
        self.apellidos = input("Digite sus apellidos")
        self.dni = int(input("Digite su dni"))
        self.direccion = input("Digite su direccion")
        self.antiguedad = int(input("Digite sus años de antiguedad"))
        self.telefono = int(input("Digite su numero de telefono"))
        self.salario = float(input("Digite su salario"))
        self.matricula = int(input("Digita tu matricula"))
        self.marca = input("Digite la marca de tu auto")
        self.modelo = input("Digita el modelo de tu auto")
        self.telefono = int(input("Digita tu numero de telefono"))
        self.area_venta = input("Digita tu area de venta")
        self.porcentaje_comisiones = int(input("Digita tu porcentaje de comisiones"))
        i = 0
        for i in range(1,11):
            if self.antiguedad > i:
                i += 1
            elif self.antiguedad == i:
                porcentaje = 10/self.salario*100
                self.salario = self.salario + porcentaje * i
                return "Se a aplicado el porcentaje anual"
            else:
                return "Digite un valor correcto"

        return "La informacion fue ingresada correctamente"
    def mostrar(self):
        return f"El nombre del empleado es {self.nombre}\nsus apellidos son {self.apellidos}\nsu dni es {self.direccion}\nsu direccion es {self.direccion}\nsu antiguedad es {self.antiguedad}\nsu telefono es {self.telefono}\nsu salario es {self.salario}\ny su puesto en la empresa es vendedor"
    def agregar_cliente(self):
        self.lista_clientes = []
        cliente = input("Digita el cliente que vas a agregar")
        self.lista_clientes.append(cliente)
        print("El cliente se agrego con exito")
        return self.lista_clientes
    def eliminar_cliente(self):
        eliminar = input("Digite el cliente que va a eliminar")
        self.lista_clientes.remove(eliminar)
        return self.lista_clientes
    def cambiar_coche(self):
        print("Digite la informacion del nuevo coche")
        self.matricula = int(input("Digite la informacion de su matricula"))
        self.marca = input("Digite la marca de su vehiculo")
        self.modelo = input("Digite el modelo de su vehiculo")
        return "Se a cambiado la informacion con exito"
class Jefe_de_zona():
    def __init__(self,nombre = "",apellidos = "",dni = 0,direccion = "",antiguedad = 0,telefono = 0,salario = 0,secretario = "",lista_vendedores = [],matricula = 0,modelo = "",marca = ""):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.telefono = telefono
        self.salario = salario
        self.secretario = secretario
        self.lista_vendedores = lista_vendedores
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
    def informacion(self):
        self.nombre = input("Digite su nombre")
        self.apellidos = input("Digite sus apellidos")
        self.dni = int(input("Digite su dni"))
        self.direccion = input("Digite su direccion")
        self.antiguedad = int(input("Digite sus años de antiguedad"))
        self.telefono = int(input("Digite su numero de telefono"))
        self.salario = float(input("Digite su salario"))
        self.secretario = input("Digite cual es el secretario en funcionamiento")
        self.matricula = int(input("Digita tu matricula"))
        self.modelo = input("Digita el modelo de tu vehiculo")
        self.marca = input("Digita la marca de tu vehiculo")
        i = 0
        for i in range(1,11):
            if self.antiguedad > i:
                i += 1
            elif self.antiguedad == i:
                porcentaje = 20/self.salario*100
                self.salario = self.salario + porcentaje * i
                return "Se a aplicado el porcentaje anual"
            else:
                return "Digite un valor correcto"
    def mostrar(self):
        return f"El nombre del empleado es {self.nombre}\nsus apellidos son {self.apellidos}\nsu dni es {self.direccion}\nsu direccion es {self.direccion}\nsu antiguedad es {self.antiguedad}\nsu telefono es {self.telefono}\nsu salario es {self.salario}\ny su puesto en la empresa es jefe de zona"
    def cambiar_secretario(self):
        self.secretario = input("Digite el nuevo secretario")
        return "El secretario se a cambiado con exito"
    def cambiar_coche(self):
        print("Digite la informacion del nuevo coche")
        self.matricula = int(input("Digite la informacion de su matricula"))
        self.marca = input("Digite la marca de su vehiculo")
        self.modelo = input("Digite el modelo de su vehiculo")
        return "Se a cambiado la informacion con exito"
    def agregar_vendedor(self):
        vendedor = input("Digite el vendedor que va a agregar")
        self.lista_vendedores = []
        self.lista_vendedores.append(vendedor)
        return self.lista_vendedores
    def eliminar_vendedor(self):
        eliminar = input("Digite el vendedor que va a eliminar")
        self.lista_vendedores.remove(eliminar)
        return self.lista_vendedores
empleado_1 = Empleado()
empleado_2 = Secretario()
empleado_3 = Vendedor()
empleado_4 = Jefe_de_zona()
print(empleado_1.informacion())
print(empleado_1.cambiar_supervisor())
print(empleado_1.incrementar_salario())
print(empleado_2.informacion())
print(empleado_2.mostrar())
print(empleado_3.informacion())
print(empleado_3.mostrar)
print(empleado_3.agregar_cliente())
print(empleado_3.eliminar_cliente())
print(empleado_3.cambiar_coche())
print(empleado_4.informacion())
print(empleado_4.mostrar())
print(empleado_4.cambiar_secretario())
print(empleado_4.agregar_vendedor())
print(empleado_4.eliminar_vendedor())
