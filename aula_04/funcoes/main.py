from aula_05.editora_v2.pessoa import Pessoa
from datetime import date


carlo = Pessoa("Carlos Maia", date(1990, 10, 15))
print(carlo)
print(carlo.__repr__())
