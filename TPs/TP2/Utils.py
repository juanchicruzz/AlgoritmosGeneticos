import string
import xlsxwriter as xs

objetosVolumen = [
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

maxVolumen = 4200

objetosPeso= [
    ('1', 1800, 72),
    ('2', 600, 36),
    ('3', 1200, 60),
]

maxPeso = 3000

def guardarTabla(valores,titulo):
    tituloOP:string = 'AG_TP2_' + str(titulo.replace(" ","_").replace("/",""))
    workbook = xs.Workbook('E:/MaquinaVieja/UTN/6t0/Algoritmos Geneticos/AlgoritmosGeneticos/TPs/TP2/ResultadosExhaustivo/' + tituloOP + '.xlsx')
    valores.to_excel(excel_writer='E:/MaquinaVieja/UTN/6t0/Algoritmos Geneticos/AlgoritmosGeneticos/TPs/TP2/ResultadosExhaustivo/' + tituloOP + '.xlsx')
