from matplotlib import pyplot as plt

def graficarLista(lista,titulo):
    plt.title(titulo)
    plt.ylabel('Valor')
    plt.xlabel('Corrida')
    plt.plot(lista, label='valores')  
    plt.legend()
    #plt.savefig('C:/Users/franc/AppData/Local/Programs/Python ' + 'AG_TP1_' + str(titulo) + '.png', quality = 100, format = 'png', bbox_inches = 'tight', dpi = 100)
    plt.show()