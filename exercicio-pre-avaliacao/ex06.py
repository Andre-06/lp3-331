"""

Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

"""


def conversor(nota):
    if nota < 60:
        return 'F'
    elif nota < 70:
        return 'D'
    elif nota < 80:
        return 'C'
    elif nota < 90:
        return 'B'
    elif nota <= 100:
        return 'A'

pontuacao = int(input('Insira sua pontuação: '))
print(f'Sua nota foi: {conversor(pontuacao)}')