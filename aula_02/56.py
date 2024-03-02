# Questão 56. Para vários tributos, a base de cálculo é o salário mínimo. Faça um programa que
# leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcule e mostre quantos
# salários mínimos a pessoa ganha.

def analisa_salario():
    salario_do_usuario: float = float(input("Digite o seu salário bruto: "))
    salario_minimo: float = float(input("Digite o salário mínimo do seu país: "))

    porcentagem_do_salario_em_relacao_ao_minimo = 100 * salario_do_usuario / salario_minimo
    quantidade_de_salarios_minimos = porcentagem_do_salario_em_relacao_ao_minimo / 100

    if salario_minimo == salario_do_usuario:
        print("Você recebe um salário mínimo.")
    elif salario_do_usuario < salario_minimo:
        print(f'Você ganha {quantidade_de_salarios_minimos:.2f} salário mínimo.')
    else:
        print(f'Você ganha {quantidade_de_salarios_minimos:.2f} salários mínimos.')


analisa_salario()
