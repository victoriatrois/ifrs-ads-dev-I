# algoritmo 01

from common.utils import formata_moeda_br

# GASOLINA = 4.97
# ALCOOL = 5.78
# valor = 0
#
# nome: str = input("Digite seu nome: ")
#
# print(f'Olá {nome}')
#
# combustivel = input("Digite G - gasolina ou A - Álcool: ")
# quantidade = float(input("Digite a quantidade de litros: "))
#
# if combustivel == "G":
#     valor = quantidade * GASOLINA
# else:
#     valor = quantidade * ALCOOL
#
# print(f'Valor total RS {formata_moeda_br(valor)}')

# algoritmo 02
# nome = input("Digite o seu nome: ")
# print(f'Olá {nome}')
# 
# nr1 = input(f'Digite o primeiro número: ')
# nr2 = input(f'Digite o primeiro número: ')
# 
# inr1 = int(nr1)
# inr2 = int(nr2)
# 
# soma = inr1 + inr2
# 
# print(f'O resultado é {soma}')
# 
# if inr1 == inr2:
#     print('Os números são iguais.')
# elif inr1 > inr2:
#     print('O primeiro número é maior')
# else:
#     print('O segundo número é maior')

# algoritmo 03
# nome = input("Digite o seu nome: ")
#
# print(f'Olá {nome}')
#
# minimo = int(input("Digite quantos minutos foram falados no mês: "))
#
# if minimo > 200:
#     conta = minimo * 0.2
# elif minimo <= 400:
#     conta = minimo * 0.4
# else:
#     conta = minimo * 0.15
#
# print(f'O total da conta é RS {formata_moeda_br(conta)}.')

# excessões
# numero = ""
# try:
#     numero = input("Insira um número: ")
#     int(numero)
#     print(f'{numero}')
#
# except:
#     print(f'{numero} não pode ser convertido no tipo inteiro. Insira um valor que contenha algarismos de 0 a 9.')

# flag = True
#
# while flag:
#     try:
#         x = 0
#         fim = int(input("Digite até que número você gostaria de contar (digite números negativos para sair: "))
#
#         while x <= fim:
#             print(x)
#             x = x + 1
#
#         if fim < 0:
#             flag = False
#
#     except:
#         print("Você deve digitar um número inteiro!")

flag = True

while flag:
    try:
        a = int(input())

        if a == 100:
            raise TypeError("Customizado")
        elif a == 200:
            raise NameError("Customizado 2")
        else:
            b = a * 2
            print(f"O dobro de {a} é {b}.")

    except ValueError:
        flag: False
        print("Você não deve digitar letras!")

    except TypeError:
        print("Erro 100: Não sei fazer esse cálculo para 100.")

    except:
        print("Erro!")

else:
    print("Finalizando...")
