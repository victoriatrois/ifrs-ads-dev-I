from datetime import date
from aula_04.editora.livro import Livro
from aula_04.editora.pessoa import Pessoa
from aula_04.editora.autor import Autor

pessoa = Pessoa("Lucas Santos", date(1990, 1, 1))
autor = Autor("Sofia José", date(1980, 1, 1), "J.Doe")

print(pessoa)
print(autor)

livro = Livro("1234567890", "Test Book", "1234567890123", "Livro teste.", date(2022, 1, 1))

print(livro)

livro.adiciona_autor(autor)
print(livro.lista_autores())
livro.remove_autor(autor)
print(livro.lista_autores())