# Funções são implementações da própria linguagem
# que podem ser utilizadas para realizar tarefas específicas.
# Como:

# print()
# input()
# max()
# isinstance()

# A sintaxe para declarar uma função em Python é:
# def <nome_da_funcao>(<argumentos>):

# por sugestão, podemos sugerir o tipo dos argumentos:
# def <nome_da_funcao>(<argumento>: <tipo>):

# por sugestão, podemos sugerir o tipo do retorno:
# def <nome_da_funcao>(<argumento>: <tipo>) -> <tipo>:

# para definir o escopo da função, utilizamos a indentação:
# def <nome_da_funcao>(<argumento>: <tipo>) -> <tipo>:
#     <escopo_da_funcao>

# A função com um tipo de retorno, precisa da palavra reservada return:
# def <nome_da_funcao>(<argumento>: <tipo>) -> <tipo>:
#     <escopo_da_funcao>
#     return <valor>

# Três aspas duplas é comentário de documentação,
# NÃO é comentário de múltiplas linhas.
# """<documentação>"""
# A função help() exibe a documentação de uma função.

# Para funções que têm parâmetros, podemos configurar um valor padrão para eles.
# Ao fazermos isso, ele se torna um parâmetro opcional.
# def <nome_da_funcao>(<argumento>: <tipo> = <valor_padrao>) -> <tipo>:

# Parâmetros podem ser posicionais ou nomeados.
# Parâmetros posicionais são aqueles passados na ordem indicada pela declaração da função.
# Já parâmetros nomeados são aqueles passados com o nome do parâmetro.

# Ao definir um primeiro parâmetro opcional, todos os parâmetros seguintes devem ser opcionais.

# Uma função recursiva é uma função que chama a si mesma.
# É importante que a função recursiva tenha uma condição de parada.


# def gera_fibonacci(posicao: int) -> int:
#     """
#     Gera uma sequência de números de Fibonacci até uma determinada posição.
#     """
#     if posicao == 0 or posicao == 1:
#         return 1
#     else:
#         return gera_fibonacci(posicao - 1) + gera_fibonacci(posicao - 2)
#
#
# for x in range(1, 10):
#     numero_fibonacci = gera_fibonacci(x)
#     print(f"A posição {x} da sequencia de Fibonacci é {numero_fibonacci}")

# TK is a python library for GUI
# It stands for "Tool Kit"
# QT is another library for GUI
# It stands for "Quick Tool"

# SQLAlchemy is a library for database manipulation

# file = open("teste.txt", "w")  # a for append, r for read, w for write
# file.write("Hello, World!")
# file.close()


# def le_arquivo_csv():
#     arquivo = open("teste.csv", "w")
#     linhas = arquivo.readlines()
#
#     for linha in linhas:
#         dados = linha.replace("\n", "").split(";")
#         arquivo.write(";".join(dados))
#
#     arquivo.close()

# Orientação a objetos
# Learning Python
# em Python, tudo é um objeto, inclusive o próprio arquivo sendo rodado.

# Classes são como moldes para objetos.
# Class <nome_da_classe>:


class Carro:

# atributos de classe
    marca = "Fiat"


Carro.marca = ""
# atributos de instância

# método construtor
# def __init__ (): # método estático


# def __init__ (self, marcas): # método dinâmico
#     self.marcas = marcas

chevette = Carro("Chevette")