# %%
# Importacion de librerias
import numpy as np
import pandas as pd
import random
from itertools import repeat

# Definicion de variables reutilizadas
crossoverProb: float = 0.75
mutationProb: float = 0.20
cant_poblacion: int = 50
cant_iteraciones: int = 1500
coef_arrastre = 0.05
coef_induccionAxial = 0.333
diametroTurbina = 47
tamañoCelda = 94



binaryList = [0, 1]

# %%
# Definicion de funciones

'''
 binaryToDecimal:
  Funcion que recibe una lista conformada por una secuencia de 0 y 1 que se revierte,
  luego se enumera de la forma (posicion, valor) y se hace una sumatoria de 2 elevado a la posicion de
  cada elemento de la lista multiplicado por el valor de ese mismo elemento.
'''
def binaryToDecimal(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


'''
 objFunction:
  Funcion que recibe una lista conformada por una secuencia de 0 y 1, que se convierte en un numero decimal
  y luego se retorna la funcion objetivo del problema (x/coeficiente)^2.
'''
def objFunction(individual: list):
    x = binaryToDecimal(individual)
    return 1

'''
 fitnessFunction:
  Funcion que recibe la poblacion y un individuo, crea una lista con los valores
  de la funcion objetivo de cada individuo de la poblacion y retorna el fitness
  del individuo enviado en los parametros.
'''
def fitnessFunction(pop: list, individual):
    x = objFunction(individual)
    objFuncPopulation = list(map(objFunction, pop))
    return (x/sum(objFuncPopulation))

'''
 randomIndividual:
  Funcion que retorna un individuo aleatorio con 30 genes.
'''
def randomIndividual():
    individual = np.mod(np.random.permutation(10*10).reshape(10,10),2)
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

'''
 decision:
  Funcion que recibe una probabilidad, y la compara con un numero random entre  0 y 1,
  luego retorna true si la probabilidad es mayor o igual, y false si es menor.
'''
def decision(probability):
    return random.random() < probability

'''
 selection:
  Funcion que recibe una poblacion y un booleano dependiendo si la seleccion es de elite o no,
   luego se calcula el largo de la poblacion, se crea una lista con los indices de la poblacion y 
   una lista con los valores fitness de cada elemento de la poblacion.
   Si es elite se seleccionan y guardan los dos mejores individuos de la poblacion a traves de los valores fitness.
   Por ultimo se seleccionan al azar, y guardan, los individuos de la poblacion, en base a la lista de valores fitness.
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
        parents.append(pop[x])
    return parents

'''
 selectionTournament:
    Funcion que recibe una poblacion y un booleano dependiendo si la seleccion es de elite o no 
    y el porcentaje de poblacion que va al torneo.
    Se crea una lista con los indices de la poblacion y una lista con los valores fitness de cada elemento de la poblacion,
    si es elite se separan a los dos mejores individuos de la poblacion a traves de los valores fitness, y el resto compite,
    y sino directamente compiten entre los seleccionados.
'''
def selectionTournament(pop:list,isElite:bool,tSize:float):
    size=len(pop)
    inxPop = [inx for inx, val in enumerate(pop)]
    fitnessList = list(map(fitnessFunction, repeat(pop), pop))
    parents = []
    inxParents=[]
    if(isElite):
        size=size-2
        fitAndInx = list(zip(inxPop,fitnessList))
        fitAndInx.sort(key=lambda tup: tup[1], reverse=True)
        parents.append(pop[fitAndInx[0][0]])
        parents.append(pop[fitAndInx[1][0]])

    # Se filtran la cantidad de jugadores para que de un numero exacto de cruces posibles POTENCIA DE 2

    #playersCount = 2**(round(np.sqrt(tSize * len(pop)))) ESTO ESTABA MAL
    
    playersCount = 0
    countPotencia = 1
    while playersCount < (tSize * len(pop)):
        anterior = playersCount
        playersCount = 2^countPotencia
        countPotencia += 1

    playersCount = anterior

    # Se seleccionan los padres al azar, compiten hasta quedar uno solo y se guarda en la lista de padres
    for i in range(size):
        players=np.random.choice(a=inxPop, size=playersCount)
        players= list(players)
        while len(players) > 1:

            for i in range(len(players)//2):

                # Si el fitnes del jugador 1 es mayor al del jugador 2, se elimina el jugador 2, sino el jugador 1
                if fitnessList[players[i]] > fitnessList[players[i+1]]:
                    players.pop(i+1)
                else:
                    players.pop(i)

        inxParents.extend(players)

    for x in inxParents:
        parents.append(pop[x])


    return parents

'''
 crossover:
    Funcion que recibe dos individuos.
    Se selecciona al azar el punto de corte y se guarda en dos listas (una para cada individuo) los genes 
    menores o iguales a ese punto de corte, y luego se extienden a cada lista los genes
    del otro indivuo que son mayores al punto de corte.
'''
def crossover(ind1, ind2):
    point = np.random.randint(0, 28)
    newInd1 = [gen for inx, gen in enumerate(ind1) if inx <= point]
    newInd2 = [gen for inx, gen in enumerate(ind2) if inx <= point]
    newInd1.extend([gen for inx, gen in enumerate(ind2) if inx > point])
    newInd2.extend([gen for inx, gen in enumerate(ind1) if inx > point])

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
