from Equipo import Equipo
class Partido():
    def __init__(self,equipo1,equipo2):
        self.equipo1=equipo1
        self.equipo2 = equipo2

    def anotarGol(self,equipo): 
        equipo.setGoles()

    def mostrarResultado(self):
        print(f"El resultado es {self.equipo1.goles} - {self.equipo2.goles}")
    
    def finalizarPartido(self):
        self.mostrarResultado()
        print("Acabó el encuentro")

        
