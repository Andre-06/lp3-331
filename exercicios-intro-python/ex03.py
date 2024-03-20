"""

Ex03 - Crie um programa em Python que recebe como entrada o valor de uma compra e apresenta como 
saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:

    Compras entre R$ 0,01 e R$ 9,99 - 0% de desconto
    Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
    Compras entre R$ 100,00 e R$ 499,99 - 10% de desconto
    Compras iguais ou superiores a R$ 500,00 - 15% de desconto

"""

valor = float(input())
desconto = 0.0

if valor >= 10.0 and valor < 100.0:
    desconto = 0.05
elif valor < 500:
    desconto = 0.1
elif valor >= 500:
    desconto = 0.15
    
print(f'Desconto aplicado: {desconto * 100}%')
print('Valor Final: %.2f' % (valor * (1 - desconto)))
