from Equipo import Equipo
from Jugador import Jugador
from Partido import Partido

class Main():

 adebayor = Jugador ("adebayor",11,"dc")
 munir = Jugador ("munir",7,"mc")
 gravesen = Jugador ("Gravesen",2,"def")
 juan = Jugador ("Juan",10,"def")

 jbarca = [adebayor,munir]
 
 jmadrid = [gravesen,juan]

 barca = Equipo(jbarca)

 madrid = Equipo(jmadrid)

 clasico = Partido (madrid,barca)

 clasico.anotarGol(barca)
 clasico.mostrarResultado()
 clasico.finalizarPartido()