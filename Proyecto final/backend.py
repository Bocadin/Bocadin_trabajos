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
        self.archivo_usuarios = os.path.join(os.path.dirname(__file__), "usuarios.csv")
        self.usuarios = {}
        self._cargar_usuarios()
        
    def _cargar_usuarios(self):
        if not os.path.exists(self.archivo_usuarios):
            print(f"\nEl archivo {self.archivo_usuarios} no existe. Se creará al registrar usuarios.")
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
        self.propietario = Usuario
        self.inquilino = Usuario

class Servicio():
    def __init__(self, idServicio, nombre, tipo, tarifa):
        self.idServicio = idServicio
        self.nombre = nombre
        self.tipo = tipo
        self.tarifa = tarifa

    def calcular_costo(self, cantidad):
        return cantidad * self.tarifa

class Consumo():
    def __init__(self, idConsumo, tipoConsumo, cantidad, casa, servicio):
        self.idConsumo = idConsumo
        self.tipoConsumo = tipoConsumo
        self.cantidad = cantidad
        self.fecha = datetime.now()
        self.casa = casa
        self.servicio = servicio

    def calcular_total(self):
        return self.servicio.calcular_costo(self.cantidad)

class Recibo():
    def __init__(self, idRecibo, usuario, casa):
        self.idRecibo = idRecibo
        self.usuario = usuario
        self.casa = casa
        self.consumos = []
        self.total = 0
        self.fecha = datetime.now()
        self.estado = "pendiente"

    def agregar_consumo(self, consumo):
        self.consumos.append(consumo)

    def calcular_total(self):
        self.total = sum(c.calcular_total() for c in self.consumos)
        return self.total

    def marcar_pagado(self):
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
        self.fechaReporte = datetime.now()