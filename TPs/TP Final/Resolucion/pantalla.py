from cProfile import label
from tkinter import *
from random import *
from xml.etree.ElementTree import tostring
from PIL import Image,ImageTk
from numpy import place
import Functions as f
from itertools import repeat
from itertools import chain
import numpy as np

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

    potenciaIndividuo = f.objFunction(individuo)
    mostrarPotencias = potenciaIndividuo
    mostrarPotencias = np.array(mostrarPotencias).transpose()
    potenciaIndividuo = list(chain.from_iterable(potenciaIndividuo))

    textoAerogeneradores = "Cantidad de aerogeneradores: " + str(sum(sum(individuo)))
    aerogeneradores = Label(root, text= textoAerogeneradores)
    aerogeneradores.grid(row = 1, column= 0)
    aerogeneradores.config(fg="white",bg= "#0B0301")

    textoViento = "            Velocidad del viento:  " + str(f.wind0) + " m/s desde Norte" 
    viento = Label(root, text= textoViento)
    viento.grid(row = 2, column = 0)
    viento.config(fg="white",bg= "#0B0301")

    textoPotencia = "Potencia total generada:  " + str(sum(potenciaIndividuo)) + " kW/s" 
    potencia = Label(root, text= textoPotencia)
    potencia.grid(row = 3, column = 0)
    potencia.config(fg="white",bg= "#0B0301")

    individuo = np.array(individuo).transpose()
    print(individuo)


    for i in range(int(fil)):
        btnlista.append([])
        for j in range(int(col)):
            if individuo[i][j] == 1:
                potenciaCelda = mostrarPotencias[i][j]
                btnlista[i].append(Button(f1, text= "            "+ str(potenciaCelda) +"kW", wraplength= 40, justify=CENTER , font=('Helvetica 8 bold'), image=imagen ,compound = CENTER , bd=0, fg = "black"))
            else:
                btnlista[i].append(Button(f1, bd=0))
            btnlista[i][j].config(bg="white",borderwidth = 1, activebackground = "#A2FBFF", relief = "solid")
            btnlista[i][j].place(relx = ncol*j, rely = nfil*i, relwidth= ncol, relheight= nfil)

    root.mainloop()
