# Questão 40. Faça um programa para jogar Pedra, papel e tesoura. Para jogar, o usuário deverá
# indicar seu nome e o símbolo. Considere para os símbolos: 1 - pedra, 2 - tesoura e 3 - papel. Para
# saber mais sobre o jogo, verifique em (https://pt.wikipedia.org/wiki/Pedra,_papel_e_tesoura)

def exibe_titulo():
    print("\t\t---------------")
    print("\t\t| Janken pon! |")
    print("\t\t---------------")


def escolhe_modo_de_jogo():
    while True:
        try:
            modo_de_jogo = int(input(
                "\nInsira:\n\t\t"
                "1 - para jogar com a máquina\n\t\t"
                "2 - para jogar com outra pessoa\n\t\t_"
            ))

            if modo_de_jogo not in [1, 2]:
                raise ValueError("\nValor inválido")
            return modo_de_jogo

        except ValueError as erro:
            print(erro)


def registra_jogada():
    while True:
        try:
            jogada_do_jogador = int(input(
                "\nInsira:\n\t\t"
                "1 - pedra\n\t\t"
                "2 - papel\n\t\t"
                "3 - tesoura\n\t\t_"
            ))
            print("\n" * 100)

            if jogada_do_jogador not in [1, 2, 3]:
                raise ValueError("\nValor inválido.")

            return jogada_do_jogador
        except ValueError as erro:
            print(erro)


def gera_jogada_do_oponente():
    from random import choice

    pedra_papel_tesoura = ['pedra', 'papel', 'tesoura']

    jogada_do_oponente = choice(pedra_papel_tesoura)

    return jogada_do_oponente


def analisa_rodada(modo_de_jogo, jogada_do_jogador_1, jogada_do_jogador_2):
    match jogada_do_jogador_1:
        case 'pedra':
            if jogada_do_jogador_1 == jogada_do_jogador_2:
                print(f"!!! {'EMPATE' if modo_de_jogo == 2 else 'EMPATE'} !!!")
            elif jogada_do_jogador_2 == "papel":
                print(f"!!! {'VITÓRIA do JOGADOR 2' if modo_de_jogo == 2 else 'DERROTA'} !!!")
            else:
                print(f"!!! {'VITÓRIA do JOGADOR 1' if modo_de_jogo == 2 else 'VITÓRIA'} !!!")

        case 'papel':
            if jogada_do_jogador_1 == jogada_do_jogador_2:
                print(f"!!! {'EMPATE' if modo_de_jogo == 2 else 'EMPATE'} !!!")
            elif jogada_do_jogador_2 == "tesoura":
                print(f"!!! {'VITÓRIA do JOGADOR 2' if modo_de_jogo == 2 else 'DERROTA'} !!!")
            else:
                print(f"!!! {'VITÓRIA do JOGADOR 1' if modo_de_jogo == 2 else 'VITÓRIA'} !!!")

        case 'tesoura':
            if jogada_do_jogador_1 == jogada_do_jogador_2:
                print(f"!!! {'EMPATE' if modo_de_jogo == 2 else 'EMPATE'} !!!")
            elif jogada_do_jogador_2 == "tesoura":
                print(f"!!! {'VITÓRIA do JOGADOR 2' if modo_de_jogo == 2 else 'DERROTA'} !!!")
            else:
                print(f"!!! {'VITÓRIA do JOGADOR 1' if modo_de_jogo == 2 else 'VITÓRIA'} !!!")


def exibe_resultado(modo_de_jogo, jogada_do_jogador_1, jogada_do_jogador_2):
    titulo_single_player = "\nSua jogada:\t\tvs.\t\tJogada do bot:"
    titulo_dual_player = "\nJogada do Jogador 1:\t\tvs.\t\tJogada do Jogador 2:"

    jogadas_single_player = f"{jogada_do_jogador_1}\t\t\t\t\t{jogada_do_jogador_2}"
    jogadas_dual_player = f"{jogada_do_jogador_1}\t\t\t\t\t\t\t\t{jogada_do_jogador_2}"

    titulo = f"{titulo_dual_player if modo_de_jogo == 2 else titulo_single_player}"
    jogadas = f"{jogadas_dual_player if modo_de_jogo == 2 else jogadas_single_player}"

    print(f"\n{titulo}")
    print(f"{jogadas}\n")


def executa_rodada(modo_de_jogo, jogadas_possiveis):
    if modo_de_jogo == 2:
        print("\n===> Jogador 1 <===")
    jogada_do_jogador_1 = jogadas_possiveis[int(registra_jogada())]
    if modo_de_jogo == 2:
        print("\n===> Jogador 2 <===")
    jogada_do_jogador_2 = gera_jogada_do_oponente() if modo_de_jogo == 1 else jogadas_possiveis[int(registra_jogada())]

    exibe_resultado(modo_de_jogo, jogada_do_jogador_1, jogada_do_jogador_2)

    return jogada_do_jogador_1, jogada_do_jogador_2


def executa_jogo():
    exibe_titulo()
    mapeamento_de_jogadas = {1: 'pedra', 2: 'papel', 3: 'tesoura'}

    modo_de_jogo = escolhe_modo_de_jogo()

    jogada_do_jogador_1, jogada_do_jogador_2 = executa_rodada(modo_de_jogo, mapeamento_de_jogadas)
    analisa_rodada(modo_de_jogo, jogada_do_jogador_1, jogada_do_jogador_2)


executa_jogo()
