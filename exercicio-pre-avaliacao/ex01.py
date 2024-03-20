import random

"""

Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

"""

numero = random.randint(1, 100)

while True:
    escolha = int(input('Adivinhe o número: '))
    
    if numero == escolha:
        break
    
    print('Mais alto' if numero > escolha else 'Mais baixo')
    
print('Você acertou!')