# 1. número

# int
idade = 20

# float
altura = 1.6

# complex
# cálculos com números complexos
numero_complexo = 1 + 2j

# 2. boolean
verdade = True
mentira = False

# sequencias
# String, lista, tuple, set, dict

# str
# conjunto de caracter
nome = 'Joao da Silva'
nome = 'Maria da Silva'

# str de múltiplas linhas
frase = """
Olá Mundinho!
Parabens
"""

# interpolação de str
nome = 'Maria'
idade = 78
mensagem = f'{nome} é uma pessoa legal! Ela tem {idade} anos.'

# char
# não existe
# usar string de tamanho 1

letra = 'A'

# Acessar caracter em string
nome = 'Silvio Santos'
print(nome[9]) # >>> l

# Métodos str

print(nome.upper()) # >>> SILVIO SANTOS
print(nome.lower()) # >>> silvio santos
print(nome.capitalize()) # >>> Silvio santos
print(len(nome)) # >>> 13
print(nome.count('o')) # >>> 2
print(nome.split('o')) # >>> ['Silvi', ' Sant', 's']
print(nome.replace('S', 'K')) # >>> Kilvio Kantos
print(nome.endswith('tos')) # >>> True


# list
# lista de valores
# permite diferentes tipos de dados na mesma lista

habilidades = ['pyhton', 'java', 'javascript']

print(habilidades[1]) # >>> java

for habilidade in habilidades:
    print(habilidade)

# adiciona, insere e remove
habilidades.append('css') # ['pyhton', 'java', 'javascript', 'css']

habilidades.insert(3, 'html') # ['pyhton', 'java', 'javascript', 'html', 'css']

habilidades.remove('css') # ['pyhton', 'java', 'javascript', 'html']

# tuple
# "lista" de valores
# não pode ser alterada
opcoes = ('sim', 'não', 'talvez')
rpg_racas = ('humano', 'elfo', 'anão', 'tiefiling')

def estatistica_notas(notas: list[float]):
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    
    return (maior_nota, menor_nota, round(media, 2))

notas = [10, 3.5, 7.4]
estatistica = estatistica_notas(notas)
print(estatistica)

maior, menor, media = estatistica
print(maior, menor, media)

# set
# conjunto de valores
# não é indexado
# permite elementos duplicados

habilidades = {'java', 'python'}
habilidades.add('js')
habilidades.add('java')
print(habilidades)

print([item for item in habilidades][2])

# dict
# palavra -> definição
# chave -> valor
# key -> value

nome = 'Silvio'
idade = 89
patrimonio = 2_000_000_000
altura = 170

pessoa = {
    nome: 'Silvio',
    idade: 89,
    patrimonio: 2_000_000_000,
    altura: 1.7
}

print(pessoa[patrimonio])

# None
# variaveis que serão inicializadas em tempo de execução (JIT)
# retorno ou parametros de função
nulo = None