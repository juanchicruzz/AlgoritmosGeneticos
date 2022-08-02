import pandas as pd
import numpy as np


#Tabla Vientos - Potencia
d = {'viento': np.arange(0,26), 'potencia': [0,0,0,0,53,106,166,252,350,464,560,630,660,660,660,660,660,660,660,660,660,660,660,660,660,0]} # SE APAGA POR PRECUACION 
df = pd.DataFrame(data=d)
#print(df)

#Random Binary Matrix
seedMatrix = [1 if x <= 24 else 0 for x in range(100)]
 
print (seedMatrix)

individual = np.random.permutation(seedMatrix).reshape(10,10)


#------------------------------------ # Viento Este
individual = np.mod(np.random.permutation(10*10).reshape(10,10),2)
print("Viento  Este")
print (individual)
print("-----------------------")

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
print("Viento Oeste")
individualOeste = individual
for j in range(len(individualOeste)):
    a.append(list(reversed(individualOeste[j])))
mat = np.array(a)
print(mat.reshape(10,10))
print("-----------------------")


#------------------------------------ # Viento Norte

print("Viento Norte")
individualNorte = individual
individualNorte = individualNorte.transpose()
print(individual)


#------------------------------------ # Viento Sur

print("Viento Sur")
individualSur = individual
individualSur = individualSur.transpose()
a=[]
for j in range(len(individualSur)):
    a.append(list(reversed(individualSur[j])))
mat = np.array(a)
print(mat.reshape(10,10))
print("-----------------------")







 