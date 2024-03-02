# Questão 75. Faça um algoritmo que leia a quantidade de DVDs que uma locadora possui e o
# valor que ela cobra por cada aluguel, mostrando ao final as informações conforme as questões:
#   • Sabe-se que um terço dos DVDs são alugadas por mês (feito: estima_dvds_alugados_por_mes),
#     mostre o faturamento anual da locadora (feito: calcula_projecao_anual);
#   • Quando um cliente atrasa a entrega, é cobrada uma multa de 10% sobre o valor do aluguel.
#     Sabe-se que um décimo dos DVDs alugados no mês são devolvidos com atraso, calcule o
#     valor ganho com multas por mês; feito: calcula_receita_mensal_com_multas
#   • Sabe-se ainda que 2% dos DVDs acabam estragando
#     ao longo do ano, e um décimo do total (feito: calcula_perda_de_dvds_ao_ano)
#     é comprado para reposição, mostre a quantidade de DVDs que a locadora terá no final do ano
#     (feito: calcula_total_de_dvds_apos_12_meses).

def estima_dvds_alugados_por_mes(quantidade_de_dvds: int):
    quantidade_de_dvds_alugados_ao_mes: int = int(quantidade_de_dvds * 0.33)

    return quantidade_de_dvds_alugados_ao_mes


def calcula_projecao_anual(quantidade_de_dvds_alugados_ao_mes, valor_da_diaria: float):
    faturamento_anual = quantidade_de_dvds_alugados_ao_mes * valor_da_diaria * 12

    return faturamento_anual


def calcula_receita_mensal_com_multas(dvds_alugados_ao_mes: int, valor_da_diaria: float):
    receita_mensal_por_multas: float = dvds_alugados_ao_mes * 0.1 * valor_da_diaria

    return receita_mensal_por_multas


def calcula_perda_de_dvds_ao_ano(quantidade_de_dvds: int):
    perda_de_dvds_ao_ano: int = int(quantidade_de_dvds * 0.2)

    return perda_de_dvds_ao_ano


def calcula_total_de_dvds_apos_12_meses(quantidade_de_dvds: int):
    dvds_que_estragam: int = int(calcula_perda_de_dvds_ao_ano(quantidade_de_dvds))
    dvds_ao_final_de_12_meses: int = int(quantidade_de_dvds - dvds_que_estragam)

    return dvds_ao_final_de_12_meses
from common.utils import formata_moeda_br

def analisa_locadora():
    total_de_dvds_da_locadora: int = int(input("Insira a quantidade de DVDs que a locadora possui: "))
    valor_da_diaria: float = float(input("Insira a diária cobrada por DVD: "))

    estimativa_de_dvds_alugados_ao_mes = estima_dvds_alugados_por_mes(total_de_dvds_da_locadora)
    estimativa_de_dvds_alugados_ao_ano = calcula_projecao_anual(estimativa_de_dvds_alugados_ao_mes, valor_da_diaria)
    receita_mensal_com_multas = calcula_receita_mensal_com_multas(total_de_dvds_da_locadora, valor_da_diaria)
    dvds_perdidos_ano_ano = calcula_perda_de_dvds_ao_ano(total_de_dvds_da_locadora)
    total_de_dvds_da_locadora_apos_um_ano = calcula_total_de_dvds_apos_12_meses(total_de_dvds_da_locadora)

    print(f'Número de DVDs alugados ao mês: {estimativa_de_dvds_alugados_ao_mes}.')
    print(f'A projeção da receita de DVDs alugados ao ano é de R${formata_moeda_br(estimativa_de_dvds_alugados_ao_ano)}.')
    print(f'Por mês são faturados R${formata_moeda_br(receita_mensal_com_multas)} com multas.')
    print(f'Ao longo de um ano, serão danificados {dvds_perdidos_ano_ano} DVDs.')
    print(f'Portanto, a locadora terá {total_de_dvds_da_locadora_apos_um_ano} DVDs ao final de um ano.')


analisa_locadora()
