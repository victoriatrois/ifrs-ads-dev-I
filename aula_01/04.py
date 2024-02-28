# 4. Lê dois números e mostra a soma. Ante do resultado, deverá aparecer a mensagem: SOMA.
def soma():
    primeira_parcela: int = int(input("Digite a primeira parcela: "))
    segunda_parcela: int = int(input("Digite a segunda parcela: "))
    soma = primeira_parcela + segunda_parcela
    print(f'SOMA: {soma}')


soma()
