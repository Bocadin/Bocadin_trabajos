from models import *


print("\n""----Biblioteca Smart----""\n")
mat1= Material(1244556, "El principito", 1943, True)
mat2 = Material(1244557, "Crónica de una muerte anunciada", 1981, True)
mat3 = Material(1244558, "Fahrenheit 451", 1953, False)
mat4 = Material(1244559, "El Aleph", 1949, True)
mat5 = Material(1244560, "La ciudad y los perros", 1963, True)
mat6 = Material(1244561, "Ensayo sobre la ceguera", 1995, False)
mat7 = Material(1244562, "Rayuela", 1963, True)
mat8 = Material(1244563, "Drácula", 1897, True)
mat9 = Material(1244564, "Moby Dick", 1851, False)
mat10 = Material(1244565, "Frankenstein", 1818, True)


#mat1.actualizarDisponibilidad()
#print("\n")
#mat1.obtenerDetalles()


book1= Libro( "Dan Brown", "1894826136785", "Thriller", 1731183, "Inferno", 2013, True )
book2 = Libro("Gabriel García Márquez", "9780307474728", "Realismo Mágico", 1731184, "Cien años de soledad", 1967, True)
book3 = Libro("George Orwell", "9780451524935", "Distopía", 1731185, "1984", 1949, False)
book4 = Libro("J.K. Rowling", "9780747532743", "Fantasía", 1731186, "Harry Potter y la piedra filosofal", 1997, True)
book5 = Libro("Isabel Allende", "97800608", "Ficción Histórica", 1731187, "La casa de los espíritus", 1982, True)
book6 = Libro("Frank Herbert", "9780441172719", "Ciencia Ficción", 1731188, "Dune", 1965, False)
book7 = Libro("Stephen King", "9781501142970", "Terror", 1731189, "It (Eso)", 1986, True)
book8 = Libro("Antoine", "9780156012195", "Infantil", 1731190, "El Principito", 1943, True)
book9 = Libro("Agatha Christie", "9780062073402", "Misterio", 1731191, "Asesinato en el Orient Express", 1934, True)
book10 = Libro("Ernest Hemingway", "978068480", "Aventura", 1731192, "El viejo y el mar", 1952, False)

#book6.validarISBN()
#print("\n")
#book5.validarISBN()
#print("\n")
#book3.consultarAutor()


revist1= Revista(90, "Mensual", 18938490, "Algarabia", 2025, True )
revist2 = Revista(145, "Mensual", 18938491, "National Geographic", 2024, True)
revist3 = Revista(52, "Semanal", 18938492, "Time Magazine", 2024, True)
revist4 = Revista(12, "Anual", 18938493, "Resumen Científico", 2023, False)
revist5 = Revista(305, "Mensual", 18938494, "Muy Interesante", 2025, True)
revist6 = Revista(88, "Bimestral", 18938495, "Diseño Interior", 2024, True)
revist7 = Revista(15, "Semanal", 18938496, "The Economist", 2025, False)
revist8 = Revista(201, "Mensual", 18938497, "Vogue", 2024, True)
revist9 = Revista(45, "Trimestral", 18938498, "Arqueología Mexicana", 2023, True)
revist10 = Revista(10, "Semanal", 18938499, "Proceso", 2025, True)

#revist1.obtenerEdicion()
#print("\n")
#revist1.obtenerPeriodicidad()


digi1 = MaterialDigital("PDF", "https://bit.ly/python-basico", 15.5, 300121, "Guía de Python 3", 2024, True)
digi2 = MaterialDigital("EPUB", "https://bit.ly/limpio-codigo", 4.2, 300231, "Código Limpio", 2008, True)
digi3 = MaterialDigital("PDF", "https://bit.ly/ia-futuro", 22.1, 300311, "Inteligencia Artificial", 2025, True)
digi4 = MaterialDigital("MP4", "https://bit.ly/curso-git", 450.0, 307485, "Video Curso Git & GitHub", 2023, True)
digi5 = MaterialDigital("PDF", "https://bit.ly/diseno-patrones", 18.3, 304635, "Patrones de Diseño", 1994, True)
digi6 = MaterialDigital("EPUB", "https://bit.ly/algoritmos-v3", 6.8, 30474, "Algoritmos Avanzados", 2022, True)
digi7 = MaterialDigital("PDF", "https://bit.ly/redes-cisco", 35.5, 3007377, "Fundamentos de Redes", 2024, True)
digi8 = MaterialDigital("MP4", "https://bit.ly/taller-docker", 310.0, 335735, "Workshop Docker Express", 2025, True)
digi9 = MaterialDigital("PDF", "https://bit.ly/sql-expert", 12.4, 305735, "SQL para Expertos", 2021, True)
digi10 = MaterialDigital("EPUB", "https://bit.ly/web-react", 5.9, 3035623, "React.js Moderno", 2024, True)


#digi10.descargar()
#print("\n")
#digi10.generarLink()

