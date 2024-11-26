'''Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.'''

from concessionaria import Concessionaria
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def main():
    # Criar uma concessionária
    concessionaria = Concessionaria("Auto Center")

    # Criar veículos
    carro = Car("Toyota", "Corolla", 2021, 4)
    moto = Motorcycle("Honda", "CB500", 2020, 500)
    caminhão = Truck("Volvo", "FH", 2019, 18000)

    # Adicionar veículos à concessionária
    concessionaria.adicionar_veiculo(carro)
    concessionaria.adicionar_veiculo(moto)
    concessionaria.adicionar_veiculo(caminhão)

    # Exibir veículos na concessionária
    concessionaria.exibir_veiculos()

if __name__ == "__main__":
    main()


# onde a classe Concessionaria contém uma lista de instâncias das classes Car, Motorcycle, e Truck.