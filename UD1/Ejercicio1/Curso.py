class Curso: 
    
    usuarios=[]
    calificaciones = []
  
    def __init__(self,titulo,instructor,precio,clases,cpromedio = 0.0):
        self.titulo = titulo
        self.intructor = instructor
        self.precio = precio
        self.clases = clases
        self.cpromedio = cpromedio
    
    def __str__(self):
        return f'({self.titulo}, {self.intructor}, {self.precio}, {self.clases}, {self.usuarios}, {self.calificaciones}, {self.cpromedio})'
    
    def new_user_enrolled(self , user):
        Curso.usuarios.append(user)

    def received_a_rating(self , calificacion):
        Curso.calificaciones.append(calificacion)
        self.cpromedio = sum(Curso.calificaciones) /len(Curso.calificaciones)

        

    def show_details(self , titulo):
        if self.titulo == titulo:
            print(self.__str__())
        else:
            print("No existe el curso")