#%%
#IMPORT LIBRARIES AND DEFINE COMMON VARIABLES
import numpy as np
import pandas as pd
import random

crossoverProb :float = 0.75
mutationProb :float = 0.05 
coef=(2**30)-1

binaryList = [0,1]
population =[]
cycles=20
#%%
#DEFINE FUNCTIONS

def binaryToDecimal(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def objFunction(individual:list):
    x = binaryToDecimal(individual)
    return (x/coef)**2

def fitnessFunction(individual,pop:list):
    x = binaryToDecimal(individual)
    decimalPopulation = list(map(binaryToDecimal,pop))
    return (x/sum(decimalPopulation))

def maxInPop(pop):
    decimalPopulation = map(binaryToDecimal,pop)
    return max(decimalPopulation)
    

def minInPop(pop):
    decimalPopulation = map(binaryToDecimal,pop)
    return min(decimalPopulation)

def randomIndividial():
    individual = np.random.choice(binaryList, size = 30)
    return individual

def initializePopulation():
    a = []
    for i in range(10):
        a.append(randomIndividial())
    return a
    
def decision(probability):
    return random.random() < probability

def selection():
    #ACA RULETA
    return

def crossover(ind1,ind2):
    point = np.random.randint(1,28)
    newInd1 = [val for inx,val in enumerate(ind1) if inx<point]
    #PIENSO QUE LA MEJOR FORMA ES DIVIDIR EL IND1 y EL IND2 EN DOS PARTES, EL PRE Y EL POST E INTERCALARLOS.    

def mutation():
    return

#%%
population = initializePopulation()

decimalPopulation = map(binaryToDecimal,population)

print(list(decimalPopulation))