per1= Persona(1738393, "Jetro", "jet@gmail.com")
per2= Persona (17389494, "Enisha", "Enis@gmail.com")
per3 = Persona(17389495, "Dante", "dante.al@gmail.com")
per4 = Persona(17389496, "Valeria", "val.rios@gmail.com")
per5 = Persona(17389497, "Julian", "july_99@hotmail.com")
per6 = Persona(17389498, "Beatriz", "bea.tris@outlook.com")
per7 = Persona(17389499, "Marcos", "m.perez@gmail.com")
per8 = Persona(17389500, "Elena", "ele.na88@yahoo.com")
per9 = Persona(17389501, "Samuel", "sam_pro@gmail.com")
per10 = Persona(17389502, "Fiona", "fiona_sky@gmail.com")

#per1.log_in("Jetro", "jet@gmail.com")
#print("\n")
#per1.actualizar_perfil("Jet", "jet@gmail.com")
#print("\n")
#Prueba 2
#per1.log_in("Jety", "jet@gmail.com")


usu1= Usuario(13, 124465, "Alice", "al@hjgmail.com")
usu2 = Usuario(13, 556677, "Mateo", "m.espinosa@outlook.com")
usu3 = Usuario(13, 882233, "Saori", "s.tanaka@workmail.jp")
usu4 = Usuario(13, 449911, "Thiago", "thiago.silva@brasil.br")
usu5 = Usuario(13, 773300, "Amira", "amira.h@global.net")
usu6 = Usuario(13, 225588, "Lukas", "l.muller@berlin.de")
usu7 = Usuario(13, 991144, "Ximena ", "xortiz@universidad.edu")
usu8 = Usuario(13, 336699, "Kofi ", "kmensah@accra.gh")
usu9 = Usuario(13, 660022, "Svetlana ", "s.ivanko@mail.ru")
usu10 = Usuario(13, 114477, "Chen ", "wei.chen@tech.cn")

#usu1.consultarDisponibilidad(book1)
#print("\n")
#usu9.solicitarPrestamo(book1)
#print("\n")
#usu2.consultarDisponibilidad(book3)

biblio1= Bibliotecario(12243545, 2312441, "Juan Carlos", "juanw@gmail.com")
biblio2 = Bibliotecario(12243546, 2312442, "Tulio", "tulio.triv@biblioteca.com")
biblio3 = Bibliotecario(12243547, 2312443, "Juanín", "juanin.j@correo.cl")
biblio4 = Bibliotecario(12243548, 2312444, "Guaripolo", "guaripolo_favorito@oficina.com")
biblio5 = Bibliotecario(12243549, 2312445, "Patana", "patana.t@prensa.cl")
biblio6 = Bibliotecario(12243550, 2312446, "Mario Hugo", "mhugo.perros@mascotas.com")
biblio7 = Bibliotecario(12243551, 2312447, "Policarpo", "policarpo.top@ranking.cl")
biblio8 = Bibliotecario(12243552, 2312448, "Mico el Micófono", "mico.mic@entrevistas.com")
biblio9 = Bibliotecario(12243553, 2312449, "Huachimingo", "huachi.coleccion@peluches.cl")
biblio10 = Bibliotecario(12243554, 2312450, "Calcetín", "calcetin.rombos@heroes.com")

#store1.actualizarCatalogo(book1)
#print("\n")
#store1.verificarStock(book1)

#biblio10.gestionarPrestamo("Julian", book2, 13124252)
#print("\n")
#biblio10.gestionarPrestamo(usu5, book2, 13124252)
#print("\n")
#biblio10.transferirMaterial(book1,store1, store3)

store1= Sucursal(137484, "Biblioteca del norte")
store2 =  Sucursal(137485, "Sede Central Histórica")
store3 =  Sucursal(137486, "Biblioteca del Sur ")
store4 =  Sucursal(137487, "Sucursal Oriente - Parque")
store5 =  Sucursal(137488, "Biblio-Tec Poniente")
store6 =  Sucursal(137489, "Sede Digital Metropolitana")
store7 =  Sucursal(137490, "Biblioteca Infantil Los Pinos")
store8 =  Sucursal(137491, "Sucursal Universitaria")
store9 =  Sucursal(137492, "Estación Cultural del Este")
store10 = Sucursal(137493, "Biblio-Móvil Itinerante")

#store1.actualizarCatalogo(book10)
#print("\n")
#store1.verificarStock(book10)


