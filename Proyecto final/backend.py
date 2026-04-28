import csv
import os
from datetime import datetime

class Usuario:
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
        try:
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
        except Exception as e:
            print(f"Error al cargar usuarios desde el archivo: {e}")

    def registrarUsuario(self, nombre, tipoUsuario, contraseña):

        # Validación de duplicidad para evitar registros repetidos
        for u in self.usuarios.values():
            if u.nombre == nombre:
                print(f"Registro fallido: El usuario '{nombre}' ya existe.")
                return None

# Generación de ID
        nuevo_id = str(len(self.usuarios) + 1)
        usuario = Usuario(nuevo_id, nombre, contraseña, tipoUsuario)
        self.usuarios[nuevo_id] = usuario

# Persistencia en archivo csv
        archivoExiste = os.path.exists(self.archivo_usuarios)
        with open(self.archivo_usuarios, mode='a', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)

# Verificacion de integridad
            if not archivoExiste or os.stat(self.archivo_usuarios).st_size == 0:
                writer.writerow(['idUsuario', 'nombre', 'tipoUsuario', 'contraseña'])
            writer.writerow([nuevo_id, nombre, tipoUsuario, contraseña])

        print(f"Usuario {nombre} registrado con éxito en el sistema.")
        return usuario

    def guardar_csv_nuevo(self):
        try:
            with open(self.archivo_usuarios, mode='w', newline='', encoding='utf-8') as archivo:
 
                campos = ['idUsuario', 'nombre', 'tipoUsuario', 'contraseña']
                writer = csv.DictWriter(archivo, fieldnames=campos)
                
# Escritura de encabezados y datos desde la memoria ram
                writer.writeheader()
                for u in self.usuarios.values():
                    writer.writerow({
                        'idUsuario': u.idUsuario,
                        'nombre': u.nombre,
                        'tipoUsuario': u.tipoUsuario,
                        'contraseña': u.contraseña
                    })
            return True
        except Exception as e:
            print(f"Error al sincronizar base de datos: {e}")
            return False

# Actuzlizacion de contraseña
    def actualizarContraseña(self, nombre_usuario, nueva_contraseña):
        usuario_encontrado = False
        
# Iteración sobre los usuarios cargados
        for u in self.usuarios.values():
            if u.nombre == nombre_usuario:
# Actualización del atributo en el objeto
                u.contraseña = nueva_contraseña
                usuario_encontrado = True
                break
        
# Si hubo un cambio exitoso, reescribimos el archivo csv
        if usuario_encontrado:
            return self.guardar_csv_nuevo()
        
        print("El usuario no fue localizado para el cambio de clave.")
        return False
# Fin de funciiom agrega

    def eliminarUsuario(self, idUsuario):
        if idUsuario in self.usuarios:
            del self.usuarios[idUsuario]
            self.guardar_csv_nuevo()
            print(f"Usuario con ID {idUsuario} ha sido removido.")
        else:
            print("El ID proporcionado no coincide con ningún usuario activo.")

    def autenticar(self, nombre, contraseña):
        for usuario in self.usuarios.values():
            if usuario.nombre == nombre and usuario.contraseña == contraseña:
                return usuario
        return None

    def iniciar_sesion(self, nombre, contraseña):
        usuario = self.autenticar(nombre, contraseña)
        if usuario:
            print(f"Acceso concedido: Bienvenido {usuario.nombre} ({usuario.tipoUsuario})")
            return usuario
        else:
            print("Acceso denegado: Credenciales inválidas.")
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