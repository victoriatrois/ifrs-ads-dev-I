# Questão 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcula_area_quadrado():
    lado: float = float(input("Insira o lado do quadrado: "))
    print(f" A área de um quadrado de lado {lado ** 2}")


calcula_area_quadrado()

