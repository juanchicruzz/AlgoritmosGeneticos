#%%
# Importacion de librerias
import numpy as np
import pandas as pd
import random
from itertools import repeat
from itertools import chain

# Definicion de variables reutilizadas
potencias = {'viento': np.arange(0,26), 'potencia': [0,0,0,0,53,106,166,252,350,464,560,630,660,660,660,660,660,660,660,660,660,660,660,660,660,0]} # SE APAGA POR PRECUACION 
dfpotencias = pd.DataFrame(data=potencias)


seedMatrix = [1 if x <= 24 else 0 for x in range(100)]
crossoverProb: float = 0.75
mutationProb: float = 0.20
cant_poblacion: int = 10
cant_iteraciones: int = 15
coef_arrastre = 0.05
coef_induccionAxial = 0.333
diametroTurbina = 47
tamañoCelda = 94
wind0 = 16
binaryList = [0, 1]

# Definicion de funciones

def FindNextAerogenerator(f,index):
    cantidadCelda = 0
    for i in range(index+1,len(f)):
        if f[i] == 0:
            cantidadCelda = cantidadCelda + 1
        else:
            cantidadCelda = cantidadCelda + 1
            break
    return cantidadCelda

'''
    Recibe viento y distancia hasta el proximo aerogenerador
    Devuelve el viento que RECIBE el proximo aerogenerador
'''

def windAfterGenerator(wind,distance):
    windAffected = wind*(1-(2*coef_induccionAxial/((1+coef_arrastre+(distance/diametroTurbina/2))**2)))
    return windAffected


'''
 objFunction: retorna una matriz con las potencias generadas en cada celda/aerogenerador
'''
def objFunction(individual: list):
    potenciaIndividual = []
    for indiceFila,fila in enumerate(individual):
        potenciaFila = []
        windActual = wind0
        for indexActual,celda in enumerate(fila):
            if celda == 1:
                potenciaFila.append(dfpotencias['potencia'][dfpotencias['viento'] == round(windActual)].values[0].astype('int'))
                #print("Aerogenerador: ",indexActual,"Fila:", indiceFila)
                distancia =  FindNextAerogenerator(fila,indexActual) * tamañoCelda
                if distancia <= (2.3 * tamañoCelda):
                    windActual = windAfterGenerator(windActual,distancia)
                else:
                    windActual = wind0
            else:
                potenciaFila.append(0)
        potenciaIndividual.append(potenciaFila)
    return potenciaIndividual

'''
 fitnessFunction:
'''
def fitnessFunction(pop: list, individual):
    x = objFunction(individual) # cambiar por funcion objetivo calculada de antemano
    x = list(chain.from_iterable(x))
    objFuncPopulation = list(map(objFunction, pop)) # same aca pero de la poblacion
    for i in range(2):
        objFuncPopulation = list(chain.from_iterable(objFuncPopulation))
    print("potenciaIndividuo: ",sum(x))
    potenciaInd = sum(x)
    potenciaPoblacion = sum(objFuncPopulation)
    print("potenciaPoblacion: ",sum(objFuncPopulation))
    return (potenciaInd / potenciaPoblacion)
    

'''
 randomIndividual:
  Funcion que retorna un individuo aleatorio con 30 genes.
'''
def randomIndividual():
    individual = np.random.permutation(seedMatrix).reshape(10,10)
    return individual

'''
 initializePopulation:
  Funcion que retorna una poblacion de largo 10 con individuos aleatorios.
'''
def initializePopulation():
    a = []
    for i in range(cant_poblacion):
        a.append(randomIndividual())
    return a

# %%
'''
 decision:
'''
def decision(probability):
    return random.random() < probability

'''
 selection:
'''
def selection(pop,isElite:bool):
    size=len(pop)
    inxPop = [inx for inx, val in enumerate(pop)]
    fitnessList = list(map(fitnessFunction, repeat(pop), pop))
    parents = []
    if(isElite):
        size=size-2
        fitAndInx = list(zip(inxPop,fitnessList))
        fitAndInx.sort(key=lambda tup: tup[1], reverse=True)
        parents.append(pop[fitAndInx[0][0]])
        parents.append(pop[fitAndInx[1][0]])

    inxParents = np.random.choice(a=inxPop, p=fitnessList, size=size)
    for x in inxParents:
        padre = pop[x]
        parents.append(padre)
    return parents


'''
 crossover:
 clase

 casillero
 aerogenerador: boolean
 potencia: int
 fitness: float
 x: int
 y: int

    [(aero,potencia,fitness,x,y)]
'''
def crossover(padre1, padre2):
    matrizObjetivo1 = objFunction(padre1)
    matrizObjetivo2 = objFunction(padre1)
    for i in range(len(matrizObjetivo1)):
        for j in range(len(matrizObjetivo1[i])):
            padre1[i][j] = (padre1[i][j], matrizObjetivo1[i][j])
            padre2[i][j] = (padre2[i][j], matrizObjetivo2[i][j])

    listaFilas = list(chain.from_iterable(padre1))
    listaFilas.extend(list(chain.from_iterable(padre2)))
    listaColumna = list(chain.from_iterable(padre1.transpose()))
    listaColumna.extend(list(chain.from_iterable(padre2.transpose())))
    listaFilas.sort(key=lambda tup: sum(tup[2]), reverse=True)
    listaColumna.sort(key=lambda tup: sum(tup[2]), reverse=True)
    newInd1 = listaFilas[:10]
    newInd2 = listaColumna[:10]


    return newInd1, newInd2

'''
 mutation:
    Funcion que recibe un individuo y muta en un punto elegido al azar.
'''
def mutation(ind):
    point = np.random.randint(0, 29)
    if ind[point] == 0:
        ind[point] = 1
    else:
        ind[point] = 0
    return ind


# %%
