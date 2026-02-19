#Importamos librerías
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
def boton_clic():
    print("Eres lesbiana!")

def actualizar_etiqueta():
    nuevo_texto = entrada.get()
    etiqueta.config(text=nuevo_texto)
    
    
#Definimos la ventana
ven1 = tk.Tk()
#Le damos un título a la ventana
ven1.title("Loma Maria Rico")
#Programamos dimensiones
ven1.geometry("1000x1000")
# Iniciar el bucle principal de la aplicación



etiqueta = tk.Label(ven1,text="¡Hola, Grupo de tonotos!", 
    font=("Arial", 28, "italic"), fg="light green",padx=20, pady=10)
etiqueta.pack()


etiqueta2 = tk.Label(ven1,text="Mi nombre es Estefania :)", 
    font=("Arial", 28, "bold"), fg="Pink",padx=20, pady=10)
etiqueta2.pack()

entrada = tk.Entry(ven1, width=30)
entrada.pack(pady=10)

boton = tk.Button(ven1, text="Actualizar", command=actualizar_etiqueta)
boton.pack()

etiqueta = tk.Label(ven1, text="Texto inicial", font=("Arial", 12))
etiqueta.pack(pady=10)
ven1.mainloop()

imagen = Image.open("bbeeae78be4c06640550550714a92382.jpg")
imagen = imagen.resize((400, 300))  # Redimensionar si es necesario
imagen_tk = ImageTk.PhotoImage(imagen) 
label_imagen = tk.Label(ven1, image=imagen_tk)
label_imagen.pack(pady=20) 


boton = tk.Button(ven1, text="Haz click aquí si eres un Therian ", command=boton_clic,
                  font=("Comic Sans",30),fg="Grey",bg="White")
boton.pack(pady=20) 


ven1.mainloop()