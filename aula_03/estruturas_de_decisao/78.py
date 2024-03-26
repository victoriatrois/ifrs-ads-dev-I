# Questão 78. Faca um algoritmo que possa converter determinada quantia de dinheiro em reais
# para uma das seguintes moedas:
# • e – euro
# • l - libra esterlina
# • d - dólar ($)

from common.utils import exibe_menu
from forex_python.converter import CurrencyRates


def converte_moeda(valor_em_reais: float):
    cr = CurrencyRates()
    exibe_menu(["e - euro", "l - libra esterlina", "d - dólar ($)"])
    moeda = input("Insira a moeda desejada: ")
    valor_convertido = 0

    if moeda not in ["e", "l", "d"]:
        print("Moeda inválida.")
        return

    match moeda:
        case "e":
            valor_convertido = valor_em_reais / cr.get_rate('BRL', 'EUR')
            print(f"R$ {valor_em_reais} convertido para euros é € ", end="")

        case "l":
            valor_convertido = valor_em_reais / cr.get_rate('BRL', 'GBP')
            print(f"R$ {valor_em_reais} convertido para libras é £ ", end="")

        case "d":
            valor_convertido = valor_em_reais / cr.get_rate('BRL', 'USD')
            print(f"R$ {valor_em_reais} convertido para dólares é $ ", end="")

        case _:
            print("Moeda inválida.")

    print(f"{valor_convertido:.2f}")


converte_moeda(1.00)
