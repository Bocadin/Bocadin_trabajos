from models import *

print(f"---Monito's cafe---""\n")

per1= Persona(177398, "Felix", "fe@lixgmail.com")
per2=Persona (167484, "María", "mar1@gmail.com")
per3 = Persona(198234, "Carlos", "carlos@gmail.com")
per4 = Persona(145672, "Ana", "ana@gmail.com")
per5 = Persona(176543, "Luis", "luis@gmail.com")
per6 = Persona(189345, "Sofía", "sofia@gmail.com")
per7 = Persona(154789, "Diego", "diego@gmail.com")
per8 = Persona(167890, "Elena", "elena@gmail.com")
per9 = Persona(190234, "Jorge", "jorge@gmail.com")
per10 = Persona(178456, "Lucía", "lucia@gmail.com")

#per5.log_in("Luis", "luis@gmail.com")
#per5.actualizar_perfil("Luiz11", "Lu11ma@gmail.com")

pedido1= Pedido(127374, 50.00, "PREPARANDO")
pedido2 = Pedido(127375, 120.50, "ENTREGADO")
pedido3 = Pedido(127376, 45.00, "PENDIENTE")
pedido4 = Pedido(127377, 85.00, "PREPARANDO")
pedido5 = Pedido(127378, 30.00, "ENTREGADO")
pedido6 = Pedido(127379, 150.75, "PENDIENTE")
pedido7 = Pedido(127380, 65.25, "PENDIENTE")
pedido8 = Pedido(127381, 200.00, "PREPARANDO")
pedido9 = Pedido(127382, 12.50, "ENTREGADO")
pedido10 = Pedido(127383, 95.00, "ENTREGADO")



inventario1 = Inventario()
inventario1.ingredientes["Cafe"] = 50
inventario1.ingredientes["Leche"] = 0
inventario1.ingredientes["Azucar"] = 40
inventario1.ingredientes["Te"] = 50             
inventario1.ingredientes["Chocolate"] = 100    
inventario1.ingredientes["Hielo"] = 1000       
inventario1.ingredientes["Harina"] = 400      
inventario1.ingredientes["Huevo"] = 60       
inventario1.ingredientes["Mantequilla"] = 80  
inventario1.ingredientes["Fruta"] = 150


#inventario1.reducirStock("Cafe", 10)
#inventario1.notificarFaltante("Leche")



clien1= Cliente(10,177398, "Felix", "fe@lixgmail.com" )
clien12= Cliente(100, 167484, "María", "mar1@gmail.com")
clien3= Cliente(20, 198234, "Carlos", "carlos@gmail.com" )
clien4= Cliente( 50, 145672, "Ana", "ana@gmail.com")
clien5= Cliente(150,176543, "Luis", "luis@gmail.com" )
clien6 = Cliente (40, 189345, "Sofía", "sofia@gmail.com")
clien7 = Cliente(30,154789, "Diego", "diego@gmail.com")
clien8 = Cliente(70, 167890, "Elena", "elena@gmail.com")
clien9 = Cliente(15, 190234, "Jorge", "jorge@gmail.com")
clien10 = Cliente(5, 178456, "Lucía", "lucia@gmail.com")

#clien1.realizarPedido(pedido1)
#clien1.consultarHistorial()
#print("\n")
#clien1.cajearPuntos(10, pedido1)

emple1=Empleado(1893937, "BARISTA", 143627, "Lion", "l1on@gmail.com")
emple2 = Empleado(1893938, "GERENTE", 143628, "Elen", "elen.g@gmail.com")
emple3 = Empleado(1893939, "MESERO", 143629, "Marcos", "markos_v@gmail.com")
emple4 = Empleado(1893940, "BARISTA", 143630, "Sophia", "soi.coffee@gmail.com")
emple5 = Empleado(1893941, "GERENTE", 143631, "Ricardo", "ric_admin@gmail.com")
emple6 = Empleado(1893942, "MESERO", 143632, "Lucía", "lu_cia@gmail.com")
emple7 = Empleado(1893943, "BARISTA", 143633, "Mateo", "matt_b@gmail.com")
emple8 = Empleado(1893944, "MESERO", 143634, "Valeria", "val_vendas@gmail.com")
emple9 = Empleado(1893945, "BARISTA", 143635, "Daniel", "dan_barista@gmail.com")
emple10 = Empleado(1893946, "GERENTE", 143636, "Clara", "clara_manager@gmail.com")

