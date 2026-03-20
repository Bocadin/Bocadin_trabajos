from datetime import datetime, timedelta

class Material ():
    def __init__ (self, idMaterial, titulo, añoPublicacion, disponible):
        self.idMaterial= idMaterial
        self.titulo= titulo
        self.añoPublicacion= añoPublicacion
        self.disponible= disponible

    def actualizarDisponibilidad(self):
        self.disponible = not self.disponible
        print(f"Disponibilidad de '{self.titulo}' actualizada a: {self.disponible}")

    def obtenerDetalles(self):
        print(f"ID: {self.idMaterial}  //  Título: {self.titulo} //  Año: {self.añoPublicacion}")


class Libro(Material):
    def __init__(self, autor, isbn, genero, idMaterial, titulo, añoPublicacion, disponible ):
        super(). __init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor= autor
        self.isbn= str(isbn)
        self.genero= genero

    def validarISBN(self):
        if len(self.isbn) == 13:
            print(f"ISBN verificado: {self.isbn}")
        else: 
            print("ISBN inválido, verifica los dígitos")

    def consultarAutor(self):
        print(f"El autor de {self.titulo} es {self.autor}")


class Revista(Material):
    def __init__( self, edicion, periodicidad, idMaterial, titulo, añoPublicacion, disponible):
        super(). __init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion= edicion
        self.periodicidad = periodicidad
    
    def obtenerEdicion(self):
        print(f"La edicion de la revista {self.titulo} es: {self.edicion}")

    def obtenerPeriodicidad(self):
        print(f"La revista '{self.titulo}' se publica de forma {self.periodicidad}")



