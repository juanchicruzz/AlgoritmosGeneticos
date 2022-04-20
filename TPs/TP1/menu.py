
import os
from PyInquirer import style_from_dict, Token, prompt, Separator

os.system ("cls")
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