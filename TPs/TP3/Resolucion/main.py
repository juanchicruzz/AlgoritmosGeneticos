import funciones as f
import datos
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import statistics
import random
from tqdm import tqdm

# ------------ ALGORITMO GREEDY --------------------------- #


def greedy(inicial):
    recorrido = []
    distTotal = 0
    recorrido.append(inicial)

    provActual = inicial
    while (len(recorrido) < len(provincias)):
        # get --> proxima ciudad sin haber sido recorrida
        provProx, distMin = datos.CalculaProvMinDistancia(provActual, recorrido)
        distTotal += distMin
        recorrido.append(provProx)
        provActual = provProx

    # calculo la distancia entre la ultima capital del recorrido y la inicial
    distTotal += datos.CalculaDistancia(inicial, recorrido[-1])
    # y agrego al inicial al final del recorrido
    recorrido.append(inicial)
    return recorrido, distTotal

# --------------------------- OPCION DOS --------------------------- #


def MejorRecorrido(provincias):
    distMin = math.inf
    recorridoMin = []

    # utilizo greedy para cada capital y me quedo con la mejor.
    for p in provincias:
        recorrido, distancia = greedy(p)
        if(distancia < distMin):
            distMin = distancia
            recorridoMin = recorrido
    return recorridoMin, distMin


# --------------------------- Algoritmo Genético --------------------------- #

def rellenarPoblacionInicial(cantCromosomas):
    poblacion = []
    for j in range(cantCromosomas):
        individuo = []
        for i in range(24):
            individuo.append(i)         #genero una lista del 0 al 23 (24 provincias contando capital federal)
        random.shuffle(individuo)       #desordeo de forma aleatoria al individuo
        poblacion.append(individuo)
    return poblacion


def funcionObjetivo(recorrido):
    return 1/datos.CalculaDistanciaDeRecorrido(recorrido)   # 1/distancia recorrida -> menor distancia mejor puntuacion


def rellenarFuncionesObjetivoYFitness(poblacion):
    # rellenar F objetivo
    listaFObjetivo = []
    listaFitness = []

    for i in range(len(poblacion)):
        listaFObjetivo.append(funcionObjetivo(poblacion[i]))

    # rellenar F fitness.
    sumatotal = sum(listaFObjetivo) #calculo el total de la poblacion

    for i in range(len(poblacion)):
        listaFitness.append(listaFObjetivo[i] / sumatotal) #calculo la proporcion de cada individuo de la poblacion

    return listaFitness, listaFObjetivo


def ruleta(poblacion, listaFitness):
    pareja = []
    inxPop = [inx for inx, val in enumerate(poblacion)]

    # elijo cada uno de los padres.
    for veces in range(2):
        indice = np.random.choice(a=inxPop, p=listaFitness, size=1) # ruleta proporcional al fitnes/ --> [7] --> sum[7] --> 7
        pareja.append(poblacion[sum(indice)])
    return pareja


def Crossover_Ciclico(p1, p2):
    # se copia para resolver problemas de referencias #
    hijo = p2.copy()
    indexP1 = 0
    sigue = True
    while(sigue):
        hijo[indexP1] = p1[indexP1]

        valorP2 = p2[indexP1]
        # calculo el indice en el padre 1 donde se encuentra el valorP2
        indexP1 = p1.index(valorP2)

        if(valorP2 in hijo):
            sigue = False

    return hijo


def crossover(padres, prob):
    r = random.uniform(0, 1)
    if(r <= prob):
        hijo1 = Crossover_Ciclico(padres[0], padres[1])
        hijo2 = Crossover_Ciclico(padres[1], padres[0])
        return hijo1, hijo2
    else:
        return padres[0], padres[1]


def mutacion(hijoOriginal, prob):
    # hacemos una copia para que no ocurran problemas de referencias de Python
    hijo = hijoOriginal.copy()

    r = random.uniform(0, 1)
    if(r <= prob):
        indice1 = int(random.uniform(0, len(hijo)))
        indice2 = int(random.uniform(0, len(hijo)))

        vAux = hijo[indice1]
        hijo[indice1] = hijo[indice2]
        hijo[indice2] = vAux
    return hijo


def mostrarGraficasEnPantalla(ejeX, minimos, maximos, media, minHistorico):
    plt.plot(ejeX, minimos, label='Minimos', linewidth=2, color="red", alpha=0.6)
    plt.plot(ejeX, maximos, label='Maximos', linewidth=2, color="blue", alpha=0.6)
    plt.plot(ejeX, media, label='Media', linewidth=2, color="green", alpha=0.6)
    plt.plot(ejeX, minHistorico, label='Mejor Historico', linewidth=2, color="black", alpha=1)

    plt.legend()
    plt.ylabel(' Valor de la Funcion Objetivo ')
    plt.xlabel(' Generación ')
    plt.show()


