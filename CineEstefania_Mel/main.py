from models import *
from datetime import datetime, timedelta


print("\n""----RANITAS CINE----""\n")
per1=Persona (1234565, "Jetro", "jetc123@gmail.com", 85945621)
per2=Persona (1637849, "Kyle", "ki2122@gmail.com", 273494858)
per3=Persona (1783939, "Carmen", "ajcc@gmacil.com", 1734947459)
per4=Persona (1928374, "Luis", "luis98@gmail.com", 28374655)
per5=Persona (2039485, "Ana", "ana_21@gmail.com", 39847566)
per6=Persona (2147596, "Pedro", "pedro77@gmail.com", 48756321)
per7=Persona (2258607, "Maria", "maria.lopez@gmail.com", 56473829)
per8=Persona (2369718, "Jorge", "jorge_dev@gmail.com", 67584930)
per9=Persona (2470829, "Sofia", "sofia23@gmail.com", 78695041)
per10=Persona (2581930, "Kenny", "rkennyo89@gmail.com", 89706152)


usua1= Usuario(15, [], 1234565, "Jetro", "jetc123@gmail.com", 85945621 )
usua2= Usuario(10, [], 1637849, "Kyle", "ki2122@gmail.com", 273494858)
usua3= Usuario(5, [], 1783939, "Carmen", "ajcc@gmacil.com", 1734947459)
usua4 = Usuario(20, [], 1928374, "Luis", "luis98@gmail.com", 28374655)
usua5 = Usuario(0,  [], 2039485, "Ana", "ana_21@gmail.com", 39847566)
usua6 = Usuario(12, [], 2147596, "Pedro", "pedro77@gmail.com", 48756321)
usua7 = Usuario(30, [], 2258607, "Maria", "maria.lopez@gmail.com", 56473829)
usua8 = Usuario(8,  [], 2369718, "Jorge", "jorge_dev@gmail.com", 67584930)
usua9 = Usuario(15, [], 2470829, "Sofia", "sofia23@gmail.com", 78695041)
usua10 = Usuario(50, [], 2581930, "Kenny", "rkennyo89@gmail.com", 89706152)

emple1= Empleado(1243342424 , "ADMIN", "08:00", 312135351, "Laura", "admin@email.com", 5555555)
emple2= Empleado(132141241, "TAQUILLERO", "09:00", 34134133, "Paola", "aplapal@gmail.com", 18193947 )
emple3 = Empleado(132141243, "LIMPIEZA", "07:00", 34134134, "Carlos", "carlos@cine.com", 2837461)
emple4 = Empleado(132141244, "LIMPIEZA", "15:00", 34134135, "Marta", "marta@cine.com", 2837462)
emple5 = Empleado(132141245, "ADMIN", "23:00", 34134136, "Juana", "Juana_limp@cine.com", 2837463)
emple6 = Empleado(132141246, "TAQUILLERO", "14:00", 34134137, "Elena", "elena@cine.com", 2837464)
emple7 = Empleado(132141247, "TAQUILLERO", "18:00", 34134138, "Roberto", "robert@cine.com", 2837465)
emple8 = Empleado(132141248, "ADMIN", "14:00", 34134139, "Sergio", "sergio_admin@cine.com", 2837466)
emple9 = Empleado(132141249, "ADMIN", "22:00", 34134140, "Ana", "ana_gerencia@cine.com", 2837467)
emple10 = Empleado(132141250, "LIMPIEZA", "10:00", 34134141, "Luquitas", "luc189_l@cine.com", 2837468)

espa1= Espacio(123455, "Sala 1", "Primer piso", False)
espa2= Espacio(181939, "Sala 2", "Primer piso", True )
espa3= Espacio(177365, "Sala 3", "Primer piso", True)
espa4 = Espacio(192837, "Sala 4", "Primer piso", True)
espa5 = Espacio(203948, "Sala 5", "Primer piso", False)
espa6 = Espacio(214759, "Sala 6", "Segundo piso", True)
espa7 = Espacio(225860, "Sala 7", "Segundo piso", False)
espa8 = Espacio(236971, "Sala 8", "Segundo piso", False)
espa9 = Espacio(247082, "Sala 9", "Segundo piso", True)
espa10 = Espacio(258193, "Sala 10", "Segundo piso", True)

