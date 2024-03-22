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
    canditados[list(canditados.keys())[voto - 1]] += 1

print('\nRESULTADOS: \n')


canditadosList = list(sorted(canditados, key=canditados.get, reverse=True))
votosList = [canditados[i] for i in canditadosList]
if votosList[0] == votosList[1] == votosList[2]:
    print(f'{canditadosList[0]} ({canditados[canditadosList[0]]} votos) **EMPATADO**')
    print(f'{canditadosList[1]} ({canditados[canditadosList[1]]} votos) **EMPATADO**')
    print(f'{canditadosList[2]} ({canditados[canditadosList[2]]} votos) **EMPATADO**')
elif votosList[0] == votosList[1]:
    print(f'{canditadosList[0]} ({canditados[canditadosList[0]]} votos) **EMPATADO**')
    print(f'{canditadosList[1]} ({canditados[canditadosList[1]]} votos) **EMPATADO**')
    print(f'{canditadosList[2]} ({canditados[canditadosList[2]]} votos) ')
else:
    print(f'{canditadosList[0]} ({canditados[canditadosList[0]]} votos) **ELEITO**')
    print(f'{canditadosList[1]} ({canditados[canditadosList[1]]} votos) ')
    print(f'{canditadosList[2]} ({canditados[canditadosList[2]]} votos) ')