from matplotlib import pyplot as plt

'''
 graficarLista:
    Funcion que recibe una lista de elementos (que poseen la corrida y el valor), y un titulo para el grafico.
    Se asignan los valores de las coordenadas x e y, se grafica, luego se agregan las leyendas y se muestra el grafico.
'''
def graficarLista(lista,titulo):
    plt.title(titulo)
    plt.ylabel('Valor')
    plt.xlabel('Corrida')
    plt.plot(lista, label='valores')  
    plt.legend()
    #plt.savefig('C:/Users/franc/AppData/Local/Programs/Python ' + 'AG_TP1_' + str(titulo) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()