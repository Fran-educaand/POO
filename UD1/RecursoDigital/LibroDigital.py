from RecursoDigital import RescursoDigital
class LibroDigital (RescursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.num_paginas = num_paginas

    def abrir(self):
        print(f"Abriend libro {self.getTitulo()} en formato {self.formato}")
    
    def tipo(self):
        return f"Libro"