#emple8.actualizarInventario("Pan", 10, inventario1)
#print("\n")
#emple2.actualizarInventario("Pan", 10, inventario1)
#emple2.actualizarInventario("Leche", 5, inventario1)
#print("\n")
#emple3.cambiarEstadoPedido(pedido3, "ENTREGADO")


produ1= ProductoBase(173839, "Cafe americano", 35)
produ2= ProductoBase(163784, "Donas de chocolate", 15)
produ3 = ProductoBase(173840, "Capuccino", 45)
produ4 = ProductoBase(173841, "Latte de Vainilla", 50)
produ5 = ProductoBase(163785, "Muffin de Arándanos", 25)
produ6 = ProductoBase(163786, "Galleta de Avena", 18)
produ7 = ProductoBase(173842, "Espresso Doble", 40)
produ8 = ProductoBase(173843, "Té Verde", 30)
produ9 = ProductoBase(163787, "Rebanada de Pastel", 55)
produ10 = ProductoBase(163788, "Bagel con Queso", 42)

bebi1= Bebida("Grande", "FRIA", 173398, "Frape capuchino", 25)
bebi2 = Bebida("Mediano", "CALIENTE", 173399, "Latte Macchiato", 45)
bebi3 = Bebida("Chico", "CALIENTE", 173400, "Espresso", 30)
bebi4 = Bebida("Grande", "FRIA", 173401, "Té Helado Limón", 35)
bebi5 = Bebida("Mediano", "FRIA", 173402, "Smoothie de Fresa", 55)
bebi6 = Bebida("Grande", "CALIENTE", 173403, "Chocolate Abuelita", 40)
bebi7 = Bebida("Chico", "FRIA", 173404, "Cold Brew", 48)
bebi8 = Bebida("Mediano", "CALIENTE", 173405, "Té Chai Latte", 50)
bebi9 = Bebida("Grande", "FRIA", 173406, "Moka Helado", 52)
bebi10 = Bebida("Chico", "CALIENTE", 173407, "Americano", 28)

#bebi3.agregarExtra("Chocolate")
#bebi3.calcularPrecioFinal()
#print(bebi3.calcularPrecioFinal())


post1 = Postre(False, False, 163789, "Cheesecake de Fresa", 45)
post2 = Postre(True, True, 163790, "Brownie Vegano Sin Gluten", 55)
post3 = Postre(False, True, 163791, "Galleta de Chispas Sin Gluten", 20)
post4 = Postre(True, False, 163792, "Panqué de Plátano Vegano", 35)
post5 = Postre(False, False, 163793, "Tarta de Manzana", 40)
post6 = Postre(False, False, 163794, "Croissant de Mantequilla", 30)
post7 = Postre(True, True, 163795, "Trufas de Chocolate Amargo", 15)
post8 = Postre(False, True, 163796, "Muffin de Vainilla Sin Gluten", 28)
post9 = Postre(True, False, 163797, "Dona Vegana de Canela", 22)
post10 = Postre(False, False, 163798, "Eclair de Chocolate", 48)


#clien1.realizarPedido(pedido1)
#clien1.consultarHistorial()
#clien1.cajearPuntos(10, pedido1)


#pedido1.calcularTotal(bebi3)
#bebi3.agregarExtra("Chocolate")
#pedido1.calcularTotal(post2)
#print("\n")
#pedido1.validarStock(bebi1, inventario1)

print(f"RETO")
#---INVENTARIO---
inventario1 = Inventario()
inventario1.ingredientes["Cafe"] = 20
inventario1.ingredientes["Leche"] = 15
inventario1.ingredientes["Chocolate"] = 10
inventario1.ingredientes["Azucar"] = 30

#---EMPLEADO---
emple1 = Empleado(1, "GERENTE", 1001, "Laura", "laura@cafe.com")

#---CLIENTE---
cliente1 = Cliente(50, 2001, "Carlos", "carlos@gmail.com")

#---BEBIDA---
bebida1 = Bebida("Grande", "CALIENTE", 1, "Cafe", 60)



#---POSTRE---
postre1 = Postre(True, False, 2, "Brownie", 35)


print(f"---PEDIDO---")
pedido1 = Pedido(101, 0, "PENDIENTE")
pedido1.validarStock(bebida1, inventario1)
pedido1.calcularTotal(bebida1)
bebida1.agregarExtra("Dulce de leche")
pedido1.calcularTotal(postre1)


cliente1.realizarPedido(pedido1)

inventario1.reducirStock("Cafe", 1)
inventario1.reducirStock("Chocolate", 1)

cliente1.consultarHistorial()