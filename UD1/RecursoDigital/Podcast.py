from RecursoDigital import RescursoDigital

class Podcast (RescursoDigital):
    def __init__(self, titulo, autor, anio, num_episodios, tema):
        super().__init__(titulo, autor, anio)
        self.num_episodios = num_episodios
        self.tema = tema

    def abrir(self):
        print(f"Abriendo podcast {self.titulo} presentado por {self.anfitrion}")
    
    def tipo(self):
        return f"Podcast"