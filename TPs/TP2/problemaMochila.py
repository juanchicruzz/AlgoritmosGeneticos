'''
Consiste en elegir, de entre un conjunto de n elementos, 
(cada uno con un valor $i, y un volumen Vi), 
aquellos que puedan ser cargados en una mochila 
de volumen V de manera que el valor obtenido sea máximo.

Cuáles son los elementos de la lista siguiente que 
cargaremos en una mochila de 4200 cm3 de manera que su 
valor en $ sea máximo.

'''
from itertools import chain, combinations
import pandas as pd

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



objetos = [
    ('1', 150, 20),
    ('2', 325, 40),
    ('3', 600, 50),
    ('4', 805, 36),
    ('5', 430, 25),
    ('6', 1200, 64),
    ('7', 770, 54),
    ('8', 60, 18),
    ('9', 930, 46),
    ('10', 353, 28),
]
mochilaMax = 4200

#exhaustivo

subsets = list(allSubsets(objetos))

listaConValores = [totalVolumeAndValue(el) for el in subsets]

dfValores = pd.DataFrame(listaConValores, columns=['elementos', 'valor', 'volumen'])

dfValores.sort_values(by=['valor'], ascending=False, inplace=True)
filtradoMax= dfValores[dfValores['volumen'] <= mochilaMax]

print("a")