sal1= Sala( "SALA_2D", 50, True, 123455, "Sala 1", "Primer piso", False)
sal2= Sala( "SALA_3D", 45, False, 181939, "Sala 2", "Primer piso", True )
sal3= Sala( "SALA_IMAX", 30, False, 177365, "Sala 3", "Primer piso", True)
sal4 = Sala("SALA_2D", 40, False, 192837, "Sala 4", "Primer piso", True)
sal5 = Sala("SALA_3D", 35, True, 203948, "Sala 5", "Primer piso", False)
sal6 = Sala("SALA_IMAX", 50, True, 214759, "Sala 6", "Segundo piso", True)
sal7 = Sala("SALA_2D", 45, False, 225860, "Sala 7", "Segundo piso", False)
sal8 = Sala("SALA_3D", 40, False, 236971, "Sala 8", "Segundo piso", False)
sal9 = Sala("SALA_IMAX", 30, True, 247082, "Sala 9", "Segundo piso", True)
sal10 = Sala("SALA_2D", 50, True, 258193, "Sala 10", "Segundo piso", True)

zonafood= ZonaComida(123455, "Sala 1", "Primer piso", False)

pel1= Pelicula( "Spiderman 1", 120, "Accion")
pel2=Pelicula("It", 120, "Terror")
pel3 = Pelicula("Seven", 127, "thriller")
pel4 = Pelicula("Cars", 117, "Animacion") 
pel5 = Pelicula("Bajos Instintos", 128, "cine erotico")
pel6 = Pelicula("Frozen", 102, "Fantasia") 
pel7 = Pelicula("Toy Story", 81, "Animacion")
pel8 = Pelicula("Interestelar", 169, "Ciencia Ficcion")
pel9 = Pelicula("La La Land", 128, "Musical")
pel10 = Pelicula("Shrek", 90, "Comedia")


fun1 = Funcion(12234511, pel1, sal1, "14:00", 60)
fun2 = Funcion(12234512, pel2, sal2, "15:30", 65)
fun3 = Funcion(12234513, pel3, sal3, "17:00", 70)
fun4 = Funcion(12234514, pel4, sal4, "18:30", 60)
fun5 = Funcion(12234515, pel5, sal5, "20:00", 75)
fun6 = Funcion(12234516, pel6, sal6, "14:00", 80)
fun7 = Funcion(12234517, pel7, sal7, "16:15", 55)
fun8 = Funcion(12234518, pel8, sal8, "19:00", 60)
fun9 = Funcion(12234519, pel9, sal9, "21:30", 80)
fun10 = Funcion(12234520, pel10, sal10, "22:00", 60)

prom1=Promocion("PROMO1", "Descuento por fidelidad", 15, datetime(2026, 12, 31))
prom2= Promocion("PROMO2", "Descuento por aniversario para todos", 10, datetime(2026, 4, 15))
prom3= Promocion("PROMO3", "Descuento del dia de amor y la amistad", 10, datetime(2026, 2, 16))
prom4 = Promocion("PROMO4", "Especial de Semana Santa", 20, datetime(2026, 4, 5))
prom5 = Promocion("PROMO5", "Promoción Día del Niño, solo para niños de 1-14 años", 25, datetime(2026, 4, 30))
prom6 = Promocion("PROMO6", "Descuento Vacaciones de Verano", 15, datetime(2026, 7, 15))
prom7 = Promocion("PROMO7", "Promo Fiestas Patrias", 10, datetime(2026, 9, 16))
prom8 = Promocion("PROMO8", "Especial de Halloween solo para clientes con disfraz", 13, datetime(2026, 10, 31))
prom9 = Promocion("PROMO9", "Black Friday Cine", 50, datetime(2026, 11, 27))
prom10 = Promocion("PROMO10", "Regalo de Navidad", 30, datetime(2026, 12, 25))


reserv1= Reserva(112413513, usua1, fun1, ["A1", "A2"], 120, "PENDIENTE")
reserv2 = Reserva(112413514, usua2, fun2, ["B5"], 65, "PAGADA")           
reserv3 = Reserva(112413515, usua3, fun3, ["C1", "C2", "C3"], 210, "PENDIENTE") 
reserv4 = Reserva(112413516, usua4, fun4, ["D10", "D11"], 120, "PAGADA")   
reserv5 = Reserva(112413517, usua5, fun5, ["A1"], 75, "PAGADA")            
reserv6 = Reserva(112413518, usua6, fun6, ["F1", "F2"], 160, "PAGADA")     
reserv7 = Reserva(112413519, usua7, fun7, ["G4", "G5", "G6"], 165, "PENDIENTE") 
reserv8 = Reserva(112413520, usua8, fun8, ["H1"], 60, "PAGADA")            
reserv9 = Reserva(112413521, usua9, fun9, ["J12", "J13"], 160, "PAGADA")  
reserv10 = Reserva(112413522, usua10, fun10, ["K1"], 60, "PENDIENTE")   


