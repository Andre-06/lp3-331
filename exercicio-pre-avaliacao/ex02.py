"""

Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

"""

num = int(input('Digite o multiplicador: '))
for i in range(1, 11): print(f'{num} x {i} = {i * num}') 