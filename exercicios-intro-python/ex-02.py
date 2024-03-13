# Ex02 - Escreva um programa em Python que solicita ao usuário três números e 
# apresenta a média aritmética dos números informados.

nums = [float(i) for i in input().split(' ')]
print('Media: ' + str(sum(nums) / len(nums)))
