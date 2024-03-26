from datetime import datetime


def eh_menor_de_idade(data_nascimento):
    if (datetime.today() - data_nascimento).days / 365.25 < 18:
        return True
    else:
        return False


def tem_responsavel(responsavel):
    if responsavel is not None:
        return True
    pass


class Atleta:
    """
    Classe que representa um atleta.
    """

    numero_de_responsaveis = 0
    numero_de_atletas = 0

    def __init__(self, nome, data_nascimento, esporte, responsavel=None):
        try:
            data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")\
                if isinstance(data_nascimento, str)\
                else data_nascimento

            if eh_menor_de_idade(data_nascimento) and not tem_responsavel(responsavel):
                raise ValueError("Atletas menores devem ter um responsável.")

            self.nome = nome
            self.data_nascimento = data_nascimento
            self.esporte = esporte
            self.responsavel = responsavel
            Atleta.numero_de_atletas += 1
            if tem_responsavel(self.responsavel):
                Atleta.numero_de_responsaveis += 1

        except Exception as error:
            raise error

    def __str__(self):
        """
        Retorna informações de um atleta.
        """
        to_string_atleta = f"Nome: {self.nome}\nData de nascimento: {self.data_nascimento}\nEsporte: {self.esporte}"
        if not eh_menor_de_idade(self.data_nascimento):
            return to_string_atleta + "\n"

        else:
            if eh_menor_de_idade(self.data_nascimento) and tem_responsavel(self.responsavel):
                return to_string_atleta + f"\nResponsável: {self.responsavel}\n"

    def __del__(self):
        """
        Decrementa o contador.
        """
        if self.responsavel is not None:
            Atleta.numero_de_responsaveis -= 1
        Atleta.numero_de_atletas -= 1


comissao = []

atleta1 = Atleta("Lucas Santos", "2000-01-01", "Futebol")
print(atleta1)
atleta2 = Atleta("Lucas Santos", "2010-01-01", "Futebol", "Maria")
print(atleta2)

atleta_rugby = Atleta("Ricardo", "2001-10-20", "Rugby")
print(atleta_rugby)
atleta_ping_pong = Atleta("Carlos", "2010-10-15", "Ping Pong", "Marcos")
print(atleta_ping_pong)
atleta_futebol_1 = Atleta("Kannemann", "1980-05-15", "Futebol", "Geromel")
print(atleta_futebol_1)
atleta_futebol_2 = Atleta("Geromel", "1990-03-02", "Futebol")
print(atleta_futebol_2)

comissao.append(atleta_futebol_1)
comissao.append(atleta_ping_pong)
comissao.append(atleta_rugby)
comissao.append(atleta_futebol_2)

print("------------------------------ Atletas profissionais Cadastrados ------------------------------")
for atleta in comissao:
    print(atleta)

print("------------------------------ Atletas profissionais de Futebol ------------------------------")
for atleta in comissao:
    if atleta.esporte == "Futebol":
        print(atleta)

print("------------------------------ Total de pessoas na comissão ------------------------------")
print(f"Atletas: {Atleta.numero_de_atletas}")
print(f"Responsáveis: {Atleta.numero_de_responsaveis}")
print(f"TOTAL: {Atleta.numero_de_atletas + Atleta.numero_de_responsaveis}")



