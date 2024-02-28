# 2. Mostrar a média aritmética entre 3 números fornecidos pelo usuário.
def calcula_media():
    primeira_nota: float = float(input("Digite a primeira nota: "))
    segunda_nota: float = float(input("Digite a segunda nota: "))
    terceira_nota: float = float(input("Digite a terceira nota: "))
    media = (primeira_nota + segunda_nota + terceira_nota) / 3
    print(f'A média das notas {primeira_nota}, {segunda_nota} e {terceira_nota} é {media}.')


calcula_media()
