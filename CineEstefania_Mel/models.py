from enum import Enum
from datetime import datetime


class Persona():
    def __init__(self, idPersona, nombre, email, telefono):
        self.idPersona= idPersona
        self.nombre= nombre 
        self.email= email
        self.telefono= telefono
    
    def log_in (self, nombre_ingresado, email_ingresado ):
        print(f"Ingresa tu usuario y Email")
        if self.nombre== nombre_ingresado and self.email == email_ingresado:
           print(f"Hola, bienvenido {self.nombre} has iniciado sesión")

        else:
            print("Correo o usuario incorrecto")

    def log_out(self):
        print(f"Cerrando sesión :)")
    
    def actualizar_datos (self, nuevo_nombre, nuevo_email):
        print("Ingresa los nuevos datos:")
        self.nombre= nuevo_nombre 
        self.email= nuevo_email
        print(f"Los datos han sido actualizados, el nuevo nombre es: {nuevo_nombre} y el nuevo email es: {nuevo_email} ")

class Usuario(Persona): 
    def __init__(self, puntosFidelidad, historialReservas, idPersona, nombre, email, telefono):
       super().__init__(idPersona, nombre, email, telefono)
       self.puntosFidelidad = puntosFidelidad
       self.historialReservas =  historialReservas
       self.reservaciones=[]

    def crearReserva(self, funcion, asientos):
        if asientos <= funcion.calcularAsientosLibres():
            funcion.asientosOcupados += asientos
            self.reservaciones.append({"funcion": funcion, "asientos": asientos})
            print(f"Reserva realizada para '{funcion.pelicula.titulo}' en {funcion.sala.nombre_espacio}.")
        else:
            print("No hay suficientes asientos disponibles.")

    def cancelar_reserva(self, funcion):
        reserva = next((r for r in self.reservaciones if r["funcion"] == funcion), None)
        if reserva:
            funcion.asientosOcupados -= reserva["asientos"]
            self.reservaciones.remove(reserva)
            print(f"La reserva fue cancelada para '{funcion.pelicula.titulo}'.")
        else:
            print("No existe una reserva para esta función")

class Rol(Enum):
    TAQUILLERO = 1
    ADMIN = 2
    LIMPIEZA = 3

class Empleado(Persona):
    def __init__(self, idEmpleado, rol, horario , idPersona, nombre, email, telefono ):
        super().__init__(idPersona, nombre, email, telefono)
        self.rol = Rol[rol]
        self.idEmpleado= idEmpleado
        self.horario= horario

    def marcaEntrada(self):
        print (f"Entrada de {self.nombre} con ID: {self.idEmpleado} a las {self.horario}")

    def gestionarFunciones(self):
        if self.rol == Rol.ADMIN:
            print("Persona Autorizada, entrando a sistema...")
        else:
            print("Persona no autorizada")

    def agregar_funcion(self, funcion):
      if not self.gestionarFunciones:
        print("Acceso denegado. Solo los administradores pueden agregar funciones.")
        return
    
      print(f"Función agregada: {funcion.pelicula.titulo} "
          f"a las {funcion.horario_inicio} en la sala {funcion.sala.nombre_espacio}.")

    def modificar_promocion(self, promocion, nuevo_descuento, nuevas_condiciones):
        if not self.gestionarFunciones:
            print("Acceso denegado. Solo los administradores pueden modificar promociones.")
            return
        
        promocion.porcentajeDescuento = nuevo_descuento
        promocion.descripcion = nuevas_condiciones
        print(f"Promoción modificada: {nuevo_descuento}% de descuento. {nuevas_condiciones}.")


class Espacio():
    def __init__(self,idEspacio, nombre_espacio, ubicacion, estado_limpio):
        self.idEspacio = idEspacio
        self.nombre_espacio= nombre_espacio
        self.ubicacion= ubicacion
        self.estado_limpio= estado_limpio
    
    def verificarDisponibilidad(self):
        if self.estado_limpio:
            print(f"Disponible la {self.nombre_espacio} para su uso en {self.ubicacion}")
        else:
            print(f"Necesita mantenimiento la {self.nombre_espacio} en {self.ubicacion}")

    def limpiarEspacio(self):
        self.estado_limpio = True
        print(f"La {self.nombre_espacio} fue limpiada en {self.ubicacion}")

class Tipo(Enum):
    SALA_2D = 1
    SALA_3D= 2
    SALA_IMAX= 3

class Sala(Espacio):
    def __init__(self,tipo, capacidadTotal, esVip, idEspacio, nombre_espacio, ubicacion, estado_limpio):
        super().__init__(idEspacio, nombre_espacio, ubicacion, estado_limpio)
        self.tipo=Tipo[tipo]
        self.capacidadTotal= capacidadTotal
        self.esVip= esVip

    def ajustarAforo(self, aforo):
        self.aforo= aforo
        if  0< aforo <50:
            self.capacidadTotal=aforo
            print(f"La {self.nombre_espacio}: tiene una capacidad de : {self.capacidadTotal} personas.")
        else:
            print(f"Sin capacidad suficiente")
    
    def obtenerTipoSala(self): 
        tipo_sala = self.tipo.name  
        if self.esVip:
            print(f"La {self.nombre_espacio} es una sala {tipo_sala} VIP.")
        else:
            print(f"La {self.nombre_espacio} es una sala {tipo_sala} normal.")

