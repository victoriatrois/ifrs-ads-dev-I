# Questão 2. Faça um Programa que peça um número e então mostre a mensagem:
# “O número informado foi [número]”.
def echo():
    numero_informado: int = int(input("Informe um número: "))
    print(f'O número informado foi {numero_informado}')


echo()
