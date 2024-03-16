# Questão 6. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna
# essa idade expressa em dias.

def calcula_idade_em_dias(idade_em_anos):
    idade_em_dias = idade_em_anos * 365

    return idade_em_dias


print(calcula_idade_em_dias(1))
print(calcula_idade_em_dias(32))
