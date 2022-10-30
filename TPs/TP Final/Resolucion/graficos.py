from matplotlib import pyplot as plt

'''
 graficarLista:
    Funcion que recibe una lista de elementos (que poseen la corrida y el valor), y un titulo para el grafico.
    Se asignan los valores de las coordenadas x e y, se grafica, luego se agregan las leyendas y se muestra el grafico.
'''
def graficarLista(lista,titulo):
    plt.title(titulo)
    plt.ylabel('Función Objetivo')
    plt.xlabel('Corrida')
    plt.plot(lista, label='valores')  
    plt.legend()
    #plt.savefig('E:/MaquinaVieja/UTN/6t0/Algoritmos Geneticos/AlgoritmosGeneticos/TPs/TP1/COLOQUIO/' + 'AG_TP1_' + str(titulo.replace(" ","_").replace("/","")) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    #plt.savefig('D:/Visual Studio Code/Github/AlgoritmosGeneticos/TPs/TP1/OPG200/' + 'AG_TP1_' + str(titulo.replace(" ","_").replace("/","")) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()

def graficarConjunto(ejeX, minimos, maximos, media, titulo):
    plt.title(titulo)
    plt.plot(ejeX, minimos, label='Minimos', linewidth=2, color="red", alpha=0.6)
    plt.plot(ejeX, maximos, label='Maximos', linewidth=2, color="blue", alpha=0.6)
    plt.plot(ejeX, media, label='Media', linewidth=2, color="green", alpha=0.6)

    plt.legend()
    plt.ylabel(' Valor de la Funcion Objetivo ')
    plt.xlabel(' Generación ')
    plt.show()