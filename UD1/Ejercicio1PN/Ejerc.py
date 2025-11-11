
# Animal: Pero, Hgato, Caballo
# Mineral: pirita, cuarzo ,
# Persona: Paula, javier
# Caballo: Rocinante, bucefalo, pegaso
# Perro: goofy, Snoopy, pluto, ayudantedesantaclaus, Gaika, Milu
# Gato: garfield,tom , silvestre
'''
2 Haz una lista con los atributos que podría tener la clase caballo. A continuación haz una lista con los posibles métodos (acciones asociadas a los caballos). 
Hecho esto implementa la clase Caballo y pruébala creando instancias y aplicándole algunos métodos.
Ejemplo:
Hola, me llamo Babieca

Hola, yo soy Lykos
Ñam ñam ñam
Tocotoc tocotoc tocotoc
'''

class Caballo:
    def __init__(self,nombre , edad , sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def sonido(self):
        print("Tocotoc tocotoc tocotoc , Hiiiiiiieeeeee")
    
    def meLLamo(self):
        print(f"Mi nombre es {self.nombre} , tengo {self.edad} años y soy {self.sexo}")
    
    def comer(self):
        print("Ñam ñam ñam")




