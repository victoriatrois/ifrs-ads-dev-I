# Questão 10. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A
# função deve retornar um valor booleano.

def exibe_classificacao(valor):
    if valor % 2 == 0:
        return True
    else:
        return False


exibe_classificacao(1)
exibe_classificacao(2)
exibe_classificacao(3)
exibe_classificacao(4)
exibe_classificacao(6)
exibe_classificacao(8)
exibe_classificacao(12)