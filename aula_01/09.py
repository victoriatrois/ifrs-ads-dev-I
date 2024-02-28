# 9. Entre com a base e a altura de um retângulo e mostre os resultados:
# a. Perímetro (Perímetro é igual à soma dos 4 lados).
# b. Área (Área é igual à base vezes altura).
def calcula_perimetro_de_retangulo(base: float, altura: float):
    perimetro: float = (base * 2) + (altura * 2)
    return perimetro


def calcula_area_de_retangulo(base: float, altura: float):
    area: float = base * altura
    return area


def analisa_retangulo():
    base: float = float(input("Insira a base do retângulo: "))
    altura: float = float(input("Insira a altura do retângulo: "))

    print(f'Perímetro: {calcula_perimetro_de_retangulo(base, altura)}')
    print(f'Área: {calcula_area_de_retangulo(base, altura)}')


analisa_retangulo()
