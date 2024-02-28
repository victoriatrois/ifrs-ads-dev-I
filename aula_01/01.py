# 1. Mostrar na tela o produto entre dois números fornecidos pelo usuário.
def multiplica():
    primeiro_fator: int = int(input("Digite o primeiro fator: "))
    segundo_fator: int = int(input("Digite o segundo fator: "))
    produto = primeiro_fator * segundo_fator
    print(f'O produto de {primeiro_fator} e {segundo_fator} é {produto}.')


multiplica()
