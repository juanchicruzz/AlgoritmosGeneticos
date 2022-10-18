from tkinter import N
from tkinter.tix import COLUMN
from typing import List
import pandas as pd
import numpy as np
import Functions as f
from itertools import repeat
from itertools import chain



seedMatrix = [1 if x <= 25 else 0 for x in range(100)]
individual1 = np.random.permutation(seedMatrix).reshape(10,10)
individual2 = np.random.permutation(seedMatrix).reshape(10,10)
h1,h2 = f.crossover(individual1,individual2)

def FindNextAerogenerator(f,index):
    cantidadCelda = 0
    for i in range(index+1,len(f)):
        if f[i] == 0:
            cantidadCelda = cantidadCelda + 1
        else:
            cantidadCelda = cantidadCelda + 1
            break
    return cantidadCelda


                


d = {'viento': np.arange(0,26), 'potencia': [0,0,0,0,53,106,166,252,350,464,560,630,660,660,660,660,660,660,660,660,660,660,660,660,660,0]}

d = pd.DataFrame(d)
#print(d)
d.sort_values(by=['viento'], ascending=False, inplace=True)
potencias = []
potencias.append(d['potencia'][d['viento'] == round(6)].values[0].astype('int'))
potencias.append(d['potencia'][d['viento'] == round(11.5)].values[0].astype('int'))
potencias.append(d['potencia'][d['viento'] == round(15.5)].values[0].astype('int'))
potencias.append(d['potencia'][d['viento'] == round(24.5)].values[0].astype('int'))
potencias.append(d['potencia'][d['viento'] == round(6)].values[0].astype('int'))
potencias.append(0)

#print(potencias)
#print("Viento  Este")
#print (individual)
#print("-----------------------")

'''
Pensando funcion Fitness
 U(0)
 -> [0 1 1 1 0 1 0 1 0 0]       * Loop por fila iniciando velocidad del viento U(0)
 -> [0 1 1 0 0 1 0 0 1 0]       * El viento es diferente para cada una de las filas
 -> [0 0 0 0 0 0 1 0 0 0]       * El efecto estela altera al que esta directamente detras (¿cada vez que hay un 0 se resetea?)
 -> [1 0 1 0 1 0 1 1 0 0]       * TERRENO DE QUE TAMAÑO VA A SER (CANTIDAD DE CELDAS)
 -> [0 1 1 1 1 0 1 1 0 0]       * TE PODES PASAR CUANDO MUTAS o CRUZAS DE LOS 25 AEROGENERADORES
 -> [1 1 0 0 1 1 1 1 1 1]       * 
 -> [0 0 0 1 1 1 0 1 1 0]
 -> [0 1 1 0 0 0 0 1 0 0]
 -> [0 1 1 1 0 1 0 1 1 0]
 -> [1 1 0 1 1 0 1 1 0 1]

'''

#------------------------------------ # Viento Oeste
a=[]
#print("Viento Oeste")
individualOeste = individual1
for j in range(len(individualOeste)):
    a.append(list(reversed(individualOeste[j])))
mat = np.array(a)
#print(mat.reshape(10,10))
#print("-----------------------")


#------------------------------------ # Viento Norte

#print("Viento Norte")
individualNorte = individual1
individualNorte = individualNorte.transpose()
#print(individualNorte)
#print(individualNorte.transpose())


#------------------------------------ # Viento Sur

#print("Viento Sur")
individualSur = individual1
individualSur = individualSur.transpose()
a=[]
for j in range(len(individualSur)):
    a.append(list(reversed(individualSur[j])))
mat = np.array(a)
#print(mat.reshape(10,10))
#print("-----------------------")







 