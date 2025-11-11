'''Crea las clases Animal, Mamifero, Ave, Gato, Perro, Canario, Pinguino y Lagarto. Crea, al menos, tres métodos específicos de cada clase y redefine el/los método/s cuando sea necesario. Prueba las clases creadas en un programa en el que se instancien objetos y se les apliquen métodos.
Ejemplo:
Estoy comiendo palomitas
Soy un pingüino programador, estoy programando en Java
Zzzzzzz
Toma mi patita
Toma pecho, hazte grande
Estoy cuidando mis crias
Estoy tomando el Sol
Zzzzzzz'''

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def dormir(self):
        print(f"{self.nombre} está durmiendo Zzzzzzz")

    def comer(self):
        print(f"{self.nombre} está comiendo")

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido")
class Mamifero(Animal):
    def amamantar(self):
        print(f"{self.nombre} está amamantando a sus crías")

    def cuidar_crias(self):
        print(f"{self.nombre} está cuidando a sus crías")
class Ave(Animal):
    def volar(self):
        print(f"{self.nombre} está volando")

    def poner_huevos(self):
        print(f"{self.nombre} está poniendo huevos")
class Gato(Mamifero):
    def maullar(self):
        print(f"{self.nombre} dice: Miau Miau")

    def rascar(self):
        print(f"{self.nombre} está rascando el sofá")
class Perro(Mamifero):
    def ladrar(self):
        print(f"{self.nombre} dice: Guau Guau")

    def traer_pelota(self):
        print(f"{self.nombre} está trayendo la pelota")
class Canario(Ave):
    def cantar(self):
        print(f"{self.nombre} está cantando")

    def volar_alrededor(self):
        print(f"{self.nombre} está volando alrededor de la jaula")
class Pinguino(Ave):
    def nadar(self):
        print(f"{self.nombre} está nadando")

    def deslizarse(self):
        print(f"{self.nombre} se está deslizando sobre el hielo")
class Lagarto(Animal):
    def tomar_sol(self):
        print(f"{self.nombre} está tomando el sol")

    def mudar_piel(self):
        print(f"{self.nombre} está mudando su piel")
# Pruebas de las clases

if __name__ == "__main__":
    gato = Gato("Mickey", 5)
    perro = Perro("Snoopy", 3)
    canario = Canario("Zazu", 1)
    pinguino = Pinguino("Pingu", 4)
    lagarto = Lagarto("Lagatito", 2)

    gato.maullar()
    gato.rascar()
    gato.dormir()

    perro.ladrar()
    perro.traer_pelota()
    perro.cuidar_crias()

    canario.cantar()
    canario.volar_alrededor()
    canario.poner_huevos()

    pinguino.nadar()
    pinguino.deslizarse()
    pinguino.comer()

    gato.amamantar()
    
    lagarto.tomar_sol()
    lagarto.mudar_piel()
    lagarto.dormir()
