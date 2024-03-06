## Operadores Aritiméticos
# Soma, Subtração, Multiplicação, Divisão, Resto da Divisão, Potenciação
#   + ,     -    ,      *       ,     /  ,        %        ,     **

nota1 = 10
nota2 = 6.5

media = (nota1 + nota2) / 2

# 2 elevado ao quadrado
potencial = 2 ** 2

# 2 elevado ao cubo
potencial2 = 2 ** 3

# Operadores de Atribuição
# =, +=, -= ...

idade = 17
idade += 10


# Operadores Lógicos
# and, or, not

# and              or
# 1 1 = 1       1 1 = 1          
# 1 0 = 0       1 0 = 1
# 0 1 = 0       0 1 = 1
# 0 0 = 0       0 0 = 0

# Operador de Comparação
# ==, !=, >, <, >=, <=

idade = 17
maior_de_idade = idade >= 18 

if maior_de_idade:
    print('Maior de Idade')
else:
    print('Menor de Idade')
    
# Operador is
# compara os valores do objeto e se ocupam mesmo espaço na memória

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

c = a
print(c is a)

# Opeador in e not in

print('a' in 'Java')
print('Maria' in ['Pedro', 'Ana'])

alunos = ['Pedro', 'Ana']
aluno = 'Maria'
print(aluno in alunos)
print(aluno not in alunos)