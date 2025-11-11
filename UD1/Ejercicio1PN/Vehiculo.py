class Vehiculo:
    vehiculosCreados = []
    kilometrosTotales=0
    def __init__(self,kilometrosRecorrido=0):
        self.kilometrosRecorrido = kilometrosRecorrido
        
class Bicicleta(Vehiculo):

    def __init__(self, kilometrosRecorrido=0):
        super().__init__(kilometrosRecorrido)

    def comprastebici(self):
        print("Compraste una bici")
   
    def caballito(self,kilometros):
        self.kilometrosRecorrido += kilometros

    def verKm(self):
        print( f"La bici tiene {self.kilometrosRecorrido} km")
        
class Coche(Vehiculo):
    def __init__(self, kilometrosRecorrido=0):
        super().__init__(kilometrosRecorrido)

    def comprastecoche(self):
        print("Compraste un coche")

    def andaCoche(self,kilometros):
        self.kilometrosRecorrido += kilometros

    def verKm(self):
        print(f"El coche tiene {self.kilometrosRecorrido} km")




bici =Bicicleta()
coche = Coche ()
Vehiculo.vehiculosCreados=[bici,coche]
while True:
    print('''ELIGE UNA OPCION:
       1.Compra la bicicleta
       2. Haz el caballito con la bicicleta
       3.Compra el coche el coche
       4.Anda con el coche
       5.Ver kilometraje de la bicicleta
       6.Ver kilometraje del coche
       7.Ver kilometraje total
       8.Salir''')
    resp = int(input(" "))

    

    match resp:
        case 1:

            bici.comprastebici()
        case 2:
            txt  = int(input("Cuantos km avanzastes: "))
            bici.caballito(txt)
        case 3:
            coche.comprastecoche()
        case 4:
            txt  = int(input("Cuantos km avanzastes: "))
            coche.andaCoche(txt)
        case 5:
            bici.verKm()
        case 6:
            coche.verKm()
        case 7:
            
            for i in Vehiculo.vehiculosCreados:
                Vehiculo.kilometrosTotales += i.kilometrosRecorrido  
            print(f"Kilometrajes totales {Vehiculo.kilometrosTotales}")
        case 8:
            print("Pues adios")
        case _:
            print("Espabila...")


