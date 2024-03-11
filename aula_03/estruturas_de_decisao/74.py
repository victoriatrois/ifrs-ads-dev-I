# Questão 74. Faça um algoritmo que leia um número e informe se ele é divisível por 3
# OU divisível por 7.

def eh_divisivel(dividendo: int, divisor: int):
    if dividendo % divisor == 0:
        return True


def analiza_divisibilidade():
    try:
        numero_a_conferir = int(input("Insira um número: "))

        if eh_divisivel(numero_a_conferir, 3):
            print(f"{numero_a_conferir} é divisível por 3")
        elif eh_divisivel(numero_a_conferir, 7):
            print(f"{numero_a_conferir} é divisível por 7")
        else:
            print("O número inserido não é divisível por 3 nem por 7.")

    except ValueError:
        print("Não compatível com números decimais.\nDivisibilidade é uma propriedade do conjunto dos números inteiros.")


analiza_divisibilidade()