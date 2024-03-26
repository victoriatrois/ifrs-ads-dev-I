import locale
from datetime import date, datetime


class Pessoa:
    """
    Classe que representa uma pessoa.
    """

    __slots__ = ["__nome", "__data_nascimento"]

    def __init__(self, nome: str, data_nascimento: date):
        try:
            data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date() \
                if isinstance(data_nascimento, str) \
                else data_nascimento
            if not isinstance(data_nascimento, date) and not isinstance(data_nascimento, str):
                raise ValueError("A data de nascimento deve ser do tipo date ou str.")

            self.nome = nome
            self.data_nascimento = data_nascimento

        except Exception as erro:
            raise erro

    def __str__(self):
        locale.setlocale(locale.LC_ALL, '')

        if isinstance(self.data_nascimento, date):
            data_nascimento_str = self.data_nascimento.strftime('%x')
        else:
            data_nascimento_str = self.data_nascimento

        return (f'Nome: {self.nome}\n'
                f'Data de nascimento: {data_nascimento_str}')

    def __repr__(self):
        return f'Pessoa({self.nome}, {self.data_nascimento})'

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        try:
            if not isinstance(nome, str):
                raise ValueError("O nome deve ser uma string.")

            if len(nome) < 10 or len(nome) > 100:
                raise ValueError("O nome deve ter entre 10 e 100 caracteres.")

            self.__nome = nome
        except Exception as erro:

            raise erro

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

