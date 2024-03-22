"""

Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário 
onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. 
Depois, teste a função com diferentes textos fornecidos pelo usuário. 

"""
import re

CASOS_IGNORADOS = {'9', '8', '7', '6', '5', '4', '3', '2', '1', '0', 'e', 'que', 'nos', 'umas', 'praquele', 'neste', 'aos', 'esse', 'nelas', 'para', 'a', 'ao', 'nisto', 'nisso', 'uma', 'aquilo', 'ele', 'os', 'disto', 'o', 'ante', 'nuns', 'naquele', 'pelo', 'per', 'um', 'àquilo', 'trás', 'sob', 'à', 'nas', 'uns', 'pros', 'numas', 'daquilo', 'pelos', 'disso', 'das', 'praquilo', 'pela', 'de', 'entre', 'deles', 'pro', 'isto', 'aquele', 'neles', 'daquele', 'pra', 'num', 'àquele', 'delas', 'às', 'pras', 'após', 'até', 'desde', 'eles', 'naquilo', 'dum', 'em', 'as', 'isso', 'elas', 'sem', 'nesse', 'dela', 'da', 'duma', 'do', 'deste', 'por', 'dos', 'ela', 'desse', 'pelas', 'sobre', 'contra', 'no', 'este', 'nele', 'dumas', 'perante', 'nela', 'duns', 'dele', 'numa', 'com', 'na'}
def contagem_palavras(arquivo):
    texto = re.sub(r'[^\w\s]', '', arquivo)
    texto = texto.lower()
    texto = (re.findall
             (r'\b\w+\b', texto))

    dicionario = dict()
    for i in set(texto):
        if i not in CASOS_IGNORADOS:
            dicionario[i] = texto.count(i)

    return {i: dicionario[i] for i in sorted(dicionario, key=dicionario.get, reverse=True)}


input('Pressione enter para prosseguir e aguarde carregamento... ')
with open('texto.txt', 'r', encoding='utf-8') as arquivo:
    arquivo = arquivo.read()

resultado = contagem_palavras(arquivo)
resultado_ordenado = {}
for i in resultado:
    if resultado[i] not in resultado_ordenado.keys():
        resultado_ordenado[resultado[i]] = list()

    resultado_ordenado[resultado[i]].append(i)

for i in sorted(resultado_ordenado, reverse=True):
    print(f'{i} -> {sorted(resultado_ordenado[i])}')
