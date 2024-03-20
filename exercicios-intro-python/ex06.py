"""

Ex06. Crie um programa em Python que recebe como entrada o comprimento, altura e a largura de um aquário
      e calcule as seguintes informações.

    O volume do aquário em litros;
    A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo
    utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.

Utilize funções.

"""


class Valores:
    def __init__(self, altura, largura, comprimento, temperatura_desejada, temperatura_ambiente):
        self.altura = altura
        self.largura = largura
        self.comprimento = comprimento
        self.temperatura_desejada = temperatura_desejada
        self.temperatura_ambiente = temperatura_ambiente


def calcula_valores(volume=False, potencia=False, filtragem=False, valores: Valores = None):
    if volume:
        return valores.comprimento * valores.altura * valores.largura
    if potencia:
        return valores.comprimento * valores.altura * valores.largura * 0.05 * (
                    valores.temperatura_desejada - valores.temperatura_ambiente)
    if filtragem:
        return (valores.comprimento * valores.altura * valores.largura * 2, valores.comprimento * valores.altura *
                valores.largura * 3)


def formata_dados(volume=0.0, potencia=0.0, filtragem=(0.0, 0.0)):
    return (f'Volume: {volume} | Potencia: {abs(potencia)} | Filtragem (p/ hora): {filtragem[0]} mínima, '
            f'{filtragem[1]} máxima')


comprimento = float(input('Insira o comprimento: '))
altura = float(input('Insira a altura: '))
largura = float(input('Insira a largura: '))

temperatura_desejada = float(input('Insira a temperatuda desejada para o aquario: '))
temperatura_ambiente = float(input('Insira a temperatura amebiente: '))
valores = Valores(altura, largura, comprimento, temperatura_desejada, temperatura_ambiente)

volume = calcula_valores(volume=True, valores=valores)
potencia = calcula_valores(potencia=True, valores=valores)
filtragem = calcula_valores(filtragem=True, valores=valores)

print(formata_dados(volume, potencia, filtragem))
