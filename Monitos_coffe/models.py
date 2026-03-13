from enum import Enum

class Persona():
    def __init__ (self, idPersona, nombre, email):
        self.idPersona= idPersona
        self.nombre= nombre
        self.email= email

    def log_in(self, nombre_ingresado, email_ingresado):
        print("Ingrese su usuario:""\n")
        if self.nombre== nombre_ingresado and self.email == email_ingresado:
           print(f"Usuario: {nombre_ingresado} /// Email: {email_ingresado}")
           print(f"---Bienvenido a Monito's cafe---""\n")

        else:
            print(f"Usuario: {nombre_ingresado} --- Email: {email_ingresado}")
            print("Correo o usuario incorrecto")

    def actualizar_perfil(self, nuevo_nombre, nuevo_email):
        print("Ingresa los nuevos datos:")
        self.nombre= nuevo_nombre 
        self.email= nuevo_email
        print(f"Los datos han sido actualizados, el nuevo nombre es: {nuevo_nombre} y el nuevo email es: {nuevo_email} ")

class Cliente(Persona):
    def __init__ (self, puntosFidelidad, idPersona, nombre, email):
        super ().__init__ (idPersona, nombre, email)
        self.puntosFidelidad = puntosFidelidad
        self.historialPedidos= []

    def realizarPedido(self, pedido):
        self.historialPedidos.append(pedido)
        print(f"Pedido {pedido.idPedido} registrado a nombre de: {self.nombre}.")

    def consultarHistorial(self):
        print(f"\n--- Historial de Pedidos de {self.nombre} ---")
        
        if  not self.historialPedidos:
            print("No hay pedidos registrados aún.")
        else:
            for u, pedido in enumerate (self.historialPedidos, start=1):
                print(f"{u}. ---Pedido: {pedido.idPedido}---")
                print(f"Total: ${pedido.total}")
                print(f"Estado: {pedido.estadoPedido}")
    
    def cajearPuntos(self, cantidad_canje, pedido):
        if self.puntosFidelidad>= cantidad_canje:
            descuento = cantidad_canje/5
            pedido.total-= descuento
            self.puntosFidelidad-= cantidad_canje
            print(f"---Canje completado!! :D ---")
            print(f"Se aplico un descuento de ${descuento}")
            print(f"Total final: {pedido.total}")

        else: 
            print(f"Puntos insuficientes")

class Roles(Enum):
    BARISTA= 1
    MESERO= 2
    GERENTE= 3

class Empleado (Persona):
    def __init__(self, idEmpleado, rol, idPersona, nombre, email):
        super(). __init__(idPersona, nombre, email)
        self.idEmpleado= idEmpleado
        self.rol= Roles[rol]

    def actualizarInventario(self, ingrediente, cantidad, stock):
        if self.rol == Roles.GERENTE:
            print("Bienvenido, abriendo inventario...")
            if ingrediente in stock.ingredientes:
                stock.ingredientes[ingrediente]+= cantidad 
                print(f"El stock ha sido modificado a {stock.ingredientes[ingrediente]}")
            else:
                stock.ingredientes[ingrediente] = cantidad
                print(f"Se han agregado {cantidad} unidades de un nuevo ingrediente {ingrediente} ")

        else:
            print("Persona no autorizada")

    def cambiarEstadoPedido(self, pedido, new_estado):
        pedido.estadoPedido = Estado[new_estado]
        print(f"Pedido {pedido.idPedido} actualizado {pedido.estadoPedido}")

class ProductoBase():
    def __init__(self, idProducto, nombre, precioBase):
        self.idProducto= idProducto
        self.nombre = nombre
        self.precioBase= precioBase

class Temp(Enum):
    FRIA= 1 
    CALIENTE= 2

class Bebida(ProductoBase):
    def __init__ (self, tamaño, temperatura, idProducto, nombre, precioBase):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño= tamaño
        self.temperatura= Temp[temperatura]
        self.modificadores= []

    def agregarExtra (self, extra):
        self.modificadores.append(extra)
        print(f"Se agregó {extra}")

    def calcularPrecioFinal(self):
        new_costo = len(self.modificadores) * 10
        precio_final = self.precioBase + new_costo
        return precio_final

    

class Postre(ProductoBase):
    def __init__(self, esVegano, sinGluten, idProducto, nombre, precioBase):
        super().__init__ (idProducto, nombre, precioBase)
        self.esVegano = esVegano
        self.sinGluten = sinGluten

class Estado(Enum):
    PENDIENTE= 1
    PREPARANDO= 2
    ENTREGADO = 3
    
class Pedido():
    def __init__(self, idPedido, total, estadoPedido):
        self.idPedido= idPedido
        self.total= total
        self.estadoPedido = Estado[estadoPedido]
        self.productos = []
    
    def calcularTotal(self, producto):
        self.productos.append(producto)
        total = 0

        for p in self.productos:
            if isinstance(p, Bebida):
                total += p.calcularPrecioFinal()
            else:
                total += p.precioBase

        self.total = total
        print(f"El costo total es de: {total}")
        return total
    
    def validarStock(self, producto, stock_dispo):
        if producto.nombre in stock_dispo.ingredientes:
            stock = stock_dispo.ingredientes[producto.nombre]
            if stock >0:
             print(f"Existe stock suficiente de: {producto.nombre}")
            else: 
               print(f"No existe stock disponible de {producto.nombre}")
        else:
            print(f"{producto.nombre} no está registrado en el inventario")

class Inventario():
    def __init__ (self):
            self.ingredientes = {}

    def reducirStock(self, ingrediente, cantidad):
        if ingrediente not in self.ingredientes:
            print(f"No existe {ingrediente} en el inventario")
            return
        
        if self.ingredientes[ingrediente]< cantidad:
            print(f"No hay stock suficiente de {ingrediente}")
        else: 
            self.ingredientes[ingrediente]-=cantidad
            print(f"Disponible: {self.ingredientes[ingrediente]}")

    def notificarFaltante(self, ingrediente):
        if ingrediente in self.ingredientes and self.ingredientes[ingrediente] == 0:
            print(f"--Aviso-- sin stock de {ingrediente} ")



        



    





        



    



    



    



