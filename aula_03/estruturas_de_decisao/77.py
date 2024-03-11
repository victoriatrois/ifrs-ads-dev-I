# Questão 77. Faça um programa que calcula a área de determinadas figuras geométricas. O
# programa deverá apresentar um menu com as seguintes opções:
# • Quadrado (lado2)
# • Retângulo (comprimento * largura)
# • Círculo (3,14 * raio2)
# • Trapézio ((base maior + base menor) * altura/2)
# Conforme a opção, o programa deve pedir os valores necessários para realizar o cálculo.

from math import pi

from common.utils import remove_diacriticos

def exibe_menu():
    print("Menu:")
    print("Quadrado")
    print("Retângulo")
    print("Círculo")
    print("Trapézio")


def requere_valores(figura):
    match remove_diacriticos(figura).lower():
        case "quadrado":
            return float(input("Insira o valor do lado: "))
        case "retangulo":
            return float(input("Insira o valor do comprimento: ")), float(input("Insira o valor da largura: "))
        case "circulo":
            return float(input("Insira o valor do raio: "))
        case "trapezio":
            return float(input("Insira o valor da base maior: ")), float(input("Insira o valor da altura: ")), float(input("Insira o valor da base menor: "))
        case _:
            print("Opção inválida.")


def calcula_area_de_quadrado(valor_do_lado):
    area = valor_do_lado ** 2

    return area


def calcula_area_de_retangulo(altura, comprimento):
    area = altura * comprimento

    return area


def calcula_area_de_circulo(raio):
    area = pi * (raio ** 2)

    return area


def calcula_area_de_trapezio(base_maior, altura, base_menor):
    area = ((base_maior + base_menor) / 2) * altura

    return area


def calcula_area_de_figura_geometrica():
    exibe_menu()

    figura = input("Digite o nome da figura que deseja saber a área: ")

    match remove_diacriticos(figura).lower():
        case "quadrado":
            valor_do_lado = requere_valores(figura)
            area = calcula_area_de_quadrado(valor_do_lado)
        case "retangulo":
            comprimento, largura = requere_valores(figura)
            area = calcula_area_de_retangulo(comprimento, largura)
        case "circulo":
            raio = requere_valores(figura)
            area = calcula_area_de_circulo(raio)
        case "trapezio":
            base_maior, altura, base_menor = requere_valores(figura)
            area = calcula_area_de_trapezio(base_maior, altura, base_menor)
        case _:
            print("Opção inválida.")
            return

    print(f"A área do {figura} é: {area:.2f}")


calcula_area_de_figura_geometrica()
