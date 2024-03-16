from carro import Carro

compacto = Carro()
compacto.marca = "Renault"
compacto.modelo = "Twingo"
compacto.ano = 2001

print(f"O carro {compacto.modelo} é da marca {compacto.marca} e foi fabricado em {compacto.ano}.")

hatch = Carro()
hatch.ano = 2022
hatch.marca = "Fiat"
hatch.modelo = "Pulse"

print(f"O carro {compacto.modelo} é da marca {compacto.marca} e foi fabricado em {compacto.ano}.")

SUV = Carro()
SUV.ano = 2024
SUV.marca = "Honda"
SUV.modelo = "HR-V"
