from itertools import chain, combinations
import pandas as pd
import tablas

# Funciones de greedy 

#Objeto - numero , volumen , valor

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
lista = list(objetos)
valores = []
for i in range(0,10):
    iVi = lista[i][2] / lista[i][1]
    lista[i] = (*lista[i], iVi)


dfValores = pd.DataFrame(lista, columns=['elemento', 'volumen', 'valor','iVi'])
dfValores.sort_values(by=['iVi'], ascending=False, inplace=True)

resultado = []
vActual = 0
valorTotal = 0
for index, row in dfValores.iterrows():
    if vActual <= mochilaMax:
        if( (vActual+row['volumen']) <= mochilaMax):
            resultado.append(row['elemento'])
            vActual = vActual + row['volumen']
            valorTotal = valorTotal + row['valor']
    else: continue

print(resultado)
print(vActual)
print(valorTotal)

