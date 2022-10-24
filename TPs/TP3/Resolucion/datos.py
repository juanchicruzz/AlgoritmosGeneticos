import os
import pandas as pd
import math



provincias = [
    # Capital, posEnExcel
    ("Cdad. de Bs. As.", 0, 534, 374),
    ("Córdoba", 1, 400, 280),
    ("Corrientes", 2, 537, 185),
    ("Formosa", 3, 549, 142),
    ("La Plata", 4, 550, 395),
    ("La Rioja", 5, 320, 234),
    ("Mendoza", 6, 277, 331),
    ("Neuquén", 7, 295, 494),
    ("Paraná", 8, 490, 300),
    ("Posadas", 9, 623, 179),
    ("Rawson", 10, 370, 610),
    ("Resistencia", 11, 533, 170),
    ("Río Gallegos", 12, 312, 844),
    ("S.F.d.V.d. Catamarca", 13, 357, 206),
    ("S.M. de Tucumán", 14, 361, 153),
    ("S.S. de Jujuy", 15, 366, 88),
    ("Salta", 16, 364, 104),
    ("San Juan", 17, 286, 292),
    ("San Luis", 18, 347, 338),
    ("Santa Fe", 19, 485, 285),
    ("Santa Rosa", 20, 390, 427),
    ("Sgo. Del Estero", 21, 420, 170),
    ("Ushuaia", 22, 328, 927),
    ("Viedma", 23, 418, 545),
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

    #distancia del recorrido se le sume la vuelta.
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
