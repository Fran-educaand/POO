from RecursoDigital import RescursoDigital
class VideoCurso (RescursoDigital):
    def __init__(self, titulo, autor, anio, duracion_minutos, nivel):
        super().__init__(titulo, autor, anio)
        self.duracion_minutos = duracion_minutos
        self.nivel = nivel

    def abrir(self):
        print(f"Abriendo video curso {self.titulo} en plataforma {self.plataforma}")
    
    def tipo(self):
        return f"Video"