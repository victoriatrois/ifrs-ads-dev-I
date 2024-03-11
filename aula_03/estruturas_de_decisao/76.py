# Questão 76. Faça um programa que leia a idade de uma pessoa e informe sua classe eleitoral:
# • Não eleitor (abaixo de 16 anos)
# • Eleitor obrigatório (entre 18 anos e 65 anos)
# • Eleitor facultativo (entre 16 e 18 anos e acima dos 65 anos)

try:
    idade_do_eleitor = int(input("Insira sua idade: "))

    if idade_do_eleitor < 0 or idade_do_eleitor > 120:
        raise ValueError("Invalid age. Please enter a realistic age.")
except ValueError as erro:
    print(erro)
else:
    if idade_do_eleitor < 16:
        print("Proibido votar.")
    elif 18 <= idade_do_eleitor <= 65:
        print("Voto obrigatório")
    else:
        print("Voto facultativo")