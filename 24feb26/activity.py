import tkinter as tk
from tkinter import messagebox

# Función para mostrar el estado del Checkbutton
def mostrar_estado():
    if var.get() == 1:
        messagebox.showinfo("Estado", "Checkbutton seleccionado")
    else:
        messagebox.showinfo("Estado", "Checkbutton no seleccionado")

root = tk.Tk()
root.title("Ejemplo de Checkbutton")
# Variable para almacenar el estado del Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Seleccionar opción", variable=var)
checkbutton.pack(pady=70, padx=90)
boton = tk.Button(root, text="Mostrar estado", command=mostrar_estado)
boton.pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()