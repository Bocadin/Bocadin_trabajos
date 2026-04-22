import csv
import os
from datetime import datetime

class Usuario ():
    def __init__(self, idUsuario, nombre, contraseña, tipoUsuario):
        self.idUsuario = idUsuario
        self.nombre = nombre 
        self.contraseña = contraseña 
        self.tipoUsuario = tipoUsuario

    def iniciar_sesion(self, nombre, contraseña):
        usuario = self.autenticar(nombre, contraseña)
        if usuario:
            print(f"Bienvenido {usuario.nombre} ({usuario.tipoUsuario})")
            return usuario
        else:
            print("Credenciales incorrectas.")
            return None


class SistemaGestionResidentes:
    def __init__(self):
        self.archivo_usuarios = os.path.join(os.path.dirname(__file__), "usuarios.csv")
        self.usuarios = {}
        self._cargar_usuarios()
        
        
    def _cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            print(f"El archivo {self.archivo_usuarios} no existe. Se creará al registrar usuarios.")
            return
        
        with open(self.archivo_usuarios, mode='r', newline='', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for row in reader:
                usuario = Usuario(
                    row['idUsuario'],
                    row['nombre'],
                    row['contraseña'],
                    row['tipoUsuario']
                )
                self.usuarios[usuario.idUsuario] = usuario
    

    def guardar_csv_nuevo(self):
        with open(self.archivo_usuarios, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=['idUsuario', 'nombre', 'tipoUsuario', 'contraseña'])
            writer.writeheader()
            for usuario in self.usuarios.values():
                writer.writerow({
                    'idUsuario': usuario.idUsuario,
                    'nombre': usuario.nombre,
                    'tipoUsuario': usuario.tipoUsuario,
                    'contraseña': usuario.contraseña
                })


    def registrarUsuario(self, nombre, tipoUsuario, contraseña):
        # Validar duplicados
        for u in self.usuarios.values():
            if u.nombre == nombre:
                print("El usuario ya existe.")
                return
        
        # Generar nuevo ID
        nuevo_id = str(max([int(id) for id in self.usuarios.keys()], default=0) + 1)

        nuevo_usuario = Usuario(nuevo_id, nombre, contraseña, tipoUsuario)
        self.usuarios[nuevo_id] = nuevo_usuario

        archivoExiste = os.path.exists(self.archivo_usuarios)

        with open(self.archivo_usuarios, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=['idUsuario', 'nombre', 'tipoUsuario', 'contraseña'])
            
            if not archivoExiste or os.stat(self.archivo_usuarios).st_size == 0:
                writer.writeheader()
            
            writer.writerow({
                'idUsuario': nuevo_usuario.idUsuario,
                'nombre': nuevo_usuario.nombre,
                'tipoUsuario': nuevo_usuario.tipoUsuario,
                'contraseña': nuevo_usuario.contraseña
            })


    def eliminarUsuario(self, idUsuario):
        if idUsuario in self.usuarios:
            del self.usuarios[idUsuario]
            self.guardar_csv_nuevo()
            print(f"Usuario con ID {idUsuario} eliminado correctamente.")
        else:
            print(f"El usuario con ID {idUsuario} no existe.")


    def autenticar(self, nombre, contraseña):
        for usuario in self.usuarios.values():
            if usuario.nombre == nombre and usuario.contraseña == contraseña:
                return usuario
        return None



class Residente (Usuario): 
    def __init__ (self, tipoResidente, idUsuario, nombre, contraseña, tipoUsuario):
        super(). __init__ (idUsuario, nombre, contraseña, tipoUsuario)
        self.tipoResidente = tipoResidente
    
class Administrador(Usuario):
    def __init__ (self, idUsuario, nombre, contraseña, tipoUsuario):
        super(). __init__(idUsuario, nombre, contraseña, tipoUsuario)

class Casa():
    def __init__(self, idCasa, numero):
        self.idCasa= idCasa
        self.numero = numero 
        self.propietario = Usuario
        self.inquilino = Usuario

class Servicio():
    def __init__ (self, idServicio, name, tipo, tarifa):
        self.idServicio= idServicio
        self.nombreServ= name 
        self.tipo= tipo 
        self.tarifa= tarifa  

class Consumo ():
    def __init__ (self, idConsumo, type, cantidad):
        self.idConsumo = idConsumo
        self.tipoConsumo = type
        self.cantidad= cantidad
    #tengo dudas en la parte del uso del datetime en las clases 
        self.fecha= datetime
        self.casa= Casa
        self.servicio = Servicio

class Recibo ():
    def __init__ (self, idRecibo, total, estado):
        self.idRecibo= idRecibo
        self.usuario = Usuario
        self.total= total 
        self.fecha= datetime
        self.estado= estado 
        self.casa = Casa 

class Pago():
    def __init__(self, idPago, estado):
        self.idPago = idPago
        self.recibo = Recibo
        self.fechaPago= datetime
        self.estado= estado

class Reporte():
    def __init__(self, idReporte, descripcion):
        self.idReporte= idReporte
        self.usuario= Usuario
        self.descripcion= descripcion
        self.fechaReporte= datetime