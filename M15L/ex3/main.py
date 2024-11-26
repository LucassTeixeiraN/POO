'''Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.'''

from automovel import Automovel
from moto import Moto
from caminhao import Caminhao

def main():
    veiculos = [
        Automovel("Tesla", "Model 3", 2021, 75),
        Moto("Kawasaki", "Ninja 400", 2020, 399),
        Caminhao("Mercedes", "Actros", 2019, 20000)
    ]

    for veiculo in veiculos:
        veiculo.registrar()
        if isinstance(veiculo, Automovel):
            print(veiculo.info_bateria())
            print()
        elif isinstance(veiculo, Moto):
            print(veiculo.info_cilindrada())
            print()

        elif isinstance(veiculo, Caminhao):
            print(veiculo.info_capacidade_carga())
            print()

if __name__ == "__main__":
    main()