# Questão 66. O coração humano bate em média uma vez por segundo. Desenvolva um algoritmo
# para calcular e mostrar quantas vezes o coração de uma pessoa baterá se viver X anos.
# Considere como dado de entrada a idade da pessoa.
#   Considerações:
#       1 ano = 365,25 dias,
#       1 dia = 24 horas,
#       1 hora = 60 minutos e
#       1 minuto = 60 segundos

from common.utils import formata_numero_com_pontos


def converte_anos_em_segundos(ano: int):
    segundos_em_um_ano: int = 365.25 * 24 * (60 ** 2)
    ano_em_segundos = ano * segundos_em_um_ano

    return ano_em_segundos


def calcula_batidas_de_coracao_numa_vida():
    idade: int = int(input("Digite uma idade: "))

    batidas_em_uma_vida = formata_numero_com_pontos(int(converte_anos_em_segundos(idade)))

    print(f'Ao longo de {idade} anos, um coração bate aproximadamente {batidas_em_uma_vida} vezes.')


calcula_batidas_de_coracao_numa_vida()
