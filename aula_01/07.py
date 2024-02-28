# 7. Leia 4 números inteiros e mostre a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4.
def calcula_media_ponderada():
    primeiro_numero: int = int(input("Digite o primeiro número: "))
    segundo_numero: int = int(input("Digite o segundo número: "))
    terceiro_numero: int = int(input("Digite o terceiro número: "))
    quarto_numero: int = int(input("Digite o quarto número: "))
    media_ponderada: float = float(primeiro_numero +
                                   (segundo_numero * 2) +
                                   (terceiro_numero * 3) +
                                   (quarto_numero * 4)) / 10
    print(f'A média ponderada de {primeiro_numero}, {segundo_numero}, {terceiro_numero} e {quarto_numero}é {media_ponderada}')


calcula_media_ponderada()
