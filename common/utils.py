from unicodedata import normalize


def apara_ponto_flutuante(numero_a_aparar):
    if numero_a_aparar.is_integer():
        return int(numero_a_aparar)
    else:
        return numero_a_aparar


def calcula_percentual(parte, total):
    percentual = parte / total * 100

    return percentual


def exibe_menu(opcoes):
    print("Insira:")
    for opcao in opcoes:
        print(opcao)
    return opcoes


def formata_moeda_br(valor):
    reais, centavos = f"{valor:.2f}".split('.')

    reais = reais[::-1]
    reais = '.'.join([reais[i:i + 3] for i in range(0, len(reais), 3)])
    reais = reais[::-1]

    formatado_em_reais = f"{reais},{centavos}"

    return formatado_em_reais


def formata_numero_com_pontos(numero):
    numero_com_pontos = format(numero, ',').replace(',', '.')
    return numero_com_pontos


def inverte_numero(numero_a_inverter):
    return int(str(numero_a_inverter)[::-1])


def remove_diacriticos(palavra):
    forma_normalizada = normalize('NFKD', palavra)
    palavra_em_ascii = forma_normalizada.encode('ASCII', 'ignore')
    return palavra_em_ascii.decode()