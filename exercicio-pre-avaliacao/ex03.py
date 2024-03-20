import unicodedata
import re

"""

Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

"""

vogais = ['a', 'e', 'i', 'o', 'u']
vogais_quantas = 0

frase = unicodedata.normalize('NFKD', input('Digite uma frase: ')).encode('ASCII','ignore').decode('ASCII').lower()

fraseNegativa = re.sub('[a-z ]', '', frase)
print(fraseNegativa)
frase = [i for i in frase if i not in fraseNegativa]


for i in vogais:
    vogais_quantas += frase.count(i)
    
print(f'VOGAIS: {vogais_quantas} \nCONSOANTES: {len(frase) - vogais_quantas}')