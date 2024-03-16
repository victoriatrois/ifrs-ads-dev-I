from typing import List, Optional

from aula_04.editora.livro import Livro


class Editora:
    """
    Classe que representa uma editora.
    """

    _codigo = ''
    _razao_social = ''
    _nome_fantasia = ''
    _email = ''
    _livros = []
    def __init__(self, codigo: str, razao_social: str, nome_fantasia: Optional[str] = '', email: Optional[str] = ''):
        self._codigo = codigo
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._email = email
        self._livros = []

    def __str__(self):
        return f"Editora(cod={self._codigo}, razao_social={self._razao_social}, nome_fantasia={self._nome_fantasia}, email={self._email})"

    def listar_livros(self) -> List['Livro']:
        return self._livros

    def publicar(self, livro: 'Livro') -> None:
        if livro not in self._livros:
            self._livros.append(livro)