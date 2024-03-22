"""

Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo 
(ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

"""

palindromo = lambda palavra: print('É palíndromo' if palavra.replace(' ', '') == palavra.replace(' ', '')[::-1] else 'Não é palíndromo')
palindromo(input('Digite uma palavra: '))