# Questão 72. Ler um número inteiro com 3 casas decimais e mostrar se o algarismo da casa das 3
# centenas é par ou ímpar.

while True:
    try:
        numero_a_analisar = input("Insira um número com 3 casas decimais: ")
        casas_decimais = numero_a_analisar.split(".")[1]
        if len(casas_decimais) != 3:
            raise ValueError("\nValor inválido")

        casas_decimais = int(casas_decimais[2])

        if casas_decimais % 2 == 0:
            print("O algarismo que compõe as casas decimais é par.")
        else:
            print("O algarismo que compõe as casas decimais é ímpar.")
        break
    except ValueError as erro:
        print(erro)
    except IndexError:
        print("\nValor inválido. Insira um número com 3 casas decimais.")
