# 13. Leia o numerador e o denominador de uma fração e transforme-o em um número decimal.
def transforma_em_decimal():
    numerador: float = float(input("Digite o dividendo: "))
    denominador: float = float(input("Digite o divisor: "))
    if denominador != 0:
        decimal = numerador / denominador
        print(f'A fração:\t{numerador} = {decimal}\n\t\t\t————\n\t\t\t{denominador}')
    else:
        print('NaN')


transforma_em_decimal()
