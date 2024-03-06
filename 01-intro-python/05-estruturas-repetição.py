"""

>>> FOR - posicao 0 até a posicao final

for variavel_dinamica in lista:
    corpo

>>> range(start, stop, step)

range(5) => 0, 1, 2, 3, 4
range()

"""

for letra in 'Ola Mundo':
    print(letra)
    
prontutarios = ['SP1', 'SP2', 'SP3']

for prontuario in prontutarios:
    print(prontuario)
    
for i in range(5):
    print(i)    

for i in range(0, 12, 2):
    print(i)
    
lista = list(range(1, 101))

"""

>>> WHILE
 
contador = incio
WHILE contador < fim:
    corpo
    contador += 1

>>> BREAK - para o loop
>>> CONTINUE - para a iteração

"""

# comando = ''
# while True:   
#     if comando == 'sair':
#         break
#     if comando == '1':
#         print('baba')
#     if comando == '2':
#         print('boey')
        
    # comando = input('Digite um comando: ')  

numeros = [3, -1, 2, 0, -4, 5]
for numero in numeros:
    if numero < 0:
        continue
    print(numero)
    
for numero in numeros:
    if numero > 0:
        print(numero)
        
"""

>>> COMPREENSÃO DE LISTAS

lista_gerada = [variavel FOR variavel IN lista |IF condicao|]

"""
 
positivos = [numero for numero in numeros if numero > 0]
elevado_quadrado = [numero ** 2 for numero in numeros]


        

    