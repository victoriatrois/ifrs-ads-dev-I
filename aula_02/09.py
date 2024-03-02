# Questão 9. Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

def converte_em_graus_celsius():
    temperatura_em_fahrenheit: float = float(input("Insira a temperatura em ºF: "))
    temperatura_em_celsius = 5 * (temperatura_em_fahrenheit - 32) / 9
    print(f'{temperatura_em_fahrenheit}ºF são {temperatura_em_celsius}ºC.')


converte_em_graus_celsius()