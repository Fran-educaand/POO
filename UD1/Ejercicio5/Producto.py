class Producto: 
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio

    def descuento (self,porcentaje):
        if porcentaje > 0 and porcentaje <100:
           return porcentaje * 100 / self.precio
        else: return("Mal echo")

    @classmethod
    def desdeTexto(cls,texto):
        producto = texto.split(",")
        prd = Producto(producto[0],producto[1])
        print (type(prd))
        print(f'{prd.nombre},{prd.precio}')
        return f'{prd.nombre},{prd.precio}'
    
    @staticmethod
    def precioValido(precio):
        if precio>0:
         return True
        else: False

Producto.desdeTexto("Camiseta,10")
    