"""
1) Haz una clase llamada Persona que siga las siguientes condiciones:
 Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que
se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo.
Si quieres añadir algún atributo puedes hacerlo.
 Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0 números,
cadena vacía para String, etc.). Sexo será hombre por defecto, usa una constante para ello.
 Se implantarán varios constructores:
o Un constructor por defecto.
o Un constructor con el nombre, edad y sexo, el resto por defecto.
o Un constructor con todos los atributos como parámetro.
 Los métodos que se implementaran son:
o calcularIMC(): calculara si la persona está en su peso ideal (peso en kg/(altura^2 en m)), si
esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número
entre 20 y 25 (incluidos), significa que está por debajo de su peso ideal la función devuelve un
0 y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un
1. Te recomiendo que uses constantes para devolver estos valores.
 esMayorDeEdad (): indica si es mayor de edad, devuelve un booleano.
 comprobar Sexo(char sexo): comprueba que el sexo introducido es correcto. Si no es
correcto, será H. No será visible al exterior.
 string(): devuelve toda la información del objeto.

"""

class Calcular():
    def __init__(self,peso,altura):
        self.peso = peso
        self.altura = altura    
    def calcular_imc(self,peso = 0,altura = 0):
        self.peso = float(input("Digita tu peso"))
        self.altura = float(input("Digite su altura"))
        imc = self.peso/self.altura**2
        if imc < 20:
            imc = -1
            print("Estas en un peso ideal")
        elif imc >= 20 and imc <= 25:
            imc = 0
            print("Estas por debajo de tu peso ideal")
        else:
            imc = 1
            print("Tienes sobrepeso")
        return f"Este es el resultado del imc {imc}"


class Edad(): 
    def __init__(self,estado_edad = False,edad = 0):
            self.estado_edad = estado_edad
            self.edad = edad
    def es_mayor(self):
        self.edad = int(input("Digita tu edad"))     
        if self.edad >= 18:
            self.estado_edad = True
            print("La persona es mayor de edad")
        else:
            self.estado_edad = False
            print("La persona es menor de edad")
        return f"Este es el resultado de la edad {self.estado_edad}"
    
class Sexo():
    def __init__(self,sexo = ""):
        self.sexo = sexo
    def comprobrar(self):
            self.sexo = input("Digite su sexo").strip()
            if self.sexo  ==  "Hombre":
                self.sexo = "Hombre"
                
            elif self.sexo == "Mujer":
                self.sexo = "Mujer"
                
            else:
                self.sexo = "H"
            return f"Este es el resultado del sexo {self.sexo}"
            
class Datos():
    def __init__(self,nombre = "",edad = 0,sexo = "",peso = 0,altura = 0,dni = 0):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
    def string(self):
        self.nombre = input("Digita tu nombre")
        self.dni = input("Digita tu dni")
        info = f"El nombre de la persona es{self.nombre} su edad es {self.edad} su sexo es {self.sexo} la altura es {self.altura} su peso es {self.peso} y su dni es  {self.dni}"
        return info


class Persona(Calcular,Edad,Sexo,Datos):
    def __init__(self,nombre = "",edad = 0,sexo = "",peso = 0,altura = 0,dni = 0):
        pass
persona_2 = Persona()
print(f"{persona_2.es_mayor()} {persona_2.comprobrar()} {persona_2.calcular_imc()}")
print(f"{persona_2.string()}")


        
        
        