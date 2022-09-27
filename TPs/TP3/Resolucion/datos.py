import os
import pandas as pd
import math

provincias = [
    # Capital, posEnExcel
    ("Cdad. de Bs. As.", 0),
    ("Córdoba", 1),
    ("Corrientes", 2),
    ("Formosa", 3),
    ("La Plata", 4),
    ("La Rioja", 5),
    ("Mendoza", 6),
    ("Neuquén", 7),
    ("Paraná", 8),
    ("Posadas", 9),
    ("Rawson", 10),
    ("Resistencia", 11),
    ("Río Gallegos", 12),
    ("S.F.d.V.d. Catamarca", 13),
    ("S.M. de Tucumán", 14),
    ("S.S. de Jujuy", 15),
    ("Salta", 16),
    ("San Juan", 17),
    ("San Luis", 18),
    ("Santa Fe", 19),
    ("Santa Rosa", 20),
    ("Sgo. Del Estero", 21),
    ("Ushuaia", 22),
    ("Viedma", 23),
]

# leo los datos del excel y los meto en la variable datos
dir_file = os.path.dirname(os.path.abspath(__file__))
dir_db = dir_file + "\TablaCapitales.xlsx"
datos = pd.read_excel(r"{}".format(dir_db))

# los datos se pueden llamar de la forma: data[0][0]
# o con el nombre del renglón data['Córdoba'][0]


def CalculaDistancia(provA, provB):
    global datos
    return datos[provA[0]][provB[1]]


def CalculaProvMinDistancia(provA, arrayRepetidos):
    global datos
    prov = provA[0]

    provinciaMasCercana = ''
    distMin = math.inf

    # busco entre todas las distancias la mas corta.
    for p in provincias:
        dist = datos[prov][p[1]]
        if(0 < dist < distMin):
            if(p not in arrayRepetidos):
                provinciaMasCercana = p
                distMin = dist

    # devuelvo la provincia mas cercana y la distancia.
    return provinciaMasCercana, distMin

def mapearRecorrido(recorridoNumerico):
    recorrido = []
    for n in recorridoNumerico:
        recorrido.append(provincias[n])
    return recorrido

def CalculaDistanciaDeRecorrido(r):
    global datos

    # antes de nada, hago que a la distancia del recorrido se le sume la vuelta.
    recorridoNumerico = r + [r[0]]

    distTotal = 0
    # tengo que "mapear" el recorrido, porque lo recibí en numeros.
    recorrido = mapearRecorrido(recorridoNumerico)

    for i in range(len(recorrido) - 1):
        pActual = recorrido[i]
        pProx = recorrido[i + 1]
        dist = datos[pActual[0]][pProx[1]]
        distTotal += dist
    return distTotal
