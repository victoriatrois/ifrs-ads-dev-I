from typing import List
from datetime import date

from aula_04.editora.pessoa import Pessoa


class Autor(Pessoa):
    """
    Classe que representa um autor.
    """
    def __init__(self, nome: str, data_nascimento: date, pseudonimo: str):
        super().__init__(nome, data_nascimento)
        self._pseudonimo = pseudonimo
        self._trabalhos = []

