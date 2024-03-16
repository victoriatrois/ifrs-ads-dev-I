# Questão 1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu
# volume (v = (4 * Pi * R3) / 3).

from math import pi


def calcula_volume(raio):
    volume = (4 * pi * raio ** 3) / 3

    return volume


print(f"O volume da esfera é: {calcula_volume(3):.2f} m³")
