import csv
import os
from datetime import datetime

class Usuario ():
    def __init__(self, idUsuario, nombre, contraseña, tipoUsuario):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.contraseña = contraseña
        self.tipoUsuario = tipoUsuario

class SistemaGestionResidentes:
    def __init__(self):
        self.archivo_usuarios = "usuarios.csv"
        self.usuarios = {}
        self.cargar_usuarios()

    def cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
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

    def registrarUsuario(self, nombre, tipoUsuario, contraseña):
        for u in self.usuarios.values():
            if u.nombre == nombre:
                print("El usuario ya existe.")
                return None

        nuevo_id = str(len(self.usuarios) + 1)

        usuario = Usuario(nuevo_id, nombre, contraseña, tipoUsuario)
        self.usuarios[nuevo_id] = usuario

        archivoExiste = os.path.exists(self.archivo_usuarios)

        with open(self.archivo_usuarios, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)

            if not archivoExiste or os.stat(self.archivo_usuarios).st_size == 0:
                writer.writerow(['idUsuario', 'nombre', 'tipoUsuario', 'contraseña'])

            writer.writerow([nuevo_id, nombre, tipoUsuario, contraseña])

        print("Usuario registrado.")
        return usuario
    
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
    
    def iniciar_sesion(self, nombre, contraseña):
        usuario = self.autenticar(nombre, contraseña)
        if usuario:
            print(f"Bienvenido {usuario.nombre} ({usuario.tipoUsuario})")
            return usuario
        else:
            print("Credenciales incorrectas.")
        return None


class Residente (Usuario):
    def __init__(self, idUsuario, nombre, contraseña, tipoResidente):
        super().__init__(idUsuario, nombre, contraseña, "residente")
        self.tipoResidente = tipoResidente

class Administrador(Usuario):
    def __init__(self, idUsuario, nombre, contraseña):
        super().__init__(idUsuario, nombre, contraseña, "admin")

class Casa():
    def __init__(self, idCasa, numero):
        self.idCasa = idCasa
        self.numero = numero
        self.propietario = None
        self.inquilino = None


class Servicio():
    def __init__(self, idServicio, nombre, tipo, tarifa):
        self.idServicio = idServicio
        self.nombre = nombre
        self.tipo = tipo
        self.tarifa = tarifa

    def calcular_costo(self, cantidad):
        return cantidad * self.tarifa


class Consumo:
    def __init__(self, idConsumo, cantidad, casa, servicio):
        self.idConsumo = idConsumo
        self.cantidad = cantidad
        self.servicio = servicio
        self.fecha = datetime.now()
        self.casa = casa
        self.servicio = servicio

    def total(self):
        return self.servicio.calcular_costo(self.cantidad)


class Recibo():
    def __init__(self, idRecibo, usuario):
        self.idRecibo = idRecibo
        self.usuario = usuario
        self.consumos = []
        self.total = 0
        self.estado = "pendiente"

    def agregar_consumo(self, consumo):
        self.consumos.append(consumo)

    def calcular_total(self):
        self.total = sum(c.total() for c in self.consumos)
        return self.total

    def pagar(self):
        self.estado = "pagado"

class Pago():
    def __init__(self, idPago, recibo):
        self.idPago = idPago
        self.recibo = recibo
        self.fechaPago = datetime.now()
        self.estado = "realizado"

class Reporte():
    def __init__(self, idReporte, usuario, descripcion):
        self.idReporte = idReporte
        self.usuario = usuario
        self.descripcion = descripcion
        self.fecha = datetime.now()