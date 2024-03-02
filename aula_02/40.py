# Questão 40. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar
# todos os cavalos comprados para um haras.

def determina_ferraduras():
    numero_de_cavalos: int = int(input("Insira o número total de cavalos que o haras possui: "))
    total_de_ferraduras: int = numero_de_cavalos * 4

    print(f'O total de ferraduras necessárias é de {total_de_ferraduras}.')


determina_ferraduras()