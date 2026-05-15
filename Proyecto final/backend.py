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
        self.foto_perfil = foto_perfil

    def iniciarSesion(self, sistema, contraseña):
        #Verifica credenciales y retorna el usuario si son válidas.
        if self.contraseña == contraseña and self.estado == "activo":
            return self
        return None

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
        return Reporte(idReporte, self.idUsuario, descripcion)

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
    def __init__(self, idUsuario, Username, contraseña, correo, foto_perfil=None):
        super().__init__(
            idUsuario, Username, contraseña, correo, "admin",
            "Administrador", "Oficina Central", "0000000000",
            "activo", foto_perfil or os.path.join(os.path.dirname(os.path.abspath(__file__)), "admin_icon.png")
        )

    def activar_usuario(self, sistema, id_usuario, nombre_real, direccion, telefono):
        #Completa los datos del residente y le da acceso total.
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
        self.archivo_reportes  = os.path.join(base_dir, "reportes.csv")

        self.usuarios  = {}
        self.servicios = {}
        self.consumos  = {}
        self.casas     = {}
        self.recibos   = {}
        self.reportes  = {}

        self.cargar_usuarios()
        self.asegurar_admin_default()
        self.cargar_servicios()
        self.cargar_consumos()
        self.cargar_casas()
        self.cargar_recibos()
        self.cargar_reportes()

    # Helpers de carga
    def _instanciar_usuario(self, row):
        tipo = row.get('tipoUsuario', 'residente')
        foto_perfil = row.get('foto_perfil')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if foto_perfil and not os.path.isabs(foto_perfil):
            # Solo convertimos a absoluta si no es una cadena vacía o nula
            foto_perfil = os.path.join(base_dir, foto_perfil)

        # Si sigue siendo vacío y es admin, le ponemos el icono por defecto
        if not foto_perfil and tipo == "admin":
            foto_perfil = os.path.join(base_dir, "admin_icon.png")

        kwargs = dict(
            idUsuario       = row['idUsuario'],
            Username        = row['Username'],
            correo         = row.get('correo', ""),
            contraseña      = row['contraseña'],
            nombre_completo = row.get('nombre_completo', ""),
            direccion       = row.get('direccion', ""),
            telefono        = row.get('telefono', ""),
            estado          = row.get('estado', "pendiente"),
            foto_perfil     = foto_perfil,
        )
        if tipo == "admin":
            # Instanciar como Administrador para que tenga todos sus métodos
            u = Administrador(
                idUsuario  = kwargs["idUsuario"],
                Username   = kwargs["Username"],
                contraseña = kwargs["contraseña"],
                correo     = kwargs["correo"],
                foto_perfil= kwargs.get("foto_perfil"),
            )
            # Preservar campos adicionales que vengan del CSV
            u.nombre_completo = kwargs.get("nombre_completo", "Administrador")
            u.direccion       = kwargs.get("direccion", "Oficina Central")
            u.telefono        = kwargs.get("telefono", "0000000000")
            u.estado          = kwargs.get("estado", "activo")
        else:
            # propietario / inquilino / residente → instancia Residente
            u = Residente(tipoResidente=tipo, **kwargs)
        return u

    # Carga de datos
    def cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            return
        try:
            with open(self.archivo_usuarios, mode='r', newline='', encoding='utf-8-sig') as f:
                for row in csv.DictReader(f):
                    u = self._instanciar_usuario(row)
                    self.usuarios[u.idUsuario] = u
            print("Usuarios cargados con éxito.")
        except Exception as e:
            print(f"Error al cargar usuarios: {e}")

    def asegurar_admin_default(self):
        if "admin" not in self.usuarios:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            ruta_admin_foto = os.path.join(base_dir, "admin_icon.png")
            admin = Administrador("admin", "Admin SAC", "1234", "admin@sac.com", ruta_admin_foto)
            self.usuarios["admin"] = admin
            self.guardar_csv_nuevo()

    def cargar_servicios(self):
        if not os.path.exists(self.archivo_servicios):
            return
        try:
            with open(self.archivo_servicios, mode='r', newline='', encoding='utf-8-sig') as f:
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
            with open(self.archivo_consumos, mode='r', newline='', encoding='utf-8-sig') as f:
                for row in csv.DictReader(f):
                    # Compatibilidad con CSVs viejos que usaban 'casa_id'
                    u_id = row.get('usuario_id', row.get('casa_id', ''))
                    c = Consumo(row['idConsumo'], float(row['cantidad']),
                                u_id, row['servicio_id'],
                                row.get('fecha'), row.get('estado', 'pendiente'),
                                float(row.get('lectura_actual', 0)))
                    self.consumos[c.idConsumo] = c
        except Exception as e:
            print(f"Error al cargar consumos: {e}")

    def cargar_casas(self):
        if not os.path.exists(self.archivo_casas):
            return
        try:
            with open(self.archivo_casas, mode='r', newline='', encoding='utf-8-sig') as f:
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
            with open(self.archivo_recibos, mode='r', newline='', encoding='utf-8-sig') as f:
                for row in csv.DictReader(f):
                    u_id = row['usuario_id']
                    user_obj = self.usuarios.get(u_id, u_id) 
                    r = Recibo(row['idRecibo'], user_obj)
                    r.total_pagar = float(row.get('total', 0))
                    r.estado      = row.get('estado', 'pendiente')
                    r.periodo     = row.get('periodo', '')
                    
                    # Cargar IDs de consumos vinculados
                    c_ids_str = row.get('consumos_ids', "")
                    if c_ids_str:
                        r.consumos_ids = c_ids_str.split(";")
                        r.consumos = [self.consumos[cid] for cid in r.consumos_ids if cid in self.consumos]
                    
                    self.recibos[r.idRecibo] = r
        except Exception as e:
            print(f"Error al cargar recibos: {e}")

    def cargar_reportes(self):
        if not os.path.exists(self.archivo_reportes):
            return
        try:
            with open(self.archivo_reportes, mode='r', newline='', encoding='utf-8-sig') as f:
                for row in csv.DictReader(f):
                    rep = Reporte(
                        row['idReporte'],
                        row['usuario_id'],
                        row['descripcion'],
                        row.get('titulo', ''),
                        row.get('tipo', 'Mantenimiento'),
                        row.get('prioridad', 'Media'),
                        row.get('estado', 'Pendiente'),
                        row.get('fecha', ''),
                        row.get('foto1', ''),
                        row.get('foto2', ''),
                        row.get('foto3', ''),
                        row.get('nombre_reporta', row['usuario_id'])
                    )
                    self.reportes[rep.idReporte] = rep
        except Exception as e:
            print(f"Error al cargar reportes: {e}")

    # Guardado de datos
    def guardar_csv_nuevo(self):
        #Reescribe usuarios.csv con el estado actual en memoria.
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
                campos = ['idConsumo', 'cantidad', 'fecha', 'servicio_id', 'usuario_id', 'estado', 'lectura_actual']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for c in self.consumos.values():
                    writer.writerow({'idConsumo': c.idConsumo, 'cantidad': c.cantidad,
                                     'fecha': c.fecha, 'servicio_id': c.servicio_id,
                                     'usuario_id': c.usuario_id, 'estado': c.estado,
                                     'lectura_actual': getattr(c, 'lectura_actual', 0)})
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
                campos = ['idRecibo', 'usuario_id', 'total', 'estado', 'periodo', 'consumos_ids']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for r in self.recibos.values():
                    u_id = getattr(r.usuario, 'idUsuario', r.usuario)
                    c_ids = ";".join(getattr(r, 'consumos_ids', []))
                    writer.writerow({
                        'idRecibo': r.idRecibo, 
                        'usuario_id': u_id,
                        'total': r.total_pagar, 
                        'estado': r.estado,
                        'periodo': r.periodo,
                        'consumos_ids': c_ids
                    })
            return True
        except Exception as e:
            print(f"Error al sincronizar recibos: {e}")
            return False

    def guardar_reportes_csv(self):
        try:
            with open(self.archivo_reportes, mode='w', newline='', encoding='utf-8') as f:
                campos = ['idReporte', 'usuario_id', 'titulo', 'tipo', 'descripcion', 'fecha', 'prioridad', 'estado', 'foto1', 'foto2', 'foto3', 'nombre_reporta']
                writer = csv.DictWriter(f, fieldnames=campos)
                writer.writeheader()
                for r in self.reportes.values():
                    writer.writerow({
                        'idReporte': r.idReporte,
                        'usuario_id': r.usuario_id,
                        'titulo': r.titulo,
                        'tipo': r.tipo,
                        'descripcion': r.descripcion,
                        'fecha': r.fecha,
                        'prioridad': r.prioridad,
                        'estado': r.estado,
                        'foto1': r.foto1,
                        'foto2': r.foto2,
                        'foto3': r.foto3,
                        'nombre_reporta': r.nombre_reporta
                    })
            return True
        except Exception as e:
            print(f"Error al sincronizar reportes: {e}")
            return False

    #Gestión de usuarios
    def registroforAdmin(self, Username, contraseña, correo, tipoResidente="residente"):
        # Verificar duplicado de username
        for u in self.usuarios.values():
            if u.Username == Username and u.correo == correo:
                return "error_duplicado"

        ids = [int(u.idUsuario) for u in self.usuarios.values() if str(u.idUsuario).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)

        nuevo_usuario = Residente(
            tipoResidente  = tipoResidente,
            idUsuario      = nuevo_id,
            Username       = Username,
            contraseña     = contraseña,
            correo         = correo,
            nombre_completo= "",
            direccion      = "",
            telefono       = "",
            estado         = "pendiente",
        )
        self.usuarios[nuevo_id] = nuevo_usuario

        return "exito" if self.guardar_csv_nuevo() else "error_guardado"

    #Modificar datos
    def actualizarContraseña(self, Username, nueva_contraseña):
        for u in self.usuarios.values():
            if u.Username == Username:
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
    def registrar_consumo(self, cantidad, usuario_id, servicio_id, fecha=None, lectura_actual=0):
        ids = [int(c.idConsumo) for c in self.consumos.values() if str(c.idConsumo).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        c = Consumo(nuevo_id, float(cantidad), usuario_id, servicio_id, fecha, "pendiente", lectura_actual)
        self.consumos[nuevo_id] = c
        self.guardar_consumos_csv()
        return c

    def obtener_ultima_lectura(self, usuario_id, servicio_id):
        # Buscar el consumo más reciente para este par usuario-servicio con comparación robusta
        u_id_str = str(usuario_id)
        s_id_str = str(servicio_id)
        c_list = [c for c in self.consumos.values() if str(c.usuario_id) == u_id_str and str(c.servicio_id) == s_id_str]
        
        if not c_list:
            return 0.0
        # Ordenar por ID asumiendo incrementalidad
        ultimo = max(c_list, key=lambda x: int(x.idConsumo))
        return float(getattr(ultimo, 'lectura_actual', 0.0))

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
    def generar_recibo(self, usuario_id, periodo, total, consumos_ids=None):
        ids = [int(r.idRecibo) for r in self.recibos.values() if str(r.idRecibo).isdigit()]
        nuevo_id = str(max(ids, default=0) + 1)
        
        # Vincular con el objeto usuario real si es posible
        user_obj = self.usuarios.get(usuario_id, usuario_id)
        r = Recibo(nuevo_id, user_obj, periodo)
        r.total_pagar = total
        
        if consumos_ids:
            r.consumos_ids = consumos_ids
            # Vincular objetos de consumo en memoria
            r.consumos = [self.consumos[cid] for cid in consumos_ids if cid in self.consumos]
            
        self.recibos[nuevo_id] = r
        self.guardar_recibos_csv()
        return r

    def pagar_recibo(self, id_recibo):
        if id_recibo in self.recibos:
            rec = self.recibos[id_recibo]
            rec.estado = "pagado"
            # También marcar sus consumos como pagados
            for c_id in getattr(rec, 'consumos_ids', []):
                if c_id in self.consumos:
                    self.consumos[c_id].estado = "pagado"
            
            # Si no tiene consumos_ids pero tiene consumos en memoria (por carga reciente)
            for c in rec.consumos:
                c.estado = "pagado"
                
            self.guardar_recibos_csv()
            self.guardar_consumos_csv()
            return True
        return False

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

    # Gestión de reportes
    def crear_reporte(self, usuario_id, titulo, tipo, descripcion, prioridad="Media", foto1="", foto2="", foto3="", nombre_reporta=""):
        import re
        # Extraer solo los números del ID (ej: #12A -> 12)
        ids = []
        for r in self.reportes.values():
            match = re.search(r'(\d+)', r.idReporte)
            if match:
                ids.append(int(match.group(1)))

        numeric_id = max(ids, default=0) + 1
        id_str = f"{numeric_id}A" # Genera 1A, 2A, etc.

        rep = Reporte(id_str, usuario_id, descripcion, titulo, tipo, prioridad, "Pendiente", foto1=foto1, foto2=foto2, foto3=foto3, nombre_reporta=nombre_reporta)
        self.reportes[id_str] = rep
        self.guardar_reportes_csv()
        return rep

    def editar_reporte_estado(self, idReporte, nuevo_estado):
        if idReporte in self.reportes:
            self.reportes[idReporte].estado = nuevo_estado
            self.guardar_reportes_csv()
            return True
        return False

    def eliminar_reporte(self, idReporte):
        if idReporte in self.reportes:
            del self.reportes[idReporte]
            self.guardar_reportes_csv()
            return True
        return False


class Casa:
    def __init__(self, idCasa, numero):
        self.idCasa     = idCasa
        self.numero     = numero
        self.propietario = ""
        self.inquilino   = ""

    def asignarPropietario(self, usuario_id, sistema=None):
        if sistema:
            if usuario_id not in sistema.usuarios:
                return False
        self.propietario = usuario_id
        if sistema:
            sistema.guardar_casas_csv()
        return True

    def asignarInquilino(self, usuario_id, sistema=None):
        if sistema:
            if usuario_id not in sistema.usuarios:
                return False
        self.inquilino = usuario_id
        if sistema:
            sistema.guardar_casas_csv()
        return True


class Servicio:
    def __init__(self, idServicio, nombre, tipo, tarifa):
        self.idServicio = idServicio
        self.nombre     = nombre
        self.tipo       = tipo
        self.tarifa     = tarifa

    def calcular_costo(self, cantidad):
        #Calcula el costo según la cantidad consumida y la tarifa del servicio.
        return cantidad * self.tarifa


class Consumo:
    def __init__(self, idConsumo, cantidad, usuario_id, servicio_id,
                 fecha=None, estado="pendiente", lectura_actual=0):
        self.idConsumo   = idConsumo
        self.cantidad    = cantidad
        self.usuario_id  = usuario_id
        self.servicio_id = servicio_id
        self.fecha       = fecha if fecha else datetime.now().strftime("%Y-%m-%d")
        self.estado      = estado
        self.lectura_actual = lectura_actual

    def total(self, sistema):
        #Calcula el total del consumo usando la tarifa del servicio asociado.
        if self.servicio_id in sistema.servicios:
            return sistema.servicios[self.servicio_id].calcular_costo(self.cantidad)
        return 0


class Recibo:
    def __init__(self, idRecibo, usuario, periodo=""):
        self.idRecibo    = idRecibo
        self.usuario     = usuario
        self.consumos    = []
        self.consumos_ids = []
        self.total_pagar = 0
        self.estado      = "pendiente"
        self.periodo     = periodo

    def agregar_consumo(self, consumo):
        self.consumos.append(consumo)

    def calcular_total(self, sistema):
        #Recalcula el total sumando todos los consumos vinculados al recibo.
        self.total_pagar = sum(c.total(sistema) for c in self.consumos)
        return self.total_pagar

    def pagar(self):
        #Marca el recibo como pagado.
        self.estado = "pagado"


class Pago:
    def __init__(self, idPago, recibo):
        self.idPago    = idPago
        self.recibo    = recibo
        self.fechaPago = datetime.now()
        self.estado    = "realizado"

    def proceso_pago(self):
        # Valida que el recibo esté pendiente, lo marca pagado y confirma el pago.
        # Retorna True si se procesó correctamente, False si ya estaba pagado.
        if self.recibo.estado == "pendiente":
            self.recibo.pagar()
            self.estado    = "realizado"
            self.fechaPago = datetime.now()
            return True
        # El recibo ya fue pagado anteriormente
        self.estado = "rechazado"
        return False


class Reporte:
    def __init__(self, idReporte, usuario_id, descripcion, titulo="", tipo="Mantenimiento", prioridad="Media", estado="Pendiente", fecha=None, foto1="", foto2="", foto3="", nombre_reporta=""):
        self.idReporte   = idReporte
        self.usuario_id  = usuario_id
        self.nombre_reporta = nombre_reporta
        self.titulo      = titulo if titulo else f"{tipo} #{idReporte}"
        self.tipo        = tipo
        self.descripcion = descripcion
        self.prioridad   = prioridad
        self.estado      = estado
        self.fecha       = fecha if fecha else datetime.now().strftime("%Y-%m-%d")
        self.foto1       = foto1
        self.foto2       = foto2
        self.foto3       = foto3

    def generarReporte(self):
        return {
            "idReporte":   self.idReporte,
            "titulo":      self.titulo,
            "tipo":        self.tipo,
            "descripcion": self.descripcion,
            "usuario_id":  self.usuario_id,
            "prioridad":   self.prioridad,
            "estado":      self.estado,
            "fecha":       self.fecha,
            "foto1":       self.foto1,
            "foto2":       self.foto2,
            "foto3":       self.foto3,
            "nombre_reporta": self.nombre_reporta
        }
