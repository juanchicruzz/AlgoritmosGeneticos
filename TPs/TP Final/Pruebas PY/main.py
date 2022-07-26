#%%

# Importacion de librerias y archivos 
import Functions as fc
import numpy as np
import graficos as g
import tablas as t

# Declaracion de variables estaticas reutilizables

tournamentSize = 0.4
emp = " "
#%%
def ejecucion(cycles,initPopulation):
    print("SELECCION RULETA SIN ELITISMO")
    population = initPopulation
    objFuncPopulation = list(map(fc.objFunction, population))
    maxList=[max(objFuncPopulation)]
    promList=[np.average(objFuncPopulation)]
    minList=[min(objFuncPopulation)]
    for j in range(0,cycles):
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
        inxnextGen = [inx for inx, val in enumerate(nextGeneration)]
        objandInx = list(zip(inxnextGen,objFuncPopulation))
        objandInx.sort(key=lambda tup: tup[1], reverse=True)
        print("Ciclo ",j+1," Cromosoma: ",''.join(map(str, (nextGeneration[objandInx[0][0]]))))
        maxList.append(max(objFuncPopulation))
        promList.append(np.average(objFuncPopulation))
        minList.append(min(objFuncPopulation))
        population=nextGeneration

    # Graficado de los resultados obtenidos a partir de los metodos definidos en el archivo graficos.py
    g.graficarLista(maxList,"Maximos Ruleta s/ Elitismo")
    g.graficarLista(minList,"Minimos Ruleta s/ Elitismo")
    g.graficarLista(promList,"Promedios Ruleta s/ Elitismo")
    t.guardarTabla(maxList,minList,promList,"Ruleta s/ Elitismo")



    # %%

    print("SELECCION RULETA CON ELITISMO")

    population = initPopulation
    objFuncPopulation = list(map(fc.objFunction, population))
    maxList=[max(objFuncPopulation)]
    promList=[np.average(objFuncPopulation)]
    minList=[min(objFuncPopulation)]
    for j in range(0,cycles):
        parents = fc.selection(population,True)
        nextGeneration = []
        
        #Se agregan los dos primeros por elitismo
        nextGeneration.append(parents[0])
        nextGeneration.append(parents[1])

        for i in range(2,9,2): #i va saltando de dos en dos lo que nos permite tomar i e i+1 como padres sin repetirlos
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
        inxnextGen = [inx for inx, val in enumerate(nextGeneration)]
        objandInx = list(zip(inxnextGen,objFuncPopulation))
        objandInx.sort(key=lambda tup: tup[1], reverse=True)
        print("Ciclo ",j+1," Cromosoma: ",''.join(map(str, (nextGeneration[objandInx[0][0]]))))
        maxList.append(max(objFuncPopulation))
        promList.append(np.average(objFuncPopulation))
        minList.append(min(objFuncPopulation))
        population=nextGeneration

    # Graficado de los resultados obtenidos a partir de los metodos definidos en el archivo graficos.py
    g.graficarLista(maxList,"Maximos Ruleta c/ Elitismo")
    g.graficarLista(minList,"Minimos Ruleta c/ Elitismo")
    g.graficarLista(promList,"Promedios Ruleta c/ Elitismo")
    t.guardarTabla(maxList,minList,promList,"Ruleta c/ Elitismo")

