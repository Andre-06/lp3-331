"""

Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário 
onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
Depois, teste a função com diferentes textos fornecidos pelo usuário. 

"""
import re

casos_ignorados = {'9', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'e', 'que', 'nos', 'umas', 'praquele', 'neste', 'aos', 'esse', 'nelas', 'para', 'a', 'ao', 'nisto', 'nisso', 'uma', 'aquilo', 'ele', 'os', 'disto', 'o', 'ante', 'nuns', 'naquele', 'pelo', 'per', 'um', 'àquilo', 'trás', 'sob', 'à', 'nas', 'uns', 'pros', 'numas', 'daquilo', 'pelos', 'disso', 'das', 'praquilo', 'pela', 'de', 'entre', 'deles', 'pro', 'isto', 'aquele', 'neles', 'daquele', 'pra', 'num', 'àquele', 'delas', 'às', 'pras', 'após', 'até', 'desde', 'eles', 'naquilo', 'dum', 'em', 'as', 'isso', 'elas', 'sem', 'nesse', 'dela', 'da', 'duma', 'do', 'deste', 'por', 'dos', 'ela', 'desse', 'pelas', 'sobre', 'contra', 'no', 'este', 'nele', 'dumas', 'perante', 'nela', 'duns', 'dele', 'numa', 'com', 'na'}

input('Pressione qualquer tecla para prosseguir e aguarde carregamento... ')

with open('texto.txt', 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.read()

texto = re.sub(r'[^\w\s]', '', arquivo)
texto = texto.lower()
texto = (re.findall
         (r'\b\w+\b', texto))

dicionario = dict()
for i in set(texto):
    if i not in casos_ignorados and not i.startswith('http'):
        dicionario[i] = texto.count(i)

print('RESULTADOS')

for i in sorted(dicionario, key=dicionario.get, reverse=True):
    print(i + ': ' + str(dicionario[i]))
