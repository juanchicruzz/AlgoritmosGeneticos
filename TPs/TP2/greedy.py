from itertools import chain, combinations
import pandas as pd
import Utils as U

# Funciones de greedy 

#Objeto - numero , volumen , valor

if (False):
    objetos = U.objetosVolumen
    mochilaMax = U.maxVolumen
else:
    objetos = U.objetosPeso
    mochilaMax = U.maxPeso


lista = list(objetos)
valores = []
for i in range(0,len(objetos)):
    iVi = lista[i][2] / lista[i][1]
    lista[i] = (*lista[i], iVi)


dfValores = pd.DataFrame(lista, columns=['elemento', 'volumen', 'valor','iVi'])
dfValores.sort_values(by=['iVi'], ascending=False, inplace=True)
print(dfValores)
resultado = []
vActual = 0
valorTotal = 0
for index, row in dfValores.iterrows():

    if( (vActual+row['volumen']) <= mochilaMax):
        resultado.append(row['elemento'])
        vActual = vActual + row['volumen']
        valorTotal = valorTotal + row['valor']


print(resultado)
print(vActual)
print(valorTotal)



