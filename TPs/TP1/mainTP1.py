#%%
import Functions as fc
import numpy as np
import graficos as g

cycles = 100
tournamentSize = 0.4



population = fc.initializePopulation()
objFuncPopulation = list(map(fc.objFunction, population))
maxList=[max(objFuncPopulation)]
promList=[np.average(objFuncPopulation)]
minList=[min(objFuncPopulation)]


#%%

for i in range(0,cycles):
    parents = fc.selection(population,False)
    nextGeneration = []
    for i in range(0,9,2): #creo que aca puedo usar CHUNKS.
        ind1 = []
        ind2 = []
        ind1 = parents[i]
        ind2 = parents[i+1]
        if(fc.decision(fc.crossoverProb)):
            ind1,ind2 = fc.crossover(ind1,ind2)
        if(fc.decision(fc.mutationProb)):
            ind1 = fc.mutation(ind1)
        if(fc.decision(fc.mutationProb)):
            ind2 = fc.mutation(ind2)

        nextGeneration.append(ind1)        
        nextGeneration.append(ind2)        
    
    objFuncPopulation = list(map(fc.objFunction, nextGeneration))
    maxList.append(max(objFuncPopulation))
    promList.append(np.average(objFuncPopulation))
    minList.append(min(objFuncPopulation))
    population=nextGeneration

g.graficarLista(maxList,"Maximos")
g.graficarLista(minList,"Minimos")
g.graficarLista(promList,"Promedios")

# %%
