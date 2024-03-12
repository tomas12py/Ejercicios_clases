"""
Cree una clase llamada Factura, que una ferretería podría utilizar para representar una
factura por un artículo vendido en la tienda. Una factura debe incluir cuatro piezas de
información como miembros de datos: un número de pieza (string) la descripción de la pieza
(string), la cantidad
de artículos de ese tipo que se van a comprar (int) y el precio por artículo (int).
a. Su clase debe tener un método constructor que inicialice a los cuatro miembros de datos.
b. Proporcione una función establecer y una función obtener para cada miembro de datos.
c. Proporcione una función miembro llamada obtenerMontoFactura que calcule el monto de
la factura (es decir, que multiplique la cantidad por el precio del articulo) y después 
d. Si la cantidad no es positiva, debe establecerse en 0. Si el precio por artículo no es
positivo, debe establecerse en 0.
e. Escriba un programa de prueba que demuestra las capacidades de la clase Factura
"""

class Factura():
    def __init__(self,num_pieza = "",descripcion = "",cantidad = 0,precio = 0):
        self.num_pieza = str(num_pieza)
        self.descripcion = str(descripcion)
        self.cantidad = int(cantidad)
        self.precio = int(precio)
    def establecer(self):
        print("Ingrese la informacion para crear su articulo")
        self.num_pieza = input("Digite el numero de pieza")
        self.descripcion = input("Digite la descripcion del articulo")
        self.cantidad = int(input("Digite la cantidad de existencias del articulo"))
        self.precio = int(input("Digite el precio del articulo"))
        return"Creaste la informacion del articulo con exito"
    def obtener(self):
        return f"\nEl numero de pieza es:{self.num_pieza}\ndescripcion:{self.descripcion}\nla cantidad del articulo es: {self.cantidad}\nel precio del articulo es {self.precio}"
    def obtenerMontoFactura(self):
        if self.cantidad > 0 and self.precio > 0:
            total = self.cantidad * self.precio
            return total
        elif self.cantidad <= 0 and self.precio <= 0:
            self.cantidad = 0
            self.precio = 0
Factura_1 = Factura()
print(f"{Factura_1.establecer()}{Factura_1.obtener()} y el valor del monto de su articulo es: {Factura_1.obtenerMontoFactura()}")
