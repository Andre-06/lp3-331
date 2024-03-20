"""

Ex04 - O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a 
sequência de caracteres BR, em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.

Exemplos válidos:

    BR0001X
    BR1236X
    BR9999X

Exemplos inválidos:

    br0001X
    BR126X
    BR99999X
    BR9999Y
    
Crie uma função em Python que implementa essa verificação
    

"""
import random


def verificar_codigo(codigo: str):
    if len(codigo) != 7:
        return False
    if not codigo.startswith('BR'):
        return False
    if not any(i.isdigit() for i in codigo[2:5]):
        return False
    if not codigo.endswith('X'):
        return False

    return True


__init__ = ''

if __init__ == '__init__':
    validos = ['BR0001X', 'BR1236X', 'BR9999X']
    invalidos = ['br0001X', 'BR126X', 'BR99999X', 'BR9999Y']
    mistura = validos + invalidos
    random.shuffle(mistura)

    [print(f'{codigo}: {verificar_codigo(codigo)}') for codigo in mistura]
