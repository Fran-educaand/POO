class Equipo():
    def __init__(self,jugadores,goles=0):
        self.jugadores = jugadores
        self.goles = goles
    
    def setGoles(self):
        self.goles += 1
        return self.goles
     
