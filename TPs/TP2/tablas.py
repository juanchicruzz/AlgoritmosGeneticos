import string
import pandas as pd
import xlsxwriter as xs

def guardarTabla(valores,titulo):
    tituloOP:string = 'AG_TP2_' + str(titulo.replace(" ","_").replace("/",""))
    workbook = xs.Workbook('D:/Visual Studio Code/Github/AlgoritmosGeneticos/TPs/TP2/ResultadosExhaustivo/' + tituloOP + '.xlsx')
    valores.to_excel(excel_writer='D:/Visual Studio Code/Github/AlgoritmosGeneticos/TPs/TP2/ResultadosExhaustivo/' + tituloOP + '.xlsx')
