# Questão 61. Faça um programa que passa temperatura em celsius e mostra em fahrenheit.

def converte_em_graus_fahrenheit():
    temperatura_em_celsius: float = float(input("Insira a temperatura em ºC: "))
    temperatura_em_fahrenheit = (temperatura_em_celsius * 9 / 5) + 32
    print(f'{temperatura_em_celsius}ºC são {temperatura_em_fahrenheit}ºF.')


converte_em_graus_fahrenheit()