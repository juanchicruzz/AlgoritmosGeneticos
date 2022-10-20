# Importacion de librerias y archivos 
import Functions as fc
import numpy as np
import graficos as g
import tablas as t
import pantalla as p

# Declaracion de variables estaticas reutilizables

emp = " "

def ejecucion(cycles,initPopulation):
    print("SELECCION RULETA SIN ELITISMO")
    ciclos = [0]
    population = initPopulation
    objFuncPopulation = list(map(fc.objFunction, population))
    objFuncPopulationLista = fc.castFuncionObjetivo(objFuncPopulation)
    maxList=[max(objFuncPopulationLista)]
    promList=[np.average(objFuncPopulationLista)]
    minList=[min(objFuncPopulationLista)]

    mejorIndividuoSE = []

    for j in range(1,cycles):
        parents = fc.selection(population,False)
        nextGeneration = []
        for i in range(0,50,2): #i va saltando de dos en dos lo que nos permite tomar i e i+1 como padres sin repetirlos
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

        #validar aerogeneradores
        for i in range (len(nextGeneration)):
                if ((sum(sum(nextGeneration[i]))) > 25):
                    individuoAux = fc.validarCantidadAerogeneradores(nextGeneration[i])
                    nextGeneration[i] = individuoAux           

        ciclos.append(j)
        print("ciclo: ", j)
        objFuncPopulation = list(map(fc.objFunction, nextGeneration))
        objFuncPopulationLista = fc.castFuncionObjetivo(objFuncPopulation)
        #inxnextGen = [inx for inx, val in enumerate(nextGeneration)]
        #objandInx = list(zip(inxnextGen,objFuncPopulationLista))
        #objandInx.sort(key=lambda tup: tup[1], reverse=True)
        #print("Ciclo ",j+1," Cromosoma: ",''.join(map(str, (nextGeneration[objandInx[0][0]]))))
        maxList.append(max((objFuncPopulationLista)))
        promList.append(np.average((objFuncPopulationLista)))
        minList.append(min((objFuncPopulationLista)))
        population=nextGeneration
        mejorIndividuoSE.append(parents[0])

    # Graficado de los resultados obtenidos a partir de los metodos definidos en el archivo graficos.py
    #g.graficarLista(maxList,"Maximos Ruleta s/ Elitismo")
    #g.graficarLista(minList,"Minimos Ruleta s/ Elitismo")
    #g.graficarLista(promList,"Promedios Ruleta s/ Elitismo")
    g.graficarConjunto(ciclos,minList,maxList,promList)
    #t.guardarTabla(maxList,minList,promList,"Ruleta s/ Elitismo")
    p.DibujarIndividuo(mejorIndividuoSE[-1])




    print("SELECCION RULETA CON ELITISMO")
    mejorIndividuoE = []
    ciclos = [0]
    population = initPopulation
    objFuncPopulation = list(map(fc.objFunction, population))
    objFuncPopulationLista = fc.castFuncionObjetivo(objFuncPopulation)
    maxList=[max(objFuncPopulationLista)]
    promList=[np.average(objFuncPopulationLista)]
    minList=[min(objFuncPopulationLista)]
    for j in range(1,cycles):
        print("ciclo: ", j)
        parents = fc.selection(population,True)
        nextGeneration = []
        
        nextGeneration.append((parents[0]))
        nextGeneration.append((parents[1]))

        for i in range(2,50,2): #i va saltando de dos en dos lo que nos permite tomar i e i+1 como padres sin repetirlos
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
        

        #validar aerogeneradores
        for i in range (len(nextGeneration)):  
                if ((sum(sum(nextGeneration[i]))) > 25):
                    individuoAux = fc.validarCantidadAerogeneradores(nextGeneration[i])
                    nextGeneration[i] = individuoAux  
        
        ciclos.append(j)
        objFuncPopulation = list(map(fc.objFunction, nextGeneration))
        objFuncPopulationLista = fc.castFuncionObjetivo(objFuncPopulation)
        # inxnextGen = [inx for inx, val in enumerate(nextGeneration)]
        # objandInx = list(zip(inxnextGen,objFuncPopulationLista))
        # objandInx.sort(key=lambda tup: tup[1], reverse=True)
        # print("Ciclo ",j+1," Cromosoma: ",''.join(map(str, (nextGeneration[objandInx[0][0]]))))
        maxList.append(max(objFuncPopulationLista))
        promList.append(np.average(objFuncPopulationLista))
        minList.append(min(objFuncPopulationLista))
        population=nextGeneration

        mejorIndividuoE.append(parents[0])



    # Graficado de los resultados obtenidos a partir de los metodos definidos en el archivo graficos.py
    #g.graficarLista(maxList,"Maximos Ruleta c/ Elitismo")
    #g.graficarLista(minList,"Minimos Ruleta c/ Elitismo")
    #g.graficarLista(promList,"Promedios Ruleta c/ Elitismo")
    g.graficarConjunto(ciclos,minList,maxList,promList)
    #t.guardarTabla(maxList,minList,promList,"Ruleta c/ Elitismo")
    print(mejorIndividuoE[-1])
    p.DibujarIndividuo(mejorIndividuoE[-1])

