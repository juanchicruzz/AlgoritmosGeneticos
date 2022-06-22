from itertools import chain, combinations
import pandas as pd
import Utils as U


'''
Genera todos los subconjuntos existentes del conjunto de objetos. (conjunto potencia)

combinations(s, r) -> devuelve todas las combinaciones de r elementos de s.
por lo tanto repetimos esto variando r de 1 a len(s)+1. 
+1 porque Range(1,10) seria [1,2,3,4,5,6,7,8,9]
entonces debemos agregar uno para llegar a toda la extencion del conjunto.
'''

def allSubsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1 ,len(s)+1))


'''
Recibe como parametro un subconjunto de objetos.
Devuelve el Volumen y el Valor total de los objetos y la lista de objetos
incluida en el subconjunto.
'''

def totalVolumeAndValue(lista):
    total_volume = 0
    total_value = 0
    elementos = ""
    for i in lista:
        total_volume += i[1]
        total_value += i[2]
        elementos = elementos + i[0] + ", "
    return [elementos, total_value, total_volume]


def EjecutaExhaustivo(vol:bool):

    '''
        vol -> flag que permite cambiar entre problema 1 o 2.
    '''
    if (vol):
        objetos = U.objetosVolumen
        mochilaMax = U.maxVolumen
    else:
        objetos = U.objetosPeso
        mochilaMax = U.maxPeso


    subsets = list(allSubsets(objetos))

    '''
        Recorre los subconjuntos y le aplica la funcnion totalVolumeAndValue.
        devolviendo una lista de los resultados (elementos del subconjunto, volumen total y valor total)
    '''

    listaConValores = [totalVolumeAndValue(el) for el in subsets]

    dfValores = pd.DataFrame(listaConValores, columns=['elementos', 'valor', 'volumen'])

    '''
        Ordena la tabla de valores de mayor a menor por el valor total.
        Filtra la tabla por volumenes menores al maximo de la mochila.
    '''

    dfValores.sort_values(by=['valor'], ascending=False, inplace=True)

    filtradoMax= dfValores[dfValores['volumen'] <= (mochilaMax)]

    print(filtradoMax)




