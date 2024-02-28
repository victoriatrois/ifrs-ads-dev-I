# Questão 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def calcula_media_de_4():
    primeira_nota: float = float(input("Digite a primeira nota: "))
    segunda_nota: float = float(input("Digite a segunda nota: "))
    terceira_nota: float = float(input("Digite a terceira nota: "))
    quarta_nota: float = float(input("Digite a quarta nota: "))
    media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
    print(f'A média das notas {primeira_nota}, {segunda_nota}, {terceira_nota} e {quarta_nota} é {format(media, ".2f")}.')


calcula_media_de_4()
