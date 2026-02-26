import tkinter as tk 
from PIL import Image, ImageTk


def ventana_one():
    global ventana_one
    ven1=tk.Tk()
    ven1.title("Ventana 1")
    ven1.config(bg="light pink")
    ven1.geometry("700x500")
    
    etiqueta1=tk.Label(ven1, text="Reino Animal ",bg="White", font=("Arial",16, "bold" ))
    etiqueta1.grid(row=0, column=0, padx=5, pady=5)
    imagen = Image.open("C:/Users/EMA 4 - 206/Documents/ventanasdezooligoco/iamgen1.jpg")
    imagen = imagen.resize((400, 300))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(ven1, image=imagen_tk)
    label_imagen.grid(row=1, column=0, padx=5, pady=5)
  

    radiobutton1 = tk.Radiobutton(ven1, text="Jirafa", )
    radiobutton1.pack(pady=5)

    radiobutton2 = tk.Radiobutton(ven1, text="Elefante", )
    radiobutton2.pack(pady=5)

    radiobutton3 = tk.Radiobutton(ven1, text="León", )
    radiobutton3.pack(pady=5)
    
    radiobutton4 = tk.Radiobutton(ven1, text="Castor", )
    radiobutton3.pack(pady=5)


    #botoncito=tk.Button(ven1, text="Ir a ventanita", command=ventana_two)
    #botoncito.pack(pady=10)
    
    ven1.mainloop()
    
ventana_one()