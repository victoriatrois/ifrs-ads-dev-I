# 5. Lê um número e mostra a terça parte deste número.
def informa_um_terco():
    numero_a_dividir: float = float(input("Digite o número que deseja dividir por 3: "))
    terca_parte = numero_a_dividir / 3
    print(f'Um terço de {numero_a_dividir} é {terca_parte}')


informa_um_terco()