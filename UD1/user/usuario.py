class Usuario:
 
    def __init__(self,nombre,email):
      self.nombre = nombre
      self.email=email
    
    def setNombre (self,nombre):
      self.nombre = nombre
     
    
    def setEmail (self,email):
      self.email = email
    
    
    def getNombre (self):
      return self.nombre
    
    def getEmail (self):
      return self.email
    
    def presentacion(self):
      print( f"Mi nombre es {self.nombre} y mi email es {self.email}")

class Alumno (Usuario):
  
  def __init__(self, nombre, email, curso, media):
    super().__init__(nombre, email)
    self.curso = curso
    self.media = media

  def presentacion(self):
      print( f"Soy {self.nombre}, estudiante de {self.curso}, con una nota media de {self.media}")  

class Profesor (Usuario):
  
  def __init__(self, nombre, email, especialidad):
    super().__init__(nombre, email)
    self.especialidad = especialidad

  def presentacion(self):
      print( f"Soy el profesor {self.nombre}, especialista en {self.especialidad}") 

if __name__=="__main__":
  
  user = Usuario("Antonio", "user@")
  alumno = Alumno("Alex", "alumno@","Aleman",5.5)
  profesor = Profesor("Pere", "profesor@","Mates")
  
  lista = [user,alumno,profesor]

  for i,valor in enumerate (lista):
    valor.presentacion()