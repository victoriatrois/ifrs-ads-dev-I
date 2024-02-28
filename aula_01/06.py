# 6. Lê dois números e mostre os seguintes resultados:
# a. Dividendo;
# b. Divisor;
# c. Quociente;
# d. Resto (para calcular o resto de uma divisão, utilize o operador MOD (em C: %).

def divide():
    dividendo: float = float(input("Digite o dividendo: "))
    divisor: float = float(input("Digite o divisor: "))
    if divisor != 0:
        quociente = dividendo / divisor
        resto = dividendo % divisor
        print(f'Dividendo: {dividendo}\nDivisor: {divisor}\nQuociente: {quociente}\nResto: {resto}')
    else:
        print('NaN')


divide()
