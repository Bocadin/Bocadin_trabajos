import csv
import os
from datetime import datetime

class Usuario:
    def __init__(self, idUsuario, Username, contraseña, correo, tipoUsuario,
                 nombre_completo="", direccion="", telefono="",
                 estado="pendiente", foto_perfil=None):
        self.idUsuario = idUsuario
        self.Username = Username
        self.contraseña = contraseña
        self.correo = correo
        self.tipoUsuario = tipoUsuario
        self.nombre_completo = nombre_completo  if nombre_completo else "Sin Nombre"
        self.direccion = direccion if direccion else "Sin Dirección"
        self.telefono = telefono if telefono else "Sin Teléfono"
        self.estado = estado if estado else "pendiente"
        self.foto_perfil = foto_perfil if foto_perfil else "admin_default.png"

    def consultar_perfil(self):
        return {
            "idUsuario":       self.idUsuario,
            "nombre_completo": self.nombre_completo,
            "tipoUsuario":     self.tipoUsuario,
            "correo":          self.correo,
            "direccion":       self.direccion,
            "telefono":        self.telefono,
            "foto_perfil":     self.foto_perfil,
        }

    def actualizar_perfil(self, nuevo_Username=None, nueva_foto=None, nueva_contraseña=None, nuevo_correo=None):
        if nuevo_Username:   self.Username   = nuevo_Username
        if nueva_foto:       self.foto_perfil = nueva_foto
        if nueva_contraseña: self.contraseña  = nueva_contraseña
        if nuevo_correo:     self.correo      = nuevo_correo


class Residente(Usuario):
    def __init__(self, tipoResidente, idUsuario, Username, contraseña, correo,
                 nombre_completo="", direccion="", telefono="",
                 estado="pendiente", foto_perfil=None):
        super().__init__(idUsuario, Username, contraseña, correo, tipoResidente,
                         nombre_completo, direccion, telefono,
                         estado, foto_perfil)
        self.tipoResidente = tipoResidente
        self.recibos = []

    def consultar_consumos(self, lista_consumos):
        return [c for c in lista_consumos if c.usuario_id == self.idUsuario]

    def ver_recibos(self):
        return self.recibos

    def reportar_falla(self, idReporte, descripcion):
        return Reporte(idReporte, self, descripcion)

    def pago_servicio(self, recibo, idPago):
        if recibo.estado == "pendiente":
            pago = Pago(idPago, recibo)
            recibo.pagar()
            return pago
        return None
    
    #PRUEBA DE FUNCIÓN PARA USUARIO PARA MOSTRAR PAGO
    def obtener_informacion_pago(self, sistema):
        # Buscar consumos pendientes
        consumos_pendientes = [c for c in sistema.consumos.values() if c.usuario_id == self.idUsuario and c.estado == "pendiente"]
        total_pendiente = sum(c.total(sistema) for c in consumos_pendientes)
        
        if consumos_pendientes:
            # Encontrar la fecha más reciente de los consumos
            fecha_vencimiento = "25 de " + datetime.now().strftime("%B, %Y")
        else:
            fecha_vencimiento = "Sin pagos pendientes"
            
        return {
            "fecha": fecha_vencimiento,
            "monto": f"${total_pendiente:.2f}"
        }


class Administrador(Usuario):
    def __init__(self, idUsuario, nombre, contraseña, correo, foto_perfil=None):
        super().__init__(
            idUsuario, nombre, contraseña, correo, "admin",
            "Administrador", "Oficina Central", "0000000000",
            "activo", foto_perfil or "admin_icon.png"
        )

    def activar_usuario(self, sistema, id_usuario, nombre_real, direccion, telefono):
        """Completa los datos del residente y le da acceso total."""
        if id_usuario in sistema.usuarios:
            user = sistema.usuarios[id_usuario]
            user.nombre_completo = nombre_real
            user.direccion       = direccion
            user.telefono        = telefono
            user.estado          = "activo"
            sistema.guardar_csv_nuevo()
            return True
        return False

