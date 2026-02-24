import tkinter as tk
from tkinter import messagebox

# Función para mostrar diferentes tipos de messagebox
def mostrar_messagebox():
    # Mostrar un messagebox de información
    messagebox.showinfo("Información", "Se va a acabar el mundo mañana.")
    
    # Mostrar un messagebox de advertencia
    messagebox.showwarning("Advertencia", "Cuidadoooo, correee!!!!!!.")
    
    # Mostrar un messagebox de error
    messagebox.showerror("Error", "Mentira :)")
    
    # Mostrar un messagebox de pregunta (sí/no)
    respuesta = messagebox.askyesno("Pregunta", "¿Te gusta el chocolate?")
    if respuesta:
        messagebox.showinfo("Respuesta", "¡Genial! Eres una buena persona.")
    else:
        messagebox.showinfo("Respuesta", "Oh :( tal vez te vayas al infierno")

ventana1=tk.Tk()
ventana1.title("Uso del messagebox")
ventana1.geometry("600x400")

ventana1.config(bg="lavender")

boton1= tk.Button(ventana1, text="Mostrar MessageBox", command=mostrar_messagebox)
boton1.pack(pady=20)

ventana1.mainloop()
