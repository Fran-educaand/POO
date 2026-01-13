from .RecursoDigital import RecursoDigital

class LibroDigital(RecursoDigital):
    def __init__(self, titulo, autor, anio, num_paginas, formato):
        super().__init__(titulo, autor, anio)
        self.formato = formato
        self.num_paginas = num_paginas

    def abrir(self):
        print(f"Abriendo libro {self.getTitulo()} en formato {self.formato}")

    def tipo(self):
        return "Libro"

    def descripcion(self):
        return f"Número de páginas: {self.num_paginas}, Formato: {self.formato}"
        