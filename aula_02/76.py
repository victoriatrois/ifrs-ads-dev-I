# Questão 76. Desenvolva um programa que, dado um número de conta-corrente com três dígitos,
# retorna o valor do dígito verificador, o qual é calculado da seguinte forma:
#   Exemplo: número da conta: 235
#
# • Somar o número da conta com o seu inverso: 235 + 532 = 767
# • Multiplicar cada dígito pela sua ordem posicional e somar estes resultados:
#       7 6 7 (7 * 1) + (7 * 2) + (7 * 3) = 40
# • O último digito desse resultado é o dígito verificador da conta (40 -> 0)
from common.utils import inverte_numero

def calcula_digito_verificador(numero_intermediario):
    digito_verificador = 0
    posicao = 1

    for digito in str(numero_intermediario):
        digito_verificador += int(digito) * posicao
        posicao += 1

    return digito_verificador


def exibe_digito_verificador():
    numero_da_conta = int(input("Insira o número da conta: "))
    inverso_do_numero_da_conta = inverte_numero(numero_da_conta)
    numero_intermediario = numero_da_conta + inverso_do_numero_da_conta
    digito_verificador = calcula_digito_verificador(numero_intermediario)

    print(f'O digito verificador é {digito_verificador}.')


exibe_digito_verificador()