# Questão 10. Faça um Programa que peça 2 números inteiros e um número real.
# mostre: o produto do dobro do primeiro com metade do segundo. A soma do triplo do primeiro
# com o terceiro. O terceiro elevado ao cubo.

primeiro_valor: int = int(input("Insira um número inteiro: "))
segundo_valor: int = int(input("Insira um segundo número inteiro: "))
terceiro_valor: float = float(input("Insira um segundo número inteiro: "))

dobro_do_primeiro_valor = primeiro_valor * 2
metade_do_segundo_valor = segundo_valor / 2
triplo_do_primeiro_valor = primeiro_valor * 3

produto_do_dobro_do_primeiro_com_metade_do_segundo = dobro_do_primeiro_valor * metade_do_segundo_valor
soma_do_triplo_do_primeiro_com_o_terceiro = triplo_do_primeiro_valor + terceiro_valor
terceiro_valor_elevado_ao_cubo = terceiro_valor ** 3

print(f'O dobro do primeiro número vezes a metade do segundo é: {produto_do_dobro_do_primeiro_com_metade_do_segundo}.')
print(f'A soma do triplo do primeiro número com o terceiro é: {soma_do_triplo_do_primeiro_com_o_terceiro}.')
print(f'O terceiro número elevado ao cubo é: {terceiro_valor_elevado_ao_cubo}.')
