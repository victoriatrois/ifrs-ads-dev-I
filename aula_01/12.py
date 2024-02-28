# 12. Calcule o valor de uma prestação em atraso, utilizando a fórmula:
# PRESTAÇÃO = VALOR + (VALOR * (TAXA/100) * TEMPO).
def calcula_atraso_de_prestacao():
    valor_devido: float = float(input("Insira o valor devido: "))
    taxa: float = float(input("Insira o percentual da taxa de juros: "))
    tempo: float = float(input("Insira o tempo total de empréstimo: "))
    prestacao = valor_devido + (valor_devido * (taxa / 100) * tempo)
    print(f'A prestação deste mês está em: {prestacao}')


calcula_atraso_de_prestacao()
