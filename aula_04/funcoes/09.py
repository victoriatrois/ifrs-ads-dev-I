# Questão 9. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou
# negativo. A função deve retornar um valor booleano.


def verifica_sinal(numero):
    try:
        if numero < 0:
            return False
        elif numero > 0:
            return True
        else:
            raise ValueError("Zero não nem positivo nem negativo.")
    except ValueError as erro:
        print(erro)
        return None


verifica_sinal(-1)
verifica_sinal(0)
verifica_sinal(1)
