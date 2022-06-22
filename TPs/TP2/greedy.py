import pandas as pd
import Utils as U

def EjecutaGreedy(vol:bool):

    #vol -> flag que permite cambiar entre problema 1 o 2.

    if (vol):
        objetos = U.objetosVolumen
        mochilaMax = U.maxVolumen
    else:
        objetos = U.objetosPeso
        mochilaMax = U.maxPeso

    ''' Recorre la lista de objetos y la aplica la funcion heuristica
        y lo agrega a la tupla. '''

    lista = list(objetos)
    for i in range(0,len(objetos)):
        iVi = lista[i][2] / lista[i][1]
        lista[i] = (*lista[i], iVi)

    # Trasforma la lista en una TABLA y ordena de mayor a menos por el ivi.

    dfValores = pd.DataFrame(lista, columns=['elemento', 'volumen', 'valor','iVi'])
    dfValores.sort_values(by=['iVi'], ascending=False, inplace=True)

    resultado = []
    vActual = 0
    valorTotal = 0

    ''' Recorre la tabla de objetos y los agrega al resultado final si y solo si, la suma de 
        los volumenes no supera el maximo de la mochila.
        si supera, no lo agrega y sigue con el proximo elemento. '''

    for index, row in dfValores.iterrows():

        if( (vActual+row['volumen']) <= mochilaMax):
            resultado.append(row['elemento'])
            vActual = vActual + row['volumen']
            valorTotal = valorTotal + row['valor']

    print(resultado)
    print(vActual)
    print(valorTotal)