presta1= Prestamo(1283873, usu3, book3, datetime.now(), datetime.now() + timedelta(days=7))
presta2 = Prestamo(1283874, usu1, book1, datetime.now(), datetime.now() + timedelta(days=-20))
presta3 = Prestamo(1283875, usu2, digi3, datetime.now(), datetime.now() + timedelta(days=7))
presta4 = Prestamo(1283876, usu4, revist1, datetime.now(), datetime.now() + timedelta(days=5))
presta5 = Prestamo(1283877, usu5, mat8, datetime.now(), datetime.now() + timedelta(days=7))
presta6 = Prestamo(1283878, usu6, revist2, datetime.now(), datetime.now() + timedelta(days=5))
presta7 = Prestamo(1283879, usu7, book5, datetime.now(), datetime.now() + timedelta(days=7))
presta8 = Prestamo(1283880, usu8, revist3, datetime.now(), datetime.now() + timedelta(days=5))
presta9 = Prestamo(1283881, usu9, digi4, datetime.now(), datetime.now() + timedelta(days=7))
presta10 = Prestamo(1283882, usu10, mat2, datetime.now(), datetime.now() + timedelta(days=7))


#presta1.finalizarPrestamo()
#print("\n")
#presta1.estaVencido()

pena1 = Penalizacion(0, "Sin motivo", False)
pena2 = Penalizacion(50, "Retraso de 5 días", True)
pena3 = Penalizacion(10, "Retraso de 1 día", True)
pena4 = Penalizacion(20, "Retraso de 2 días", False)
pena5 = Penalizacion(30, "Retraso de 3 días", False)
pena6 = Penalizacion(70, "Retraso de 7 días", True)
pena7 = Penalizacion(100, "Retraso de 10 días", False)
pena8 = Penalizacion(150, "Retraso de 15 días", False)
pena9 = Penalizacion(40, "Retraso de 4 días", True)
pena10 = Penalizacion(300, "Retraso de 30 días", False) 


#pena10.calcularMulta(presta2)
#print("\n")
#pena10.bloquearUsuario(usu4)
#print("\n")
#pena7.calcularMulta(presta2)


cata1= Catalogo()

#store1.actualizarCatalogo(book1)


#cata1.agregarMaterial(book1)
##print("\n")
#cata1.buscarPorAutor("Dan Brown")
#print("\n")
#cata1.buscarEnSucursales(book1, store1)






#biblio1.log_in("Juan Carlos", "juanw@gmail.com")
#per1.log_in("Jetro", "jet@gmail.com")


# 1. Creamos las Sucursales
sucursal_norte = Sucursal(101, "Sede Norte")
sucursal_sur = Sucursal(102, "Sede Sur")

# 2. Creamos el Material (Libros, Revistas, Digital)
libro1 = Libro("Gabriel García Márquez", "9780307474728", "Realismo Mágico", 1, "Cien Años de Soledad", 1967, True)
revista1 = Revista("Edición Especial AI", "Mensual", 2, "Tech World", 2024, True)
digital1 = MaterialDigital("PDF", "https://biblioteca.com/download/python101", 15, 3, "Python Básico", 2023, True)

# 3. Registramos material en las sucursales y en el catálogo general
catalogo_general = Catalogo()
catalogo_general.agregarMaterial(libro1)
catalogo_general.agregarMaterial(revista1)
catalogo_general.agregarMaterial(digital1)

sucursal_norte.actualizarCatalogo(libro1)
sucursal_norte.actualizarCatalogo(revista1)
sucursal_sur.actualizarCatalogo(digital1)

# 4. Creamos al Personal y Usuarios
bibliotecario_pepe = Bibliotecario("EMP001", 50, "Pepe Perez", "pepe@biblioteca.com")
usuario_ana = Usuario(3, 200, "Ana Lopez", "ana@correo.com")

# --- INICIO DEL RETO / FLUJO DE PRUEBA ---

print("--- 1. INICIO DE SESIÓN ---")
bibliotecario_pepe.log_in("Pepe Perez", "pepe@biblioteca.com")

print("\n--- 2. BÚSQUEDA Y DISPONIBILIDAD ---")
catalogo_general.buscarPorAutor("Gabriel García Márquez")
usuario_ana.consultarDisponibilidad(libro1)

print("\n--- 3. GESTIÓN DE PRÉSTAMO ---")
# Pepe gestiona el préstamo de 'Cien Años de Soledad' para Ana
bibliotecario_pepe.gestionarPrestamo(usuario_ana, libro1, "P-001")

print("\n--- 4. INTENTO DE DESCARGA DIGITAL ---")
digital1.descargar()

print("\n--- 5. TRANSFERENCIA ENTRE SUCURSALES ---")
# Intentamos mover la revista de Norte a Sur
bibliotecario_pepe.transferirMaterial(revista1, sucursal_norte, sucursal_sur)

print("\n--- 6. VERIFICACIÓN DE VENCIMIENTO Y MULTA ---")
# Vamos a simular que el préstamo de Ana se venció (manipulando la fecha manualmente para la prueba)
prestamo_ana = usuario_ana.listaActiva[0]
prestamo_ana.fechaDevolucion = datetime.now() - timedelta(days=5) # Venció hace 5 días

multa = Penalizacion(0, "", False)
multa.calcularMulta(prestamo_ana)
multa.bloquearUsuario(usuario_ana)

print("\n--- 7. FINALIZACIÓN Y DEVOLUCIÓN ---")
prestamo_ana.finalizarPrestamo()

