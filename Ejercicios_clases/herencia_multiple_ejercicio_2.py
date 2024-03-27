"""
Crearemos una superclase llamada Electrodoméstico con las siguientes características:
 Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso. Indica que se
podrán heredar.
 Por defecto, el color será blanco, el consumo energético sera F, el precioBase es de 100 € y el peso de
5 kg. Usa constantes para ello.
 Los colores disponibles son blancos, negro, rojo, azul y gris. No importa si el nombre está en
mayúsculas o en minúsculas.
 Los constructores que se implementarán serán
o Un constructor por defecto.
o Un constructor con el precio y peso. El resto por defecto.
o Un constructor con todos los atributos.
 Los métodos que implementara serán:
o Métodos de todos los atributos.
o comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es
correcta usara la letra por defecto. Se invocará al crear el objeto y no sera visible.
o comprobarColor(String color): comprueba que el color es correcto, sino lo es usa el color
por defecto. Se invocará al crear el objeto y no será visible.
o precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño,
también. Esta es la lista de precios:
Los métodos que se implementara serán:
Método get de carga.
precioFinal():, si tiene una carga mayor de 30 kg, aumentara el precio 50 €, sino es así no se incrementara el precio. Llama al método padre y añade el código necesario. Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.
Crearemos una subclase llamada Television con las siguientes características:
Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano), ademas de los atributos heredados.
Por defecto, la resolución sera de 20 pulgadas y el sintonizador sera false.
Los constructores que se implementaran serán:
Un constructor por defecto.
Un constructor con el precio y peso. El resto por defecto.
Un constructor con la resolución, sintonizador TDT y el resto de atributos heredados. Recuerda que debes llamar al constructor de la clase padre.
Los métodos que se implementara serán:
Método get de resolución y sintonizador TDT.
precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un 30% y si tiene un sintonizador TDT incorporado, aumentara 50 €. Recuerda que las condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.
Ahora crea una clase ejecutable que realice lo siguiente:
 Crea un array de Electrodomesticos de 10 posiciones.
 Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
 Ahora, recorre este array y ejecuta el método precioFinal().
 Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones, por un lado, el de
las lavadoras por otro y la suma de los Electrodomesticos (puedes crear objetos Electrodomestico,
pero recuerda que Television y Lavadora también son electrodomésticos). Recuerda el uso operador
instanceof.
Por ejemplo, si tenemos un Electrodoméstico con un precio final de 300, una lavadora de 200 y una
televisión de 500, el resultado final será de 1000 (300+200+500) para electrodomésticos, 200 para lavadora y
500 para televisión
"""
class Electrodomestico():
    def __init__(self,precio_base = 100,color = "Blanco",consumo_energetico = "F",peso = 5):
        self.precio_base = precio_base
        self.color = color
        self.consumo_energetico = consumo_energetico
        self.peso = peso

    def comprobar_consumo_energetico(self):
        self.consumo_energetico = input("Digite un rango entre A y F").strip()
        if self.consumo_energetico == "A":
            self.consumo_energetico = self.consumo_energetico
        elif self.consumo_energetico == "B":
            self.consumo_energetico = self.consumo_energetico
        elif self.consumo_energetico == "C":
            self.consumo_energetico = self.consumo_energetico
        elif self.consumo_energetico == "D":
            self.consumo_energetico = self.consumo_energetico
        elif self.consumo_energetico == "E":
            self.consumo_energetico = self.consumo_energetico
        elif self.consumo_energetico == "F":
            self.consumo_energetico = self.consumo_energetico
        else:
            self.consumo_energetico = self.consumo_energetico
            return "Ingresa un valor correcto"
        return f"Tu estado de consumo energetico es {self.consumo_energetico}"      
    def comprobar_color(self):
        self.color = input("Digita un color").strip()
        if self.color == self.color.capitalize():
            self.color = self.color
        elif self.color == self.color.upper():
                self.color = self.color
        elif self.color == self.color.lower():
            self.color = self.color
        else:
            self.color = "Digite un valor correcto"
        if self.color == "Blanco".upper() or self.color == "Blanco".lower() or self.color == "Blanco".capitalize():
            self.color = self.color
            return self.color
        elif  self.color == "Negro".upper() or self.color == "Negro".lower() or self.color == "Negro".capitalize():
            self.color = self.color
            return self.color
        elif  self.color == "Rojo".upper() or self.color == "Rojo".lower() or self.color == "Rojo".capitalize():
            self.color = self.color
            return self.color
        elif  self.color == "Azul".upper() or self.color == "Azul".lower() or self.color == "Azul".capitalize():
            self.color = self.color
            return self.color
        elif  self.color == "Gris".upper() or self.color == "Gris".lower() or self.color == "Gris".capitalize():
            self.color = self.color
            return self.color
        else:
            self.color = "Blanco"
            return self.color
    def precio_final(self):

        self.peso = int(input("Digita tu peso"))      

        match self.consumo_energetico:
         case "A":
             self.precio_base = self.precio_base + 100
         case "B": 
             self.precio_base = self.precio_base + 80
         case "C":
                self.precio_base = self.precio_base + 60
         case "D":
                self.precio_base = self.precio_base + 50
         case "E":
                self.precio_base = self.precio_base + 30
         case "F":
                self.precio_base = self.precio_base + 10 

        if  self.peso > 0 and self.peso <= 19:
                self.precio_base +=  10
                return f"El precio total es {self.precio_base}"
        elif self.peso > 20 and self.peso <= 49:
                self.precio_base += 50
                return f"El precio total es {self.precio_base}"
        elif self.peso > 50 and self.peso <= 79:
             self.precio_base += 80
             return f"El precio total es {self.precio_base}"
        else:
            self.precio_base += 100
            return f"El precio total es {self.precio_base}"

