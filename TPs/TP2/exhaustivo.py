from itertools import chain, combinations
import pandas as pd
import Utils as U


def allSubsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1 ,len(s)+1))


def totalVolumeAndValue(lista):
    total_volume = 0
    total_value = 0
    elementos = ""
    for i in lista:
        total_volume += i[1]
        total_value += i[2]
        elementos = elementos + i[0] + ", "
    return [elementos, total_value, total_volume]

#objeto = [numero,volumen,valor]

if (False):
    objetos = U.objetosVolumen
    mochilaMax = U.maxVolumen
else:
    objetos = U.objetosPeso
    mochilaMax = U.maxPeso




#exhaustivo

subsets = list(allSubsets(objetos))
#print(subsets)

listaConValores = [totalVolumeAndValue(el) for el in subsets]

dfValores = pd.DataFrame(listaConValores, columns=['elementos', 'valor', 'volumen'])

dfValores.sort_values(by=['valor'], ascending=False, inplace=True)

filtradoMax= dfValores[dfValores['volumen'] <= (mochilaMax)]

print(filtradoMax)


#U.guardarTabla(filtradoMax,"resultados")