class SistemaGestionResidentes:

    # Inicialización 
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.archivo_usuarios  = os.path.join(base_dir, "usuarios.csv")
        self.archivo_servicios = os.path.join(base_dir, "servicios.csv")
        self.archivo_consumos  = os.path.join(base_dir, "consumos.csv")
        self.archivo_casas     = os.path.join(base_dir, "casas.csv")
        self.archivo_recibos   = os.path.join(base_dir, "recibos.csv")

        self.usuarios  = {}
        self.servicios = {}
        self.consumos  = {}
        self.casas     = {}
        self.recibos   = {}

        self.cargar_usuarios()
        self.asegurar_admin_default()
        self.cargar_servicios()
        self.cargar_consumos()
        self.cargar_casas()
        self.cargar_recibos()

    # Helpers de carga
    def _instanciar_usuario(self, row):
        """
        Crea el objeto correcto (Residente o Usuario genérico) según tipoUsuario.
        Esto garantiza que el tipo quede reflejado en el objeto desde el arranque.
        """
        tipo = row.get('tipoUsuario', 'residente')
        kwargs = dict(
            idUsuario       = row['idUsuario'],
            Username        = row['Username'],
            correo         = row.get('correo', ""), 
            contraseña      = row['contraseña'],
            nombre_completo = row.get('nombre_completo', ""),
            direccion       = row.get('direccion', ""),
            telefono        = row.get('telefono', ""),
            estado          = row.get('estado', "pendiente"),
            foto_perfil     = row.get('foto_perfil', "admin_default.png"),
        )
        if tipo == "admin":
            # Eliminamos tipoUsuario de kwargs si existiera, aunque aquí no está
            u = Usuario(tipoUsuario="admin", **kwargs)
        else:
            # propietario / inquilino / residente → instancia Residente
            u = Residente(tipoResidente=tipo, **kwargs)
        return u

    # Carga de datos
    def cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            return
        try:
            with open(self.archivo_usuarios, mode='r', newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    u = self._instanciar_usuario(row)
                    self.usuarios[u.idUsuario] = u
            print("Usuarios cargados con éxito.")
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")

    def asegurar_admin_default(self):
        if "admin" not in self.usuarios:
            admin = Usuario("admin", "Admin SAC", "1234", "admin@sac.com", "admin",
                            "Admin Principal", "Oficina Central", "000000",
                            "activo", "admin_icon.png")
            self.usuarios["admin"] = admin
            self.guardar_csv_nuevo()

    def cargar_servicios(self):
        if not os.path.exists(self.archivo_servicios):
            return
        try:
            with open(self.archivo_servicios, mode='r', newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    s = Servicio(row['idServicio'], row['nombre'],
                                 row['tipo'], float(row['tarifa']))
                    self.servicios[s.idServicio] = s
        except Exception as e:
            print(f"Error al cargar servicios: {e}")

    def cargar_consumos(self):
        if not os.path.exists(self.archivo_consumos):
            return
        try:
            with open(self.archivo_consumos, mode='r', newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    # Compatibilidad con CSVs viejos que usaban 'casa_id'
                    u_id = row.get('usuario_id', row.get('casa_id', ''))
                    c = Consumo(row['idConsumo'], float(row['cantidad']),
                                u_id, row['servicio_id'],
                                row.get('fecha'), row.get('estado', 'pendiente'))
                    self.consumos[c.idConsumo] = c
        except Exception as e:
            print(f"Error al cargar consumos: {e}")

    def cargar_casas(self):
        if not os.path.exists(self.archivo_casas):
            return
        try:
            with open(self.archivo_casas, mode='r', newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    c = Casa(row['idCasa'], row['numero'])
                    c.propietario = row.get('propietario_id', '')
                    c.inquilino   = row.get('inquilino_id', '')
                    self.casas[c.idCasa] = c
        except Exception as e:
            print(f"Error al cargar casas: {e}")

    def cargar_recibos(self):
        if not os.path.exists(self.archivo_recibos):
            return
        try:
            with open(self.archivo_recibos, mode='r', newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    r = Recibo(row['idRecibo'], row['usuario_id'])
                    r.total_pagar = float(row.get('total', 0))
                    r.estado      = row.get('estado', 'pendiente')
                    r.periodo     = row.get('periodo', '')
                    self.recibos[r.idRecibo] = r
        except Exception as e:
            print(f"Error al cargar recibos: {e}")

    # Guardado de datos
    def guardar_csv_nuevo(self):
        """Reescribe usuarios.csv con el estado actual en memoria."""
        try:
            campos = ['idUsuario', 'Username', 'contraseña', 'tipoUsuario', 'correo',
                      'nombre_completo', 'direccion', 'telefono', 'estado', 'foto_perfil']
            with open(self.archivo_usuarios, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for u in self.usuarios.values():
                    writer.writerow({
                        'idUsuario':       u.idUsuario,
                        'Username':        u.Username,
                        'contraseña':      u.contraseña,
                        'tipoUsuario':     u.tipoUsuario,
                        'correo':          u.correo,
                        'nombre_completo': u.nombre_completo,
                        'direccion':       u.direccion,
                        'telefono':        u.telefono,
                        'estado':          u.estado,
                        'foto_perfil':     u.foto_perfil,
                    })
            return True
        except Exception as e:
            print(f"Error al sincronizar usuarios: {e}")
            return False

    def guardar_servicios_csv(self):
        try:
            with open(self.archivo_servicios, mode='w', newline='', encoding='utf-8') as f:
                campos = ['idServicio', 'nombre', 'tipo', 'tarifa']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for s in self.servicios.values():
                    writer.writerow({'idServicio': s.idServicio, 'nombre': s.nombre,
                                     'tipo': s.tipo, 'tarifa': s.tarifa})
            return True
        except Exception as e:
            print(f"Error al sincronizar servicios: {e}")
            return False

    def guardar_consumos_csv(self):
        try:
            with open(self.archivo_consumos, mode='w', newline='', encoding='utf-8') as f:
                campos = ['idConsumo', 'cantidad', 'fecha', 'servicio_id', 'usuario_id', 'estado']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for c in self.consumos.values():
                    writer.writerow({'idConsumo': c.idConsumo, 'cantidad': c.cantidad,
                                     'fecha': c.fecha, 'servicio_id': c.servicio_id,
                                     'usuario_id': c.usuario_id, 'estado': c.estado})
            return True
        except Exception as e:
            print(f"Error al sincronizar consumos: {e}")
            return False

    def guardar_casas_csv(self):
        try:
            with open(self.archivo_casas, mode='w', newline='', encoding='utf-8') as f:
                campos = ['idCasa', 'numero', 'propietario_id', 'inquilino_id']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for c in self.casas.values():
                    writer.writerow({'idCasa': c.idCasa, 'numero': c.numero,
                                     'propietario_id': c.propietario,
                                     'inquilino_id': c.inquilino})
            return True
        except Exception as e:
            print(f"Error al sincronizar casas: {e}")
            return False

    def guardar_recibos_csv(self):
        try:
            with open(self.archivo_recibos, mode='w', newline='', encoding='utf-8') as f:
                campos = ['idRecibo', 'usuario_id', 'total', 'estado', 'periodo']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for r in self.recibos.values():
                    writer.writerow({'idRecibo': r.idRecibo, 'usuario_id': r.usuario,
                                     'total': r.total_pagar, 'estado': r.estado,
                                     'periodo': getattr(r, 'periodo', '')})
            return True
        except Exception as e:
            print(f"Error al sincronizar recibos: {e}")
            return False

    #Gestión de usuarios
    def registroforAdmin(self, NameUser, contraseña, correonew, tipoResidente="residente"):
        """
        Registra un nuevo residente desde la pantalla de login.
        El tipo (propietario / inquilino / residente) queda guardado en el CSV.
        La cuenta se crea en estado PENDIENTE hasta que el admin la active.
        """
        # Verificar duplicado de username
        for u in self.usuarios.values():
            if u.Username == NameUser and u.correo == correonew:
                return "error_duplicado"

        ids = [int(u.idUsuario) for u in self.usuarios.values() if str(u.idUsuario).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)

        nuevo_usuario = Residente(
            tipoResidente  = tipoResidente,
            idUsuario      = nuevo_id,
            Username       = NameUser,
            contraseña     = contraseña,
            correo         = correonew,
            nombre_completo= "",
            direccion      = "",
            telefono       = "",
            estado         = "pendiente",
        )
        self.usuarios[nuevo_id] = nuevo_usuario

        return "exito" if self.guardar_csv_nuevo() else "error_guardado"
    
    #Modificar datos
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
        """Retorna el objeto usuario si las credenciales son válidas."""
        for usuario in self.usuarios.values():
            if usuario.Username == nombre and usuario.contraseña == contraseña:
                if usuario.estado == "pendiente":
                    return "usuario_pendiente"
                return usuario
        return None

    # Gestión de servicios
    def crear_servicio(self, nombre, tipo, tarifa):
        ids = [int(s.idServicio) for s in self.servicios.values() if str(s.idServicio).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        s = Servicio(nuevo_id, nombre, tipo, float(tarifa))
        self.servicios[nuevo_id] = s
        self.guardar_servicios_csv()
        return s

    def editar_servicio(self, idServicio, nombre=None, tipo=None, tarifa=None):
        if idServicio in self.servicios:
            s = self.servicios[idServicio]
            if nombre:           s.nombre = nombre
            if tipo:             s.tipo   = tipo
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

    # Gestión de consumos
    def registrar_consumo(self, cantidad, usuario_id, servicio_id, fecha=None):
        ids = [int(c.idConsumo) for c in self.consumos.values() if str(c.idConsumo).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        c = Consumo(nuevo_id, float(cantidad), usuario_id, servicio_id, fecha, "pendiente")
        self.consumos[nuevo_id] = c
        self.guardar_consumos_csv()
        return c

    def marcar_consumo_pagado(self, idConsumo):
        if idConsumo in self.consumos:
            self.consumos[idConsumo].estado = "pagado"
            self.guardar_consumos_csv()
            return True
        return False

    def eliminar_consumo(self, idConsumo):
        if idConsumo in self.consumos:
            del self.consumos[idConsumo]
            self.guardar_consumos_csv()
            return True
        return False

    # Gestión de recibos
    def generar_recibo(self, usuario_id, periodo, total):
        ids = [int(r.idRecibo) for r in self.recibos.values() if str(r.idRecibo).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        r = Recibo(nuevo_id, usuario_id, periodo)
        r.total_pagar = total
        self.recibos[nuevo_id] = r
        self.guardar_recibos_csv()
        return r

    #Gestión de casas
    def crear_casa(self, numero, propietario_id="", inquilino_id=""):
        ids = [int(c.idCasa) for c in self.casas.values() if str(c.idCasa).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        c = Casa(nuevo_id, numero)
        c.propietario = propietario_id
        c.inquilino   = inquilino_id
        self.casas[nuevo_id] = c
        self.guardar_casas_csv()
        return c

class Casa:
    def __init__(self, idCasa, numero):
        self.idCasa     = idCasa
        self.numero     = numero
        self.propietario = ""
        self.inquilino   = ""


class Servicio:
    def __init__(self, idServicio, nombre, tipo, tarifa):
        self.idServicio = idServicio
        self.nombre     = nombre
        self.tipo       = tipo
        self.tarifa     = tarifa

    def calcular_costo(self, cantidad):
        return cantidad * self.tarifa


class Consumo:
    def __init__(self, idConsumo, cantidad, usuario_id, servicio_id,
                 fecha=None, estado="pendiente"):
        self.idConsumo  = idConsumo
        self.cantidad   = cantidad
        self.usuario_id = usuario_id
        self.servicio_id = servicio_id
        self.fecha      = fecha if fecha else datetime.now().strftime("%Y-%m-%d")
        self.estado     = estado

    def total(self, sistema):
        if self.servicio_id in sistema.servicios:
            return sistema.servicios[self.servicio_id].calcular_costo(self.cantidad)
        return 0


class Recibo:
    def __init__(self, idRecibo, usuario, periodo=""):
        self.idRecibo   = idRecibo
        self.usuario    = usuario
        self.consumos   = []
        self.total_pagar = 0
        self.estado     = "pendiente"
        self.periodo    = periodo

    def agregar_consumo(self, consumo):
        self.consumos.append(consumo)

    def calcular_total(self, sistema):
        self.total_pagar = sum(c.total(sistema) for c in self.consumos)
        return self.total_pagar

    def pagar(self):
        self.estado = "pagado"


class Pago:
    def __init__(self, idPago, recibo):
        self.idPago    = idPago
        self.recibo    = recibo
        self.fechaPago = datetime.now()
        self.estado    = "realizado"


class Reporte:
    def __init__(self, idReporte, usuario, descripcion):
        self.idReporte  = idReporte
        self.usuario    = usuario
        self.descripcion = descripcion
        self.fecha      = datetime.now()