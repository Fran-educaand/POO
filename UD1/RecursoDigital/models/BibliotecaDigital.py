class BibliotecaDigital:

    def __init__(self,__recursos=[]):
        self.__recursos = __recursos

    def añadirRecursos (self,recurso):
        self.__recursos.append(recurso)

    def listarRecursos (self):
        for recurso in self.__recursos:
            print(f"{recurso.tipo()}  {recurso.descripcion()}")
    
    def abrirRecurso (self):
        for recurso in self.__recursos:
            recurso.abrir()