def elitismo(poblacion, listaFitness, cantElite):
    # Creamos una copia de la lista (Fitness u objetivo), elegimos el mejor(el max), lo borramos
    # y volvemos a elegir el mejor. Luego sacamos los indices en el arreglo original.
    # y agregamos en la proximaGeneracion la poblacion en el indice de los mejores.

    indiceMejor = []
    copiaFitness = listaFitness.copy()
    elites = []

    for i in range(cantElite):
        mejor = max(copiaFitness)
        indiceMejor.append(listaFitness.index(mejor))
        copiaFitness.remove(mejor)

    for i in range(cantElite):
        elites.append(poblacion[indiceMejor[i]])

    return elites


def Genetico(provincias):
    # Arreglo de poblaciones.
    poblacion = []
    proximaGeneracion = []

    # F objetivo y F Fitness.
    listaFObjetivo = []
    listaFitness = []

    # Parametros iniciales.
    cantMaximaGeneraciones = 200
    cantIndividuosEnPoblacion = 50
    p_crossover = 0.9
    p_mutacion = 0.15

    # arreglos graficos.
    mostrarGraficas = True 
    ejeX = []
    minimos = []
    maximos = []
    medias = []
    minHistorico = []

    hayElitismo = input("¿Aplicar elitismo? (s/n): ")
    if(hayElitismo.lower() == 's'):
        hayElitismo = True
        cantElite = 10
    else:
        hayElitismo = False
        cantElite = 0

    # inicializo poblacion y lista fitness
    poblacion = rellenarPoblacionInicial(cantIndividuosEnPoblacion)
    listaFitness, listaFObjetivo = rellenarFuncionesObjetivoYFitness(poblacion)

    # variables para guardar los mejores.
    distMinima = 0
    MejorRecorrido = []

    cantidadCiclos = 0

    for i in range(cantMaximaGeneraciones):
        cantidadCiclos += 1
        # aplica el ELITISMO
        if(hayElitismo):
            proximaGeneracion += elitismo(poblacion, listaFObjetivo, cantElite)

        for i in range(int((len(poblacion) - cantElite) / 2)):
            # seleccionar 2 individuos para el cruce
            padres = ruleta(poblacion, listaFitness)
            # cruzar con cierta probabilidad 2 individuos y obtener descendientes
            hijo1, hijo2 = crossover(padres, p_crossover)
            # Mutar con cierta probabilidad
            hijomutado1 = mutacion(hijo1, p_mutacion)
            hijomutado2 = mutacion(hijo2, p_mutacion)

            proximaGeneracion.append(hijomutado1)
            proximaGeneracion.append(hijomutado2)

        poblacion = proximaGeneracion.copy()
        proximaGeneracion = []
        listaFObjetivo = []
        listaFitness = []

        # rellena funcion fitness y objetivo.
        listaFitness, listaFObjetivo = rellenarFuncionesObjetivoYFitness(poblacion)

        # calculo el mejor
        mejorFObjetivo = max(listaFObjetivo) # max porq esta inverso 
        if(mejorFObjetivo >= distMinima):    # cambio a mayor y distMin inicial = 0 
            distMinima = mejorFObjetivo
            MejorRecorrido = poblacion[listaFObjetivo.index(mejorFObjetivo)]

        # guardo los arreglos para generar las graficas
        if(mostrarGraficas):
            # guardo los mejores, peores y la media de esta generacion
            ejeX.append(cantidadCiclos)
            listaFObjetivoOriginal = list(map(lambda x: x**-1,listaFObjetivo))
            minimos.append(min(listaFObjetivoOriginal))
            maximos.append(max(listaFObjetivoOriginal))
            medias.append(statistics.mean(listaFObjetivoOriginal))
            mejorDistancia = int(distMinima**-1)
            minHistorico.append(mejorDistancia)


    if(mostrarGraficas):

        mostrarGraficasEnPantalla(ejeX, minimos, maximos, medias, minHistorico)

    return datos.mapearRecorrido(MejorRecorrido + [MejorRecorrido[0]]), datos.CalculaDistanciaDeRecorrido(MejorRecorrido)

# --------------------------- MAIN --------------------------- #


provincias = datos.provincias

print(" ----------------------------------------- ")
print(" 1 - Elegir provincia y realizar Heuristica")
print(" 2 - Mejor recorrido utilizando la Heuristica")
print(" 3 - Algoritmo Genético")
print(" ----------------------------------------- ")
op = input('Seleccione una opción: ')

if(op == '1'):
    capitalInicial = f.elegirCapital()
    recorrido, distTotal = greedy(capitalInicial)
if(op == '2'):
    recorrido, distTotal = MejorRecorrido(provincias)
if(op == '3'):
    recorrido, distTotal = Genetico(provincias)


f.realizarRecorrido(recorrido, distTotal)
