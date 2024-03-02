# Questão 71. Crie um algoritmo que leia uma hora do dia e informe quantos minutos se passaram
# desde o início do dia.

def hora_eh_valida(hora:int) -> bool:
    if hora < 0 or hora > 24:
        return False
    else:
        return True


def minuto_eh_valido(minutos:int) -> bool:
    if minutos < 0 or minutos > 60:
        return False
    else:
        return True


def informa_minutos():
    hora_atual: int = int(input("Digite a hora atual (formato 24-horas): "))
    minuto_atual: int = int(input("Digite os minutos: "))
    minutos_passados: int

    if not hora_eh_valida(hora_atual) and not minuto_eh_valido(minuto_atual):
        print("Valores para hora E minutos inválidos")
    elif not hora_eh_valida(hora_atual):
        print("Valor de hora inválido.")
    elif not minuto_eh_valido(minuto_atual):
        print("Valor de minutos inválido.")
    else:
        hora_atual *= 60
        minutos_passados = hora_atual + minuto_atual
        print(f'Até então, no dia de hoje, se passaram {minutos_passados} minutos.')


informa_minutos()