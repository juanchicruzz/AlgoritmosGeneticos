# %%
# IMPORT LIBRARIES AND DEFINE COMMON VARIABLES
import numpy as np
import pandas as pd
import random
from itertools import repeat

crossoverProb: float = 0.75
mutationProb: float = 0.15
coef = (2**30)-1

binaryList = [0, 1]

# %%
# DEFINE FUNCTIONS


def binaryToDecimal(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))


def objFunction(individual: list):
    x = binaryToDecimal(individual)
    return (x/coef)**2


def fitnessFunction(pop: list, individual):
    x = objFunction(individual)
    objFuncPopulation = list(map(objFunction, pop))
    return (x/sum(objFuncPopulation))


def randomIndividual():
    individual = np.random.choice(binaryList, size=30)
    return individual


def initializePopulation():
    a = []
    for i in range(10):
        a.append(randomIndividual())
    return a


def decision(probability):
    return random.random() < probability


def selection(pop,isElite:bool):
    size=list.count(pop)
    inxPop = [inx for inx, val in enumerate(pop)]
    fitnessList = list(map(fitnessFunction, repeat(pop), pop))
    parents = []
    if(isElite):
        size=size-2
        fitAndInx = list(zip(inxPop,fitnessList))
        fitAndInx.sort(fitAndInx, key=lambda tup: tup[1], reverse=True)
        parents.append(pop[fitAndInx[0][0]])
        parents.append(pop[fitAndInx[1][0]])

    inxParents = np.random.choice(a=inxPop, p=fitnessList, size=size)
    for x in inxParents:
        parents.append(pop[x])
    return parents

def selectionTournament(pop,isElite:bool,tSize):
    size=list.count(pop)
    inxPop = [inx for inx, val in enumerate(pop)]
    fitnessList = list(map(fitnessFunction, repeat(pop), pop))
    parents = []
    if(isElite):
        size=size-2
        fitAndInx = list(zip(inxPop,fitnessList))
        fitAndInx.sort(fitAndInx, key=lambda tup: tup[1], reverse=True)
        parents.append(pop[fitAndInx[0][0]])
        parents.append(pop[fitAndInx[1][0]])

    # inxParents = np.random.choice(a=inxPop, p=fitnessList, size=10)
    # for x in inxParents:
    #     parents.append(pop[x])

    playersCount = 2**(round(np.sqrt(tSize * list.count(pop)))) 

    #multiplico tSize(porcentaje de pop que van a torneo) por size de pop
    #redondeo el numero a numero entero y hago 2 elevado al resultado para que de una cantidad
    #posible de cruces

    for i in range(size):
        players=np.random.choice(a=inxPop, size=playersCount)
        partialWinners=[]
##
        for j in range(0,playersCount-1,2): 
            p1 = []
            p2 = []
            p1 = players[i]
            p2 = players[i+1]



    return parents


def crossover(ind1, ind2):
    point = np.random.randint(0, 28)
    newInd1 = [gen for inx, gen in enumerate(ind1) if inx <= point]
    newInd2 = [gen for inx, gen in enumerate(ind2) if inx <= point]
    newInd1.extend([gen for inx, gen in enumerate(ind2) if inx > point])
    newInd2.extend([gen for inx, gen in enumerate(ind1) if inx > point])

    return newInd1, newInd2


def mutation(ind):
    point = np.random.randint(0, 29)
    if ind[point] == 0:
        ind[point] = 1
    else:
        ind[point] = 0
    return ind


# %%
#population = initializePopulation()
#
#decimalPopulation = map(binaryToDecimal, population)
#
#print(list(decimalPopulation))
#fitnessList = list(map(fitnessFunction, repeat(population), population))
#print(fitnessList)
#
#parents = selection(population)
#
#print(list(map(binaryToDecimal, parents)))
# %%