class Lavadora(Electrodomestico):
    def __init__(self,precio_base = 100,color = "Blanco",consumo_energetico = "F",peso = 5,carga = 5):
        self.carga = carga
        super().__init__(precio_base,color,consumo_energetico,peso)
    def obtener_carga(self):
        return f"Tu carga es {self.carga}"
    def precio_final(self):
        self.carga = int(input("Digite su carga")) 
        if self.carga > 30:
            self.precio_base = self.precio_base + 50
        else:
            self.precio_base = self.precio_base
        return super().precio_final()

class Television(Electrodomestico):
    def __init__(self,precio_base = 100,color = "Blanco",consumo_energetico = "F",peso = 5,resolucion = 20,sintonizador_tdt = False):
          self.resolucion = resolucion
          self.sintonizador_tdt =  sintonizador_tdt 
          super().__init__(precio_base,color,consumo_energetico,peso)
    def  datos_tv(self):
         return f"Su resolucion es {self.resolucion} y el estado de su sintonizador es {self.sintonizador_tdt}"

    def precio_final(self):
        super().precio_final()
        numero_booleano = int(input("Para saber el estado de su sintonizador digite 0 si es False o digite 1 si es True"))
        self.sintonizador_tdt = bool(numero_booleano)
        self.resolucion = int(input("Digita tu resolucion"))
        print(self.sintonizador_tdt)
        if self.sintonizador_tdt == True :
             print("Se aplica un costo extra del sintonizador")
             self.precio_base = self.precio_base + 50
        elif self.sintonizador_tdt == False:
             print("No se aplica un costo extra del sintonizador")
             self.precio_base = self.precio_base
        if self.resolucion > 40:
            porcentaje = 30/100*self.precio_base
            self.precio_base = self.precio_base + porcentaje
        else:
             self.precio_base =  self.precio_base

        return f"Y el precio total es {round(float(self.precio_base))}"


class Valores_precio():
     def __init__(self,lista_valores):
          self.lista_valores = lista_valores


Electrodomestico_1 = Lavadora()
Electrodomestico_2  = Television()
print(Electrodomestico_1.comprobar_consumo_energetico(),Electrodomestico_1.precio_final())
print(Electrodomestico_2.comprobar_consumo_energetico(),Electrodomestico_2.precio_final())