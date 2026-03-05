import tkinter as tk 
from backend import *
from tkinter import messagebox

def ventana_one():
    ven1= tk.Tk()
    ven1.title("Ventana de Registro")
    ven1.geometry("500x400")

    
    eti1=tk.Label(ven1, text="Nombre", bg="White", font="Arial")
    eti1.pack(pady=5, padx=5)
    
    entrada = tk.Entry(ven1, width=60)
    entrada.pack(pady=10)
    
    eti2=tk.Label(ven1, text="Edad", bg="White", font="Arial")
    eti2.pack(pady=5, padx=5)
    
    entrada2= tk.Entry(ven1, width=60)
    entrada2.pack(pady=10)
    
    eti3=tk.Label(ven1, text="Comida favorita", bg="White", font="Arial")
    eti3.pack(pady=5, padx=5)  
    
    entrada3= tk.Entry(ven1, width=60)
    entrada3.pack(pady=10) 
    
    
    def registrar():
        name=entrada.get()
        age=entrada2.get()
        food=entrada3.get()
        nuevo_usuario=Usuario(name, age, food)
        entrada.delete(0, tk.END)
        entrada2.delete(0, tk.END)
        entrada3.delete(0, tk.END)
        messagebox.showinfo("Registro de usuario", "Tu registro de usuario fue existoso ;)")
        
    
    botoncito1=tk.Button (ven1, text="Registrar", command= registrar)
    botoncito1.pack(pady=5, padx=5)  
    
    def mostrar():
        print(Usuario.mostrar_usuarios)
    botoncito2=tk.Button (ven1, text="Mostrar lista", command=mostrar)
    botoncito2.pack(pady=5)
    
    ven1.mainloop()
    
ventana_one()
    
    
