from tkinter import *
from random import *
from xml.etree.ElementTree import tostring
from PIL import Image,ImageTk
import Functions as f

def DibujarIndividuo(individuo):
    root = Tk()
    root.title("Posicionamiento de aerogeneradores")
    root.geometry("900x700")
    root.config(bg="#0B0301")

    fil = 10
    col = 10

    nfil = 1/fil
    ncol = 1/col

    btnlista = []


    f1 = Frame(root)
    f1.config(bg = "#0B0301")
    f1.place(relx= 0.1, rely = 0.1, relwidth= 0.8, relheight= 0.8)


    # Read the Image
    image = Image.open("molino.png")
    
    # Resize the image using resize() method
    #resize_image = image.resize((1, 1))
    #imagenGenerador = PhotoImage(resize_image)

    imagen = PhotoImage(file = "molino.png")

    textoAerogeneradores = "Cantidad de aerogeneradores: " + str(sum(sum(individuo)))

    aerogeneradores = Label(root, text= textoAerogeneradores )
    aerogeneradores.grid(row = 0, column= 0)
    aerogeneradores.config(fg="white",bg= "#0B0301")

    textoViento = "               Velocidad del viento:  " + str(f.wind0) + " km/h desde Este" 
    viento = Label(root, text= textoViento)
    viento.grid(row = 1, column = 0)
    viento.config(fg="white",bg= "#0B0301")


    for i in range(int(fil)):
        btnlista.append([])
        for j in range(int(col)):
            if individuo[i][j] == 1:
                btnlista[i].append(Button(f1, image=imagen, bd=0))
            else:
                btnlista[i].append(Button(f1, bd=0))
            btnlista[i][j].config(bg="#07A01E",borderwidth = 1, activebackground = "#A2FBFF", relief = "solid")
            btnlista[i][j].place(relx = ncol*j, rely = nfil*i, relwidth= ncol, relheight= nfil)

    root.mainloop()
