class Producto: 
    def __init__(self, nombre, precio_base, stock):
        self.nombre = nombre 
        self.precio_base = precio_base
        self.stock = stock
        
    def aplicar_descuento(self, porcentaje):
        self.precio_base*=(1-porcentaje)
        print (f"el nuevo precio es {self.precio_base}")
    def actualizar_stock(self, cantidad):
        if (self.stock+cantidad)<0:
            print("no puedes tener stock negativo")
        else:
            self.stock += cantidad 
            print (f"la nueva cantidad es {self.stock}")
        
class Categoria:
    def __init__(self, nombre_categoria, lista_prductos):
        self.nombre_categoria= nombre_categoria
        self.lista_productos=[]