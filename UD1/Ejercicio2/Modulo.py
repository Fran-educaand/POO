class Modulo():
    def __init__(self,nombre , horas):
        self.nombre = nombre
        self.horas = horas
    
    def getnombre(self):
        return self.nombre
    
    def gethoras(self):
        return self.horas
    
    def __str__(self):
        return f"Horas: {self.horas} Nombre: {self.nombre} "
    
