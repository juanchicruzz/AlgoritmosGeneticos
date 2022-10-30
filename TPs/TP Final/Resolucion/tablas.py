import string
import pandas as pd
import xlsxwriter as xs

def guardarTabla(listaMaximos,listaMinimos,listaPromedios,titulo):
    dfMaxi = pd.DataFrame (listaMaximos, columns = ['Maximos'])
    dfMin = pd.DataFrame (listaMinimos, columns = ['Minimos'])
    dfProm = pd.DataFrame (listaPromedios, columns = ['Promedios'])

    dfAux = dfMaxi.merge(dfMin,left_index= True,right_index=True)
    dfOP = dfAux.merge(dfProm,left_index= True,right_index=True)
    tituloOP:string = 'AG_TP1_' + str(titulo.replace(" ","_").replace("/",""))
    #workbook = xs.Workbook('E:/MaquinaVieja/UTN/6t0/Algoritmos Geneticos/AlgoritmosGeneticos/TPs/TP1/COLOQUIO/' + tituloOP + '.xlsx')
    #dfOP.to_excel(excel_writer='E:/MaquinaVieja/UTN/6t0/Algoritmos Geneticos/AlgoritmosGeneticos/TPs/TP1/COLOQUIO/' + tituloOP + '.xlsx')

    