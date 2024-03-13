"""

>>> FUNÇÃO
>>> modularizar o programa; encapsular o código; reuso; manuteabilidade

>>> DECLARAÇÃO:

def nome_da_funcao (entrada1, entrada2 ...):
    corpo
    da
    funcao
    
    return retorno

>>> Exemplo1: SÓ PODE ACESSAR SE A HORA ESTIVER ENTRE 8H E 18H

"""

hora_atual = 12

# Estagiario
if hora_atual >= 8 and hora_atual <= 18:
    print("Permitido ao acesso")
    
# Junior
def dentro_do_horario_comercial (hora_atual: int):
    if hora_atual >= 8 and hora_atual <= 18:
        return True
    else:
        return False
    
# Pleno
def dentro_do_horario_comercial (hora_atual: int):
    return hora_atual >= 8 and hora_atual <= 18

# Senior  
dentro_do_horario_comercial = lambda hora_atual: hora_atual >= 8 and hora_atual <= 18

"""

>>> FUNCAO SEM RETORNO
>>> side effect - efeito colateral: altera a execução do código ou de uma variável global; 

>>> Exemplo: funcao que printa algo, só vai funcionar dentro do terminal do Visual Studio

enviar_email(montar_frase(nome)) 
enviar_email(diga_ola(nome)) -> Nao Funciona

"""

def diga_ola(nome):
    print(f'Ola, {nome}')
    
def monta_frase(nome):
    return f'Ola, {nome}'


diga_ola('Latorre')
print(monta_frase('Latchorre'))

""" 

>>> PARAMETROS E ARGUMENTOS
>>> Parametros: referencias da função que podem ser acessada dentro da funcao
>>> Argumentos: os valores passados pela funcao para o paramentro

def somar(PAREMENTRO1, PAREMETRO2):
    return a + b
    
somar(ARGUMENTO1, ARGUMENTO2)

>>> Paramentros com valor padrao

def funcao (parametro = valor_padrao):
    corpo

"""
    
def somar(a, b):
    return a + b

somar(10.2, 5.9)

def montar_mensagem (mensagem= 'Bom dia', nome= 'Tristeza'):
    return f'{mensagem}, {nome}'

print(montar_mensagem('Sejam Bem', 'viados'))
print(montar_mensagem())
print(montar_mensagem(nome='Marcos'))

"""

>>> Escopo de variavel

def funcao():
    var = 12
    
print(var) -> não funciona, ta no escopo global e var no escopo local

"""

def calcular_media(nota1, nota2, nota3):
    media = sum(nota1, nota2, nota3) / 3
    return media

# print(media)

total = 0
def soma_tres(num1, num2, num3):
    # global total
    total = num1 + num2 + num3
    return total

print(total)
soma_tres(1, 4, 5)
print(total)

"""

>>> DOCSTRING: Comentário para documentação de funções e arquivos

"""

def somar(numero1: int, numero2: int):
    """_summary_

    Função que soma dois números inteiros

    Args:
        numero1 (int): primeiro numero inteiro
        numero2 (int): segundo numero inteiro

    Returns:
        int: a soma dos dois números
    """
    return numero1 + numero2

"""

>>> Funcoes Built In: funcoes que ja existem no python por padrao

>>> type(var): retorna o tipo da variavel

type('Mariazinha')
-> <class 'string'> 

>>> len(var): retorna o tamanho da variavel

len([1, 2, 300])
-> 3

>>> sum(list): soma os valores da lista

sum([1, 2, 2])
-> 5

>>> max(list): maior item da lista

max([1, 2, 2])
-> 2

>>> min(list): menor item da lista

min([1, 2, 2])
-> 1

>>> input(string): recebe uma informação do ususario pelo terminal

print(Ola input('nome: '))
-> Nome: marcos
-> Ola Marcos

"""