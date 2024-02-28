# 3. Lê um número e mostra seu sucessor e seu antecessor na tela.
def exibe_vizinhos():
    numero_informado: int = int(input("Informe o número desejado: "))
    antecessor = numero_informado - 1
    sucessor = numero_informado + 1
    print(f'Número informado: {numero_informado}\nAntecessor: {antecessor}\nSucessor: {sucessor}')


exibe_vizinhos()
