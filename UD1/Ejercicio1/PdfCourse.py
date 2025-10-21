from Curso import Curso

class PdfCourse (Curso) :
	
     def __init__(self,titulo,instructor,precio,clases,pages):

        super().__init__(titulo,instructor,precio,clases)
        
        self.pages=pages
        

pdf_course = PdfCourse( "Python", "Fran",49.99, 10,100)
pdf_course.show_details("Python")