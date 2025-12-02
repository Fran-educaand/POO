class RecursoDigital:
    def __init__(self,__titulo,__autor,__anio):
      self.__titulo = __titulo
      self.__autor=__autor
      self.__anio = __anio
    
    def setTitulo (self,__titulo):
      self.__titulo = __titulo
    
    def setAutor (self,autor):
      self.__autor = autor
     
    def setAño (self,año):
      self.__anio = año
    
    def getTitulo (self):
      return self.__titulo
    
    def getAutor (self):
      return self.__autor
    
    def getAño (self):
      return self.__anio
    
    def descripcion_basica(self):
      print( f"Titulo: {self.__titulo}, Autor: {self.__autor}, Año: {self.__anio}")

    def abrir(self):
      print("Abriendo...")
    
    def tipo(self):
      return f"Recurso Genérico"