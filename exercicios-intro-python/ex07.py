"""

Ex07. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma
calculadora em Python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o
indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso
para chegar no peso normal (imc = 24,9).

IMC = peso / altura * altura

Classificação
----------------------------------
IMC           Classificação
-----------------------------------
< 18,5         Baixo peso
18,5 a 24,9     Peso normal
25,0 a 29,9     Excesso de peso
30,0 a 34,9     Obesidade de Classe 1
35,0 a 39,9     Obesidade de Classe 2
>= 40,00      Obesidade de Classe 3

Utilize funções.

"""

def calcula_imc(peso, altura):
    return peso / (altura * altura)

def classificacao(peso, altura):
    imc = calcula_imc(peso, altura)

    if imc < 18.5:
        return 'Baixo peso'
    elif imc < 25:
        return 'Peso normal'
    elif imc < 30:
        return 'Excesso de peso'
    elif imc < 35:
        return 'Obesidade de Classe 1'
    elif imc < 40:
        return 'Obesidade de Classe 2'
    else:
        return 'Obesidade de Classe 3'


def kilos_ideal (peso, altura):
    IMC_IDEAL = 24.9
    """
    
    24.9 = peso / altura * altura
    peso = 24.9 * altura * altura
    
    """
    c = classificacao(peso, altura)
    if c == 'Peso normal':
        return IMC_IDEAL * altura * altura - peso

    return 0


peso = float(input('Seu peso (kg): '))
altura = float(input('Sua altura (m): '))

print(f'\nPeso: {peso} | Altura: {altura}\n{classificacao(peso, altura)} ({calcula_imc(peso, altura):.1f}) | '
      f'Kg para modificar: {kilos_ideal(peso, altura):.3f}')
