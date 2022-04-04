# %%
# IMPORT LIBRARIES AND DEFINE COMMON VARIABLES
import numpy as np
import pandas as pd
import random
from itertools import repeat

crossoverProb: float = 0.75
mutationProb: float = 0.05
coef = (2**30)-1

binaryList = [0, 1]
population = []
cycles = 20
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


def selection(pop):
    inxPop = [inx for inx, val in enumerate(pop)]
    fitnessList = list(map(fitnessFunction, repeat(pop), pop))
    inxParents = np.random.choice(a=inxPop, p=fitnessList, size=10)
    parents = []
    for x in inxParents:
        parents.append(pop[x])
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
