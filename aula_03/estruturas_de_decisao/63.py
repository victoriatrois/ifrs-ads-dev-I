# Questão 63. Faça um programa que faça 5 perguntas para um usuário sobre um crime. As
# perguntas são:
# • "Telefonou para a vítima?"
# • "Esteve no local do crime?"
# • "Mora perto da vítima?"
# • "Devia para a vítima?"
# • "Já trabalhou com a vítima?"

# Questão 64. O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder "SIM"a 2 questões ela deve ser classificada como "Suspeita", entre 3
# e 4 ("SIM") como "Cúmplice"e se responder "SIM"para as 5 perguntas, então mostrar mensagem
# "Assassino". Caso contrário, ele será classificado como "Inocente".

from unicodedata import normalize

perguntas = [
    "Você telefonou para a vítima?",
    "Você esteve no local do crime?",
    "Você mora perto da vítima?",
    "Você devia para a vítima?",
    "Você já trabalhou com a vítima?"
]

respostas = []

print("Digite SIM ou NÃO:\n")
for pergunta in perguntas:
    print(pergunta)

    resposta = normalize('NFKD', input("_")).encode('ASCII', 'ignore').decode().upper()
    respostas.append(resposta)

numero_de_sins = respostas.count("SIM")

if numero_de_sins == 2:
    classificacao = "Suspeito"
elif 3 <= numero_de_sins <= 4:
    classificacao = "Cúmplice"
elif numero_de_sins == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"O respondente é classificado como {classificacao}.")

