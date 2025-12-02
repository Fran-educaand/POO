from RecursoDigital import RecursoDigital

class Podcast (RecursoDigital):
    def __init__(self, titulo, autor, anio, num_episodios, tema):
        super().__init__(titulo, autor, anio)
        self.num_episodios = num_episodios
        self.tema = tema

    def abrir(self):
        print(f"Abriendo podcast {self.getTitulo()}")
    
    def tipo(self):
        return f"Podcast"
    
    def descripcion(self):
        return f"Número de episodios: {self.num_episodios}, Tema: {self.tema}"