# Questão 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
from common.utils import formata_moeda_br


def calcula_salario():
    valor_ganho_por_hora: float = float(input("Insira quanto você ganha por hora: "))
    total_de_horas_trabalhadas: float = float(input("Insira o total de horas que você trabalha no mês: "))
    salario_bruto: float = valor_ganho_por_hora * total_de_horas_trabalhadas

    print(f'Você ganha R${formata_moeda_br(salario_bruto)} por mês.')


calcula_salario()
