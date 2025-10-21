import Modulo
class Calificacion():

    def __init__(self,modulo,nombre,horas):
           super().__init__(horas, nombre)
           self.modulo = modulo
           self.setNotaFinal=0
    
    def getModulo(self):
         pass
    
    def getnotaFinal(self):
         pass
    
    def setNotaFinal(notaFinal):
         return notaFinal