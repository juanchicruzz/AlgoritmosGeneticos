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
row = 0
for i in range(0,9):
    iVi = lista[i][2] / lista[i][1]
    lista[i] = (*lista[i], iVi)

print(lista)
