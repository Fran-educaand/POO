class Despedida:
    def __init__(self,nombre,hora):
       self.nombre = nombre
       self.hora = hora

    
    def mostrar_despedida(self):
        if self.hora <12:
            print(f'Que tengas una excelente mañana {self.nombre}')
        elif self.hora>=12 and self.hora <21:
            print(f'Que tengas una buena tarde {self.nombre}')
        elif self.hora>=21:
            print(f'Que tengas una buena noche {self.nombre}')

    @classmethod
    def desdeTexto(cls,texto):
        dsp = texto.split(",")
        dsp = Despedida(dsp[0],dsp[1])
        print(f'{dsp.nombre},{dsp.precio}')
        return dsp
    

    @staticmethod
    def precioValido(hora):
        if hora>=0 and hora<= 23:
         return True
        else: False

desp = Despedida("Fran",16)
desp.mostrar_despedida()
