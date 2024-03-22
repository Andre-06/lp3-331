"""

Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) 
e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

"""
import random

frames = [
    '''
 _______
 |     |
 |    ( )   
 |  
 |    
 |
---
    ''',
    '''
 _______
 |     |
 |   (._.)   
 |  
 |    
 |
---
    ''',
    '''
 _______
 |     |
 |   (._.)   
 |     |
 |    
 |
---
    ''',
    '''
 _______
 |     |
 |   (._.)   
 |  >--|
 |    
 |
---
    ''',
    '''
 _______
 |     |
 |   (._.)   
 |  >--|--<
 |    
 |
---
    ''',
    '''
 _______
 |     |
 |   (._.)   
 |  >--|--<
 |    / 
 |
---
    ''',
    '''
 _______
 |     |
 |   (x_x)   
 |  >--|--<
 |    / \\
 |
---
    '''
]

print('''
JOGO DA FORCA
Descubra as letras que formam a palavra antes do bonequinho ser desfalecido

TEMA: Animais

 _______
 |     |
 |    ( )   
 |  
 |    
 |
---
''')

dicionario = [
    "piranha",
    "chinchila",
    "caracol",
    "cavalo-marinho",
    "búfalo",
    "arraia",
    "javali",
    "orangotango",
    "gato",
    "girafa",
    "estrela-do-mar",
    "atum",
    "hipopótamo",
    "bugio",
    "avestruz",
    "pinguim",
    "iguana",
    "lebre",
    "carpa",
    "lesma",
    "peixe-espada",
    "lince",
    "alce",
    "atum",
    "jiboia",
    "hipopótamo",
    "coruja",
    "tubarão",
    "urubu"
]

palavra = random.choice(dicionario)
erros = set()
acertos = ['_' if i != '-' else '-' for i in palavra]

while True:
    print('Palavra: ' + ''.join(acertos))
    print('Erros: ' + ' - '.join(erros))

    if '_' not in acertos:
        print('\nAcertou!')
        break
    if len(erros) == 6:
        print('\nMais sorte na próxima!')
        print('A resposta era: ' + palavra)
        break

    texto_input = input('Digite a letra ou palavra da forca: ')
    while not texto_input or not texto_input.strip():
        texto_input = input('Digite a letra ou palavra da forca: ')

    for letra in texto_input:
        if letra in palavra:
            acertos = [i if i == letra and j == '_' else '_' if j == '_' else j for i, j in zip(palavra, acertos)]
        else:
            erros.add(letra)

    print(frames[len(erros)])


