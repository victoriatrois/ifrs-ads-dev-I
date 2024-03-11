# Questão 15. Faça um algoritmo que leia um número e mostre se ele é divisível por 5 OU por 9.


def eh_divisivel(dividendo: int, divisor: int):
    if dividendo % divisor == 0:
        return True


def analiza_divisibilidade():
    try:
        numero_a_conferir = int(input("Insira um número: "))

        if eh_divisivel(numero_a_conferir, 5):
            print(f"{numero_a_conferir} é divisível por 5")
        elif eh_divisivel(numero_a_conferir, 9):
            print(f"{numero_a_conferir} é divisível por 9")
        else:
            print("O número inserido não é divisível por 5 nem por 9.")

    except ValueError:
        print("Não compatível com números decimais.\nDivisibilidade é uma propriedade do conjunto dos números inteiros.")


analiza_divisibilidade()
