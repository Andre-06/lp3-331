"""

Ex09 - Implemente o jogo termo:

REGRAS:

Objetivo:
    Descobrir o TERMO do dia (ou seja, a palavra do dia) em 6 tentativas.
Como jogar:
    Cada tentativa deve ser uma palavra de 5 letras.
    Para submeter a palavra, clique na tecla “Enter”.
    Feedback após cada tentativa:

A cor dos quadrados irá mudar de acordo com os seguintes exemplos:
    Verde: A letra está na palavra e está na posição correta.
    Amarelada: A letra está na palavra, mas está na posição errada.
    Cinzento: A letra não faz parte da palavra.

"""
import random

from colorama import Fore, Style

with open('dicionario.txt', 'r', encoding='utf-8') as dicionario:
    palavras = [linha.strip() for linha in dicionario]
    palavra = random.choice(palavras)

mensagem_inicial = lambda: print(f'''

JOGO TERMO

Descubra a palavra de 5 letras
A cor dos quadrados irá mudar de acordo com os seguintes exemplos:
    Verde: A letra está na palavra e está na posição correta.
    Amarelada: A letra está na palavra, mas está na posição errada.
    Cinzento: A letra não faz parte da palavra.

    {Fore.GREEN} C {Style.RESET_ALL} A  S {Fore.YELLOW} A {Style.RESET_ALL} R 
    
COMECE!
''')

quadro = lambda: print(f'''
   ++=================++
   ||  {tentativas[0]}  ||
   ||  {tentativas[1]}  ||
   ||  {tentativas[2]}  ||
   ||  {tentativas[3]}  ||
   ||  {tentativas[4]}  ||
   ||  {tentativas[5]}  ||
   ++=================++

''')

tentativas = [' '*13]*6
numero_tentativas = 0

mensagem_inicial()

while True:
    tentativa = input('Digite a palavra: ').strip().lower()

    while (not tentativa
           or len(tentativa) != 5
           or tentativa not in palavras):
        tentativa = input('Digite a palavra: ').lower()

    array_retorno = []
    for letra_correta, letra_tentativa in zip(palavra, tentativa):
        if letra_correta == letra_tentativa:
            array_retorno.append(f'{Fore.GREEN}{letra_tentativa.upper()}{Style.RESET_ALL}')
        elif letra_tentativa in palavra:
            array_retorno.append(f'{Fore.YELLOW}{letra_tentativa.upper()}{Style.RESET_ALL}')
        else:
            array_retorno.append(f'{Fore.LIGHTBLACK_EX}{letra_tentativa.upper()}{Style.RESET_ALL}')
    tentativas[numero_tentativas] = '  '.join(array_retorno)
    numero_tentativas += 1

    quadro()

    if tentativa == palavra:
        print('Acertou!')
        break
    elif numero_tentativas == 6:
        print('Mais sorte na próxima!')
        print('A palavra era: ' + palavra.upper())
        break


