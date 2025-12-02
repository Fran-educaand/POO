if __name__ == "__main__":
    from LibroDigital import LibroDigital
    from VideoCurso import VideoCurso
    from Podcast import Podcast
    from BibliotecaDigital import BibliotecaDigital

    biblioteca = BibliotecaDigital()

    libro1 = LibroDigital("1984", "George Orwell", 1949, 328, "PDF")
    video1 = VideoCurso("Python para Principiantes", "Juan Pérez", 2021, 120, "Básico")
    podcast1 = Podcast("Historia", "Antonio", 2020, 50, "Historia")

    biblioteca.añadirRecursos(libro1)
    biblioteca.añadirRecursos(video1)
    biblioteca.añadirRecursos(podcast1)

    biblioteca.listarRecursos()
    biblioteca.abrirRecurso()