class MaterialDigital(Material):
    def __init__(self, tipoArchivo, urlDescarga, tamañoMB, idMaterial, titulo, añoPublicacion, disponible):
        super(). __init__( idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo= tipoArchivo
        self.urlDescarga= urlDescarga
        self.tamañoMb= tamañoMB
    
    def descargar(self):
        if self.disponible:
            print(f"Descargando '{self.titulo}'...")
            print(f"Archivo: {self.tipoArchivo}")
            print(f"Tamaño: {self.tamañoMb} MB")
            print(f"URL: {self.urlDescarga}")
        else:
            print(f"El material '{self.titulo}' no está disponible para descarga.")

    def generarLink(self):
        print(f"Link de descarga para '{self.titulo}': {self.urlDescarga}")


class Persona():
    def __init__ (self, idPersona, name, email):
        self.idPersona= idPersona
        self.nombre = name
        self.email= email

    def log_in(self, nombre_ingresado, email_ingresado):
        print("Ingrese su usuario:""\n") 
        if self.nombre == nombre_ingresado and self.email == email_ingresado:
           print(f"Usuario: {nombre_ingresado} /// Email: {email_ingresado}")
           print(f"---Bienvenido a Biblioteca Smart---""\n")

           if isinstance(self, Usuario):
                print(f"Has iniciado sesión {self.nombre}")

           elif isinstance(self, Bibliotecario):
                print(f"Has iniciado sesión como BIBLIOTECARIO con id: {self.idEmpleado}")

        else:
            print(f"Usuario: {nombre_ingresado} --- Email: {email_ingresado}")
            print("Correo o usuario incorrecto")

    def actualizar_perfil(self, nuevo_nombre, nuevo_email):
        print("Ingresa los nuevos datos:")
        self.nombre= nuevo_nombre 
        self.email= nuevo_email
        print(f"Los datos han sido actualizados, el nuevo nombre es: {nuevo_nombre} y el nuevo email es: {nuevo_email} ")


class Usuario(Persona):
    def __init__ (self, limitePrestamos, idPersona, name, email):
        super(). __init__(idPersona, name, email)
        self.limitePrestamos = limitePrestamos
        self.listaActiva= []
        self.bloqueado = False

    def consultarDisponibilidad(self, material): 
        if material.disponible:
            print(f"El material '{material.titulo}' está disponible.")
            return True
        else:
            print(f"El material '{material.titulo}' no está disponible.")
            return False
        
    def solicitarPrestamo(self, material):
        print(f"{self.nombre} solicita el préstamo de '{material.titulo}'")
        return material
 

class Bibliotecario(Persona):
    def __init__ (self, idEmpleado, idPersona, name,  email):
        super(). __init__ (idPersona, name, email)
        self.idEmpleado= idEmpleado
    
    def gestionarPrestamo(self, usuario, material, idPrestamo ):
        if isinstance(usuario, Usuario):
            if material.disponible:
                if len(usuario.listaActiva) < usuario.limitePrestamos:
                    prestamo = Prestamo(idPrestamo, usuario, material, datetime.now(), datetime.now() + timedelta(days=7))
                    usuario.listaActiva.append(prestamo)
                    material.actualizarDisponibilidad()

                    print(f"Préstamo registrado por el bibliotecario {self.nombre}")
                else :
                    print("El usuario alcanzó su límite de préstamos")
            else:
                print("El material no está disponible")
        else:
            print("Solo se pueden prestar materiales a usuarios")

    def transferirMaterial(self, material, sucursalOrigen, sucursalDestino):
        if sucursalOrigen.verificarStock(material) and material.disponible:
            sucursalOrigen.catalogoLocal.remove(material)
            sucursalDestino.catalogoLocal.append(material)
            print(f"El material '{material.titulo}' fue transferido de {sucursalOrigen.nombreSucursal} a {sucursalDestino.nombreSucursal}")

        else:
            print(f"El material '{material.titulo}' no existe en el catálogo de {sucursalOrigen.nombreSucursal}")


class Sucursal():
    def __init__ (self, idSucursal, nombreSucursal):
        self.idSucursal = idSucursal
        self.nombreSucursal = nombreSucursal
        self.catalogoLocal= []

    def actualizarCatalogo(self, material):
        self.catalogoLocal.append(material)
        print(f"Se agregó un nuevo material: {material.titulo}")

    def verificarStock(self, material):
        if material in self.catalogoLocal:
            print(f"El material {material.titulo} se encuentra disponible")
            return True
        else: 
            print (f"Material no disponible")
            return False


class Prestamo():
    def __init__(self, idPrestamo, usuario, material, fechaInicio, fechaDevolucion):
        self.idPrestamo = idPrestamo
        self.usuario = usuario
        self.material = material
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.activo = True

    def finalizarPrestamo(self):
        if self.activo:
            self.activo = False
            self.material.disponible = True

            if self in self.usuario.listaActiva:
                self.usuario.listaActiva.remove(self)

            print(f"El préstamo {self.idPrestamo} ha finalizado.")
            print(f"El usuario {self.usuario.nombre} devolvió '{self.material.titulo}'.")
            print(f"El material ahora está disponible nuevamente.")

        else:
            print("El préstamo ya estaba finalizado")


    def estaVencido(self):

        fecha_actual = datetime.now()

        if fecha_actual > self.fechaDevolucion:
            print(f"El préstamo {self.idPrestamo} está vencido")
            return True
        else:
            print(f"El préstamo {self.idPrestamo} aún está en tiempo")
            return False
        
class Penalizacion ():
    def __init__(self, monto, motivo, pagada):
        self.monto= monto 
        self.motivo= motivo 
        self.pagada= pagada

    def calcularMulta(self, prestamo):
        if prestamo.estaVencido():
            dias_retraso = (datetime.now() - prestamo.fechaDevolucion).days
            self.monto = dias_retraso * 10
            self.motivo = f"Retraso de {dias_retraso} días"
            
            print(f"Multa generada: ${self.monto}")
            print(f"---Motivo: {self.motivo}---")
            return self.monto

        else:
            print("No hay multa, el préstamo no está vencido")
            return 0

    def bloquearUsuario(self, usuario):
        if not self.pagada:
            if not usuario.bloqueado:
                usuario.bloqueado = True
                print(f"El usuario {usuario.nombre} ha sido bloqueado por falta de pago")
            else:
                print("El usuario ya esta bloqueado")

class Catalogo():
    def __init__ (self):
        self.materiales= []

    def agregarMaterial(self, material):
        self.materiales.append(material)

    def buscarPorAutor(self, autor):
        resultados = []

        for material in self.materiales:
            if isinstance(material, Libro) and material.autor == autor:
                resultados.append(material)

        if resultados:
            for u in resultados:
                print(f"Encontrado: {u.titulo}")
        else:
            print("No se encontraron libros de ese autor")
       

    def buscarEnSucursales(self, material, sucursales):
        if not isinstance(sucursales, list):
            sucursales= [sucursales]
        
        encontrado= False
        for sucursal in sucursales:
            if material in sucursal.catalogoLocal:
                estado = "Disponible" if material.disponible else "No disponible"
                print(f"{material.titulo} -> {sucursal.nombreSucursal} ({estado})")
                encontrado = True

        if not encontrado:
            print("El material no se encuentra en ninguna sucursal")