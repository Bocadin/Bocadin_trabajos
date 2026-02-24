import tkinter as tk

# Crear ventana
root = tk.Tk()
root.title("Ejemplo de Grid")
root.geometry("500x200")
root.config(bg="lightblue")

# Crear etiquetas y campos de entrada con grid
etiqueta1=tk.Label(root, text="Nombre:")
etiqueta1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entradota=tk.Entry(root, width=20)
entradota.grid(row=0, column=1, padx=5, pady=5)

etiqueta2=tk.Label(root, text="Correo:")
etiqueta2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entradita=tk.Entry(root, width=10)
entradita.grid(row=1, column=1, padx=5, pady=5, sticky="W")

# Botón centrado en dos columnas
tk.Button(root, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()