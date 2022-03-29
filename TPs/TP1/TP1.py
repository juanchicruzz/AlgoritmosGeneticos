#%%
#IMPORT LIBRARIES AND DEFINE COMMON VARIABLES
import numpy as np
import pandas as pd
import random

crossover:float = 0.75
mutation :float = 0.05 
coef=(2**30)-1

binaryList = [0,1]
pupulation=[]
cycles=20
#%%
#DEFINE FUNCTIONS

def objFunction(x:int):
    return (x/coef)**2

def randomIndividial():
    individual = np.random.choice(binaryList, size = 30)
    return individual

def initializePopulation(population:list):

    return 
    
def decision(probability):
    return random.random() < probability