print("\n""----Personas de RANITAS CINE----""\n")
per1.log_in("Jetro", "jetc123@gmail.com" )
per1.log_out()
per1.actualizar_datos("Jet1", "jety@gmail.com")

print("--Usuario2---""\n")
per2.log_in("Sara", "sarmmm@gmail.com")
per2.log_out()
per2.actualizar_datos("Kylee22", "k1mmh@gmail.com""\n")

print("--Usuario3---""\n")
per3.log_in("Carmen", "ajcc@gmacil.com")
per3.log_out()
per3.actualizar_datos("Carmen12", "carmen12@gmail.com""\n")
print("--Usuario4---""\n")


print("\n""----Usuarios de RANITAS CINE----""\n")
usua1.crearReserva(fun2,2 )
usua1.cancelar_reserva(fun2)

usua2.crearReserva(fun4, 1)
usua2.cancelar_reserva(fun3)

usua4.crearReserva(fun6,3)
usua6.crearReserva(fun1, 4)

print("\n""----Empleados de RANITAS CINE----""\n")
emple1.marcaEntrada()
emple1.gestionarFunciones()
emple1.agregar_funcion(fun1)
emple1.modificar_promocion(prom1, 10, "Descuento por fidelidad depues de 3 meses")

emple10.marcaEntrada()
emple10.gestionarFunciones()

emple2.marcaEntrada()
emple2.gestionarFunciones()


print("\n""----Espacios de RANITAS CINE----""\n")
espa1.verificarDisponibilidad()
espa1.limpiarEspacio()
espa1.verificarDisponibilidad()
print("\n")
espa2.verificarDisponibilidad()

print("\n""----Salas de RANITAS CINE----""\n")
sal1.ajustarAforo(45)
sal1.obtenerTipoSala()
print("\n")
sal5.ajustarAforo(60)
sal5.obtenerTipoSala()

print("\n""----Zona de comida de RANITAS CINE----""\n")
zonafood.actualizar_Inventario("Palomitas", 100)
zonafood.actualizar_Inventario("Refrescos", 50)
zonafood.actualizar_Inventario("Hot Dogs", 40)
zonafood.actualizar_Inventario("Nachos", 60)
zonafood.actualizar_Inventario("Chocolates", 80)
zonafood.actualizar_Inventario("Gomitas", 75)
zonafood.actualizar_Inventario("Icee", 30)
zonafood.actualizar_Inventario("Papas Fritas", 45)
zonafood.actualizar_Inventario("Dulces de Leche", 25)
zonafood.actualizar_Inventario("Agua Embotellada", 100)
print("\n")
zonafood.venderProducto("Palomitas", 2)
zonafood.venderProducto("Nachos", 70)


print("\n""----Peliculas de RANITAS CINE----""\n")
pel1.obtener_Sinopsis("La historia de un hombre que se combierte en un hombre con poderes de araña")
print("\n")
pel1.esAptaParaTodoPublico()
print("\n")

print("\n""----Funciones de RANITAS CINE----""\n")
fun1.calcularAsientosLibres()
print("\n")
fun1.obtenerDetallesFuncion()


print("\n""----Reservas de RANITAS CINE----""\n")
reserv1.confirmarPago()
reserv2.confirmarPago()
print("\n")
reserv1.generarTicket()
print("\n")
reserv1.aplicarPromocion(prom2)



print("\n""----Promos de RANITAS CINE----""\n")
prom1.esValida(usua1)
prom4.esValida(usua3)
print("\n")
prom1.aplicarDescuento(120)
prom4.aplicarDescuento(120)





print("\n---- RETO 1: RESERVAR MULTIPLES ASIENTOS ----\n")
reserv1.generarTicket()
reserv3.generarTicket()
reserv7.generarTicket()

print("\n")


print("---RETO 2---")
fun1.calcularAsientosLibres()
fun3.calcularAsientosLibres()
fun7.calcularAsientosLibres()

print("\nUsuario intenta reservar más asientos\n")
usua1.crearReserva(fun1, 3)
fun1.calcularAsientosLibres()
print("\n")


print("---RETO 3---")
emple1.agregar_funcion(fun1)
emple5.agregar_funcion(fun5)
emple8.agregar_funcion(fun8)
print("\n---- APLICAR PROMOCION ----\n")
reserv1.aplicarPromocion(prom1)
reserv7.aplicarPromocion(prom6)
print("\n")