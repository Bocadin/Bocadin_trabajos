import tkinter as tk 
from tkinter import messagebox

def nuevo_archivo():
    messagebox.showinfo("Nuevo archivo", "Creaste un nuevo archivo")

def guardar_archivo():
    messagebox.showinfo("Guardar archivo", "Guardaste el archivo")

def cortar_a():
    messagebox.showinfo("Cortar archivo", "Cortaste un texto")

def pegar_a():
    messagebox.showinfo("Pegar archivo", "Pegaste un texto")
   
ventanita=tk.Tk()
ventanita.title("uso de menus")
ventanita.geometry("400x300")
barra_menu=tk.Menu(ventanita)
menu_archivo= tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Guardar" ,command=guardar_archivo)

menu_edicion=tk.Menu(barra_menu, tearoff=0)
menu_edicion.add_command(label="Cortar", command=cortar_a)
menu_edicion.add_command(label="Pegar", command=pegar_a)


barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Ayuda", menu=menu_edicion)
ventanita.config(menu=barra_menu)


ventanita.mainloop()

