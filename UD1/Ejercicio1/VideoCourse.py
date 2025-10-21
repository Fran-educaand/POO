from Curso import Curso

class VideoCourse(Curso): 

    def __init__(self,titulo,instructor,precio,clases,lenght_video):

        super().__init__(titulo,instructor,precio,clases)
        
        self.lenght_video=lenght_video

video_course = VideoCourse( "IA", "Antonio", 49.99, 10,100)
video_course.show_details("IA")
