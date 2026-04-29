import csv
import os

base_direccion = os.path.dirname(__file__)

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
    
    crear_archivo("usuarios.csv", [
        "idUsuario", "nombre", "tipoUsuario", "contraseña"
    ])

    crear_archivo("casas.csv", [
        "idCasa", "numero", "propietario_id", "inquilino_id"
    ])

    crear_archivo("servicios.csv", [
        "idServicio", "nombre", "tipo", "tarifa"
    ])

    crear_archivo("consumos.csv", [
        "idConsumo", "cantidad", "fecha", "servicio_id", "casa_id"
    ])

    crear_archivo("recibos.csv", [
        "idRecibo", "usuario_id", "total", "estado"
    ])

    crear_archivo("reportes.csv", [
        "idReporte", "usuario_id", "descripcion", "fecha"
    ])


if __name__ == "__main__":
    crear_base_csv()