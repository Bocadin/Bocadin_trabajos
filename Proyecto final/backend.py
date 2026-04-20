import csv
import os
from datetime import datetime

class Usuario ():
    def __init__(self, idUsuario, nombre, contraseña, tipoUsuario):
        self.idUsuario = idUsuario
        self.nombre = nombre 
        self.contraseña = contraseña 
        self.tipoUsuario = tipoUsuario

    def iniciarSesion():
        pass

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