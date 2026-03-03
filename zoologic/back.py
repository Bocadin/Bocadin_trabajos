from logging import root
import tkinter as tk 
from PIL import Image, ImageTk


def ventana_one():
    global ven1
    ven1=tk.Tk()
    ven1.title("Ventana 1")
    ven1.config(bg="light green")
    ven1.geometry("700x500")
    
    etiqueta1=tk.Label(ven1, text="Reino Animal ",bg="White", font=("Arial",22, "bold" ))
    etiqueta1.pack()
    frame1=tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=20, pady=20)
    imagen = Image.open("C:/Users/240019110/Documents/zoologic/iamgen1.jpg")
    imagen = imagen.resize((400, 300))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    var=tk.IntVar()
    radiobutton1 = tk.Radiobutton(frame2, text="León", variable=var, value=1)
    radiobutton1.pack(padx=5)
    radiobutton2 = tk.Radiobutton(frame2, text="Elefante", variable=var, value=2)
    radiobutton2.pack(padx=5)
    radiobutton3 = tk.Radiobutton(frame2, text="Castor", variable=var, value=3)
    radiobutton3.pack(padx=5)
    radiobutton4 = tk.Radiobutton(frame2, text="Jirafa", variable=var, value=4)
    radiobutton4.pack(padx=5)


    def mostrar_seleccion():
        seleccion = var.get()
        if seleccion == 1:
            ventana_leon()
        elif seleccion == 2:
            ventana_elefante()
        elif seleccion == 3:
            ventana_castor()
        elif seleccion == 4:
            ventana_jirafa()
    
    botoncito=tk.Button(ven1, text="Ir a ventanita", command=mostrar_seleccion)
    botoncito.pack(pady=10, padx=10)

    ven1.mainloop()
    

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()  
    ventana_one()  

def ventana_elefante():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Los Elefantes")
    ven2.geometry("700x500")
    ven2.config(bg="light blue")

    eti2=tk.Label(ven2,text="Elefante",bg="white",font=("Arial",22,"bold"))
    eti2.pack(pady=10)
    frame3=tk.Frame(ven2)
    frame3.pack(fill=tk.X, padx=20, pady=20)
    imagen3= Image.open("C:/Users/240019110/Documents/zoologic/elefantito.jpg")
    imagen3= imagen3.resize((400, 300))  
    imagen_tk = ImageTk.PhotoImage(imagen3) 
    label_imagen = tk.Label(frame3, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    text1=tk.Label(frame3, text="Un elefante MUY FELIz :): Los elefantes son una familia de mamíferos cuadrúpedos de gran tamaño, famosos por sus grandes orejas y trompa prensil, así como sus colmillos blancos y largos de marfil, además de por ser los animales terrestres más voluminosos que existen hoy en día en el mundo.", wraplength=200, justify="left")
    text1.grid(row=0, column=2, padx=5, pady=5)

    boton2=tk.Button(ven2,text="ir a ventana principal",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)

    ven2.mainloop()


def ventana_leon():
    global ven3
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("Los Leones")
    ven3.geometry("700x500")
    ven3.config(bg="light yellow")

    eti2=tk.Label(ven3,text="León",bg="white",font=("Arial",22,"bold"))
    eti2.pack(pady=10)
    frame4=tk.Frame(ven3)
    frame4.pack(fill=tk.X, padx=20, pady=20)
    imagen = Image.open("C:/Users/240019110/Documents/zoologic/leoncito.jpg")
    imagen = imagen.resize((400, 300))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame4, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    
    etiqueta22=tk.Label(frame4, text="Un leon MUY FELIz :): es un mamífero carnívoro de la familia de los félidos y una de las cinco especies del género Panthera. Los leones salvajes viven en poblaciones cada vez más dispersas y fragmentadas del África subsahariana" ,wraplength=200, justify="left")
    etiqueta22.grid(row=0, column=2, padx=5, pady=5)

    boton2=tk.Button(ven3,text="ir a ventana principal",command=lambda: regresar_a_primera(ven3) )
    boton2.pack(pady=30)

    ven3.mainloop()


def ventana_castor():
    global ven4
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("Los Castores")
    ven4.geometry("700x500")
    ven4.config(bg="grey")

    eti2=tk.Label(ven4,text="Castor",bg="white",font=("Arial",22,"bold"))
    eti2.pack(pady=10)
    frame5=tk.Frame(ven4)
    frame5.pack(fill=tk.X, padx=20, pady=20)
    imagen = Image.open("C:/Users/240019110/Documents/zoologic/castorcito.jpg")
    imagen = imagen.resize((400, 300))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame5, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    
    etiqueta33=tk.Label(frame5, text="Un castor MUY FELIz :):  son un género de roedores semiacuáticos nativos de América del Norte y Eurasia que se caracterizan por sus amplias y escamosas colas. Este género, de todos los que pertenecen a la familia Castoridae" ,wraplength=200, justify="left")
    etiqueta33.grid(row=0, column=2, padx=5, pady=5)

    boton2=tk.Button(ven4,text="ir a ventana principal",command=lambda: regresar_a_primera(ven4) )
    boton2.pack(pady=30)

    ven4.mainloop()

def ventana_jirafa():
    global ven5
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("Los Jirafas")
    ven5.geometry("700x500")
    ven5.config(bg="orange")

    eti2=tk.Label(ven5,text="Jirafa",bg="white",font=("Arial",22,"bold"))
    eti2.pack(pady=10)
    frame6=tk.Frame(ven5)
    frame6.pack(fill=tk.X, padx=20, pady=20)
    imagen = Image.open("C:/Users/240019110/Documents/zoologic/Jirafa.jpg")
    imagen = imagen.resize((400, 300))  
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame6, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)
 
    
    etiqueta44=tk.Label(frame6, text="Una jirafa MUY FELIz :): s una especie de mamífero artiodáctilo, de la familia Giraffidae propio de África. Es la más alta de todas las especies de animales terrestres existentes, ya que puede alcanzar una altura máxima de 5,7 m y un peso que varía entre 750 y 1600 kg" ,wraplength=200, justify="left")
    etiqueta44.grid(row=0, column=2, padx=5, pady=5)

    boton2=tk.Button(ven5,text="ir a ventana principal",command=lambda: regresar_a_primera(ven5) )
    boton2.pack(pady=30)

    ven5.mainloop()

ventana_one()