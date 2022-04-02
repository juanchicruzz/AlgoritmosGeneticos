import TP1 as fc
import numpy as np



population = fc.initializePopulation()
objFuncPopulation = list(map(fc.objFunction, population))
maxList=[max(objFuncPopulation)]
promList=[np.average(objFuncPopulation)]
minList=[min(objFuncPopulation)]

print(maxList)
print(minList)
print(promList)

for i in range(20):
    parents = fc.selection(population)
    #for i in range(0,29,2):
        