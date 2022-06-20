from itertools import chain, combinations
import pandas as pd
import tablas

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

for i in lista:
    iVi = i[2] / i[1]
    valores.append(iVi)

print(lista)
print(valores)


