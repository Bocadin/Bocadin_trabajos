import csv
import os
from datetime import datetime

class Usuario:
    def __init__(self, idUsuario, Username, contraseña, tipoUsuario, nombre_completo, direccion, telefono, estado, foto_perfil = None):
        self.idUsuario = idUsuario
        self.Username = Username
        self.contraseña = contraseña
        self.tipoUsuario = tipoUsuario
        self.nombre_completo = nombre_completo if nombre_completo else "Sin Nombre"
        self.direccion = direccion if direccion else "Sin Dirección"
        self.telefono = telefono if telefono else "Sin Teléfono"
        self.estado = estado if estado else "Activo"
        self.foto_perfil = foto_perfil if foto_perfil else "admin_default.png"
    
    def consultar_perfil(self):
        return {
            "idUsuario": self.idUsuario,
            "nombre_completo": self.nombre_completo,
            "tipoUsuario": self.tipoUsuario,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "foto_perfil": self.foto_perfil
            
        }
    
    def actualizar_perfil(self, nuevo_Username=None, nueva_foto=None, nueva_contraseña=None):
        if nuevo_Username:
            self.Username = nuevo_Username
        if nueva_foto:
            self.foto_perfil = nueva_foto
        if nueva_contraseña:
            self.contraseña = nueva_contraseña


class SistemaGestionResidentes:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.archivo_usuarios = os.path.join(base_dir, "usuarios.csv")
        self.usuarios = {}
        self.cargar_usuarios()
        self.asegurar_admin_default()

    def asegurar_admin_default(self):
        # Crear admin si no existe
        if "admin" not in self.usuarios:
            ruta_foto = ruta_foto = os.path.join(os.path.dirname(__file__), "admin_icon.png")  # para la foto
            admin = Usuario("admin", "Admin SAC", "1234", "admin", "Administrador", "Oficina SAC", "123456789", "Activo", ruta_foto)
            self.usuarios["admin"] = admin
            self.guardar_csv_nuevo()

    def cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            return
        try:
            with open(self.archivo_usuarios, mode='r', newline='', encoding='utf-8') as archivo:
                # Usamos DictReader para leer por nombres de columna
                reader = csv.DictReader(archivo)
                for row in reader:
                    # Creamos el objeto Usuario usando las llaves del CSV
                    u = Usuario(
                        row['idUsuario'],
                        row['Username'],
                        row['contraseña'],
                        row['tipoUsuario'],
                        row.get('nombre_completo', ""),
                        row.get('direccion', ""),
                        row.get('telefono', ""),
                        row.get('estado', "pendiente"),
                        row.get('foto_perfil', "admin_default.png")
                    )
                    self.usuarios[u.idUsuario] = u
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")

    def registroforAdmin(self, NameUser, contraseña ):
        """
        Función que dispara el botón de registro en el Login.
        Crea la cuenta en estado PENDIENTE.
        """
        for u in self.usuarios.values():
            if u.Username == NameUser:
                return "error_duplicado"

        ids = [int(u.idUsuario) for u in self.usuarios.values() if str(u.idUsuario).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)

        # Se crea con los campos de información real vacíos
        nuevo_usuario = Usuario(nuevo_id, NameUser, contraseña, "residente", "", "", "","pendiente")
        self.usuarios[nuevo_id] = nuevo_usuario
        
        if self.guardar_csv_nuevo():
            return "exito"
        return "error_guardado"

    def guardar_csv_nuevo(self):
        """Reescribe el archivo CSV con la información actual en memoria"""
        try:
            with open(self.archivo_usuarios, mode='w', newline='', encoding='utf-8') as archivo:
 
                campos = ['idUsuario', 'Username', 'tipoUsuario', 'contraseña','nombre_completo', 'direccion', 'telefono', 'estado', 'foto_perfil']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                
# Escritura de encabezados y datos desde la memoria ram
                writer.writeheader()
                for u in self.usuarios.values():
                    writer.writerow({
                        'idUsuario': u.idUsuario,
                        'Username': u.Username,
                        'tipoUsuario': u.tipoUsuario,
                        'contraseña': u.contraseña,
                        'nombre_completo': u.nombre_completo,
                        'direccion': u.direccion,
                        'telefono': u.telefono,
                        'estado': u.estado,
                        'foto_perfil': u.foto_perfil
                    })
            return True
        except Exception as e:
            print(f"Error al sincronizar base de datos: {e}")
            return False

    def actualizarContraseña(self, nombre_username, nueva_contraseña):
        for u in self.usuarios.values():
            if u.Username == nombre_username:
                u.contraseña = nueva_contraseña
                return self.guardar_csv_nuevo()
        return False

    def eliminarUsuario(self, idUsuario):
        if idUsuario in self.usuarios:
            del self.usuarios[idUsuario]
            self.guardar_csv_nuevo()
            print(f"Usuario con ID {idUsuario} eliminado.")
        else:
            print("El ID no existe.")

    def autenticar(self, nombre, contraseña):   
        #Retorna el objeto usuario si es válido.
        for usuario in self.usuarios.values():
            if usuario.Username == nombre and usuario.contraseña == contraseña:
                if usuario.estado == "pendiente":
                    return "usuario_pendiente"
                return usuario
        return None

class Residente (Usuario):
    def __init__(self,tipoResidente, idUsuario, Username, contraseña, tipoUsuario, nombre_completo, direccion, telefono, estado):
        super().__init__(idUsuario, Username, contraseña, "residente", nombre_completo, direccion, telefono, estado)
        self.tipoResidente = tipoResidente

    def consultar_consumos(self, lista_consumos):
        return [c for c in lista_consumos if c.casa.inquilino == self or c.casa.propietario == self]
    
    def ver_Recibos(self):
        return self.recibos 
    
    def reportar_falla(self, idReporte, descripción):
        return Reporte(idReporte, self, descripción)
    
    def pago_servicio(self, recibo, idPago):
        if recibo.estado =="pendiente":
            pago = Pago (idPago, recibo)
            recibo.marcar_pagado()
            return pago
        return None

class Administrador(Usuario):
    def __init__(self, idUsuario, nombre, contraseña):
        super().__init__(idUsuario, nombre, contraseña, "admin")

    def activar_usuario(self, sistema, id_usuario, nombre_real, direccion, telefono):
        #El Admin usa esta función para 'Enlazar' la cuenta con datos reales.

        if id_usuario in sistema.usuarios:
            user = sistema.usuarios[id_usuario]
            user.nombre_completo = nombre_real
            user.direccion = direccion
            user.telefono = telefono
            user.estado = "activo" # Aquí se le da acceso total
            
            sistema.guardar_csv_nuevo()
            return True
        return False


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
        self.casa = casa
        self.servicio = servicio
        self.fecha = datetime.now()

    def total(self):
        return self.servicio.calcular_costo(self.cantidad)

class Recibo():
    def __init__(self, idRecibo, usuario):
        self.idRecibo = idRecibo
        self.usuario = usuario
        self.consumos = []
        self.total_pagar = 0
        self.estado = "pendiente"

    def agregar_consumo(self, consumo):
        self.consumos.append(consumo)

    def calcular_total(self):
        self.total_pagar = sum(c.total() for c in self.consumos)
        return self.total_pagar

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