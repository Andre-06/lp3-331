from ex04 import verificar_codigo

"""

Ex05 - Crie um programa em Python que solicita ao usuário um identificador e apresenta se o que foi 
informado é um valor válido ou inválido.

"""

codigo = input('Insira o código: ')
print('Código Válido' if verificar_codigo(codigo) else 'Código Inválido')
Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.