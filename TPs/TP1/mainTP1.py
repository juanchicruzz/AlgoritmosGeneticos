#%%

# Importacion de librerias y archivos 
import Functions as fc
import numpy as np
import graficos as g

# Declaracion de variables estaticas reutilizables
cycles = 1000
tournamentSize = 0.4


# Definicion de variables a utilizar a partir de los metodos definidos en el archivo Functions.py
population = fc.initializePopulation()
objFuncPopulation = list(map(fc.objFunction, population))
maxList=[max(objFuncPopulation)]
promList=[np.average(objFuncPopulation)]
minList=[min(objFuncPopulation)]


#%%
'''
El orden de ejecucion del programa es:
 1- Se ejecuta el programa tantas veces como ciclos se han solicitado.
  Para cada ciclo:
    2- Se seleccionan los padres de a dos.
    Para cada par de padres:
        3- Se realiza el crossover si de acuerdo a la probabilidad de crossover la decision es que se haga.
        4- Se realiza la mutacion de ambos individuos si de acuerdo a la probabilidad de mutacion la decision es que se haga (por separado).
        5- Se guardan los nuevos individuos.
    Una vez terminado el proceso de seleccion, cruce y mutacion:
    6- Se actualizan los valores derivados de la poblacion.
    7- Se reemplaza la poblacion anterior por la nueva.
 Una vez ejecutados todos los ciclos:
    8- Se grafican los resultados obtenidos.
'''
for i in range(0,cycles):
    parents = fc.selection(population,False)
    nextGeneration = []
    for i in range(0,9,2): #i va saltando de dos en dos lo que nos permite tomar i e i+1 como padres sin repetirlos
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

# Graficado de los resultados obtenidos a partir de los metodos definidos en el archivo graficos.py
g.graficarLista(maxList,"Maximos")
g.graficarLista(minList,"Minimos")
g.graficarLista(promList,"Promedios")

# %%
