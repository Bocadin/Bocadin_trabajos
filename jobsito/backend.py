import csv                                                            
  
class Usuario():
    lista=[]
    def __init__(self, name, age, food):
        self.nombre= name
        self.edad= age
        self.comidafav= food 
        if self not in Usuario.lista:
            Usuario.lista.append(self)
            
    def mostrar_info(self):
        return f"El usuario {self.nombre} tiene {self.edad} y le gusta {self.comidafav}"
    
    @classmethod
    def mostrar_usuarios(cls):
        return cls.lista
    
    @classmethod
    def guardar_usuarios():
        campos=["nombre", "edad","comida"]
        with open("personitas.csv", "w", encoding="utf-8") as f:
            escritor=csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow ({"nombre":u.nombre, "edad":u.edad, "comida":u.comidafav})