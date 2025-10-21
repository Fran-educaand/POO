import Persona
import Calificacion
class Alumno(Persona):
    def __init__(self, dni, nombre, apellidos, fechaNacimiento, ciclo):
        
        super().__init__(self, dni, nombre,  apellidos, fechaNacimiento)
        self.ciclo = ciclo
        self.notas = []        
        

    def matricular(self,modulo):

        calificacion = Calificacion(modulo,"Fisica",11)
        self.notas.append(calificacion)
      
        return True
    
    def calificar(self, nota,modulo):
        
        for n in self.notas:
            if notas[n.getModulo().getNombre()] == modulo.getNombre():
                notas[n].setNotafinal(nota)
            else:
                print("El modulo no se encontró")

        pass
    
    def promociona(self):
        return True
    
    def getNotamedia(self):
        pass
    
    def __str__(self):
        return f"DNI: {self.dni} Nombre: {self.nombre} Apellidos: {self.apellidos} FechaNacimiento: {self.fechaNacimiento} Ciclo: {self.ciclo} "
    
