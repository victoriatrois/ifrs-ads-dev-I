from datetime import date


class Pessoa:
    def __init__(self, nome: str, data_nascimento: date):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def __str__(self):
        return (f'Nome: {self.nome}\n'
                f'Data de nascimento: {self.data_nascimento}')

    def __repr__(self):
        return f'Pessoa({self.nome}, {self.data_nascimento})'

