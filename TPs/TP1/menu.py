
import os
from PyInquirer import style_from_dict, Token, prompt, Separator



# Limpieza de terminal.
os.system ("cls")

'''
menu:
    A traves de la libreria PyInquirier se crea un menu con las opciones de seleccion de estrategia, elitismo,
    y el numero de iteraciones deseadas, para luego ejecutar el programa.
'''

def menu():
    questions = [
        {
            'type': 'list',
            'name': 'estrategia',
            'message': 'Elija el tipo de seleccion que deseea utilizar',
            'choices': [
                'Seleccion de Ruleta',
                'Seleccion de Torneo',
            ],
            'filter': lambda val: val.lower()
        },
        {
            'type': 'list',
            'name': 'elitismo',
            'message': 'Desea realizar Elitismo?',
            'choices': [
                'SI',
                'NO'
                ],
            'filter': lambda val: val.lower()
        },
            {
            'type': 'input',
            'name': 'iteraciones',
            'message': 'Ingrese el número de iteraciones que desee',
            'validate': lambda val: int(val) >= 0 and int(val) <= 10000
        },
    ]
    answers = prompt(questions)
    return answers


x = menu()