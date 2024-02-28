# Questão 3. Faça um Programa que peça dois números e imprima a soma.
def soma_v2():
    primeira_parcela: int = int(input("Digite a primeira parcela: "))
    segunda_parcela: int = int(input("Digite a segunda parcela: "))
    soma = primeira_parcela + segunda_parcela
    print(f'{primeira_parcela} + {segunda_parcela} = {soma}.')


soma_v2()
