"""

Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, 
no final, mostrar o número de votos de cada candidato e quem foi o vencedor. 

"""

mensagem = '''
VOTE NO SEU CANDIDATO:

LUK CHO MAN - DIGITE 1
CLAUDETE SILVA - DIGITE 2
LATORRE DOS SANTOS - DIGITE 3

'''

canditados = {
    'LUK CHO MAN': 0,
    'CLAUDETE SILVA': 0,
    'LATORRE DOS SANTOS': 0
}

print(mensagem)
for i in range(10): 
    voto = int(input('Seu voto: '))
    print(list(canditados.keys))
    canditados[[canditados.keys][voto - 1]] += 1

print(sorted(canditados, key=canditados.get, reverse=True))

print('RESULTADOS\n')
    



    