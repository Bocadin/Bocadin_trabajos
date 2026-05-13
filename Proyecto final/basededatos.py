import csv
import os

base_direccion = os.path.dirname(os.path.abspath(__file__))

def crear_archivo(nombre, encabezados):
    ruta = os.path.join(base_direccion, nombre)

    if not os.path.exists(ruta):
        with open(ruta, mode='w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(encabezados)

        print(f"{ruta} creado.")

    else:
        print(f"{ruta} ya existe.")


def crear_base_csv():

    # Usuarios
    crear_archivo("usuarios.csv", [
        "idUsuario",
        "Username",
        "contraseña",
        "tipoUsuario",
        "correo",
        "nombre_completo",
        "direccion",
        "telefono",
        "estado",
        "foto_perfil"
    ])

    # Casas
    crear_archivo("casas.csv", [
        "idCasa",
        "numero",
        "propietario_id",
        "inquilino_id"
    ])

    # Servicios
    crear_archivo("servicios.csv", [
        "idServicio",
        "nombre",
        "tipo",
        "tarifa"
    ])

    # Consumos
    crear_archivo("consumos.csv", [
        "idConsumo",
        "cantidad",
        "fecha",
        "servicio_id",
        "usuario_id",
        "estado"
    ])

    # Recibos
    crear_archivo("recibos.csv", [
        "idRecibo",
        "usuario_id",
        "total",
        "estado",
        "periodo"
    ])

    # Reportes — encabezados alineados con guardar_reportes_csv() del backend
    crear_archivo("reportes.csv", [
        "idReporte",
        "usuario_id",
        "titulo",
        "tipo",
        "descripcion",
        "fecha",
        "prioridad",
        "estado"
    ])


if __name__ == "__main__":
    crear_base_csv()