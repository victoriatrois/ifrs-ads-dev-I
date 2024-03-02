# Questão 13. João Papo-de-Pescador, homem de bem, comprou um microcomputador para
# controlar o rendimento diário de seu trabalho.
#
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso.
# Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar.
# Caso contrário, mostrar tais variáveis com o conteúdo ZERO.

def excede_peso(peso: float):
    return peso > 50


def calcula_multa(peso_pescado: float):
    return (peso_pescado - 50) * 4


def verifica_irregularidade():
    peso_pescado: float = float(input("Insira quantos quilos o Sr. pescou hoje, Seu João: "))

    if excede_peso(peso_pescado):
        print(f'MULTA: {calcula_multa(peso_pescado)}.')
    else:
        print("Sem multa hoje, Seu João.")


verifica_irregularidade()
