#Crea la clase Fraccion. Los atributos serán numerador y denominador. Y algunos de los métodos pueden ser invierte, simplifica, multiplica, divide, etc. 
#Prueba la clase creada en un programa en el que se instancien objetos y se les apliquen métodos.
#Ejemplo:
#-7/8 x 5 = -35/8
#-7/8 ^-1 = -8/7
#-7/8 x 3/5 = -21/40
#-7/8 : 3/5 = -35/24
#-910/350 = -13/5



from math import gcd


class Fraccion:

   

    def __init__(self,numerador,denomirador):
        self.numerador = numerador
        self.denomirador=denomirador

    def invertir(self):
        self.numerador , self.denomirador = self.denomirador , self.numerador

    def multiplicar (self):
        resultado= self.numerador * self.denomirador
        print(f"La multiplicacion es {resultado}")

    def dividir (self):
        resultado= self.numerador * self.denomirador
        print(f"La multiplicacion es {resultado}")

    def simplifica(self):
        divisor = gcd(self.numerador,self.denomirador)
        self.numerador //=divisor
        self.denomirador //= divisor

frac = Fraccion(10,5)
frac.multiplicar()
frac.dividir()
frac.invertir()
    
