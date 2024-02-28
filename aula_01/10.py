from math import pi


# 10. Lê o raio de um círculo e mostre como saída o perímetro (2*π*Raio) e a área (π*Raio2).
def calcula_perimetro_de_circulo(pi: float, raio: float):
    perimetro: float = 2 * pi * raio
    return perimetro


def calcula_area_de_circulo(pi: float, raio: float):
    area: float = pi * (raio ** 2)
    return area


# TODO: formatar casas decimais
def analisa_circulo():
    raio: float = float(input("Insira o raio do círculo que deseja analizar: "))
    perimetro: float = calcula_perimetro_de_circulo(pi, raio)
    area: float = calcula_area_de_circulo(pi, raio)
    print(f'Um círculo com raio {raio} tem um perímetro de {perimetro} e uma área de {area}')


analisa_circulo()
