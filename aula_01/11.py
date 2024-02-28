# 11. Calcule e mostre a área de um triângulo (área é igual a (base x altura) dividido por 2).
def calcula_area_de_triangulo():
    base: float = float(input("Insira a base do triângulo: "))
    altura: float = float(input("Insira a altura do triângulo: "))
    area: float = (base * altura) / 2
    print(f'A área de um triângulo com base {base} e altura {altura} é de: {area}')


calcula_area_de_triangulo()
