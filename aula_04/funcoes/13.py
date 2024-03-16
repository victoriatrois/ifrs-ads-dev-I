# Questão 13. Faça uma função que recebe 3 valores inteiros por parâmetro e retorna-os ordenados
# em ordem crescente.

def ordena_numeros(valor_1, valor_2, valor_3, crescente=True):
    valores_ordenados = sorted([valor_1, valor_2, valor_3])
    if not crescente:
        valores_ordenados.reverse()
    return valores_ordenados


print(ordena_numeros(3, 2, 1, True))
print(ordena_numeros(3, 2, 1, False))
