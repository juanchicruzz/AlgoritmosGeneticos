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


def validarCantidadAerogeneradores(individuo):
    cantidadAerogeneradoresActual = sum(sum(individuo)) # cuento cantidad actual de generadores
    if (cantidadAerogeneradoresActual > 25):

        individuo = np.array(individuo,dtype=object)
        matrizObjetivo = objFunction(individuo) # calculo f.Objetivo del individuo

        for i in range(len(matrizObjetivo)):
            for j in range(len(matrizObjetivo[i])):
                individuo[i][j] = (matrizObjetivo[i][j],individuo[i][j],i,j) # Genero matrix (potencia,aerogenerador,x,y)

        individuo = list(chain.from_iterable(individuo))
         
        individuo.sort(key=lambda x: x[0], reverse=False) #Ordeno la lista de menor  a mayor segun potencia
        
        for i in range(len(individuo)): #Ordeno la lista de menor  a mayor segun potencia
            if individuo[i][1] == 1:
                listIndividual = list(individuo[i])
                listIndividual[1] = 0   #Elimino aerogenerador
                individuo[i] = tuple(listIndividual)
                cantidadAerogeneradoresActual = cantidadAerogeneradoresActual - 1
                if cantidadAerogeneradoresActual <= 25:
                    break; #Finalizo bucle si tengo 25 generadores

        #Reorganizo el individuo segun las coordenadas de la matriz
        individuo = ([(celda[2],celda[3],celda[1]) for celda in individuo])
        individuo.sort(key=lambda x: (x[0],x[1]), reverse=False)
        individuo = np.reshape([celda[2] for celda in individuo],(10, 10))
    return individuo


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


def crossover(padre1, padre2):
    padre1 = np.array(padre1,dtype=object)
    padre2 = np.array(padre2,dtype=object)
    matrizObjetivo1 = objFunction(padre1)
    matrizObjetivo2 = objFunction(padre2)
    for i in range(len(matrizObjetivo1)):
        for j in range(len(matrizObjetivo1[i])):
            padre1[i][j] = (matrizObjetivo1[i][j],padre1[i][j])
            padre2[i][j] = (matrizObjetivo2[i][j],padre2[i][j])


    listaFilas = list((padre1))
    listaFilas.extend(list((padre2)))

    def potenciaFila(fila):
        return (sum(i for i, j in fila))

    listaColumna = list((padre1.transpose()))
    listaColumna.extend(list((padre2.transpose())))

    listaFilas.sort(key=lambda fila: potenciaFila(list(fila)), reverse=True)
    listaColumna.sort(key=lambda fila: potenciaFila(list(fila)), reverse=True)

    # Mejores Filas - Mejores Columnas
    newInd1 = listaFilas[:10]
    newInd2 = listaColumna[:10]

    # Reescalado y restablecer matriz Original
    newInd1 = list(chain.from_iterable(newInd1))
    newInd2 = list(chain.from_iterable(newInd2))
    newInd1 = np.reshape([celda[1] for celda in newInd1],(10, 10))
    newInd2 = np.reshape([celda[1] for celda in newInd2],(10, 10))


    # Validar Cant maxima de aerogeneradores por individuo
    newInd1 = validarCantidadAerogeneradores(newInd1)
    newInd2 = validarCantidadAerogeneradores(newInd2)

    return newInd1, newInd2

'''
 mutation:
    Funcion que recibe un individuo y muta en un punto elegido al azar.
'''
def mutation(ind):
    pointx = np.random.randint(0, 10)
    pointy = np.random.randint(0, 10)
    if ind[pointx][pointy] == 0:
        ind[pointx][pointy] = 1
    else:
        ind[pointx][pointy] = 0

    ind = validarCantidadAerogeneradores(ind)
    return ind



