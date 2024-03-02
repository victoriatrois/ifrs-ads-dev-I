# Questão 55. Todo restaurante, embora por lei não possa obrigar o cliente a pagar, cobra 10%
# para o garçom. Faça um programa que leia o valor gasto com as despesas realizadas em um
# restaurante e mostre o valor total com a gorjeta.
from common.utils import formata_moeda_br


def exibe_gorjeta():
    total_da_nota: float = float(input("Insira o quanto você gastou: "))
    gorjeta: float = formata_moeda_br(total_da_nota * 0.1)

    print(f'Do total gasto, R${gorjeta} foi de gorjeta.')


exibe_gorjeta()