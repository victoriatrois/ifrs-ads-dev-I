from typing import List, Optional
from datetime import date

from aula_04.editora.autor import Autor


class Livro:
    """
    Classe que representa um livro.
    """

    codigo = ''
    titulo = ''
    isbn = ''
    resumo = ''
    publicacao = 0
    _autores = []

    def __init__(self, codigo: str, titulo: str, isbn: str, resumo: Optional[str] = '', publicacao: Optional[date] = None):
        if not (len(codigo) == 10):
            raise ValueError("O campo 'código' deve ter exatamente 10 caracteres.")
        if not (1 <= len(titulo) <= 100):
            raise ValueError("O campo 'título' deve ter entre 1 e 100 caracteres.")
        if not (10 <= len(resumo) <= 500):
            raise ValueError("O campo 'resumo' deve ter entre 10 e 500 caracteres.")
        if not (len(isbn) == 13):
            raise ValueError("O campo 'ISBN' deve ter exatamente 13 caracteres.")

        self.codigo = codigo
        self.titulo = titulo
        self.isbn = isbn
        self.resumo = resumo
        self.publicacao = publicacao if publicacao else date.today()
        self._autores = []

    def __str__(self):
        return (f"Código: {self.codigo}\n"
                f"Título: {self.titulo}\n"
                f"ISBN: {self.isbn}\n"
                f"Resumo: {self.resumo}\n"
                f"Data de publicação: {self.publicacao}")

    def lista_autores(self) -> List['Autor']:
        return self._autores

    def adiciona_autor(self, autor: 'Autor') -> bool:
        if autor not in self._autores:
            self._autores.append(autor)
            return True
        return False

    def remove_autor(self, autor: 'Autor') -> bool:
        if autor in self._autores:
            self._autores.remove(autor)
            return True
        return False
