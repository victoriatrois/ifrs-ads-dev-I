class Carro:
    """
    Implementa um carro com marca e modelo.
    """

    marca = ''
    modelo = ''
    ano = 0
    placa = ''
    chassi = ''
    cor = ''
    cor_lateral = ''
    velocidade = 0
    consumo = 0
    tipo_de_combustivel = ''

    def __init__(self):
        pass

    def movimenta():
        """
        Movimenta o carro.
        """
        print("Comecei a me movimentar.")
        pass

    def freia():
        """
        Freia o carro.
        """
        print("Estou freando.")
        pass

    def acelera():
        """
        Acelera o carro.
        """
        print("Estou acelerando.")
        pass


    def estaciona():
        """
        Estaciona o carro.
        """
        print("Estou estacionando.")
        pass

    def get_velocidade(self):
        """
        Retorna a velocidade do carro.
        """
        return self.velocidade