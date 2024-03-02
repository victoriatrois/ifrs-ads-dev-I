# Questão 64. Considerando uma eleição com 2 candidatos, elabore um algoritmo que lê o
# número total de eleitores, o número de votos do 1o candidato e o número de votos do 2o
# candidato. O algoritmo deverá apresentar o percentual de votos de cada um dos candidatos e o
# percentual de votos nulos.
from common.utils import calcula_percentual


def calcula_votos_nulos(total_de_eleitores, votos_do_primeiro_candidato, votos_do_segundo_candidato):
    votos_nulos: int = total_de_eleitores - (votos_do_primeiro_candidato + votos_do_segundo_candidato)

    return votos_nulos


def calcula_eleicoes():
    total_de_eleitores: int = int(input("Insira o total de eleitores: "))
    votos_do_primeiro_candidato: int = int(input("Insira o total de votos do primeiro candidato: "))
    votos_do_segundo_candidato: int = int(input("Insira o total de votos do segundo candidato: "))
    votos_nulos = calcula_votos_nulos(total_de_eleitores, votos_do_primeiro_candidato, votos_do_segundo_candidato)

    percentual_do_primeiro_candidato = calcula_percentual(votos_do_primeiro_candidato, total_de_eleitores)
    percentual_do_segundo_candidato = calcula_percentual(votos_do_segundo_candidato, total_de_eleitores)

    print(f'O percentual do primeiro candidato foi de {percentual_do_primeiro_candidato}%.')
    print(f'O percentual do segundo candidato foi de {percentual_do_segundo_candidato}%.')

    if votos_nulos > 0:
        percentual_de_votos_nulos = calcula_percentual(votos_nulos, total_de_eleitores)
        print(f'O percentual de votos nulos foi de {percentual_de_votos_nulos}%.')


calcula_eleicoes()