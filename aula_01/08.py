# 8. Lê o saldo de uma aplicação e imprima o novo saldo, considerado o reajuste de 1%.
def reajusta_aplicacao():
    saldo_atual: float = float(input("Digite o saldo da sua aplicação: "))
    reajuste: float = saldo_atual * 0.1
    saldo_reajustado: float = saldo_atual + reajuste
    print(f'Seu saldo reajustado é {saldo_reajustado}')


reajusta_aplicacao()
