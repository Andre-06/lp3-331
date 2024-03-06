"""

if, if/else, if, elif, else, ternario, match

>>> IF

if condicao:
    corpo
    corpo
    corpo    
    
""" 

idade = 20
if idade >= 18:
    print('Maior de Idade')


"""

>>> IF ELSE

if condicao:
    corpo
    corpo
else:
    corpo
   
"""

idade = 15
if idade >= 18:
    print('Maior de Idade')
else:
    print('Menor de Idade')


"""

>>> ELIF

if condicao:
    corpo
elif:
    corpo
else:
    corpo

>>> crianca (0 - 12), adolescente (13 - 17), adulto (18 - 59), idoso (60+)

"""

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')
    
"""

>>> IF ANINHADO (EVITAR)

if condicao:
    if condicao:
        if condicao:
        else:
    else:
else:

if condicao and condicao and condicao:
    corpo
else:
    corpo

"""    

email = 'foo@bar.com'
senha = 'foobar1232'

if email == 'foo@bar.com':
    if senha == 'foobar1234':
        print('Acesso Liberado')
    else:
        print('Email ou Senha Incorreto')
else:
    print('Email ou Senha Incorreto')


if email == 'foo@bar.com' and senha == 'foobar1232':
    print('Acesso Liberado')
else:
    print('Acesso Negado')


"""

>>> condicao complexa dentro do IF
>>> permitir a entrada se:
>>> o usuario nao estiver bloqueado E 
>>> usuario for um funcionario E
>>> hora atual entre 08 e 18
>>> OU usuario for admin

"""

usuario_bloqueado = False
usuario_fulcionario = True
hora_atual = 22
usuario_admin = False

if usuario_admin or ((hora_atual > 8 and hora_atual < 18) and usuario_fulcionario and not usuario_bloqueado):
    print('Acesso Liberado')
else:
    print('Acesso Negado')

usuario_admin = True
    
horario_comercial = hora_atual >= 8 and hora_atual <= 18
usuario_ativo = usuario_fulcionario and not usuario_bloqueado
liberado = usuario_admin or (horario_comercial and usuario_ativo)

if liberado:
    print('Acesso Liberado')
else:
    print('Acesso Negado')
    
"""

>>> OPERADOR TERNÁRIO   

variavel = condicao_verdadeira IF condicao ELSE condicao_falsa

"""

status = 'maior' if idade >= 18 else 'menor'

""" 

Usuario passa o dia e quer saber que dia da semana é
1- Domingo, 2 - Segunda ...

"""

dias_da_semana = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
}

dia = 3

if dia in dias_da_semana: print(dias_da_semana[dia])

"""

>>> MATCH 

MATCH variavel:
    CASE condicao1:
        corpo
    CASE condicao2:
        corpo
    CASE condicao3:
        corpo
    CASE condicao4:
        corpo
    CASE condicao5:
        corpo
    CASE condicao6:
        corpo
    CASE _:
        default

"""

dia = 7

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Valor Inválido')

match     dia:
    case 1 | 7:
        print('Final de Semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia Útil')
    case _:
        print('Valor Inválido')

