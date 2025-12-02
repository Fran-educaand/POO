from RecursoDigital import RecursoDigital
class VideoCurso (RecursoDigital):
    def __init__(self, titulo, autor, anio, duracion_minutos, nivel):
        super().__init__(titulo, autor, anio)
        self.duracion_minutos = duracion_minutos
        self.nivel = nivel

    def abrir(self):
        print(f"Abriendo video curso {self.getTitulo()}")
    
    def tipo(self):
        return f"Video"
    def descripcion(self):
        return f"Duración: {self.duracion_minutos} minutos, Nivel: {self.nivel}"
    
    