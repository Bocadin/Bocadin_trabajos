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
        self.archivo_servicios = os.path.join(base_dir, "servicios.csv")
        self.archivo_consumos = os.path.join(base_dir, "consumos.csv")
        self.archivo_casas = os.path.join(base_dir, "casas.csv")
        
        self.usuarios = {}
        self.servicios = {}
        self.consumos = {}
        self.casas = {}
        self.recibos = {}
        
        self.cargar_usuarios()
        self.asegurar_admin_default()
        self.cargar_servicios()
        self.cargar_consumos()
        self.cargar_casas()
        self.cargar_recibos()

    def asegurar_admin_default(self):
        if "admin" not in self.usuarios:
            # Llenamos los 9 campos para el admin
            admin = Usuario("admin", "admin", "1234", "admin", 
                            "Admin Principal", "Oficina Central", "000000", "Activo", "admin_icon.png")
            self.usuarios["admin"] = admin
            self.guardar_csv_nuevo()

    def cargar_usuarios(self):
        """Lee el CSV y carga los objetos Usuario en el diccionario self.usuarios"""
        if not os.path.exists(self.archivo_usuarios):
            return
        try:
            with open(self.archivo_usuarios, mode='r', newline='', encoding='utf-8') as archivo:
                # DictReader usa la primera fila del CSV como llaves
                reader = csv.DictReader(archivo)
                for row in reader:
                    # Creamos el objeto Usuario con los 9 datos del CSV
                    u = Usuario(
                        idUsuario=row['idUsuario'],
                        Username=row['Username'],
                        contraseña=row['contraseña'],
                        tipoUsuario=row['tipoUsuario'],
                        nombre_completo=row.get('nombre_completo', "Sin Nombre"),
                        direccion=row.get('direccion', "Sin Dirección"),
                        telefono=row.get('telefono', "Sin Teléfono"),
                        estado=row.get('estado', "Activo"),
                        foto_perfil=row.get('foto_perfil', "admin_default.png")
                    )
                    # Lo guardamos en nuestro diccionario de la RAM
                    self.usuarios[u.idUsuario] = u
            print("Base de datos cargada con éxito.")
        except Exception as e:
            print(f"Error crítico al cargar usuarios: {e}")

    def cargar_servicios(self):
        if not os.path.exists(self.archivo_servicios): return
        try:
            with open(self.archivo_servicios, mode='r', newline='', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for row in reader:
                    s = Servicio(row['idServicio'], row['nombre'], row['tipo'], float(row['tarifa']))
                    self.servicios[s.idServicio] = s
        except Exception as e: print(f"Error al cargar servicios: {e}")

    def guardar_servicios_csv(self):
        try:
            with open(self.archivo_servicios, mode='w', newline='', encoding='utf-8') as archivo:
                campos = ['idServicio', 'nombre', 'tipo', 'tarifa']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writeheader()
                for s in self.servicios.values():
                    writer.writerow({'idServicio': s.idServicio, 'nombre': s.nombre, 'tipo': s.tipo, 'tarifa': s.tarifa})
            return True
        except Exception as e:
            print(f"Error al sincronizar servicios: {e}")
            return False

    def cargar_consumos(self):
        if not os.path.exists(self.archivo_consumos): return
        try:
            with open(self.archivo_consumos, mode='r', newline='', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for row in reader:
                    # Soportar el formato viejo que tenía 'casa_id'
                    u_id = row.get('usuario_id', row.get('casa_id', ''))
                    c = Consumo(row['idConsumo'], float(row['cantidad']), u_id, row['servicio_id'], row['fecha'], row.get('estado', 'pendiente'))
                    self.consumos[c.idConsumo] = c
        except Exception as e: print(f"Error al cargar consumos: {e}")

    def guardar_consumos_csv(self):
        try:
            with open(self.archivo_consumos, mode='w', newline='', encoding='utf-8') as archivo:
                campos = ['idConsumo', 'cantidad', 'fecha', 'servicio_id', 'usuario_id', 'estado']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writeheader()
                for c in self.consumos.values():
                    writer.writerow({'idConsumo': c.idConsumo, 'cantidad': c.cantidad, 'fecha': c.fecha, 'servicio_id': c.servicio_id, 'usuario_id': c.usuario_id, 'estado': c.estado})
            return True
        except Exception as e:
            print(f"Error al sincronizar consumos: {e}")
            return False

    def cargar_casas(self):
        if not os.path.exists(self.archivo_casas): return
        try:
            with open(self.archivo_casas, mode='r', newline='', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for row in reader:
                    c = Casa(row['idCasa'], row['numero'])
                    c.propietario = row.get('propietario_id', '')
                    c.inquilino = row.get('inquilino_id', '')
                    self.casas[c.idCasa] = c
        except Exception as e: print(f"Error al cargar casas: {e}")

    def guardar_casas_csv(self):
        try:
            with open(self.archivo_casas, mode='w', newline='', encoding='utf-8') as archivo:
                campos = ['idCasa', 'numero', 'propietario_id', 'inquilino_id']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writeheader()
                for c in self.casas.values():
                    writer.writerow({'idCasa': c.idCasa, 'numero': c.numero, 'propietario_id': c.propietario, 'inquilino_id': c.inquilino})
            return True
        except Exception as e:
            print(f"Error al sincronizar casas: {e}")
            return False

    def cargar_recibos(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_recibos = os.path.join(base_dir, "recibos.csv")
        if not os.path.exists(ruta_recibos): return
        try:
            with open(ruta_recibos, mode='r', newline='', encoding='utf-8') as archivo:
                reader = csv.DictReader(archivo)
                for row in reader:
                    r = Recibo(row['idRecibo'], row['usuario_id'])
                    r.total_pagar = float(row.get('total', 0))
                    r.estado = row.get('estado', 'pendiente')
                    r.periodo = row.get('periodo', '')
                    self.recibos[r.idRecibo] = r
        except Exception as e: print(f"Error al cargar recibos: {e}")

    def guardar_recibos_csv(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_recibos = os.path.join(base_dir, "recibos.csv")
        try:
            with open(ruta_recibos, mode='w', newline='', encoding='utf-8') as archivo:
                campos = ['idRecibo', 'usuario_id', 'total', 'estado', 'periodo']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                writer.writeheader()
                for r in self.recibos.values():
                    writer.writerow({'idRecibo': r.idRecibo, 'usuario_id': r.usuario, 'total': r.total_pagar, 'estado': r.estado, 'periodo': getattr(r, 'periodo', '')})
            return True
        except Exception as e:
            print(f"Error al sincronizar recibos: {e}")
            return False

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
        try:
            with open(self.archivo_usuarios, mode='w', newline='', encoding='utf-8') as archivo:
                # Definimos los 9 campos en el orden correcto
                campos = ['idUsuario', 'Username', 'contraseña', 'tipoUsuario', 
                          'nombre_completo', 'direccion', 'telefono', 'estado', 'foto_perfil']
                
                writer = csv.DictWriter(archivo, fieldnames=campos)
                
                writer.writeheader()
                for u in self.usuarios.values():
                    writer.writerow({
                        'idUsuario': u.idUsuario,
                        'Username': u.Username,
                        'contraseña': u.contraseña,
                        'tipoUsuario': u.tipoUsuario,
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

    def crear_servicio(self, nombre, tipo, tarifa):
        # Crea y guarda un nuevo servicio (ej. Agua o Luz)
        ids = [int(s.idServicio) for s in self.servicios.values() if str(s.idServicio).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        nuevo_servicio = Servicio(nuevo_id, nombre, tipo, float(tarifa))
        self.servicios[nuevo_id] = nuevo_servicio
        self.guardar_servicios_csv()
        return nuevo_servicio

    def editar_servicio(self, idServicio, nombre=None, tipo=None, tarifa=None):
        if idServicio in self.servicios:
            s = self.servicios[idServicio]
            if nombre: s.nombre = nombre
            if tipo: s.tipo = tipo
            if tarifa is not None: s.tarifa = float(tarifa)
            self.guardar_servicios_csv()
            return True
        return False

    def eliminar_servicio(self, idServicio):
        if idServicio in self.servicios:
            del self.servicios[idServicio]
            self.guardar_servicios_csv()
            return True
        return False

    def registrar_consumo(self, cantidad, usuario_id, servicio_id, fecha=None):
        # Registra un nuevo consumo para un inquilino y lo guarda como 'pendiente'
        ids = [int(c.idConsumo) for c in self.consumos.values() if str(c.idConsumo).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        nuevo_consumo = Consumo(nuevo_id, float(cantidad), usuario_id, servicio_id, fecha, "pendiente")
        self.consumos[nuevo_id] = nuevo_consumo
        self.guardar_consumos_csv()
        return nuevo_consumo

    def marcar_consumo_pagado(self, idConsumo):
        # Cambia el estado de un movimiento (consumo) a pagado
        if idConsumo in self.consumos:
            self.consumos[idConsumo].estado = "pagado"
            self.guardar_consumos_csv()
            return True
        return False

    def eliminar_consumo(self, idConsumo):
        # Elimina permanentemente un movimiento del registro
        if idConsumo in self.consumos:
            del self.consumos[idConsumo]
            self.guardar_consumos_csv()
            return True
        return False

    def generar_recibo(self, usuario_id, periodo, total):
        # Genera un nuevo recibo en la base de datos
        ids = [int(r.idRecibo) for r in self.recibos.values() if str(r.idRecibo).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        r = Recibo(nuevo_id, usuario_id, periodo)
        r.total_pagar = total
        self.recibos[nuevo_id] = r
        self.guardar_recibos_csv()
        return r

    def crear_casa(self, numero, propietario_id="", inquilino_id=""):
        ids = [int(c.idCasa) for c in self.casas.values() if str(c.idCasa).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        nueva_casa = Casa(nuevo_id, numero)
        nueva_casa.propietario = propietario_id
        nueva_casa.inquilino = inquilino_id
        self.casas[nuevo_id] = nueva_casa
        self.guardar_casas_csv()
        return nueva_casa

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
        self.recibos = []

    def consultar_consumos(self, lista_consumos):
        return [c for c in lista_consumos if c.casa.inquilino == self or c.casa.propietario == self]
    
    def ver_Recibos(self):
        return self.recibos
    
    def reportar_falla(self, idReporte, descripción):
        return Reporte(idReporte, self, descripción)
    
    def pago_servicio(self, recibo, idPago):
        if recibo.estado =="pendiente":
            pago = Pago (idPago, recibo)
            recibo.pagar()
            return pago
        return None

class Administrador(Usuario):
    def __init__(self, idUsuario, nombre, contraseña):
        super().__init__(
            idUsuario,
            nombre,
            contraseña,
            "admin",
            "Administrador",
            "Oficina Central",
            "0000000000",
            "activo"
        )

    def activar_usuario(self, sistema, id_usuario, nombre_real, direccion, telefono):

        if id_usuario in sistema.usuarios:
            user = sistema.usuarios[id_usuario]
            user.nombre_completo = nombre_real
            user.direccion = direccion
            user.telefono = telefono
            user.estado = "activo"

            sistema.guardar_csv_nuevo()
            return True

        return False
class Casa():
    def __init__(self, idCasa, numero):
        self.idCasa = idCasa
        self.numero = numero
        self.propietario = ""
        self.inquilino = ""

class Servicio():
    def __init__(self, idServicio, nombre, tipo, tarifa):
        self.idServicio = idServicio
        self.nombre = nombre
        self.tipo = tipo
        self.tarifa = tarifa

    def calcular_costo(self, cantidad):
        return cantidad * self.tarifa

class Consumo:
    def __init__(self, idConsumo, cantidad, usuario_id, servicio_id, fecha=None, estado="pendiente"):
        self.idConsumo = idConsumo
        self.cantidad = cantidad
        self.usuario_id = usuario_id
        self.servicio_id = servicio_id
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d")
        self.estado = estado

    def total(self, sistema):
        if self.servicio_id in sistema.servicios:
            return sistema.servicios[self.servicio_id].calcular_costo(self.cantidad)
        return 0

class Recibo():
    def __init__(self, idRecibo, usuario, periodo=""):
        self.idRecibo = idRecibo
        self.usuario = usuario
        self.consumos = []
        self.total_pagar = 0
        self.estado = "pendiente"
        self.periodo = periodo

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