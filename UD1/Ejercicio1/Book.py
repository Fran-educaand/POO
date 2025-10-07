class Book:

    def __init__(self, isbn, titulo, autor, editorial, pagina, precio, ejemplares):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.pagina = pagina
        if precio < 50 or precio > 1000:
            print("El precio debe estar entre 50 y 1000")
        else: self.precio = precio
        self.precio = precio
        self.ejemplares = ejemplares

    def to_string(self):
        return f'ISBN: {self.isbn}, Titulo: {self.titulo},  Paginas: {self.pagina}, Precio: {self.precio}, Ejemplares: {self.ejemplares}'

    def in_stock(self):
        if self.ejemplares > 0:
            return True
        else:
            return False
        
    
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

books = [book1, book2, book3, book4]
for book in books:
   print( book.to_string()) 

for book in books:
    if book.autor == 'Jack':
      print(book.titulo)  



















   
    

