from datetime import date
from aula_05.editora_v2.pessoa import Pessoa


class Autor(Pessoa):
    """
        Classe que representa um autor.
    """

    __slots__ = ["__pseudonimo", "__trabalhos"]

    def __init__(self, nome: str, data_nascimento: date, pseudonimo: str):
        super().__init__(nome, data_nascimento)
        self.__pseudonimo = pseudonimo
        self.__trabalhos = []

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudonimo):
        self.__pseudonimo = pseudonimo

    @property
    def trabalhos(self):
        return self.__trabalhos

    @trabalhos.setter
    def trabalhos(self, trabalhos):
        self.__trabalhos = trabalhos

    def