class ZonaComida(Espacio):
    def __init__(self, idEspacio, nombre_espacio, ubicacion, estado_limpio):
        super().__init__(idEspacio, nombre_espacio, ubicacion, estado_limpio)
        self.Productos=[]
        self.stockActual = {}

    def venderProducto(self, producto_name, cantidad_venta):
        if producto_name in self.stockActual and self.stockActual[producto_name] >= cantidad_venta:
            self.stockActual[producto_name] -= cantidad_venta
            print(f"La venta fue de: {cantidad_venta} {producto_name}")
        else:
            print(f"No hay suficiente stock de {producto_name}.")

    def actualizar_Inventario(self, producto_name, cantidad):
        if producto_name in self.stockActual:
            self.stockActual[producto_name] += cantidad
        else:
            self.stockActual[producto_name] = cantidad
        print(f"Inventario actualizado: {producto_name} tiene {self.stockActual[producto_name]} unidades.")


class Pelicula():
    def __init__(self, titulo, duracion, genero):
        self.titulo= titulo
        self.duracion= duracion 
        self.genero= genero

    def obtener_Sinopsis(self, sipnosis):
        self.sipnosis= sipnosis
        print(f"Pelicula {self.titulo}/ Sipnosis: {self.sipnosis}  ")

    def esAptaParaTodoPublico(self):
        if self.genero =="terror"  or self.genero=="thriller" or self.genero=="cine erotico":
            print("Categoria con contenido violento, no apto para todo publico")
        else: 
            print("Apta para todo publico")

class Funcion():
    def __init__(self,idFuncion, pelicula, sala, horario_inicio, precioBase):
        self.idFuncion= idFuncion
        self.pelicula= pelicula
        self.sala= sala
        self.horario_inicio= horario_inicio
        self.precioBase= precioBase        
        self.asientosOcupados=0
        
    def calcularAsientosLibres(self):
        disponibles = self.sala.capacidadTotal - self.asientosOcupados
        print (f"Los asientos dsiponibles para la funcion {self.idFuncion} son: {disponibles}")
        return disponibles
    
    def obtenerDetallesFuncion(self):
        print("--- DETALLES DE LA FUNCIÓN ---")
        print(f"Película: {self.pelicula.titulo}")
        print(f"Sala: {self.sala.nombre_espacio} ({self.sala.tipo})")
        print(f"Horario: {self.horario_inicio}")
        print(f"Precio: ${self.precioBase}")
        self.pelicula.esAptaParaTodoPublico() 

class Estado(Enum):
    PENDIENTE= 1
    PAGADA= 2 
    CANCELADA= 3

      
class Reserva():
    def __init__(self, idReserva, usuario, funcion, asientos, montoTotal, estado):
        self.idReserva = idReserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos
        self.montoTotal = montoTotal
        self.estado = Estado[estado]

        self.funcion.asientosOcupados += len(asientos)

    def confirmarPago(self):
        if self.estado == Estado.PENDIENTE:
            self.estado = Estado.PAGADA
            self.usuario.puntosFidelidad += 5
            print(f"Pago confirmado para la reserva {self.idReserva}.")
        else:
            print("La reserva ya no está pendiente.")

    def generarTicket(self):
        print("\n" + "="*20)
        print("      TICKET DE CINE")
        print("="*20)
        print(f"Pelicula: {self.funcion.pelicula.titulo}")
        print(f"Sala: {self.funcion.sala.nombre_espacio}")
        print(f"Asientos: {', '.join(self.asientos)}")
        print(f"Total Pagado: ${self.montoTotal}")
        print(f"Estado: {self.estado.value}")
        print("="*20 + "\n")

    def aplicarPromocion(self, promo):
        if promo.esValida(self.usuario):
          self.montoTotal = promo.aplicarDescuento(self.montoTotal)
          print(f"Promoción aplicada. Nuevo total: ${self.montoTotal}")

class Promocion():
    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentajeDescuento = porcentajeDescuento
        self.fechaExpiracion = fechaExpiracion 

    def esValida(self, usuario):
        fecha_actual = datetime.now()
        if fecha_actual > self.fechaExpiracion:
            print("La promoción ha expirado.")
            return False
        if usuario.puntosFidelidad <10:
            print("El usuario no tiene suficientes puntos para esta promoción.")
            return False
        print("Promoción válida.")
        return True

    def aplicarDescuento(self, monto):
        descuento = monto * (self.porcentajeDescuento / 100)
        nuevo_total = monto - descuento
        print(nuevo_total)
        return nuevo_total
