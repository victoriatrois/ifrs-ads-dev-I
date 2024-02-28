# Questão 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi


# 10. Lê o raio de um círculo e mostre como saída o perímetro (2*π*Raio) e a área (π*Raio2).
def calcula_area():
    raio: float = float(input("Insira o raio do círculo que deseja analizar: "))
    area: float = pi * (raio ** 2)
    print(f'Um círculo com raio {format(raio, ".2f")} tem uma área de {format(area, ".2f")}')


calcula_area()
