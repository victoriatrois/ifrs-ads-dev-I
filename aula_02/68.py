# Questão 68. Antes de o racionamento de energia ser decretado, quase ninguém falava em
# quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sabe-se que
# 100 quilowatts de energia custa um sétimo do salário mínimo, fazer um algoritmo que receba o
# valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e imprima:
#   • o valor em reais de cada quilowatts
#   • o valor em reais a ser pago
#   • o novo valor a ser pago por essa residência com um desconto de 10%

from common.utils import formata_moeda_br


def analisa_gasto_mensal_de_energia():
    salario_minimo = float(input("Digite o salário mínimo do país onde mora: "))
    gasto_mensal_em_quilowatts = float(input("Digite seu gasto mensal em quilowatts: "))
    valor_de_100_quilowatts = salario_minimo / 7
    valor_unitario_do_quilowatt = valor_de_100_quilowatts / 100
    gasto_mensal_em_reais = gasto_mensal_em_quilowatts * valor_unitario_do_quilowatt
    gasto_mensal_com_desconto = gasto_mensal_em_reais - (gasto_mensal_em_reais * 0.1)

    print(f'Seu gasto mensal por quilowatt é de R${formata_moeda_br(valor_unitario_do_quilowatt)}.')
    print(f'O valor total da sua conta de energia ficou em R${formata_moeda_br(gasto_mensal_em_reais)}.')
    print(f'O valor total da sua conta de energia com 10% de desconto fica em R${formata_moeda_br(gasto_mensal_com_desconto)}.')


analisa_gasto_mensal_de_energia()
