# identificadores
# letras, numeros e _
# não pode ser palavras reservadas: if, None, True ...
# case sensitive

nome = "Pedro"
Nome = "Pedro"

# variáveis 
# tudo em minúsculo
# separador _
# snake_case

idade = 20
pessoa_fisica = "Marcio"
pessoa_juridica = "Paula"
imposto_de_renda_retido_na_fonte = 2200.45

# tipo
# python inferência de tipo
# tipo definido no valor literal

idade = 20 # int
nome = "Pedrão" # str

# constantes
# não existe constantes
# convenção: nome em maiúsculo

PI = 3.1415

# comentário de uma única linha

'''
    comentário de multiplas linhas
'''

# docstring (comentário de documentação)
# documentar classes, módulos, funções ...

'''
    public static somar(double numero1, double numero2) {
        return numero1 + numero2;
    }
'''

def somar(numero1: int, numero2: int):
    '''
        Função que soma dois números inteiros

        :param numero1: primeiro numero inteiro
        :param numero2: segundo numero inteiro
        :return: a soma dos dois números
    '''
    return numero1 + numero2

print(somar(1, 1))