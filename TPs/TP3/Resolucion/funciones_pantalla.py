# defino algunos colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
tamaño_circulo = 6
# ---
provincias = []
provinciaSeleccionada = ''



def elegirCapital():
    import os
    import datos
    provincias = datos.provincias
    os.system('cls')
    capital = input('Elija la capital inicial: ')
    for p in provincias:
        print (p[0])
        if p[0] == capital:
            return p


def realizarRecorrido(recorrido, dist):
    import os
    # doy el listado de como se recorrieron las provincias en consola.
    os.system("cls")
    print(" Las capitales se recorrieron en este orden:")
    for p in recorrido:
        print(' - ' + p[0])
    print()
    print(" Cantidad de Km recorridos: " + str(dist))
